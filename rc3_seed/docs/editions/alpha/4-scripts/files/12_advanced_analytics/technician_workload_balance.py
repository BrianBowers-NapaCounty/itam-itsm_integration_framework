from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))
from _common import bootstrap

"""Compare active assigned workload by technician and assignment group."""

from collections import Counter
args,cfg,connector,log=bootstrap(__doc__)
tech=Counter();group=Counter()
for t in connector.iter_tickets(limit=args.limit):
    if str(t.status).lower() in {"closed","resolved","complete","completed"}: continue
    tech[t.assignee or "(Unassigned)"]+=1
    group[t.assignment_group or "(No group)"]+=1
print("Technician workload")
for k,v in tech.most_common(): print(k,v)
print("\nGroup workload")
for k,v in group.most_common(): print(k,v)
