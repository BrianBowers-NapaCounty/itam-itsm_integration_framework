# Infrastructure Configuration
Configuration details.

<div class="rc3-extension">

## Expanded 1.0.0 Guidance

```{image} /_images/symbol-information.png
:alt: 1-1-4-configuration
:width: 64px
:class: page-symbol
```

<div>

#### Infrastructure Configuration

For the on-prem pattern, IIS can front the Flask application, terminate or pass TLS depending on policy, restrict paths, forward requests to the Python application runtime, and provide familiar Windows operations support. ArcGIS Web Adaptor may also run under IIS for ArcGIS Enterprise components; however, the Flask application should remain separately governed and not be treated as part of the ArcGIS Web Adaptor itself.

<div class="diagram">

<div class="diagram-title">

Deployment lifecycle

</div>

</div>

</div>

</div>
