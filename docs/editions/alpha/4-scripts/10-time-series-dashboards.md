```{image} /_images/symbol-screen.png
:alt: Time-Series & Dashboard Data
:width: 64px
:class: page-symbol
```

# Time-Series & Dashboard Data

Reusable reporting windows, time-series extraction, period comparison, and dashboard-ready datasets.

## Category inventory

| File | Type | Maturity |
| --- | --- | --- |
| `list_reporting_windows.py` | PY | DEMO-RUNNABLE |
| `export_metric_series.py` | PY | ARC-GIS-CONFIGURED |
| `chart_metric_series.py` | PY | ARC-GIS-CONFIGURED |
| `compare_reporting_periods.py` | PY | DEMO-RUNNABLE |
| `materialize_period_summaries.py` | PY | DEMO-RUNNABLE |
| `dashboard_dataset_inventory.py` | PY | DEMO-RUNNABLE |
| `period_comparison_workbench.ipynb` | IPYNB | DEMO-RUNNABLE |
| `time_series_workbench.ipynb` | IPYNB | DEMO-RUNNABLE |

## `list_reporting_windows.py`

Print the standard rolling/calendar reporting windows used by Capybara.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | DEMO-RUNNABLE |
| Suggested use | Ad-hoc / demonstration. |
| External writes | Read/analysis-oriented; no external write detected. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

**Configuration keys referenced:** `analytics.time_zone`.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/10_time_series_dashboards/list_reporting_windows.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`list_reporting_windows.py <files/10_time_series_dashboards/list_reporting_windows.py>`
## `export_metric_series.py`

Export a hosted/local metric time series for a chosen reporting window.

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
python files/10_time_series_dashboards/export_metric_series.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`export_metric_series.py <files/10_time_series_dashboards/export_metric_series.py>`
## `chart_metric_series.py`

Generate a PNG time-series chart from historical Metric_Snapshots.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | ARC-GIS-CONFIGURED |
| Suggested use | Ad-hoc / demonstration. |
| External writes | Writes report/output files locally. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

**Configuration keys referenced:** `analytics.example_metric`, `analytics.example_window`, `analytics.time_zone`.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/10_time_series_dashboards/chart_metric_series.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`chart_metric_series.py <files/10_time_series_dashboards/chart_metric_series.py>`
## `compare_reporting_periods.py`

Demonstrate period-over-period comparisons from stored metric rows.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | DEMO-RUNNABLE |
| Suggested use | Ad-hoc / demonstration. |
| External writes | Read/analysis-oriented; no external write detected. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

**Configuration keys referenced:** `analytics.time_zone`.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/10_time_series_dashboards/compare_reporting_periods.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`compare_reporting_periods.py <files/10_time_series_dashboards/compare_reporting_periods.py>`
## `materialize_period_summaries.py`

Materialize standard period rows for dashboard selectors.  This reference implementation records window boundaries; production deployments should query/aggregate Metric_Snapshots for each metric/dimension and fill values.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | DEMO-RUNNABLE |
| Suggested use | Ad-hoc / demonstration. |
| External writes | May write to ArcGIS/analytics storage when configured. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

**Configuration keys referenced:** `analytics.time_zone`.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/10_time_series_dashboards/materialize_period_summaries.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`materialize_period_summaries.py <files/10_time_series_dashboards/materialize_period_summaries.py>`
## `dashboard_dataset_inventory.py`

Print suggested ArcGIS Dashboard/Experience Builder data-source usage.

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
python files/10_time_series_dashboards/dashboard_dataset_inventory.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`dashboard_dataset_inventory.py <files/10_time_series_dashboards/dashboard_dataset_inventory.py>`
## `period_comparison_workbench.ipynb`

Provides side-by-side period definitions for week/month/quarter/year comparisons and a place to compute changes from hosted metric history.

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
Open `files/10_time_series_dashboards/period_comparison_workbench.ipynb` in Jupyter and run cells from top to bottom.
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`period_comparison_workbench.ipynb <files/10_time_series_dashboards/period_comparison_workbench.ipynb>`
## `time_series_workbench.ipynb`

Queries Metric_Snapshots for a selected period, charts values, and prepares the same series for ArcGIS Dashboards or external reporting.

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
Open `files/10_time_series_dashboards/time_series_workbench.ipynb` in Jupyter and run cells from top to bottom.
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`time_series_workbench.ipynb <files/10_time_series_dashboards/time_series_workbench.ipynb>`
