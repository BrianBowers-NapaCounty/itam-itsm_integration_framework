"""A minimal polling-loop example suitable for Task Scheduler wrapper usage.

Production deployments should normally let an external scheduler invoke a
single iteration rather than keeping an endless notebook/kernel process alive.
"""

from datetime import datetime, timedelta, timezone
from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap

args,cfg,connector,log = bootstrap(__doc__)
minutes = int(cfg.get("sync.lookback_minutes",15))
since = datetime.now(timezone.utc)-timedelta(minutes=minutes)
rows = list(connector.iter_tickets(updated_since=since,limit=args.limit))
print(f"{len(rows)} tickets updated in the last {minutes} minutes")
for t in rows:
    print(t.number,t.status,t.updated_at)
