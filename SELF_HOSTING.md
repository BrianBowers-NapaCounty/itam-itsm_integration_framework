# Self-hosting the DOCX and self-contained HTML

After `python tools/build_release.py`, copy these two files from `release/` to the web directory that serves:

`http://gis.napa.ca.gov/Data/Brian/CCISDA-CSAC/`

Files:

- `capybara-framework-expanded.html`
- `capybara-framework-expanded.docx`

Keep those exact filenames unless you also update `docs/downloads.md`.

Recommended public URLs:

- `http://gis.napa.ca.gov/Data/Brian/CCISDA-CSAC/capybara-framework-expanded.html`
- `http://gis.napa.ca.gov/Data/Brian/CCISDA-CSAC/capybara-framework-expanded.docx`

You may also host the generated PDF/ePub/HTML.ZIP there, but Read the Docs will publish its own native PDF/ePub/HTML.ZIP after a successful Sphinx build.
