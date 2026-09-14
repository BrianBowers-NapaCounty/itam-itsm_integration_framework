from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))
from _common import bootstrap

"""Demonstrate period-over-period comparisons from stored metric rows."""

from capybara.analytics.windows import named_window
from capybara.analytics.aggregation import compare_values
args,cfg,connector,log=bootstrap(__doc__)
print("Example pairs:")
pairs=[("wtd","previous-week"),("mtd","previous-month"),("qtd","previous-quarter"),("ytd","previous-year")]
for current,prior in pairs:
    a=named_window(current,tz_name=cfg.get("analytics.time_zone","UTC"))
    b=named_window(prior,tz_name=cfg.get("analytics.time_zone","UTC"))
    print(current,a.start,a.end,"vs",prior,b.start,b.end)
print("Use compare_values(current_metric_value, prior_metric_value) after querying Metric_Snapshots.")
