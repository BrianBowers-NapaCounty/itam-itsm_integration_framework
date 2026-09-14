"""Consistent logging and correlation IDs for examples."""

from __future__ import annotations
import logging
import uuid


def correlation_id(prefix="capy"):
    return f"{prefix}-{uuid.uuid4().hex[:12]}"


def configure_logging(level="INFO"):
    logging.basicConfig(
        level=getattr(logging, str(level).upper(), logging.INFO),
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    return logging.getLogger("capybara")
