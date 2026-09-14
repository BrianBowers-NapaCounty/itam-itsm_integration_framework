"""Alert managers about tickets held for parts/equipment/procurement longer than threshold."""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap
from capybara.services.notifications import parts_hold_tickets, ConsoleNotifier, SMTPNotifier

args,cfg,connector,log = bootstrap(__doc__)
days = int(cfg.get("thresholds.parts_hold_days",5))
rows = parts_hold_tickets(list(connector.iter_tickets(limit=args.limit)),days=days)
if not rows:
    print("No prolonged parts/procurement holds.")
    raise SystemExit(0)

text = "\n".join(
    f"- {t.number}: {t.short_description} | {t.status} | {t.hold_reason or '(no reason supplied)'} | {t.location_id}"
    for t in rows
)
notifier = SMTPNotifier(cfg) if cfg.get("smtp.enabled",False) and not cfg.dry_run else ConsoleNotifier()
notifier.send(f"Capybara: {len(rows)} ticket(s) waiting on parts/equipment",text)
