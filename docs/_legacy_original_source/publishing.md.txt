# Publishing a New Edition

This guide explains how to publish a new Capybara edition/version, including all required metadata and step-by-step instructions for both the **git command line** and the **GitHub web interface**.

---

## 1. Edition Metadata (`VERSION` file)

Each edition folder contains a `VERSION` file with the following variables:

```
# docs/editions/XXX/VERSION

author_supplemental=Brian Bowers; Jon C. Jones; Catalina Llanos; Chris Gomez; Dave Torres; Dan Reid
copyright_supplemental=© 2026 Capybara Project Authors; Additional Contributors
edition_name=Original Edition
edition_version=1.0.0
edition_tagline=The First Stable Release
edition_description=Original edition of the Capybara Framework Implementation Guide.
````

**Notes:**

* `author_supplemental` – Contributors after the original authors
* `copyright_supplemental` – Additional copyright statements
* `edition_name` – Name of the edition
* `edition_version` – Version number (Semantic Versioning)
* `edition_tagline` – Short tagline describing the edition
* `edition_description` – Full description of this edition

---

## 2. Publishing via Git Command Line

Assuming your current branch is `main` and you are on **Alpha Edition 0.x.y**:

### Step 1: Create the new edition folder

```
mkdir -p docs/editions/original
```

### Step 2: Add content

* Copy relevant Markdown, images, templates, and other assets into the folder
* Add/update the `VERSION` file with the new edition metadata

### Step 3: Update `docs/index.md`

* Update the toctree to point to the new edition folder:

````
```{toctree}
:maxdepth: 2
:caption: Original Edition (1.0.0)
:titlesonly:

editions/original/index
````

````

### Step 4: Commit changes
```
git add docs/editions/original docs/index.md
git commit -m "Publish Capybara: Original Edition 1.0.0"
````

### Step 5: Create a Git tag

```
git tag -a v1.0.0 -m "Capybara: Original Edition 1.0.0"
```

### Step 6: Push to GitHub

```
git push origin main --tags
```

---

## 3. Publishing via GitHub Web Interface

### Step 1: Create a new edition folder

1. Go to your repository on GitHub
2. Navigate to `/docs/editions/`
3. Click **Add file → Create new folder**
4. Name it `original` (or your new edition slug)

### Step 2: Add content and `VERSION` file

1. Inside the new folder, click **Add file → Create new file**
2. Name it `VERSION` and paste the edition metadata (see section 1)
3. Repeat for `index.md` and any other edition-specific content

### Step 3: Update `index.md` to point to the new edition

1. Navigate to `/docs/index.md`
2. Click **Edit** and update the toctree to reference:

```
editions/original/index
```

### Step 4: Commit changes

* Add a commit message like:
  `"Publish Capybara: Original Edition 1.0.0"`

### Step 5: Create a GitHub Release (optional)

1. Go to the **Releases** tab of your repository
2. Click **Draft a new release**
3. Tag version `v1.0.0` and title it `"Capybara: Original Edition 1.0.0"`
4. Optionally add release notes
5. Click **Publish release**

---

## 4. Post-publishing Checklist

* ✅ Update `conf.py` if any default edition metadata needs to change
* ✅ Verify `docs/index.md` points to the correct edition
* ✅ Ensure the new edition is building correctly on **Read the Docs**
* ✅ Confirm `capybara_edition.html` displays the correct edition name, version, and tagline in the sidebar
* ✅ Verify Supplemental Matter is included in the sidebar (style notes, branding, file naming, code of conduct, contributing, changelog)
* ✅ Tag the release in Git (`git tag`) for semantic versioning

---

## 5. Notes for Future Editions

* Use Semantic Versioning (`MAJOR.MINOR.PATCH`)
* Always update the `VERSION` file in the edition folder
* Ensure that `index.md` references the correct edition folder
* Supplemental Matter remains the same across editions
* Contributors should update `authors_supplemental` and `copyright_supplemental` when appropriate
