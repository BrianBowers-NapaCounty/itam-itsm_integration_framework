"""Display canonical fields plus a small sample of raw vendor records."""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap
from capybara.core.serialization import write_json

args,cfg,connector,log = bootstrap(__doc__)
tickets = list(connector.iter_tickets(limit=args.limit or 3))
assets = list(connector.iter_assets(limit=args.limit or 3))
payload = {
    "platform":connector.platform_name,
    "capabilities":sorted(connector.capabilities),
    "ticket_samples":[{"canonical":t,"raw":t.raw} for t in tickets],
    "asset_samples":[{"canonical":a,"raw":a.raw} for a in assets],
}
path = write_json(cfg.output_dir/"itsm-schema-samples.json",payload)
print(path)
