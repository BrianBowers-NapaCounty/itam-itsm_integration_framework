from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))
from _common import bootstrap

"""Compute and persist a governance/data-quality score snapshot."""

from capybara.analytics.aggregation import data_quality_row
from capybara.analytics.store import build_store
from capybara.analytics.service import run_id
args,cfg,connector,log=bootstrap(__doc__)
tickets=list(connector.iter_tickets(limit=args.limit))
known_file=cfg.source.parent/"sample_data"/"known_locations.txt"
known={x.strip() for x in known_file.read_text().splitlines() if x.strip()} if known_file.exists() else set()
row=data_quality_row(tickets,known_locations=known,run_id=run_id("dq"))
print(row)
print(build_store(cfg).add_rows("Data_Quality_Snapshots",[row]))
