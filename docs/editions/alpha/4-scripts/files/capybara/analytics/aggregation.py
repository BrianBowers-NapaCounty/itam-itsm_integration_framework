"""Daily facts, period summaries, comparisons, data quality, and simple anomaly detection."""

from __future__ import annotations
from collections import Counter, defaultdict
from datetime import datetime, timezone
from statistics import median
import math

from .metrics import REGISTRY

def _active(t):
    return str(t.status).strip().lower() not in {"closed","resolved","complete","completed","cancelled","canceled"}

def ticket_daily_rows(tickets, *, day, run_id=""):
    groups=defaultdict(list)
    for t in tickets:
        key=(t.location_id or "", t.assignment_group or "")
        groups[key].append(t)
    out=[]
    now=datetime.now(timezone.utc)
    for (location,group), rows in groups.items():
        ages=[]
        for t in rows:
            stamp=t.opened_at
            if stamp:
                ages.append((now-stamp.astimezone(timezone.utc)).total_seconds()/3600)
        out.append({
            "DAY":day,"FACILITY_ID":"","LEVEL_ID":"","LOCATION_ID":location,
            "ASSIGN_GROUP":group,"CATEGORY":"",
            "OPENED":sum(1 for t in rows if t.opened_at and t.opened_at.date()==day.date()),
            "CLOSED":sum(1 for t in rows if not _active(t)),
            "ACTIVE":sum(1 for t in rows if _active(t)),
            "ON_HOLD":sum(1 for t in rows if "hold" in f"{t.status} {t.hold_reason}".lower() or "await" in f"{t.status} {t.hold_reason}".lower()),
            "UNASSIGNED":sum(1 for t in rows if _active(t) and not t.assignee),
            "SLA_BREACHED":sum(1 for t in rows if t.due_at and _active(t) and t.due_at.astimezone(timezone.utc)<now),
            "AVG_AGE_HOURS":sum(ages)/len(ages) if ages else 0.0,
            "RUN_ID":run_id,
        })
    return out

def asset_daily_rows(assets, *, day, run_id=""):
    groups=defaultdict(list)
    for a in assets:
        groups[(a.location_id or "", a.department or "", a.status or "")].append(a)
    out=[]
    for (location,dept,status), rows in groups.items():
        out.append({
            "DAY":day,"FACILITY_ID":"","LOCATION_ID":location,"DEPARTMENT":dept,
            "ASSET_STATUS":status,"ASSET_COUNT":len(rows),
            "MISSING_COUNT":sum(1 for a in rows if any(x in str(a.status).lower() for x in ("missing","lost","stolen"))),
            "SPARE_COUNT":sum(1 for a in rows if "spare" in str(a.status).lower()),
            "ASSIGNED_COUNT":sum(1 for a in rows if bool(a.assigned_to)),
            "UNASSIGNED_COUNT":sum(1 for a in rows if not a.assigned_to),
            "RUN_ID":run_id,
        })
    return out

def data_quality_row(tickets, *, known_locations=None, run_id="", observed=None):
    observed=observed or datetime.now(timezone.utc)
    n=max(1,len(tickets))
    known=set(known_locations or [])
    loc=sum(1 for t in tickets if bool(t.location_id))/n
    assignee=sum(1 for t in tickets if bool(t.assignee))/n
    asset=sum(1 for t in tickets if bool(t.asset_id))/n
    known_rate=sum(1 for t in tickets if t.location_id and (not known or t.location_id in known))/n
    ids=[t.id for t in tickets if t.id]
    dup=(len(ids)-len(set(ids)))/max(1,len(ids))
    # Weighted example score; organizations should tune weights explicitly.
    score=(0.35*loc + 0.20*assignee + 0.20*asset + 0.25*known_rate) * (1-dup)
    return {
        "OBSERVED_UTC":observed,"SCORE":score,
        "LOCATION_COMPLETENESS":loc,"ASSIGNEE_COMPLETENESS":assignee,
        "ASSET_LINK_RATE":asset,"KNOWN_LOCATION_RATE":known_rate,
        "DUPLICATE_RATE":dup,"NOTES":"Reference weighted score; tune locally.","RUN_ID":run_id,
    }

def compare_values(current, prior):
    cur=float(current or 0); prv=float(prior or 0)
    diff=cur-prv
    pct=None if prv==0 else diff/prv
    return {"current":cur,"prior":prv,"change_abs":diff,"change_pct":pct}

def robust_anomalies(points, *, z=3.5):
    """Median absolute deviation anomaly detector.

    `points` is iterable of (timestamp, numeric_value).
    """
    pts=list(points)
    vals=[float(v) for _,v in pts if v is not None]
    if len(vals)<5:
        return []
    med=median(vals)
    deviations=[abs(v-med) for v in vals]
    mad=median(deviations)
    if mad==0:
        return []
    out=[]
    for ts,v in pts:
        if v is None: continue
        score=0.6745*(float(v)-med)/mad
        if abs(score)>=z:
            out.append({"timestamp":ts,"value":float(v),"robust_z":score,"median":med,"mad":mad})
    return out
