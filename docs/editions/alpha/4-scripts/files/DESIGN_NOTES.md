# Scripts Architecture Notes

## Layer 1 — Canonical core

`capybara/core` contains models, configuration, connector contracts, logging,
and shared utilities. No file in this layer should know whether the ITSM system
is ServiceNow, TeamDynamix, Cherwell, or something else.

## Layer 2 — Platform connectors

`capybara/connectors` translates platform-specific REST requests/responses into
canonical Capybara objects. Adding a future connector should not require
rewriting reports or monitoring routines.

The connector contract intentionally stays small:

- health check
- get / iterate tickets
- get / iterate assets
- update ticket
- add work note
- expose declared capabilities

## Layer 3 — ArcGIS / Indoors access

`capybara/arcgis` wraps ArcGIS API for Python connections and operational
feature-layer access. It does not own ITSM interpretation.

## Layer 4 — Reusable services

`capybara/services` implements matching, synchronization, reconciliation,
monitoring, notification selection, and report construction using canonical
objects.

## Layer 5 — Operational scripts and notebooks

The numbered task folders are intentionally thin entry points. They demonstrate
scheduled automation and ad-hoc invocation without burying reusable logic in
single-use scripts.

## Safe defaults

Examples are deliberately conservative:

- writes require `dry_run = false`;
- production credentials are read from environment variables;
- TLS verification is on;
- no connector stores passwords or tokens in source;
- automatic reconciliation repairs are restricted to clearly safe cases;
- alerts can be previewed through the console notifier before SMTP is enabled.
