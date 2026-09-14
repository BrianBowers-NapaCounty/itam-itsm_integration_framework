#!/usr/bin/env python3
from pathlib import Path, PurePosixPath
import argparse, csv, json, re

MD_HEAD = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.M)
RST_HEAD = re.compile(r"^(.+?)\n([=\-~^\"`:+*#<>_]{3,})\s*$", re.M)
CLASS_REF = re.compile(r"class\s*=\s*[\"']([^\"']+)[\"']", re.I)
STYLE_REF = re.compile(r"style\s*=\s*[\"']([^\"']+)[\"']", re.I)
ASSET_REF = re.compile(r"(?:/_images/|_images/|\.\./_images/)([^\s\)\]\"'<>]+)", re.I)


def authored(x):
    return x[:-4] if x.endswith(".txt") else x


def norm(s):
    return re.sub(r"\s+", " ", s or "").strip().lower()


def headings(text):
    out = [m.group(2).strip() for m in MD_HEAD.finditer(text)]
    out += [m.group(1).strip() for m in RST_HEAD.finditer(text)]
    return out


def significant_blocks(text):
    text = re.sub(r"```\{toctree\}.*?```", "", text, flags=re.S)
    text = re.sub(r"\.\.\s+toctree::.*?(?=\n\S|\Z)", "", text, flags=re.S)
    blocks = []
    for block in re.split(r"\n\s*\n+", text):
        block = block.strip()
        if len(norm(block)) >= 90 and not re.fullmatch(r"[#=\-~`*\s]+", block):
            blocks.append(block)
    return blocks


