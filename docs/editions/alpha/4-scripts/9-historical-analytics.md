```{image} /_images/symbol-technicalnote.png
:alt: Historical Analytics & Hosted Tables
:width: 64px
:class: page-symbol
```

# Historical Analytics & Hosted Tables

Persistent ArcGIS Online/Enterprise hosted-table history for snapshots, events, reconciliation, and health telemetry.

## Category inventory

| File | Type | Maturity |
| --- | --- | --- |
| `bootstrap_analytics_service.py` | PY | ARC-GIS-CONFIGURED |
| `capture_daily_snapshot.py` | PY | DEMO-RUNNABLE |
| `backfill_metric_snapshots.py` | PY | PSEUDOCODE-HEAVY |
| `publish_event_history.py` | PY | PSEUDOCODE-HEAVY |
| `publish_sync_health.py` | PY | ARC-GIS-CONFIGURED |
| `publish_reconciliation_history.py` | PY | ARC-GIS-CONFIGURED |
| `analytics_bootstrap.ipynb` | IPYNB | DEMO-RUNNABLE |

## `bootstrap_analytics_service.py`

Create/verify the Capybara hosted analytics tables.  If analytics.item_id is blank, this script attempts to create an empty hosted feature service using the current GIS account, then adds the standard tables. Creating hosted services requires appropriate privileges.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | ARC-GIS-CONFIGURED |
| Suggested use | Ad-hoc / demonstration. |
| External writes | Read/analysis-oriented; no external write detected. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

**Configuration keys referenced:** `analytics.chunk_size`, `analytics.folder`, `analytics.item_id`, `analytics.service_name`.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/09_historical_analytics/bootstrap_analytics_service.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`bootstrap_analytics_service.py <files/09_historical_analytics/bootstrap_analytics_service.py>`
## `capture_daily_snapshot.py`

Capture current canonical ITSM/ITAM state into historical analytics tables.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | DEMO-RUNNABLE |
| Suggested use | Suitable for scheduled execution after local review; cadence depends on the workflow. |
| External writes | Read/analysis-oriented; no external write detected. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/09_historical_analytics/capture_daily_snapshot.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`capture_daily_snapshot.py <files/09_historical_analytics/capture_daily_snapshot.py>`
## `backfill_metric_snapshots.py`

Backfill chart-ready historical metric rows from externally supplied period extracts.  A production backfill normally needs historical ITSM exports because current tickets cannot reconstruct prior point-in-time backlog accurately. This script therefore demonstrates the storage contract and refuses to fabricate history.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | PSEUDOCODE-HEAVY |
| Suggested use | Suitable for scheduled execution after local review; cadence depends on the workflow. |
| External writes | Read/analysis-oriented; no external write detected. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/09_historical_analytics/backfill_metric_snapshots.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`backfill_metric_snapshots.py <files/09_historical_analytics/backfill_metric_snapshots.py>`
## `publish_event_history.py`

Publish normalized ITSM change events from an event JSON file.  Expected JSON fields: event_utc,event_type,record_type,record_id,public_id, field_name,old_value,new_value,location_id,asset_id,correlation.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | PSEUDOCODE-HEAVY |
| Suggested use | Ad-hoc / demonstration. |
| External writes | May write to ArcGIS/analytics storage when configured. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/09_historical_analytics/publish_event_history.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`publish_event_history.py <files/09_historical_analytics/publish_event_history.py>`
## `publish_sync_health.py`

Sample connector/ArcGIS health and write one Sync_Health history row.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | ARC-GIS-CONFIGURED |
| Suggested use | Suitable for scheduled execution after local review; cadence depends on the workflow. |
| External writes | May write to ArcGIS/analytics storage when configured. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/09_historical_analytics/publish_sync_health.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`publish_sync_health.py <files/09_historical_analytics/publish_sync_health.py>`
## `publish_reconciliation_history.py`

Run source-vs-operational reconciliation and persist issues historically.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | ARC-GIS-CONFIGURED |
| Suggested use | Ad-hoc / demonstration. |
| External writes | May write to ArcGIS/analytics storage when configured. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

**Configuration keys referenced:** `arcgis.operational_item_id`, `arcgis.operational_layer_index`.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/09_historical_analytics/publish_reconciliation_history.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`publish_reconciliation_history.py <files/09_historical_analytics/publish_reconciliation_history.py>`
## `analytics_bootstrap.ipynb`

Explores the hosted-table schema, reporting windows, and a local SQLite demo store before any Portal/AGOL writes are enabled.

| Property | Value |
| --- | --- |
| Type | IPYNB |
| Maturity | DEMO-RUNNABLE |
| Suggested use | Ad-hoc / demonstration. |
| External writes | Read/analysis-oriented; no external write detected. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

### Output

Interactive tables/charts and optional exports produced by notebook cells.

### Example use

```text
Open `files/09_historical_analytics/analytics_bootstrap.ipynb` in Jupyter and run cells from top to bottom.
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`analytics_bootstrap.ipynb <files/09_historical_analytics/analytics_bootstrap.ipynb>`
