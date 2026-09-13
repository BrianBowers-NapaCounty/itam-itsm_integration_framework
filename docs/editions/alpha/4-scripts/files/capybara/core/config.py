"""TOML + environment configuration helpers."""

from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import os
import tomllib
from typing import Any


class ConfigError(RuntimeError):
    pass


@dataclass
class Config:
    data: dict[str, Any]
    source: Path | None = None

    def section(self, name: str) -> dict[str, Any]:
        value = self.data.get(name, {})
        return value if isinstance(value, dict) else {}

    def get(self, dotted: str, default=None):
        cur: Any = self.data
        for part in dotted.split("."):
            if not isinstance(cur, dict) or part not in cur:
                return default
            cur = cur[part]
        return cur

    def env_value(self, dotted_env_name: str, *, required=False, default=None):
        env_name = self.get(dotted_env_name)
        if not env_name:
            if required:
                raise ConfigError(f"Missing environment-variable name setting: {dotted_env_name}")
            return default
        value = os.getenv(str(env_name), default)
        if required and not value:
            raise ConfigError(f"Required environment variable is not set: {env_name}")
        return value

    @property
    def dry_run(self) -> bool:
        return bool(self.get("general.dry_run", True))

    @property
    def output_dir(self) -> Path:
        p = Path(str(self.get("general.output_dir", "./output")))
        if self.source and not p.is_absolute():
            p = self.source.parent / p
        p.mkdir(parents=True, exist_ok=True)
        return p


def load_config(path: str | Path = "config.toml") -> Config:
    path = Path(path)
    if not path.exists():
        raise ConfigError(
            f"Configuration file not found: {path}. Copy config.example.toml to config.toml first."
        )
    with path.open("rb") as fh:
        return Config(tomllib.load(fh), source=path.resolve())
