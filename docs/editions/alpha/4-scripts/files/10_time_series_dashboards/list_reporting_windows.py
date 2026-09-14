from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))
from _common import bootstrap

"""Print the standard rolling/calendar reporting windows used by Capybara."""

from capybara.analytics.windows import common_windows
args,cfg,connector,log=bootstrap(__doc__)
for w in common_windows(tz_name=cfg.get("analytics.time_zone","UTC")):
    print(f"{w.code:18} {w.start.isoformat()} -> {w.end.isoformat()}  {w.label}")
