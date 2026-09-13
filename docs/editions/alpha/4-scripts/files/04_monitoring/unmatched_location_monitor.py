"""Measure weak/missing location references against a known-location text file."""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap
from capybara.services.monitoring import unmatched_location_rate

args,cfg,connector,log = bootstrap(__doc__)
known_file = cfg.source.parent/"sample_data"/"known_locations.txt"
known = {x.strip() for x in known_file.read_text(encoding="utf-8").splitlines() if x.strip()}
tickets = list(connector.iter_tickets(limit=args.limit))
rate = unmatched_location_rate(tickets,known)
threshold = float(cfg.get("thresholds.max_unmatched_location_rate",0.05))
print(f"unmatched rate: {rate:.1%}")
if rate > threshold:
    print(f"WARNING: above configured tolerance {threshold:.1%}")
