```{image} /_images/symbol-telescope.png
:alt: Architecture Pattern Selection
:width: 64px
:class: page-symbol
```

# Architecture Pattern Selection

| Criterion | Pattern 1: Mostly On-Prem | Pattern 2: Azure VM | Pattern 3: Advanced Brokered HA | Pattern 4: ArcGIS for ServiceNow |
| --- | --- | --- | --- | --- |
| Primary goal | Use existing on-prem ArcGIS Enterprise and IIS/SQL Server skills. | Move the same pattern to cloud-hosted VMs and Azure controls. | Harden for reliability, queueing, observability, security, and scale. | Adopt vendor-supported ServiceNow/ArcGIS integration capabilities. |
| Custom Python | High | High | High but modularized | Low to moderate depending on gaps |
| Ingress model | ServiceNow outbound REST to IIS/Flask | ServiceNow outbound REST to Azure WAF/App Gateway/Flask | API gateway + broker + worker pool | Vendor connector / ServiceNow app mechanisms |
| Best for | County with mature on-prem GIS | County with Azure-first infrastructure | Mission-critical or multi-agency usage | Future simplified/vendor-supported deployment |
| Main caution | Webhook exposure and middleware operations | Cost, latency, network routing, and cloud governance | Complexity and operational maturity required | Release status, licensing, feature fit, and support boundaries |
