"""Template for turning structured integration logs into an API failure-rate metric."""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap

args,cfg,connector,log = bootstrap(__doc__)
print("Production logic:")
print("- Query structured integration log rows for a rolling time window.")
print("- Group by endpoint/platform and HTTP class.")
print("- Exclude expected validation failures from transport failure rate.")
print("- Alert immediately on 401/403; retry 429/5xx according to policy.")
print("- Track numerator=failed API calls, denominator=all API calls.")
