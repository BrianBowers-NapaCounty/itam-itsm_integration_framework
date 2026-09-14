"""Template queue/dead-letter monitoring routine."""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap

args,cfg,connector,log = bootstrap(__doc__)
print("Metrics to expose:")
print("queue_depth, oldest_pending_age, dead_letter_count, retry_count, workers_alive")
print("This sample leaves storage implementation open (SQL Server, SQLite, Service Bus, etc.).")
