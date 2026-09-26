#!/usr/bin/env python3
"""Download public runtime chunks discovered by rendered Chrome network capture."""

from __future__ import annotations

import hashlib
import json
import re
import time
from pathlib import Path
from urllib.parse import urlparse

import requests

ROOT = Path(__file__).resolve().parent
METADATA = ROOT / "metadata"
DESTINATION = ROOT / "assets" / "scripts"
DESTINATION.mkdir(parents=True, exist_ok=True)

rendered = json.loads((METADATA / "rendered-dom-inventory.json").read_text(encoding="utf-8"))
urls = sorted({
    url
    for page in rendered.values()
    for url in page.get("runtime_urls_not_in_static_inventory", [])
    if urlparse(url).hostname in {"plexusdevelopmentgroup.ca", "assets.zyrosite.com", "cdn.zyrosite.com"}
    and not url.endswith("/traffic.txt")
})

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (compatible; PlexusWebsiteResearch/1.0; public runtime archive)",
    "Referer": "https://plexusdevelopmentgroup.ca/",
})
records = []
processed = set()
while urls and len(processed) < 500:
    url = urls.pop(0)
    if url in processed:
        continue
    processed.add(url)
    try:
        response = session.get(url, timeout=(15, 90))
        record = {
            "url": url,
            "final_url": response.url,
            "status": response.status_code,
            "content_type": response.headers.get("Content-Type"),
            "bytes": len(response.content),
            "sha256": hashlib.sha256(response.content).hexdigest(),
            "referenced_by_rendered_pages": [
                name for name, page in rendered.items()
                if url in page.get("runtime_urls_not_in_static_inventory", [])
            ],
        }
        if response.ok and response.content:
            filename = Path(urlparse(response.url).path).name
            path = DESTINATION / f"{record['sha256'][:12]}-{filename}"
            path.write_bytes(response.content)
            record["downloaded"] = True
            record["local_path"] = str(path.relative_to(ROOT))
            if "javascript" in (response.headers.get("Content-Type") or "") or filename.endswith((".js", ".mjs")):
                text = response.text
                discovered = set(re.findall(r"(?:https://plexusdevelopmentgroup\.ca)?(/_astro-[^/\"'`\s]+/[A-Za-z0-9_.-]+\.js)", text))
                for match in discovered:
                    absolute = "https://plexusdevelopmentgroup.ca" + match
                    if absolute not in processed:
                        urls.append(absolute)
        else:
            record["downloaded"] = False
            record["error"] = f"HTTP {response.status_code}"
    except requests.RequestException as exc:
        record = {"url": url, "downloaded": False, "error": str(exc)}
    records.append(record)
    time.sleep(0.05)

(METADATA / "rendered-runtime-assets.json").write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps({
    "runtime_assets": len(records),
    "downloaded": sum(bool(item.get("downloaded")) for item in records),
    "bytes": sum(item.get("bytes", 0) for item in records),
}, indent=2))
