```{image} /_images/symbol-api.png
:alt: 1-3-3-cherwell
:width: 64px
:class: page-symbol
```

<div>

### Integration-Cherwell and Other ITSM Tools

The Capybara pattern generalizes beyond ServiceNow. Cherwell, TeamDynamix, Jira Service Management, BMC Helix, and similar systems can participate if they support API access, event triggers, scheduled exports, or reliable polling. The ServiceNow-specific pattern should therefore be implemented with an adapter boundary, so other ITSM systems can reuse the same Indoors and middleware layers later.

</div>