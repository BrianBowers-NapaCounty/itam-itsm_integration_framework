```{image} /_images/symbol-microscope2.png
:alt: 3-4-troubleshooting-guide
:width: 64px
:class: page-symbol
```

<div>

### Troubleshooting Guide

<div class="table-wrap">

| Symptom                                         | Likely Cause                                                                                             | Recommended Action                                                                                                                         |
|-------------------------------------------------|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Ticket appears in ServiceNow but not on the map | No matching location, failed sync, API permission failure, or filtered status                            | Check queue/log entry, verify location crosswalk, confirm layer edit permissions, and run manual reconciliation.                           |
| Asset appears on the wrong floor                | Ambiguous room code, stale floor mapping, duplicate unit name, or missing facility context               | Require facility + level + unit matching and add a confidence score or exception review queue.                                             |
| Map link opens but shows no feature             | Feature was not created, URL parameters are stale, permissions block access, or layer definition changed | Validate feature ID, layer URL, user permissions, and web map item configuration.                                                          |
| Webhook fires repeatedly                        | Status write-back triggers a new outbound event loop                                                     | Add source-system flags, event deduplication, idempotency keys, or business-rule exclusions.                                               |
| Integration account suddenly fails              | Expired credential, rotated secret, disabled account, MFA change, or permission update                   | Check secrets store, account status, token lifetime, OAuth client, and audit logs.                                                         |
| Dashboard counts do not match ServiceNow        | Time-window mismatch, filtering mismatch, failed records, or derived layer design                        | Document dashboard filters, compare counts by status/date/facility, and run reconciliation report.                                         |
| Updates are slow or unreliable                  | Large payloads, missing pagination, API throttling, inefficient queries, or network latency              | Use incremental sync, pagination, batching, retry backoff, and field minimization.                                                         |
| Duplicate features are created                  | Missing unique key, non-idempotent create logic, or crosswalk failure                                    | Use upsert behavior, enforce unique integration keys, and reconcile duplicates before expanding scope.                                     |
| Users cannot see the mapped content             | Portal sharing, group membership, license, or item permission issue                                      | Check item sharing, group access, Indoors privileges, role permissions, and user type.                                                     |
| Security review blocks deployment               | Unclear boundary, exposed endpoint, overprivileged integration account, or insufficient logging          | Provide data-flow diagrams, least-privilege roles, credential storage design, endpoint protection, audit logs, and incident response plan. |

</div>

#### Resource Type Symbols

Future downloadable assets use file-type symbols as consistent markers for the kind of material being referenced.

<div>

<span class="semantic-role-chip" semantic-role="file_py">Python script</span><span class="semantic-role-chip" semantic-role="file_ipynb">Jupyter notebook</span><span class="semantic-role-chip" semantic-role="file_xlsx">XLSX calculator / workbook</span><span class="semantic-role-chip" semantic-role="file_pptx">PPTX presentation</span><span class="semantic-role-chip" semantic-role="file_pdf">PDF deliverable</span><span class="semantic-role-chip" semantic-role="file_docx">DOCX deliverable</span><span class="semantic-role-chip" semantic-role="file_md">Markdown source</span><span class="semantic-role-chip" semantic-role="file_zip">ZIP release bundle</span><span class="semantic-role-chip" semantic-role="file_htmlzip">Web documentation package</span>

</div>

</div>