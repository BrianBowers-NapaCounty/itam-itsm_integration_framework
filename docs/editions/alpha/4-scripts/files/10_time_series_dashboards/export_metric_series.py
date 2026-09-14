from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))
from _common import bootstrap

"""Export a hosted/local metric time series for a chosen reporting window."""

import argparse,csv
from capybara.analytics.store import build_store,HostedAnalyticsStore
from capybara.analytics.windows import named_window
from capybara.analytics.series import metric_series_hosted,metric_series_sqlite

args,cfg,connector,log=bootstrap(__doc__)
metric=cfg.get("analytics.example_metric","tickets.active")
window=named_window(cfg.get("analytics.example_window","3-month"),tz_name=cfg.get("analytics.time_zone","UTC"))
store=build_store(cfg)
series=metric_series_hosted(store,metric,window) if isinstance(store,HostedAnalyticsStore) else metric_series_sqlite(store,metric,window)
path=cfg.output_dir/f"{metric.replace('.','_')}-{window.code}.csv"
with path.open("w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f);w.writerow(["timestamp","value"]);w.writerows(series)
print(path)
