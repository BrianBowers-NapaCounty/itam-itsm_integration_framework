"""Hosted-table definitions used by the historical analytics service.

Field names are intentionally concise and broadly compatible with ArcGIS
Online / Enterprise hosted feature-service tables.
"""

from __future__ import annotations

def f(name, type_, *, alias=None, length=None, nullable=True):
    d={"name":name,"alias":alias or name,"type":type_,"nullable":nullable,"editable":True}
    if length is not None:
        d["length"]=length
    return d

OID = f("OBJECTID","esriFieldTypeOID",nullable=False)

TABLES = {
    "Analytics_Runs": {
        "name":"Analytics_Runs",
        "type":"Table",
        "objectIdField":"OBJECTID",
        "fields":[OID,
            f("RUN_ID","esriFieldTypeString",length=64,nullable=False),
            f("RUN_TYPE","esriFieldTypeString",length=80),
            f("STARTED_UTC","esriFieldTypeDate"),
            f("FINISHED_UTC","esriFieldTypeDate"),
            f("STATUS","esriFieldTypeString",length=24),
            f("ROWS_WRITTEN","esriFieldTypeInteger"),
            f("MESSAGE","esriFieldTypeString",length=1000),
            f("CORRELATION","esriFieldTypeString",length=80),
        ]},
    "Metric_Snapshots": {
        "name":"Metric_Snapshots","type":"Table","objectIdField":"OBJECTID",
        "fields":[OID,
            f("OBSERVED_UTC","esriFieldTypeDate",nullable=False),
            f("PERIOD_CODE","esriFieldTypeString",length=40),
            f("PERIOD_START","esriFieldTypeDate"),
            f("PERIOD_END","esriFieldTypeDate"),
            f("METRIC_CODE","esriFieldTypeString",length=80,nullable=False),
            f("METRIC_LABEL","esriFieldTypeString",length=160),
            f("METRIC_VALUE","esriFieldTypeDouble"),
            f("UNIT","esriFieldTypeString",length=32),
            f("DIMENSION","esriFieldTypeString",length=80),
            f("DIM_VALUE","esriFieldTypeString",length=240),
            f("SOURCE_COUNT","esriFieldTypeInteger"),
            f("RUN_ID","esriFieldTypeString",length=64),
        ]},
    "Ticket_Daily": {
        "name":"Ticket_Daily","type":"Table","objectIdField":"OBJECTID",
        "fields":[OID,
            f("DAY","esriFieldTypeDate",nullable=False),
            f("FACILITY_ID","esriFieldTypeString",length=100),
            f("LEVEL_ID","esriFieldTypeString",length=100),
            f("LOCATION_ID","esriFieldTypeString",length=160),
            f("ASSIGN_GROUP","esriFieldTypeString",length=160),
            f("CATEGORY","esriFieldTypeString",length=160),
            f("OPENED","esriFieldTypeInteger"),
            f("CLOSED","esriFieldTypeInteger"),
            f("ACTIVE","esriFieldTypeInteger"),
            f("ON_HOLD","esriFieldTypeInteger"),
            f("UNASSIGNED","esriFieldTypeInteger"),
            f("SLA_BREACHED","esriFieldTypeInteger"),
            f("AVG_AGE_HOURS","esriFieldTypeDouble"),
            f("RUN_ID","esriFieldTypeString",length=64),
        ]},
    "Asset_Daily": {
        "name":"Asset_Daily","type":"Table","objectIdField":"OBJECTID",
        "fields":[OID,
            f("DAY","esriFieldTypeDate",nullable=False),
            f("FACILITY_ID","esriFieldTypeString",length=100),
            f("LOCATION_ID","esriFieldTypeString",length=160),
            f("DEPARTMENT","esriFieldTypeString",length=160),
            f("ASSET_STATUS","esriFieldTypeString",length=80),
            f("ASSET_COUNT","esriFieldTypeInteger"),
            f("MISSING_COUNT","esriFieldTypeInteger"),
            f("SPARE_COUNT","esriFieldTypeInteger"),
            f("ASSIGNED_COUNT","esriFieldTypeInteger"),
            f("UNASSIGNED_COUNT","esriFieldTypeInteger"),
            f("RUN_ID","esriFieldTypeString",length=64),
        ]},
    "Event_History": {
        "name":"Event_History","type":"Table","objectIdField":"OBJECTID",
        "fields":[OID,
            f("EVENT_UTC","esriFieldTypeDate",nullable=False),
            f("EVENT_TYPE","esriFieldTypeString",length=80),
            f("RECORD_TYPE","esriFieldTypeString",length=40),
            f("RECORD_ID","esriFieldTypeString",length=120),
            f("PUBLIC_ID","esriFieldTypeString",length=120),
            f("FIELD_NAME","esriFieldTypeString",length=120),
            f("OLD_VALUE","esriFieldTypeString",length=500),
            f("NEW_VALUE","esriFieldTypeString",length=500),
            f("LOCATION_ID","esriFieldTypeString",length=160),
            f("ASSET_ID","esriFieldTypeString",length=120),
            f("CORRELATION","esriFieldTypeString",length=80),
            f("RUN_ID","esriFieldTypeString",length=64),
        ]},
    "Sync_Health": {
        "name":"Sync_Health","type":"Table","objectIdField":"OBJECTID",
        "fields":[OID,
            f("OBSERVED_UTC","esriFieldTypeDate",nullable=False),
            f("CONNECTOR_OK","esriFieldTypeSmallInteger"),
            f("ARCGIS_OK","esriFieldTypeSmallInteger"),
            f("SYNC_LAG_MIN","esriFieldTypeDouble"),
            f("UNMATCHED_RATE","esriFieldTypeDouble"),
            f("API_FAILURE_RATE","esriFieldTypeDouble"),
            f("QUEUE_DEPTH","esriFieldTypeInteger"),
            f("DEAD_LETTERS","esriFieldTypeInteger"),
            f("MESSAGE","esriFieldTypeString",length=1000),
            f("RUN_ID","esriFieldTypeString",length=64),
        ]},
    "Reconciliation_History": {
        "name":"Reconciliation_History","type":"Table","objectIdField":"OBJECTID",
        "fields":[OID,
            f("OBSERVED_UTC","esriFieldTypeDate",nullable=False),
            f("RECORD_TYPE","esriFieldTypeString",length=40),
            f("RECORD_ID","esriFieldTypeString",length=120),
            f("ISSUE_CODE","esriFieldTypeString",length=120),
            f("SEVERITY","esriFieldTypeString",length=32),
            f("SAFE_REPAIR","esriFieldTypeSmallInteger"),
            f("SOURCE_VALUE","esriFieldTypeString",length=500),
            f("TARGET_VALUE","esriFieldTypeString",length=500),
            f("RUN_ID","esriFieldTypeString",length=64),
        ]},
    "Period_Summaries": {
        "name":"Period_Summaries","type":"Table","objectIdField":"OBJECTID",
        "fields":[OID,
            f("GENERATED_UTC","esriFieldTypeDate",nullable=False),
            f("PERIOD_CODE","esriFieldTypeString",length=40),
            f("PERIOD_LABEL","esriFieldTypeString",length=100),
            f("PERIOD_START","esriFieldTypeDate"),
            f("PERIOD_END","esriFieldTypeDate"),
            f("DIMENSION","esriFieldTypeString",length=80),
            f("DIM_VALUE","esriFieldTypeString",length=240),
            f("METRIC_CODE","esriFieldTypeString",length=80),
            f("METRIC_VALUE","esriFieldTypeDouble"),
            f("PRIOR_VALUE","esriFieldTypeDouble"),
            f("CHANGE_ABS","esriFieldTypeDouble"),
            f("CHANGE_PCT","esriFieldTypeDouble"),
            f("RUN_ID","esriFieldTypeString",length=64),
        ]},
    "Data_Quality_Snapshots": {
        "name":"Data_Quality_Snapshots","type":"Table","objectIdField":"OBJECTID",
        "fields":[OID,
            f("OBSERVED_UTC","esriFieldTypeDate",nullable=False),
            f("SCORE","esriFieldTypeDouble"),
            f("LOCATION_COMPLETENESS","esriFieldTypeDouble"),
            f("ASSIGNEE_COMPLETENESS","esriFieldTypeDouble"),
            f("ASSET_LINK_RATE","esriFieldTypeDouble"),
            f("KNOWN_LOCATION_RATE","esriFieldTypeDouble"),
            f("DUPLICATE_RATE","esriFieldTypeDouble"),
            f("NOTES","esriFieldTypeString",length=1000),
            f("RUN_ID","esriFieldTypeString",length=64),
        ]},
}

def table_definitions(names=None):
    names = names or list(TABLES)
    return [TABLES[n] for n in names]
