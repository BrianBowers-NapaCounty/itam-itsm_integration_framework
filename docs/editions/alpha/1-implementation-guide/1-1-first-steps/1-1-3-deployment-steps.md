# Deployment Steps
Deployment instructions.

<div class="rc3-extension">

## Expanded 1.0.0 Guidance

```{image} /_images/symbol-information.png
:alt: 1-1-3-deployment-steps
:width: 64px
:class: page-symbol
```

<div>

#### Deployment Steps

1.  Define pilot use cases and acceptance criteria.
2.  Inventory ServiceNow data fields, references, and event triggers.
3.  Inventory ArcGIS Indoors layers and identify stable location keys.
4.  Create the crosswalk schema and matching rules.
5.  Deploy Flask receiver in dev/test.
6.  Configure ServiceNow outbound REST event for a test table.
7.  Implement queue, worker, ServiceNow client, ArcGIS client, and logging.
8.  Test one-way ServiceNow-to-ArcGIS flow.
9.  Test ArcGIS context write-back to ServiceNow.
10. Add scheduled reconciliation and dead-letter review.
11. Run a security and operations review.
12. Move to controlled pilot production.

</div>

</div>
