"""Inventory fields/capabilities for configured ArcGIS operational, asset, and unit layers."""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap
from capybara.arcgis.client import ArcGISClient
from capybara.core.serialization import write_json

args,cfg,connector,log = bootstrap(__doc__)
client = ArcGISClient.from_config(cfg)
rows = []
for label,item_key,index_key in [
    ("operational","arcgis.operational_item_id","arcgis.operational_layer_index"),
    ("assets","arcgis.asset_item_id","arcgis.asset_layer_index"),
    ("units","arcgis.unit_item_id","arcgis.unit_layer_index"),
]:
    item_id = cfg.get(item_key)
    if not item_id:
        continue
    layer = client.feature_layer(item_id,cfg.get(index_key,0))
    rows.append({
        "name":label,"url":layer.url,
        "capabilities":getattr(layer.properties,"capabilities",""),
        "object_id_field":getattr(layer.properties,"objectIdField",""),
        "fields":[dict(f) for f in layer.properties.fields],
    })
print(write_json(cfg.output_dir/"arcgis-schema.json",rows))
