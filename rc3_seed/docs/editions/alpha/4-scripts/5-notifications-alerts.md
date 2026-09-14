```{image} /_images/symbol-exclamation2.png
:alt: Notifications & Alerts
:width: 64px
:class: page-symbol
```

# Notifications & Alerts

Management and maintainer alerts for loss, backlog, procurement delays, stale work, and integration failures.

## Category inventory

| File | Type | Maturity |
| --- | --- | --- |
| `alert_missing_assets.py` | PY | DEMO-RUNNABLE |
| `alert_stale_unassigned_tickets.py` | PY | DEMO-RUNNABLE |
| `alert_parts_on_order.py` | PY | DEMO-RUNNABLE |
| `alert_failed_sync.py` | PY | PSEUDOCODE-HEAVY |
| `manager_daily_digest.py` | PY | DEMO-RUNNABLE |
| `alert_preview.ipynb` | IPYNB | DEMO-RUNNABLE |

## `alert_missing_assets.py`

Email/preview an alert when assets are flagged missing, lost, or stolen.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | DEMO-RUNNABLE |
| Suggested use | Ad-hoc / demonstration. |
| External writes | May send email when SMTP is enabled. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

**Configuration keys referenced:** `smtp.enabled`.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/05_notifications_alerts/alert_missing_assets.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`alert_missing_assets.py <files/05_notifications_alerts/alert_missing_assets.py>`
## `alert_stale_unassigned_tickets.py`

Escalate active tickets that remain unassigned beyond a configured interval.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | DEMO-RUNNABLE |
| Suggested use | Ad-hoc / demonstration. |
| External writes | Read/analysis-oriented; no external write detected. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

**Configuration keys referenced:** `thresholds.stale_unassigned_hours`.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/05_notifications_alerts/alert_stale_unassigned_tickets.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`alert_stale_unassigned_tickets.py <files/05_notifications_alerts/alert_stale_unassigned_tickets.py>`
## `alert_parts_on_order.py`

Alert managers about tickets held for parts/equipment/procurement longer than threshold.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | DEMO-RUNNABLE |
| Suggested use | Ad-hoc / demonstration. |
| External writes | May send email when SMTP is enabled. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

**Configuration keys referenced:** `smtp.enabled`, `thresholds.parts_hold_days`.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/05_notifications_alerts/alert_parts_on_order.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`alert_parts_on_order.py <files/05_notifications_alerts/alert_parts_on_order.py>`
## `alert_failed_sync.py`

Template for notifying maintainers when a reconciliation/export contains high-severity drift.

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
python files/05_notifications_alerts/alert_failed_sync.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`alert_failed_sync.py <files/05_notifications_alerts/alert_failed_sync.py>`
## `manager_daily_digest.py`

Build one management digest instead of sending one message per exception.

| Property | Value |
| --- | --- |
| Type | PY |
| Maturity | DEMO-RUNNABLE |
| Suggested use | Suitable for scheduled execution after local review; cadence depends on the workflow. |
| External writes | Read/analysis-oriented; no external write detected. |

### Inputs and prerequisites

Canonical connector data and `config.toml`; some examples additionally require ArcGIS item/layer IDs.

**Configuration keys referenced:** `thresholds.parts_hold_days`, `thresholds.stale_unassigned_hours`.

### Output

Console output and/or files/hosted-table rows as described by the script.

### Example use

```text
python files/05_notifications_alerts/manager_daily_digest.py --config config.toml
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`manager_daily_digest.py <files/05_notifications_alerts/manager_daily_digest.py>`
## `alert_preview.ipynb`

Shows which records would trigger missing-asset, stale-unassigned, and parts/procurement-hold alerts before any SMTP delivery is enabled.

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
Open `files/05_notifications_alerts/alert_preview.ipynb` in Jupyter and run cells from top to bottom.
```

### Processing logic

1. Load the shared Capybara configuration and selected connector.
2. Normalize vendor records into canonical Capybara models.
3. Apply the category-specific selection, analysis, synchronization, or reporting logic.
4. Emit results through local files, ArcGIS tables/layers, ITSM write-back, or notification adapters as applicable.
5. Preserve dry-run or explicit safety controls before external writes.

### Production considerations

Treat this file as a reference implementation. Validate local field mappings, permissions, error handling, retention, scheduling, logging, and secrets management before production use.

**Download:** {download}`alert_preview.ipynb <files/05_notifications_alerts/alert_preview.ipynb>`
