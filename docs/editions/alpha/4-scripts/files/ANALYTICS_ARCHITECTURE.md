# Capybara Historical Analytics Architecture

## Why persist history?

ITSM and operational GIS layers usually describe the **current** state well.
Questions such as these require durable history:

- How did backlog change over the last year?
- Is the unmatched-location rate improving?
- Which facilities consistently generate the most service demand?
- Are procurement holds becoming longer?
- Did asset-loss exceptions increase this quarter?
- Was last week's sync reliability worse than the prior four weeks?
- Which assignment groups repeatedly carry aging work?

The analytics subsystem therefore treats historical facts as a separate,
append-oriented data product.

## Recommended hosted service

One hosted feature service, for example:

`Capybara_Analytics`

containing nonspatial hosted tables:

1. `Analytics_Runs`
2. `Metric_Snapshots`
3. `Ticket_Daily`
4. `Asset_Daily`
5. `Event_History`
6. `Sync_Health`
7. `Reconciliation_History`
8. `Period_Summaries`
9. `Data_Quality_Snapshots`

These tables are dashboard-friendly and can be shared more restrictively than
the source ITSM system.

## Data grain

### Metric_Snapshots
One row per `metric_code` + period + dimension combination.

### Ticket_Daily
One row per day + facility/level/assignment/status dimension combination.

### Asset_Daily
One row per day + facility/department/status dimension combination.

### Event_History
One row per normalized state transition or significant integration event.

### Sync_Health
One row per health sampling interval.

### Reconciliation_History
One row per reconciliation issue or aggregated issue family.

## Reporting windows

The reusable window library supports:

- 1 year / 365 days
- 6 months
- 3 months
- last 90 / 30 / 14 / 7 days
- yesterday
- current week-to-date
- previous week
- current month-to-date
- previous month
- current quarter-to-date
- previous quarter
- current year-to-date
- previous year
- custom start/end

Both rolling windows and calendar-aligned windows are useful. They answer
different questions and should not be treated as interchangeable.

## Data retention

Fine-grained events may be retained for a shorter period than summarized
daily/monthly facts. A practical pattern is:

- event history: 12–24 months;
- health samples: 12 months;
- daily facts: several years;
- monthly/period summaries: long-term;
- run manifests: long-term.

Local policy should control the actual schedule.

## Dashboard architecture

ArcGIS Dashboards, Experience Builder, notebooks, or external BI tools can read
the hosted analytics tables without direct access to ServiceNow/Cherwell/TDX.

This reduces coupling between management reporting and live operational APIs.
