"""Canonical data models shared by every ITSM connector and workflow."""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any


class MatchStatus(str, Enum):
    MATCHED = "Matched"
    NEEDS_REVIEW = "Needs Review"
    AMBIGUOUS = "Ambiguous"
    NOT_FOUND = "Not Found"
    RETIRED = "Retired"
    SUPPRESSED = "Suppressed"


@dataclass(slots=True)
class LocationRef:
    source_id: str = ""
    name: str = ""
    facility_id: str = ""
    level_id: str = ""
    unit_id: str = ""
    match_status: MatchStatus = MatchStatus.NOT_FOUND
    confidence: float = 0.0
    notes: str = ""


@dataclass(slots=True)
class Ticket:
    id: str
    number: str
    short_description: str = ""
    status: str = ""
    priority: str = ""
    assignment_group: str = ""
    assignee: str = ""
    location_id: str = ""
    asset_id: str = ""
    opened_at: datetime | None = None
    updated_at: datetime | None = None
    due_at: datetime | None = None
    hold_reason: str = ""
    source: str = ""
    raw: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class Asset:
    id: str
    asset_tag: str = ""
    serial_number: str = ""
    name: str = ""
    status: str = ""
    assigned_to: str = ""
    location_id: str = ""
    model: str = ""
    department: str = ""
    updated_at: datetime | None = None
    source: str = ""
    raw: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class HealthCheck:
    component: str
    ok: bool
    message: str
    latency_ms: float | None = None
    details: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class ReconciliationIssue:
    record_type: str
    record_id: str
    issue: str
    severity: str = "warning"
    safe_to_repair: bool = False
    source_value: Any = None
    target_value: Any = None


@dataclass(slots=True)
class OperationResult:
    operation: str
    ok: bool
    message: str = ""
    correlation_id: str = ""
    records_read: int = 0
    records_written: int = 0
    warnings: list[str] = field(default_factory=list)
    details: dict[str, Any] = field(default_factory=dict)


def parse_datetime(value: Any) -> datetime | None:
    """Best-effort ISO-ish parser used by connectors.

    Vendor connectors may override this when a platform has special date
    semantics. Naive datetimes are interpreted as UTC for demonstration use.
    """
    if not value:
        return None
    if isinstance(value, datetime):
        return value if value.tzinfo else value.replace(tzinfo=timezone.utc)
    text = str(value).strip().replace("Z", "+00:00")
    for candidate in (text, text.replace(" ", "T")):
        try:
            dt = datetime.fromisoformat(candidate)
            return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
        except ValueError:
            pass
    return None
