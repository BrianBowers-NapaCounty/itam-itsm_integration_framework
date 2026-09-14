*This page mirrors the repository's *`/CONTRIBUTING.md`*. All changes should be made at the root.*

# Contributing to Capybara

Thank you for your interest in contributing to Capybara. Community contributions are welcome, encouraged, and essential to the long-term health of this project.

This document explains how to contribute in a way that is consistent with the project's goals, structure, and licensing.

---

## License Context

This repository is licensed under the MIT License, as described in the `LICENSE` file.

By submitting a contribution, you agree that:

- Your contributions are provided freely and openly to the global community.
- Your contributions may be used, modified, merged, published, distributed, sublicensed, and/or sold, consistent with the MIT License.
- You grant the project maintainers and all downstream users the same permissions granted by the MIT License, without additional restrictions.

### Attribution Requirement

While the MIT License permits broad reuse, this project includes the following project-level requirement, which contributors must respect:

- The file `AUTHORS.md` must not be modified.
- The file `AUTHORS.md` must be included in all future forks, redistributions, and derivative works of this repository.

This requirement exists to preserve authorship history and credit. Contributions that attempt to remove, alter, or bypass this requirement will not be accepted.

---

## How to Contribute

You may contribute in many ways, including but not limited to:

- Documentation improvements
- New content, examples, or frameworks
- Bug fixes or corrections
- Structural or organizational improvements
- Clarifications or refinements to existing material

All contributions should be made via pull requests and should follow the conventions described below.

---

## Repository Conventions

To keep the repository organized, maintainable, and navigable, contributors are expected to follow these conventions.

### Folder Structure

- Whenever possible, new content should be added to an appropriate subfolder, whether existing or newly created.
- Adding content directly to the top-level `Capybara` folder is strongly discouraged, except where explicitly required by existing structure or maintainers.
- If a suitable subfolder does not exist, contributors are encouraged to create one.

### README Files

- All new subfolders must include a `README.md` describing their purpose, contents, and intended usage.
- For existing subfolders, contributors should update and maintain the associated `README.md` when changes are made.

Clear, accurate documentation is considered a core part of any contribution.

### Changelog Updates

- The file `CHANGELOG.md` in the top-level `Capybara` folder must always be updated to reflect any additions, removals, or modifications made to the repository.
- Changelog entries should be concise, descriptive, and grouped under the appropriate version heading.

Pull requests that modify content without a corresponding changelog update may be requested to revise before acceptance.

---

## Versioning and Releases

This project follows Semantic Versioning (SemVer):

`MAJOR.MINOR.PATCH`

Each version must be preceded by an Edition Codename, chosen by the contributor or release author.

Examples:

- `Capybara: Purple Edition 3.5.14`
- `Capybara: Verdant Edition 2.1.0`

### Initial Release

The initial public release, planned for September 2026, will be:

- **Capybara: Original Edition 1.0.0**

Subsequent releases should increment version numbers according to SemVer rules and include meaningful changelog entries.

---

## Publishing a New Edition and Version

Capybara editions and versions are published using standard Git and GitHub workflows, following Semantic Versioning (SemVer) and the project's Edition + Version naming convention.

The **Publishing a New Edition** section explains how to publish a new edition using either the command-line Git workflow or the GitHub web interface, using the transition from:

> Capybara: Alpha Edition 0.x.y to Capybara: Original Edition 1.0.0

as a real-world example.

### After Publishing

Once a new edition is published:

- The release tag (`v1.0.0`) becomes the canonical reference point for that edition.
- Documentation hosting platforms (such as Read the Docs) may be configured to expose the version publicly.
- All future development should proceed on `main` toward the next edition or version (for example, `1.1.0` or a future edition).

### Notes on Pre-Releases

Pre-release editions (such as Alpha or Beta editions using `0.x.y` versions):

- May be published without tags.
- Should clearly indicate their pre-release status in documentation.
- Do not imply long-term stability or backward compatibility.

The Original Edition 1.0.0 represents Capybara's first stable, production-ready release and establishes the baseline for all future versions.

By following these steps, contributors help ensure Capybara releases remain consistent, traceable, and easy for the global community to adopt and build upon.

---

## Style Notes and Guidelines

The **Style Notes and Guidelines** section in the project's guide back-matter establishes the baseline stylistic and structural conventions for this repository.

- All contributors are expected to honor the examples and guidelines in that section.
- Deviations from established style patterns are discouraged, but not forbidden.

### Intentional Style Changes

If a contributor makes a carefully considered decision to depart from existing style precedents:

- The new version's **Style Notes and Guidelines** section must be updated to document and justify the new style choices.
- The change should be explained clearly in the changelog.

This ensures that style evolution is intentional, documented, and understandable to future contributors.

---

## Original Edition 1.0.0 Contribution Requirements

Contributions should preserve authoritative-system boundaries, platform-neutral core logic, U.S. English spelling, accessible documentation, and dry-run-first examples.

Open an issue or pull request describing the use case, affected platforms, data ownership, and test approach.

---

## Final Notes

- Contributions should be respectful, constructive, and well-documented.
- Large or structural changes are encouraged to be discussed in an issue before submission.
- Maintainers reserve the right to request revisions to ensure consistency with this guide.

Thank you for helping make Capybara better for everyone.

---
