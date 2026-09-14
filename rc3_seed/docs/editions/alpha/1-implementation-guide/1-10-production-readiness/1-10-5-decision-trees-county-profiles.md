```{image} /_images/symbol-telescope.png
:alt: Implementation Decision Trees and County Profiles
:width: 64px
:class: page-symbol
```

# Implementation Decision Trees and County Profiles

## Implementation Decision Trees

**Decision support**

Decision trees help teams choose a pattern without prematurely overbuilding or under-securing the solution.

### Do you need near-real-time updates?

1. No: begin with scheduled sync.
2. Yes: use webhook plus queue plus worker.
3. Yes, with high security restrictions: use API gateway, private connectivity, brokered queue, or outbound-only relay pattern.

### Do you need ServiceNow write-back?

1. No: publish one-way spatial operational layers.
2. Yes, for context only: write back map URLs, place IDs, and confidence values.
3. Yes, workflow-altering: require formal change control, testing, and service owner approval.

### Do you have reliable indoor identifiers?

1. Yes: use direct crosswalk matching.
2. Partially: use aliases, confidence scores, and exception review.
3. No: prioritize data cleanup before expanding automation.

### How complex should the architecture be?

1. One building / one use case: scheduled script may be enough.
2. Multiple facilities / operational dashboards: queue-backed middleware is preferred.
3. High availability / regulated data: gateway, vault, SIEM, HA database, and formal support model.

## County Implementation Profiles

**Adoption profiles**

Different counties can enter the framework at different levels of complexity while preserving the same governance principles.

| Profile | Description | Recommended Pattern | Primary Risk |
| --- | --- | --- | --- |
| Small County Pilot | One building, one ticket type, limited asset scope. | Scheduled sync with manual reconciliation. | Data cleanup postponed until after pilot. |
| Medium County Rollout | Multiple facilities, several ticket types, manager dashboards. | Webhook + queue + worker with limited write-back. | Unclear ownership of crosswalks and aliases. |
| Large County Enterprise | Many departments, facilities, dashboards, and support groups. | Brokered middleware, formal environments, monitoring, security review. | Architecture and governance complexity. |
| High-Security Pattern | Sensitive locations, constrained connectivity, strict audit requirements. | Private connectivity, API gateway, minimal write-back, SIEM logging. | Longer security and network coordination. |
| Connector-First Pattern | Agency wants vendor-supported integration where feature coverage is sufficient. | ArcGIS-ServiceNow connector approach with local governance overlays. | Feature gaps, licensing, and extensibility limits. |
