"""High-level analytics capture orchestration."""

from __future__ import annotations
from datetime import datetime, timezone
import uuid

from .metrics import all_metrics
from .aggregation import ticket_daily_rows, asset_daily_rows, data_quality_row


def run_id(prefix="analytics"):
    return f"{prefix}-{uuid.uuid4().hex[:12]}"

def run_manifest(run_id, run_type, *, status="Started", rows=0, message="", started=None, finished=None, correlation=""):
    return {
        "RUN_ID":run_id,"RUN_TYPE":run_type,
        "STARTED_UTC":started or datetime.now(timezone.utc),
        "FINISHED_UTC":finished,
        "STATUS":status,"ROWS_WRITTEN":rows,"MESSAGE":message,"CORRELATION":correlation,
    }

def current_metric_rows(tickets,assets,*,known_locations=None,period_code="snapshot",run_id="",observed=None):
    observed=observed or datetime.now(timezone.utc)
    rows=[]
    for m in all_metrics(tickets=tickets,assets=assets,known_locations=known_locations):
        rows.append({
            "OBSERVED_UTC":observed,"PERIOD_CODE":period_code,
            "PERIOD_START":observed,"PERIOD_END":observed,
            "METRIC_CODE":m["metric_code"],"METRIC_LABEL":m["metric_label"],
            "METRIC_VALUE":m["metric_value"],"UNIT":m["unit"],
            "DIMENSION":"all","DIM_VALUE":"all","SOURCE_COUNT":len(tickets)+len(assets),
            "RUN_ID":run_id,
        })
    return rows

def capture_daily(store,tickets,assets,*,known_locations=None,observed=None):
    observed=observed or datetime.now(timezone.utc)
    rid=run_id("daily")
    store.add_rows("Analytics_Runs",[run_manifest(rid,"daily_capture",started=observed)])
    written=0
    pieces=[
        ("Metric_Snapshots",current_metric_rows(tickets,assets,known_locations=known_locations,run_id=rid,observed=observed)),
        ("Ticket_Daily",ticket_daily_rows(tickets,day=observed,run_id=rid)),
        ("Asset_Daily",asset_daily_rows(assets,day=observed,run_id=rid)),
        ("Data_Quality_Snapshots",[data_quality_row(tickets,known_locations=known_locations,run_id=rid,observed=observed)]),
    ]
    for table,rows in pieces:
        store.add_rows(table,rows)
        written+=len(rows)
    store.add_rows("Analytics_Runs",[run_manifest(rid,"daily_capture",status="Completed",rows=written,
                                                   started=observed,finished=datetime.now(timezone.utc))])
    return {"run_id":rid,"rows_written":written}
