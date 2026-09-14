# ArcGIS Enterprise
Enterprise setup instructions.

<div class="rc3-extension">

## Extended guidance for the Original Edition

```{image} /_images/symbol-information.png
:alt: 1-2-2-enterprise
:width: 64px
:class: page-symbol
```

<div>

### ArcGIS Enterprise

The Enterprise pattern should treat Indoors data as an authoritative indoor GIS asset. That includes layer publishing, map configuration, group permissions, sharing, dashboard access, branch/versioning considerations where applicable, data-quality processes, and administrative ownership.

#### 4.1.1 Enterprise components

<div class="table-wrap">

| Component                         | Role in Capybara                                                                          | Implementation note                                                                        |
|-----------------------------------|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Portal for ArcGIS                 | Identity, content, maps, apps, groups, dashboard items, and access control.               | Use a dedicated integration account and controlled groups for operational layers.          |
| ArcGIS Server                     | Hosts referenced or hosted feature services, map services, and associated endpoints.      | Integration writes should target carefully scoped editable layers.                         |
| ArcGIS Data Store                 | Supports hosted feature layers and other Enterprise data capabilities.                    | Use in accordance with Enterprise deployment type and hosting-server configuration.        |
| SQL Server enterprise geodatabase | May store authoritative or registered Indoors feature classes, depending on local design. | Validate database version and ArcGIS support matrix before production.                     |
| Web Adaptor / reverse proxy       | Provides standard web-server integration and route exposure for Portal/Server.            | Do not confuse ArcGIS Web Adaptor responsibilities with Flask middleware responsibilities. |

</div>

#### 4.1.2 Indoors layers

At minimum, Capybara requires a stable representation of buildings/facilities, levels/floors, units/spaces, and optionally indoor assets, occupants, pathways, and points of interest. The integration should avoid writing authoritative geometry unless the workflow explicitly governs geometry changes. Most ITSM integration updates should write operational attributes and derived layers, not alter base floorplans.

</div>

</div>
