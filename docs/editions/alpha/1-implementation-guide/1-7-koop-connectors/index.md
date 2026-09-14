```{image} /_images/symbol-api.png
:alt: Koop and Connector Patterns
:width: 64px
:class: page-symbol
```

# Koop and Connector Patterns

This section expands the ArcGIS for ServiceNow discussion with a detailed treatment of Esri's earlier Koop-based ServiceNow feature-service pattern. In public Esri materials, the newer vendor-supported capability is named **ArcGIS for ServiceNow**with two named components: **Connector for ServiceNow** and **ArcGIS Maps for ServiceNow**. Some project discussions may casually call this a collector-style or connector solution; this document uses the public product names where possible and compares those capabilities with the older open-source Koop pattern and the Capybara Framework's original Python middleware concept.

How the three patterns differThe Koop pattern primarily exposes ServiceNow incidents and requests to ArcGIS as a read-through ArcGIS-style FeatureServer and separately loads Indoors location data into ServiceNow. The new ArcGIS for ServiceNow pattern is a vendor-supported integration family designed to make ServiceNow data available in ArcGIS and ArcGIS maps available in ServiceNow. The original Capybara pattern is a locally governed Python integration service that receives events, persists queues/logs/crosswalks, updates ArcGIS operational layers, and writes enriched context back to ServiceNow.

```{toctree}
:maxdepth: 2

1-7-1-koop-overview-mechanics
1-7-2-loader-launch-actions
1-7-3-comparison-decision-matrix
1-7-4-security-controls
```
