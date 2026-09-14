"""Measure ticket-location completeness against an approved location identifier list."""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap
from capybara.services.reporting import location_match_quality
from capybara.core.serialization import write_html_table

args,cfg,connector,log = bootstrap(__doc__)
known = {x.strip() for x in (cfg.source.parent/"sample_data"/"known_locations.txt").read_text().splitlines() if x.strip()}
rows = location_match_quality(list(connector.iter_tickets(limit=args.limit)),known)
print(write_html_table(cfg.output_dir/"location-match-quality.html","Location Match Quality",rows))
