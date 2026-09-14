"""Escalate active tickets that remain unassigned beyond a configured interval."""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap
from capybara.services.notifications import stale_unassigned_tickets, ConsoleNotifier

args,cfg,connector,log = bootstrap(__doc__)
hours = int(cfg.get("thresholds.stale_unassigned_hours",8))
rows = stale_unassigned_tickets(list(connector.iter_tickets(limit=args.limit)),hours=hours)
text = "\n".join(f"- {t.number}: {t.short_description} | {t.status} | location={t.location_id}" for t in rows)
if rows:
    ConsoleNotifier().send(f"Capybara: {len(rows)} stale unassigned ticket(s)",text)
else:
    print("No stale unassigned tickets.")
