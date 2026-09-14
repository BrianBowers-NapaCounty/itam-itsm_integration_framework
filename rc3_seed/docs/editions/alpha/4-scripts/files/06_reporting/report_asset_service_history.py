"""Rank assets by associated ticket history."""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap
from capybara.services.reporting import asset_service_history
from capybara.core.serialization import write_html_table

args,cfg,connector,log = bootstrap(__doc__)
rows = asset_service_history(list(connector.iter_tickets(limit=args.limit)),
                             list(connector.iter_assets(limit=args.limit)))
print(write_html_table(cfg.output_dir/"asset-service-history.html","Asset Service History",rows))
