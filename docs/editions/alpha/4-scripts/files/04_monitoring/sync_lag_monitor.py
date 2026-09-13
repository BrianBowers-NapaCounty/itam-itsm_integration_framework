"""Measure age of the newest visible ITSM update as a simple polling/sync-lag signal."""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap
from capybara.services.monitoring import sync_lag_minutes

args,cfg,connector,log = bootstrap(__doc__)
tickets = list(connector.iter_tickets(limit=args.limit or 250))
lag = sync_lag_minutes(tickets)
threshold = float(cfg.get("thresholds.max_sync_lag_minutes",30))
print("lag_minutes =",lag)
if lag is not None and lag > threshold:
    raise SystemExit(f"WARNING: lag {lag:.1f} exceeds threshold {threshold:.1f}")
