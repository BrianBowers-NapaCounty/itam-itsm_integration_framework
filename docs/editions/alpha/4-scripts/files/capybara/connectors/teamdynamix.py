"""TeamDynamix Web API connector.

ADAPTER-SKELETON:
The Web API uses JSON and Bearer JWT authentication. Ticket retrieval and patch
endpoints are implemented; search-body and local custom-attribute mappings are
deliberately left configurable because TDX applications differ.
"""

from __future__ import annotations
from typing import Any
import requests

from ..core.connector import ITSMConnector
from ..core.http import request_with_retry
from ..core.models import Ticket, Asset, HealthCheck, OperationResult, parse_datetime


class TeamDynamixConnector(ITSMConnector):
    platform_name = "TeamDynamix"
    capabilities = frozenset({"tickets.read","tickets.update","tickets.note","assets.read"})

    def __init__(self, *, base_url, app_id, token):
        self.base_url = base_url.rstrip("/")
        self.app_id = int(app_id)
        self.session = requests.Session()
        self.session.headers.update({
            "Accept":"application/json",
            "Content-Type":"application/json",
            "Authorization":f"Bearer {token}",
        })

    def _url(self, tail):
        return f"{self.base_url}/api/{self.app_id}/{tail.lstrip('/')}"

    def _request(self, method, tail, **kwargs):
        return request_with_retry(self.session, method, self._url(tail), **kwargs)

    def health_check(self):
        import time
        t0 = time.perf_counter()
        try:
            r = self._request("GET", "tickets/statuses")
            return HealthCheck(self.platform_name, r.ok, "Ticket API reachable", (time.perf_counter()-t0)*1000)
        except Exception as exc:
            return HealthCheck(self.platform_name, False, f"{type(exc).__name__}: {exc}")

    def _ticket(self, r):
        return Ticket(
            id=str(r.get("ID","")), number=str(r.get("ID","")),
            short_description=str(r.get("Title","")), status=str(r.get("StatusName") or r.get("StatusID","")),
            priority=str(r.get("PriorityName") or r.get("PriorityID","")),
            assignment_group=str(r.get("ResponsibleGroupName","")),
            assignee=str(r.get("ResponsibleFullName","")),
            location_id=str(r.get("LocationID") or r.get("LocationName","")),
            asset_id=str(r.get("AssetID","")),
            opened_at=parse_datetime(r.get("CreatedDate")),
            updated_at=parse_datetime(r.get("ModifiedDate")),
            due_at=parse_datetime(r.get("EndDate")),
            hold_reason=str(r.get("StatusName","")) if "hold" in str(r.get("StatusName","")).lower() else "",
            source=self.platform_name, raw=r,
        )

    def get_ticket(self, record_id):
        return self._ticket(self._request("GET", f"tickets/{record_id}").json())

    def iter_tickets(self, *, updated_since=None, limit=None, raw_filter=None):
        # TDX's ticket-search request body is environment/application specific.
        # Pass a dict through raw_filter to add local search fields.
        body: dict[str, Any] = dict(raw_filter or {}) if isinstance(raw_filter, dict) else {}
        if limit:
            body.setdefault("MaxResults", int(limit))
        rows = self._request("POST", "tickets/search", json=body).json()
        for r in rows[:limit] if limit else rows:
            ticket = self._ticket(r)
            if not updated_since or (ticket.updated_at and ticket.updated_at >= updated_since):
                yield ticket

    def get_asset(self, record_id):
        r = self._request("GET", f"cmdb/{record_id}").json()
        return Asset(
            id=str(r.get("ID","")), asset_tag=str(r.get("Tag","") or r.get("SerialNumber","")),
            serial_number=str(r.get("SerialNumber","")), name=str(r.get("Name","")),
            status=str(r.get("StatusName","")), assigned_to=str(r.get("OwnerFullName","")),
            location_id=str(r.get("LocationID") or r.get("LocationName","")),
            model=str(r.get("ModelName","")), department=str(r.get("AccountName","")),
            updated_at=parse_datetime(r.get("ModifiedDate")), source=self.platform_name, raw=r,
        )

    def iter_assets(self, *, updated_since=None, limit=None, raw_filter=None):
        # CMDB search payloads vary; this demonstrates the adapter seam.
        body = dict(raw_filter or {}) if isinstance(raw_filter, dict) else {}
        if limit:
            body.setdefault("MaxResults", int(limit))
        rows = self._request("POST", "cmdb/search", json=body).json()
        for r in rows[:limit] if limit else rows:
            yield self.get_asset(r.get("ID"))

    def update_ticket(self, record_id, fields):
        # JSON Patch is supported by current TDX ticket endpoints.
        patch = [{"op":"replace","path":f"/{k}","value":v} for k,v in fields.items()]
        self._request("PATCH", f"tickets/{record_id}", json=patch)
        return OperationResult("update_ticket", True, "TeamDynamix ticket patched", records_written=1)

    def add_work_note(self, record_id, note):
        # TDX exposes ticket feed/comment operations. Local visibility settings
        # can be added to this payload as needed.
        self._request("POST", f"tickets/{record_id}/feed", json={"Comments":note})
        return OperationResult("add_work_note", True, "TeamDynamix feed entry added", records_written=1)
