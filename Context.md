# Plexus Development Group Website Context

> Start here. This file is the handoff record for any designer, developer, or coding agent continuing the Plexus Development Group website.

> For a fast resume, read `CHECKPOINT.md` first. It captures the current state, the most recent work, the open client questions and the likely next steps. This file remains the full durable record.

Last updated: September 25, 2026  
Project status: Implemented, responsive, published as a private review build, and packaged for handoff  
Session note: Legacy content integration is complete. Ten routes, all verified. Nothing mid-edit, nothing blocked.

## 1. Project mission

Build a premium, cinematic website for Plexus Development Group that feels commissioned by a high-end real estate and architecture studio. The experience should establish trust, scale, and local relevance without looking like a generic website builder template, a technology startup, or a single-apartment sales page.

Plexus must be presented as the parent development platform. Lifestyle Enclave is one project within the portfolio, not the identity of the company.

The core positioning currently used throughout the site is:

- Development
- Investment
- Land
- Halifax and Nova Scotia focus
- A broader Atlantic Canada outlook
- Long-term value across residential, commercial, industrial, logistics, and strategic land opportunities

The hero statement is: **Building tomorrow's Nova Scotia.**

## 2. Current status

The current version is a static, multi-page website generated from Python and JSON. It has a full-screen Halifax waterfront film hero, a calm opening sequence, two immersive wide-screen scroll passages, a portfolio browser, individual project pages, leadership content, forms, galleries, accessibility support, and mobile fallbacks.

Current live review URL:

- https://plexus-development.criyx-ai.chatgpt.site

Sites project ID:

- `appgprj_6aa1021dc0108191bb99ac48783f2da6`

Current Git HEAD when this handoff was written:

- `5ba8ff076c4978054d41cecaccbb7513a9dd7acf`
- `Refine hero video presentation`

The review build is intentionally marked `noindex,nofollow`. Do not remove that directive until the final production-domain launch is approved.

## 3. Non-negotiable product direction

Preserve these decisions unless the client explicitly changes them:

1. Plexus is the primary brand and parent development group.
2. Lifestyle Enclave must remain a small, clearly contained project story.
3. The homepage must not read like an apartment leasing website.
4. The hero must retain its moving Halifax drone and waterfront footage.
5. There must be no hero-specific play or pause button.
6. The hero must remain edge-to-edge. Do not place its main content inside a floating card or rounded container.
7. The opening loader must feel calm, deliberate, and premium rather than fast or flashy.
8. Hero content should appear only after the opening sequence finishes, using a quiet reveal.
9. Preserve the horizontal portfolio scroll on wide screens.
10. Preserve the pinned four-chapter `What we build` passage on wide screens.
11. Mobile and reduced-motion layouts must return these complex passages to natural document flow.
12. Avoid a technology, SaaS, dashboard, or futuristic interface aesthetic.
13. Avoid the rounded-card visual language common to template builders.
14. Avoid em dashes and copy patterns that feel machine-generated.
15. Never invent project approvals, dates, metrics, testimonials, awards, partners, or completed construction claims.
16. Label renderings, concepts, and planning-stage material honestly.

## 4. Brand and design language

### Visual character

- Premium architectural editorial design
- Minimal, restrained, and high-contrast
- Film and typography carry the emotion
- Large serif display type with disciplined sans-serif support
- Generous whitespace and deliberate pacing
- Square and architectural geometry rather than soft SaaS cards
- Fine rules, small labels, editorial numbering, and location metadata
- Alternating mineral-white and deep-forest sections
- Motion that is cinematic but never hectic

### Core palette

- Deep forest: approximately `#142820`
- Dark theme and browser color: `#132822`
- Warm paper: approximately `#f5f5f0`
- Restrained brass and muted gold: approximately `#c9b780` to `#d3c591`
- Neutral charcoal overlays over film

The hero originally became too green. The current treatment intentionally reduces that tint:

- Desktop video filter: `saturate(.9) contrast(1.02) brightness(.92)`
- Mobile video filter: `saturate(.88) contrast(1.02) brightness(.86)`
- Overlays use neutral charcoal gradients rather than a heavy green wash

