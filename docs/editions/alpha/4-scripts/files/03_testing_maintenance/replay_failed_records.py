"""Skeleton for replaying a reviewed dead-letter/error export.

A production queue should keep event IDs, attempts, timestamps, error classes,
source record IDs, and payload hashes. This demo only documents the replay seam.
"""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap

args,cfg,connector,log = bootstrap(__doc__)
print("PSEUDOCODE:")
print("1. Read reviewed failed-event CSV/queue table.")
print("2. Reject rows not explicitly marked ApprovedForReplay.")
print("3. Re-fetch authoritative ITSM record instead of trusting stale payload.")
print("4. Re-run normalize -> match -> ArcGIS publish -> writeback.")
print("5. Record new correlation ID and preserve the original event ID.")
