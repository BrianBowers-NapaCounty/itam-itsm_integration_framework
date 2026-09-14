from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))
from _common import bootstrap

"""Validate required hosted analytics table names and fields."""

from capybara.analytics.store import build_store,HostedAnalyticsStore
from capybara.analytics.schemas import TABLES
args,cfg,connector,log=bootstrap(__doc__)
store=build_store(cfg)
if not isinstance(store,HostedAnalyticsStore):
    print("Local SQLite store selected; tables already materialized from canonical schema.")
    raise SystemExit(0)
errors=[]
for name,schema in TABLES.items():
    if name not in store.tables:
        errors.append(f"Missing table: {name}");continue
    actual={f["name"] for f in store.tables[name].properties.fields}
    expected={f["name"] for f in schema["fields"]}
    for missing in sorted(expected-actual):
        errors.append(f"{name}: missing field {missing}")
print("OK" if not errors else "\n".join(errors))
raise SystemExit(1 if errors else 0)
