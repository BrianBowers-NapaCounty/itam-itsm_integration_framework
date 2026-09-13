"""Connector factory. Imports vendor adapters only when selected."""

from __future__ import annotations
from pathlib import Path
from ..core.config import Config


def build_connector(cfg: Config):
    name = str(cfg.get("general.connector","mock")).strip().lower()

    if name == "mock":
        from .mock import MockConnector
        sample = Path(str(cfg.get("general.sample_data","./sample_data")))
        if cfg.source and not sample.is_absolute():
            sample = cfg.source.parent / sample
        return MockConnector(sample)

    if name in {"servicenow","snow"}:
        from .servicenow import ServiceNowConnector
        s = cfg.section("servicenow")
        return ServiceNowConnector(
            base_url=s["base_url"],
            incident_table=s.get("incident_table","incident"),
            asset_table=s.get("asset_table","alm_hardware"),
            bearer_token=cfg.env_value("servicenow.token_env"),
            username=cfg.env_value("servicenow.username_env"),
            password=cfg.env_value("servicenow.password_env"),
            page_size=s.get("page_size",500),
        )

    if name in {"teamdynamix","tdx"}:
        from .teamdynamix import TeamDynamixConnector
        s = cfg.section("teamdynamix")
        return TeamDynamixConnector(
            base_url=s["base_url"], app_id=s["app_id"],
            token=cfg.env_value("teamdynamix.token_env", required=True),
        )

    if name == "cherwell":
        from .cherwell import CherwellConnector
        s = cfg.section("cherwell")
        return CherwellConnector(
            base_url=s["base_url"],
            client_id=cfg.env_value("cherwell.client_id_env", required=True),
            username=cfg.env_value("cherwell.username_env", required=True),
            password=cfg.env_value("cherwell.password_env", required=True),
            auth_mode=s.get("auth_mode","Internal"),
            incident_saved_search=s.get("incident_saved_search",""),
        )

    raise ValueError(f"Unknown connector: {name}")
