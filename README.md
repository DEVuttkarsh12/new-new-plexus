# Plexus Development Group website

This repository generates a static review site for Plexus Development Group. The September 2026 revamp follows the client strategy document and positions Plexus around development, investment, acquisitions, land and partnerships. Its public claims stay within the previously captured project record.

## Preview

```sh
python3 generate_site.py
python3 -m http.server 8080 --directory dist
```

Open `http://127.0.0.1:8080/`. Production serves `dist/` directly. The generator writes 28 content pages, nine legacy URL fallbacks, a sitemap, robots.txt and a 404 page. `LAUNCH = False` keeps the review build out of search indexes. Set `LAUNCH = True` and update `ORIGIN` in `generate_site.py` only when the production domain and publication content are approved.

## Edit

- `generate_site.py`: layout, navigation, page copy, metadata, structured data and route generation.
- `projects.json`: sourced project profiles, stage labels, facts and galleries.
- `dist/revamp.css`: navy, warm white and gold responsive design system.
- `dist/revamp.js`: navigation, portfolio filtering, site search, video behaviour and email-draft forms.
- `dist/assets/`: locally hosted source media.
- `REVAMP-IMPLEMENTATION.md`: source boundaries, external integration setup and launch tasks.
- `research/`: complete legacy public-site capture and claim review.

Run `python3 generate_site.py` after editing the generator or project data. CSS and JavaScript are served directly from `dist/`.

## Important preview limitations

The static forms open a prepared draft in the visitor's email app. They do not transmit or upload files, send confirmations, create CRM records or mark a submission as received. The site says this plainly beside each form. CRM, secure document handling, analytics, CMS access, approved corporate photography/video and production redirects need real services or approved material before launch. See `REVAMP-IMPLEMENTATION.md`.
