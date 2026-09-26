# Plexus Development Group: current design direction

Updated September 25, 2026.

## Positioning

The website presents Plexus as the parent development platform. The hierarchy now moves through:

1. Halifax and Nova Scotia as the place of operation
2. Development, investment and land as the group mandate
3. Residential, commercial, industrial and strategic land as connected pillars
4. A portfolio with projects at several stages
5. Long-term development practice and local relationships
6. Pavneet Singh as development leadership within the wider group

Lifestyle Enclave is one of four portfolio entries. Its apartment and construction storytelling lives on its detail page rather than defining the homepage.

## Art direction

The design combines deep forest green, mineral ivory and restrained brass with large editorial serif typography. Content sits directly in the viewport rather than inside rounded hero cards. Fine rules, small location metadata and disciplined spacing create the visual system.

The hero uses licensed Halifax waterfront film to establish place and scale. A left-aligned title, concise platform statement and a single portfolio link keep the first screen focused. The circular logo treatment in the navigation retains the original mark while making its square artwork feel intentional.

## Immersive sequences

The opening uses a quiet signature fade, a brief hold and a slow dissolve. Hero copy enters only after the loader is removed.

The development mandate becomes a pinned four-chapter sequence on wide screens. Each chapter changes the sector title, description, navigation state and progress line. The section uses typography and abstract rings instead of unrelated property imagery.

The existing horizontal portfolio remains intact and now leads with Two River, Mineville, Cornwallis Park and the wider community pipeline. Lifestyle Enclave appears in the complete portfolio grid below.

Reduced-motion mode removes pinning and presents every chapter in natural document order. Phones do the same, with the project journey remaining swipeable.

## Leadership treatment

Pavneet Singh appears in a separate editorial section after the portfolio. The official portrait has been cropped to remove the quotation and phone number embedded in the source artwork. The copy uses the verified role `Real Estate Developer` and avoids unverified executive titles.

## Portfolio record

The projects page carries four layers of information instead of one grid:

1. The filterable project browser, limited to entries with a full detail page.
2. The group-structure chart, rebuilding the previous site's hierarchy graphic as a readable four-branch tree. A root node, a 2px gold stem and trunk, and a drop into each branch. Branch headers carry a name count, a one-line summary of what the branch covers, and a list of names. Names with a detail page are links; earlier names are plain text with an `Earlier name` tag. The chart's own note block discloses every correction applied to the source.

   The chart is deliberately the heaviest art direction on the site. It is the only diagram, and a structure diagram that reads as delicate linework fails at its one job. The weight comes from the 2px trunk and drops, a 9px gold square on the root, a 9px marker per branch, larger branch headers and heavier name text.

   The Clean Energy branch has no children in the source. Rather than leave a void or invent content, the column states what is actually true: no detail was ever published, and its only appearance in published copy is wind and solar integration among the Cornwallis concept's potential uses, with a link to that record.

3. The asset-class strip, carrying the previous projects page's list of what the group considers.
4. The opportunity register, pairing the Wilmot and Lucasville legacy concept visuals with their qualified descriptions, closed by a band for Greenwood and Plexus Storage.

Earlier names are typographically linked but visually unboxed, so the register reads as a record rather than a gallery of unbuilt projects. Concept values use a neutral dot marker instead of the confirmation checkmark used for verified project features.

## Sector index

The "explore by sector" block is built as an index table, not a list of links. A `No. / Sector / What it covers` header row plus a fixed 300px sector column keep the description and the arrow in the same position on every row. Without the header the rows read as scattered links with a wide void between the name and the description, which is what made an earlier version look cut out.

The block also omits the page you are already on and renumbers the rest, so a reader is never offered a link back to where they are. `/projects/` shows four destinations rather than five.

## Sector pages

Residential, Commercial and Industrial each follow the same structure: page hero, a statement of why the sector matters, the development types the previous site named, the approach language, and the full opportunity record. Rows alternate image and copy, and rows with no published imagery use a hatched placeholder that says so rather than filling the space with unrelated stock.

Every sector page ends with a cross-link hub that omits the current sector and renumbers the remaining rows, so it always reads as a complete set of destinations.

