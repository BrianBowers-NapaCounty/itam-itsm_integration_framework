from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))
from _common import bootstrap

"""Generate a PNG time-series chart from historical Metric_Snapshots."""

from datetime import datetime,timezone
import matplotlib.pyplot as plt
from capybara.analytics.store import build_store,HostedAnalyticsStore
from capybara.analytics.windows import named_window
from capybara.analytics.series import metric_series_hosted,metric_series_sqlite

args,cfg,connector,log=bootstrap(__doc__)
metric=cfg.get("analytics.example_metric","tickets.active")
window=named_window(cfg.get("analytics.example_window","3-month"),tz_name=cfg.get("analytics.time_zone","UTC"))
store=build_store(cfg)
rows=metric_series_hosted(store,metric,window) if isinstance(store,HostedAnalyticsStore) else metric_series_sqlite(store,metric,window)
xs=[];ys=[]
for ts,v in rows:
    if isinstance(ts,(int,float)): ts=datetime.fromtimestamp(ts/1000,timezone.utc)
    xs.append(ts);ys.append(v)
plt.figure(figsize=(10,4))
plt.plot(xs,ys,marker="o")
plt.title(f"{metric} — {window.label}")
plt.xlabel("Date");plt.ylabel("Value");plt.grid(True,alpha=.25);plt.tight_layout()
path=cfg.output_dir/f"{metric.replace('.','_')}-{window.code}.png"
plt.savefig(path,dpi=160);plt.close()
print(path)
