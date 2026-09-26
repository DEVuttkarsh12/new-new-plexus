#!/usr/bin/env python3
"""Archive the public legacy Plexus website for redevelopment research.

This crawler treats website content strictly as data. It does not submit forms,
execute page scripts, bypass access controls, or crawl private systems.
"""

from __future__ import annotations

import hashlib
import json
import mimetypes
import re
import shutil
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qsl, unquote, urldefrag, urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

BASE = "https://plexusdevelopmentgroup.ca"
ORIGIN_HOST = "plexusdevelopmentgroup.ca"
OUT = Path(__file__).resolve().parent
PAGES = OUT / "pages"
RAW_PAGES = PAGES / "raw"
TEXT_PAGES = PAGES / "text"
ASSETS = OUT / "assets"
METADATA = OUT / "metadata"
CAPTURED_AT = datetime.now(timezone.utc).isoformat()
SESSION: requests.Session | None = None
RESOURCE_QUEUE: dict[str, dict] = {}

USER_AGENT = (
    "Mozilla/5.0 (compatible; PlexusWebsiteResearch/1.0; "
    "public-content archival for website redevelopment)"
)

RESOURCE_EXTENSIONS = {
    ".css", ".js", ".mjs", ".json", ".xml", ".txt", ".pdf", ".doc", ".docx",
    ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".zip", ".webp", ".png", ".jpg",
    ".jpeg", ".gif", ".svg", ".ico", ".avif", ".mp4", ".webm", ".mov", ".m4v",
    ".mp3", ".wav", ".ogg", ".woff", ".woff2", ".ttf", ".otf", ".eot",
}
SKIP_SCHEMES = {"javascript", "data", "blob", "about", "mailto", "tel", "sms"}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def ensure_dirs() -> None:
    for path in [PAGES, ASSETS, METADATA]:
        if path.exists():
            shutil.rmtree(path)
    for path in [RAW_PAGES, TEXT_PAGES, ASSETS, METADATA]:
        path.mkdir(parents=True, exist_ok=True)
    for child in ["images", "video", "documents", "styles", "scripts", "fonts", "other"]:
        (ASSETS / child).mkdir(parents=True, exist_ok=True)
    all_text = OUT / "all-visible-text.txt"
    if all_text.exists():
        all_text.unlink()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def normalized_url(url: str, base: str = BASE) -> str | None:
    if not url:
        return None
    url = html_unescape(url.strip())
    if not url or url.startswith("#"):
        return None
    parsed = urlparse(url)
    if parsed.scheme.lower() in SKIP_SCHEMES:
        return None
    url, _ = urldefrag(urljoin(base, url))
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return None
    return url


def html_unescape(value: str) -> str:
    # Avoid importing another module for the few entities represented in attributes.
    return (
        value.replace("&amp;", "&")
        .replace("&quot;", '"')
        .replace("&#39;", "'")
        .replace("&apos;", "'")
        .replace("&lt;", "<")
        .replace("&gt;", ">")
    )


def same_site(url: str) -> bool:
    host = (urlparse(url).hostname or "").lower().removeprefix("www.")
    return host == ORIGIN_HOST


def page_path(url: str) -> str:
    parsed = urlparse(url)
    path = unquote(parsed.path or "/")
    if path != "/" and path.endswith("/"):
        path = path[:-1]
    slug = re.sub(r"[^a-zA-Z0-9._-]+", "-", path.strip("/")) or "home"
    return slug.lower()


def response_record(response: requests.Response) -> dict:
    return {
        "url": response.url,
        "status": response.status_code,
        "final_url": response.url,
        "headers": dict(response.headers),
        "fetched_at": now_iso(),
    }


def parse_srcset(value: str) -> list[str]:
    """Parse HTML srcset without mistaking transform commas for separators."""
    value = value or ""
    candidates = re.split(r",\s*(?=(?:https?://|data:|/))", value)
    if len(candidates) == 1 and "," in value and " " not in value.split(",", 1)[0]:
        candidates = value.split(",")
    urls: list[str] = []
    for candidate in candidates:
        parts = candidate.strip().split()
        if parts:
            urls.append(parts[0])
    return urls


def attr_records(page_url: str, attributes: dict[str, str]) -> list[dict]:
    records = []
    for attribute, value in attributes.items():
        values = parse_srcset(value) if attribute in {"srcset", "imagesrcset"} else [value]
        for raw in values:
            url = normalized_url(raw, page_url)
            if url:
                records.append({"url": url, "attribute": attribute, "raw": raw})
    return records


