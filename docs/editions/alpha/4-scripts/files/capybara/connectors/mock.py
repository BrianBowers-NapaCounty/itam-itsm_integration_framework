"""Demo connector backed by local JSON files."""

from __future__ import annotations
from datetime import datetime
import json
from pathlib import Path
from typing import Iterable, Any, Mapping

from ..core.connector import ITSMConnector
from ..core.models import Ticket, Asset, HealthCheck, OperationResult, parse_datetime


class MockConnector(ITSMConnector):
    platform_name = "Mock ITSM"
    capabilities = frozenset({"tickets.read","assets.read","tickets.update","tickets.note"})

    def __init__(self, sample_dir: str | Path):
        self.sample_dir = Path(sample_dir)
        self._tickets = self._load("tickets.json")
        self._assets = self._load("assets.json")
        self.writes: list[dict] = []

    def _load(self, name):
        return json.loads((self.sample_dir / name).read_text(encoding="utf-8"))

    def _ticket(self, r):
        return Ticket(
            id=str(r["id"]), number=str(r.get("number",r["id"])),
            short_description=r.get("short_description",""), status=r.get("status",""),
            priority=str(r.get("priority","")), assignment_group=r.get("assignment_group",""),
            assignee=r.get("assignee",""), location_id=str(r.get("location_id","")),
            asset_id=str(r.get("asset_id","")), opened_at=parse_datetime(r.get("opened_at")),
            updated_at=parse_datetime(r.get("updated_at")), due_at=parse_datetime(r.get("due_at")),
            hold_reason=r.get("hold_reason",""), source=self.platform_name, raw=dict(r)
        )

    def _asset(self, r):
        return Asset(
            id=str(r["id"]), asset_tag=r.get("asset_tag",""), serial_number=r.get("serial_number",""),
            name=r.get("name",""), status=r.get("status",""), assigned_to=r.get("assigned_to",""),
            location_id=str(r.get("location_id","")), model=r.get("model",""),
            department=r.get("department",""), updated_at=parse_datetime(r.get("updated_at")),
            source=self.platform_name, raw=dict(r)
        )

    def health_check(self):
        return HealthCheck(self.platform_name, True, f"Loaded {len(self._tickets)} tickets and {len(self._assets)} assets")

    def get_ticket(self, record_id):
        for r in self._tickets:
            if str(r["id"]) == str(record_id) or str(r.get("number")) == str(record_id):
                return self._ticket(r)
        raise KeyError(record_id)

    def iter_tickets(self, *, updated_since=None, limit=None, raw_filter=None):
        rows = [self._ticket(r) for r in self._tickets]
        if updated_since:
            rows = [x for x in rows if x.updated_at and x.updated_at >= updated_since]
        if callable(raw_filter):
            rows = [x for x in rows if raw_filter(x)]
        yield from rows[:limit] if limit else rows

    def get_asset(self, record_id):
        for r in self._assets:
            if str(r["id"]) == str(record_id) or str(r.get("asset_tag")) == str(record_id):
                return self._asset(r)
        raise KeyError(record_id)

    def iter_assets(self, *, updated_since=None, limit=None, raw_filter=None):
        rows = [self._asset(r) for r in self._assets]
        if updated_since:
            rows = [x for x in rows if x.updated_at and x.updated_at >= updated_since]
        if callable(raw_filter):
            rows = [x for x in rows if raw_filter(x)]
        yield from rows[:limit] if limit else rows

    def update_ticket(self, record_id, fields: Mapping[str, Any]):
        self.writes.append({"op":"update_ticket","id":record_id,"fields":dict(fields)})
        return OperationResult("update_ticket", True, "Mock update recorded", records_written=1)

    def add_work_note(self, record_id, note):
        self.writes.append({"op":"add_work_note","id":record_id,"note":note})
        return OperationResult("add_work_note", True, "Mock note recorded", records_written=1)