### Typography

- Display serif: local `serif.ttf` and `serif-italic.ttf`
- Sans-serif system: local Switzer weights with Arial fallback
- Supporting assets also include Manrope and Special Gothic
- Keep headlines concise enough to preserve their architectural rhythm

### Logo

The original Plexus logo is a square artwork. The interface presents it inside a circular frame with a fine border and restrained shadow so it feels intentional in the navigation. Do not redraw or distort the underlying logo.

## 5. Information architecture

The production directory contains thirteen routes. The seven primary destinations deliberately mirror the previous site's navigation.

| Route | Purpose |
| --- | --- |
| `/` | Group-level homepage |
| `/projects/` | Project list, group-structure chart, asset classes, earlier-name register, opportunity register |
| `/residential/` | Residential development types, approach, pipeline and the named residential communities |
| `/commercial/` | Commercial formats, approach and the full commercial and mixed-use record |
| `/industrial/` | Industrial formats, approach and the industrial, storage and logistics record |
| `/community/` | Community themes, earlier programme record, future commitments |
| `/contact/` | Land, investment, partnership, and general enquiries |
| `/about/` | Company positioning, sectors, values, leadership |
| `/privacy/` | Website privacy explanation |
| `/projects/lifestyle-enclave/` | Lifestyle Enclave detail page |
| `/projects/two-river-mineville/` | Two River, Mineville detail page |
| `/projects/cornwallis-park/` | Cornwallis Park detail page |
| `/projects/residential-pipeline/` | Wider residential pipeline detail page |

`robots.txt` and `sitemap.xml` are generated alongside the pages. A single `LAUNCH` constant in `generate_site.py` switches indexing, canonical URLs, sharing URLs and the robots directive together, so they can never disagree.

## 6. Homepage experience

The homepage is intentionally a long-form group story. Its current sequence is:

1. Calm Plexus opening signature
2. Full-screen Halifax waterfront video hero
3. Platform introduction and positioning
4. Pinned `What we build` four-sector sequence
5. Broader Plexus platform and scope
6. Horizontal selected-opportunities journey
7. Development approach and long-view principles
8. Complete portfolio grid
9. Pavneet Singh development leadership
10. Capital partner, broker and landowner, and community audiences
11. FAQ
12. Group-level call to action and footer

The hero currently uses:

- Kicker: `DEVELOPMENT · INVESTMENT · LAND`
- Headline: `Building tomorrow's Nova Scotia.`
- Halifax waterfront footage rather than Lifestyle Enclave construction footage
- A restrained portfolio link rather than a `Watch Film` button
- A local poster frame visible before the first video frame is ready

## 7. Motion and interaction system

### Opening

The opening sequence fades in the Plexus signature, holds briefly, and dissolves slowly. It runs once per edition during a browser session using session storage. The hero content then fades into place.

Do not shorten it into a quick logo flash. The client specifically rejected a loader that felt too fast and flashy.

### Hero film

- Autoplay
- Muted
- Looping
- `playsinline` on mobile
- Separate desktop and portrait mobile renditions
- Local poster fallback
- JavaScript playback recovery when the browser allows it
- Pauses when offscreen, when the tab is hidden, and when navigation or dialogs obscure the page
- No visible hero play or pause control

The global footer motion preference remains. It pauses decorative motion across the site and is not a hero-only media control.

### Wide-screen sequences

The `What we build` section is a pinned four-chapter experience:

1. Residential communities
2. Commercial and mixed use
3. Industrial and logistics
4. Land and future growth

The selected-opportunities section uses a retained horizontal scroll through portfolio stories.

### Reduced motion and phones

`prefers-reduced-motion` and the site's motion setting disable decorative animation, video autoplay, and pinned scrolling. Mobile renders the four chapters in natural order and keeps portfolio browsing touch-friendly.

### Galleries and dialogs

- Gallery images open in a native dialog
- Escape closes the dialog
- Arrow navigation is supported
- Every thumbnail maps to its own full image and caption
- Lifestyle Enclave has a project-only construction film dialog
- The group-level hero never opens that film

## 8. Responsive behavior

The site was deliberately reviewed at:

