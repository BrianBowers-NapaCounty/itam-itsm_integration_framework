"""Hosted-table time-series extraction helpers."""

from __future__ import annotations
from datetime import datetime, timezone


def epoch_ms(dt):
    if dt.tzinfo is None: dt=dt.replace(tzinfo=timezone.utc)
    return int(dt.timestamp()*1000)

def metric_series_hosted(store, metric_code, window, *, dimension="all", dim_value="all"):
    safe_metric=str(metric_code).replace("'","''")
    safe_dim=str(dimension).replace("'","''")
    safe_val=str(dim_value).replace("'","''")
    where=(
        f"METRIC_CODE='{safe_metric}' AND DIMENSION='{safe_dim}' AND DIM_VALUE='{safe_val}' "
        f"AND OBSERVED_UTC >= DATE '{window.start.strftime('%Y-%m-%d %H:%M:%S')}' "
        f"AND OBSERVED_UTC < DATE '{window.end.strftime('%Y-%m-%d %H:%M:%S')}'"
    )
    fs=store.query("Metric_Snapshots",where=where,out_fields="OBSERVED_UTC,METRIC_VALUE",
                   order_by_fields="OBSERVED_UTC ASC")
    rows=[]
    for f in fs.features:
        a=f.attributes
        rows.append((a.get("OBSERVED_UTC"),a.get("METRIC_VALUE")))
    return rows

def metric_series_sqlite(store, metric_code, window, *, dimension="all", dim_value="all"):
    start=epoch_ms(window.start); end=epoch_ms(window.end)
    rows=store.query_rows("Metric_Snapshots",
        "METRIC_CODE=? AND DIMENSION=? AND DIM_VALUE=? AND OBSERVED_UTC>=? AND OBSERVED_UTC<?",
        (metric_code,dimension,dim_value,start,end))
    return [(r["OBSERVED_UTC"],r["METRIC_VALUE"]) for r in rows]
