"""Demonstrate writing a map/place reference back to the ITSM ticket."""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap

args,cfg,connector,log = bootstrap(__doc__)
ticket = next(iter(connector.iter_tickets(limit=1)))
map_url = cfg.get("writeback.example_map_url","https://example.invalid/indoors?unit=DEMO")
note = f"Capybara spatial context: {map_url}"

if cfg.dry_run:
    print("DRY RUN",ticket.number,note)
else:
    print(connector.add_work_note(ticket.id,note))
