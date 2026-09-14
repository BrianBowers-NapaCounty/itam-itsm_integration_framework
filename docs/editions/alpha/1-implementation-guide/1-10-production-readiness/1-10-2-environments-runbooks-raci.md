```{image} /_images/symbol-arrow2.png
:alt: Environment Promotion, Runbooks, and RACI
:width: 64px
:class: page-symbol
```

# Environment Promotion, Runbooks, and RACI

## Environment Model and Promotion Path

**Environment separation**

Development, test, staging, and production should have separate configuration, credentials, layers, and promotion procedures.

| Environment | Purpose | ServiceNow Scope | ArcGIS Scope | Promotion Gate |
| --- | --- | --- | --- | --- |
| Development | Build and unit-test scripts, transforms, and matching rules. | Mock data or sandbox records. | Developer-owned layers or scratch feature services. | Unit tests pass; no production credentials used. |
| Test | Validate API behavior, field maps, and integration flow. | Non-production instance or test tables. | Non-production Portal content or test folder/group. | Integration tests pass; security review begins. |
| Staging | Mirror production schema and deployment settings before release. | Production-like record shape with controlled sample volume. | Production-like layers, maps, and dashboards. | User acceptance testing and operational signoff. |
| Production | Operate the approved integration service. | Approved tables, fields, and write-back rules only. | Approved operational layers and dashboards. | Change control, monitoring, backups, support handoff. |

Production-data warning
Testing directly against production tickets, production assets, or production Indoors reference layers should be avoided except under a documented emergency or controlled validation procedure.

## Operational Runbooks

**Supportable operation**

Production support requires repeatable procedures for normal maintenance, failure recovery, and emergency disablement.

| Runbook | Trigger | Required Steps | Exit Criteria |
| --- | --- | --- | --- |
| Restart Flask endpoint | Health check fails or endpoint becomes unavailable. | Check logs, stop app, start app, verify `/health`, send test event. | Health endpoint returns OK and event queue accepts a test event. |
| Restart worker | Queue depth grows while endpoint is healthy. | Check worker log, stop worker, confirm no stuck lock, restart worker, monitor throughput. | Oldest pending event age decreases. |
| Reprocess failed queue item | Record corrected or transient failure resolved. | Review error, reset status, increment manual retry marker, monitor reprocessing. | Event completes or returns a clearer exception. |
| Disable ServiceNow write-back | Write-back loop, bad field mapping, or security concern. | Set write-back disabled flag, restart worker if needed, confirm ArcGIS updates continue if approved. | No further write-back attempts occur. |
| Pause ArcGIS updates | Layer schema change, Portal outage, or data-quality incident. | Set ArcGIS publishing disabled flag, continue queueing, notify stakeholders. | No layer edits occur; backlog is preserved. |
| Rotate credentials | Scheduled rotation, suspected exposure, or expired secret. | Create new secret, update store, restart app/worker, validate both API clients. | Successful ServiceNow fetch and ArcGIS edit test. |
| Recover from ServiceNow outage | API failures or outage alert. | Pause worker or allow retry, monitor retry count, resume after API stability. | Delta pull catches missed updates. |
| Recover from ArcGIS outage | Portal, Server, token, or feature-layer failures. | Queue events, suppress destructive retries, validate layer once service returns. | Backlog drains without duplicates. |
| Rebuild crosswalk | Rooms renamed, facility restructured, or new Indoors data published. | Export current crosswalk, generate candidates, review exceptions, publish versioned crosswalk. | Reconciliation exception count returns to acceptable range. |
| Weekly reconciliation report | Scheduled governance review. | Compare source and target counts, missing keys, stale statuses, duplicate mappings. | Report delivered to owners and exceptions assigned. |

## Data Governance and RACI

**Ownership before automation**

Production integration succeeds when each data domain has an owner, steward, consulted parties, and informed audiences.

| Data / Function | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| ServiceNow tickets | Service desk lead | ITSM owner | GIS, cybersecurity, operations | Managers, technicians |
| Assets and CIs | Asset manager | ITAM owner | Finance, GIS, security | Department managers |
| Indoor spaces | GIS / Indoors data steward | GIS program owner | Facilities, IT, departments | Users, managers |
| Crosswalk tables | Middleware steward | Integration owner | GIS, ITSM, ITAM | Operations support |
| Write-back fields | Middleware owner | ITSM owner | GIS, security, service desk | Technicians, managers |
| Operational dashboards | GIS / reporting steward | Operations manager | Service desk, asset manager | Leadership |
| Security controls | Security reviewer | Security officer or designee | IT operations, GIS, ITSM | Project sponsor |
| Runbooks and support | Operations support lead | Application owner | Developers, GIS, service desk | Help desk and leadership |
