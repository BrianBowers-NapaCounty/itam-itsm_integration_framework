```{image} /_images/symbol-important.png
:alt: Assumptions, Exclusions, and Framework Boundaries
:width: 64px
:class: page-symbol
```

# Assumptions, Exclusions, and Framework Boundaries

The following source section defines the planning assumptions and explicit exclusions that should travel with any Capybara implementation. Because these statements clarify scope, responsibility, and local accountability, they are incorporated as a source section.

Source section

### Assumptions & Exclusions

This section outlines the key assumptions under which the Capybara Framework is intended to be applied, as well as its inherent limitations and exclusions. These statements help set realistic expectations, clarify responsibilities, and ensure the framework is used appropriately as a strategic and planning guide rather than a prescriptive or turnkey solution.

### Assumptions

The Capybara Framework assumes the following conditions are in place, or will be addressed, by organizations choosing to adopt its guidance:

- ArcGIS Licensing Availability  
  Participating departments or municipalities maintain the required ArcGIS Online or ArcGIS Enterprise, ArcGIS Indoors, and ArcGIS Field Maps licenses necessary to support spatially enabled asset and service workflows.

- Up-to-Date GIS and Asset Data  
  Building floorplans, indoor location layers, asset inventories, and user-related spatial data are accurate, complete, and actively maintained within the organization’s GIS and ITAM systems.

- Endpoint Security Compliance  
  All mobile and desktop devices accessing Capybara-supported workflows adhere to organization-defined security baselines, identity management requirements, and acceptable-use policies.

- Interdepartmental Coordination  
  IT, GIS, Facilities, and other partner departments coordinate on data governance, location permissions, access controls, and privacy considerations to support shared use of spatial and service data.

- Reliable Network Connectivity  
  Users generally have access to stable Wi-Fi or cellular connectivity for synchronization and updates, except where offline workflows are explicitly supported (e.g., ArcGIS Field Maps offline use).

- User Device Compatibility  
  Field technicians and IT staff use mobile devices capable of running ArcGIS Field Maps and supporting required location services such as GPS, Wi-Fi positioning, or indoor positioning systems.

- Organizational Adoption and Training  
  Staff receive appropriate training and onboarding to support new workflows, including asset check-in/check-out practices, location-aware tasking, and use of mobile applications.

### Limitations and Exclusions

The Capybara Framework also acknowledges the following limitations and explicitly defines what is outside its scope:

- Indoor Positioning Accuracy  
  Location precision is constrained by the quality and availability of indoor positioning technologies (e.g., IPS, Wi-Fi triangulation, BLE beacons) and by environmental conditions within facilities.

- Data Refresh and Synchronization Rates  
  “Real-time” visibility depends on device synchronization intervals, network availability, and platform behavior; update latency may vary.

- User Compliance Dependencies  
  Accurate personnel and asset tracking relies on consistent user behavior, including carrying authorized devices, maintaining sign-in status, and following defined operational procedures.

- Privacy and Policy Constraints  
  Personnel location visibility and historical tracking may be restricted by labor agreements, privacy regulations, or organizational policy, limiting granularity for certain users or roles.

- Third-Party System Integration Constraints  
  Integration with ITSM/ITAM platforms (e.g., ServiceNow, Cityworks) is subject to vendor APIs, licensing terms, data models, and organizational configuration choices.

- Device Battery and Performance Considerations  
  Continuous location tracking and background application use may impact mobile device battery life and performance, affecting update frequency or offline behavior.

- Platform Dependency  
  Capybara is designed exclusively for the Esri ArcGIS ecosystem and does not support non-Esri mapping or indoor GIS platforms.

- Not a Turnkey Implementation or Managed Service  
  Capybara is a framework and implementation guide, not a software product, managed service, or fully configured deployment. Organizations remain responsible for system configuration, integration, and ongoing operations.

### Assumptions & Exclusions Summary

| Category | Item | Summary Description |
| --- | --- | --- |
| Assumption | ArcGIS Licensing Availability | Required ArcGIS Online or ArcGIS Enterprise, ArcGIS Indoors, and Field Maps licenses are in place to support Capybara workflows. |
| Assumption | GIS & Asset Data Readiness | Building floorplans, indoor layers, and asset inventories are accurate, current, and actively maintained. |
| Assumption | Endpoint Security Compliance | Devices accessing Capybara adhere to organizational security, identity, and access-control standards. |
| Assumption | Interdepartmental Coordination | IT, GIS, Facilities, and partner departments collaborate on data governance, permissions, and privacy controls. |
| Assumption | Network Connectivity | Reliable Wi-Fi or cellular connectivity is generally available, with offline support used where applicable. |
| Assumption | Device Compatibility | Field and IT staff use mobile devices capable of running ArcGIS Field Maps and supporting location services. |
| Assumption | Training & Adoption | Users receive appropriate training and follow defined workflows and operational procedures. |
| Limitation | Indoor Positioning Accuracy | Location precision depends on IPS, Wi-Fi triangulation, BLE beacons, and building conditions. |
| Limitation | Data Refresh Rates | Near real-time visibility varies based on sync frequency, device behavior, and connectivity. |
| Limitation | User Compliance | Accurate tracking relies on consistent user behavior (check-ins, device usage, app sign-in). |
| Limitation | Privacy Restrictions | Personnel location visibility may be limited by policy, labor agreements, or regulation. |
| Limitation | Third-Party Integration | ITSM/ITAM integration depends on vendor APIs, licensing, and system constraints. |
| Limitation | Device Battery & Performance | Continuous tracking may impact battery life and update reliability on mobile devices. |
| Exclusion | Non-Esri Platforms | Capybara applies only to the Esri ArcGIS ecosystem and does not support non-Esri GIS platforms. |
| Exclusion | Turnkey Implementation | Capybara is a framework and guide—not a preconfigured solution or managed service. |
| Exclusion | Operational Ownership | Organizations remain responsible for configuration, integration, operations, and maintenance. |

### Framework Boundaries

Taken together, these assumptions and exclusions reinforce that Capybara is intended to guide strategy, planning, and design decisions, not to replace existing systems, override governance structures, or eliminate the need for local judgment. Organizations are encouraged to adapt the framework to their technical environment, policies, and maturity level while remaining aligned with its guiding principles.

## Implementation Expansion: Making the Boundaries Operational

For an architecture implementation, these assumptions should become acceptance gates. A pilot should not proceed to production until licensing, indoor data readiness, endpoint security, stakeholder coordination, network connectivity, device compatibility, training, privacy policy, and operational ownership have each been assigned to a responsible owner.

| Boundary area | Recommended implementation control | Owner to identify |
| --- | --- | --- |
| Licensing | Confirm ArcGIS Indoors, ArcGIS Enterprise or ArcGIS Online, Field Maps, ServiceNow, and connector/API licensing before design freeze. | GIS administrator + ITSM product owner |
| Data readiness | Run a pre-pilot audit of building, floor, unit, asset, and location crosswalk completeness. | GIS data steward + IT asset manager |
| Endpoint security | Approve supported mobile and desktop baselines and define what happens when a device is out of compliance. | Security team + endpoint management team |
| Privacy | Document who can view personnel location context, whether history is retained, and what data is suppressed from dashboards. | Security/privacy/legal + HR/labor relations as applicable |
| Not turnkey | Create a support model for middleware, ServiceNow configuration, ArcGIS data maintenance, logs, credentials, and reconciliation. | Integration owner + platform owners |
