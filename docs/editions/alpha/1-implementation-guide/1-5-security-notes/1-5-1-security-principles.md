```{image} /_images/symbol-exclamation2.png
:alt: 1-5-1-security-principles
:width: 64px
:class: page-symbol
```

<div>

### Security Principles

- Prefer outbound ServiceNow-to-middleware communication over opening database access.
- Validate every incoming webhook using token, signature, timestamp, replay detection, and source restrictions.
- Run the Python bridge as a dedicated service identity with narrowly scoped permissions.
- Use HTTPS/TLS for every network hop.
- Store secrets outside source code in an approved vault or OS-protected secret store.
- Log correlation IDs, event IDs, source table, source sys_id, processing status, API response codes, and affected layer IDs.
- Redact secrets and sensitive personal data from logs.
- Separate dev, test, and production environments.

</div>