"""Tiny extension registry for local Capybara customizations."""

from __future__ import annotations
from collections import defaultdict

HOOKS=defaultdict(list)

def register(hook_name):
    def deco(fn):
        HOOKS[hook_name].append(fn)
        return fn
    return deco

def emit(hook_name, value, **context):
    for fn in HOOKS.get(hook_name,()):
        value=fn(value,**context)
    return value

# Suggested hook names:
# normalize_ticket, normalize_asset, enrich_ticket, enrich_asset,
# before_publish, after_publish, metric_rows, alert_rows, report_rows.
