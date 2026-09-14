# Metrics Catalog

Metric definitions are centralized so dashboards, notebooks, and scheduled reports use the same names and units.

| Code | Label | Unit | Source | Interpretation |
| --- | --- | --- | --- | --- |
| `assets.missing` | Missing/lost/stolen assets | count | assets | Current-state/count metric; review alongside the selected period and dimensions. |
| `assets.spare` | Spare assets | count | assets | Current-state/count metric; review alongside the selected period and dimensions. |
| `assets.total` | Assets | count | assets | Current-state/count metric; review alongside the selected period and dimensions. |
| `tickets.active` | Active tickets | count | tickets | Current-state/count metric; review alongside the selected period and dimensions. |
| `tickets.location_known_rate` | Ticket known-location rate | ratio | tickets | Ratio from 0 to 1; trend direction should be interpreted from the metric label. |
| `tickets.on_hold` | Tickets on hold | count | tickets | Current-state/count metric; review alongside the selected period and dimensions. |
| `tickets.total` | Tickets | count | tickets | Current-state/count metric; review alongside the selected period and dimensions. |
| `tickets.unassigned` | Unassigned active tickets | count | tickets | Current-state/count metric; review alongside the selected period and dimensions. |
