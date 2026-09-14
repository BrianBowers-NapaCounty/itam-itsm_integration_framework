from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))
from _common import bootstrap

"""Print suggested ArcGIS Dashboard/Experience Builder data-source usage."""

args,cfg,connector,log=bootstrap(__doc__)
print("""
Suggested dashboard sources
---------------------------
Metric_Snapshots       KPI cards + arbitrary metric series
Ticket_Daily           backlog / hold / SLA / assignment charts
Asset_Daily            asset-status and missing/spare trends
Sync_Health            middleware reliability chart
Reconciliation_History drift/error trend
Period_Summaries       period selector / comparison cards
Data_Quality_Snapshots governance quality trend

Recommended selectors:
- period_code
- facility/location
- assignment group
- department
- category
- severity
""")
