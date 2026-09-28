# Plexus Development Group

A complete responsive website for Plexus Development Group, presented as a Halifax-based building and development group. The homepage leads with Halifax waterfront film, then brings Pavneet Singh's leadership, the group's residential, commercial and industrial building work, active construction and wider project program into view. Lifestyle Enclave remains one project within the wider group.

Start with `CHECKPOINT.md` for the current state and open client questions, then `Context.md` for the full project record. The September 28 content and layout refinement is documented in `DESIGN-REFINEMENT-2026-09-28.md`; it supersedes the older pinned project and sector layouts described below.

Source: https://github.com/DEVuttkarsh12/new-new-plexus

The site contains thirteen static routes. The seven primary destinations match the previous site's navigation:

- Homepage
- Projects
- Residential
- Commercial
- Industrial
- Community
- Contact

Plus four supporting pages:

- About Plexus
- Website privacy
- Lifestyle Enclave
- Two River, Mineville
- Cornwallis Park
- Residential pipeline

## Preview locally

```sh
python3 -m http.server 8080 --directory dist
```

Open http://localhost:8080. Assets use root-relative paths, so use a server instead of opening the HTML files directly.

Alternatively, with Node 22.12 or later:

```sh
npm ci
npm run dev
```

The Vite responsive-review helper is development-only. It provides 320, 390, 430 and 1280 px review frames plus a link that replays the opening.

## Edit the website

- `generate_site.py`: shared structure, navigation, all page sections, the group-structure chart, sector pages, metadata and the launch flag.
- `projects.json`: sourced project facts, status labels, concept detail, use groups, legacy names and galleries.
- `sector_data.py`: legacy content model for the residential, commercial and industrial pages, plus the group-structure branches.
- `sector_pages.py`: shared sector-page helpers and cross-links.
- `dist/styles.css`: shared component foundations.
- `dist/experience.css`: editorial art direction, responsive layouts and motion.
- `dist/script.js`: navigation, galleries, media playback, scroll sequences, filters and enquiry behavior.
- `dist/assets/`: self-hosted fonts, logo, images and optimized video.
- `asset-sources.json`, `SOURCES.md`, `DESIGN-NOTES.md`: source and design records.

After changing the generator, project data, CSS or JavaScript, regenerate the HTML so asset fingerprints stay current:

```sh
python3 generate_site.py
```

Production serves `dist` directly. There is no production JavaScript build step.

## Media and motion

The hero selects a 1600 x 900 Halifax film on desktop and a 720 x 1280 crop on phones. Both are muted H.264 files with faststart metadata. A local poster remains visible until the first video frame plays. Playback pauses offscreen, in hidden tabs and behind navigation or dialogs.

The opening is intentionally calm: the Plexus signature fades in, holds briefly, then dissolves before the hero content appears. It runs once per edition during a browser session. Reduced-motion preferences and the footer motion switch disable decorative animation, video autoplay and pinned scrolling.

Wide screens use two immersive passages: a four-chapter development mandate and a horizontal three-project portfolio. Phones return both sections to natural reading and native horizontal browsing.

Lifestyle Enclave's full construction overview remains on its project detail page. A labelled construction aerial also appears in the homepage's selected projects passage, alongside planned and concept-stage work, to make the group's building focus tangible without making the whole site read as a single-project leasing page.

## Enquiries and hosting

The contact form validates input and prepares an email draft in the visitor's chosen email app. It does not send through a server-side form service.

## Going live

One constant controls indexing for the whole site. In `generate_site.py`:

```python
LAUNCH = False                                   # True at public launch
SITE_ORIGIN = 'https://plexus-development.criyx-ai.chatgpt.site'
```

Setting `LAUNCH = True` and pointing `SITE_ORIGIN` at the production domain, then regenerating, simultaneously:

- switches every page from `noindex,nofollow` to `index,follow,max-image-preview:large`
- rewrites every canonical URL, Open Graph URL and Twitter URL
- flips `robots.txt` from `Disallow: /` to `Allow: /` with a sitemap pointer

`sitemap.xml` and `robots.txt` are generated from the same flag, so they can never contradict the page markup. Every page also carries its own description, canonical link, Open Graph tags and a shared 1200 x 630 sharing card at `assets/og-image.png`.

`.openai/hosting.json` identifies the existing Sites project and should remain with the repository. This downloadable source omits installed dependencies, Git history and temporary review files.

## Information architecture and legacy coverage

The site carries forward the recoverable information from the previous site without promoting unverified claims.

**Projects** lists the four projects with detail pages, then rebuilds the legacy group-structure graphic as a readable chart covering residential, commercial, industrial and the clean-energy initiative. An asset-class strip, the earlier-name register and the opportunity register follow.

**Residential**, **Commercial** and **Industrial** each carry the full record for that branch: the development types the previous site named, the approach language, and every opportunity including those that never had a project page. Names that appeared only as logos or in the structure graphic are listed as earlier names, separated from projects that have real pages.

**Community** consolidates the earlier themes and records that programme details were never published.

Every concept-stage value is labelled in the interface, and every correction applied to a legacy source graphic is disclosed in an on-page note. Nothing asserts approval, ownership, availability or delivery dates the archive does not support.

## Legacy-site research archive

The complete public capture of the previous `plexusdevelopmentgroup.ca` site is stored in `research/legacy-site-capture-2026-09-25/`. It includes every sitemap route, raw and cleaned text, page metadata, forms, links, responsive assets, source images, concept-plan notes, the full hero film, rendered DOM, runtime network records, and checksums.

See `research/legacy-site-capture-2026-09-25/README.md` to navigate the archive. Treat its project claims as legacy research requiring confirmation rather than automatically approved current copy.
