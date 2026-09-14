```{image} /_images/symbol-microscope2.png
:alt: Testing, Monitoring, and Failure Analysis
:width: 64px
:class: page-symbol
```

# Testing, Monitoring, and Failure Analysis

## Testing and Validation Strategy

**Test like an integration service**

Testing should cover code, schemas, permissions, location matching, event ordering, and failure behavior.

| Test Type | What to Test | Example Acceptance Criteria |
| --- | --- | --- |
| Unit tests | Normalization, transforms, status mapping, confidence scoring. | Known inputs produce expected output fields and reason codes. |
| Location-matching tests | Direct ID, crosswalk, alias, duplicate, and no-match scenarios. | High-confidence matches are deterministic; ambiguous matches route to review. |
| API-client tests | ServiceNow and ArcGIS clients with mocked responses. | Pagination, timeout, token, and error paths behave predictably. |
| Integration tests | Non-production end-to-end flow. | Ticket becomes ArcGIS feature and approved fields write back. |
| Security tests | Unsigned webhook, invalid signature, replayed timestamp, unauthorized source. | Request is rejected and logged without queueing. |
| Duplicate-event tests | Same event delivered multiple times. | No duplicate feature and no repeated noisy write-back. |
| Load tests | Expected peak ticket/event volume. | Queue drains within defined service objective. |
| User acceptance tests | Technician and service desk workflows. | Users can understand and use map links and floor context. |

## Monitoring and Metrics

**Operational observability**

Metrics should describe freshness, reliability, backlog, error rate, data quality, and user-facing usefulness.

| Metric | Why It Matters | Suggested Alert |
| --- | --- | --- |
| Queue depth | Shows backlog or stuck workers. | Depth exceeds normal peak threshold. |
| Oldest pending event age | Shows service degradation in user-facing terms. | Oldest event exceeds service objective. |
| Events processed per hour | Measures throughput and operational load. | Unexpected drop to zero during business hours. |
| Retry rate | Indicates API, network, token, or throttling instability. | Retry rate exceeds defined baseline. |
| Dead-letter count | Shows unrecoverable failure volume. | Any critical record enters permanent failure. |
| Location match confidence | Tracks data quality and location-model health. | Median confidence drops or low-confidence count rises. |
| ServiceNow write-back failures | Identifies permission, schema, or loop-prevention issues. | Write-back failures exceed threshold. |
| ArcGIS edit failures | Identifies token, layer, schema, or Portal problems. | Any sustained edit failure window. |
| Reconciliation exception count | Tracks drift between systems. | Exceptions trend upward week over week. |
| Median processing time | Measures integration health and latency. | Processing time exceeds baseline by defined factor. |

## Failure Mode and Effects Analysis

**FMEA for integration operations**

Failure analysis helps teams document what can go wrong, how it is detected, and how the system should respond.

| Failure Mode | Effect | Detection | Mitigation |
| --- | --- | --- | --- |
| Webhook disabled | Events stop arriving. | No new webhook events during active ticket periods. | Scheduled polling fallback and webhook health check. |
| ServiceNow API outage | Records cannot be fetched. | API error logs and retry spike. | Backoff retry; backlog preserved in queue. |
| ArcGIS layer schema changed | Updates fail or attributes are dropped. | Edit failure and schema validation job. | Pause publishing; update field maps; rerun tests. |
| Duplicate room codes | Wrong location match risk. | Multiple candidates from location query. | Exception queue and unique facility-level-unit matching. |
| Expired token | API calls fail. | Authentication errors. | Token refresh, credential rotation, alert. |
| Bad write-back logic | Noisy tickets or update loop. | Repeated update events on same record. | Source flags, idempotency keys, write-back disable switch. |
| Crosswalk corruption | Records map to wrong features. | Reconciliation anomalies and user reports. | Versioned crosswalk backup and review workflow. |
| Portal permission change | Users cannot see maps or layers. | Access-denied reports and sharing audit. | Portal group review and permission baseline. |
