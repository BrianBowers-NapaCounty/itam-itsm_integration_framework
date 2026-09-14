"""ServiceNow Table API connector.

ADAPTER-SKELETON:
- Implements real REST mechanics for the Table API.
- Local field names/table choices remain configurable.
- OAuth/Bearer is preferred; Basic auth is included for controlled examples.
"""

from __future__ import annotations
from datetime import datetime, timezone
from typing import Any
import requests

from ..core.connector import ITSMConnector
from ..core.http import request_with_retry
from ..core.models import Ticket, Asset, HealthCheck, OperationResult, parse_datetime


def _value(v):
    if isinstance(v, dict):
        return v.get("display_value") or v.get("value") or ""
    return v if v is not None else ""


class ServiceNowConnector(ITSMConnector):
    platform_name = "ServiceNow"
    capabilities = frozenset({"tickets.read","assets.read","tickets.update","tickets.note"})

    def __init__(self, *, base_url, incident_table="incident", asset_table="alm_hardware",
                 bearer_token=None, username=None, password=None, page_size=500):
        self.base_url = base_url.rstrip("/")
        self.incident_table = incident_table
        self.asset_table = asset_table
        self.page_size = int(page_size)
        self.session = requests.Session()
        self.session.headers.update({"Accept":"application/json","Content-Type":"application/json"})
        if bearer_token:
            self.session.headers["Authorization"] = f"Bearer {bearer_token}"
        elif username:
            self.session.auth = (username, password or "")

    def _table(self, table):
        return f"{self.base_url}/api/now/table/{table}"

    def _get(self, url, **kwargs):
        return request_with_retry(self.session, "GET", url, **kwargs).json()

    def _patch(self, url, json):
        return request_with_retry(self.session, "PATCH", url, json=json).json()

    def health_check(self):
        import time
        started = time.perf_counter()
        try:
            payload = self._get(self._table(self.incident_table), params={"sysparm_limit":1,"sysparm_fields":"sys_id"})
            ok = isinstance(payload.get("result"), list)
            return HealthCheck(self.platform_name, ok, "Table API reachable", (time.perf_counter()-started)*1000)
        except Exception as exc:
            return HealthCheck(self.platform_name, False, f"{type(exc).__name__}: {exc}")

    def _normalize_ticket(self, r):
        return Ticket(
            id=str(_value(r.get("sys_id"))), number=str(_value(r.get("number"))),
            short_description=str(_value(r.get("short_description"))),
            status=str(_value(r.get("state"))), priority=str(_value(r.get("priority"))),
            assignment_group=str(_value(r.get("assignment_group"))),
            assignee=str(_value(r.get("assigned_to"))),
            location_id=str(_value(r.get("location"))),
            asset_id=str(_value(r.get("cmdb_ci")) or _value(r.get("asset"))),
            opened_at=parse_datetime(_value(r.get("opened_at"))),
            updated_at=parse_datetime(_value(r.get("sys_updated_on"))),
            due_at=parse_datetime(_value(r.get("due_date"))),
            hold_reason=str(_value(r.get("hold_reason"))),
            source=self.platform_name, raw=r,
        )

    def _normalize_asset(self, r):
        return Asset(
            id=str(_value(r.get("sys_id"))), asset_tag=str(_value(r.get("asset_tag"))),
            serial_number=str(_value(r.get("serial_number"))), name=str(_value(r.get("display_name")) or _value(r.get("name"))),
            status=str(_value(r.get("install_status")) or _value(r.get("substatus"))),
            assigned_to=str(_value(r.get("assigned_to"))), location_id=str(_value(r.get("location"))),
            model=str(_value(r.get("model"))), department=str(_value(r.get("department"))),
            updated_at=parse_datetime(_value(r.get("sys_updated_on"))),
            source=self.platform_name, raw=r,
        )

    def get_ticket(self, record_id):
        payload = self._get(f"{self._table(self.incident_table)}/{record_id}", params={"sysparm_display_value":"all"})
        return self._normalize_ticket(payload["result"])

    def _iter_table(self, table, *, updated_since=None, limit=None, raw_filter=None):
        offset = 0
        remaining = limit
        while True:
            take = min(self.page_size, remaining) if remaining else self.page_size
            params = {
                "sysparm_limit": take,
                "sysparm_offset": offset,
                "sysparm_display_value": "all",
                "sysparm_exclude_reference_link": "true",
            }
            clauses = []
            if updated_since:
                utc = updated_since.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
                clauses.append(f"sys_updated_on>={utc}")
            if raw_filter:
                clauses.append(str(raw_filter))
            if clauses:
                params["sysparm_query"] = "^".join(clauses)
            rows = self._get(self._table(table), params=params).get("result", [])
            if not rows:
                break
            yield from rows
            offset += len(rows)
            if remaining:
                remaining -= len(rows)
                if remaining <= 0:
                    break
            if len(rows) < take:
                break

    def iter_tickets(self, *, updated_since=None, limit=None, raw_filter=None):
        for r in self._iter_table(self.incident_table, updated_since=updated_since, limit=limit, raw_filter=raw_filter):
            yield self._normalize_ticket(r)

    def get_asset(self, record_id):
        payload = self._get(f"{self._table(self.asset_table)}/{record_id}", params={"sysparm_display_value":"all"})
        return self._normalize_asset(payload["result"])

    def iter_assets(self, *, updated_since=None, limit=None, raw_filter=None):
        for r in self._iter_table(self.asset_table, updated_since=updated_since, limit=limit, raw_filter=raw_filter):
            yield self._normalize_asset(r)

    def update_ticket(self, record_id, fields):
        result = self._patch(f"{self._table(self.incident_table)}/{record_id}", json=dict(fields))
        return OperationResult("update_ticket", True, "ServiceNow record patched", records_written=1, details={"result":result.get("result",{})})

    def add_work_note(self, record_id, note):
        return self.update_ticket(record_id, {"work_notes":note})
