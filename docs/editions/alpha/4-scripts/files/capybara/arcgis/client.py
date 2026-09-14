"""ArcGIS API for Python connection helpers."""

from __future__ import annotations
import os
from ..core.models import HealthCheck


class ArcGISClient:
    def __init__(self, gis):
        self.gis = gis

    @classmethod
    def from_config(cls, cfg):
        from arcgis.gis import GIS
        a = cfg.section("arcgis")
        profile = str(a.get("profile","")).strip()
        if profile:
            return cls(GIS(profile=profile))
        portal = str(a.get("portal_url","")).strip() or None
        username = os.getenv(str(a.get("username_env","CAPYBARA_ARCGIS_USERNAME"))) or None
        password = os.getenv(str(a.get("password_env","CAPYBARA_ARCGIS_PASSWORD"))) or None
        if portal or username:
            return cls(GIS(portal, username, password))
        return cls(GIS("home"))

    def health_check(self):
        import time
        t0 = time.perf_counter()
        try:
            me = self.gis.users.me
            return HealthCheck("ArcGIS", bool(me), f"Connected as {getattr(me,'username','unknown')}", (time.perf_counter()-t0)*1000)
        except Exception as exc:
            return HealthCheck("ArcGIS", False, f"{type(exc).__name__}: {exc}")

    def feature_layer(self, item_id, layer_index=0):
        item = self.gis.content.get(item_id)
        if not item:
            raise LookupError(f"ArcGIS item not found: {item_id}")
        return item.layers[int(layer_index)]
