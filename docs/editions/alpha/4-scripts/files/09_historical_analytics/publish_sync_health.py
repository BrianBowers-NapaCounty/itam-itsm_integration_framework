from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))
from _common import bootstrap

"""Sample connector/ArcGIS health and write one Sync_Health history row."""

from datetime import datetime,timezone
from capybara.analytics.store import build_store
from capybara.services.monitoring import sync_lag_minutes,unmatched_location_rate
from capybara.analytics.service import run_id

args,cfg,connector,log=bootstrap(__doc__)
tickets=list(connector.iter_tickets(limit=args.limit or 500))
known_file=cfg.source.parent/"sample_data"/"known_locations.txt"
known={x.strip() for x in known_file.read_text().splitlines() if x.strip()} if known_file.exists() else set()
c=connector.health_check()
a_ok=None
try:
    from capybara.arcgis.client import ArcGISClient
    a_ok=ArcGISClient.from_config(cfg).health_check().ok
except Exception:
    a_ok=False
row={
    "OBSERVED_UTC":datetime.now(timezone.utc),"CONNECTOR_OK":c.ok,"ARCGIS_OK":a_ok,
    "SYNC_LAG_MIN":sync_lag_minutes(tickets),
    "UNMATCHED_RATE":unmatched_location_rate(tickets,known),
    "API_FAILURE_RATE":None,"QUEUE_DEPTH":None,"DEAD_LETTERS":None,
    "MESSAGE":c.message,"RUN_ID":run_id("health"),
}
print(build_store(cfg).add_rows("Sync_Health",[row]))
