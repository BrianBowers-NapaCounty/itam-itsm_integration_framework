```{image} /_images/symbol-telescope.png
:alt: Advanced Analytics & Planning
:width: 64px
:class: page-symbol
```

# Advanced Analytics & Planning

Anomaly detection, SLA geography, procurement aging, refresh planning, custody exceptions, and workload balance.

## Category inventory

| File | Type | Maturity |
| --- | --- | --- |
| `detect_metric_anomalies.py` | PY | ARC-GIS-CONFIGURED |
| `procurement_hold_aging.py` | PY | DEMO-RUNNABLE |
| `sla_geography.py` | PY | DEMO-RUNNABLE |
| `refresh_wave_planner.py` | PY | DEMO-RUNNABLE |
| `asset_custody_anomalies.py` | PY | DEMO-RUNNABLE |
| `technician_workload_balance.py` | PY | DEMO-RUNNABLE |
| `anomaly_explorer.ipynb` | IPYNB | DEMO-RUNNABLE |
| `executive_trend_pack.ipynb` | IPYNB | DEMO-RUNNABLE |

## `detect_metric_anomalies.py`

Run robust MAD-based anomaly detection on one stored metric time series.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | ARC-GIS-CONFIGURED |
| Suggested use | Ad-hoc / demonstration. |
| External writes | Read/analysis-oriented; no external write detected. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

**Configuration keys referenced:** `analytics.example_metric`, `analytics.example_window`, `analytics.time_zone`.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/12_advanced_analytics/detect_metric_anomalies.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`detect_metric_anomalies.py <files/12_advanced_analytics/detect_metric_anomalies.py>`
## `procurement_hold_aging.py`

Bucket parts/equipment/procurement holds by age for management review.

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
python files/12_advanced_analytics/procurement_hold_aging.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`procurement_hold_aging.py <files/12_advanced_analytics/procurement_hold_aging.py>`
## `sla_geography.py`

Summarize current SLA-risk workload by location for later join to Indoors geometry.

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
python files/12_advanced_analytics/sla_geography.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`sla_geography.py <files/12_advanced_analytics/sla_geography.py>`
## `refresh_wave_planner.py`

Rank locations by replacement/deployment workload to help stage refresh waves.  A real implementation can add device age, warranty, model, security posture, department priority, floor adjacency, and technician capacity.

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
python files/12_advanced_analytics/refresh_wave_planner.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`refresh_wave_planner.py <files/12_advanced_analytics/refresh_wave_planner.py>`
## `asset_custody_anomalies.py`

Flag simple asset-custody conditions suitable for audit follow-up.

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
python files/12_advanced_analytics/asset_custody_anomalies.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`asset_custody_anomalies.py <files/12_advanced_analytics/asset_custody_anomalies.py>`
## `technician_workload_balance.py`

Compare active assigned workload by technician and assignment group.

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
python files/12_advanced_analytics/technician_workload_balance.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`technician_workload_balance.py <files/12_advanced_analytics/technician_workload_balance.py>`
## `anomaly_explorer.ipynb`

Uses median absolute deviation to flag unusually high/low metric observations without requiring a heavy forecasting library.

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
Open `files/12_advanced_analytics/anomaly_explorer.ipynb` in Jupyter and run cells from top to bottom.
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`anomaly_explorer.ipynb <files/12_advanced_analytics/anomaly_explorer.ipynb>`
## `executive_trend_pack.ipynb`

Starter notebook for building several management trend visuals from the persistent analytics store.

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
Open `files/12_advanced_analytics/executive_trend_pack.ipynb` in Jupyter and run cells from top to bottom.
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`executive_trend_pack.ipynb <files/12_advanced_analytics/executive_trend_pack.ipynb>`
