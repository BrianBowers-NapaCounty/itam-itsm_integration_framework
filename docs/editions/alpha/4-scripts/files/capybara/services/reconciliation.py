"""Cross-system comparison and deliberately conservative auto-repair selection."""

from __future__ import annotations
from ..core.models import ReconciliationIssue


def compare_source_to_operational(tickets, operational_rows, *, operational_id_field="ITSM_ID",
                                  operational_status_field="STATUS"):
    op = {}
    duplicates = set()
    for row in operational_rows:
        attrs = row.attributes if hasattr(row, "attributes") else row
        key = str(attrs.get(operational_id_field,""))
        if not key:
            continue
        if key in op:
            duplicates.add(key)
        op[key] = attrs

    issues = []
    source_ids = set()
    for t in tickets:
        source_ids.add(str(t.id))
        if str(t.id) not in op:
            issues.append(ReconciliationIssue(
                "ticket", str(t.id), "Missing from ArcGIS operational layer",
                severity="high" if str(t.priority) in {"1","Critical","High"} else "warning",
                safe_to_repair=True, source_value=t.status, target_value=None
            ))
            continue
        target_status = str(op[str(t.id)].get(operational_status_field,""))
        if target_status and target_status != str(t.status):
            issues.append(ReconciliationIssue(
                "ticket", str(t.id), "Status drift",
                safe_to_repair=True, source_value=t.status, target_value=target_status
            ))

    for dup in sorted(duplicates):
        issues.append(ReconciliationIssue("ticket",dup,"Duplicate operational records",severity="high",safe_to_repair=False))

    for op_id in set(op) - source_ids:
        issues.append(ReconciliationIssue("ticket",op_id,"Present in ArcGIS but absent from current source extract",
                                          severity="warning",safe_to_repair=False))
    return issues


def safe_repairs(issues):
    return [i for i in issues if i.safe_to_repair]
