# File Naming Conventions

This document outlines the **file naming standards** used in the Capybara repository, optimized for **Read the Docs**, **Sphinx**, and **GitHub**. Following these conventions ensures consistent organization, easy navigation, and proper sorting of files across platforms.

---

## 1. General Principles

1. **Consistency** is key. Always follow the conventions outlined here.
2. **Alphanumeric sorting** should naturally reflect chronological order or version history.
3. **Readability**: File names should be human-readable and descriptive of the content.
4. **Avoid special characters**: Only letters, numbers, hyphens (`-`), and underscores (`_`) are allowed. Do **not** use spaces, periods (except for extensions), or other punctuation.

---

## 2. Primary Content Files & Subfolders

For core documentation files (Markdown, reStructuredText, or similar) and subfolders:

- Use **lowercase letters only**.
- Use **hyphens (`-`)** to separate words.
- Example files and folders:
  - `index.md`
  - `changelog.md`
  - `style-notes.md`
  - `itam-integration.md`
- **Subfolders** should follow the same lowercase-hyphen pattern:
  - `images/`
  - `guides/`
  - `examples/`

**Rationale:**  
This style is compatible with **Sphinx**, **Read the Docs**, and GitHub Pages, and prevents case-sensitive conflicts on different operating systems.

---

## 3. Standard/Repository Metadata Files

Certain files should retain their **official capitalization** to conform with GitHub conventions:

| File | Purpose |
|------|---------|
| `README.md` | Main repository overview |
| `CONTRIBUTING.md` | Contribution guidelines |
| `CODE_OF_CONDUCT.md` | Community standards |
| `LICENSE.md` (or `MITLicense.md`) | Licensing information |

**Note:** These files are case-sensitive on some systems and recognized by GitHub automatically.

---

## 4. Date-Specific or Versioned Files

For memos, press releases, scripts, or other files where chronological order matters:

### 4.1 Filename Structure

BaseFilename_v###_YYYYMMDD_FL.ext

Where:

- **BaseFilename** – PascalCase (UpperCamelCase), describing the content.  
  Example: `MITLicenseAdditionsMemo`
- **v###** – Three-digit version number (always zero-padded).  
  Example: `v003`
- **YYYYMMDD** – ISO date format for proper alphanumeric sorting.  
  Example: `20260716`
- **FL** – Author initials (`Firstname-Lastname`), uppercase.  
  Example: `BB`
- **ext** – File extension (e.g., `.docx`, `.md`, `.pdf`)

### 4.2 Example

MITLicenseAdditionsMemo_v003_20260716_BB.docx

**Notes:**

- Always increment the **version number** (`v001`, `v002`, etc.) for updates.
- The **ISO date** allows chronological sorting when listing files in GitHub or local directories.
- Use **author initials** to track ownership or responsibility.

---

## 5. Optional Best Practices

- **Short, descriptive names**: Avoid overly long filenames; aim for clarity.
- **Avoid redundant dates** in the base filename if the date is already in the `YYYYMMDD` segment.
- **Folder organization**: Keep versioned files in a `versions/` or `releases/` subfolder if needed.
- **No spaces**: Always replace spaces with hyphens (`-`) or underscores (`_`) per the rules above.
- **Consistent extensions**: Stick to lowercase extensions (e.g., `.md`, `.docx`, `.pdf`) for cross-platform compatibility.

---

## 6. Summary Table of Conventions

| File Type | Naming Style | Examples |
|-----------|--------------|---------|
| Primary docs / subfolders | lowercase + hyphens | `index.md`, `style-notes.md`, `guides/` |
| Standard repo files | Uppercase (GitHub conventions) | `README.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` |
| Versioned / dated files | PascalCase + `_v###_YYYYMMDD_FL` | `MITLicenseAdditionsMemo_v003_20260716_BB.docx` |

---

## 7. References

- [Read the Docs: Markdown & reStructuredText best practices](https://docs.readthedocs.io/)
- [Sphinx documentation conventions](https://www.sphinx-doc.org/en/master/)
- [GitHub repository naming conventions](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories)

---

**Following these conventions ensures:**

- Predictable organization and sorting
- Compatibility with Sphinx, Read the Docs, and GitHub
- Clear version and author tracking
- Minimal cross-platform issues