def add_resource(resource_map: dict[str, dict], url: str, page_url: str, kind: str, raw: str = "") -> None:
    if not url:
        return
    if resource_map.get(url):
        refs = resource_map[url]["referenced_by"]
        if page_url not in refs:
            refs.append(page_url)
        return
    resource_map[url] = {
        "url": url,
        "kind": kind,
        "raw": raw or url,
        "referenced_by": [page_url],
    }


def extract_page(page_url: str, response: requests.Response) -> tuple[dict, dict[str, dict], set[str]]:
    raw_bytes = response.content
    if "charset=" not in response.headers.get("Content-Type", "").lower():
        response.encoding = "utf-8"
    raw_html = response.text
    soup = BeautifulSoup(raw_html, "html.parser")
    resources: dict[str, dict] = {}
    internal_links: set[str] = set()

    def collect(attrs: dict[str, str], kind: str) -> None:
        for record in attr_records(page_url, attrs):
            add_resource(resources, record["url"], page_url, kind, record["raw"])

    for img in soup.find_all("img"):
        collect({
            "src": img.get("src", ""),
            "srcset": img.get("srcset", ""),
            "data-src": img.get("data-src", ""),
            "data-lazy-src": img.get("data-lazy-src", ""),
        }, "image")
    for source in soup.find_all("source"):
        collect({"src": source.get("src", ""), "srcset": source.get("srcset", "")}, "image-source")
    for media in soup.find_all(["video", "audio"]):
        collect({"src": media.get("src", ""), "poster": media.get("poster", "")}, "media")
    for source in soup.find_all(["video", "audio"]):
        collect({"src": source.get("src", "")}, "media-source")
    for link in soup.find_all("link"):
        rel = " ".join(link.get("rel", [])).lower()
        href = link.get("href", "")
        if set(rel.split()) & {"preconnect", "dns-prefetch", "prefetch"}:
            continue
        if href:
            kind = "stylesheet" if "stylesheet" in rel else "link"
            if "icon" in rel:
                kind = "icon"
            elif "preload" in rel and (link.get("as") or "").lower() in {"image", "font"}:
                kind = "preload"
            collect({"href": href}, kind)
    for script in soup.find_all("script"):
        if script.get("src"):
            collect({"src": script["src"]}, "script")
    for tag in soup.find_all(True):
        style = tag.get("style")
        if style:
            for raw_url in re.findall(r"url\((?:['\"])?([^)'\"\s]+)", style):
                if raw_url.startswith("#") or raw_url.lower().startswith(("%23", "data:")):
                    continue
                add_resource(resources, normalized_url(raw_url, page_url) or "", page_url, "inline-css-url", raw_url)

    for anchor in soup.find_all("a", href=True):
        href = anchor["href"].strip()
        if href.startswith(("mailto:", "tel:", "javascript:", "#")):
            continue
        url = normalized_url(href, page_url)
        if not url:
            continue
        path = urlparse(url).path.lower()
        if same_site(url) and not any(path.endswith(ext) for ext in RESOURCE_EXTENSIONS):
            internal_links.add(url)

    # Remove builder navigational links from the document extension set.
    title = soup.title.get_text(" ", strip=True) if soup.title else None
    description = None
    keywords = []
    robots = []
    canonical = None
    for meta in soup.find_all("meta"):
        name = (meta.get("name") or meta.get("property") or "").lower()
        content = meta.get("content")
        if not content:
            continue
        if name in {"description", "og:description", "twitter:description"} and description is None:
            description = clean_text(content)
        if name == "keywords":
            keywords = [part.strip() for part in content.split(",") if part.strip()]
        if name == "robots":
            robots = [part.strip() for part in content.split(",") if part.strip()]
        if name in {"og:url", "twitter:url"} and canonical is None:
            canonical = normalized_url(content, page_url)
    for link in soup.find_all("link", rel=lambda value: value and "canonical" in value):
        canonical = normalized_url(link.get("href", ""), page_url) or canonical

    headings = {}
    for level in range(1, 7):
        headings[f"h{level}"] = [clean_text(node.get_text(" ", strip=True)) for node in soup.find_all(f"h{level}")]

    for tag in soup(["script", "style", "noscript", "svg"]):
        tag.decompose()
    visible_lines = [clean_text(line) for line in soup.get_text("\n").splitlines()]
    visible_text = "\n".join(line for line in visible_lines if line)

    links = []
    for anchor in soup.find_all("a", href=True):
        links.append({
            "text": clean_text(anchor.get_text(" ", strip=True)),
            "href": anchor["href"],
            "resolved": normalized_url(anchor["href"], page_url),
            "rel": anchor.get("rel", []),
            "target": anchor.get("target"),
        })

    images = []
    for img in soup.find_all("img"):
        images.append({
            "src": img.get("src"),
            "srcset": img.get("srcset"),
            "alt": img.get("alt"),
            "title": img.get("title"),
            "width": img.get("width"),
            "height": img.get("height"),
            "loading": img.get("loading"),
        })

    media = []
    for node in soup.find_all(["video", "audio", "source"]):
        media.append({
            "tag": node.name,
            "src": node.get("src"),
            "poster": node.get("poster"),
            "type": node.get("type"),
            "label": node.get("label"),
        })

    forms = []
    for form in soup.find_all("form"):
        fields = []
        for field in form.find_all(["input", "textarea", "select", "button"]):
            fields.append({
                "tag": field.name,
                "type": field.get("type"),
                "name": field.get("name"),
                "placeholder": field.get("placeholder"),
                "required": field.has_attr("required"),
                "autocomplete": field.get("autocomplete"),
                "options": [option.get_text(" ", strip=True) for option in field.find_all("option")],
            })
        forms.append({
            "action": normalized_url(form.get("action", ""), page_url) or form.get("action", ""),
            "method": (form.get("method") or "get").lower(),
            "id": form.get("id"),
            "name": form.get("name"),
            "fields": fields,
        })

    json_ld = []
    for script in BeautifulSoup(raw_html, "html.parser").find_all("script", type="application/ld+json"):
        text = script.string or script.get_text()
        try:
            json_ld.append(json.loads(text))
        except json.JSONDecodeError:
            json_ld.append({"parse_error": True, "raw": text})

    scripts = []
    for script in BeautifulSoup(raw_html, "html.parser").find_all("script"):
        scripts.append({
            "src": script.get("src"),
            "type": script.get("type"),
            "integrity": script.get("integrity"),
            "crossorigin": script.get("crossorigin"),
        })

    styles = []
    for link in BeautifulSoup(raw_html, "html.parser").find_all("link", href=True):
        rel = " ".join(link.get("rel", [])).lower()
        if "stylesheet" in rel or "preload" in rel:
            styles.append({"href": link.get("href"), "rel": link.get("rel"), "as": link.get("as")})

    record = {
        "url": page_url,
        "response": response_record(response),
        "sha256": sha256_bytes(raw_bytes),
        "bytes": len(raw_bytes),
        "title": title,
        "description": description,
        "keywords": keywords,
        "robots": robots,
        "canonical": canonical,
        "language": soup.html.get("lang") if soup.html else None,
        "headings": headings,
        "visible_text": visible_text,
        "links": links,
        "images": images,
        "media": media,
        "forms": forms,
        "iframes": [
            {"src": iframe.get("src"), "title": iframe.get("title"), "loading": iframe.get("loading")}
            for iframe in soup.find_all("iframe")
        ],
        "scripts": scripts,
        "styles": styles,
        "json_ld": json_ld,
    }
    return record, resources, internal_links


