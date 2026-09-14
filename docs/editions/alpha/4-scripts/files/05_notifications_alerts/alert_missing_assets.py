"""Email/preview an alert when assets are flagged missing, lost, or stolen."""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap
from capybara.services.notifications import missing_assets, ConsoleNotifier, SMTPNotifier

args,cfg,connector,log = bootstrap(__doc__)
rows = missing_assets(list(connector.iter_assets(limit=args.limit)))
if not rows:
    print("No missing assets.")
    raise SystemExit(0)

text = "\n".join(f"- {a.asset_tag}: {a.name} | {a.status} | location={a.location_id or 'UNKNOWN'}" for a in rows)
subject = f"Capybara alert: {len(rows)} asset(s) require missing-equipment review"
notifier = SMTPNotifier(cfg) if cfg.get("smtp.enabled",False) and not cfg.dry_run else ConsoleNotifier()
notifier.send(subject,text)
