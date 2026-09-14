"""Rank locations by service-ticket volume; useful precursor to spatial hotspot mapping."""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap
from capybara.services.reporting import service_hotspots
from capybara.core.serialization import write_csv, write_html_table

args,cfg,connector,log = bootstrap(__doc__)
rows = service_hotspots(list(connector.iter_tickets(limit=args.limit)))
write_csv(cfg.output_dir/"service-hotspots.csv",rows)
print(write_html_table(cfg.output_dir/"service-hotspots.html","Service Demand by Location",rows,
                       "Join location_id to Indoors Units/Facilities for cartographic presentation."))
