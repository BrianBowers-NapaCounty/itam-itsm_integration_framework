# Analytics Data Dictionary

The analytics service is designed as a hosted feature service containing nonspatial tables on ArcGIS Online or ArcGIS Enterprise Portal.

## `Analytics_Runs`

| Field | ArcGIS type | Purpose |
| --- | --- | --- |
| `OBJECTID` | `esriFieldTypeOID` | ArcGIS-managed row identifier. |
| `RUN_ID` | `esriFieldTypeString` | Execution identifier used to connect rows to one capture/run. |
| `RUN_TYPE` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `STARTED_UTC` | `esriFieldTypeDate` | Operational/history field for this table grain. |
| `FINISHED_UTC` | `esriFieldTypeDate` | Operational/history field for this table grain. |
| `STATUS` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `ROWS_WRITTEN` | `esriFieldTypeInteger` | Operational/history field for this table grain. |
| `MESSAGE` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `CORRELATION` | `esriFieldTypeString` | Operational/history field for this table grain. |

## `Metric_Snapshots`

| Field | ArcGIS type | Purpose |
| --- | --- | --- |
| `OBJECTID` | `esriFieldTypeOID` | ArcGIS-managed row identifier. |
| `OBSERVED_UTC` | `esriFieldTypeDate` | UTC observation timestamp. |
| `PERIOD_CODE` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `PERIOD_START` | `esriFieldTypeDate` | Operational/history field for this table grain. |
| `PERIOD_END` | `esriFieldTypeDate` | Operational/history field for this table grain. |
| `METRIC_CODE` | `esriFieldTypeString` | Stable machine-readable metric identifier. |
| `METRIC_LABEL` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `METRIC_VALUE` | `esriFieldTypeDouble` | Numeric metric observation. |
| `UNIT` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `DIMENSION` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `DIM_VALUE` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `SOURCE_COUNT` | `esriFieldTypeInteger` | Operational/history field for this table grain. |
| `RUN_ID` | `esriFieldTypeString` | Execution identifier used to connect rows to one capture/run. |

## `Ticket_Daily`

| Field | ArcGIS type | Purpose |
| --- | --- | --- |
| `OBJECTID` | `esriFieldTypeOID` | ArcGIS-managed row identifier. |
| `DAY` | `esriFieldTypeDate` | Operational/history field for this table grain. |
| `FACILITY_ID` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `LEVEL_ID` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `LOCATION_ID` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `ASSIGN_GROUP` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `CATEGORY` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `OPENED` | `esriFieldTypeInteger` | Operational/history field for this table grain. |
| `CLOSED` | `esriFieldTypeInteger` | Operational/history field for this table grain. |
| `ACTIVE` | `esriFieldTypeInteger` | Operational/history field for this table grain. |
| `ON_HOLD` | `esriFieldTypeInteger` | Operational/history field for this table grain. |
| `UNASSIGNED` | `esriFieldTypeInteger` | Operational/history field for this table grain. |
| `SLA_BREACHED` | `esriFieldTypeInteger` | Operational/history field for this table grain. |
| `AVG_AGE_HOURS` | `esriFieldTypeDouble` | Operational/history field for this table grain. |
| `RUN_ID` | `esriFieldTypeString` | Execution identifier used to connect rows to one capture/run. |

## `Asset_Daily`

| Field | ArcGIS type | Purpose |
| --- | --- | --- |
| `OBJECTID` | `esriFieldTypeOID` | ArcGIS-managed row identifier. |
| `DAY` | `esriFieldTypeDate` | Operational/history field for this table grain. |
| `FACILITY_ID` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `LOCATION_ID` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `DEPARTMENT` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `ASSET_STATUS` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `ASSET_COUNT` | `esriFieldTypeInteger` | Operational/history field for this table grain. |
| `MISSING_COUNT` | `esriFieldTypeInteger` | Operational/history field for this table grain. |
| `SPARE_COUNT` | `esriFieldTypeInteger` | Operational/history field for this table grain. |
| `ASSIGNED_COUNT` | `esriFieldTypeInteger` | Operational/history field for this table grain. |
| `UNASSIGNED_COUNT` | `esriFieldTypeInteger` | Operational/history field for this table grain. |
| `RUN_ID` | `esriFieldTypeString` | Execution identifier used to connect rows to one capture/run. |

## `Event_History`

