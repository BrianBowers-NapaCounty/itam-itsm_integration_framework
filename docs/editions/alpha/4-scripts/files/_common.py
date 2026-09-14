"""Shared command-line bootstrap for sample task scripts."""

from __future__ import annotations
import argparse, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from capybara.core.config import load_config
from capybara.connectors.registry import build_connector
from capybara.core.logging_utils import configure_logging


def bootstrap(description):
    p = argparse.ArgumentParser(description=description)
    p.add_argument("--config", default=str(HERE.parent/"config.toml"))
    p.add_argument("--limit", type=int, default=None)
    args = p.parse_args()
    cfg = load_config(args.config)
    log = configure_logging(cfg.get("general.log_level","INFO"))
    connector = build_connector(cfg)
    return args, cfg, connector, log
