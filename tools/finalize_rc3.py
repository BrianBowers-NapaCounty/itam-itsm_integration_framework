#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path, PurePosixPath
from urllib.parse import urljoin, unquote
import argparse, base64, json, random, re, shutil, time
import requests

LIVE_BASE = "https://capybara-framework.readthedocs.io/en/latest/"
SOURCE_MANIFEST = Path("legacy_baseline/LEGACY_BASELINE_MANIFEST.json")

MD_TOC = re.compile(r"```\{toctree\}\s*\n(.*?)```", re.S)
RST_TOC = re.compile(r"\.\.\s+toctree::\s*\n((?:[ \t].*\n|\s*\n)*)", re.M)
RST_HEAD = re.compile(r"^(.+?)\n([=\-~^\"`:+*#<>_]{3,})\s*$", re.M)
DOWNLOAD_ROLE = re.compile(r":download:`(?:[^`<>]*?<)?([^`<>]+?)(?:>)?`", re.I)
RST_INCLUDE = re.compile(r"^\s*\.\.\s+(?:include|literalinclude)::\s+(.+?)\s*$", re.I | re.M)
MD_LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+['\"][^'\"]*['\"])?\)")


def nap(lo=.45, hi=1.15):
    time.sleep(random.uniform(lo, hi))


def selenium_fetch(driver, url):
    driver.set_script_timeout(180)
    if "capybara-framework.readthedocs.io" not in (driver.current_url or ""):
        driver.get(LIVE_BASE)
    script = r'''
    const url=arguments[0], done=arguments[arguments.length-1];
    fetch(url,{method:'GET',cache:'no-store',credentials:'omit'})
      .then(async r=>{
        if(!r.ok){done({ok:false,status:r.status,url:r.url});return;}
        const b=new Uint8Array(await r.arrayBuffer()); let s=''; const C=0x8000;
        for(let i=0;i<b.length;i+=C) s+=String.fromCharCode.apply(null,b.subarray(i,i+C));
        done({ok:true,status:r.status,url:r.url,data:btoa(s),ct:r.headers.get('content-type')||''});
      }).catch(e=>done({ok:false,status:0,error:String(e),url:url}));
    '''
    res = driver.execute_async_script(script, url)
    if not res.get("ok"):
        raise RuntimeError(res)
    return base64.b64decode(res["data"])


def fetch(session, url, driver=None, retries=4):
    last = None
    for i in range(retries):
        nap()
        try:
            r = session.get(url, timeout=90, allow_redirects=True)
            if r.status_code == 429:
                time.sleep(random.uniform(12, 30))
                last = RuntimeError("429")
                continue
            r.raise_for_status()
            return r.content
        except Exception as exc:
            last = exc
            if driver is not None:
                try:
                    return selenium_fetch(driver, url)
                except Exception as browser_exc:
                    last = RuntimeError(f"requests={exc!r}; selenium={browser_exc!r}")
            time.sleep(min(12, 3 * (i + 1)))
    raise RuntimeError(f"Unable to fetch {url}: {last}")


