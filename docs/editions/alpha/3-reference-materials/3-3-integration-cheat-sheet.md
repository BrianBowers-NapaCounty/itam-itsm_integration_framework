# Integration Cheat Sheet
Cheat sheet content.

<div class="rc3-extension">

## Extended guidance for the Original Edition

```{image} /_images/symbol-api.png
:alt: 3-3-integration-cheat-sheet
:width: 64px
:class: page-symbol
```

<div>

### Integration Cheat Sheet

<div class="table-wrap">

| Need                                    | Recommended Pattern                                                 | Primary Benefit                                                   | Watch For                                                      |
|-----------------------------------------|---------------------------------------------------------------------|-------------------------------------------------------------------|----------------------------------------------------------------|
| Simple pilot visibility                 | Scheduled Python sync                                               | Low complexity and fast proof of concept                          | Stale data between scheduled runs                              |
| Near-real-time ticket updates           | Webhook + queue + worker middleware                                 | Fresh operational layers and timely write-back                    | Endpoint security, retries, and monitoring                     |
| Read-through feature-service facade     | Koop provider pattern                                               | ArcGIS-compatible access to external records                      | Query translation, caching, permissions, and supportability    |
| Vendor-supported ServiceNow integration | ArcGIS for ServiceNow / connector pattern                           | Reduced custom development where supported                        | Licensing, feature coverage, extensibility, and release timing |
| Complex county-specific workflows       | Capybara Python middleware                                          | Custom mapping, write-back, queueing, logging, and reconciliation | Operational ownership and technical maturity                   |
| High security / low exposure            | Outbound pull, brokered queue, API gateway, or private connectivity | Reduced public endpoint exposure                                  | Architecture complexity and network coordination               |

</div>

#### Common Field Mapping

<div class="table-wrap">

| ServiceNow / ITSM Field       | ArcGIS / Indoors Field                  | Purpose                                                         |
|-------------------------------|-----------------------------------------|-----------------------------------------------------------------|
| `incident.sys_id`             | `ticket_id` or integration key          | Durable ticket linkage.                                         |
| `incident.number`             | `ticket_number`                         | Human-readable ticket reference.                                |
| `incident.state`              | `status`                                | Map symbology and dashboard filtering.                          |
| `incident.priority`           | `priority`                              | Urgency, hotspot, and dispatch analysis.                        |
| `cmdb_ci.sys_id`              | `sn_ci_sys_id`                          | Links a CI to a mapped indoor asset.                            |
| `alm_asset.asset_tag`         | `asset_tag`                             | Human-readable asset lookup.                                    |
| `cmn_location`                | `unit_id``level_id``facility_id`        | Converts text/location references into indoor spatial context.  |
| `assigned_to`                 | `technician_id` or related attribute    | Supports routing, assignment visibility, and workload analysis. |
| Map URL / place ID write-back | ArcGIS item URL, unit URL, or route URL | Returns spatial context to the ITSM record.                     |

</div>

</div>

</div>
