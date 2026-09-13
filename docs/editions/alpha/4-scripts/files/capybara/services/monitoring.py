"""Reusable health and quality metrics."""

from __future__ import annotations
from datetime import datetime, timezone


def sync_lag_minutes(tickets):
    stamps = [t.updated_at for t in tickets if t.updated_at]
    if not stamps:
        return None
    newest = max(stamps)
    return max(0.0, (datetime.now(timezone.utc) - newest.astimezone(timezone.utc)).total_seconds()/60.0)


def unmatched_location_rate(tickets, known_location_ids):
    rows = list(tickets)
    if not rows:
        return 0.0
    unmatched = sum(1 for t in rows if not t.location_id or t.location_id not in known_location_ids)
    return unmatched / len(rows)


def summarize_health(*checks):
    return {
        "ok": all(c.ok for c in checks),
        "components": [
            {"component":c.component,"ok":c.ok,"message":c.message,"latency_ms":c.latency_ms}
            for c in checks
        ],
    }
