# Problem Statement

<img class="capybara-right" width="250px" src="/en/latest/_images/L.png" alt="Capybara with a bright idea" style="filter: sepia(25%);">County IT departments manage thousands of physical IT assets across numerous buildings, floors, offices, and shared spaces, yet asset and service management systems often lack precise, intuitive spatial context. This results in slower incident response, inconsistent asset records, inefficient field work, and limited visibility into location-based risks and dependencies.

A spatially enabled ITAM/ITSM solution—integrating ArcGIS Indoors with an existing IT service management platform—addresses these challenges by embedding floorplan-level location intelligence directly into IT workflows. A spatially enabled ITAM/ITSM solution reduces operational blind spots, strengthens accountability, and supports more resilient County IT operations.

<div class="rc3-extension">

## Extended guidance for the Original Edition

```{image} /_images/symbol-information.png
:alt: 0-2-problem-statement
:width: 64px
:class: page-symbol
```

<div>

### Problem Statement

Many service tickets include a weak location description: “printer near Finance,” “conference room display broken,” “new phones for the building across town,” or “replacement workstation at east-side cubicle.” These descriptions are meaningful to humans but difficult for service systems to use without a formal place model. The result is manual lookup, repeated clarification, inconsistent dispatch, fragmented asset visibility, and reporting that lacks a spatial dimension.

Capybara addresses this by turning ticket and asset records into location-enriched operational records. It does not require ServiceNow to become a GIS. It does not require ArcGIS Indoors to become a ticketing system. It uses integration to preserve strengths: ServiceNow controls service work; ArcGIS controls spatial context; Python translates between them.

</div>

</div>
