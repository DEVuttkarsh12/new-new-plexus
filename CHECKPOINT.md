# CHECKPOINT

Resume point for the Plexus Development Group website.
Last updated September 26, 2026, at the end of the GitHub push session.

Read this file first, then `Context.md` for the full durable project record.

Nothing is mid-edit and nothing is blocked. Working tree is clean, local `main` matches `origin/main`, and the review server is running at http://127.0.0.1:8080.

---

## 1. Where the project stands

The site is feature-complete, verified across every route and breakpoint, documented, and under version control.

Across the last three sessions:

1. Renamed the portfolio concept to **Projects** and rebuilt the navigation to match the previous site exactly.
2. Added **three new sector pages** (Residential, Commercial, Industrial) and the **group-structure chart**, so legacy content that had nowhere to live now has a home.
3. Completed the production-readiness layer: per-page metadata, canonical URLs, an Open Graph sharing card, and a generated sitemap and robots file controlled by one flag.
4. Made the group-structure chart deliberately heavier, since a structure diagram rendered as delicate linework fails at its one job.
5. Rebuilt the "explore by sector" block as an index table, fixing a self-referential link and the wide void between each sector name and its description.
6. Initialised Git and pushed the whole project to GitHub.

Current state:

- 13 generated static routes
- 28 assets, 20 MB
- 104 route/width combinations audited with zero critical findings
- Every page has a unique description, canonical link and Open Graph tags
- 2 commits on `main`, clean tree, in sync with the remote
- No unverified legacy claim is presented as approved fact

## 2. Non-negotiable rules

These came from the client and still govern every change:

1. Never invent project approvals, dates, metrics, testimonials, awards, partners or completed construction claims.
2. Label renderings, concepts and planning-stage material honestly, in the interface itself.
3. Do not change the color theme, typography or design language. The palette, type system and editorial grid are settled.
4. Do not promote unverified legacy claims into confident marketing copy.
5. Respect media licenses. If rights are uncertain, flag it rather than shipping it.
6. When a legacy source is corrected, disclose the correction on the page rather than applying it silently.

## 3. Navigation

The seven primary destinations mirror the previous site exactly:

| Nav item | Route |
| --- | --- |
| Home | `/` |
| Projects | `/projects/` |
| Residential | `/residential/` |
| Commercial | `/commercial/` |
| Industrial | `/industrial/` |
| Community | `/community/` |
| Contact | `/contact/` |

Supporting pages reachable from the footer and elsewhere: `/about/` and `/privacy/`, plus the four project detail pages.

The word "Portfolio" was removed from all navigation, headings and body copy. It survives only in CSS class names (`portfolio-register`, `portfolio_opportunities`) and in `projects.json`'s historical notes, which is harmless.

## 4. Routes

| Route | Purpose |
| --- | --- |
| `/` | Group-level homepage |
| `/projects/` | Project list, group-structure chart, asset classes, earlier-name register, opportunity register |
| `/residential/` | Residential types, approach, pipeline, the eight named communities |
| `/commercial/` | Commercial formats, approach, six commercial opportunities |
| `/industrial/` | Industrial formats, approach, five industrial and storage opportunities |
| `/community/` | Community themes, earlier programme record, future commitments |
| `/contact/` | Enquiries |
| `/about/` | Positioning, sectors, values, leadership |
| `/privacy/` | Website privacy |
| `/projects/lifestyle-enclave/` | Project detail |
| `/projects/two-river-mineville/` | Project detail |
| `/projects/cornwallis-park/` | Project detail |
| `/projects/residential-pipeline/` | Pipeline detail |

## 5. Architecture

Static site generated from Python and JSON. No framework, no production JavaScript build step.

```
generate_site.py     shared structure, nav, page sections, chart, metadata, launch flag
sector_data.py       legacy content model for the sector pages and structure branches
sector_pages.py      shared sector-page helpers and cross-links
projects.json        sourced project facts, concept detail, use groups, legacy names
dist/styles.css      component foundations
dist/experience.css  art direction, responsive layouts, motion
dist/script.js       nav, galleries, media, scroll sequences, filters, enquiry
dist/assets/         fonts, logo, images, video, OG card
asset-sources.json   asset provenance
```

