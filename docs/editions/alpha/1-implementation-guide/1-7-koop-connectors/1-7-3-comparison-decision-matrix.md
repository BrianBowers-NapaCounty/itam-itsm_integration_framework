```{image} /_images/symbol-look2.png
:alt: Connector Comparison and Decision Matrix
:width: 64px
:class: page-symbol
```

```{image} /_images/logo-servicenow.png
:alt: Connector Comparison and Decision Matrix
:width: 150px
:class: page-logo
```

# Connector Comparison and Decision Matrix

## Comparison: Koop Pattern, New ArcGIS for ServiceNow, and Original Capybara

| Dimension | Koop-based repository pattern | New ArcGIS for ServiceNow / Connector pattern | Original Capybara Python middleware pattern |
| --- | --- | --- | --- |
| Primary direction | ArcGIS consumes ServiceNow incident/request data as feature-service-like output; ServiceNow receives Indoors location data through loader; Indoors can launch ServiceNow forms. | Bidirectional product family: ServiceNow data appears in ArcGIS through a Connector, and ArcGIS maps/scenes appear inside ServiceNow through ArcGIS Maps for ServiceNow. | Bidirectional custom middleware: ServiceNow events and polling feed ArcGIS operational layers; ArcGIS context writes back to ServiceNow. |
| Data persistence | Primarily read-through for incidents/requests; location data is loaded into ServiceNow. | Public Esri descriptions emphasize direct/live access to ServiceNow data and reduced duplication. | Usually persists queue/log/crosswalk data and may persist derived ArcGIS operational features. |
| Technology stack | Node.js, Koop.js, ServiceNow Table API, Python/ArcPy loader, ArcGIS clients. | Esri-supported ServiceNow app and ArcGIS Enterprise custom data feed / connector capabilities. | Python, Flask, queue database, ServiceNow REST APIs, ArcGIS API for Python, ArcGIS Enterprise. |
| Best use | Read-only or mostly read-only map visualization of incidents/requests and Indoors-to-ServiceNow form launch. | Vendor-supported live ServiceNow data in ArcGIS and map/web-scene experience inside ServiceNow. | Custom, auditable local-government workflows with queues, reconciliation, governance-specific matching, and write-back logic. |
| Operational maturity | Older open-source sample/reference architecture; likely requires modernization for current Node, ServiceNow, ArcGIS, and security practices. | Emerging Esri product capability; beta/release maturity, licensing, and support boundary must be validated. | Locally owned and fully controllable, but requires sustained engineering and operations ownership. |
| Indoors specificity | Strong Indoors relationship through location loader and launch actions. | Must be evaluated for floor-aware Indoors depth, unit/level handling, and indoor routing workflows. | Can be built specifically around Indoors facilities, levels, units, pathways, assets, occupants, and dashboards. |
| Write-back and workflow | Launch actions can create/open ServiceNow forms; the feature-service layer itself is not a general workflow engine. | Public descriptions include taking actions such as initiating service requests or work orders from the map interface. | Can perform custom ServiceNow PATCHes, work notes, assignment hints, confidence statuses, and reconciliation outcomes. |

## Pros, Cons, Risks, and Benefits

### Koop-based pattern

### Benefits

- Provides a practical ArcGIS-facing façade over ServiceNow records.
- Can avoid copying incident/request data into a separate ArcGIS hosted feature layer.
- Uses Indoors launch actions to connect map users directly to ServiceNow forms.
- Separates location seeding from live incident/request visualization.
- Can be useful for proof-of-concept work when an organization wants ServiceNow incidents on an indoor map quickly.

### Risks / limitations

- Older sample code may require dependency modernization, security review, and compatibility testing.
- Read-through performance depends on ServiceNow API speed, limits, query design, and caching.
- ArcGIS client behavior may expose query patterns that are awkward to translate into ServiceNow Table API calls.
- Read-only feature-service views do not automatically solve write-back, reconciliation, or workflow orchestration.
- Incident/request attributes may contain sensitive operational or personnel information.

