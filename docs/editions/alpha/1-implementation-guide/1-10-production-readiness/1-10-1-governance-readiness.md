```{image} /_images/symbol-target.png
:alt: Release Governance and Production Readiness
:width: 64px
:class: page-symbol
```

# Release Governance and Production Readiness

## What Belongs in This Guide vs. Companion Materials

**Document scope**

Core governance and design guidance belongs in this guide. Editable implementation assets should be maintained as source-controlled companion files.

| Material | In This Guide | Companion Read the Docs Asset | Reason |
| --- | --- | --- | --- |
| Production readiness checklist | Yes | Printable PDF / spreadsheet version | The checklist belongs in the guide, but agencies need a fillable version. |
| Field mapping templates | Yes | CSV/XLSX/YAML templates | The concepts belong here; implementation teams need editable mappings. |
| SQL DDL | Yes, starter version | Versioned SQL scripts | Starter DDL clarifies architecture; executable scripts should be maintained separately. |
| Python middleware scripts | Architecture and examples | Full source files and notebooks | Production code needs version control, tests, and release packaging. |
| Budget calculator | Inputs and assumptions | Spreadsheet calculator | Calculators need formulas and editable local assumptions. |
| Presentation templates | Messaging guidance | PPTX / PDF templates | Reusable communication material is better as separate files. |
| Runbooks | Core procedure summaries | Detailed operational runbook files | Local teams will need environment-specific commands and contacts. |

## Release Governance

**Release governance**

Release governance keeps the public framework, local adaptations, and future contributions understandable, reviewable, and maintainable.

| Release Element | Production Rule | Why It Matters |
| --- | --- | --- |
| Edition numbering | Use named editions for major public releases and maintenance numbers for smaller corrections. | Readers can cite a stable edition while the framework remains a living document. |
| Change categories | Classify changes as editorial, technical, security, architectural, operational, or breaking. | Different changes require different levels of review. |
| Technical review | Require review by someone familiar with ArcGIS Enterprise, ArcGIS Indoors, Python, and ITSM/ITAM APIs. | Prevents diagrams and implementation steps from drifting away from workable practice. |
| Security review | Require review of authentication, authorization, credentials, exposure, logging, and data classification. | Integration services create new data flows and potential attack surfaces. |
| Operational review | Require review by the team that will monitor, restart, repair, and explain the integration. | A working pilot is not production-ready until it is supportable. |
| Accessibility and publication review | Check headings, tables, alt text, print output, icons, QR codes, and link labels. | The framework is intended for public reading, reuse, and PDF export. |
| Deprecation | Mark outdated connector patterns, vendor-specific references, and obsolete scripts before removal. | Maintains historical clarity without endorsing stale practices. |

### Release Review Matrix

| Change Type | Technical Review | Security Review | Operational Review | Editorial Review |
| --- | --- | --- | --- | --- |
| Editorial correction | Optional | No | No | Required |
| New diagram | Required | Conditional | Conditional | Required |
| New middleware procedure | Required | Required | Required | Required |
| Credential or security guidance | Required | Required | Required | Required |
| Connector or vendor pattern | Required | Conditional | Required | Required |
| Breaking change to templates or scripts | Required | Required | Required | Required |

## Production Readiness Review

**Go-live gate**

Before go-live, the implementation team should answer every readiness question or formally accept the risk.

| Area | Readiness Questions | Evidence to Collect |
| --- | --- | --- |
| Hosting | Where does the middleware run? Who patches it? Is the runtime supported? | Server record, application owner, patch schedule, recovery procedure. |
| Security | Are tokens, service accounts, webhook signatures, and credentials controlled? | Credential inventory, permissions matrix, secrets procedure, security signoff. |
| Monitoring | Can support staff see queue depth, failed events, API errors, retries, and reconciliation exceptions? | Dashboard, alert rules, log examples, escalation path. |
| Resilience | What happens when ServiceNow, ArcGIS, the database, or the network is unavailable? | Retry policy, outage test, backoff settings, recovery runbook. |
| Data quality | How are unresolved locations, duplicate matches, stale rooms, and retired assets handled? | Exception queue, alias review process, reconciliation report. |
| Support ownership | Who owns the endpoint, worker, queue, field maps, layers, write-back rules, and dashboards? | RACI, on-call expectations, support contacts. |
| Change control | How are schema, API, workflow, and map-layer changes reviewed before production? | Change ticket template, review checklist, rollback plan. |
