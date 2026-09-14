"""Build one management digest instead of sending one message per exception."""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap
from capybara.services.notifications import missing_assets, stale_unassigned_tickets, parts_hold_tickets, ConsoleNotifier

args,cfg,connector,log = bootstrap(__doc__)
tickets = list(connector.iter_tickets(limit=args.limit))
assets = list(connector.iter_assets(limit=args.limit))
missing = missing_assets(assets)
unassigned = stale_unassigned_tickets(tickets,hours=int(cfg.get("thresholds.stale_unassigned_hours",8)))
holds = parts_hold_tickets(tickets,days=int(cfg.get("thresholds.parts_hold_days",5)))
text = (
    f"Missing assets: {len(missing)}\n"
    f"Stale unassigned tickets: {len(unassigned)}\n"
    f"Long parts/procurement holds: {len(holds)}\n"
)
ConsoleNotifier().send("Capybara daily management digest",text)
