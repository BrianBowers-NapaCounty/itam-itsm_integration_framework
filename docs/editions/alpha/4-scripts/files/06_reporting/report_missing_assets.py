"""Create a management-friendly missing/lost/stolen asset inventory."""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap
from capybara.services.notifications import missing_assets
from capybara.core.serialization import write_csv, write_html_table

args,cfg,connector,log = bootstrap(__doc__)
assets = missing_assets(list(connector.iter_assets(limit=args.limit)))
rows = [{"asset_tag":a.asset_tag,"name":a.name,"status":a.status,"assigned_to":a.assigned_to,
         "location_id":a.location_id,"department":a.department,"serial_number":a.serial_number} for a in assets]
write_csv(cfg.output_dir/"missing-assets.csv",rows)
print(write_html_table(cfg.output_dir/"missing-assets.html","Missing / Lost / Stolen Assets",rows))
