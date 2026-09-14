"""Template for notifying maintainers when a reconciliation/export contains high-severity drift."""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap

args,cfg,connector,log = bootstrap(__doc__)
print("Production implementation should:")
print("1. Read reconciliation issues from queue/database, not only CSV.")
print("2. Alert on high-priority source records absent from ArcGIS.")
print("3. Alert on duplicate crosswalks/schema errors immediately.")
print("4. Include correlation IDs and links to the support runbook.")
