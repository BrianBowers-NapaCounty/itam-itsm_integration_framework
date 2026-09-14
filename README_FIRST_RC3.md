# Deploy RC3

Run `Capybara_RC3_Integrated_Deployment.ipynb` from the repository root. It recovers the still-live Alpha source/assets **before** the Git push, integrates expanded Original Edition guidance into the same routes, requires a completeness-audit PASS, pushes `main` to `BrianBowers-NapaCounty/itam-itsm_integration_framework`, rebuilds the existing `capybara-framework` Read the Docs project, then runs the Selenium live visual-behavior audit.
