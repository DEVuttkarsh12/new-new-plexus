# Live legacy-site refresh, September 28, 2026

Source: https://plexusdevelopmentgroup.ca/

This refresh follows the public sitemap and all internal page links. It captures seven canonical pages, robots.txt and sitemap.xml. Each page's HTML hash exactly matches the comprehensive September 25 capture. The root URL without its trailing slash resolves to the same homepage and is deduplicated.

- `pages/`: exact original HTML responses.
- `all-visible-text.txt`: the full extracted page text, including original wording and errors.
- `capture.json`: response records, hashes, headings, metadata, links, images, media, forms, scripts, schema, resource references and comparisons with the original capture.
- `../refresh_legacy.py`: reproducible refresh script.
- `responsive-audit.json`: 52 completed page/width reviews of the redesign, including footer and hero geometry, image sizing, missing media and browser errors.
- `interaction-audit.json`: completed navigation, filter, image-preview, disclosure, motion and contact-field checks.

504 direct resource URLs were rediscovered. The original comprehensive archive also follows stylesheet dependencies and browser runtime requests, retaining 661 referenced static URLs, 617 unique files, 43 deduplicated source images, the hero film, rendered DOM, network records, screenshots and visual analysis. Those records are reused because every current public page is byte-for-byte unchanged.

See `../legacy-site-capture-2026-09-25/README.md` for the exhaustive archive and `../../DESIGN-REFINEMENT-2026-09-28.md` for the content-to-design mapping. Source material remains evidence of what the site published; project status and unverified claims retain their existing qualifications.

No forms were submitted and no private or authenticated areas were accessed.
