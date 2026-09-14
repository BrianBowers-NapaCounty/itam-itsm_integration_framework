"""Illustrate conservative auto-repair: only issues explicitly marked safe are eligible."""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap
from capybara.services.reconciliation import safe_repairs

args,cfg,connector,log = bootstrap(__doc__)
print("This entry point is intentionally a guardrail.")
print("Feed ReconciliationIssue objects from reconcile_operational_layer.py into safe_repairs().")
print("Automatic deletion of duplicates/orphans is intentionally NOT implemented.")
