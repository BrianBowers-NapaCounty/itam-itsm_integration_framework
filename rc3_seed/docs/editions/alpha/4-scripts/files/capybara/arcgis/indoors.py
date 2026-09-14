"""Helpers for matching canonical location IDs to ArcGIS Indoors Units."""

from __future__ import annotations
from ..core.models import LocationRef, MatchStatus


class IndoorsUnitResolver:
    def __init__(self, units_layer, *, unit_id_field="UNIT_ID", name_field="NAME"):
        self.units = units_layer
        self.unit_id_field = unit_id_field
        self.name_field = name_field

    def by_unit_id(self, unit_id):
        safe = str(unit_id).replace("'","''")
        rows = self.units.query(
            where=f"{self.unit_id_field}='{safe}'",
            out_fields=f"{self.unit_id_field},{self.name_field},FACILITY_ID,LEVEL_ID",
            return_geometry=True,
        ).features
        if len(rows) == 1:
            a = rows[0].attributes
            return LocationRef(
                source_id=str(unit_id), name=str(a.get(self.name_field,"")),
                facility_id=str(a.get("FACILITY_ID","")), level_id=str(a.get("LEVEL_ID","")),
                unit_id=str(a.get(self.unit_id_field,"")),
                match_status=MatchStatus.MATCHED, confidence=1.0,
            ), rows[0].geometry
        if len(rows) > 1:
            return LocationRef(source_id=str(unit_id), match_status=MatchStatus.AMBIGUOUS, notes="Duplicate unit IDs"), None
        return LocationRef(source_id=str(unit_id), match_status=MatchStatus.NOT_FOUND), None
