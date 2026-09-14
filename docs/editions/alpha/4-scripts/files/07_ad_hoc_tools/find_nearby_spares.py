"""ArcGIS-powered example: query spare-equipment points near a supplied geometry.

This demonstrates a cool spatial use case without prescribing a particular
Indoors asset schema. Configure your asset layer's status/model fields locally.
"""

import argparse,sys,json
from pathlib import Path
HERE=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(HERE))
from capybara.core.config import load_config
from capybara.arcgis.client import ArcGISClient

p=argparse.ArgumentParser()
p.add_argument("x",type=float); p.add_argument("y",type=float)
p.add_argument("--distance",type=float,default=250)
p.add_argument("--config",default=str(HERE.parent/"config.toml"))
a=p.parse_args(); cfg=load_config(a.config)
layer=ArcGISClient.from_config(cfg).feature_layer(cfg.get("arcgis.asset_item_id"),cfg.get("arcgis.asset_layer_index",0))
geometry={"x":a.x,"y":a.y,"spatialReference":{"wkid":3857}}
fs=layer.query(where="STATUS='Spare'",geometry=geometry,distance=a.distance,
               units="esriSRUnit_Meter",out_fields="*",return_geometry=True)
print(f"{len(fs.features)} nearby spare(s)")
for f in fs.features:
    print(json.dumps(f.attributes,default=str))
