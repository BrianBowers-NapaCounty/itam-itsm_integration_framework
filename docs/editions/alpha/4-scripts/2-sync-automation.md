```{image} /_images/symbol-arrow2.png
:alt: Synchronization & Automation
:width: 64px
:class: page-symbol
```

# Synchronization & Automation

Scheduled pulls, operational-layer synchronization, asset publishing, and ITSM write-back patterns.

## Category inventory

| File | Type | Maturity |
| --- | --- | --- |
| `incremental_ticket_sync.py` | PY | ARC-GIS-CONFIGURED |
| `sync_assets_to_operational_layer.py` | PY | ARC-GIS-CONFIGURED |
| `scheduled_pull.py` | PY | DEMO-RUNNABLE |
| `writeback_map_context.py` | PY | DEMO-RUNNABLE |
| `sync_walkthrough.ipynb` | IPYNB | DEMO-RUNNABLE |

## `incremental_ticket_sync.py`

Pull recently updated ITSM tickets and upsert an ArcGIS operational layer.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | ARC-GIS-CONFIGURED |
| Suggested use | Suitable for scheduled execution after local review; cadence depends on the workflow. |
| External writes | May write to ArcGIS/analytics storage when configured. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

**Configuration keys referenced:** `arcgis.operational_item_id`, `arcgis.operational_layer_index`, `sync.lookback_minutes`.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/02_sync_automation/incremental_ticket_sync.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`incremental_ticket_sync.py <files/02_sync_automation/incremental_ticket_sync.py>`
## `sync_assets_to_operational_layer.py`

Demonstrate asset-to-ArcGIS attribute synchronization with safe dry-run behavior.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | ARC-GIS-CONFIGURED |
| Suggested use | Suitable for scheduled execution after local review; cadence depends on the workflow. |
| External writes | May write to ArcGIS/analytics storage when configured. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

**Configuration keys referenced:** `arcgis.asset_item_id`, `arcgis.asset_layer_index`.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/02_sync_automation/sync_assets_to_operational_layer.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`sync_assets_to_operational_layer.py <files/02_sync_automation/sync_assets_to_operational_layer.py>`
## `scheduled_pull.py`

A minimal polling-loop example suitable for Task Scheduler wrapper usage.  Production deployments should normally let an external scheduler invoke a single iteration rather than keeping an endless notebook/kernel process alive.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | DEMO-RUNNABLE |
| Suggested use | Suitable for scheduled execution after local review; cadence depends on the workflow. |
| External writes | Read/analysis-oriented; no external write detected. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

**Configuration keys referenced:** `sync.lookback_minutes`.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/02_sync_automation/scheduled_pull.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`scheduled_pull.py <files/02_sync_automation/scheduled_pull.py>`
## `writeback_map_context.py`

Demonstrate writing a map/place reference back to the ITSM ticket.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | DEMO-RUNNABLE |
| Suggested use | Suitable for scheduled execution after local review; cadence depends on the workflow. |
| External writes | May write back to the ITSM platform when dry-run is disabled. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

**Configuration keys referenced:** `writeback.example_map_url`.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/02_sync_automation/writeback_map_context.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`writeback_map_context.py <files/02_sync_automation/writeback_map_context.py>`
## `sync_walkthrough.ipynb`

Walks through normalization and the ArcGIS upsert payload without committing edits.

| Property | Value |
| --- | --- |
| Type | IPYNB |
| Maturity | DEMO-RUNNABLE |
| Suggested use | Suitable for scheduled execution after local review; cadence depends on the workflow. |
| External writes | May write to ArcGIS/analytics storage when configured. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

### Output

Interactive tables/charts and optional exports produced by notebook cells.

### Example use

```text
Open `files/02_sync_automation/sync_walkthrough.ipynb` in Jupyter and run cells from top to bottom.
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`sync_walkthrough.ipynb <files/02_sync_automation/sync_walkthrough.ipynb>`