- 320 px
- 390 px
- 430 px
- 1280 px
- 1920 px

The 375 px phone target is part of the design intent even though the helper currently exposes 320, 390, and 430 px presets.

Important behavior:

- No document-level horizontal overflow
- Phone navigation opens and closes correctly
- Hero switches to the portrait poster and video source
- Pinned sequences become readable static sections on small screens
- Horizontal portfolio passage remains natively swipeable
- Type scales and line breaks are adjusted for narrow screens
- Gallery and dialog controls remain keyboard and touch accessible

### Wide-screen collision fix

A prior 1920 x 850 review revealed overlapping copy in the pinned `What we build` section. The cause was a second large-screen centering offset being applied inside an already centered 1440 px frame.

The fix was:

- Remove the duplicated `@media (min-width: 1441px)` offset
- Add `max-width: 560px` to `.mandate-pinned .mandate-scenes`
- Keep only one active chapter at a time on desktop

Do not reintroduce another viewport-centering transform on that scene column.

## 9. Content and factual inventory

### Company

- Name: Plexus Development Group
- Base: Halifax, Nova Scotia
- Positioning: Development, investment, and land acquisition platform
- Current geographic language: Nova Scotia focus with a broader Atlantic Canada outlook

### Contact

- Email: `info@plexusdevelopmentgroup.ca`
- Phone: `+1 902 809 9399`
- Address: `3845 Joseph Howe Drive, Suite 100, Halifax, Nova Scotia`

### Portfolio represented in this build

#### Lifestyle Enclave

- Location: Upper Hammonds Plains
- Sector: Residential
- Stage: Under construction
- Scale: 102 homes
- Unit language: One-bedroom plus den and two-bedroom plus den
- Planned shared spaces: Fitness centre, resident lounge, and community room
- External project site: https://lifestyleenclave.ca/

All renderings and undated construction footage are labelled. Availability, parking, storage, tours, and move-in timing must be confirmed with the leasing team.

#### Two River, Mineville

- Also introduced in older material as Notting Hill
- Location: Mineville, Nova Scotia
- Stage: Planned
- Land area: 73 acres
- Concept: 54 fourplex lots and 216 planned residential units
- Proposed features remain subject to change

#### Cornwallis Park

- Location: Annapolis County, Nova Scotia
- Stage: Planning review
- Land area: 240 acres
- Long-term residential, commercial, and complementary uses are concepts subject to planning and zoning approvals

#### Residential pipeline

Names currently included:

- The Sables
- The Parks of Cole Harbour
- Crownvale
- Sarnaaz Valley
- The Amiora
- The Chamelias

These are presented as future opportunities without invented scopes or delivery dates.

### Leadership

- Pavneet Singh
- Current safe role used by the website: `Real Estate Developer · Halifax, Nova Scotia`
- Leadership copy connects his real estate advisory, investment, land, and local-market perspective to Plexus

Earlier supporting material has used stronger titles and aggregate portfolio claims, including founder or director language, 6+ projects, 1,100+ units or capacity, and 500+ acres. Those figures are not currently relied upon in the website interface. Revalidate them directly with Plexus before adding them to public marketing copy.

## 10. Asset inventory and provenance

All production assets are stored locally in `dist/assets/`.

### Brand and fonts

- `logo.png`: Original Plexus artwork, presented in a circular UI treatment
- `serif.ttf`, `serif-italic.ttf`: Editorial display family
- `Switzer-400.woff2`, `Switzer-500.woff2`, `Switzer-600.woff2`, `Switzer-700.woff2`
- `manrope-400.ttf`, `manrope-600.ttf`
- `SpecialGothic-700-Latin.woff2`

Font license notes are in `licenses/`.

### Group-level Halifax media

- `halifax-waterfront.mp4`: Optimized 1600 x 900 desktop film, approximately 7.7 MB
- `halifax-waterfront-mobile.mp4`: Optimized 720 x 1280 phone crop, approximately 3.3 MB
- `halifax-waterfront.webp`: Desktop poster
- `halifax-waterfront-mobile.webp`: Phone poster

The film is a text-free Halifax waterfront establishing shot published by MaxMedyk under the Pixabay Content License. It establishes place and scale. It is not evidence of a Plexus-owned site.

