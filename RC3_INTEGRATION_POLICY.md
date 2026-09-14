# RC3 Integration Policy — Complete Content, Alpha Look

RC3 is the publication candidate for **Capybara: Original Edition 1.0.0**.

The live Alpha documentation is the editorial and visual baseline. RC3 extends that baseline in place. No existing section, subsection, page, raw HTML class, inline wrapping style, visual resource, animation, branding asset, downloadable artifact, or public route may disappear silently.

The exact surviving `_sources` are archived, all 170 legacy `_images` are restored, all 178 exposed download artifacts are archived/remapped, and the live Alpha `capybara.css`, logo, edition image, and favicon are restored as the primary presentation assets. Expanded prose is merged into corresponding pages; new subjects are added as neighboring sections in the same navigation.

`tools/audit_rc3.py` writes a page-by-page coverage matrix and fails publication when legacy headings, substantive content blocks, media references, classes, inline styles, assets, downloads, or required routes are missing. `tools/verify_live_visual_behavior.py` verifies the published favicon, logo, Alpha CSS, callouts, wrapped illustrations, animation, and broken-image state through Selenium.
