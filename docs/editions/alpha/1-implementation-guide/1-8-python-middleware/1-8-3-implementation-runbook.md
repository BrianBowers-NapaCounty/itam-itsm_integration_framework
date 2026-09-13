```{image} /_images/symbol-pythonlogo2.png
:alt: Middleware Implementation Runbook
:width: 64px
:class: page-symbol
```

# Middleware Implementation Runbook

This runbook describes a practical implementation pattern for a Python bridge between ServiceNow and ArcGIS Indoors. A production-ready bridge should separate event receipt, queueing, record lookup, normalization, indoor-location matching, ArcGIS publishing, ServiceNow write-back, logging, retry, and reconciliation. This separation is operationally important because each step fails differently, uses different permissions, and needs separate monitoring.

**Implementation assets**

Production Python middleware scripts, maintenance utilities, detailed runbooks, extended checklists, cheat sheets, budget calculators, presentation templates, and deployment instructions will be maintained through the public Capybara Read the Docs project.

<https://capybara-framework.readthedocs.io/en/latest/>

## Recommended Repository Layout

Project layout

Project layout / configuration

```
capybara-middleware/ app/ __init__.py routes/ health.py admin.py servicenow_events.py clients/ servicenow_client.py arcgis_client.py services/ ingest.py fetch_context.py normalize.py location_match.py transform.py publish_arcgis.py writeback.py reconcile.py models/ queue_models.py log_models.py crosswalk_models.py config/ settings.py field_maps.yaml layer_maps.yaml scripts/ run_worker.py scheduled_pull.py reconcile_all.py rotate_logs.py export_reports.py tests/ test_location_match.py test_transform.py test_idempotency.py docs/ runbook.md deployment.md troubleshooting.md requirements.txt .env.example
```

## Configuration and Secrets

Do not hard-code ServiceNow credentials, ArcGIS credentials, client secrets, webhook tokens, or database passwords. Store runtime settings outside the repository and use an approved secrets mechanism for production. The application should refuse to start when required secrets or endpoints are missing.

Project layout

Project layout / configuration

```
# .env.example
APP_ENV=production
LOG_LEVEL=INFO
DATABASE_URL=mssql+pyodbc://...
SERVICENOW_INSTANCE=https://example.service-now.com
SERVICENOW_CLIENT_ID=...
SERVICENOW_CLIENT_SECRET=...
SERVICENOW_WEBHOOK_SHARED_SECRET=...
ARCGIS_PORTAL_URL=https://gis.example.gov/portal
ARCGIS_CLIENT_ID=...
ARCGIS_CLIENT_SECRET=...
ARCGIS_INCIDENT_LAYER_ITEM_ID=...
ARCGIS_ASSET_LAYER_ITEM_ID=...
WEBHOOK_ALLOWED_IPS=...
```

## Minimum Middleware Tables

| Table | Purpose | Typical Fields |
| --- | --- | --- |
| `integration_event_queue` | Durable queue of inbound and scheduled work items. | `event_id``source_table``source_sys_id``event_type``status``retry_count``next_attempt_at``last_error` |
| `sync_log` | Step-by-step audit trail. | `log_id``event_id``step``status``message``duration_ms``created_at` |
| `id_crosswalk` | Persistent mapping between ServiceNow and ArcGIS identifiers. | `sn_table``sn_sys_id``arcgis_layer``arcgis_globalid``facility_id``level_id``unit_id` |
| `location_alias` | Governed aliases for building, floor, room, desk, and shared-space labels. | `source_value``normalized_value``match_type``confidence``is_active` |
| `reconciliation_result` | Stores comparison results from scheduled audits. | `run_id``entity_type``source_count``target_count``exception_count``summary_json` |

## Webhook Event Intake

The webhook endpoint should authenticate the request, validate the payload shape, deduplicate the event, write it to the queue, and return quickly. Slower downstream work belongs in a worker process.

Python

Python implementation example

```
@bp.post("/servicenow/event")
def receive_event(): raw_body = request.get_data() signature = request.headers.get("X-Capybara-Signature", "") validate_signature(raw_body, signature) payload = request.get_json(force=True) event_id = queue_repo.enqueue( source_system="servicenow", source_table=payload["table"], source_sys_id=payload["sys_id"], event_type=payload["event_type"], payload=payload, ) return {"accepted": True, "event_id": event_id}, 202
```

## Worker Processing Pipeline

1. **Claim the event.** Lock one queue row so two workers do not process the same event.
2. **Fetch full context from ServiceNow.** Retrieve the ticket, task, asset, CI, caller, assigned user, assignment group, and location records needed for the workflow.
3. **Normalize values.** Standardize building codes, floor labels, room numbers, timestamps, status values, priority values, and asset identifiers.
4. **Resolve indoor context.** Match the record to a facility, level, unit, room, cubicle, shared space, or zone in ArcGIS Indoors.
5. **Transform to ArcGIS attributes.** Build the target feature attributes and geometry reference required by the operational layer.
6. **Upsert the ArcGIS feature.** Query by integration key and update when found; create only when no existing feature exists.
7. **Write back approved context.** Return map URLs, place IDs, unit IDs, confidence scores, or short work notes to ServiceNow.
8. **Finalize or retry.** Record the result, schedule retry for transient failures, or route data-quality issues to exception review.