def route_for(rel):
    p = PurePosixPath(rel)
    if p.name.lower() in ("index.md", "index.rst"):
        return str(p.parent / "index.html")
    return str(p.with_suffix(".html"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    docs = repo / "docs"
    manifest = json.loads((repo / "legacy_baseline/LEGACY_BASELINE_MANIFEST.json").read_text(encoding="utf-8"))
    archive = docs / "_legacy_original_source"
    errors, warnings, rows = [], [], []
    legacy_names = {authored(x) for x in manifest["sources"]}

    for src in manifest["sources"]:
        rel = authored(src)
        lp = archive / src
        target = docs / rel
        if not lp.exists():
            errors.append(f"missing archived legacy source: {src}")
            continue
        if not target.exists():
            alt = target.with_suffix(".rst" if target.suffix == ".md" else ".md")
            if alt.exists():
                target = alt
            else:
                errors.append(f"missing outgoing source: {rel}")
                continue
        legacy = lp.read_text(encoding="utf-8", errors="replace")
        outgoing = target.read_text(encoding="utf-8", errors="replace")
        missing_h = [h for h in headings(legacy) if norm(h) not in norm(outgoing)]
        missing_b = [b for b in significant_blocks(legacy) if norm(b) not in norm(outgoing)]
        legacy_assets = sorted(set(ASSET_REF.findall(legacy)))
        missing_assets = [a for a in legacy_assets if a not in outgoing]
        classes = sorted(set(sum((x.split() for x in CLASS_REF.findall(legacy)), [])))
        missing_classes = [c for c in classes if c not in outgoing]
        styles = sorted(set(STYLE_REF.findall(legacy)))
        missing_styles = [s for s in styles if s not in outgoing]

        disposition = "preserved+extended"
        if rel in (
            "branding.rst", "media-kit.rst",
            "editions/alpha/5-visual-resources/5-3-videos.rst",
            "editions/alpha/5-visual-resources/5-4-graphics.rst",
            "editions/alpha/5-visual-resources/5-5-icons.rst",
        ):
            disposition = "preserved-exact-live-source"
        if rel in ("index.md", "editions/alpha/index.md"):
            disposition = "stable-route+richer-landing"

        if missing_h and rel not in ("index.md", "editions/alpha/index.md"):
            errors.append(f"{rel}: missing legacy headings: {missing_h}")
        if missing_b and rel not in ("index.md", "editions/alpha/index.md"):
            errors.append(f"{rel}: {len(missing_b)} substantive legacy block(s) missing")
        if missing_assets:
            errors.append(f"{rel}: missing media refs: {missing_assets}")
        if missing_classes:
            errors.append(f"{rel}: missing HTML/CSS classes: {missing_classes}")
        if missing_styles:
            errors.append(f"{rel}: missing inline styles: {missing_styles}")

        rows.append({
            "legacy_source": src,
            "outgoing_source": target.relative_to(docs).as_posix(),
            "legacy_route": route_for(rel),
            "disposition": disposition,
            "headings_missing": len(missing_h) if rel not in ("index.md", "editions/alpha/index.md") else 0,
            "substantive_blocks_missing": len(missing_b) if rel not in ("index.md", "editions/alpha/index.md") else 0,
            "media_refs_missing": len(missing_assets),
            "classes_missing": len(missing_classes),
            "styles_missing": len(missing_styles),
        })

    for name in manifest["images"]:
        if not (docs / "_images" / name).exists():
            errors.append(f"missing legacy image: {name}")
    for item in manifest["downloads"]:
        if not (docs / "_legacy_downloads" / item["hash"] / item["filename"]).exists():
            errors.append(f"missing legacy download archive: {item['filename']}")

    for group, names in manifest["protected_sets"].items():
        if not isinstance(names, list) or group == "critical_pages":
            continue
        for name in names:
            if name.lower().endswith((".png", ".gif", ".jpg", ".jpeg", ".svg")) and not (docs / "_images" / name).exists():
                errors.append(f"protected {group} asset missing: {name}")

    gif = docs / "_images/capybara-coffee-animation-transparent.gif"
    if not gif.exists() or gif.read_bytes()[:6] not in (b"GIF87a", b"GIF89a"):
        errors.append("animated GIF missing/invalid")

    for name in ("capybara.css", "capybara-logo.png", "edition_alpha.png", "favicon.ico"):
        if not (docs / "_static" / name).exists():
            errors.append(f"primary Alpha presentation asset missing: _static/{name}")

    conf = (docs / "conf.py").read_text(encoding="utf-8")
    if 'html_css_files = ["capybara.css", "rc3-additions.css"]' not in conf:
        errors.append("Alpha CSS is not the primary stylesheet")
    if 'html_favicon = "_static/favicon.ico"' not in conf:
        errors.append("original favicon not configured")
    if 'html_logo = "_static/capybara-logo.png"' not in conf:
        errors.append("original sidebar logo not configured")

    # Preserve but explicitly surface known license-language divergence.
    contrib = docs / "contributing.md"
    license_file = repo / "LICENSE.md"
    if contrib.exists() and license_file.exists():
        ctext = contrib.read_text(encoding="utf-8", errors="replace")
        ltext = license_file.read_text(encoding="utf-8", errors="replace")
        if "MIT License" in ctext and ("PDDL" in ltext or "Public Domain Dedication" in ltext):
            warnings.append("Recovered contributing page says MIT License while repository LICENSE.md says PDDL 1.0; preserved for deliberate reconciliation.")

    style = docs / "style-notes.md"
    if not style.exists():
        errors.append("style-notes.md missing")
    else:
        st = style.read_text(encoding="utf-8", errors="replace")
        for needle in ("5-4-graphics", "5-5-icons", "callout-icon", "callout"):
            if needle not in st:
                errors.append(f"style notes missing required reference: {needle}")

    for rel in (
        "branding.rst", "contributing.md",
        "editions/alpha/5-visual-resources/5-3-videos.rst",
        "editions/alpha/5-visual-resources/5-4-graphics.rst",
        "editions/alpha/5-visual-resources/5-5-icons.rst",
    ):
        if not (docs / rel).exists():
            errors.append(f"critical page missing: {rel}")

    seed = repo / "rc3_seed/docs"
    for p in seed.rglob("*"):
        if not p.is_file() or p.suffix not in (".md", ".rst"):
            continue
        rel = p.relative_to(seed).as_posix()
        if rel not in legacy_names and not (docs / rel).exists():
            errors.append(f"new RC3 page missing: {rel}")

    coverage = repo / "legacy_baseline/RC3_COVERAGE_MATRIX.csv"
    with coverage.open("w", newline="", encoding="utf-8") as f:
        fields = list(rows[0].keys()) if rows else ["legacy_source"]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    report = {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "warnings": warnings,
        "legacy_pages_checked": len(rows),
        "legacy_images_expected": len(manifest["images"]),
        "legacy_downloads_expected": len(manifest["downloads"]),
    }
    (repo / "legacy_baseline/RC3_COMPLETENESS_AUDIT.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"RC3 completeness audit: {report['status']} — {len(errors)} error(s), {len(warnings)} warning(s)")
    for item in errors[:100]:
        print("ERROR:", item)
    return 0 if not errors else 2


if __name__ == "__main__":
    raise SystemExit(main())
