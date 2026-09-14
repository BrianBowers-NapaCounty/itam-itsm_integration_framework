```{image} /_images/symbol-heavylift.png
:alt: Pattern 3 — Reliable and Secure Brokered Architecture
:width: 64px
:class: page-symbol
```

# Pattern 3 — Reliable and Secure Brokered Architecture

The recommended advanced pattern uses a brokered event core. Instead of having Flask do any long-running work, Flask only authenticates and queues. Worker pools process events with idempotency, backoff, dead-letter handling, and strict rate controls. Observability is built in from day one.

#### Advanced controls

- Idempotency keys prevent duplicate events from producing duplicate features or notes.
- Dead-letter queues preserve failed events for manual review.
- Worker leasing prevents two workers from processing the same event simultaneously.
- Separate read and write service accounts reduce blast radius.
- Rate-limiting protects both ServiceNow and ArcGIS Enterprise from retry storms.
- Observable correlation IDs make cross-system troubleshooting realistic.