Python

Python implementation example

```
def process_event(event): record = servicenow_client.fetch_record_with_context( table=event.source_table, sys_id=event.source_sys_id, ) normalized = normalize_record(record) match = location_matcher.resolve(normalized) if not match.is_usable: raise NeedsReviewError(match.reason) feature_payload = transform_to_arcgis(normalized, match) arcgis_result = arcgis_client.upsert_feature( layer_name="Operational_Incidents", integration_key=event.source_sys_id, attributes=feature_payload["attributes"], geometry=feature_payload["geometry"], ) writeback_service.update_servicenow( table=event.source_table, sys_id=event.source_sys_id, map_url=arcgis_result.get("map_url"), unit_id=match.unit_id, facility_id=match.facility_id, level_id=match.level_id, confidence_score=match.confidence, )
```

## Location Matching Rules and Confidence

Location matching should prefer deterministic identifiers. Fuzzy matching should be treated as an exception-support mechanism, not the primary production rule.

| Priority | Rule | Example | Confidence |
| --- | --- | --- | --- |
| 1 | Direct place or unit ID | `u_arcgis_unit_id` on the ticket | Very high |
| 2 | Crosswalk table match | `cmn_location.sys_id → unit_id` | Very high |
| 3 | Facility + level + room code | `Main Campus / 03 / 3-214` | High |
| 4 | Asset-derived location | Mapped printer already linked to known room | Medium to high |
| 5 | Governed alias table | `“3rd floor printer area”`official space ID | Medium |
| 6 | Fuzzy candidate review | Approximate room or space label | Low; review required |

## ArcGIS Upsert Pattern

For most Capybara workflows, the integration should update derived operational layers rather than overwrite authoritative Indoors reference layers. Facilities, levels, units, and routes remain governed GIS content. Tickets, work orders, deployment tasks, and incident hotspots are operational overlays.

Python

Python implementation example

```
def upsert_feature(layer, integration_key, attributes, geometry): existing = layer.query( where=f"integration_key = '{integration_key}'", out_fields="objectid,globalid", return_geometry=False, ) if existing.features: object_id = existing.features[0].attributes["objectid"] attributes["objectid"] = object_id return layer.edit_features( updates=[{"attributes": attributes, "geometry": geometry}] ) attributes["integration_key"] = integration_key return layer.edit_features( adds=[{"attributes": attributes, "geometry": geometry}] )
```

## ServiceNow Write-Back Pattern

Write-back should be limited and purposeful. Good write-back fields include map URL, matched place ID, facility/level/unit identifiers, match confidence, and a short integration note. Do not overwrite authoritative ITSM/ITAM workflow state unless that behavior has been explicitly approved.

REST / API

REST write-back example

```
PATCH /api/now/table/incident/{sys_id} { "u_arcgis_map_url": "https://gis.example.gov/portal/apps/...", "u_arcgis_facility_id": "MAIN", "u_arcgis_level_id": "03", "u_arcgis_unit_id": "ROOM_3_214", "u_arcgis_match_confidence": "0.98", "work_notes": "Capybara linked this incident to Main Campus / Level 03 / Room 3-214."
}
```

## Error Handling and Retry Policy

| Error Type | Retry? | Recommended Response |
| --- | --- | --- |
| ServiceNow timeout or network failure | Yes | Retry with exponential backoff and jitter. |
| ArcGIS token expiration | Yes | Refresh session and retry once or twice. |
| Permission denied | No | Stop affected process and alert the administrator. |
| Missing location or ambiguous room | No automatic retry | Send to exception review or data correction. |
| Layer schema mismatch | No | Stop updates to the affected layer and notify GIS maintainers. |
| Duplicate crosswalk | No | Route to reconciliation report and manual correction. |

## Windows / IIS Deployment Pattern

1. Provision a dedicated host or controlled shared application server.
2. Create a dedicated service account with least-privilege permissions.
3. Install a supported Python runtime and isolated virtual environment.
4. Configure IIS bindings, TLS certificates, request-size limits, and reverse proxy rules.
5. Store credentials in an approved secrets mechanism.
6. Deploy the Flask application and verify `/health`.
7. Run worker processing as a separate service or scheduled task.
8. Enable structured logging, alerting, backups, credential rotation, and reconciliation reporting.

## Operational Acceptance Criteria

- Unauthorized or malformed events are rejected and logged.
- Accepted events are persisted before downstream processing begins.
- Idempotent processing prevents duplicate ArcGIS features and duplicate write-back.
- Location matching produces a confidence score and reason code.
- Every event can be traced from receipt to completion through logs and queue state.
- Administrators can manually requeue failed records without editing source data directly.
- The support runbook covers restart, credential rotation, schema change, and emergency disablement procedures.
