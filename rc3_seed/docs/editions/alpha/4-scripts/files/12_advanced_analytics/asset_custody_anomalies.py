from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))
from _common import bootstrap

"""Flag simple asset-custody conditions suitable for audit follow-up."""

args,cfg,connector,log=bootstrap(__doc__)
for a in connector.iter_assets(limit=args.limit):
    flags=[]
    if not a.location_id: flags.append("NO_LOCATION")
    if not a.assigned_to and "spare" not in str(a.status).lower(): flags.append("NO_CUSTODIAN")
    if any(x in str(a.status).lower() for x in ("missing","lost","stolen")): flags.append("LOSS_STATUS")
    if flags: print(a.asset_tag,a.name,",".join(flags))
