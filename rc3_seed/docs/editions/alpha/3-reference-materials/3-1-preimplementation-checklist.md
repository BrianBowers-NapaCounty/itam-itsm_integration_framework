```{image} /_images/symbol-checkmark2.png
:alt: 3-1-preimplementation-checklist
:width: 64px
:class: page-symbol
```

<div>

### Pre-implementation Checklist

<div class="checklist-grid">

<div class="check-card">

#### Governance and Sponsorship

- Executive sponsor identified.
- GIS, ITSM/ITAM, cybersecurity, facilities, and service desk stakeholders identified.
- Decision owner assigned for architecture pattern selection.
- Data-owner roles documented for ServiceNow, ArcGIS, and middleware artifacts.
- Change-management and communications approach drafted.

</div>

<div class="check-card">

#### Data Readiness

- Buildings, floors, rooms, cubicles, shared spaces, and facilities have consistent identifiers.
- Asset records include usable location references.
- CMDB / asset records have durable IDs such as sys_id, asset tag, or serial number.
- Indoor GIS layers contain stable facility, level, and unit identifiers.
- Known duplicate, stale, missing, or ambiguous records have been logged.

</div>

<div class="check-card">

#### Security and Access

- Integration accounts are dedicated and least-privilege.
- API credentials are stored outside source code.
- Webhook, API gateway, VPN, or private connectivity approach is approved.
- PII, sensitive asset, and security-sensitive location fields are classified.
- Audit logging and retention expectations are documented.

</div>

<div class="check-card">

#### Technical Readiness

- ArcGIS Enterprise / Indoors environment is available and tested.
- ServiceNow or ITSM/ITAM API access is available in a non-production environment.
- Development, test, and production separation is planned.
- Middleware hosting, scheduling, logging, and backup locations are identified.
- Error handling, retries, reconciliation, and manual reprocessing are included in design.

</div>

<div class="check-card">

#### Operational Readiness

- Runbook owner identified.
- Support model defined for after-hours failures, credential rotation, and API outages.
- Dashboard consumers identified.
- Success metrics and pilot exit criteria defined.
- Training and user-support materials drafted.

</div>

</div>

</div>