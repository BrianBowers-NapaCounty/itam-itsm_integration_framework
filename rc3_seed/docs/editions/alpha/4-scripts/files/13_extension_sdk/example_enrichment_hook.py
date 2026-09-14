from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))
from _common import bootstrap

"""Example extension hook that adds local context to a normalized payload."""

from capybara.extensions.hooks import register,emit

@register("enrich_ticket")
def add_local_support_zone(payload,**context):
    payload=dict(payload)
    loc=str(payload.get("location_id",""))
    payload["support_zone"]="North" if loc.startswith(("LIB","NEW")) else "Central"
    return payload

args,cfg,connector,log=bootstrap(__doc__)
t=next(iter(connector.iter_tickets(limit=1)))
payload={"ticket_id":t.id,"location_id":t.location_id}
print(emit("enrich_ticket",payload,ticket=t))
