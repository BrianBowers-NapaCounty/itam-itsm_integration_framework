from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))
from _common import bootstrap

"""Capture current canonical ITSM/ITAM state into historical analytics tables."""

from capybara.analytics.store import build_store
from capybara.analytics.service import capture_daily

args,cfg,connector,log=bootstrap(__doc__)
tickets=list(connector.iter_tickets(limit=args.limit))
assets=list(connector.iter_assets(limit=args.limit))
known_file=cfg.source.parent/"sample_data"/"known_locations.txt"
known={x.strip() for x in known_file.read_text().splitlines() if x.strip()} if known_file.exists() else set()
store=build_store(cfg)
print(capture_daily(store,tickets,assets,known_locations=known))