`generate_site.py`, `sector_data.py` and `projects.json` are the source of truth. Never hand-edit `dist/*.html` for lasting changes. CSS and JavaScript live in `dist/` on purpose.

After any change, run:

```sh
python3 generate_site.py
```

The generator refreshes cache-busting query strings across all pages.

## 6. Running locally

```sh
python3 -m http.server 8080 --directory dist
```

Then open http://localhost:8080. A server is required; assets use root-relative paths.

Optional Vite review helper (development only):

```sh
npm ci
npm run dev
```

Verification:

```sh
python3 -m py_compile generate_site.py sector_data.py sector_pages.py
python3 -m json.tool projects.json >/dev/null
python3 -m json.tool asset-sources.json >/dev/null
node --check dist/script.js
python3 generate_site.py
```

## 7. Going live

One constant controls indexing for the whole site, in `generate_site.py`:

```python
LAUNCH = False
SITE_ORIGIN = 'https://plexus-development.criyx-ai.chatgpt.site'
```

Setting `LAUNCH = True` and pointing `SITE_ORIGIN` at the production domain, then regenerating, simultaneously switches robots meta to `index,follow,max-image-preview:large`, rewrites every canonical and sharing URL, and flips `robots.txt` to `Allow: /` with a sitemap pointer. `sitemap.xml` and `robots.txt` are generated from the same flag, so they cannot contradict the markup.

This was tested in both directions and reverted. **This is the one remaining step before a real launch, and it is a client decision, not a code change.**

## 8. Open items for the client

These need a human answer. Do not guess them.

1. **Office hours** on the contact page came from the previous site and must be reconfirmed.
2. **Greenwood vs Lucasville.** Legacy material describes Greenwood as a commercial project in Lucasville. Unresolved, and stated as such on the commercial page.
3. **Plexus Storage.** Described as a platform across multiple Nova Scotia locations. Ownership, operating relationship, facility names and addresses were never published.
4. **CHSDF contribution details.** Dates, amounts, events and photographs were never published.
5. **Residential pipeline names.** Scope, location, ownership and status for all six named communities plus the eight structure-graphic names.
6. **Concept media rights** for `wilmot-concept.webp` and `lucasville-concept.webp`. Both are only used inside the labelled opportunity register.
7. **Lifestyle Enclave** pricing, availability, parking, storage and move-in timing, from the leasing team.
8. **Aggregate claims** such as 6+ projects, 1,100+ units and 500+ acres exist in older material but are deliberately unused.
9. **Production domain and launch approval** for the `LAUNCH` flag.

## 9. The group-structure chart and the sector index

### Chart

The previous site published a hierarchy image. It is rebuilt on `/projects/` as a four-branch chart, and the page discloses four corrections in its own note block:

- The source spells the commercial branch `Cornwalis`. Shown as Cornwallis.
- The Sables appears under both residential and commercial in the source and is repeated rather than merged.
- Two River, Mineville is not in the source graphic. Added because it has a full project page.
- The source places Cornwallis Park under industrial. The project page describes broader mixed-use potential, which the note records.

Each branch shows a name count (10, 04, 05, 00), a one-line summary of what it covers, and its list of names. The art direction is deliberately the heaviest on the site: 2px gold trunk and drop lines, a 9px square on the root node, 9px markers per branch, larger headers and heavier name text. Names with a detail page are links; earlier names are plain text tagged `Earlier name`.

The Clean Energy branch has no children in the source. Rather than leave a large void or invent content, that column states what is actually true: nothing was ever published, and the only appearance in published copy is wind and solar integration among the Cornwallis concept's potential uses, with a link to that record. The text lives in `sector_data.py` under the branch's `note` key.

### Sector index

The "explore by sector" block is an index table, not a list of links. A `No. / Sector / What it covers` header row plus a fixed 300px sector column keep the description and arrow in identical positions on every row. Without that header the rows read as scattered links with a wide void, which is what made the earlier version look cut out.

It also omits the page you are already on and renumbers the rest, so a reader is never offered a link back to where they are. All four hubs show exactly four destinations with no self-link. The destination list is `SECTOR_CROSS_LINKS` in `sector_pages.py`; `cross_links()` does the filtering and renumbering.

