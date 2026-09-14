# Data Dictionary
Data dictionary content.

<div class="rc3-extension">

## Extended guidance for the Original Edition

```{image} /_images/symbol-information.png
:alt: 2-3-data-dictionary
:width: 64px
:class: page-symbol
```

<div>

### Data Dictionary

<div class="table-wrap">

| Field                 | System            | Purpose                                                                                  |
|-----------------------|-------------------|------------------------------------------------------------------------------------------|
| `incident.sys_id`     | ServiceNow        | Stable primary identifier for an incident record.                                        |
| `incident.number`     | ServiceNow        | User-facing ticket number.                                                               |
| `cmdb_ci.sys_id`      | ServiceNow        | Stable identifier for an affected CI.                                                    |
| `cmn_location.sys_id` | ServiceNow        | Stable identifier for ServiceNow location record.                                        |
| `facility_id`         | ArcGIS Indoors    | Identifier for a facility/building.                                                      |
| `level_id`            | ArcGIS Indoors    | Identifier for a floor/level.                                                            |
| `unit_id`             | ArcGIS Indoors    | Identifier for a room, unit, cubicle, shared space, or work area.                        |
| `globalid`            | ArcGIS            | Global unique identifier for a feature, often useful for stable cross-system references. |
| `u_arcgis_map_url`    | ServiceNow custom | Write-back field containing a URL to a relevant ArcGIS map/app location.                 |

</div>

</div>

</div>
