from pathlib import Path
import json,re,shutil,subprocess,zipfile,hashlib,sys
ROOT=Path(__file__).resolve().parents[1]; DOCS=ROOT/'docs'; OUT=ROOT/'release'; BUILD=ROOT/'_build_release'
OUT.mkdir(exist_ok=True); BUILD.mkdir(exist_ok=True)
pages=json.loads((ROOT/'tools/book_manifest.json').read_text())

def clean_myst(text,page):
    # Convert MyST image fences to ordinary Markdown images for Pandoc.
    def img(m):
        block=m.group(0); path=re.search(r'```\{image\}\s+([^\n]+)',block).group(1).strip()
        altm=re.search(r':alt:\s*([^\n]+)',block); alt=altm.group(1).strip() if altm else ''
        if path.startswith('/_images/'): path=str((DOCS/path.lstrip('/')).resolve())
        elif path.startswith('/_static/'): path=str((DOCS/path.lstrip('/')).resolve())
        return f'![{alt}]({path})'
    text=re.sub(r'```\{image\}[^`]+```',img,text,flags=re.S)
    text=re.sub(r'```\{toctree\}.*?```','',text,flags=re.S)
    text=re.sub(r'\{download\}`([^`<]+)\s*<([^>]+)>`',r'\1 (`\2`)',text)
    # Remove Sphinx roles that Pandoc does not know.
    text=re.sub(r':\w+:`([^`]+)`',r'\1',text)
    return text

parts=['---\ntitle: "Capybara Framework"\nauthor: "Team Capybara"\ndate: "September 2026"\nlang: en-US\n---\n']
for rel in pages:
    p=ROOT/rel
    if not p.exists(): continue
    txt=clean_myst(p.read_text(encoding='utf-8'),p)
    # Demote duplicate top-level title after main title so book hierarchy stays sane.
    parts.append('\n\n'+txt+'\n\n')
book=BUILD/'capybara-framework-book.md';book.write_text(''.join(parts),encoding='utf-8')
css=BUILD/'book.css';css.write_text("body{font-family:Arial,sans-serif;max-width:1100px;margin:auto;padding:2rem;color:#222;line-height:1.45}h1,h2,h3{color:#263D68}table{border-collapse:collapse;width:100%}th,td{border:1px solid #777;padding:.35rem;vertical-align:top}th{background:#f0e8df}img{max-width:100%;height:auto}code{white-space:pre-wrap}")
base=['pandoc',str(book),'--standalone','--toc','--metadata','title=Capybara Framework','--resource-path',str(ROOT)]
subprocess.run(base+['-o',str(OUT/'capybara-framework-expanded.docx')],check=True)
subprocess.run(base+['-o',str(OUT/'capybara-framework-expanded.epub')],check=True)
subprocess.run(base+['--embed-resources','--css',str(css),'-o',str(OUT/'capybara-framework-expanded.html')],check=True)
# A printable HTML is useful even when PDF is produced through LibreOffice.
subprocess.run(base+['--css',str(css),'-o',str(OUT/'capybara-framework-print.html')],check=True)
# Convert DOCX to PDF with LibreOffice when available.
lo=shutil.which('libreoffice') or shutil.which('soffice')
if lo:
    subprocess.run([lo,'--headless','--convert-to','pdf','--outdir',str(OUT),str(OUT/'capybara-framework-expanded.docx')],check=True)
# Offline HTML.ZIP: single self-contained HTML + README is robust without Sphinx; RTD will produce the native multi-page HTMLZIP.
readme=BUILD/'HTMLZIP_README.txt';readme.write_text('Open capybara-framework-expanded.html in a browser. Read the Docs also publishes a native multi-page HTML.ZIP after a successful build.\n')
with zipfile.ZipFile(OUT/'capybara-framework-html.zip','w',zipfile.ZIP_DEFLATED) as z:
    z.write(OUT/'capybara-framework-expanded.html','index.html');z.write(readme,'README.txt')
# Checksums
files=[p for p in OUT.iterdir() if p.is_file() and p.name!='SHA256SUMS.txt']
(OUT/'SHA256SUMS.txt').write_text('\n'.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}' for p in sorted(files))+'\n')
print('Built',len(files),'release files in',OUT)
