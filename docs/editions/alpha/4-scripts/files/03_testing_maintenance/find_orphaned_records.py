"""Find ArcGIS operational records whose source ITSM ID is absent from the extract."""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap
from capybara.arcgis.client import ArcGISClient
from capybara.arcgis.operational import OperationalLayer
from capybara.core.serialization import write_csv

args,cfg,connector,log = bootstrap(__doc__)
source_ids = {str(t.id) for t in connector.iter_tickets(limit=args.limit)}
op = OperationalLayer(ArcGISClient.from_config(cfg).feature_layer(
    cfg.get("arcgis.operational_item_id"),cfg.get("arcgis.operational_layer_index",0)
))
orphans = []
for f in op.all():
    sid = str(f.attributes.get("ITSM_ID",""))
    if sid and sid not in source_ids:
        orphans.append({"ITSM_ID":sid,"OBJECTID":f.attributes.get("OBJECTID"),"status":f.attributes.get("STATUS")})
print(write_csv(cfg.output_dir/"orphaned-operational-records.csv",orphans))
