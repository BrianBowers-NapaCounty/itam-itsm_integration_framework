```{image} /_images/symbol-talkingpoints.png
:alt: County Context and Business Value
:width: 64px
:class: page-symbol
```

# County Context and Business Value

This section places the technical architecture in its local-government business context. The source text below is incorporated from the attached *County Context - Business Value.docx* section document. It is presented as a source section so its original survey framing, user-story language, and business-value language remain intact.

How this section informs the architectureThe county-context material justifies why Capybara should focus on buildings, floors, office locations, asset visibility, technician deployment, audit readiness, and leadership reporting. It also provides survey evidence that local-government IT departments have a real floorplan-visibility gap.

Source section

### County Context

Capybara was born out of the CCISDA-CSAC Technology Executive Credential Program, which centers on information services in California county governments. For a project like this, focusing on California counties makes sense because they sit at the intersection of scale, complexity, and public accountability in government operations. Counties are responsible for maintaining vast and diverse portfolios of facilities, technology assets, and personnel—often spread across hundreds of buildings and multiple cities—while delivering critical services to millions of residents. This creates a strong need for better visibility into where assets and staff are located, how resources are being used, and how quickly issues can be resolved.

County governments also face unique operational pressures: aging infrastructure, constrained budgets, strict regulatory and audit requirements, and a growing expectation for data-driven decision-making. Many counties already operate mature ITSM/ITAM systems and use GIS extensively, but these systems are rarely integrated in a way that supports day-to-day operations inside buildings. Capybara directly addresses this gap by connecting indoor location context with asset and service data, improving efficiency without requiring wholesale replacement of existing systems.

Finally, counties represent a high-impact opportunity because solutions developed at the county level are inherently reusable and scalable. California’s counties vary widely in size and sophistication, making them an ideal proving ground for a framework that can be adapted statewide and beyond. Improvements in county IT operations translate directly into better service delivery, faster issue resolution, and more effective stewardship of public resources—magnifying the impact well beyond any single organization.

County governments manage a large, diverse, and geographically distributed asset base. They depend on a wide range of IT assets to deliver essential public services, including:

End-user devices (desktops, laptops, tablets, mobile devices)

Network and data center equipment

Servers, storage, and cloud resources

Software applications and licenses

Public safety and field technology systems

These assets are:

Purchased and maintained using taxpayer and grant funds

Distributed across multiple department building and campus locations

Subject to audit, public records, cybersecurity, and licensing compliance requirements

Critical to public safety, health services, courts, elections, and daily operations

In a recent survey conducted by team Capybara it was determined...

...That a vast majority of counties that responded have over 15 buildings where IT assets are deployed, and that ¾ of these counties report that they would benefit from being able to manage IT assets’ physical locations and deploy support technicians accordingly.

### December 2025 Survey Results

Representatives from the IT departments of 16 California counties (of 58 total, 27.6%) responded to a survey poll distributed in December 2025. Response counts were:

Placer (2), San Luis Obispo (2), Tulare (2), Fresno (1), Kern (1), Kings (1), Lassen (1), Orange (1), San Joaquin (1), Stanislaus (1), Trinity (1), Tuolumne (1), Yolo (1), others (0)

To the question “Which of the following help-desk, ticketing/work-order, and asset-service products does your organization use?”, respondents said:

ServiceNow (6), TDX (2), BossDesk (2), OpenGOV (2), NinjaOne (1), Giva (1), AllSight (1),  
 I don’t know (2)

Responses to the rest of the questions were as follows:

Does your county’s ITSM & ITAM solution support the display of asset locations overlayed on building floorplans?

| Yes (0, 0%) No (10, 62.5%) I don't know (6, 37.5%) |  |
| --- | --- |

Do you think your IT department could benefit from this floorplan functionality to manage assets’ locations and deploy support technicians?

| Yes (12, 75%) No (2, 12.5%) I don’t know (2, 12.5%) |  |
| --- | --- |

Does your County IT already have a consistent, repeatable framework for planning and deploying modern, spatially enabled IT asset-tracking system?

