"""Operational-layer read/write adapter."""

from __future__ import annotations
from ..core.models import OperationResult


class OperationalLayer:
    def __init__(self, feature_layer, *, id_field="ITSM_ID"):
        self.layer = feature_layer
        self.id_field = id_field

    def query_by_source_id(self, source_id, *, return_geometry=True):
        safe = str(source_id).replace("'", "''")
        fs = self.layer.query(
            where=f"{self.id_field}='{safe}'",
            out_fields="*",
            return_geometry=return_geometry,
        )
        return fs.features

    def all(self, *, where="1=1", return_geometry=False):
        return self.layer.query(where=where, out_fields="*", return_geometry=return_geometry).features

    def upsert_attributes(self, source_id, attrs, *, geometry=None, dry_run=True):
        existing = self.query_by_source_id(source_id, return_geometry=False)
        payload = {"attributes":{self.id_field:source_id, **dict(attrs)}}
        if geometry is not None:
            payload["geometry"] = geometry

        if dry_run:
            return OperationResult("arcgis_upsert", True, "Dry-run: edit not submitted", details={"payload":payload})

        if existing:
            oid_field = self.layer.properties.objectIdField
            payload["attributes"][oid_field] = existing[0].attributes[oid_field]
            result = self.layer.edit_features(updates=[payload])
            return OperationResult("arcgis_update", True, "Feature updated", records_written=1, details=result)

        result = self.layer.edit_features(adds=[payload])
        return OperationResult("arcgis_add", True, "Feature added", records_written=1, details=result)