| Field | ArcGIS type | Purpose |
| --- | --- | --- |
| `OBJECTID` | `esriFieldTypeOID` | ArcGIS-managed row identifier. |
| `EVENT_UTC` | `esriFieldTypeDate` | Operational/history field for this table grain. |
| `EVENT_TYPE` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `RECORD_TYPE` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `RECORD_ID` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `PUBLIC_ID` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `FIELD_NAME` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `OLD_VALUE` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `NEW_VALUE` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `LOCATION_ID` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `ASSET_ID` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `CORRELATION` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `RUN_ID` | `esriFieldTypeString` | Execution identifier used to connect rows to one capture/run. |

## `Sync_Health`

| Field | ArcGIS type | Purpose |
| --- | --- | --- |
| `OBJECTID` | `esriFieldTypeOID` | ArcGIS-managed row identifier. |
| `OBSERVED_UTC` | `esriFieldTypeDate` | UTC observation timestamp. |
| `CONNECTOR_OK` | `esriFieldTypeSmallInteger` | Operational/history field for this table grain. |
| `ARCGIS_OK` | `esriFieldTypeSmallInteger` | Operational/history field for this table grain. |
| `SYNC_LAG_MIN` | `esriFieldTypeDouble` | Operational/history field for this table grain. |
| `UNMATCHED_RATE` | `esriFieldTypeDouble` | Operational/history field for this table grain. |
| `API_FAILURE_RATE` | `esriFieldTypeDouble` | Operational/history field for this table grain. |
| `QUEUE_DEPTH` | `esriFieldTypeInteger` | Operational/history field for this table grain. |
| `DEAD_LETTERS` | `esriFieldTypeInteger` | Operational/history field for this table grain. |
| `MESSAGE` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `RUN_ID` | `esriFieldTypeString` | Execution identifier used to connect rows to one capture/run. |

## `Reconciliation_History`

| Field | ArcGIS type | Purpose |
| --- | --- | --- |
| `OBJECTID` | `esriFieldTypeOID` | ArcGIS-managed row identifier. |
| `OBSERVED_UTC` | `esriFieldTypeDate` | UTC observation timestamp. |
| `RECORD_TYPE` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `RECORD_ID` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `ISSUE_CODE` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `SEVERITY` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `SAFE_REPAIR` | `esriFieldTypeSmallInteger` | Operational/history field for this table grain. |
| `SOURCE_VALUE` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `TARGET_VALUE` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `RUN_ID` | `esriFieldTypeString` | Execution identifier used to connect rows to one capture/run. |

## `Period_Summaries`

| Field | ArcGIS type | Purpose |
| --- | --- | --- |
| `OBJECTID` | `esriFieldTypeOID` | ArcGIS-managed row identifier. |
| `GENERATED_UTC` | `esriFieldTypeDate` | Operational/history field for this table grain. |
| `PERIOD_CODE` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `PERIOD_LABEL` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `PERIOD_START` | `esriFieldTypeDate` | Operational/history field for this table grain. |
| `PERIOD_END` | `esriFieldTypeDate` | Operational/history field for this table grain. |
| `DIMENSION` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `DIM_VALUE` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `METRIC_CODE` | `esriFieldTypeString` | Stable machine-readable metric identifier. |
| `METRIC_VALUE` | `esriFieldTypeDouble` | Numeric metric observation. |
| `PRIOR_VALUE` | `esriFieldTypeDouble` | Operational/history field for this table grain. |
| `CHANGE_ABS` | `esriFieldTypeDouble` | Operational/history field for this table grain. |
| `CHANGE_PCT` | `esriFieldTypeDouble` | Operational/history field for this table grain. |
| `RUN_ID` | `esriFieldTypeString` | Execution identifier used to connect rows to one capture/run. |

## `Data_Quality_Snapshots`

| Field | ArcGIS type | Purpose |
| --- | --- | --- |
| `OBJECTID` | `esriFieldTypeOID` | ArcGIS-managed row identifier. |
| `OBSERVED_UTC` | `esriFieldTypeDate` | UTC observation timestamp. |
| `SCORE` | `esriFieldTypeDouble` | Operational/history field for this table grain. |
| `LOCATION_COMPLETENESS` | `esriFieldTypeDouble` | Operational/history field for this table grain. |
| `ASSIGNEE_COMPLETENESS` | `esriFieldTypeDouble` | Operational/history field for this table grain. |
| `ASSET_LINK_RATE` | `esriFieldTypeDouble` | Operational/history field for this table grain. |
| `KNOWN_LOCATION_RATE` | `esriFieldTypeDouble` | Operational/history field for this table grain. |
| `DUPLICATE_RATE` | `esriFieldTypeDouble` | Operational/history field for this table grain. |
| `NOTES` | `esriFieldTypeString` | Operational/history field for this table grain. |
| `RUN_ID` | `esriFieldTypeString` | Execution identifier used to connect rows to one capture/run. |
