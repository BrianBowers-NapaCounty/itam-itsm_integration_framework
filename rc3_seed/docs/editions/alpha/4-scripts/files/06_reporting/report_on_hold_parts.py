"""Produce CSV + HTML reports for tickets waiting on parts/equipment/procurement."""

from pathlib import Path
import sys
_SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_ROOT))

from _common import bootstrap
from capybara.services.reporting import tickets_on_hold
from capybara.core.serialization import write_csv, write_html_table

args,cfg,connector,log = bootstrap(__doc__)
rows = tickets_on_hold(list(connector.iter_tickets(limit=args.limit)))
print(write_csv(cfg.output_dir/"tickets-on-hold.csv",rows))
print(write_html_table(cfg.output_dir/"tickets-on-hold.html","Tickets On Hold — Parts / Equipment",rows,
                       "Review procurement bottlenecks, aging holds, affected facilities, and assignment ownership."))