### Portfolio media

- `lifestyle-front.webp`: Architectural rendering
- `lifestyle-back.webp`: Architectural rendering
- `lifestyle-arrival.webp`: Architectural rendering
- `lifestyle-lobby.webp`: Architectural rendering
- `lifestyle-drone.webp`: Genuine project construction aerial
- `plexus-overview.mp4`: Optimized Lifestyle Enclave construction film, used only on that project page
- `mineville.webp`: Concept visual
- `cornwallis.webp`: Concept plan
- `community.webp`: General Plexus portfolio concept
- `pavneet-singh.webp`: Official portrait crop with the source graphic's promotional text removed from view
- `hero-sky.png`: Decorative generated sky background retained as a project asset

The connected `Pavneet-Singh-media` Drive folder was reviewed earlier. Most of its imagery is Lifestyle Enclave apartment, amenity, construction, and marketing material, so it was deliberately confined to the Lifestyle Enclave context instead of defining the Plexus parent brand.

Do not present architectural renderings or concept plans as photography of completed places.

## 11. Source and reference inventory

### Primary content and asset sources

- Original Plexus website: https://plexusdevelopmentgroup.ca/
- Original project index: https://plexusdevelopmentgroup.ca/nova-scotia-construction-projects
- Residential context: https://plexusdevelopmentgroup.ca/residential-construction
- Commercial context: https://plexusdevelopmentgroup.ca/commercial-construction
- Industrial context: https://plexusdevelopmentgroup.ca/industrial-construction
- Community context: https://plexusdevelopmentgroup.ca/community
- Lifestyle Enclave: https://lifestyleenclave.ca/
- Pavneet Singh: https://realtorpavneetsingh.ca/
- Halifax film source page: https://pixabay.com/videos/harbour-building-port-ocean-harbor-48067/
- Halifax film publisher: MaxMedyk
- Halifax film license: Pixabay Content License

Exact source URLs and production mappings are recorded in `asset-sources.json` and `SOURCES.md`.

### User-supplied visual references

- Homy Framer template reference: https://homy.framer.media/
- Framer real-estate template library: https://www.framer.com/marketplace/search/?q=real+estate

The user asked for the quality, composition, and immersive feeling of the references, not for paid template code or assets to be copied. No Framer template code is included in this project.

### Premium agency and property references researched

- Vide Infra, Springs: https://videinfra.com/work/springs?expertise=8
- Vide Infra, Silver Pinewood Residences: https://videinfra.com/work/silver-pinewood-residences?expertise=8
- Vide Infra, Likova: https://videinfra.com/work/likova
- Locomotive, Désourdy: https://locomotive.ca/en/work/desourdy
- Locomotive, Populous: https://locomotive.ca/en/work/populous
- Aman Beverly Hills: https://www.aman.com/aman-beverly-hills
- Chelsea Barracks: https://www.chelseabarracks.com/

These references informed film pacing, typographic scale, editorial restraint, spatial rhythm, and the relationship between architecture and motion. Nothing was copied verbatim.

### Feedback references

Client and user screenshots also guided the work:

- A dead `03 / OUR EXPERTISE +` spacer was identified and removed
- Client feedback requested a moving video and a stronger `wow` experience
- A wide-screen screenshot exposed the mandate-section text collision that was fixed

## 12. Architecture and source of truth

### Project files

- `generate_site.py`: Generates every HTML route and shared structure
- `projects.json`: Portfolio facts, stages, galleries, notes, and features
- `dist/styles.css`: Baseline components and shared styles
- `dist/experience.css`: Premium art direction, advanced layouts, motion, and responsive rules
- `dist/script.js`: Loader, video behavior, reveals, pinned scenes, horizontal journey, galleries, filters, navigation, and forms
- `dist/assets/`: All local fonts, images, posters, and video
- `vite.config.mjs`: Local dev server plus responsive-review helper
- `package.json`: Minimal Vite development dependency
- `.openai/hosting.json`: Sites static-hosting configuration and project identity
- `README.md`: Concise operational overview
- `DESIGN-NOTES.md`: Current design rationale and validation record
- `SOURCES.md`: Human-readable source and provenance notes
- `asset-sources.json`: Asset-level source map
- `licenses/`: Font and source license records