## Community page

The community route uses the same typographic hierarchy as the About page: a statement, four numbered pillars, a dark honest-record section for the earlier CHSDF and financial-education material, and a closing long-view commitment. It carries no unverified metrics and states plainly which details were never published.

## Navigation

Seven primary destinations, matching the previous site: Home, Projects, Residential, Commercial, Industrial, Community, Contact. About and Privacy are supporting pages reachable from the footer.

Seven links plus a call-to-action is the tightest layout on the site. Spacing tightens across three desktop bands (1500px+, 1101–1340px, 810–1000px) before the mobile menu takes over. On mobile, link size is driven by viewport height with `clamp()` so all seven links and the tagline fit without scrolling from 320 x 568 upward.

## Reference principles

The direction was informed by primary agency and official property sources previously researched for the project:

- Vide Infra, Springs: https://videinfra.com/work/springs?expertise=8
- Vide Infra, Silver Pinewood Residences: https://videinfra.com/work/silver-pinewood-residences?expertise=8
- Vide Infra, Likova: https://videinfra.com/work/likova
- Locomotive, Désourdy: https://locomotive.ca/en/work/desourdy
- Locomotive, Populous: https://locomotive.ca/en/work/populous
- Aman Beverly Hills: https://www.aman.com/aman-beverly-hills
- Chelsea Barracks: https://www.chelseabarracks.com/

These references informed pacing, scale, restraint and the relationship between film and architecture. No paid template code, reference assets, fictional awards, testimonials or budget claims were copied.

## Operational limits

The Halifax hero footage is an establishing view, not evidence of a Plexus-owned property. Concept imagery is labelled. The contact form prepares an email draft. The preview remains private and excluded from search indexing. Responsive review verifies layout behavior in browser frames but is not physical-device certification.

## Validation for this revision

- Confirmed the licensed Halifax film advances on desktop and the 720 x 1280 rendition advances on a 320 px phone frame.
- Confirmed the mobile poster selects the portrait source before video playback.
- Reviewed the desktop hero, group mandate, selected-opportunity passage, leadership section, About page and Contact page.
- Exercised all four mandate chapter states and the horizontal portfolio navigation.
- Reviewed 320 and 390 px phone layouts with no document-level horizontal overflow.
- Opened and closed the phone navigation and verified its What we build anchor.
- Verified reduced-motion mode removes pinned sequences and pauses background film.
- Verified the smaller Lifestyle Enclave gallery image opens its own lobby source and caption.
- Verified the Lifestyle Enclave overview video exists only on its project page and cleans up after closing.
- Validated all thirteen routes, local references, duplicate IDs, image alt attributes, JavaScript syntax and video codecs.
- Swept all thirteen routes at 360, 390, 768, 810, 1024, 1280, 1440 and 1920 px with no document-level horizontal overflow, no broken images, no missing alt attributes, no unnamed links or buttons, no duplicate IDs and no heading-level jumps.
- Confirmed every lazy-loaded image resolves after scrolling, including the two legacy concept visuals.
- Confirmed the group-structure chart renders all four branches with the correct name counts and that every correction note is present.
- Confirmed the sector index shows exactly four destinations on every page that carries it, with no link back to the current page.
- Confirmed the desktop nav holds seven links plus the call-to-action at 1440, 1280, 1024, 900, 820 and 810 px.
- Confirmed the mobile menu shows all seven links and the tagline with no clipping at 320 x 568, 360 x 640, 390 x 844 and 430 x 932.
- Confirmed the active nav state is correct on every route, including project detail pages resolving to Projects.
- Exercised portfolio search, clear-filters and the empty state, and confirmed the result counter stays accurate.
- Opened the concept lightbox, stepped between both opportunity images and confirmed closing restores focus and clears the modal state.
- Confirmed the sector cross-link hubs omit the current sector and renumber correctly.
- Confirmed every page has a unique meta description, a canonical link and Open Graph tags pointing at the sharing card.
- Confirmed flipping `LAUNCH` to `True` switches robots meta, robots.txt and canonical URLs together, and that reverting restores the review state.
- No authored page-level browser errors were observed.
