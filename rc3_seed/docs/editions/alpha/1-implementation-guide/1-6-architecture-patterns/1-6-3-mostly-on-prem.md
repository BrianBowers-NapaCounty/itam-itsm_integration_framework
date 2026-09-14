```{image} /_images/symbol-heavylift.png
:alt: Pattern 1 — Mostly On-Prem ArcGIS Enterprise + IIS/Flask
:width: 64px
:class: page-symbol
```

```{image} /_images/logo-servicenow.png
:alt: Pattern 1 — Mostly On-Prem ArcGIS Enterprise + IIS/Flask
:width: 150px
:class: page-logo
```

# Pattern 1 — Mostly On-Prem ArcGIS Enterprise + IIS/Flask

Pattern 1 is the default Capybara architecture for local governments that already host ArcGIS Enterprise and SQL Server internally. ServiceNow is cloud-hosted, but it only sends outbound HTTPS events. The county controls the middleware, ArcGIS Enterprise, data, network boundaries, and logs.

Pattern 1 — Mostly on-prem with outbound ServiceNow REST

Python

Diagram

```mermaid
flowchart LR
    subgraph SNCloud["ServiceNow Cloud"]
        SN["ServiceNow ITSM / ITAM"]
        BR["Business Rule / Flow / Outbound REST Message"]
    end

    subgraph CountyEdge["County Edge / IIS"]
        FW["Firewall / WAF"]
        IIS["IIS"]
        Flask["Flask Webhook Endpoint"]
    end

    subgraph MW["Python Middleware"]
        Q[("integration_event_queue")]
        Worker["Worker Processor"]
        CW[("Crosswalk + Sync DB")]
        Log[("Audit / Retry / Dead-letter")]
        Poll["Scheduled Polling Job"]
    end

    subgraph Arc["On-Prem ArcGIS Enterprise"]
        Portal["Portal for ArcGIS"]
        Server["ArcGIS Server"]
        GDB[("SQL Server Enterprise Geodatabase")]
        Indoors["ArcGIS Indoors Apps / Dashboards"]
    end

    SN --> BR
    BR -->|"HTTPS POST JSON"| FW
    FW --> IIS
    IIS --> Flask
    Flask -->|"validate + enqueue"| Q
    Q --> Worker
    Poll -->|"delta queries"| SN
    Poll --> Q
    Worker -->|"ServiceNow REST GET/PATCH"| SN
    Worker -->|"ArcGIS API for Python"| Portal
    Portal --> Server
    Server --> GDB
    Server --> Indoors
    Worker --> CW
    Worker --> Log
    Worker -->|"map URLs / place IDs / work notes"| SN

    style SN fill:#B3717A,color:#fff
    style BR fill:#B3717A,color:#fff
    style Flask fill:#908849,color:#fff
    style Worker fill:#908849,color:#fff
    style Poll fill:#908849,color:#fff
    style Portal fill:#669DD5,color:#fff
    style Server fill:#669DD5,color:#fff
    style Indoors fill:#669DD5,color:#fff
```

#### Pattern 1 technical steps

1. ServiceNow business rule, flow, or outbound REST message identifies a relevant record event.
2. ServiceNow sends a small signed JSON payload to the Flask endpoint.
3. IIS/WAF enforces TLS, host headers, request size, and routing.
4. Flask validates authentication, timestamp, replay window, event schema, and allowed table/event type.
5. Flask stores the event and returns `202 Accepted`.
6. A worker claims the event, fetches authoritative records from ServiceNow, and resolves references.
7. The matcher resolves locations/assets to Indoors units/assets.
8. The ArcGIS client queries and edits feature layers.
9. The writer patches ServiceNow with map context and status.
10. Logs and reconciliation reports preserve traceability.