### Legacy-site research capture

A comprehensive public archive of the previous Hostinger/Zyro site is stored at:

- `research/legacy-site-capture-2026-09-25/`

The capture was completed on September 25, 2026 and includes all seven sitemap routes, original HTML, clean page text, parsed metadata, internal and external links, responsive resources, 43 deduplicated image sources, the full Pexels hero film, rendered DOM, full-page desktop screenshots, browser network logs, runtime JavaScript, media contact sheets, and SHA-256 checksums.

Start with these files when researching legacy copy or media:

- `research/legacy-site-capture-2026-09-25/README.md`
- `research/legacy-site-capture-2026-09-25/CONTENT-AND-PROJECT-INDEX.md`
- `research/legacy-site-capture-2026-09-25/CLAIMS-NEEDS-CONFIRMATION.md`
- `research/legacy-site-capture-2026-09-25/SEO-TECHNICAL-INVENTORY.md`
- `research/legacy-site-capture-2026-09-25/MEDIA-INVENTORY.md`
- `research/legacy-site-capture-2026-09-25/MEDIA-VISUAL-NOTES.md`

Important capture findings that remain research leads rather than approved current claims:

- The legacy projects page used both `Two River Subdivision, Mineville` and `Notting Hill`.
- The Cornwallis concept image adds `121 Normandy Road`, PID `05268909`, and a detailed mixed-use plan. An official Cornwallis Park planning strategy archived alongside the capture is effective March 27, 2025 and amended June 8, 2026, so the legacy phrase `zoning under review` requires revalidation.
- The legacy residential page says Lifestyle Enclave was available from August 2026, while the current project site checked during the capture says planned move-in beginning October 2026.
- The Wilmot, Greenwood, and Lucasville commercial sections conflict internally and require client clarification.
- Legacy-only or graphic-only names include Novabella Retirement Homes, The Aralias, The Evangeline, and Clean Energy Initiative.
- The old site used functioning Hostinger-hosted forms. This is historical implementation context only; the current revamped contact form intentionally prepares an email draft.
- The old site was indexable, had generic social links, empty social-image metadata, and no dedicated privacy route. Do not copy those technical decisions into the revamped site.

The archive records what the public legacy site stated. It does not independently prove ownership, approvals, delivery status, project scope, community contributions, or commercial media rights. Preserve the existing rule against publishing unverified legacy claims.

### Legacy information carried into the interface

Recoverable legacy information is published in a way that preserves the record without presenting it as approved fact.

**Group structure.** The previous site published a hierarchy graphic. It is rebuilt on `/projects/` as a readable chart with the same four branches and the same names. Corrections are disclosed on the page rather than applied silently: the source's `Cornwalis` is shown as Cornwallis, The Sables is repeated in both branches because the source did, Two River is added because it has a full project page, and Cornwallis Park stays under industrial while the note records that the project page describes broader mixed-use potential.

**Sector pages.** `/residential/`, `/commercial/` and `/industrial/` each carry the development types the previous site named, the approach language, and every opportunity in that branch, including names that never had a project page. All content comes from `sector_data.py`, which is sourced entirely from the capture.

**Project detail.** Lifestyle Enclave uses residence mix, approximate areas, amenity detail and the October 2026 planned move-in from the current first-party project site. Two River exposes the concept plan's density, zoning, lot sizes, home dimensions and amenity list as concept values and swaps the confirmation checkmark for a neutral marker. Cornwallis Park adds the concept address, PID, setting, access and grouped residential, commercial and landscape possibilities alongside the archived planning-strategy dates.

**Residential pipeline.** Keeps the six named communities and adds the eight residential names from the structure graphic in a clearly separated earlier-names block. The legacy `several hundred units` aggregate is deliberately not repeated.

**Opportunity register.** Presents Wilmot and Lucasville with surviving legacy concept visuals, and Greenwood and Plexus Storage in a qualified band. Both name the source conflicts. The Wilmot image has its source typo band cropped out.

