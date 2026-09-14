```{image} /_images/symbol-technicalnote.png
:alt: Operations Runbook Checklist
:width: 64px
:class: page-symbol
```

# Operations Runbook Checklist

- Verify ServiceNow outbound REST event rule is active.
- Confirm Flask health endpoint responds internally and externally as intended.
- Check certificate expiration dates for IIS, ArcGIS, and ServiceNow integration endpoints.
- Review queue depth, retry count, and dead-letter queue daily during pilot.
- Run reconciliation after schema changes, ServiceNow upgrades, ArcGIS upgrades, and middleware releases.
- Export and archive integration logs according to local retention policy.
- Test credential rotation in non-production before enforcing production rotation.
