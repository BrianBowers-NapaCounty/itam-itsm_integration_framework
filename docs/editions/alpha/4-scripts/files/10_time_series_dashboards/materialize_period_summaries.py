from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))
from _common import bootstrap

"""Materialize standard period rows for dashboard selectors.

This reference implementation records window boundaries; production deployments
should query/aggregate Metric_Snapshots for each metric/dimension and fill values.
"""

from datetime import datetime,timezone
from capybara.analytics.windows import common_windows
from capybara.analytics.store import build_store
from capybara.analytics.service import run_id
args,cfg,connector,log=bootstrap(__doc__)
rid=run_id("periods"); now=datetime.now(timezone.utc)
rows=[]
for w in common_windows(tz_name=cfg.get("analytics.time_zone","UTC")):
    rows.append({"GENERATED_UTC":now,"PERIOD_CODE":w.code,"PERIOD_LABEL":w.label,
                 "PERIOD_START":w.start,"PERIOD_END":w.end,"DIMENSION":"all","DIM_VALUE":"all",
                 "METRIC_CODE":"window_definition","METRIC_VALUE":None,"PRIOR_VALUE":None,
                 "CHANGE_ABS":None,"CHANGE_PCT":None,"RUN_ID":rid})
print(build_store(cfg).add_rows("Period_Summaries",rows))
