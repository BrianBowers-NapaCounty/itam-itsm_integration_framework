# Capybara Framework

**Spatial ITAM / ITSM Integration with ArcGIS Indoors**

Capybara is an open reference framework for connecting indoor GIS context to existing IT service-management and asset-management systems. It combines architecture guidance, governance, production-readiness material, platform-neutral Python reference code, sample connectors, reporting/alerting workflows, and historical analytics patterns.

## What is included

- Sphinx/MyST documentation preserving the existing Alpha page paths.
- Integration patterns for on-premises, Azure VM, brokered, Koop, and vendor-supported connector approaches.
- Reference connectors for ServiceNow, TeamDynamix, Cherwell, and a no-credentials MockConnector.
- ArcGIS API for Python examples for operational layers, Indoors crosswalks, hosted analytics tables, and spatial reporting.
- Monitoring, reconciliation, alerts, reporting, historical time-series, advanced analytics, and extension examples.
- Reproducible Read the Docs configuration plus local multi-format release tooling.

## Quick start

```text
python docs/editions/alpha/4-scripts/files/06_reporting/report_on_hold_parts.py --config config.toml
```

Use `docs/quick-start.md` for the zero-credentials demo path.

## RC3 publication model

The Original Edition 1.0.0 uses the still-live Alpha site as its content and visual baseline. Before deployment, `Capybara_RC3_Integrated_Deployment.ipynb` recovers the exact public source, all protected media/downloads, and the original `capybara.css`; it then extends those same pages and routes with the expanded architecture, automation, analytics, operations, and production-readiness material. Publication is blocked unless the page-by-page completeness audit passes.

## Documentation

Production site: https://capybara-framework.readthedocs.io

## Recovery provenance

This repository is a reconstructed and expanded continuation of the original Capybara documentation project. See `RECOVERY_NOTES.md` and `SOURCE_PROVENANCE.md`.

## License

Open Data Commons Public Domain Dedication and License (PDDL) 1.0. See `LICENSE.md`.
