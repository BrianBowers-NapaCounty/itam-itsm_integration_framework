"""Side-by-side troubleshooting view of one ITSM ticket and matching ArcGIS feature."""

import argparse,sys,json
from pathlib import Path
HERE=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(HERE))
from capybara.core.config import load_config
from capybara.connectors.registry import build_connector
from capybara.arcgis.client import ArcGISClient
from capybara.arcgis.operational import OperationalLayer

p=argparse.ArgumentParser(); p.add_argument("ticket_id")
p.add_argument("--config",default=str(HERE.parent/"config.toml")); a=p.parse_args()
cfg=load_config(a.config); c=build_connector(cfg); t=c.get_ticket(a.ticket_id)
op=OperationalLayer(ArcGISClient.from_config(cfg).feature_layer(cfg.get("arcgis.operational_item_id"),
                                                                 cfg.get("arcgis.operational_layer_index",0)))
features=op.query_by_source_id(t.id)
print("ITSM:",t)
print("ArcGIS:",[f.attributes for f in features])
