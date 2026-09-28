# Content and layout refinement

The September 28 direction is a simple, contemporary website for a development group with a builder's focus. Retain the legacy site's information and sector hierarchy, make projects easier to scan, reduce repetition and fix the footer on small screens.

## Source review

The existing September 25 crawl is exhaustive: seven pages, exact text, project and image information, 43 original image sources, a hierarchy graphic, location map, media, runtime resources and rendered screenshots.

A fresh sitemap and internal-link crawl confirms that all seven canonical public pages match that capture exactly. The current source and comparison records are saved in `research/legacy-site-refresh-2026-09-28/`. The full original statement is also stored in `legacy_content.json` for the About disclosure.

## How the original information is presented

| Legacy information | Modern presentation |
| --- | --- |
| Seven navigation links | Same seven destinations in desktop and mobile navigation |
| Welcome and company mission | Concise home introduction; full company statement available on About |
| Residential, commercial, industrial services | Three simple service rows linked to dedicated sectors |
| Projects, locations, stages and concepts | Compact cards linked to complete project records |
| Group structure graphic | Responsive semantic hierarchy with the original graphic available to enlarge |
| All names in the hierarchy | Retained in the chart; source corrections remain disclosed |
| Asset classes | Compact list on Projects |
| Nova Scotia project location map | Original map, contained thumbnail and image preview; source limitations accessible |
| Residential community logos | Restored logo gallery; named communities retain status qualifications |
| Wilmot, Greenwood and Lucasville | Commercial summaries with contained concepts and expandable detail |
| Plexus Storage and industrial names | Original Storage artwork and concise industrial records |
| Sustainability, impact and priorities | Home commitments in three native disclosures |
| Partner priorities | Three concise partner columns |
| Community priorities, CHSDF and intentions | Compact Community page, source intentions and moments in disclosures |
| Detailed Mineville and Cornwallis programme | Retained facts, proposed features, use groups and full expandable descriptions |
| Contact details and hours | Retained contact page and shared footer |
| Long original text and source errors | Preserved exactly in the research archive |

## Layout decisions

- The homepage has one service overview and one project selection. The previous pinned passages and duplicate listing sections are retired.
- Projects has a simple page index, four compact cards, optional filters, the hierarchy, asset classes, map and sector links.
- Standard project-card images are capped at 275 px on desktop and 210 px on phones. Selected home images are smaller. Sector concept images use `object-fit: contain` so embedded information remains visible.
- Interior headings use a compact scale. Section spacing follows the content rather than occupying whole viewports.
- Native disclosures preserve longer information without placing every paragraph in the initial page flow.
- The footer wordmark uses the width of its container and a normal line box. Its letters stay within the available width, including phone layouts.
- Hero positioning is independent of its small vertical parallax transform. The Halifax video and the existing opening sequence remain.

## Implementation

`generate_site.py` composes the pages. `projects.json` and `sector_data.py` retain the sourced facts. `legacy_content.json` holds exact company prose and community intentions. `dist/refinement.css` is the final responsive layer over the established brand styles. Retired page-generation sections and repeated FAQs were removed.

Newly restored images are optimized WebP copies of the original Plexus artwork, reference graphics and community photographs. Their exact source URLs and limitations are recorded in `asset-sources.json`.

## Review

Completed results are saved in `research/legacy-site-refresh-2026-09-28/responsive-audit.json` and `interaction-audit.json`.

- All 13 routes reviewed at 360, 390, 768 and 1440 px: 52 combinations, zero detected horizontal overflow, clipped footer wordmarks, missing images or browser errors. The homepage title also fits within the hero at each width.
- Search, location and stage filters, reset and empty states passed. Mobile navigation, Escape-to-close, image-preview open/close, chart and project disclosures, and motion preferences passed.
- Contact subjects populate from enquiry links, required fields reject an empty form, and the published email destination is correct. No enquiry was sent.
- Python and JavaScript syntax checks passed. All generated internal destinations and assets resolve, and `git diff --check` passes.
- The Projects page's total source text, including closed disclosures, is reduced from 1,441 to 576 words. Detailed records remain on their project and sector pages, and full original wording remains in the source archive.

The work remains local and reviewable. Production indexing and the existing review deployment have not been changed.
