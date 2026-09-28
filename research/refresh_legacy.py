"""Refresh every public legacy page without replacing the original deep archive."""
from pathlib import Path
import importlib.util
import json
import hashlib
from urllib.parse import urlparse
from datetime import datetime, timezone
import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).parent
OLD = ROOT / 'legacy-site-capture-2026-09-25'
OUT = ROOT / 'legacy-site-refresh-2026-09-28'
spec = importlib.util.spec_from_file_location('legacy_capture', OLD / 'capture.py')
capture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(capture)
OUT.mkdir(exist_ok=True)
(OUT / 'pages').mkdir(exist_ok=True)
session = requests.Session()
session.headers['User-Agent'] = capture.USER_AGENT
base = capture.BASE
queue = [base + '/']
records, resources, visited, infrastructure = [], {}, set(), []
for path in ['robots.txt', 'sitemap.xml']:
    response = session.get(base + '/' + path, timeout=40)
    (OUT / path).write_bytes(response.content)
    infrastructure.append({'url':response.url,'status':response.status_code})
    if path == 'sitemap.xml':
        queue.extend(x.get_text() for x in BeautifulSoup(response.text,'xml').find_all('loc'))
while queue:
    url = queue.pop(0)
    if url.rstrip('/') == base:
        url = base + '/'
    if url in visited:
        continue
    visited.add(url)
    response = session.get(url, timeout=40)
    response.raise_for_status()
    slug = urlparse(url).path.strip('/') or 'home'
    (OUT / 'pages' / (slug.replace('/','-') + '.html')).write_bytes(response.content)
    record, asset_records, links = capture.extract_page(url, response)
    records.append(record)
    resources.update(asset_records)
    queue.extend(sorted(x for x in links if capture.same_site(x) and x not in visited))
    print(slug, response.status_code, len(response.content), flush=True)
old = {x['url']:x for x in json.loads((OLD/'metadata/pages.json').read_text())}
comparison = []
for record in records:
    before = old.get(record['url'], {})
    comparison.append({'url':record['url'], 'same_html':before.get('sha256') == record['sha256'],
                       'same_visible_text':before.get('visible_text') == record.get('visible_text')})
report = {'captured_at':datetime.now(timezone.utc).isoformat(), 'pages':records,
          'resources':resources,'infrastructure':infrastructure,'comparison':comparison}
(OUT/'capture.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
texts = []
for record in records:
    soup = BeautifulSoup((OUT/'pages'/((urlparse(record['url']).path.strip('/') or 'home')+'.html')).read_text(),'html.parser')
    for el in soup(['script','style','noscript']):
        el.decompose()
    texts.append(record['url']+'\n'+soup.get_text('\n',strip=True))
(OUT/'all-visible-text.txt').write_text('\n\n'.join(texts))
print(json.dumps({'pages':len(records),'referenced_resources':len(resources),'comparison':comparison},indent=2))
