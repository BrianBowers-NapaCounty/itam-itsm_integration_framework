```{image} /_images/symbol-commandline2.png
:alt: Sample Configuration and SQL DDL
:width: 64px
:class: page-symbol
```

# Sample Configuration and SQL DDL

## Sample Configuration Files

**Configuration as controlled source**

Field maps, layer references, write-back rules, and thresholds should live in reviewed configuration files rather than being scattered across code.

### Sample YAML Layer and Field Map

```
layers:
  incidents:
    portal_url: "https://gis.example.gov/portal"
    item_id: "abc123"
    layer_name: "Operational_Incidents"
    integration_key: "integration_key"

field_maps:
  incident:
    sys_id: integration_key
    number: ticket_number
    short_description: summary
    priority: priority
    state: status
    sys_updated_on: source_updated_at

writeback:
  incident:
    enabled: true
    fields:
      u_arcgis_map_url: map_url
      u_arcgis_facility_id: facility_id
      u_arcgis_level_id: level_id
      u_arcgis_unit_id: unit_id
      u_arcgis_match_confidence: confidence

matching:
  confidence_thresholds:
    auto_writeback: 0.90
    publish_without_writeback: 0.70
    needs_review: 0.69
  rules:
    - direct_unit_id
    - location_crosswalk
    - facility_level_room
    - asset_existing_location
    - governed_alias
    - fuzzy_candidate_review
```

### Sample Environment Configuration

```
environments:
  dev:
    servicenow_instance: "https://dev.example.service-now.com"
    arcgis_portal: "https://gis-dev.example.gov/portal"
    writeback_enabled: false
  test:
    servicenow_instance: "https://test.example.service-now.com"
    arcgis_portal: "https://gis-test.example.gov/portal"
    writeback_enabled: true
  prod:
    servicenow_instance: "https://example.service-now.com"
    arcgis_portal: "https://gis.example.gov/portal"
    writeback_enabled: true
    require_hmac_signature: true
    require_ip_allowlist: true
```

## Sample SQL DDL

**Starter operational schema**

The following DDL illustrates the kind of state tables a middleware service needs. Production scripts should be versioned separately.

```
CREATE TABLE dbo.integration_event_queue (
    event_id UNIQUEIDENTIFIER NOT NULL PRIMARY KEY,
    source_system NVARCHAR(50) NOT NULL,
    source_table NVARCHAR(128) NOT NULL,
    source_sys_id NVARCHAR(128) NOT NULL,
    event_type NVARCHAR(128) NOT NULL,
    payload_json NVARCHAR(MAX) NULL,
    status NVARCHAR(50) NOT NULL DEFAULT 'queued',
    retry_count INT NOT NULL DEFAULT 0,
    next_attempt_at DATETIME2 NULL,
    locked_by NVARCHAR(128) NULL,
    locked_at DATETIME2 NULL,
    last_error NVARCHAR(MAX) NULL,
    created_at DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME(),
    updated_at DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME()
);

CREATE INDEX IX_event_queue_status_next
ON dbo.integration_event_queue (status, next_attempt_at, created_at);

CREATE TABLE dbo.sync_log (
    log_id BIGINT IDENTITY(1,1) PRIMARY KEY,
    event_id UNIQUEIDENTIFIER NULL,
    step_name NVARCHAR(128) NOT NULL,
    status NVARCHAR(50) NOT NULL,
    message NVARCHAR(MAX) NULL,
    source_table NVARCHAR(128) NULL,
    source_sys_id NVARCHAR(128) NULL,
    arcgis_layer NVARCHAR(256) NULL,
    arcgis_globalid NVARCHAR(128) NULL,
    duration_ms INT NULL,
    created_at DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME()
);

CREATE TABLE dbo.id_crosswalk (
    crosswalk_id BIGINT IDENTITY(1,1) PRIMARY KEY,
    sn_table NVARCHAR(128) NOT NULL,
    sn_sys_id NVARCHAR(128) NOT NULL,
    arcgis_layer NVARCHAR(256) NOT NULL,
    arcgis_globalid NVARCHAR(128) NULL,
    facility_id NVARCHAR(128) NULL,
    level_id NVARCHAR(128) NULL,
    unit_id NVARCHAR(128) NULL,
    is_active BIT NOT NULL DEFAULT 1,
    updated_at DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME(),
    CONSTRAINT UQ_crosswalk UNIQUE (sn_table, sn_sys_id, arcgis_layer)
);

CREATE TABLE dbo.location_alias (
    alias_id BIGINT IDENTITY(1,1) PRIMARY KEY,
    source_value NVARCHAR(512) NOT NULL,
    normalized_value NVARCHAR(512) NOT NULL,
    facility_id NVARCHAR(128) NULL,
    level_id NVARCHAR(128) NULL,
    unit_id NVARCHAR(128) NULL,
    match_type NVARCHAR(64) NOT NULL,
    confidence DECIMAL(5,4) NOT NULL,
    is_active BIT NOT NULL DEFAULT 1
);

CREATE TABLE dbo.reconciliation_result (
    run_id UNIQUEIDENTIFIER NOT NULL,
    result_id BIGINT IDENTITY(1,1) PRIMARY KEY,
    entity_type NVARCHAR(128) NOT NULL,
    source_count INT NULL,
    target_count INT NULL,
    exception_count INT NULL,
    summary_json NVARCHAR(MAX) NULL,
    created_at DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME()
);
```
