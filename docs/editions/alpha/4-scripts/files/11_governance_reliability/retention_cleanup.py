from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))
from _common import bootstrap

"""Preview retention cutoffs; destructive deletion requires explicit local implementation approval."""

from datetime import datetime,timedelta,timezone
args,cfg,connector,log=bootstrap(__doc__)
now=datetime.now(timezone.utc)
for key in ("retention_days_event_history","retention_days_sync_health","retention_days_runs"):
    days=int(cfg.get(f"analytics.{key}",365))
    cutoff=now-timedelta(days=days)
    print(f"{key}: retain {days} days -> cutoff {cutoff.isoformat()}")
print("No records were deleted. Use HostedAnalyticsStore.delete_where() only with an explicit reviewed WHERE clause.")
