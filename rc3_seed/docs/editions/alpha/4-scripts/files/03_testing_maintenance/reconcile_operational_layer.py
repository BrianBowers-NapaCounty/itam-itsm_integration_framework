"""Compare ITSM tickets with the ArcGIS operational layer and export drift."""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap
from capybara.arcgis.client import ArcGISClient
from capybara.arcgis.operational import OperationalLayer
from capybara.services.reconciliation import compare_source_to_operational
from capybara.core.serialization import write_csv

args,cfg,connector,log = bootstrap(__doc__)
tickets = list(connector.iter_tickets(limit=args.limit))
client = ArcGISClient.from_config(cfg)
layer = OperationalLayer(client.feature_layer(cfg.get("arcgis.operational_item_id"),
                                               cfg.get("arcgis.operational_layer_index",0)))
issues = compare_source_to_operational(tickets,layer.all())
print(write_csv(cfg.output_dir/"reconciliation-issues.csv",issues))
