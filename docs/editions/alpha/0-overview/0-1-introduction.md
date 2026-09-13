```{image} /_images/symbol-information.png
:alt: 0-1-introduction
:width: 64px
:class: page-symbol
```

<div>

### Introduction

The Capybara Framework treats indoor spatial context as an operational IT capability. ServiceNow contains the authoritative record of work, request state, service ownership, asset lifecycle, assignment, work notes, approvals, and closure. ArcGIS Indoors contains authoritative indoor spatial context: sites, facilities, levels, units, spaces, routes, maps, floorplans, and indoor assets. Python middleware connects these two worlds without requiring either platform to surrender its core role.

In the most common Capybara pattern, ServiceNow emits event notifications when incidents, requests, tasks, assets, or work orders are created or updated. A Python/Flask application receives the event, validates it, stores a lightweight queue record, then uses ServiceNow REST APIs to retrieve full authoritative details. The worker then uses ArcGIS API for Python to query indoor spatial context, update operational feature layers, and write map links or place IDs back into ServiceNow.

<div class="callout tip">

<span class="callout-title">Implementation posture</span>Capybara is not a replacement for ServiceNow, ArcGIS Indoors, ArcGIS Enterprise, ArcGIS Pro, or a future Esri-supported connector. It is an architecture pattern and governance model for making those systems work together in a local-government IT environment.

</div>

</div>