from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))
from _common import bootstrap

"""Run source-vs-operational reconciliation and persist issues historically."""

from datetime import datetime,timezone
from capybara.arcgis.client import ArcGISClient
from capybara.arcgis.operational import OperationalLayer
from capybara.analytics.store import build_store
from capybara.analytics.service import run_id
from capybara.services.reconciliation import compare_source_to_operational

args,cfg,connector,log=bootstrap(__doc__)
tickets=list(connector.iter_tickets(limit=args.limit))
op=OperationalLayer(ArcGISClient.from_config(cfg).feature_layer(
    cfg.get("arcgis.operational_item_id"),cfg.get("arcgis.operational_layer_index",0)))
issues=compare_source_to_operational(tickets,op.all())
rid=run_id("recon"); now=datetime.now(timezone.utc)
rows=[{
    "OBSERVED_UTC":now,"RECORD_TYPE":x.record_type,"RECORD_ID":x.record_id,
    "ISSUE_CODE":x.issue,"SEVERITY":x.severity,"SAFE_REPAIR":x.safe_to_repair,
    "SOURCE_VALUE":str(x.source_value or ""),"TARGET_VALUE":str(x.target_value or ""),"RUN_ID":rid,
} for x in issues]
print(build_store(cfg).add_rows("Reconciliation_History",rows))
