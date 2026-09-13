from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))
from _common import bootstrap

"""Document duplicate-snapshot detection keys without automatically deleting records."""

args,cfg,connector,log=bootstrap(__doc__)
print("""
Recommended uniqueness keys:
Metric_Snapshots: OBSERVED_UTC + METRIC_CODE + DIMENSION + DIM_VALUE + RUN_ID
Ticket_Daily:     DAY + LOCATION_ID + ASSIGN_GROUP + CATEGORY + RUN_ID
Asset_Daily:      DAY + LOCATION_ID + DEPARTMENT + ASSET_STATUS + RUN_ID
Sync_Health:      OBSERVED_UTC + RUN_ID

Detect duplicates first; retain the newest reviewed row or re-run cleanly.
Automatic destructive deduplication is intentionally omitted.
""")
