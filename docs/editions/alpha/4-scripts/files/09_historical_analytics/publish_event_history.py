from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))
from _common import bootstrap

"""Publish normalized ITSM change events from an event JSON file.

Expected JSON fields: event_utc,event_type,record_type,record_id,public_id,
field_name,old_value,new_value,location_id,asset_id,correlation.
"""

import argparse,json
from capybara.analytics.store import build_store
from capybara.analytics.service import run_id

args,cfg,connector,log=bootstrap(__doc__)
# Optional convention: place reviewed event export in sample_data/events.json.
path=cfg.source.parent/"sample_data"/"events.json"
if not path.exists():
    print("No sample_data/events.json found. This is an event-ingest template.")
    raise SystemExit(0)
rid=run_id("events")
rows=[]
for e in json.loads(path.read_text(encoding="utf-8")):
    rows.append({
        "EVENT_UTC":e.get("event_utc"),"EVENT_TYPE":e.get("event_type"),
        "RECORD_TYPE":e.get("record_type"),"RECORD_ID":e.get("record_id"),
        "PUBLIC_ID":e.get("public_id"),"FIELD_NAME":e.get("field_name"),
        "OLD_VALUE":e.get("old_value"),"NEW_VALUE":e.get("new_value"),
        "LOCATION_ID":e.get("location_id"),"ASSET_ID":e.get("asset_id"),
        "CORRELATION":e.get("correlation"),"RUN_ID":rid,
    })
print(build_store(cfg).add_rows("Event_History",rows))
