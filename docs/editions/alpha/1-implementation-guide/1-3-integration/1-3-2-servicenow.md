# Integration-ServiceNow
ServiceNow instructions.

<div class="rc3-extension">

## Expanded 1.0.0 Guidance

```{image} /_images/symbol-api.png
:alt: 1-3-2-servicenow
:width: 64px
:class: page-symbol
```

<div>

### Integration-ServiceNow

#### 5.2.1 Outbound REST trigger strategy

ServiceNow can send an outbound REST message from script-capable areas when an event is triggered. For Capybara, the recommended outbound event includes only enough information to identify the changed record and event type. The middleware then queries ServiceNow for authoritative current state, avoiding over-large webhook payloads and reducing field-coupling.

#### 5.2.2 ServiceNow API calls

<div class="table-wrap">

| Action                  | Example endpoint class     | Purpose                                                                                       |
|-------------------------|----------------------------|-----------------------------------------------------------------------------------------------|
| Get full incident/task  | Table API                  | Retrieve authoritative details after webhook event.                                           |
| Get CI/asset context    | CMDB/Table API             | Resolve affected asset, serial number, asset tag, lifecycle status, assignment, and location. |
| Get user/caller context | Table API                  | Resolve caller, department, location, contact route, and assignment relationships.            |
| Patch enriched fields   | Table API                  | Write map URLs, place IDs, match status, confidence, and sync state.                          |
| Add work note           | Table API or record update | Provide traceable statement of GIS enrichment or error.                                       |

</div>

</div>

</div>
