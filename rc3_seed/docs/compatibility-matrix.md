# Compatibility Matrix

| Component | Reference posture | Notes |
| --- | --- | --- |
| ArcGIS Online | Supported architecture | Hosted tables/layers and notebooks can be used. |
| ArcGIS Enterprise Portal | Supported architecture | Preferred where on-premises control is required. |
| ArcGIS Indoors | Core spatial system | Facility/level/unit identifiers are the principal spatial crosswalk. |
| ArcGIS API for Python | Reference implementation | Examples use `GIS`, `FeatureLayer.query()`, and edit operations. |
| ServiceNow | Most complete sample connector | Table API patterns, normalization, update/write-note examples. |
| TeamDynamix | Reference adapter | Web API / Bearer token model; local fields remain configurable. |
| Cherwell | Reference adapter / skeleton | Saved searches and local Business Object mapping require local configuration. |
| MockConnector | Demo-runnable | Included JSON samples require no credentials. |
| SMTP | Optional notification channel | Console preview is the safe default. |
| SQLite | Local analytics demo | Allows historical analytics without AGOL/Portal. |
