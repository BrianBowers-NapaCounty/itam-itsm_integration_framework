"""Create a starter ITSM-location-to-Indoors-unit crosswalk for review."""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap
from capybara.core.serialization import write_csv

args,cfg,connector,log = bootstrap(__doc__)
tickets = list(connector.iter_tickets(limit=args.limit))
locs = sorted({t.location_id for t in tickets if t.location_id})
rows = [{"itsm_location_id":x,"arcgis_unit_id":"","match_status":"Needs Review",
         "confidence":0.0,"review_notes":""} for x in locs]
print(write_csv(cfg.output_dir/"location-crosswalk-starter.csv",rows))