## 10. Research archive

The public capture of the previous site lives at `research/legacy-site-capture-2026-09-25/`. On this machine it is roughly 187 MB and 749 files, but **only part of it is in Git**.

Versioned, because every unverified claim on the current site traces back to it:

- All six research reports and `all-visible-text.txt`
- All 16 metadata JSON and CSV records
- All 5 capture scripts, so the binaries are reproducible
- The Cornwallis planning strategy as extracted `.txt`

Deliberately untracked, each commented in `.gitignore`:

- `assets/`, `chrome-netlogs/`, `media-originals/`, `full-page-screenshots/`, `media-contact-sheets/`
- Two contact sheets at the archive root
- `external-references/*.pdf`
- `SHA256SUMS`

The reason is twofold. Those binaries are third-party media, a Pexels film and Unsplash stock, whose redistribution rights are recorded as unconfirmed in `SOURCES.md`, and pushing them into a **public** repository is not a decision an agent should make on its own. They are also 105 MB of weight in a repository that otherwise contains one website.

Start with:

- `README.md` — archive index and methodology
- `CONTENT-AND-PROJECT-INDEX.md` — exhaustive page and project content digest
- `CLAIMS-NEEDS-CONFIRMATION.md` — conflicts, stale claims, naming issues, copy errors
- `SEO-TECHNICAL-INVENTORY.md` — SEO, hosting, schema, forms, cookies, redirects, media
- `MEDIA-INVENTORY.md` — all 43 image sources with dimensions, alt text, pages, local paths
- `MEDIA-VISUAL-NOTES.md` — visual review of every concept, logo, plan and image

**This exclusion is pending client sign-off.** If they want the full archive published, remove those lines from `.gitignore`, `git add -A`, and push. It is a normal commit, not a history rewrite.

The archive records what the public legacy site stated. It does not prove ownership, approvals, delivery status, project scope, community contributions or media rights.

## 11. Likely next steps

- Reconfirmation edits once the client answers section 8
- Copy refinement on the sector pages, chart and sector index
- Decide on the research-archive exclusion described in section 10
- Launch: set `LAUNCH = True`, point `SITE_ORIGIN` at the production domain, regenerate, deploy
- Deployment to the Sites project recorded in `.openai/hosting.json`
- Project detail pages for a commercial or industrial opportunity, if real data ever exists

## 11a. Things that look like bugs but are not

Recorded so a future session does not chase them.

- **Homepage elements flagged as overflowing.** The hero film, poster and the horizontal project journey extend past the viewport by design, inside clipping containers. Document-level horizontal overflow is zero on all 13 routes. This is the only recurring audit finding and it is expected.
- **The fixed header or skip-link appearing inside section screenshots.** An artifact of capturing beyond the viewport with `position: fixed` elements present. Confirm anything suspicious with a plain viewport capture before treating it as a layout fault.
- **The `.sector_hub` showing `overflowPx: -112`.** Content sits inside the section, not outside it. That section was never clipped; it only *looked* cut out because of the row grid.

## 12. Session mechanics

This project is a Git repository, initialised on September 26, 2026 and pushed to:

- `https://github.com/DEVuttkarsh12/new-new-plexus` (public, branch `main`)

Regenerate the HTML before committing any change to the generator, project data, CSS or JavaScript, so the committed `dist/` always matches its sources.

The research archive's captured binaries are deliberately untracked. See section 10 and `.gitignore` for the rationale and the exact list. A fresh clone contains the written reports, metadata and capture scripts but not the media; re-run the capture scripts to rebuild it.

`gh` is authenticated to two accounts. The active one must be `DEVuttkarsh12` or a push will land in the wrong place:

```sh
gh auth switch --hostname github.com --user DEVuttkarsh12
```

QA tooling lives in `/tmp/opencode/` and is disposable. It includes a full-page and viewport capture harness, a selector-based section capture, a viewport-at-position capture for checking suspected fixed-element bleed, a mobile-menu prober, a geometry probe for detecting real overflow versus optical overflow, and a route/width accessibility and layout sweep. Recreate if needed; not part of the project.
