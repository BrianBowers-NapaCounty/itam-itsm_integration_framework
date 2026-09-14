```{image} /_images/symbol-exclamation2.png
:alt: 1-5-2-security-considerations
:width: 64px
:class: page-symbol
```

<div>

### Security Considerations for Capybara Integration

<div class="table-wrap">

| Threat / risk                   | Control                                   | Operational detail                                                                                     |
|---------------------------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Forged webhook                  | Signed request header or OAuth token      | Reject requests with invalid signatures, old timestamps, or unknown event IDs.                         |
| Replay attack                   | Timestamp window + idempotency key        | Store event hash and reject duplicates outside accepted replay rules.                                  |
| Over-privileged service account | Least privilege and scoped groups         | ArcGIS account should edit only required layers. ServiceNow account should patch only approved fields. |
| Data leakage through dashboards | Layer-level and app-level access controls | Separate technician, manager, and leadership views.                                                    |
| Stale operational layers        | Reconciliation and freshness indicators   | Dashboards should show last sync, queue depth, and stale-data warnings.                                |
| Credential exposure             | Vaulting and rotation                     | Do not store tokens in scripts, notebooks, Git repositories, or web.config files without protection.   |

</div>

<div class="diagram">

<div class="diagram-title">

Security boundary model

</div>

</div>

</div>