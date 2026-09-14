"""Inspect one ticket's canonical and raw vendor representation for troubleshooting."""

import argparse, sys, json
from pathlib import Path
HERE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(HERE))
from capybara.core.config import load_config
from capybara.connectors.registry import build_connector

p=argparse.ArgumentParser()
p.add_argument("ticket_id")
p.add_argument("--config",default=str(HERE.parent/"config.toml"))
a=p.parse_args()
t=build_connector(load_config(a.config)).get_ticket(a.ticket_id)
print(t)
print(json.dumps(t.raw,indent=2,default=str))
