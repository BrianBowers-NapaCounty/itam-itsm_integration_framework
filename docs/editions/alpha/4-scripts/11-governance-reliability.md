```{image} /_images/symbol-checkmark2.png
:alt: Analytics Governance & Reliability
:width: 64px
:class: page-symbol
```

# Analytics Governance & Reliability

Schema validation, retention, capture-gap detection, deduplication guidance, and data-quality scorecards.

## Category inventory

| File | Type | Maturity |
| --- | --- | --- |
| `validate_analytics_schema.py` | PY | ARC-GIS-CONFIGURED |
| `audit_snapshot_gaps.py` | PY | PSEUDOCODE-HEAVY |
| `retention_cleanup.py` | PY | ARC-GIS-CONFIGURED |
| `deduplicate_snapshot_rows.py` | PY | DEMO-RUNNABLE |
| `publish_data_quality_score.py` | PY | DEMO-RUNNABLE |
| `data_quality_scorecard.ipynb` | IPYNB | DEMO-RUNNABLE |

## `validate_analytics_schema.py`

Validate required hosted analytics table names and fields.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | ARC-GIS-CONFIGURED |
| Suggested use | Ad-hoc / demonstration. |
| External writes | Read/analysis-oriented; no external write detected. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/11_governance_reliability/validate_analytics_schema.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`validate_analytics_schema.py <files/11_governance_reliability/validate_analytics_schema.py>`
## `audit_snapshot_gaps.py`

Detect missing daily-capture dates in an exported/local Analytics_Runs history.

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
python files/11_governance_reliability/audit_snapshot_gaps.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`audit_snapshot_gaps.py <files/11_governance_reliability/audit_snapshot_gaps.py>`
## `retention_cleanup.py`

Preview retention cutoffs; destructive deletion requires explicit local implementation approval.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | ARC-GIS-CONFIGURED |
| Suggested use | Ad-hoc / demonstration. |
| External writes | Contains guarded destructive-maintenance capability. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/11_governance_reliability/retention_cleanup.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`retention_cleanup.py <files/11_governance_reliability/retention_cleanup.py>`
## `deduplicate_snapshot_rows.py`

Document duplicate-snapshot detection keys without automatically deleting records.

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
python files/11_governance_reliability/deduplicate_snapshot_rows.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`deduplicate_snapshot_rows.py <files/11_governance_reliability/deduplicate_snapshot_rows.py>`
## `publish_data_quality_score.py`

Compute and persist a governance/data-quality score snapshot.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | DEMO-RUNNABLE |
| Suggested use | Ad-hoc / demonstration. |
| External writes | May write to ArcGIS/analytics storage when configured. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/11_governance_reliability/publish_data_quality_score.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`publish_data_quality_score.py <files/11_governance_reliability/publish_data_quality_score.py>`
## `data_quality_scorecard.ipynb`

Calculates a reference governance score from location, assignment, asset-link, known-location, and duplicate-ID quality indicators.

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
Open `files/11_governance_reliability/data_quality_scorecard.ipynb` in Jupyter and run cells from top to bottom.
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`data_quality_scorecard.ipynb <files/11_governance_reliability/data_quality_scorecard.ipynb>`
