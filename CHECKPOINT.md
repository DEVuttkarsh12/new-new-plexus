# Plexus website checkpoint

Last updated September 29, 2026, after the centred hero and visual polish.
Read this file first; `Context.md` contains the historical project record.

## Current state

The client requested a simpler, more professional development-group and builder website based on the live legacy site's content and structure. This supersedes the earlier direction to retain the large pinned project and sector sequences.

The September 29 follow-up centres the homepage hero headline, supporting text and project link as one composition. The smaller-image direction and simplified pages remain in place. Shared typography, project labels, hover and focus treatments, and partner-column spacing have received a restrained polish in `dist/refinement.css`. This follow-up is complete and included in the current revision; website deployment remains a separate action.

The redesign is applied across all 13 routes and generated into `dist/`. The preview is served at http://127.0.0.1:8080/ when the local server is running. The client has authorized committing and pushing this revision to GitHub on `main` at `DEVuttkarsh12/new-new-plexus`. Website deployment has not been requested.

## Completed work

- Recovered the previous checkpoint, project data, asset provenance and exhaustive September 25 legacy archive.
- Refetched every public page through the sitemap and internal navigation. All seven canonical page HTML hashes exactly match the previous capture.
- Preserved full source text, headings, links, form definitions and resource references in `research/legacy-site-refresh-2026-09-28/`.
- Simplified the homepage to introduction, services, selected projects, development commitments and partner priorities.
- Rebuilt Projects around compact project cards, optional filters, the group structure, asset classes and the original location map.
- Removed repeated name registers, oversized concept passages, the repeated eleven-question FAQ and unused page-generation helpers.
- Reduced heading sizes, spacing, image heights and project-gallery dimensions across the site.
- Kept detailed project information inside native disclosures and retained sourced facts, features, labels and enquiry links.
- Restored residential brand artwork, Plexus Storage artwork, the original hierarchy and location map. Community moments and longer intentions are available inside disclosures.
- Preserved the full original company statement on About through `legacy_content.json`.
- Repaired the shared footer wordmark with container-relative typography and a normal line box. Contact details and all seven navigation destinations remain accessible.
- Corrected the homepage title layout so positioning is independent of its parallax transform.
- Centred the hero composition on desktop, tablet and phones, with symmetric headline padding, balanced supporting copy and a centre-weighted video overlay.
- Added fine brass rules around the desktop hero overline, consistent service-link arrows, subtle partner dividers and clearer disclosure focus states.
- Corrected project-status and project-scale contrast on the dark homepage section; retained all existing image assets and compact image heights.

## Architecture and editing

Source of truth: `generate_site.py`, `projects.json`, `sector_data.py`, `sector_pages.py`, `legacy_content.json`.

CSS and JavaScript intentionally live in `dist/`: `styles.css` supplies foundations, `experience.css` supplies existing brand styling, and `refinement.css` supplies the final compact presentation and responsive rules. `script.js` provides navigation, filters, image previews, motion preferences and the enquiry draft.

Regenerate after changing source, styles or scripts:

```sh
python3 generate_site.py
```

Local preview:

```sh
python3 -m http.server 8080 --bind 127.0.0.1 --directory dist
```

## Durable constraints

Preserve forest, paper and brass, the Halifax hero film, the Plexus parent-group identity, seven primary navigation destinations, honest concept labels and sourced project facts. Do not invent approvals, ownership, operating facilities, testimonials or delivery milestones.

Retain the complete September 25 archive. The September 28 refresh validates that archive; it does not replace its original media and browser captures.

## Remaining external decisions

Production launch settings remain `LAUNCH = False` and the existing review-site origin. A production-domain launch remains a separate decision. GitHub synchronization is authorized; DNS, website deployment and contact-form submission are outside this push.

Legacy questions about Greenwood/Lucasville naming, Plexus Storage locations, CHSDF programme details, move-in timing and project approvals remain documented in `Context.md` and the research claims register. Full text and source imagery must not be treated as independent proof of those claims.

## Validation and next resume

Completed browser review: 13 routes at 360, 390, 768 and 1440 px, 52 combinations with zero detected overflow, footer clipping, missing images or browser errors. Navigation, project filters and reset, image previews, native disclosures, motion preferences and contact fields passed their interaction checks. Syntax and internal-link checks also passed. No contact enquiry was submitted.

September 29 review: all 13 routes at 320, 390, 768, 1440 and 1920 px (65 combinations) passed with no horizontal overflow, clipped footer wordmarks, missing images or browser errors. The hero headline, description and link are horizontally centred within 0.02 px at every tested width, with no title clipping or overlap with hero metadata. Selected homepage project images remain at or below 230 px. Mobile navigation, Escape, homepage disclosures, the hero-to-projects link, project search and reset passed. Final desktop and phone screenshots were inspected, including the project and partner sections. Internal asset/link checks, JavaScript syntax and `git diff --check` passed. The disposable audit and screenshots live in `/tmp/plexus-browser/` and `/tmp/plexus-*.png`.

See `DESIGN-REFINEMENT-2026-09-28.md` and `research/legacy-site-refresh-2026-09-28/` for source mappings and the final review record. Disposable browser tooling and screenshots live under `/tmp/plexus-review/`.

Next action: review the local redesign with the client, apply any specific feedback, and deploy the existing review build if requested. Do not resume the retired full-screen project sequences from the earlier checkpoint.
