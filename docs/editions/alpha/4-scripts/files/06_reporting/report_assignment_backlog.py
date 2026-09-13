"""Summarize active ticket backlog by assignment group."""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap
from capybara.services.reporting import assignment_backlog
from capybara.core.serialization import write_csv, write_html_table

args,cfg,connector,log = bootstrap(__doc__)
rows = assignment_backlog(list(connector.iter_tickets(limit=args.limit)))
write_csv(cfg.output_dir/"assignment-backlog.csv",rows)
print(write_html_table(cfg.output_dir/"assignment-backlog.html","Assignment Backlog",rows))
