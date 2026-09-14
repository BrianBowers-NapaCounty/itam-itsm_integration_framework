from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))
from _common import bootstrap

"""Example local metric plug-in registered without editing core analytics code."""

from capybara.analytics.metrics import metric,compute

@metric("local.high_priority","Local high-priority active tickets","count")
def high_priority(tickets,assets=None,**_):
    return float(sum(1 for t in tickets if str(t.priority) in {"1","2","Critical","High"} and
                     str(t.status).lower() not in {"closed","resolved"}))

args,cfg,connector,log=bootstrap(__doc__)
tickets=list(connector.iter_tickets(limit=args.limit))
assets=list(connector.iter_assets(limit=args.limit))
print(compute(["local.high_priority"],tickets=tickets,assets=assets))