| Yes (1, 6.25%) No (14, 87.5%) I don't know (1, 6.25%) |  |
| --- | --- |

How does your IT department track the physical locations of your IT assets?

| Street Address (3, 18.75%) Network topology location (by network connection) (3, 18.75%) Other (3, 18.75%) I don't know (1, 6.25%) others (0, 0%) |  |
| --- | --- |

How does your IT department display/visualize the physical locations of your IT assets?

| We don't have this ability (6, 37.5%) Organizational campus maps (2, 12.5%) Network topology maps with spatial clustering (1, 6.25%) Other (1, 6.25%) others (0, 0%) |  |
| --- | --- |

How many distinct office locations does your county occupy (not including employees’ work-from-home offices)?

| 15 or more (14, 87.5%) 10 to 14 (1, 6.25%) 5 to 9 (1, 6.25%) Less than 5 (0, 0%) |  |
| --- | --- |

Do you have any additional comments or details related to mapping/visualizing IT assets’ locations?

| “This is exciting. I was afraid of being saddled in a boring project. This is not boring. I could see this extending into the parking lot for LE Agencies, i.e. patrol vehicles. Also, Radio sites, rack elevation.” “Sounds like a really cool tool idea.” “No” “Kings County is pretty small, so we don't really need such specific location tracking for assets. We use the Dell Asset tag as part of the PC name so we can find a machine if it moves to another network segment if needed. But I could definitely see the need for a large County.” “I've worked for a few larger departments and each one typically created bar codes for the jack location of where the equipment would be assigned. For laptops and other mobile devices we assigned them to the employee's badge number.” “I'm familiar with the tools and features from ESRI. A consideration if that's where your leaning is that not all county IT agencies manage ESRI for their respective counties. When I was at Ventura, IT Services did, but here in Orange County, Public Works does and they don't share. It would be nice though for us with over 200 locations. Let me know how I can help. Thanks!” |
| --- |

In many counties, IT asset data is:

Fragmented across spreadsheets, ticketing systems, and procurement tools

Inconsistently tracked where the asset is currently located

Lacking full lifecycle visibility (purchase → deployment → support → retirement)

Without a centralized asset management approach, counties often face:

Incomplete or outdated inventories

Difficulty tracking asset ownership, lifecycle, and location

Redundant purchases across departments

A plan for replacements and upgrades

Audit findings related to asset control and depreciation

Increased risk of loss, theft, or unsupported equipment

Respond efficiently to audits, security incidents, or public records requests

### User Stories

- 1. County IT Director  
  As a County IT Director, I want to see a high-level, real-time view of IT assets and service activity across county facilities so that I can make informed decisions about staffing, investment, and risk.

- 2. IT Operations Manager  
  As an IT Operations Manager, I want to assign service requests based on technician proximity and workload so that incidents are resolved faster and resources are used efficiently.

- 3. GIS Program Manager  
  As a GIS Program Manager, I want indoor maps to reflect current asset and location data so that spatial information remains trusted and useful across departments.

- 4. IT Asset Manager  
  As an IT Asset Manager, I want to understand where assets are physically located and how often they require service so that I can improve lifecycle planning and reduce unplanned downtime.

- 5. IT Service Desk Supervisor  
  As a Service Desk Supervisor, I want incoming tickets to be automatically associated with specific assets and locations so that triage and escalation decisions are faster and more accurate.

- 6. County IT Service Technician  
  As an IT Service Technician, I want to navigate directly to the correct building, floor, and room and view an asset’s service history so that I can complete repairs efficiently on the first visit.

- 7. County Employee (End User)  
  As a County employee, I want to submit a service request tied to my location so that support staff can find and assist me without additional back-and-forth.

- 8. Facilities and IT Coordination Lead  
  As a Facilities and IT coordination lead, I want shared visibility into building layouts and technology assets so that facilities changes and IT work can be planned together.

- 9. County Executive or Department Head  
  As a County executive, I want summary dashboards that show service performance and asset health by facility so that I can understand operational impacts without reviewing technical details.