def write(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def authored(src):
    return src[:-4] if src.endswith(".txt") else src


def title_and_rest_md(text):
    m = re.search(r"^#\s+.+?\s*$", text, re.M)
    if not m:
        return "", text
    return m.group(0), (text[:m.start()] + text[m.end():]).lstrip("\n")


def title_and_rest_rst(text):
    m = RST_HEAD.search(text)
    if not m:
        return "", text
    return m.group(0), (text[:m.start()] + text[m.end():]).lstrip("\n")


def parse_md_toc(block):
    opts, items = [], []
    for line in block.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith(":"):
            opts.append(line)
        else:
            items.append(s)
    return opts, items


def union_md_toctree(legacy, seed):
    seed_trees = list(MD_TOC.finditer(seed))
    if not seed_trees:
        return legacy
    out = legacy
    for sm in seed_trees:
        sopts, sitems = parse_md_toc(sm.group(1))
        lm = MD_TOC.search(out)
        if not lm:
            out = out.rstrip() + "\n\n" + sm.group(0) + "\n"
            continue
        lopts, litems = parse_md_toc(lm.group(1))
        merged = litems + [x for x in sitems if x not in litems]
        opts = lopts or sopts
        body = "\n".join(opts + ([""] if opts and merged else []) + merged)
        repl = "```{toctree}\n" + body + "\n```"
        out = out[:lm.start()] + repl + out[lm.end():]
    return out


def parse_rst_toc(body):
    opts, items = [], []
    for line in body.splitlines():
        if not line.strip():
            continue
        if line.lstrip().startswith(":"):
            opts.append(line)
        elif line.startswith((" ", "\t")):
            items.append(line.strip())
    return opts, items


def union_rst_toctree(legacy, seed):
    sm = RST_TOC.search(seed)
    if not sm:
        return legacy
    sopts, sitems = parse_rst_toc(sm.group(1))
    lm = RST_TOC.search(legacy)
    if not lm:
        return legacy.rstrip() + "\n\n" + sm.group(0) + "\n"
    lopts, litems = parse_rst_toc(lm.group(1))
    merged = litems + [x for x in sitems if x not in litems]
    opts = lopts or sopts
    body = "\n".join(opts + ([""] if opts and merged else []) + ["   " + x for x in merged]) + "\n"
    return legacy[:lm.start(1)] + body + legacy[lm.end(1):]


def remove_md_toctrees(text):
    return MD_TOC.sub("", text)


def remove_rst_toctrees(text):
    return RST_TOC.sub("", text)


def norm(text):
    return re.sub(r"\s+", " ", text or "").strip().lower()


def seed_body_md(seed):
    _, rest = title_and_rest_md(seed)
    return remove_md_toctrees(rest).strip()


def seed_body_rst(seed):
    _, rest = title_and_rest_rst(seed)
    return remove_rst_toctrees(rest).strip()


def append_extension_md(base, seed_body):
    if not seed_body or norm(seed_body) in norm(base):
        return base
    if not re.search(r"^#{2,6}\s+", seed_body, re.M) and len(seed_body) < 650:
        return base.rstrip() + "\n\n" + seed_body.strip() + "\n"
    return (
        base.rstrip()
        + '\n\n<div class="rc3-extension">\n\n'
        + "## Extended guidance for the Original Edition\n\n"
        + seed_body.strip()
        + "\n\n</div>\n"
    )


def append_extension_rst(base, seed_body):
    if not seed_body or norm(seed_body) in norm(base):
        return base
    if not RST_HEAD.search(seed_body) and len(seed_body) < 650:
        return base.rstrip() + "\n\n" + seed_body.strip() + "\n"
    return (
        base.rstrip()
        + '\n\n.. raw:: html\n\n   <div class="rc3-extension">\n\n'
        + "Extended guidance for the Original Edition\n"
        + "--------------------------------------------\n\n"
        + seed_body.strip()
        + '\n\n.. raw:: html\n\n   </div>\n'
    )


def merge_page(rel, legacy, seed):
    seed_first = {"index.md", "editions/alpha/index.md"}
    exact_live = {
        "branding.rst",
        "media-kit.rst",
        "editions/alpha/5-visual-resources/5-3-videos.rst",
        "editions/alpha/5-visual-resources/5-4-graphics.rst",
        "editions/alpha/5-visual-resources/5-5-icons.rst",
    }
    if rel in exact_live:
        return legacy
    if rel.endswith(".md"):
        if rel in seed_first:
            out = union_md_toctree(seed, legacy)
            phrase = "Welcome to the Capybara Framework Implementation Guide."
            if phrase in legacy and phrase not in out:
                out = out.replace("\n\n", "\n\n" + phrase + "\n\n", 1)
            return out
        out = union_md_toctree(legacy, seed)
        return append_extension_md(out, seed_body_md(seed))
    if rel.endswith(".rst"):
        out = union_rst_toctree(legacy, seed)
        return append_extension_rst(out, seed_body_rst(seed))
    return legacy


def resolve_dep(source_rel, raw):
    raw = unquote(raw.strip().strip("'\""))
    if not raw or raw.startswith(("http://", "https://", "#", "mailto:", "data:")):
        return None
    raw = raw.split("#", 1)[0].split("?", 1)[0]
    p = PurePosixPath(raw.lstrip("/")) if raw.startswith("/") else PurePosixPath(source_rel).parent / PurePosixPath(raw)
    parts = []
    for x in p.parts:
        if x in ("", "."):
            continue
        if x == "..":
            if parts:
                parts.pop()
        else:
            parts.append(x)
    return PurePosixPath(*parts) if parts else None


def add_style_notes_links(path):
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8", errors="replace")
    marker = "## Visual Resource Catalogs for the Original Edition"
    if marker in text:
        return
    add = (
        "\n\n## Visual Resource Catalogs for the Original Edition\n\n"
        "The style system uses the complete visual-resource catalogs as shared project assets:\n\n"
        "- [Graphics](editions/alpha/5-visual-resources/5-4-graphics)\n"
        "- [Icons and Symbols](editions/alpha/5-visual-resources/5-5-icons)\n"
        "- [Videos and Animations](editions/alpha/5-visual-resources/5-3-videos)\n"
        "- [Branding Guidelines](branding)\n\n"
        "Existing callout classes, icon classes, raw HTML, float/wrap classes, and inline style attributes remain supported in the Original Edition.\n"
    )
    path.write_text(text.rstrip() + add, encoding="utf-8")


def finalize(repo_root, driver=None):
    repo = Path(repo_root).resolve()
    docs = repo / "docs"
    seed = repo / "rc3_seed/docs"
    manifest = json.loads((repo / SOURCE_MANIFEST).read_text(encoding="utf-8"))
    session = requests.Session()
    session.headers.update({"User-Agent": "Capybara-RC3-Finalizer/1.0"})
    legacy_src = docs / "_legacy_original_source"
    legacy_dl = docs / "_legacy_downloads"
    legacy_src.mkdir(parents=True, exist_ok=True)
    legacy_dl.mkdir(parents=True, exist_ok=True)
    report = {"sources": 0, "images": 0, "downloads": 0, "static": 0, "merged": 0, "errors": []}
    source_text = {}

    for i, src in enumerate(manifest["sources"], 1):
        try:
            data = fetch(session, urljoin(LIVE_BASE, "_sources/" + src), driver)
            write(legacy_src / src, data)
            source_text[src] = data.decode("utf-8", errors="replace")
            report["sources"] += 1
            print(f"SOURCE {i:02}/{len(manifest['sources'])}: {src}")
        except Exception as exc:
            report["errors"].append({"kind": "source", "name": src, "error": str(exc)})

    for i, name in enumerate(manifest["images"], 1):
        try:
            data = fetch(session, urljoin(LIVE_BASE, "_images/" + name), driver)
            write(docs / "_images" / name, data)
            report["images"] += 1
            print(f"IMAGE {i:03}/{len(manifest['images'])}: {name}")
        except Exception as exc:
            report["errors"].append({"kind": "image", "name": name, "error": str(exc)})

    for name, target in [
        ("capybara.css", "capybara.css"),
        ("capybara-logo.png", "capybara-logo.png"),
        ("edition_alpha.png", "edition_alpha.png"),
        ("favicon.ico", "favicon.ico"),
    ]:
        try:
            data = fetch(session, urljoin(LIVE_BASE, "_static/" + name), driver)
            write(docs / "_static" / target, data)
            report["static"] += 1
            print("STATIC:", name)
        except Exception as exc:
            report["errors"].append({"kind": "static", "name": name, "error": str(exc)})

    byname = {}
    for i, item in enumerate(manifest["downloads"], 1):
        try:
            data = fetch(session, urljoin(LIVE_BASE, item["url_path"]), driver)
            dest = legacy_dl / item["hash"] / item["filename"]
            write(dest, data)
            report["downloads"] += 1
            byname.setdefault(Path(item["filename"]).name, dest)
            print(f"DOWNLOAD {i:03}/{len(manifest['downloads'])}: {item['filename']}")
        except Exception as exc:
            report["errors"].append({"kind": "download", "name": item["filename"], "error": str(exc)})

    legacy_names = {authored(x) for x in manifest["sources"]}
    for src, legacy in source_text.items():
        rel = authored(src)
        target = docs / rel
        seed_target = seed / rel
        if not seed_target.exists():
            alt = seed_target.with_suffix(".rst" if seed_target.suffix == ".md" else ".md")
            if alt.exists():
                seed_target = alt
        seed_text = seed_target.read_text(encoding="utf-8", errors="replace") if seed_target.exists() else ""
        other = target.with_suffix(".rst" if target.suffix == ".md" else ".md")
        if other.exists() and other != target:
            other.unlink()
        merged = merge_page(rel, legacy, seed_text)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(merged, encoding="utf-8")
        report["merged"] += 1

    for p in seed.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(seed)
        if rel.parts and rel.parts[0] in ("_static", "_images"):
            continue
        target = docs / rel
        if rel.as_posix() not in legacy_names and not target.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, target)

    for src, text in source_text.items():
        sr = authored(src)
        refs = list(DOWNLOAD_ROLE.findall(text)) + list(RST_INCLUDE.findall(text))
        refs += [x for x in MD_LINK.findall(text) if not x.startswith(("http://", "https://", "#"))]
        for raw in refs:
            dep = resolve_dep(sr, raw)
            if not dep:
                continue
            srcfile = byname.get(Path(str(dep)).name)
            if srcfile and srcfile.exists():
                dest = docs / Path(*dep.parts)
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(srcfile, dest)

    add_style_notes_links(docs / "style-notes.md")
    if (docs / "contributing.md").exists():
        shutil.copy2(docs / "contributing.md", repo / "CONTRIBUTING.md")

    (repo / "legacy_baseline/LAST_RC3_FINALIZE_REPORT.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    if report["errors"]:
        print(f"\nFINALIZE COMPLETED WITH {len(report['errors'])} ERROR(S)")
    else:
        print("\nRC3 finalization completed with zero fetch errors.")
    return report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    args = ap.parse_args()
    result = finalize(args.repo, None)
    raise SystemExit(2 if result["errors"] else 0)


if __name__ == "__main__":
    main()
