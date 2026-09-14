from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))
from _common import bootstrap

"""Detect missing daily-capture dates in an exported/local Analytics_Runs history."""

from datetime import datetime,timedelta,timezone
from capybara.analytics.store import build_store,HostedAnalyticsStore
args,cfg,connector,log=bootstrap(__doc__)
store=build_store(cfg)
if isinstance(store,HostedAnalyticsStore):
    fs=store.query("Analytics_Runs",where="RUN_TYPE='daily_capture' AND STATUS='Completed'",
                   out_fields="STARTED_UTC",order_by_fields="STARTED_UTC ASC")
    stamps=[f.attributes.get("STARTED_UTC") for f in fs.features]
else:
    stamps=[r["STARTED_UTC"] for r in store.query_rows("Analytics_Runs","RUN_TYPE='daily_capture' AND STATUS='Completed'")]
print("Completed daily captures:",len(stamps))
print("Production enhancement: normalize stamps to local date and enumerate gaps across the expected operating calendar.")
