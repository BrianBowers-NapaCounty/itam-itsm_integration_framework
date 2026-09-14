"""Demonstrate asset-to-ArcGIS attribute synchronization with safe dry-run behavior."""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap
from capybara.arcgis.client import ArcGISClient
from capybara.arcgis.operational import OperationalLayer

args,cfg,connector,log = bootstrap(__doc__)
client = ArcGISClient.from_config(cfg)
layer = client.feature_layer(cfg.get("arcgis.asset_item_id"),cfg.get("arcgis.asset_layer_index",0))
operational = OperationalLayer(layer,id_field="ITSM_ID")

for a in connector.iter_assets(limit=args.limit):
    attrs = {
        "ASSET_TAG":a.asset_tag,"NAME":a.name,"STATUS":a.status,
        "ASSIGNED_TO":a.assigned_to,"LOCATION_ID":a.location_id,
        "MODEL":a.model,"DEPARTMENT":a.department,
    }
    result = operational.upsert_attributes(a.id,attrs,dry_run=cfg.dry_run)
    print(a.asset_tag,result.message)
