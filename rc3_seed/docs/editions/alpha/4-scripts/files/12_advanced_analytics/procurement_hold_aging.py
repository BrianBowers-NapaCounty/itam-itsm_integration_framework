from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))
from _common import bootstrap

"""Bucket parts/equipment/procurement holds by age for management review."""

from datetime import datetime,timezone
from collections import Counter
from capybara.services.notifications import parts_hold_tickets
args,cfg,connector,log=bootstrap(__doc__)
now=datetime.now(timezone.utc); buckets=Counter()
for t in parts_hold_tickets(list(connector.iter_tickets(limit=args.limit)),days=0):
    stamp=t.updated_at or t.opened_at
    days=(now-stamp.astimezone(timezone.utc)).days if stamp else 0
    band="0-2" if days<3 else "3-6" if days<7 else "7-13" if days<14 else "14-29" if days<30 else "30+"
    buckets[band]+=1
print(dict(buckets))