- 10. Auditor or Compliance Officer  
  As an auditor, I want clear records linking assets, locations, and service activities so that compliance, accountability, and reporting requirements can be met efficiently.

### Business Value

IT Asset Tracking and Location Management project delivers meaningful and measurable business value by transforming how an organization understands, secures, and manages its technology investments.

At its core, the initiative provides real-time visibility into the IT environment. Instead of relying on spreadsheets, fragmented systems, or outdated manual records, the organization gains a centralized, authoritative source of truth for every county-owned device. Each asset’s location, status, and assigned custodian are clearly documented and continuously updated. This clarity establishes accountability at every level—no device exists without ownership, and no transfer occurs without record. For leadership, this means accurate, dependable insight into the entire technology landscape, enabling informed decision-making based on verified data rather than estimates or assumptions.

Beyond visibility, the project significantly reduces loss, theft, and unnecessary replacement costs. When assets are tracked consistently and monitored throughout their lifecycle, missing or misplaced equipment can be quickly identified and investigated. Stronger check-in, check-out, and transfer controls prevent gaps in custody that often lead to shrinkage. Over time, the organization avoids avoidable repurchases, minimizes insurance claims, and preserves the value of taxpayer-funded investments. For executive leadership, this translates directly into financial stewardship and responsible management of public resources.

The benefits extend into cybersecurity and enterprise risk management. A comprehensive asset inventory is foundational to modern security frameworks such as National Institute of Standards and Technology (NIST) and the Center for Internet Security (CIS). By identifying all connected and unmanaged devices, the organization closes blind spots that attackers frequently exploit. Improved endpoint tracking strengthens patch management, enhances incident response, and supports zero-trust security principles. Leadership gains confidence that cyber risk is being systematically reduced, and that the security posture of the organization is aligned with nationally recognized standards.

An asset tracking system also strengthens audit, grant, and compliance readiness. Accurate records of asset ownership, physical location, funding source, and custodial responsibility are readily available when auditors request documentation. Whether responding to capital asset reviews, grant compliance checks [equipment has to be specifically allocated], or IT control assessments, the organization can produce defensible, time-stamped records quickly and efficiently. This reduces staff time spent gathering documentation and lowers the likelihood of audit findings. For leadership, the value is clear: fewer compliance issues, smoother audits, and reduced administrative burden.

Finally, the project enhances operational efficiency and service reliability. When IT teams know exactly where devices are located and who is responsible for them, they spend less time searching for equipment and more time resolving issues. Incident response becomes faster, service disruptions are minimized, and equipment can be rapidly redeployed during emergencies, disasters, or staffing transitions. This agility ensures continuity of operations and sustained uptime for critical services. For leadership, the result is a more responsive organization capable of maintaining reliable technology services even under pressure.

In summary, an IT Asset Tracking and Location Management project is not simply a technical upgrade—it is an investment in visibility, accountability, financial stewardship, cybersecurity resilience, compliance readiness, and operational excellence.

## Architecture Implications of the County Context

The county context supports three core design requirements. First, the integration must handle geographically distributed facilities rather than one building or one campus. Second, it must treat asset location as an operational and compliance issue, not merely a map-display convenience. Third, it must generate value for multiple roles: technicians, service desk supervisors, asset managers, GIS program managers, IT directors, executives, and auditors.

| Source theme | Integration implication | Architecture response |
| --- | --- | --- |
| Distributed buildings and campuses | Tickets and assets need facility, level, unit, and route context. | Maintain an ArcGIS Indoors crosswalk to ServiceNow locations and assets. |
| Audit, public records, cybersecurity, and licensing pressure | Asset state must be traceable and defensible. | Keep ServiceNow authoritative for lifecycle and write integration activity to logs. |
| Need for technician deployment support | Work must be dispatchable by place, not only by queue. | Generate map links, floor-aware context, and operational dispatch layers. |
| Leadership decision-making | Reporting must connect work, assets, and places. | Build dashboards and summary views by building, floor, department, asset type, and incident pattern. |
