"""Canonical report builders."""

from __future__ import annotations
from collections import Counter, defaultdict
from dataclasses import asdict


def assignment_backlog(tickets):
    counts = Counter((t.assignment_group or "(Unassigned group)") for t in tickets
                     if str(t.status).lower() not in {"closed","resolved","complete","completed"})
    return [{"assignment_group":k,"open_tickets":v} for k,v in counts.most_common()]


def tickets_on_hold(tickets):
    markers = ("hold","parts","equipment","procure","order","vendor","awaiting")
    rows = []
    for t in tickets:
        text = f"{t.status} {t.hold_reason}".lower()
        if any(m in text for m in markers):
            rows.append({
                "number":t.number,"description":t.short_description,"status":t.status,
                "hold_reason":t.hold_reason,"assignment_group":t.assignment_group,
                "assignee":t.assignee,"location_id":t.location_id,
                "updated_at":t.updated_at,
            })
    return rows


def location_match_quality(tickets, known_locations):
    total = 0; matched = 0; no_location = 0; unknown = 0
    for t in tickets:
        total += 1
        if not t.location_id:
            no_location += 1
        elif t.location_id in known_locations:
            matched += 1
        else:
            unknown += 1
    rate = matched/total if total else 1.0
    return [{"total":total,"matched":matched,"missing_location":no_location,
             "unknown_location":unknown,"match_rate":round(rate,4)}]


def service_hotspots(tickets):
    c = Counter(t.location_id or "(No location)" for t in tickets)
    return [{"location_id":k,"ticket_count":v} for k,v in c.most_common()]


def asset_service_history(tickets, assets):
    by_asset = defaultdict(list)
    for t in tickets:
        if t.asset_id:
            by_asset[t.asset_id].append(t)
    rows = []
    for a in assets:
        work = by_asset.get(a.id,[])
        rows.append({
            "asset_tag":a.asset_tag,"asset_name":a.name,"status":a.status,
            "location_id":a.location_id,"ticket_count":len(work),
            "latest_ticket":max((t.updated_at for t in work if t.updated_at), default=None),
        })
    return sorted(rows,key=lambda r:r["ticket_count"],reverse=True)


def executive_summary(tickets, assets):
    active = [t for t in tickets if str(t.status).lower() not in {"closed","resolved","complete","completed"}]
    missing = [a for a in assets if any(x in str(a.status).lower() for x in ("missing","lost","stolen"))]
    return [{
        "tickets_total":len(tickets),
        "tickets_active":len(active),
        "assets_total":len(assets),
        "assets_missing":len(missing),
        "unassigned_active":sum(1 for t in active if not t.assignee),
        "locations_with_demand":len({t.location_id for t in active if t.location_id}),
    }]
