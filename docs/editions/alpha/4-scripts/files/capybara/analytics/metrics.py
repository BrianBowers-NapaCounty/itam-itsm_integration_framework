"""Metric registry for current-state and period/window analytics."""

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timezone
from collections import Counter
from typing import Callable, Any

@dataclass(frozen=True)
class MetricDefinition:
    code: str
    label: str
    unit: str
    source: str
    fn: Callable[..., float]

REGISTRY: dict[str, MetricDefinition] = {}

def metric(code, label, unit="count", source="tickets"):
    def deco(fn):
        REGISTRY[code] = MetricDefinition(code,label,unit,source,fn)
        return fn
    return deco

def _active(t):
    return str(t.status).strip().lower() not in {"closed","resolved","complete","completed","cancelled","canceled"}

@metric("tickets.total","Tickets","count")
def tickets_total(tickets, assets=None, **_):
    return float(len(tickets))

@metric("tickets.active","Active tickets","count")
def tickets_active(tickets, assets=None, **_):
    return float(sum(1 for t in tickets if _active(t)))

@metric("tickets.unassigned","Unassigned active tickets","count")
def tickets_unassigned(tickets, assets=None, **_):
    return float(sum(1 for t in tickets if _active(t) and not t.assignee))

@metric("tickets.on_hold","Tickets on hold","count")
def tickets_on_hold(tickets, assets=None, **_):
    markers=("hold","parts","equipment","procure","order","vendor","awaiting")
    return float(sum(1 for t in tickets if any(m in f"{t.status} {t.hold_reason}".lower() for m in markers)))

@metric("tickets.location_known_rate","Ticket known-location rate","ratio")
def known_location_rate(tickets, assets=None, known_locations=None, **_):
    if not tickets: return 1.0
    known=set(known_locations or [])
    return sum(1 for t in tickets if t.location_id and (not known or t.location_id in known))/len(tickets)

@metric("assets.total","Assets","count",source="assets")
def assets_total(tickets=None, assets=None, **_):
    return float(len(assets or []))

@metric("assets.missing","Missing/lost/stolen assets","count",source="assets")
def assets_missing(tickets=None, assets=None, **_):
    markers=("missing","lost","stolen","unable to locate","not found")
    return float(sum(1 for a in (assets or []) if any(m in str(a.status).lower() for m in markers)))

@metric("assets.spare","Spare assets","count",source="assets")
def assets_spare(tickets=None, assets=None, **_):
    return float(sum(1 for a in (assets or []) if "spare" in str(a.status).lower()))

def compute(metric_codes, *, tickets, assets, known_locations=None):
    rows=[]
    for code in metric_codes:
        d=REGISTRY[code]
        value=d.fn(tickets=tickets,assets=assets,known_locations=known_locations)
        rows.append({"metric_code":code,"metric_label":d.label,"metric_value":value,"unit":d.unit})
    return rows

def all_metrics(**kwargs):
    return compute(list(REGISTRY),**kwargs)
