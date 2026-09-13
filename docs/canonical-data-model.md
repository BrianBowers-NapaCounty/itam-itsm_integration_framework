```{image} /_images/symbol-api.png
:alt: Canonical data model
:width: 64px
:class: page-symbol
```
# Canonical Data Model and Ownership

## What owns what?

| Information | Authoritative owner |
| --- | --- |
| Incident/request/task state | ITSM platform |
| Assignment, work notes, approval, SLA | ITSM platform |
| Asset lifecycle and custody | ITAM/CMDB |
| Facility/floor/unit geometry | ArcGIS Indoors / GIS |
| Spatial identifiers and indoor geometry | GIS |
| Crosswalk confidence and integration queue state | Middleware |
| Historical integration metrics | Capybara Analytics |
| Reporting snapshots | Derived; not authoritative |

## Canonical models

The reference code normalizes vendor records into `Ticket`, `Asset`, `LocationRef`, `HealthCheck`, `ReconciliationIssue`, and `OperationResult` objects. This keeps reporting and workflow logic independent of ServiceNow, TeamDynamix, Cherwell, or future connectors.

## Location match states

`Matched`, `Needs Review`, `Ambiguous`, `Not Found`, `Retired`, and `Suppressed` are intentionally explicit so poor-quality or uncertain location matches are not silently treated as valid.
