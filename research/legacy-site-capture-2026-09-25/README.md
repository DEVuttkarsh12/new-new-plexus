# Plexus Development Group legacy website capture

Captured on **September 25, 2026** from the public site:

- https://plexusdevelopmentgroup.ca/
- https://plexusdevelopmentgroup.ca/nova-scotia-construction-projects
- https://plexusdevelopmentgroup.ca/residential-construction
- https://plexusdevelopmentgroup.ca/commercial-construction
- https://plexusdevelopmentgroup.ca/industrial-construction
- https://plexusdevelopmentgroup.ca/community
- https://plexusdevelopmentgroup.ca/contact-for-real-estate-opportunities

This directory is a research archive for the website revamp. It is not part of the production build and is not served by the current Vite site.

## Capture totals

- 7 public HTML pages
- 1 `robots.txt` and 1 XML sitemap
- 661 directly referenced static resource URLs downloaded, represented by 617 unique local files after exact-content deduplication
- 11 additional runtime JavaScript chunks found through rendered Chrome network capture
- 43 deduplicated source images, including 43 original or high-resolution source captures
- 1 full-length hero video
- 5 unique external link targets
- 7 pages also rendered in isolated headless Chrome for dynamic-DOM and runtime comparison
- 7 full-page desktop screenshots at a 1440 px viewport
- No forms were submitted
- No private systems, authenticated areas, or access controls were accessed

The complete archive is approximately 187 MB.

## Important research documents

- `CONTENT-AND-PROJECT-INDEX.md`: page-by-page content, project facts, visual-only information, and terminology
- `CLAIMS-NEEDS-CONFIRMATION.md`: conflicts, stale statements, ambiguous names, and copy issues
- `SEO-TECHNICAL-INVENTORY.md`: metadata, schema, sitemap, hosting, indexability, forms, cookies, and runtime architecture
- `MEDIA-INVENTORY.md`: all 43 unique image sources, dimensions, pages, alt text, and local paths
- `MEDIA-VISUAL-NOTES.md`: visual and embedded-text review of concept plans, logos, photography, and video
- `metadata/media-inventory.csv`: spreadsheet-friendly media inventory
- `metadata/pages.json`: complete parsed page records, text, headings, links, images, media, forms, metadata, and schema
- `metadata/assets.json`: resource-level hashes, response headers, and local paths
- `metadata/rendered-dom-inventory.json`: dynamically rendered DOM comparison
- `metadata/rendered-network.json`: browser-observed requests
- `metadata/rendered-runtime-assets.json`: dynamically loaded JavaScript archive
- `metadata/external-links.json`: every outbound link target
- `external-references/`: official Cornwallis planning material and clearly labelled related-source/search leads
- `all-visible-text.txt`: extracted text from every page in one file

## Directory map

- `pages/raw/`: original HTML responses exactly as served
- `pages/text/`: clean visible text for each HTML page
- `assets/`: responsive image variants, fonts, CSS, JavaScript, and video delivered by the legacy site
- `media-originals/`: deduplicated original or higher-resolution source images
- `media-contact-sheets/`: visual contact sheets for all unique images
- `rendered-dom/`: post-hydration DOM from isolated headless Chrome
- `full-page-screenshots/`: 1440 px full-page captures of all seven routes
- `chrome-netlogs/`: browser network logs used to find dynamic resources
- `metadata/`: structured manifests and inventories
- `legacy-hero-video-contact-sheet.jpg`: six-frame visual capture of the homepage film
- `legacy-pages-contact-sheet.jpg`: thumbnail overview of all seven full-page screenshots
- `SHA256SUMS`: checksums for every archived file except the checksum file itself

## Reproducibility scripts

- `capture.py`: polite static crawler for pages and referenced resources
- `build_media_inventory.py`: deduplicates responsive assets, captures source images, and builds contact sheets
- `capture_rendered.py`: captures rendered DOM and Chrome network logs
- `analyze_rendered.py`: compares rendered output with static crawling
- `capture_rendered_assets.py`: archives runtime JavaScript discovered in network logs
- `capture_full_page_screenshots.mjs`: captures full-page desktop screenshots through Chrome DevTools Protocol

## Scope and limits

- The crawl covered the current public legacy site, its sitemap, all internal navigation, directly referenced media, and browser-loaded runtime code.
- The only project-specific external destination is `https://lifestyleenclave.ca/`; that separate site is not duplicated wholesale in this legacy-domain capture.
- Public stock-media source URLs were preserved. Unsplash and Pexels usage remains subject to their respective licenses.
- The archive records what the public site stated. It does not independently prove project approvals, delivery status, ownership, investment claims, community contributions, or construction milestones.
- Renderings, concept plans, logos, and generic stock imagery must not be represented as completed projects or verified photographs without client confirmation.
- The Internet Archive CDX query returned no archived HTML captures for this domain during the search performed on September 25, 2026.
