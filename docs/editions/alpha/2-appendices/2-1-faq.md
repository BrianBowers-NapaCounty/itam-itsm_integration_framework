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