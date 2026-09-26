#!/usr/bin/env python3
"""Render each public legacy page in isolated headless Chrome and save DOM/netlogs."""

from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parent
DOM_DIR = ROOT / "rendered-dom"
NETLOG_DIR = ROOT / "chrome-netlogs"
PAGES = {
    "home": "https://plexusdevelopmentgroup.ca/",
    "projects": "https://plexusdevelopmentgroup.ca/nova-scotia-construction-projects",
    "residential": "https://plexusdevelopmentgroup.ca/residential-construction",
    "commercial": "https://plexusdevelopmentgroup.ca/commercial-construction",
    "industrial": "https://plexusdevelopmentgroup.ca/industrial-construction",
    "community": "https://plexusdevelopmentgroup.ca/community",
    "contact": "https://plexusdevelopmentgroup.ca/contact-for-real-estate-opportunities",
}

for directory in [DOM_DIR, NETLOG_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

for name, url in PAGES.items():
    dom_path = DOM_DIR / f"{name}.html"
    netlog_path = NETLOG_DIR / f"{name}-netlog.json"
    command = [
        "google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu",
        "--disable-dev-shm-usage", "--disable-background-networking",
        "--virtual-time-budget=10000", f"--log-net-log={netlog_path}",
        "--dump-dom", url,
    ]
    with dom_path.open("wb") as output:
        subprocess.run(command, stdout=output, stderr=subprocess.DEVNULL, check=True, timeout=90)
    print(f"{name}: {dom_path.stat().st_size} bytes")
    time.sleep(0.2)
