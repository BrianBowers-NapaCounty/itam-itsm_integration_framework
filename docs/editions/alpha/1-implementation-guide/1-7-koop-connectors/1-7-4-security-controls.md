```{image} /_images/symbol-important.png
:alt: Koop Security and Implementation Controls
:width: 64px
:class: page-symbol
```

```{image} /_images/logo-servicenow.png
:alt: Koop Security and Implementation Controls
:width: 150px
:class: page-logo
```

# Koop Security and Implementation Controls

## Security Treatment

The three patterns have different security postures. The Koop pattern exposes an ArcGIS-like endpoint that queries ServiceNow. The ArcGIS for ServiceNow pattern delegates more of the integration surface to a vendor-supported product. The Capybara pattern exposes a local webhook endpoint and outbound API clients that persist integration state. None of these is automatically safer than the others; each needs explicit controls.

| Security topic | Koop-based pattern | ArcGIS for ServiceNow | Capybara Python middleware |
| --- | --- | --- | --- |
| Credential exposure | Node/Koop service needs ServiceNow read credentials; Python loader needs ServiceNow location write permissions. | Credentials and delegated access depend on product design and admin configuration. | ServiceNow and ArcGIS service-account credentials are held by middleware/secrets vault. |
| Network exposure | FeatureServer façade may need to be reachable by ArcGIS clients; should be behind TLS, reverse proxy, and access controls. | Depends on deployment of ServiceNow app, custom data feed, and ArcGIS Enterprise/Online access. | Webhook endpoint receives ServiceNow outbound REST; should be behind WAF/IIS/API gateway and strict validation. |
| Authorization model | Must prevent users from querying more incidents/requests than they are allowed to see. | Must validate ServiceNow and ArcGIS identity propagation and object-level access behavior. | Middleware must enforce scope through service-account permissions, layer sharing, and dashboard segmentation. |
| Data minimization | Provider should expose only necessary fields, not raw incident/request payloads. | Connector/app configuration should limit displayed and queryable fields. | Mapper should write only dispatch/reporting fields into ArcGIS operational layers. |
| Auditability | Requires custom logs for ServiceNow API calls, FeatureServer queries, errors, and cache behavior. | Should use vendor logs plus local ArcGIS/ServiceNow audit logs. | Built-in queue/log/retry/dead-letter tables support auditability if implemented. |
| Staleness | Live query can be fresh, but caching or API failures may create stale map output. | Public descriptions emphasize live ServiceNow data, but freshness guarantees must be validated. | Derived layers need sync timestamps, reconciliation, and stale-data warnings. |

## Implementation Controls if Koop Is Used

1. **Modernize dependencies:** Review Node.js, Koop, request libraries, and package vulnerabilities before any deployment.
2. **Restrict ServiceNow fields:** Expose only the fields required for maps and dashboards.
3. **Implement authorization:** Do not expose a public unauthenticated FeatureServer façade over incident/request data.
4. **Prefer pass-through filters:** Translate safe attribute and time filters to ServiceNow queries to reduce payload size.
5. **Avoid premature limits:** Do not apply a ServiceNow result limit before required filters are applied unless the result semantics are documented.
6. **Protect location imports:** Treat the Python loader as a governed data-publication process with staging, validation, rollback, and audit logs.
7. **Separate environments:** Use dev/test ServiceNow and ArcGIS environments before production.
8. **Monitor actively:** Track ServiceNow API errors, endpoint latency, cache age, query volume, and rejected requests.
9. **Document support boundaries:** Identify who owns Node/Koop runtime, ServiceNow scripts, ArcGIS maps, and data stewardship.
