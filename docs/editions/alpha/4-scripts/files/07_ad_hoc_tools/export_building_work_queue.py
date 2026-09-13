"""Export active work for one location/building identifier."""

import argparse,sys
from pathlib import Path
HERE=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(HERE))
from capybara.core.config import load_config
from capybara.connectors.registry import build_connector
from capybara.core.serialization import write_csv

p=argparse.ArgumentParser()
p.add_argument("location")
p.add_argument("--config",default=str(HERE.parent/"config.toml"))
a=p.parse_args()
cfg=load_config(a.config); c=build_connector(cfg)
rows=[{"number":t.number,"description":t.short_description,"status":t.status,
       "priority":t.priority,"assignee":t.assignee}
      for t in c.iter_tickets() if t.location_id==a.location and str(t.status).lower() not in {"closed","resolved"}]
print(write_csv(cfg.output_dir/f"work-queue-{a.location}.csv",rows))
