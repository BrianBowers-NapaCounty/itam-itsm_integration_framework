from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))
from _common import bootstrap

"""Backfill chart-ready historical metric rows from externally supplied period extracts.

A production backfill normally needs historical ITSM exports because current
tickets cannot reconstruct prior point-in-time backlog accurately. This script
therefore demonstrates the storage contract and refuses to fabricate history.
"""

from capybara.analytics.store import build_store
args,cfg,connector,log=bootstrap(__doc__)
store=build_store(cfg)
print("Backfill strategy:")
print("1. Export dated historical ticket/asset snapshots from the source ITSM/warehouse.")
print("2. Normalize each dated extract through the connector/model layer.")
print("3. Compute Metric_Snapshots/Ticket_Daily/Asset_Daily for the extract date.")
print("4. Append rows with a distinct RUN_ID and preserve source-extract provenance.")
print("No synthetic historical backlog is generated from today's state.")
