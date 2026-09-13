```{image} /_images/symbol-api.png
:alt: Scripts Architecture
:width: 64px
:class: page-symbol
```

# Scripts Architecture

How the reference implementation separates canonical models, connectors, ArcGIS access, reusable services, and operational entry points. The architecture is deliberately platform-agnostic above the connector layer.

```text
capybara/
├── core/
├── connectors/
├── arcgis/
├── analytics/
├── services/
└── extensions/
```

## `models.py`

**Role:** Canonical data models.

**Download:** {download}`models.py <files/capybara/core/models.py>`

## `connector.py`

**Role:** ITSM connector contract.

**Download:** {download}`connector.py <files/capybara/core/connector.py>`

## `registry.py`

**Role:** Connector factory.

**Download:** {download}`registry.py <files/capybara/connectors/registry.py>`

## `client.py`

**Role:** ArcGIS API for Python connection helper.

**Download:** {download}`client.py <files/capybara/arcgis/client.py>`

## `reconciliation.py`

**Role:** Reusable reconciliation service.

**Download:** {download}`reconciliation.py <files/capybara/services/reconciliation.py>`

## `reporting.py`

**Role:** Reusable reporting service.

**Download:** {download}`reporting.py <files/capybara/services/reporting.py>`

