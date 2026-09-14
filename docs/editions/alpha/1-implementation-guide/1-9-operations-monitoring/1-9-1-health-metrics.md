```{image} /_images/symbol-microscope2.png
:alt: Health Metrics and Service Monitoring
:width: 64px
:class: page-symbol
```

# Health Metrics and Service Monitoring

| Metric | Why it matters | Suggested alert |
| --- | --- | --- |
| Webhook receipt count | Detect event interruptions from ServiceNow. | No events during business hours when expected. |
| Queue depth | Detect processing backlog. | Queue depth above threshold for 15+ minutes. |
| Dead-letter count | Detect unprocessable events. | Any dead-letter in production triggers review. |
| ArcGIS edit failures | Detect layer schema, permission, or service issues. | Failure rate above threshold. |
| ServiceNow API failures | Detect auth, rate, schema, or instance problems. | 401/403 immediate; 429/5xx retry policy. |
| Unmatched location rate | Measure quality of location crosswalk. | Rate above agreed tolerance. |
| Reconciliation drift | Detect records missing from either side. | Any high-priority ticket missing from operational layer. |
