# Style Notes and Guidelines

This page preserves the Alpha Edition styling conventions and adds the release
requirements for the expanded 1.0.0 documentation.

## Language

Use **U.S. English spelling** throughout the project: `catalog`, `color`,
`analyze`, `organization`, `license`, and similar forms.

## Visual Resource Catalogs

The visual conventions documented here are backed by the preserved Visual
Resources library:

- [Graphics](editions/alpha/5-visual-resources/5-4-graphics)
- [Icons and Symbols](editions/alpha/5-visual-resources/5-5-icons)
- [Videos and Animations](editions/alpha/5-visual-resources/5-3-videos)
- [Branding Guidelines](branding)

The preservation/finalization step restores the exact Alpha source of this page
before publication, including its original callout examples and CSS classes.
This release addendum is then appended so the historical examples remain
visible rather than being replaced.

## Wrapped Illustrations and Callouts

Existing raw-HTML image markup, CSS classes, and inline style attributes from
the Alpha source are protected content. In particular:

- the small Capybara illustrations that float left or right while body text
  wraps around them must remain wrapped;
- `.callout`, `.callout-icon`, and the individual semantic callout classes must
  continue to render;
- icons are supplemental visual cues and may not be the only carrier of
  meaning;
- image alt text remains required.

The original `_static/capybara.css` is preserved as
`_static/legacy-capybara.css` and is loaded **before** the expanded release CSS.

## Expanded Documentation Conventions

New material should be explicit about whether it is a strategy, reference
implementation, adapter skeleton, example, or production control. Prefer stable
identifiers and descriptive link text. New styling may extend the Alpha
conventions but should not silently break or remove them.
