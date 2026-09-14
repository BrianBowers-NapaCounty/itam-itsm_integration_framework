from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))
from _common import bootstrap

"""Summarize current SLA-risk workload by location for later join to Indoors geometry."""

from datetime import datetime,timezone
from collections import Counter
args,cfg,connector,log=bootstrap(__doc__)
now=datetime.now(timezone.utc); risk=Counter()
for t in connector.iter_tickets(limit=args.limit):
    if t.due_at and t.due_at.astimezone(timezone.utc)<now and str(t.status).lower() not in {"closed","resolved"}:
        risk[t.location_id or "(No location)"]+=1
for location,count in risk.most_common():
    print(location,count)
