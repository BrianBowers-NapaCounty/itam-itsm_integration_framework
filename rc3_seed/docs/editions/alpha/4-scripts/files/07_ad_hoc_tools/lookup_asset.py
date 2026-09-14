"""Look up an asset by ID/tag and show the canonical normalized record."""

import argparse, sys
from pathlib import Path
HERE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(HERE))
from capybara.core.config import load_config
from capybara.connectors.registry import build_connector

p=argparse.ArgumentParser()
p.add_argument("asset_id")
p.add_argument("--config",default=str(HERE.parent/"config.toml"))
a=p.parse_args()
c=build_connector(load_config(a.config))
print(c.get_asset(a.asset_id))
