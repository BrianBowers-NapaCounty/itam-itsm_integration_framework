"""Abstract ITSM connector contract.

Business workflows should depend on this interface rather than on vendor JSON.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Iterable, Mapping, Any
from .models import Ticket, Asset, HealthCheck, OperationResult


class ITSMConnector(ABC):
    platform_name = "Generic"
    capabilities: frozenset[str] = frozenset()

    def supports(self, capability: str) -> bool:
        return capability in self.capabilities

    @abstractmethod
    def health_check(self) -> HealthCheck:
        raise NotImplementedError

    @abstractmethod
    def get_ticket(self, record_id: str) -> Ticket:
        raise NotImplementedError

    @abstractmethod
    def iter_tickets(
        self,
        *,
        updated_since: datetime | None = None,
        limit: int | None = None,
        raw_filter: Any = None,
    ) -> Iterable[Ticket]:
        raise NotImplementedError

    @abstractmethod
    def get_asset(self, record_id: str) -> Asset:
        raise NotImplementedError

    @abstractmethod
    def iter_assets(
        self,
        *,
        updated_since: datetime | None = None,
        limit: int | None = None,
        raw_filter: Any = None,
    ) -> Iterable[Asset]:
        raise NotImplementedError

    def update_ticket(self, record_id: str, fields: Mapping[str, Any]) -> OperationResult:
        raise NotImplementedError(f"{self.platform_name} connector does not implement update_ticket")

    def add_work_note(self, record_id: str, note: str) -> OperationResult:
        raise NotImplementedError(f"{self.platform_name} connector does not implement add_work_note")
