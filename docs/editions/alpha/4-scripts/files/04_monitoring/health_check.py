"""Run connector and ArcGIS health checks and save machine-readable status."""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap
from capybara.core.serialization import write_json

args,cfg,connector,log = bootstrap(__doc__)
checks = [connector.health_check()]
try:
    from capybara.arcgis.client import ArcGISClient
    checks.append(ArcGISClient.from_config(cfg).health_check())
except Exception as exc:
    log.warning("ArcGIS health unavailable: %s",exc)
print(write_json(cfg.output_dir/"health.json",checks))
for c in checks:
    print(c.component,c.ok,c.message)
