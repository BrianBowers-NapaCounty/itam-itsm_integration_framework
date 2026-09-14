# Extension Developer Guide

## Add a connector

Implement the small `ITSMConnector` contract, normalize vendor records into canonical models, declare connector capabilities, and add the connector to the registry. Do not place report-specific logic inside the adapter.

## Add a metric

Register a function with the analytics metric decorator and return a numeric value with a stable code, label, unit, and source.

## Add an alert

Separate record selection from delivery. New alert policies should be independently testable and should default to console/dry-run output before SMTP or another notification adapter is enabled.

## Add a report

Consume canonical objects rather than vendor JSON. Where possible emit both machine-readable (CSV/JSON/hosted table) and human-readable (HTML/chart) output.

## Add enrichment

Use extension hooks to add local support zones, funding categories, governance classifications, department metadata, or other organization-specific context without modifying core connectors.
