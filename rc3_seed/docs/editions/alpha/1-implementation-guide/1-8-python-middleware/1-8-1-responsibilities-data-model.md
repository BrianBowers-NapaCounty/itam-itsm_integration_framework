```{image} /_images/symbol-pythonlogo2.png
:alt: Middleware Responsibilities and Internal Data Model
:width: 64px
:class: page-symbol
```

# Middleware Responsibilities and Internal Data Model

## Middleware responsibilities

| Component | Responsibility | Failure mode | Control |
| --- | --- | --- | --- |
| Flask receiver | Accept and validate inbound ServiceNow events. | Forged, duplicated, or malformed event. | Signature validation, schema validation, idempotency. |
| Queue | Separate event receipt from long processing. | Queue backlog or lost event. | Durable storage, claimed/leased rows, status transitions. |
| Worker | Fetch full records, call APIs, apply rules, update layers. | Partial update or timeout. | Transactions where possible, retry/backoff, compensation logic. |
| Crosswalk engine | Resolve ServiceNow IDs to ArcGIS IDs. | Bad or stale mapping. | Confidence score, review queue, reconciliation. |
| ArcGIS client | Query and edit Portal/feature layers. | Layer schema drift, permission error, edit failure. | Schema validation, service health checks, edit result inspection. |
| ServiceNow client | GET/PATCH records and add work notes. | Auth failure, rate limiting, unexpected schema. | Scoped account, pagination, rate controls, schema tests. |

## Middleware internal data model

Middleware storage ERD

Code / configuration

Diagram

```mermaid
erDiagram
    integration_event_queue {
        string event_id PK
        string source_system
        string source_table
        string source_sys_id
        string event_type
        string operation
        datetime received_at
        string status
        int retry_count
        string payload_json
        string idempotency_key
    }

    sync_state {
        string sync_name PK
        datetime last_successful_run
        datetime last_polled_timestamp
        string watermark
        boolean enabled
    }

    crosswalk_location {
        string sn_location_sys_id PK
        string building_code
        string floor_code
        string room_code
        string arcgis_facility_id
        string arcgis_level_id
        string arcgis_unit_id
        float confidence_score
        string match_status
    }

    crosswalk_asset {
        string sn_ci_sys_id PK
        string asset_tag
        string serial_number
        string arcgis_asset_id
        string globalid
        string match_status
    }

    processing_log {
        string log_id PK
        string event_id FK
        string level
        string message
        datetime created_at
        string correlation_id
    }

    retry_deadletter {
        string event_id PK
        string error_type
        datetime next_retry_at
        int retry_count
        string last_error
        boolean dead_letter
    }

    integration_event_queue ||--o{ processing_log : produces
    integration_event_queue ||--o| retry_deadletter : may_fail_to
    integration_event_queue }o--o| crosswalk_location : resolves_location
    integration_event_queue }o--o| crosswalk_asset : resolves_asset
```
