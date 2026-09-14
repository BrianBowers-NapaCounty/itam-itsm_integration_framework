"""Ticket-to-operational-layer synchronization."""

from __future__ import annotations
from ..core.logging_utils import correlation_id


def ticket_attributes(ticket, *, correlation=None):
    return {
        "TICKET_NO": ticket.number,
        "SUMMARY": ticket.short_description,
        "STATUS": ticket.status,
        "PRIORITY": ticket.priority,
        "ASSIGN_GRP": ticket.assignment_group,
        "ASSIGNEE": ticket.assignee,
        "LOCATION_ID": ticket.location_id,
        "ASSET_ID": ticket.asset_id,
        "SRC_UPDATED": ticket.updated_at.isoformat() if ticket.updated_at else None,
        "CORRELATION": correlation or correlation_id("sync"),
    }


def sync_ticket(ticket, operational_layer, *, geometry=None, dry_run=True):
    return operational_layer.upsert_attributes(
        ticket.id, ticket_attributes(ticket), geometry=geometry, dry_run=dry_run
    )
