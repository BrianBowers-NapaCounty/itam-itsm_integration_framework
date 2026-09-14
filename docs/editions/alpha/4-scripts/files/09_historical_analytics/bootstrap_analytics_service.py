from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))
from _common import bootstrap

"""Create/verify the Capybara hosted analytics tables.

If analytics.item_id is blank, this script attempts to create an empty hosted
feature service using the current GIS account, then adds the standard tables.
Creating hosted services requires appropriate privileges.
"""

from capybara.arcgis.client import ArcGISClient
from capybara.analytics.store import HostedAnalyticsStore
from capybara.analytics.schemas import table_definitions

args,cfg,connector,log=bootstrap(__doc__)
arc=ArcGISClient.from_config(cfg)
item_id=str(cfg.get("analytics.item_id","")).strip()

if not item_id:
    name=str(cfg.get("analytics.service_name","Capybara_Analytics"))
    create_params={
        "name":name,
        "serviceDescription":"Capybara historical analytics tables",
        "hasStaticData":False,
        "maxRecordCount":2000,
        "supportedQueryFormats":"JSON",
        "capabilities":"Create,Delete,Query,Update,Editing",
    }
    item=arc.gis.content.create_service(
        name=name, service_type="featureService", create_params=create_params,
        folder=str(cfg.get("analytics.folder","") or "") or None,
        item_properties={"title":name,"snippet":"Capybara Framework historical analytics",
                         "tags":["Capybara","ITSM","ITAM","ArcGIS Indoors","analytics"]},
    )
    item_id=item.id
    print("Created hosted service:",item_id)
    print("Add this item ID to analytics.item_id in config.toml.")

store=HostedAnalyticsStore(arc.gis,item_id,chunk_size=cfg.get("analytics.chunk_size",200))
print(store.ensure_tables())
print("Tables:",sorted(store.tables))
