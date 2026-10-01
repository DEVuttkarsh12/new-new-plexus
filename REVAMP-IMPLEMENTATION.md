# Plexus website revamp implementation and launch handoff

## Delivered in the review build

- New corporate positioning, dark navy / warm white / restrained gold visual system, accessible responsive navigation and a homepage led by locally hosted Halifax drone footage.
- Sourced “at a glance” figures, selected projects, a location interface, capabilities, reasons to work with Plexus, audience-specific partnership paths, leadership, impact, insights and news.
- Filterable portfolio and individual profiles for Lifestyle Enclave, Two River / Mineville and Cornwallis Park, with earlier residential names kept in a separate reference record. Each page labels construction material or a concept and includes source caveats.
- Acquisitions, landowner, broker, capital, municipality, careers, media centre, contact, privacy, terms, accessibility, legal and search pages.
- Unique page titles and descriptions, canonical and social tags, organization and breadcrumb structured data, sitemap, robots controls, image alt text, reduced-motion support and a static 404 page.
- Working email-draft forms with required fields, consent checkbox and a hidden spam field. No message or file is claimed to have been submitted.

## Facts that must be confirmed before broader publication

The client strategy uses examples that are not backed by the current captured materials. Do not publish them as current facts without Plexus source documents and publication approval:

| Item | Needed evidence |
| --- | --- |
| Lifestyle Enclave “completed / leasing 2026” | Current occupancy and leasing confirmation. The previously reviewed project site described construction and planned October 2026 move-in. |
| The Sable / Sables, 64 units, Lucasville, under construction | Current project name, unit mix, location, status, role, imagery and approval. Earlier public material contains a name but no verified profile. |
| Greenwood / Kings County 27 acres | Title or role, site boundary, correct location, scope and status. Earlier Greenwood copy conflicts with Lucasville. |
| Atholea / Cole Harbour 160+ acres | Site and role documentation, acreage, status and approved imagery. |
| Wilmot, Lucasville and Plexus Storage | Separate project identities, locations, current stages, Plexus role and permission to publish. |
| Cornwallis Park and Two River numbers | Current parcel, ownership/role, planning and survey confirmation. Published concepts are labelled illustrative in this build. |
| Company-wide totals | A dated, auditable project and asset register for units, acres, capital, markets and completions. Do not sum concept figures as controlled land or approved pipeline. |
| Partners, impacts, team and sustainability | Logo permissions; named leader biographies; community programme evidence; energy, water, EV, accessibility and employment measures. |

Source boundary: `research/legacy-site-capture-2026-09-25/CLAIMS-NEEDS-CONFIRMATION.md` and `projects.json`. The client strategy document provides direction, not proof of operational status.

## CRM and secure acquisition submissions

The user confirmed that no CRM or form service is available yet. The current forms therefore prepare an email draft. To enable actual submissions:

1. Choose the destination CRM and secured file store, and identify the internal owner/inbox for each audience: acquisitions, capital, municipality, tenant, media and careers.
2. Add a server-side endpoint for each form. Validate fields and file types/size on the server, apply rate limits and spam screening, and write uploads to private storage. Never expose offering memoranda or surveys through public asset URLs.
3. Create the CRM contact and opportunity with source and UTM fields; notify the assigned owner; send a confirmation email only after persistence succeeds.
4. Add a real success page and conversion event. Replace the email-draft wording only after an end-to-end submission test, including file upload and CRM record checks.
5. Publish the final privacy/retention language for those services and have counsel review capital and acquisition copy.

A private partner portal, data rooms, lead scoring, marketing automation and a CMS require product/service selection, access rules and ongoing operational ownership. They are not simulated in this public static build.

## Production setup

- Obtain approved project photography, a commissioned corporate film, professional portraits, named organizations and milestone announcements. The homepage currently uses licensed Halifax stock footage; the Lifestyle Enclave project page retains its construction film.
- Implement true HTTP 301 redirects for the nine former paths in the production host. The static fallback pages currently use meta refresh for preview continuity only.
- Choose a CMS or editorial workflow for projects, metrics, articles, jobs, images and SEO fields. `projects.json` is the interim structured project record.
- Set the production origin and launch flag in `generate_site.py`, regenerate, then verify canonical URLs, robots.txt and sitemap.xml on the actual domain.
- Connect privacy-reviewed analytics and Search Console after the production domain is known. Do not turn on advertising tags without the relevant consent controls.
- Review privacy, terms, accessibility, project disclaimers and capital language with Plexus’s advisers before public launch.
- Validate accessibility, real mobile performance, metadata, structured data, redirects, all forms and assets on production hosting.
