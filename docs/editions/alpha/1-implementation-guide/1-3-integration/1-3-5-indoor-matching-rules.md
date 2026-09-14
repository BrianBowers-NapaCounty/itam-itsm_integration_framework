```{image} /_images/symbol-arcgisindoors.png
:alt: Indoor Matching Rules
:width: 64px
:class: page-symbol
```

# Indoor Matching Rules

1. Persisted crosswalk key: ServiceNow location sys\_id or CI sys\_id already mapped to an ArcGIS unit or asset.
2. Deterministic code match: building\_code + floor\_code + room\_code.
3. Asset identifier match: asset\_tag, serial\_number, barcode, hostname, or MAC address where appropriate.
4. Controlled alias table: locally approved aliases for room names, department areas, shared spaces, or common equipment names.
5. Fuzzy match with confidence score: allowed only when ambiguous results go to review.
6. Manual review queue: no automatic map assignment if confidence falls below threshold.
