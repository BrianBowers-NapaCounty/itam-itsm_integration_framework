```{image} /_images/symbol-checkmark2.png
:alt: Quick start
:width: 64px
:class: page-symbol
```
# Quick Start

The fastest way to understand Capybara is to run the included **MockConnector** examples. No ServiceNow, TeamDynamix, Cherwell, ArcGIS Online, or Enterprise credentials are required for this demonstration path.

```text
copy docs\editions\alpha\4-scripts\files\config.example.toml config.toml
python docs/editions/alpha/4-scripts/files/06_reporting/report_on_hold_parts.py --config config.toml
python docs/editions/alpha/4-scripts/files/05_notifications_alerts/alert_missing_assets.py --config config.toml
python docs/editions/alpha/4-scripts/files/09_historical_analytics/capture_daily_snapshot.py --config config.toml
```

The sequence demonstrates the architecture end-to-end: normalized ITSM records -> operational logic -> management output -> historical analytics.
