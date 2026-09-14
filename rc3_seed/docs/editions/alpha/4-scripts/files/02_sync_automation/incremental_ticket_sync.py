"""Pull recently updated ITSM tickets and upsert an ArcGIS operational layer."""

from datetime import datetime, timedelta, timezone
from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap
from capybara.arcgis.client import ArcGISClient
from capybara.arcgis.operational import OperationalLayer
from capybara.services.sync import sync_ticket

args,cfg,connector,log = bootstrap(__doc__)
since = datetime.now(timezone.utc) - timedelta(minutes=int(cfg.get("sync.lookback_minutes",60)))
client = ArcGISClient.from_config(cfg)
layer = client.feature_layer(cfg.get("arcgis.operational_item_id"),cfg.get("arcgis.operational_layer_index",0))
operational = OperationalLayer(layer)

for ticket in connector.iter_tickets(updated_since=since,limit=args.limit):
    result = sync_ticket(ticket,operational,dry_run=cfg.dry_run)
    print(ticket.number,result.operation,result.message)
