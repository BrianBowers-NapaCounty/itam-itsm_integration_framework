"""CSV/JSON/HTML helpers with no template-engine dependency."""

from __future__ import annotations
from dataclasses import asdict, is_dataclass
from pathlib import Path
import csv, html, json


def to_plain(obj):
    if is_dataclass(obj):
        obj = asdict(obj)
    if isinstance(obj, dict):
        return {k: to_plain(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [to_plain(v) for v in obj]
    if hasattr(obj, "isoformat"):
        try:
            return obj.isoformat()
        except Exception:
            pass
    return obj


def write_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(to_plain(data), indent=2, default=str), encoding="utf-8")
    return path


def write_csv(path, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = [to_plain(r) for r in rows]
    fields = sorted({k for row in rows if isinstance(row, dict) for k in row})
    with path.open("w", newline="", encoding="utf-8-sig") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    return path


def write_html_table(path, title, rows, note=""):
    path = Path(path)
    rows = [to_plain(r) for r in rows]
    fields = sorted({k for row in rows if isinstance(row, dict) for k in row})
    th = "".join(f"<th>{html.escape(str(f))}</th>" for f in fields)
    body = []
    for row in rows:
        body.append("<tr>" + "".join(
            f"<td>{html.escape(str(row.get(f,'')))}</td>" for f in fields
        ) + "</tr>")
    doc = f"""<!doctype html>
<html><head><meta charset="utf-8"><title>{html.escape(title)}</title>
<style>
body{{font-family:Arial,sans-serif;margin:2rem;color:#222}}
table{{border-collapse:collapse;width:100%}} th,td{{border:1px solid #777;padding:.4rem;text-align:left}}
th{{background:#eee;position:sticky;top:0}} .note{{border-left:5px solid #777;padding:.6rem 1rem;background:#f7f7f7}}
</style></head><body><h1>{html.escape(title)}</h1>
<p class="note">{html.escape(note)}</p>
<table><thead><tr>{th}</tr></thead><tbody>{''.join(body)}</tbody></table></body></html>"""
    path.write_text(doc, encoding="utf-8")
    return path
