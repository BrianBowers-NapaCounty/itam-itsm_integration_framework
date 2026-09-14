```{image} /_images/symbol-important.png
:alt: Security Controls, Field Mapping, and Exceptions
:width: 64px
:class: page-symbol
```

# Security Controls, Field Mapping, and Exceptions

## Security Control Matrix

**Security posture tiers**

Minimum, recommended, and advanced controls help agencies choose an architecture that fits risk, staffing, and policy.

| Control Area | Minimum | Recommended | Advanced |
| --- | --- | --- | --- |
| Transport security | HTTPS for all endpoints. | TLS with current approved ciphers and certificate lifecycle management. | Private connectivity or mutual TLS where justified. |
| Webhook validation | Shared secret header. | HMAC signature over raw payload with timestamp validation. | HMAC, IP allowlist, replay protection, and gateway-level inspection. |
| Authentication | Dedicated integration accounts. | OAuth/app registration or platform-supported service principal model. | Short-lived credentials managed through enterprise vaulting. |
| Authorization | Least-privilege table/layer permissions. | Separate accounts for read, write, and administration. | Just-in-time access and conditional-access controls. |
| Secrets | Environment variables outside source code. | Approved secret store with access logging. | Enterprise vault, automated rotation, and break-glass procedure. |
| Logging | Application logs with event IDs. | Structured logs with step, duration, source ID, and target ID. | SIEM integration, alerting, and correlation with network/security telemetry. |
| Data minimization | Do not copy unnecessary fields. | Explicit allowlist of fields and approved write-back values. | Data classification review and automated field leakage checks. |
| Administrative controls | Manual stop/start procedure. | Feature flags for write-back, ArcGIS publishing, and worker pause. | Administrative console with audit trail and approval workflow. |

## Field Mapping Templates

**Implementation mapping templates**

Field maps should be reviewed like code because they define how records move between authoritative systems.

### ServiceNow Incident to ArcGIS Operational Incident Layer

| ServiceNow Field | ArcGIS Field | Required | Transform | Notes |
| --- | --- | --- | --- | --- |
| `sys_id` | `integration_key` | Yes | Direct | Primary idempotency key for upsert. |
| `number` | `ticket_number` | Yes | Direct | Human-readable ticket reference. |
| `short_description` | `summary` | Yes | Trim/truncate | Respect layer field length. |
| `priority` | `priority` | Yes | Normalize domain | Use stable coded values for map symbology. |
| `state` | `status` | Yes | Normalize domain | Do not assume labels are identical across systems. |
| `assignment_group` | `assignment_group` | No | Reference display lookup | Useful for operations dashboards. |
| `assigned_to` | `technician_name` | No | Reference display lookup | Minimize personal data if not required. |
| `cmdb_ci` | `ci_sys_id` | No | Reference lookup | Can support asset-derived location matching. |
| `location` | `unit_id`, `level_id`, `facility_id` | Yes | Crosswalk match | Primary spatial enrichment step. |
| `opened_at` | `opened_at_utc` | Yes | Timezone normalization | Use UTC or documented local convention. |
| `sys_updated_on` | `source_updated_at` | Yes | Timezone normalization | Supports reconciliation and stale-record detection. |

### ArcGIS to ServiceNow Write-Back Fields

| ArcGIS / Middleware Value | ServiceNow Field | Purpose | Write Policy |
| --- | --- | --- | --- |
| Map URL | `u_arcgis_map_url` | Open mapped ticket or asset context. | Allowed when map sharing is approved. |
| Facility ID | `u_arcgis_facility_id` | Building-level context. | Allowed as derived spatial context. |
| Level ID | `u_arcgis_level_id` | Floor-level context. | Allowed as derived spatial context. |
| Unit ID | `u_arcgis_unit_id` | Room, cubicle, or shared-space linkage. | Allowed after confidence threshold is met. |
| Match confidence | `u_arcgis_match_confidence` | Data-quality review support. | Allowed and recommended. |
| Integration note | `work_notes` | Human-readable summary of spatial match. | Allowed if it does not create noisy update loops. |

## Exception Handling Workflow

**Exception states**

Unmapped records, permission failures, duplicate features, and schema changes should move through explicit statuses rather than disappearing into logs.

| Status | Meaning | Typical Cause | Owner Action |
| --- | --- | --- | --- |
| `received` | Event accepted and persisted. | Webhook or scheduled pull created event. | No action unless stuck. |
| `queued` | Waiting for worker. | Normal backlog or paused worker. | Monitor queue age. |
| `in_progress` | Worker has claimed event. | Normal processing. | Investigate only if lock exceeds threshold. |
| `matched` | Indoor context resolved. | Valid crosswalk or deterministic match. | No action. |
| `published` | ArcGIS layer updated. | Successful add/update. | No action. |
| `writeback_complete` | Approved ServiceNow fields updated. | Successful write-back. | No action. |
| `needs_review` | Data-quality review required. | Missing/ambiguous location, duplicate room, retired asset. | GIS/ITSM steward corrects data or alias. |
| `retry_scheduled` | Transient failure will retry later. | Timeout, throttling, token refresh. | Monitor retry count. |
| `failed_permanently` | Automatic processing stopped. | Permission failure, schema mismatch, repeated error. | Support owner reviews and requeues manually. |
| `suppressed` | Event intentionally ignored. | Non-spatial ticket, excluded state, unsupported location. | Review suppression rules periodically. |
