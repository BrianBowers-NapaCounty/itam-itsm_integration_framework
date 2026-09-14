# Release Checklist

- [ ] Repository provenance reviewed.
- [ ] Placeholder OWNER values replaced.
- [ ] No credentials/secrets/private connection strings present.
- [ ] Python compile and unit tests pass.
- [ ] Sphinx HTML build passes locally or in CI.
- [ ] Linkcheck reviewed.
- [ ] Every local image/download reference resolves.
- [ ] No `_downloads/<hash>` path is authored in source.
- [ ] `.readthedocs.yaml` validates and includes offline formats.
- [ ] `latest` points to intended branch/version.
- [ ] RTD repository connection verified.
- [ ] RTD build succeeds before default/live rebuild.
- [ ] PDF/ePub/HTML.ZIP visible in RTD downloads.
- [ ] Self-contained HTML and DOCX copied to maintainer web server if desired.
- [ ] Changelog/version updated.


## Legacy preservation gate

- [ ] `tools/preserve_live_site.py` completed with zero fetch errors.
- [ ] `tools/audit_legacy_preservation.py --strict` returns PASS.
- [ ] 170 legacy `_images` assets are present.
- [ ] Graphics, Icons and Symbols, Branding, and Videos/Animations are complete.
- [ ] `capybara-coffee-animation-transparent.gif` is present and valid.
- [ ] `legacy-capybara.css` is loaded before expanded CSS.
- [ ] Wrapped/floating illustration behavior was visually checked.
- [ ] All legacy public docnames still resolve.
- [ ] Original `_static/favicon.ico` is restored and `html_favicon` references it.

## RC3 integrated-edition gate

- [ ] `finalize_rc3.py` reports zero recovery errors before Git push.
- [ ] `audit_rc3.py --strict` returns PASS.
- [ ] Coverage matrix accounts for every legacy source page.
- [ ] Exact Alpha `capybara.css`, favicon, logo, and edition image are active.
- [ ] All 170 legacy images and 178 legacy downloads are present.
- [ ] Graphics, icons/symbols, branding, animated GIF, wrapped illustrations, and callouts are intact.
- [ ] Post-build Selenium live visual audit returns PASS.
