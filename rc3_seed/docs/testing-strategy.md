# Testing Strategy

Capybara testing is layered: mock/unit tests -> connector contract tests -> ArcGIS schema/read tests -> dry-run integration -> controlled write tests -> reconciliation -> operational acceptance.

## Before enabling writes

- [ ] Mock tests pass.
- [ ] Connector health and representative reads pass.
- [ ] ArcGIS target schema matches expected fields.
- [ ] Location crosswalk exceptions have been reviewed.
- [ ] Dry-run output is correct.
- [ ] Least-privilege write account is approved.
- [ ] Rollback/emergency-disable procedure is tested.
- [ ] Reconciliation detects intentionally introduced drift.
- [ ] Alert routing is approved.
