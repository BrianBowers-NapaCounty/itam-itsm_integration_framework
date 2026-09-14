"""Hosted ArcGIS table store and local SQLite demonstration store."""

from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import json, sqlite3, uuid

from .schemas import TABLES, table_definitions


def arcgis_value(value):
    """Convert Python values to ArcGIS edit-friendly attribute values."""
    if isinstance(value, datetime):
        if value.tzinfo is None:
            value=value.replace(tzinfo=timezone.utc)
        return int(value.timestamp()*1000)
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, (dict,list,tuple,set)):
        return json.dumps(value,default=str)
    return value


class HostedAnalyticsStore:
    """Write analytics rows to nonspatial tables in an ArcGIS hosted feature service."""

    def __init__(self, gis, item_id, *, chunk_size=200):
        from arcgis.features import FeatureLayerCollection
        self.gis=gis
        self.item=gis.content.get(item_id)
        if not self.item:
            raise LookupError(f"Analytics feature-service item not found: {item_id}")
        self.flc=FeatureLayerCollection.fromitem(self.item)
        self.chunk_size=min(int(chunk_size),200)
        self.refresh()

    def refresh(self):
        self.flc.refresh()
        self.tables={str(t.properties.name):t for t in self.flc.tables}
        return self

    def ensure_tables(self, names=None):
        names=names or list(TABLES)
        missing=[n for n in names if n not in self.tables]
        if not missing:
            return {"success":True,"added":[]}
        payload={"tables":table_definitions(missing)}
        result=self.flc.manager.add_to_definition(payload)
        if hasattr(result,"result"):
            result=result.result()
        self.refresh()
        return {"success":bool(result.get("success",True)) if isinstance(result,dict) else True,
                "added":missing,"result":result}

    def table(self, name):
        if name not in self.tables:
            raise KeyError(f"Hosted analytics table is missing: {name}")
        return self.tables[name]

    def add_rows(self, table_name, rows):
        rows=list(rows)
        if not rows:
            return {"table":table_name,"submitted":0,"results":[]}
        table=self.table(table_name)
        results=[]
        submitted=0
        for i in range(0,len(rows),self.chunk_size):
            batch=rows[i:i+self.chunk_size]
            payload=[{"attributes":{k:arcgis_value(v) for k,v in r.items() if v is not None}} for r in batch]
            response=table.edit_features(adds=payload, rollback_on_failure=True)
            results.append(response)
            submitted+=len(batch)
        return {"table":table_name,"submitted":submitted,"results":results}

    def query(self, table_name, where="1=1", out_fields="*", order_by_fields=None):
        kwargs={"where":where,"out_fields":out_fields,"return_geometry":False}
        if order_by_fields:
            kwargs["order_by_fields"]=order_by_fields
        return self.table(table_name).query(**kwargs)

    def delete_where(self, table_name, where):
        # Destructive maintenance operation; caller must supply an explicit where clause.
        if not where or where.strip()=="1=1":
            raise ValueError("Refusing unbounded delete.")
        return self.table(table_name).delete_features(where=where)


class SQLiteAnalyticsStore:
    """Small local substitute for demos/tests when AGOL/Portal is not configured."""

    def __init__(self,path):
        self.path=Path(path)
        self.path.parent.mkdir(parents=True,exist_ok=True)
        self.db=sqlite3.connect(self.path)
        self.db.row_factory=sqlite3.Row
        self.ensure_tables()

    def ensure_tables(self,names=None):
        names=names or list(TABLES)
        for name in names:
            fields=[f for f in TABLES[name]["fields"] if f["name"]!="OBJECTID"]
            cols=["OBJECTID INTEGER PRIMARY KEY AUTOINCREMENT"]
            for f in fields:
                t=f["type"]
                sql="REAL" if t in {"esriFieldTypeDouble","esriFieldTypeSingle"} else \
                    "INTEGER" if t in {"esriFieldTypeInteger","esriFieldTypeSmallInteger","esriFieldTypeDate"} else "TEXT"
                cols.append(f'"{f["name"]}" {sql}')
            self.db.execute(f'CREATE TABLE IF NOT EXISTS "{name}" ({", ".join(cols)})')
        self.db.commit()
        return {"success":True}

    def add_rows(self,table_name,rows):
        rows=list(rows)
        if not rows:return {"table":table_name,"submitted":0}
        keys=sorted({k for r in rows for k in r})
        cols=",".join(f'"{k}"' for k in keys)
        marks=",".join("?" for _ in keys)
        vals=[]
        for r in rows:
            row=[]
            for k in keys:
                v=arcgis_value(r.get(k))
                row.append(v)
            vals.append(row)
        self.db.executemany(f'INSERT INTO "{table_name}" ({cols}) VALUES ({marks})',vals)
        self.db.commit()
        return {"table":table_name,"submitted":len(rows)}

    def query_rows(self,table_name,where="1=1",params=()):
        return [dict(r) for r in self.db.execute(f'SELECT * FROM "{table_name}" WHERE {where}',params)]

    def close(self):
        self.db.close()


def build_store(cfg, gis=None):
    item_id=str(cfg.get("analytics.item_id","")).strip()
    if item_id:
        if gis is None:
            from ..arcgis.client import ArcGISClient
            gis=ArcGISClient.from_config(cfg).gis
        return HostedAnalyticsStore(gis,item_id,chunk_size=cfg.get("analytics.chunk_size",200))
    path=cfg.get("analytics.local_sqlite_path","./output/capybara_analytics.sqlite")
    p=Path(path)
    if cfg.source and not p.is_absolute():
        p=cfg.source.parent/p
    return SQLiteAnalyticsStore(p)
