# Frequently Asked Questions

<img class="capybara-right" src="/en/latest/_images/BG.png" alt="Capybara standing with question marks above his head" style="max-height: 200px !important; width:auto !important; filter: sepia(25%);">**What is the Capybara Framework?**
   The Capybara Framework is a structured approach for integrating IT Asset Management (ITAM) and IT Service Management (ITSM) systems with indoor spatial data in ArcGIS Indoors. It provides patterns, guidance, and tools to unify operational IT workflows with physical location context.

**Who should use Capybara?**
   Capybara is designed for IT administrators, GIS analysts, facilities managers, and operations staff who need to coordinate IT assets and services across indoor spaces. It is useful for organizations seeking to improve situational awareness and decision-making with spatially-enabled IT data.

**Which platforms are supported?**
   While Capybara frequently references ArcGIS Indoors and common ITSM platforms, it is largely vendor-agnostic. The framework focuses on integration patterns and conventions rather than specific products, allowing adaptation to a variety of systems.

**How do I start an implementation?**
   Implementation typically begins with understanding your existing ITAM/ITSM systems, mapping indoor spatial data, and planning integration workflows. The Implementation Guide provides step-by-step instructions for initial setup, prerequisites, and configuration.

**Can Capybara be used incrementally?**
   Yes. The framework is designed to allow phased adoption. Organizations can start with basic integrations or pilot deployments and expand coverage and automation as workflows mature.

**What types of automation are included?**
   Capybara provides Python scripts and Jupyter notebooks for tasks such as data validation, reporting, asset synchronization, and workflow automation. These can be customized to suit local environments and operational needs.

**How does Capybara handle large or complex datasets?**
   The framework emphasizes scalable design and data management best practices. It includes guidance for organizing, validating, and synchronizing large datasets, as well as automating repetitive tasks to maintain data integrity.

**Are there templates or reference materials available?**
   Yes. Capybara includes document templates, checklists, cheat sheets, and visual resources such as diagrams, icons, and screenshots to support project planning, communication, and operational execution.

**How do I maintain the system over time?**
   The framework includes maintenance guidance, including recommended workflows for updating data, managing changes, monitoring system health, and extending functionality without disrupting existing integrations.

**Can the framework be adapted to other environments?**
    Absolutely. Capybara’s principles, patterns, and tools can be applied in various organizational contexts and indoor environments. While examples reference ArcGIS Indoors, the underlying concepts can be adapted to different GIS or IT management platforms.

<div class="rc3-extension">

## Expanded 1.0.0 Guidance

```{image} /_images/symbol-information.png
:alt: 2-1-faq
:width: 64px
:class: page-symbol
```

<div>

### Frequently Asked Questions

#### Does ServiceNow call Flask directly?

In Pattern 1, yes. ServiceNow sends an outbound REST message to a protected Flask endpoint. Pattern 3 may place an API gateway or broker in front of Flask.

#### Does Python own ticket data?

No. Python owns integration state only: queues, logs, crosswalks, retry records, timestamps, and transformation rules.

#### Should ArcGIS Indoors store all ServiceNow fields?

No. Store only the fields required for map display, dashboarding, dispatch, analysis, and reconciliation.

#### Is ArcGIS for ServiceNow a replacement?

Potentially for some workflows, once available and validated. It should be evaluated as a vendor-supported option, not assumed to replace all governance-specific middleware logic.

</div>

</div>