def safe_filename(url: str, content_type: str, digest: str) -> str:
    parsed = urlparse(url)
    raw_name = unquote(Path(parsed.path).name) or "asset"
    raw_name = re.sub(r"[^a-zA-Z0-9._-]+", "-", raw_name).strip("-.") or "asset"
    extension = Path(raw_name).suffix.lower()
    mime = content_type.split(";", 1)[0].strip().lower()
    if not extension or extension not in RESOURCE_EXTENSIONS:
        extension = mimetypes.guess_extension(mime) or ""
    return f"{digest[:12]}-{raw_name[:100]}{extension}"


def category_for(url: str, content_type: str, kind: str) -> str:
    mime = content_type.split(";", 1)[0].strip().lower()
    path = urlparse(url).path.lower()
    if mime.startswith("image/") or path.endswith((".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg", ".ico", ".avif")):
        return "images"
    if mime.startswith("video/") or mime.startswith("audio/") or path.endswith((".mp4", ".webm", ".mov", ".m4v", ".mp3", ".wav", ".ogg")):
        return "video"
    if mime.startswith("font/") or "font" in mime or path.endswith((".woff", ".woff2", ".ttf", ".otf", ".eot")):
        return "fonts"
    if kind == "stylesheet" or mime == "text/css" or path.endswith(".css"):
        return "styles"
    if kind == "script" or "javascript" in mime or path.endswith((".js", ".mjs")):
        return "scripts"
    if mime in {"application/pdf", "application/msword", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"} or path.endswith((".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".zip")):
        return "documents"
    return "other"


