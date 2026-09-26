#!/usr/bin/env python3
"""Compare rendered Chrome DOM/network activity with the static public-site capture."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent
DOM_DIR = ROOT / "rendered-dom"
NETLOG_DIR = ROOT / "chrome-netlogs"
METADATA = ROOT / "metadata"
CHROME_NOISE = {
    "clients2.google.com", "android.clients.google.com", "accounts.google.com",
    "redirector.gvt1.com", "safebrowsingohttpgateway.googleapis.com",
    "www.google.com", "content-autofill.googleapis.com",
}


def normalize_url(url: str) -> str:
    parsed = urlparse(url)
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path, "", parsed.query, ""))


def parse_netlog(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    records = []
    seen = set()
    for event in data.get("events", []):
        params = event.get("params", {})
        url = params.get("url")
        if not url or not url.startswith(("http://", "https://")):
            continue
        if event.get("type") not in {125, 132, 586}:
            continue
        record = {
            "url": url,
            "normalized_url": normalize_url(url),
            "host": (urlparse(url).hostname or "").lower(),
            "method": params.get("method", "GET"),
            "request_type": params.get("request_type"),
            "event_type": event.get("type"),
        }
        key = (record["normalized_url"], record["method"], record["request_type"])
        if key not in seen:
            seen.add(key)
            records.append(record)
    return records


def parse_rendered(path: Path) -> dict:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    for node in soup(["script", "style", "noscript", "svg"]):
        node.decompose()
    visible = "\n".join(filter(None, (re.sub(r"\s+", " ", line).strip() for line in soup.get_text("\n").splitlines())))
    return {
        "title": soup.title.get_text(" ", strip=True) if soup.title else None,
        "headings": {f"h{level}": [n.get_text(" ", strip=True) for n in soup.find_all(f"h{level}")] for level in range(1, 7)},
        "links": [
            {"text": a.get_text(" ", strip=True), "href": a.get("href"), "target": a.get("target"), "rel": a.get("rel", [])}
            for a in soup.find_all("a", href=True)
        ],
        "images": [
            {"src": img.get("src"), "alt": img.get("alt"), "width": img.get("width"), "height": img.get("height")}
            for img in soup.find_all("img")
        ],
        "media": [
            {"tag": node.name, "src": node.get("src"), "poster": node.get("poster"), "type": node.get("type")}
            for node in soup.find_all(["video", "audio", "source"])
        ],
        "forms": [
            {
                "action": form.get("action"),
                "method": form.get("method"),
                "fields": [
                    {"tag": field.name, "type": field.get("type"), "name": field.get("name"), "placeholder": field.get("placeholder")}
                    for field in form.find_all(["input", "textarea", "select", "button"])
                ],
            }
            for form in soup.find_all("form")
        ],
        "visible_text": visible,
        "dom_bytes": path.stat().st_size,
    }


def main() -> None:
    static_assets = json.loads((METADATA / "assets.json").read_text(encoding="utf-8"))
    static_urls = {normalize_url(item["url"]) for item in static_assets}
    rendered = {}
    all_network = []
    page_summaries = []
    for dom_path in sorted(DOM_DIR.glob("*.html")):
        name = dom_path.stem
        parsed_dom = parse_rendered(dom_path)
        netlog_path = NETLOG_DIR / f"{name}-netlog.json"
        network = parse_netlog(netlog_path) if netlog_path.exists() else []
        all_network.extend({"page": name, **item} for item in network)
        site_network = [item for item in network if item["host"] not in CHROME_NOISE]
        missing = sorted({item["normalized_url"] for item in site_network if item["normalized_url"] not in static_urls})
        rendered[name] = {
            **parsed_dom,
            "network_count": len(network),
            "site_network_count": len(site_network),
            "site_hosts": sorted({item["host"] for item in site_network}),
            "runtime_urls_not_in_static_inventory": missing,
        }
        page_summaries.append({
            "page": name,
            "dom_bytes": parsed_dom["dom_bytes"],
            "links": len(parsed_dom["links"]),
            "images": len(parsed_dom["images"]),
            "media": len(parsed_dom["media"]),
            "forms": len(parsed_dom["forms"]),
            "site_network_requests": len(site_network),
            "runtime_urls_not_in_static_inventory": len(missing),
        })

    (METADATA / "rendered-dom-inventory.json").write_text(json.dumps(rendered, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (METADATA / "rendered-network.json").write_text(json.dumps(all_network, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (METADATA / "rendered-capture-summary.json").write_text(json.dumps(page_summaries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(page_summaries, indent=2))


if __name__ == "__main__":
    main()
