```{image} /_images/symbol-rest.png
:alt: Connector Lab
:width: 64px
:class: page-symbol
```

# Connector Lab

Normalization experiments across ServiceNow, TeamDynamix, Cherwell, and mock data.

## Category inventory

| File | Type | Maturity |
| --- | --- | --- |
| `connector_normalization_lab.ipynb` | IPYNB | DEMO-RUNNABLE |

## `connector_normalization_lab.ipynb`

Documents the canonical contract. Use it to compare how ServiceNow, TeamDynamix, or Cherwell fields map into the same Ticket/Asset objects.

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
Open `files/08_connector_lab/connector_normalization_lab.ipynb` in Jupyter and run cells from top to bottom.
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`connector_normalization_lab.ipynb <files/08_connector_lab/connector_normalization_lab.ipynb>`
