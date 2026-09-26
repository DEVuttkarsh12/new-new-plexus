#!/usr/bin/env python3
"""Build a deduplicated image inventory and contact sheets from the legacy capture."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import time
from collections import defaultdict
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

import requests
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
METADATA = ROOT / "metadata"
ORIGINALS = ROOT / "media-originals"
SHEETS = ROOT / "media-contact-sheets"


def stable_image_key(url: str) -> str:
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower()
    path = unquote(parsed.path)
    account = "DRpyQ9BauhckYzhd"
    if host == "assets.zyrosite.com" and account in path:
        return "zyro:" + path.split(account, 1)[1].lstrip("/")
    if host == "images.unsplash.com":
        return "unsplash:" + path.lstrip("/").split("?", 1)[0]
    if host.endswith("googleusercontent.com") or "gstatic" in host or "googleapis" in host:
        return host + ":" + path
    return host + ":" + path


def original_url(url: str) -> str:
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower()
    account = "DRpyQ9BauhckYzhd"
    if host == "assets.zyrosite.com" and account in unquote(parsed.path):
        suffix = unquote(parsed.path).split(account, 1)[1].lstrip("/")
        return f"https://assets.zyrosite.com/{account}/{suffix}"
    if host == "images.unsplash.com":
        photo = unquote(parsed.path).lstrip("/")
        return f"https://images.unsplash.com/{photo}?fm=jpg&fit=max&w=2400&q=90"
    if host == "images.pexels.com":
        query = parse_qs(parsed.query)
        flat = {key: values[-1] for key, values in query.items() if key != "auto"}
        flat["fm"] = "jpg"
        flat["w"] = "2400"
        from urllib.parse import urlencode
        return f"https://{host}{parsed.path}?{urlencode(flat)}"
    return url


def safe_name(key: str) -> str:
    name = key.replace(":", "___").replace("/", "___")
    return re.sub(r"[^a-zA-Z0-9._-]+", "-", name).strip("-.")


def dimensions(path: Path) -> tuple[int | None, int | None]:
    try:
        with Image.open(path) as image:
            return image.size
    except Exception:
        return None, None


def shorten(text: str, length: int = 68) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    return text if len(text) <= length else text[: length - 1] + "…"


def make_contact_sheet(items: list[dict], index: int) -> Path:
    cell_w, cell_h = 420, 330
    cols, rows = 3, 4
    canvas = Image.new("RGB", (cols * cell_w, rows * cell_h), "#e8e8e2")
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default()
    for slot, item in enumerate(items):
        x = (slot % cols) * cell_w
        y = (slot // cols) * cell_h
        path = ROOT / (item["source_local_path"] or item["primary_local_path"])
        try:
            with Image.open(path) as source:
                preview = ImageOps.contain(source.convert("RGB"), (cell_w - 24, cell_h - 78))
            px = x + (cell_w - preview.width) // 2
            py = y + 10 + (cell_h - 78 - preview.height) // 2
            canvas.paste(preview, (px, py))
        except Exception:
            draw.rectangle((x + 12, y + 12, x + cell_w - 12, y + cell_h - 80), fill="#c8c8c2")
        label_y = y + cell_h - 62
        draw.text((x + 12, label_y), f"{index * 12 + slot + 1:02d}  {shorten(item['key'], 53)}", fill="#142820", font=font)
        draw.text((x + 12, label_y + 18), f"{item.get('width')}x{item.get('height')}  {item['alt_texts'][:1]}", fill="#37473f", font=font)
    SHEETS.mkdir(parents=True, exist_ok=True)
    destination = SHEETS / f"contact-sheet-{index + 1:02d}.jpg"
    canvas.save(destination, quality=90, optimize=True)
    return destination


def main() -> None:
    assets = json.loads((METADATA / "assets.json").read_text(encoding="utf-8"))
    pages = json.loads((METADATA / "pages.json").read_text(encoding="utf-8"))

    alt_by_url: dict[str, set[str]] = defaultdict(set)
    for page in pages:
        for image in page.get("images", []):
            alt = (image.get("alt") or "").strip()
            for field in [image.get("src"), *(image.get("srcset") or "").split(",")]:
                if field:
                    alt_by_url[field.strip().split()[0]].add(alt)

    grouped: dict[str, list[dict]] = defaultdict(list)
    for asset in assets:
        if asset.get("category") != "images" or not asset.get("downloaded"):
            continue
        grouped[stable_image_key(asset["url"])].append(asset)

    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (compatible; PlexusWebsiteResearch/1.0; public media inventory)",
        "Referer": "https://plexusdevelopmentgroup.ca/",
        "Accept": "image/avif,image/webp,image/*,*/*;q=0.8",
    })
    ORIGINALS.mkdir(parents=True, exist_ok=True)

    inventory = []
    for number, key in enumerate(sorted(grouped), start=1):
        variants = grouped[key]
        ranked = []
        for variant in variants:
            width, height = dimensions(ROOT / variant["local_path"])
            ranked.append(((width or 0) * (height or 0), variant.get("bytes", 0), variant, width, height))
        _, _, primary, width, height = max(ranked, key=lambda row: (row[0], row[1]))
        urls = {variant["url"] for variant in variants}
        alt_texts = set()
        for url in urls:
            alt_texts.update(alt_by_url.get(url, set()))
        source = original_url(primary["url"])
        source_filename = safe_name(key) + Path(urlparse(source).path).suffix.lower()
        source_path = ORIGINALS / source_filename
        source_record = {"url": source, "downloaded": False}
        existing_is_avif = source_path.exists() and b"ftypavif" in source_path.read_bytes()[:64]
        if not source_path.exists() or existing_is_avif:
            try:
                response = session.get(source, timeout=(15, 90))
                if response.ok and response.content:
                    source_path.write_bytes(response.content)
                    source_record = {
                        "url": response.url,
                        "status": response.status_code,
                        "content_type": response.headers.get("Content-Type"),
                        "bytes": len(response.content),
                        "sha256": hashlib.sha256(response.content).hexdigest(),
                        "downloaded": True,
                    }
                else:
                    source_record["error"] = f"HTTP {response.status_code}"
            except requests.RequestException as exc:
                source_record["error"] = str(exc)
            time.sleep(0.05)
        elif source_path.exists():
            source_record = {
                "url": source,
                "downloaded": True,
                "bytes": source_path.stat().st_size,
                "sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
            }
        source_width, source_height = dimensions(source_path) if source_path.exists() else (None, None)
        inventory.append({
            "number": number,
            "key": key,
            "source_filename": Path(urlparse(source).path).name,
            "source_url": source,
            "source_local_path": str(source_path.relative_to(ROOT)) if source_path.exists() else None,
            "source_width": source_width,
            "source_height": source_height,
            "source_content_type": source_record.get("content_type"),
            "source_bytes": source_record.get("bytes"),
            "source_sha256": source_record.get("sha256"),
            "source_fetch": source_record,
            "primary_used_url": primary["url"],
            "primary_local_path": primary["local_path"],
            "width": width,
            "height": height,
            "alt_texts": sorted(text for text in alt_texts if text),
            "referenced_by": sorted({page for variant in variants for page in variant.get("referenced_by", [])}),
            "variant_count": len(variants),
            "variant_urls": sorted(urls),
        })

    (METADATA / "media-inventory.json").write_text(json.dumps(inventory, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    with (METADATA / "media-inventory.csv").open("w", newline="", encoding="utf-8") as handle:
        fields = ["number", "key", "source_filename", "source_url", "source_local_path", "source_width", "source_height", "width", "height", "alt_texts", "referenced_by", "variant_count"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for item in inventory:
            row = {field: item.get(field) for field in fields}
            row["alt_texts"] = " | ".join(item["alt_texts"])
            row["referenced_by"] = " | ".join(item["referenced_by"])
            writer.writerow(row)

    lines = ["# Legacy Plexus image inventory", "", f"Unique image sources: **{len(inventory)}**", "", "Alt text is transcribed from the legacy site. Empty alt text may be intentional or may indicate an accessibility issue.", ""]
    for item in inventory:
        lines.extend([
            f"## {item['number']:02d}. {item['source_filename'] or item['key']}",
            f"- Stable key: `{item['key']}`",
            f"- Source: {item['source_url']}",
            f"- Original capture: `{item['source_local_path']}`" if item["source_local_path"] else "- Original capture: unavailable",
            f"- Dimensions: {item['source_width'] or '?'} × {item['source_height'] or '?'}",
            f"- Used on: {', '.join(Path(url).stem for url in item['referenced_by'])}",
            f"- Legacy alt text: {'; '.join(item['alt_texts']) if item['alt_texts'] else 'None'}",
            f"- Responsive variants captured: {item['variant_count']}",
            "",
        ])
    (ROOT / "MEDIA-INVENTORY.md").write_text("\n".join(lines), encoding="utf-8")

    for index in range(0, len(inventory), 12):
        make_contact_sheet(inventory[index:index + 12], index // 12)

    print(json.dumps({
        "unique_images": len(inventory),
        "originals_downloaded": sum(bool(item["source_local_path"]) for item in inventory),
        "contact_sheets": (len(inventory) + 11) // 12,
    }, indent=2))


if __name__ == "__main__":
    main()