def fetch_asset(url: str, resource: dict) -> dict:
    headers = {"Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8", "Referer": BASE + "/"}
    try:
        response = SESSION.get(url, headers=headers, timeout=(15, 90), allow_redirects=True)
        result = {
            **resource,
            "response": response_record(response),
            "fetched_at": now_iso(),
        }
        if response.ok and response.content:
            digest = sha256_bytes(response.content)
            category = category_for(response.url, response.headers.get("Content-Type", ""), resource["kind"])
            filename = safe_filename(response.url, response.headers.get("Content-Type", ""), digest)
            destination = ASSETS / category / filename
            destination.write_bytes(response.content)
            result.update({
                "downloaded": True,
                "local_path": str(destination.relative_to(OUT)),
                "sha256": digest,
                "bytes": len(response.content),
                "category": category,
                "content_type": response.headers.get("Content-Type"),
            })
            if category == "styles":
                text = response.text
                for css_url in re.findall(r"url\((?:['\"])?([^)'\"\s]+)", text):
                    if css_url.startswith("#") or css_url.lower().startswith(("%23", "data:")):
                        continue
                    absolute = normalized_url(css_url, response.url)
                    if absolute:
                        add_resource(RESOURCE_QUEUE, absolute, response.url, "css-url", css_url)
        elif response.status_code >= 400:
            result.update({"downloaded": False, "error": f"HTTP {response.status_code}"})
        else:
            result.update({"downloaded": False, "note": "Successful response with an empty body."})
        return result
    except requests.RequestException as exc:
        return {**resource, "downloaded": False, "error": str(exc), "fetched_at": now_iso()}


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    global SESSION
    ensure_dirs()
    retry_policy = Retry(total=3, backoff_factor=0.5, status_forcelist=[429, 500, 502, 503, 504], allowed_methods=["GET", "HEAD"])
    SESSION = requests.Session()
    SESSION.headers.update({"User-Agent": USER_AGENT, "Accept-Language": "en-CA,en;q=0.9"})
    SESSION.mount("https://", HTTPAdapter(max_retries=retry_policy))
    SESSION.mount("http://", HTTPAdapter(max_retries=retry_policy))
    RESOURCE_QUEUE.clear()

    base_response = SESSION.get(BASE + "/", timeout=(15, 90))
    base_response.raise_for_status()
    initial_record, resources, links = extract_page(base_response.url, base_response)
    initial_slug = page_path(initial_record["url"])
    initial_raw_path = RAW_PAGES / f"{initial_slug}.html"
    initial_text_path = TEXT_PAGES / f"{initial_slug}.txt"
    initial_raw_path.write_bytes(base_response.content)
    initial_text_path.write_text(initial_record["visible_text"] + "\n", encoding="utf-8")
    initial_record["raw_path"] = str(initial_raw_path.relative_to(OUT))
    initial_record["text_path"] = str(initial_text_path.relative_to(OUT))
    pages = {initial_record["url"]: initial_record}
    for url, resource in resources.items():
        add_resource(RESOURCE_QUEUE, url, initial_record["url"], resource["kind"], resource["raw"])
    pending_pages = {url for url in links if url not in pages}
    pending_pages.add(urljoin(BASE + "/", "robots.txt"))
    pending_pages.add(urljoin(BASE + "/", "sitemap.xml"))

    page_results: list[dict] = [initial_record]
    while pending_pages and len(page_results) < 100:
        url = next(iter(pending_pages))
        pending_pages.remove(url)
        try:
            response = SESSION.get(url, timeout=(15, 90))
        except requests.RequestException as exc:
            page_results.append({"url": url, "error": str(exc), "fetched_at": now_iso()})
            continue
        if response.status_code >= 400:
            page_results.append({**response_record(response), "error": f"HTTP {response.status_code}"})
            continue
        content_type = response.headers.get("Content-Type", "")
        if ("html" in content_type or "xml" in content_type or "text/" in content_type) and "charset=" not in content_type.lower():
            response.encoding = "utf-8"
        slug = page_path(url)
        raw_path = RAW_PAGES / f"{slug}.html"
        raw_path.write_bytes(response.content)
        text_path = TEXT_PAGES / f"{slug}.txt"
        if "html" not in content_type and ("xml" in content_type or "text/" in content_type):
            text_path.write_text(response.text, encoding="utf-8")
        if "html" in content_type:
            record, page_resources, discovered = extract_page(response.url, response)
            text_path.write_text(record["visible_text"] + "\n", encoding="utf-8")
            record["raw_path"] = str(raw_path.relative_to(OUT))
            record["text_path"] = str(text_path.relative_to(OUT))
            if record["url"] in pages:
                page_results.append(record)
                continue
            pages[record["url"]] = record
            page_results.append(record)
            for resource_url, resource in page_resources.items():
                add_resource(RESOURCE_QUEUE, resource_url, record["url"], resource["kind"], resource["raw"])
            for discovered_url in discovered:
                parsed = urlparse(discovered_url)
                if same_site(discovered_url) and not any(parsed.path.lower().endswith(ext) for ext in RESOURCE_EXTENSIONS):
                    if discovered_url not in pages:
                        pending_pages.add(discovered_url)
        else:
            page_results.append({
                **response_record(response),
                "raw_path": str(raw_path.relative_to(OUT)),
                "bytes": len(response.content),
                "sha256": sha256_bytes(response.content),
            })
        time.sleep(0.08)

    # Process assets breadth-first because CSS can add font/image dependencies.
    asset_results: list[dict] = []
    processed: set[str] = set()
    while RESOURCE_QUEUE and len(asset_results) < 1000:
        batch = [url for url in list(RESOURCE_QUEUE) if url not in processed][:40]
        if not batch:
            break
        for url in batch:
            processed.add(url)
            resource = RESOURCE_QUEUE.pop(url)
            asset_results.append(fetch_asset(url, resource))
            time.sleep(0.025)

    page_records = [record for record in page_results if record.get("title") is not None]
    outbound = defaultdict(list)
    internal = defaultdict(list)
    for page in page_records:
        for link in page.get("links", []):
            resolved = link.get("resolved")
            if not resolved:
                continue
            if same_site(resolved):
                internal[resolved].append(page["url"])
            else:
                outbound[resolved].append({"page": page["url"], "text": link.get("text"), "href": link.get("href")})

    all_text = []
    for page in sorted(page_records, key=lambda item: item["url"]):
        all_text.append(f"===== {page['url']} =====\n{page.get('title', '')}\n\n{page.get('visible_text', '')}\n")
    (OUT / "all-visible-text.txt").write_text("\n".join(all_text), encoding="utf-8")

    manifest = {
        "capture": {
            "started_or_completed_at": CAPTURED_AT,
            "base_url": BASE,
            "scope": "Public pages and publicly referenced resources on or directly used by the legacy Plexus site; no form submission or private-system access.",
            "user_agent": USER_AGENT,
        },
        "counts": {
            "html_pages": len(page_records),
            "fetch_results": len(page_results),
            "assets_referenced": len(asset_results),
            "assets_downloaded": sum(bool(item.get("downloaded")) for item in asset_results),
            "internal_link_targets": len(internal),
            "external_link_targets": len(outbound),
        },
        "pages": [
            {
                "url": page["url"],
                "title": page.get("title"),
                "description": page.get("description"),
                "canonical": page.get("canonical"),
                "bytes": page.get("bytes"),
                "raw_path": page.get("raw_path"),
                "text_path": page.get("text_path"),
            }
            for page in page_records
        ],
    }

    write_json(METADATA / "capture-manifest.json", manifest)
    write_json(METADATA / "pages.json", page_results)
    write_json(METADATA / "assets.json", asset_results)
    write_json(METADATA / "internal-links.json", dict(internal))
    write_json(METADATA / "external-links.json", dict(outbound))
    write_json(METADATA / "fetch-errors.json", [
        item for item in page_results + asset_results
        if item.get("error") or item.get("response", {}).get("status", 0) >= 400
    ])

    # Lightweight CSV for quick project-team review.
    import csv
    with (METADATA / "pages.csv").open("w", newline="", encoding="utf-8") as handle:
        fields = ["url", "title", "description", "canonical", "robots", "language", "bytes", "sha256", "raw_path", "text_path"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for page in page_records:
            writer.writerow({field: page.get(field) for field in fields})

    print(json.dumps(manifest["counts"], indent=2))


if __name__ == "__main__":
    main()
