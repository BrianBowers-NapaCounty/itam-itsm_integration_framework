```{image} /_images/symbol-api.png
:alt: ArcGIS Architecture Center Alignment
:width: 64px
:class: page-symbol
```

```{image} /_images/symbol-arcgisindoors.png
:alt: ArcGIS Architecture Center Alignment
:width: 150px
:class: page-logo
```

# ArcGIS Architecture Center Alignment

## Integration Approaches

The ArcGIS Architecture Center frames integration as a way to combine enterprise systems without reinventing their capabilities. Capybara follows that principle. It brings ServiceNow data into ArcGIS as operational layers; provides ArcGIS maps and spatial context back to ServiceNow; and supports workflow-driven movement of data and users between systems.

| Architecture Center approach | Capybara interpretation | Typical implementation |
| --- | --- | --- |
| Bring data and capabilities into ArcGIS | ServiceNow incidents, work orders, assignments, and assets appear as ArcGIS operational layers. | Python queries ServiceNow REST APIs and updates ArcGIS feature services. |
| Provide data and capabilities to other systems | ServiceNow receives indoor place context, map URLs, route links, unit IDs, and spatial-enrichment results. | Python queries ArcGIS feature layers and PATCHes ServiceNow records. |
| Integrate through workflows | ServiceNow record events trigger middleware processing, which updates GIS and writes context back to ServiceNow. | Outbound REST webhook + worker queue + reconciliation. |
| Embed ArcGIS applications | ServiceNow pages can contain embedded indoor map experiences or links that open ArcGIS Indoors at a specific place. | iframe, Experience Builder, Indoor Viewer URL parameters, or native ArcGIS Maps for ServiceNow when available. |
| Custom data feeds | ServiceNow data can be exposed as live feature-service-like data through a connector or custom feed. | ArcGIS for ServiceNow Connector, custom data feed provider, or Python-managed cache. |

## ServiceNow + ArcGIS Integration Patterns

The ArcGIS Architecture Center identifies several relevant ServiceNow integration options: ArcGIS Maps for ServiceNow, Connector for ServiceNow, embedding ArcGIS applications inside ServiceNow, using ServiceNow Integration Hub or REST messages to query ArcGIS services, accessing ServiceNow content through ArcGIS applications, Python-based ETL, Workflow Manager patterns, and mobile deep-linking patterns. Capybara incorporates these patterns into a local-government Indoors architecture.

Capybara design positionThe Python middleware pattern is not meant to compete with Esri’s native ArcGIS for ServiceNow direction. It creates a practical, transparent, locally governable bridge today, while preserving a path to adopt native Esri-supported connector capabilities as they mature.

## Pattern Fit Table

| Pattern | Strength | Limitation | Capybara use |
| --- | --- | --- | --- |
| ArcGIS Maps for ServiceNow | Provides map/web-scene experience directly inside ServiceNow. | Feature availability and beta/release status must be validated before production use. | Future embedded map option for agents and request workflows. |
| Connector for ServiceNow | Can query ServiceNow data live for ArcGIS workflows without ETL copies. | May not cover all indoor mapping, write-back, or custom governance needs. | Future replacement or complement for custom feature-feed logic. |
| Embedded ArcGIS app | Lightweight, low-code, and useful for visual context. | May be mostly presentational unless paired with APIs. | Useful first step for map context in ServiceNow. |
| REST/Integration Hub to ArcGIS | ServiceNow can enrich records by querying ArcGIS services. | Complex spatial rules may be easier in Python than in ServiceNow scripting. | Good for simple location lookup or map URL generation. |
| Python-based ETL / middleware | Flexible, transparent, testable, and easy to adapt to local schemas. | Custom code requires operational ownership. | Primary Capybara implementation pattern. |
| Workflow Manager pattern | Supports structured GIS workflows triggered from ServiceNow. | May be more workflow-heavy than needed for simple ITSM synchronization. | Useful for complex facilities/GIS review workflows. |

## Observability, Reliability, and Security Alignment

Capybara follows ArcGIS Architecture Center themes by treating integration as an enterprise system. Monitoring, baselines, secure network design, authentication, authorization, logging, retry handling, data governance, and capacity planning are design requirements rather than afterthoughts.