**Community.** Consolidates the earlier themes and records that CHSDF contribution details and financial-education programme details were never published.

**Contact.** Office hours are shown as previously published and should be reconfirmed before launch.

**Asset classes and map.** The legacy projects page's asset-class list is carried. The legacy Nova Scotia map is described rather than reproduced, because it had no legend tying markers to projects.

Any of these values can be removed or corrected in `projects.json`, `sector_data.py` and `generate_site.py` without touching the design system.

### Editing rules

`generate_site.py` and `projects.json` are the source of truth for generated page markup and content. Do not manually edit generated `dist/*.html` files for lasting changes.

The CSS and JavaScript source currently lives directly in `dist/`. This is intentional. Production serves `dist` without a JavaScript build step.

After changing the generator, project data, CSS, or JavaScript, always run:

```sh
python3 generate_site.py
```

The generator refreshes cache-busting query strings in all generated pages.

Do not overwrite the `project_id` in `.openai/hosting.json`.

## 13. Development and validation commands

Install dependencies:

```sh
npm ci
```

Regenerate the site:

```sh
python3 generate_site.py
```

Local static preview:

```sh
python3 -m http.server 8080 --directory dist
```

Vite development preview:

```sh
npm run dev
```

The Vite helper exposes `/__qa` only during development. It provides 320, 390, 430, 1280, and 1920 px review frames and a link that replays the opening animation.

In a Sites managed environment, use the official supervised preview command described by the current Sites workflow rather than creating a custom production server.

Useful checks:

```sh
node --check dist/script.js
node --check vite.config.mjs
git diff --check
```

Before a substantial release, review every route, keyboard navigation, dialogs, filters, phone menu, motion preference, reduced-motion mode, and video poster fallback.

## 14. Important fixes already completed

### Logo treatment

The raw square logo originally looked awkward in the navigation. It now sits inside an intentional circular treatment.

### Hero redesigns

The first hero was too sparse, then later became too technical. It was rebuilt as a full-screen editorial real-estate hero with premium typography and film. The container treatment and `Watch Film` button were removed.

### Loader refinement

The opening was slowed and changed from a flashy slide into a quiet dissolve. Content enters after the loader completes.

### Parent-brand repositioning

The earlier homepage overused Lifestyle Enclave imagery and felt like an apartment website. It was reorganized around the Plexus platform, four sectors, multiple projects, long-term land strategy, and development leadership. Halifax footage replaced Lifestyle Enclave footage in the group hero.

### Green tint refinement

The hero's strong forest overlay was softened to a neutral charcoal treatment while preserving text contrast.

### Gallery mapping

A smaller hero/gallery image previously opened the same garden image as the larger image. Gallery triggers now retain their own image, title, note, and index.

### Dead section removal

The inactive `03 / OUR EXPERTISE +` interstitial shown below the first hero was removed.

### Wide-screen collision

The pinned mandate section was corrected for 1920 x 850 screens. Its copy and scene columns no longer collide.

### Mobile fallbacks

Pinned desktop sections convert to natural reading order on phones. The hero uses a portrait media source and mobile poster. Layouts were checked without horizontal overflow.

### Video optimization

Desktop, mobile, and Lifestyle Enclave videos were optimized for practical delivery. The complete deployable site remains roughly 19 MB rather than shipping uncompressed source media.

## 15. Accessibility and usability

The current implementation includes:

- Semantic headings and landmarks
- Skip link
- Visible focus states
- Keyboard-accessible navigation and dialogs
- Escape and arrow-key gallery behavior
- Informative image alt text
- `aria-live` status feedback where appropriate
- Native dialog elements for project imagery and film
- Reduced-motion support
- User motion preference control
- Mobile navigation with expanded-state management
- Locally hosted media and fonts

Do not remove motion alternatives when adding animation. A premium experience must still work without motion.

## 16. Forms, privacy, and integrations

The contact form validates the visitor's input and opens a prepared email draft in the visitor's email application. It does not submit data to a server-side form provider.

The authored site currently includes no external tracker, advertising pixel, or third-party animation library. Hosting providers may still process technical delivery data.

