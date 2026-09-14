from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))
from _common import bootstrap

"""Rank locations by replacement/deployment workload to help stage refresh waves.

A real implementation can add device age, warranty, model, security posture,
department priority, floor adjacency, and technician capacity.
"""

from collections import Counter
args,cfg,connector,log=bootstrap(__doc__)
c=Counter()
for a in connector.iter_assets(limit=args.limit):
    text=f"{a.status} {a.model}".lower()
    if any(x in text for x in ("refresh","replace","retire","desktop","laptop")):
        c[a.location_id or "(No location)"]+=1
print("Candidate workload by location:")
for loc,n in c.most_common():
    print(loc,n)
