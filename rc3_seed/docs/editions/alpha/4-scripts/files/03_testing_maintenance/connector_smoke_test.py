"""Exercise connector health/read paths without performing writes."""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap

args,cfg,c,log = bootstrap(__doc__)
print(c.health_check())
ticket = next(iter(c.iter_tickets(limit=1)),None)
asset = next(iter(c.iter_assets(limit=1)),None)
print("Ticket:",ticket)
print("Asset:",asset)