Broader CRM, analytics, chatbot, booking, and attribution work has been discussed in the wider business scope, but it is not implemented in this static package. Do not claim these integrations exist until they have been built and tested.

Google Search Console verification for `plexusdevelopmentgroup.ca` has been discussed outside this package. Preserve verification and sitemap coverage during a future domain migration, but confirm the current production setup before changing DNS, meta tags, or ownership files.

## 17. Known constraints and future work

- The site remains a review build with `noindex,nofollow`
- Canonical production metadata should be finalized for the real domain before launch
- The form does not have server-side delivery, CRM routing, spam protection, or lead persistence
- Project status, unit counts, availability, and approval language should be reconfirmed with Plexus before public launch
- The Halifax film is licensed establishing footage, not a Plexus project
- Browser-frame QA is not a substitute for physical-device testing
- Accessibility should receive a final manual audit before launch
- Video autoplay can still be blocked by browser or operating-system policy, so posters must remain meaningful
- The live Sites URL is a private review destination, not the final public-domain launch
- If adding analytics, collect only what has been approved and update the privacy page

Potential future directions previously discussed, but not part of the current interface, include international investor content, family-office pathways, government partnerships, multilingual content, investment documents, an investor dashboard, and an AI investment concierge. Treat those as separate product decisions, not assumed requirements.

## 18. Next-agent checklist

Before making changes:

1. Read this file, `README.md`, `DESIGN-NOTES.md`, and `SOURCES.md`.
2. Inspect `generate_site.py`, `projects.json`, `dist/experience.css`, and `dist/script.js`.
3. Run the site and review both desktop and phone layouts.
4. Confirm whether the requested change affects group positioning, project content, or both.
5. Preserve the Halifax hero film, calm loader, horizontal portfolio, and mobile fallbacks unless the user explicitly asks otherwise.
6. Keep Plexus visually and verbally above Lifestyle Enclave in the brand hierarchy.
7. Never reintroduce a hero play or pause button.
8. Never manually patch generated HTML without updating the generator.
9. Regenerate pages after source changes.
10. Check JavaScript syntax, whitespace, every affected route, and responsive behavior.
11. Keep `noindex,nofollow` until final-launch approval.
12. Do not publish unverified facts or depict concepts as completed work.

## 19. Recent Git history

The most recent commits at handoff are:

```text
5ba8ff0 Refine hero video presentation
42349df Fix wide-screen mandate layout
f4a0e22 Optimize site video delivery
f76c2e7 Reposition Plexus as a development group
1ef2e1b Refine the drone hero with centred typography and a balanced property header
f6b42e7 Improve drone playback and expand the Plexus development story
ebdac55 Restore full-screen hero video with poster fallback and quiet playback controls
4d58ad9 Slow the brand opening and replace its slide with a quiet dissolve
8994679 Create an edge-to-edge property hero with a sequenced entrance
5db2236 Give the homepage hero a warm residential editorial composition
5e7f718 Create cinematic Plexus identity with layered architectural scroll experience
4e19787 Rebuild Plexus around HOMY reference with responsive project pages
```

Later commits supersede earlier design directions. In particular, the current version intentionally removes the hero playback control mentioned in an older commit.

## 20. Security and handoff note

This file contains no passwords, API tokens, account credentials, or private access links. The project ID and live review URL are included because they are part of the technical handoff, but deployment still requires an authorized Sites environment.

Respect all media licenses and client ownership requirements before commercial launch. If any source or usage right is uncertain, replace the asset or obtain confirmation rather than guessing.

## 21. Client direction update — September 28, 2026

The client asked for the site to read more clearly as a builder's website, while retaining its existing pages, information, project caveats, palette and premium minimal character. The homepage now places Pavneet Singh's existing portrait and leadership feature directly after the introduction and shows the labelled Lifestyle Enclave construction aerial in the selected-projects passage. The home hero remains the Halifax waterfront film, so Plexus stays the primary group brand.

Display type now uses the local Manrope family with a heavier heading weight; Switzer remains the supporting typeface. Project statuses, concept disclosures and legacy-source notes remain in place. This refreshed build has been regenerated across all 13 routes; it still needs a new visual browser review after the typography update.
