```{image} /_images/symbol-microscope2.png
:alt: Testing & Maintenance
:width: 64px
:class: page-symbol
```

# Testing & Maintenance

Smoke tests, reconciliation, orphan detection, controlled repair, and failed-event replay.

## Category inventory

| File | Type | Maturity |
| --- | --- | --- |
| `connector_smoke_test.py` | PY | DEMO-RUNNABLE |
| `reconcile_operational_layer.py` | PY | ARC-GIS-CONFIGURED |
| `find_orphaned_records.py` | PY | ARC-GIS-CONFIGURED |
| `repair_safe_drift.py` | PY | DEMO-RUNNABLE |
| `replay_failed_records.py` | PY | PSEUDOCODE-HEAVY |
| `maintenance_workbench.ipynb` | IPYNB | DEMO-RUNNABLE |

## `connector_smoke_test.py`

Exercise connector health/read paths without performing writes.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | DEMO-RUNNABLE |
| Suggested use | Ad-hoc / demonstration. |
| External writes | Read/analysis-oriented; no external write detected. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/03_testing_maintenance/connector_smoke_test.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`connector_smoke_test.py <files/03_testing_maintenance/connector_smoke_test.py>`
## `reconcile_operational_layer.py`

Compare ITSM tickets with the ArcGIS operational layer and export drift.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | ARC-GIS-CONFIGURED |
| Suggested use | Ad-hoc / demonstration. |
| External writes | Writes report/output files locally. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

**Configuration keys referenced:** `arcgis.operational_item_id`, `arcgis.operational_layer_index`.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/03_testing_maintenance/reconcile_operational_layer.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`reconcile_operational_layer.py <files/03_testing_maintenance/reconcile_operational_layer.py>`
## `find_orphaned_records.py`

Find ArcGIS operational records whose source ITSM ID is absent from the extract.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | ARC-GIS-CONFIGURED |
| Suggested use | Ad-hoc / demonstration. |
| External writes | Writes report/output files locally. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

**Configuration keys referenced:** `arcgis.operational_item_id`, `arcgis.operational_layer_index`.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/03_testing_maintenance/find_orphaned_records.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`find_orphaned_records.py <files/03_testing_maintenance/find_orphaned_records.py>`
## `repair_safe_drift.py`

Illustrate conservative auto-repair: only issues explicitly marked safe are eligible.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | DEMO-RUNNABLE |
| Suggested use | Ad-hoc / demonstration. |
| External writes | Read/analysis-oriented; no external write detected. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/03_testing_maintenance/repair_safe_drift.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`repair_safe_drift.py <files/03_testing_maintenance/repair_safe_drift.py>`
## `replay_failed_records.py`

Skeleton for replaying a reviewed dead-letter/error export.  A production queue should keep event IDs, attempts, timestamps, error classes, source record IDs, and payload hashes. This demo only documents the replay seam.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | PSEUDOCODE-HEAVY |
| Suggested use | Ad-hoc / demonstration. |
| External writes | Read/analysis-oriented; no external write detected. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/03_testing_maintenance/replay_failed_records.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`replay_failed_records.py <files/03_testing_maintenance/replay_failed_records.py>`
## `maintenance_workbench.ipynb`

Explores canonical ITSM records and demonstrates reconciliation logic. Attach a configured ArcGIS operational layer to compare live records.

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
Open `files/03_testing_maintenance/maintenance_workbench.ipynb` in Jupyter and run cells from top to bottom.
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`maintenance_workbench.ipynb <files/03_testing_maintenance/maintenance_workbench.ipynb>`
