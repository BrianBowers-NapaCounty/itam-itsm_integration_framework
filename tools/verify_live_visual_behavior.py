from pathlib import Path
import json, time

BASE = "https://capybara-framework.readthedocs.io/en/latest/"
CHECKS = [
    ("style-notes.html", "Style notes / callouts"),
    ("branding.html", "Branding"),
    ("editions/alpha/1-implementation-guide.html", "Implementation guide / wrapped art"),
    ("editions/alpha/1-implementation-guide/1-1-first-steps/1-1-2-budget-procurement.html", "Budget / wrapped art"),
    ("editions/alpha/5-visual-resources/5-3-videos.html", "Animated GIF"),
    ("editions/alpha/5-visual-resources/5-4-graphics.html", "Graphics gallery"),
    ("editions/alpha/5-visual-resources/5-5-icons.html", "Icons and symbols"),
]


def verify(driver, repo_root="."):
    results = []
    js = r'''
      const q=s=>document.querySelector(s);
      const css=[...document.styleSheets].map(x=>x.href||'inline').filter(Boolean);
      const fav=q("link[rel~='icon']")?.href||'';
      const logo=q('.wy-side-nav-search img')?.src||q('img.logo')?.src||'';
      const h1=q('h1'); const hs=h1?getComputedStyle(h1):null;
      const side=q('.wy-side-nav-search'); const ss=side?getComputedStyle(side):null;
      const floats=[...document.querySelectorAll('img,[style*="float"],.float-left,.float-right')].filter(e=>{
         const s=getComputedStyle(e); return s.float==='left'||s.float==='right';
      }).length;
      return {title:document.title,css,favicon:fav,logo,
              h1Color:hs?.color||'',h1Font:hs?.fontFamily||'',
              sidebarBackground:ss?.backgroundColor||'',
              callouts:document.querySelectorAll('.callout').length,
              calloutIcons:document.querySelectorAll('.callout-icon').length,
              floats,
              gifs:[...document.images].filter(x=>/\.gif(?:$|\?)/i.test(x.src)).map(x=>x.src),
              brokenImages:[...document.images].filter(x=>!x.complete||x.naturalWidth===0).map(x=>x.src)};
    '''
    for rel, label in CHECKS:
        driver.get(BASE + rel)
        time.sleep(.8)
        data = driver.execute_script(js)
        data.update({"route": rel, "label": label})
        results.append(data)
        print(label, "broken=", len(data["brokenImages"]), "floats=", data["floats"], "callouts=", data["callouts"])

    errors = []
    for item in results:
        if item["brokenImages"]:
            errors.append(f"{item['route']}: broken images")
        if "favicon.ico" not in item["favicon"]:
            errors.append(f"{item['route']}: original favicon not active")
        if "capybara-logo" not in item["logo"]:
            errors.append(f"{item['route']}: Capybara sidebar logo not active")
        if not any("capybara.css" in x for x in item["css"]):
            errors.append(f"{item['route']}: capybara.css not loaded")

    impl = next(x for x in results if x["route"].endswith("1-implementation-guide.html"))
    budget = next(x for x in results if x["route"].endswith("1-1-2-budget-procurement.html"))
    style = next(x for x in results if x["route"] == "style-notes.html")
    video = next(x for x in results if x["route"].endswith("5-3-videos.html"))
    if impl["floats"] < 1:
        errors.append("implementation guide: no floating/wrapped illustration detected")
    if budget["floats"] < 1:
        errors.append("budget/procurement: no floating/wrapped illustration detected")
    if style["callouts"] < 1 or style["calloutIcons"] < 1:
        errors.append("style notes: Alpha callout examples/classes not rendered")
    if not video["gifs"]:
        errors.append("videos page: animated GIF not rendered")

    output = {"status": "PASS" if not errors else "FAIL", "errors": errors, "pages": results}
    out_path = Path(repo_root) / "legacy_baseline/RC3_LIVE_VISUAL_AUDIT.json"
    out_path.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print("Live visual audit:", output["status"])
    if errors:
        for item in errors:
            print("ERROR:", item)
        raise RuntimeError("Live visual audit failed")
    return output