### New ArcGIS for ServiceNow / Connector pattern

### Benefits

- Vendor-supported direction with Esri and ServiceNow alignment.
- Designed to reduce data duplication by giving ArcGIS direct access to ServiceNow business data.
- Supports maps and scenes in ServiceNow and ServiceNow business data in ArcGIS.
- Likely easier to explain to executives, procurement, security, and support teams than a custom sample repository.
- Potentially lowers custom code burden for standard workflows.

### Risks / limitations

- Beta/release timing, licensing, and support details must be verified before production planning.
- Local-government Indoors-specific requirements may exceed baseline product behavior.
- Custom field mapping, county-specific crosswalks, and reconciliation reports may still require middleware.
- Security teams must validate authentication, authorization, logging, and data residency behavior.
- Feature parity with existing custom proof-of-concept workflows should not be assumed.

### Original Capybara pattern

### Benefits

- Maximum local control over queues, logs, crosswalks, matching rules, retry behavior, and write-back logic.
- Can support complex county-specific governance and audit requirements.
- Works well when ArcGIS Indoors needs derived operational layers, not only live ServiceNow views.
- Allows event-driven, polling, and manual reconciliation paths to coexist.
- Can be extended beyond ServiceNow to TeamDynamix, Cherwell, Cityworks, or other systems.

### Risks / limitations

- Custom code requires a product owner, maintainer, test plan, change-control process, and security review.
- Derived ArcGIS layers introduce duplication unless lifecycle and synchronization rules are explicit.
- Middleware becomes part of the operational support chain.
- Bad matching logic can create misleading map context if confidence controls are weak.
- The system can grow beyond a pilot unless scope is deliberately governed.

## Recommended Capybara Position

The Capybara Framework should document the Koop-based pattern as a historically important and technically useful reference architecture, not as the default future production recommendation. Its strongest contribution is the architectural separation of **location seeding****live ServiceNow-to-ArcGIS feature-service visualization**and **Indoors-to-ServiceNow launch actions**. Those concepts remain valuable even if an organization later adopts ArcGIS for ServiceNow or a fully custom Python middleware bridge.

Recommended selection logicUse **ArcGIS for ServiceNow** first when it is available, licensed, security-approved, and functionally deep enough for the required ServiceNow and Indoors workflows. Use **Koop** when a team needs a custom read-through feature-service façade and is prepared to own Node.js/Koop operations. Use **Capybara Python middleware** when the organization needs persistent queues, reconciliation, custom write-back, complex crosswalks, and county-specific governance.

## Decision Matrix for Local Governments

| Question | Prefer Koop | Prefer ArcGIS for ServiceNow | Prefer Capybara middleware |
| --- | --- | --- | --- |
| Need live ServiceNow incidents in ArcGIS with minimal data copy? | Possible, with custom provider work. | Yes, if Connector supports required tables and deployment model. | Possible, but usually through derived layers rather than pure live query. |
| Need queue, retry, dead-letter, and reconciliation controls? | Not inherent; must be added. | Validate product capabilities. | Yes; this is a core design feature. |
| Need to write custom enriched fields or work notes back to ServiceNow? | Not the primary feature-service pattern. | Validate supported action/write-back capabilities. | Yes; custom write-back is one of the main reasons to use it. |
| Need a vendor-supported integration path? | No; repository is open-source/sample-style and must be locally supported. | Yes, subject to release and support terms. | No; locally supported custom integration. |
| Need to incorporate non-ServiceNow ITSM tools later? | Only by writing additional providers. | Likely ServiceNow-specific. | Yes, with adapter design. |
| Need floor-aware Indoors specificity? | Strong conceptual fit because repository was built for Indoors and ServiceNow. | Must validate against current product capabilities. | Strongest if designed directly against the local Indoors model. |
