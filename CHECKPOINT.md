# Plexus website checkpoint

Updated September 30, 2026.

The client supplied `PLEXUS WEBSITE REVAMP STRATEGY.docx` and approved a full corporate repositioning. The site has been rebuilt as an institutional-style static review build with 28 generated content pages, nine old-route fallbacks, a portfolio and project pages, audience-specific partnership routes, acquisitions, leadership, impact, insights, news, media, careers, search, contact and legal pages.

The user directed us to use only previously sourced project facts and label concepts. The user also confirmed that no CRM or secure upload service is available. Forms currently prepare email drafts and explicitly say they do not send or upload through the website. The site remains a noindex review build (`LAUNCH = False`).

Source of truth: `generate_site.py`, `projects.json`, `dist/revamp.css`, `dist/revamp.js`. Run `python3 generate_site.py` after source/data changes. See `REVAMP-IMPLEMENTATION.md` for verified claims, pending external material, integrations and production tasks. Earlier `Context.md`, research captures and design notes remain as historical records.

Verification completed: Python and JavaScript syntax checks; `git diff --check`; generated internal-link audit with zero missing local links; Chrome headless review at real 390 px and 1440 px viewports; no horizontal overflow on the tested homepage, portfolio and acquisitions pages; project filter, site search, mobile menu and required contact fields behaved as expected. Screenshots are in `/tmp/plexus-cdp-*.png`.

Before production launch: confirm project status and pipeline claims; supply approved images, corporate film, leadership biographies and partner permissions; connect secure forms/CRM and analytics; configure HTTP 301 redirects; review legal text; set production origin and indexing flag; run production accessibility and performance tests.
