# Quick-start Guide
Quick start content.

<div class="rc3-extension">

## Expanded 1.0.0 Guidance

```{image} /_images/symbol-information.png
:alt: 3-2-quick-start-guide
:width: 64px
:class: page-symbol
```

<div>

### Quick-start Guide

1.  **Define one pilot use case.** Start with a workflow such as shared printer incidents, workstation deployment, phone installation, or network-drop support.
2.  **Choose the integration pattern.** Select scheduled sync, webhook-driven middleware, Koop-style read-through services, a connector approach, or a hybrid pattern.
3.  **Inventory required identifiers.** Confirm the record IDs needed for tickets, assets, CIs, facilities, levels, units, rooms, desks, and map links.
4.  **Create the crosswalk.** Map ITSM/ITAM fields to ArcGIS Indoors fields and identify derived values, defaults, and exception rules.
5.  **Build in a test environment.** Use non-production ServiceNow and ArcGIS layers until mapping, write-back, permissions, and logging are validated.
6.  **Publish the first operational layer.** Create a simple layer for incidents, assets, deployments, or work orders with only the fields required for the pilot.
7.  **Write back useful context.** Add map URLs, unit IDs, place IDs, floor context, or confidence scores back to the ITSM platform when appropriate.
8.  **Add dashboard visibility.** Provide simple operational views for service desk staff, technicians, managers, and leadership.
9.  **Test failures deliberately.** Validate API outage behavior, missing locations, duplicate matches, permission failures, retries, and reconciliation.
10. **Review and expand.** Compare pilot outcomes against success metrics before adding more assets, facilities, ticket types, or automation.

</div>

</div>
