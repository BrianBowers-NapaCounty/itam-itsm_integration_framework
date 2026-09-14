# Operations Runbook

## Daily / scheduled checks

1. Confirm connector and ArcGIS health.
2. Inspect queue depth, retry counts, and dead letters.
3. Review unmatched-location rate and reconciliation drift.
4. Capture historical analytics snapshots.
5. Review missing-equipment and procurement-hold alerts.

## Credential rotation

Rotate credentials in the approved secret store; never commit tokens or passwords. Validate read access first, then write access, then one dry-run workflow, then one controlled live transaction.

## Schema change response

Pause affected writes, run schema-discovery tools, compare expected fields, update the relevant connector or mapping, execute contract tests, and reconcile affected records before re-enabling automation.

## Emergency disablement

Disable the scheduler/webhook/worker path without deleting queued evidence. Preserve correlation IDs, logs, dead-letter records, and source-system ownership.
