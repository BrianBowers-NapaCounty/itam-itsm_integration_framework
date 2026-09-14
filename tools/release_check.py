from pathlib import Path
import argparse,re,sys,ast,json
ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/'docs'
errors=[];warnings=[]
# Image/download references
for p in DOCS.rglob('*'):
    if not p.is_file() or p.suffix.lower() not in {'.md','.rst'}: continue
    text=p.read_text(encoding='utf-8',errors='ignore')
    if re.search(r'_downloads/[0-9a-f]{16,}/',text):errors.append(f'{p}: authored hashed _downloads path')
    for ref in re.findall(r'/_images/([A-Za-z0-9_./ .-]+?\.(?:png|jpg|jpeg|gif|svg))',text):
        if not (DOCS/'_images'/ref).exists():errors.append(f'{p}: missing /_images/{ref}')
    for ref in re.findall(r'<([^<>]+)>`',text):
        if ref.startswith(('http://','https://','#')):continue
        target=(p.parent/ref).resolve()
        if 'files/' in ref and not target.exists():errors.append(f'{p}: missing download target {ref}')
# Python syntax
for p in (DOCS/'editions'/'alpha'/'4-scripts'/'files').rglob('*.py'):
    try:ast.parse(p.read_text(encoding='utf-8'))
    except Exception as e:errors.append(f'{p}: Python parse error {e}')
# Placeholders
for p in [ROOT/'README.md',ROOT/'.github/CODEOWNERS',ROOT/'CITATION.cff']:
    if p.exists() and 'OWNER' in p.read_text(encoding='utf-8'):warnings.append(f'{p}: replace OWNER placeholder before public release')
print(f'Errors: {len(errors)}  Warnings: {len(warnings)}')
for x in errors:print('ERROR',x)
for x in warnings:print('WARN ',x)
sys.exit(1 if errors else 0)
