# Legacy SEO and technical inventory

## Platform and delivery

- Platform: Hostinger Website Builder / Zyro
- Generator meta: `Hostinger Website Builder`
- Runtime pattern: Astro islands with Vue components
- Build namespace: `_astro-1785432754733`
- Server/CDN identifier: `hcdn`
- Page `Last-Modified`: July 30, 2026
- Sitemap `lastmod`: July 30, 2026
- Page cache header: `public, max-age=3600`
- HTML compression enabled
- HTTP redirects to HTTPS
- `www` redirects to the non-`www` canonical host
- Builder data identifies the template as `aigenerated`

### Security and transport headers observed

- Strict-Transport-Security with a two-year max age, includeSubDomains, and preload
- X-Content-Type-Options: nosniff
- X-XSS-Protection: 1; mode=block
- Referrer-Policy: same-origin
- Content-Security-Policy contains `frame-ancestors` allowances but is not a comprehensive content-security policy
- Hostinger platform header exposed: `X-Powered-By: HostingerWebsiteBuilder`

## Route inventory

| Route | Legacy title | Indexable | Canonical |
| --- | --- | --- | --- |
| `/` | Plexus Development Group: Expert Construction in Nova Scotia \| Plexus Development Group | Yes | `https://plexusdevelopmentgroup.ca/` |
| `/nova-scotia-construction-projects` | Plexus Development Group  Nova Scotia Construction Projects \| Plexus Development Group | Yes | Same route |
| `/residential-construction` | Residential Construction Development in Nova Scotia \| Plexus Development Group | Yes | Same route |
| `/commercial-construction` | Commercial Construction Experts in Nova Scotia \| Plexus Development Group | Yes | Same route |
| `/industrial-construction` | Industrial Construction Development Experts in Nova Scotia \| Plexus Development Group | Yes | Same route |
| `/community` | Connecting People and Community with Plexus Development Group \| Plexus Development Group | Yes | Same route |
| `/contact-for-real-estate-opportunities` | Contact Plexus Development Group for Investment Properties and Halifax Real Estate \| Plexus Development Group | Yes | Same route |

No additional same-domain content routes were found in the sitemap, internal navigation, rendered DOM, or targeted `site:` search.

## Sitemap

Source: `https://plexusdevelopmentgroup.ca/sitemap.xml`

The sitemap lists all seven public pages. All entries use the same July 30, 2026 modification timestamp. The homepage has priority `1.0`; the other pages have priority `0.5`.

The XML declares image sitemap support but contains no `<image:image>` entries.

## Robots and indexability

`https://plexusdevelopmentgroup.ca/robots.txt` contains:

```text
User-agent: *
Disallow:

Sitemap: https://plexusdevelopmentgroup.ca/sitemap.xml
```

No page contains a robots meta directive. The legacy public site was therefore indexable and followable by default.

This is opposite to the current revamped review build, which intentionally uses `noindex,nofollow`. The revamped directive should remain until approved for production launch.

## Language and international metadata

- HTML language: `en`
- Revamped site language: `en-CA`
- Only `hreflang="x-default"` is declared
- No French or other alternate-language versions exist

For the revamped Canadian site, `en-CA` is the more accurate language declaration.

## Structured data

### Homepage

JSON-LD type: `WebSite`

Includes:

- Name
- URL
- Description
- Language
- Keywords

### Other pages

JSON-LD type: `WebPage`

Includes:

- Name
- URL
- Description
- Language
- Keywords

### Missing structured data

No captured schema types were found for:

- Organization
- LocalBusiness
- RealEstateAgent
- Person
- Project
- Place
- Address
- ContactPoint
- BreadcrumbList
- FAQPage

The revamped site should add only truthful, useful schema. It should not mark planned projects as completed real-estate assets.

## Open Graph and Twitter metadata

Present:

- `og:title`
- `og:description`
- `og:type`
- `og:url`
- `og:site_name`
- `twitter:title`
- `twitter:description`
- `twitter:card: summary_large_image`

Problems:

- `og:image` exists but is empty
- `twitter:image` exists but is empty
- Image alt fields are empty
- Shared links therefore have no useful social preview image
- Twitter card requests a large image that is not supplied

## Favicon and platform icons

The site requests the same Plexus source artwork at 16, 16, 32, 32, 192, and Apple touch sizes through the Zyro image CDN.

## Form inventory

No forms were submitted during research.

| Page | Legacy form name | Visible fields | Delivery |
| --- | --- | --- | --- |
| Homepage | Contact form 16 | Name, last name, email, message | Hostinger form backend |
| Projects | None | — | — |
| Residential | Subscribe form | Email | Hostinger form backend |
| Commercial | Contact form | Name, last name, email, message | Hostinger form backend |
| Industrial | None | — | — |
| Community | Contact form 17 | Name, email, message | Hostinger form backend |
| Contact | Contact form 15 | Name, email, message | Hostinger form backend |
| Contact | Subscribe form 1 | Email field, but visible label says Your Name | Hostinger form backend |

### Submission architecture

The rendered JavaScript posts form data as JSON to a Hostinger endpoint shaped like:

```text
POST https://builder-backend.hostinger.com/u1/data/v3/post/{public-form-token}
```

Each form has a public form identifier/token embedded in the delivered page. These are not account credentials, but they have been omitted from this summary.

The submitted body contains:

- Element ID
- Form field model

The forms therefore had server-side handling in the legacy site. This differs from the current revamped site, whose form prepares an email draft.

### Validation and success states

- Required email validation is implemented
- Required message validation is implemented
- Name requirements vary between forms
- Success messages are shown after a successful Hostinger POST
- The architecture includes an optional Google conversion event only when conversion tracking is enabled
- No active Google tracking tag was identified in the captured pages

### Form UX issues

- The contact-page Stay Connected form labels an email field as Your Name
- Its placeholder says Enter full name
- Its button says Send Message
- The residential newsletter says subscribers receive exclusive special deals, which is unusual for a development-group newsletter
- No visible privacy consent or privacy link accompanies form submission
- No spam-prevention mechanism is visible in the authored form markup

## Cookies, consent, and analytics

The Hostinger runtime includes a cookie-consent component with:

- Strictly Necessary Cookies
- Platform Analytics
- Hostinger-described use of Amplitude for consent-based platform analytics

The runtime includes code paths for:

- Amplitude
- Hostinger frontend event API
- Google conversion tracking
- Hostinger builder and e-commerce endpoints

No analytics request was observed in the headless capture before consent. The captured rendered network consisted primarily of site, Zyro asset, font, Unsplash, and Pexels resources.

The legacy site does not include a dedicated privacy-policy route even though it uses forms, cookies, and consent-based analytics.

## External services and resources

### Directly used

- `assets.zyrosite.com`
- `cdn.zyrosite.com`
- `fonts.gstatic.com`
- `images.unsplash.com`
- `images.pexels.com`
- `videos.pexels.com`
- `builder-backend.hostinger.com` when a form is submitted
- `lifestyleenclave.ca` as the only project-specific outbound link

### Outbound links

- Facebook generic homepage
- Instagram generic homepage
- LinkedIn generic homepage
- X/Twitter generic homepage
- Lifestyle Enclave official site

No identifiable Plexus social profile was linked.

## Typography

The legacy pages load Google font families through Zyro/CDN resources:

- Montserrat
- Albert Sans
- Poppins
- Noto Sans Japanese
- Roboto

The archive contains 157 font files, many language and weight subsets. This is substantially heavier and more fragmented than the current revamped site's local font strategy.

## Media weight

Directly referenced static resources captured across the site:

| Resource type | Files | Approximate bytes |
| --- | ---: | ---: |
| Responsive image renditions | 493 | 48.5 MB |
| Font files/subsets | 157 | 5.6 MB |
| Hero video | 1 | 32.1 MB |
| CSS | 3 | 647 KB |
| Other resources | 7 | 1.1 MB |

An additional 1.4 MB of dynamically loaded JavaScript chunks was captured across rendered pages.

### Hero video

- Source host: Pexels
- File: `2282013-uhd_2732_1440_24fps.mp4`
- Duration: 20.83 seconds
- Resolution: 2732 × 1440
- Frame rate: 24 fps
- Codec: H.264
- Pixel format: yuv420p
- Audio: none
- Size: 32,086,497 bytes
- Used as the homepage background film
- No separate mobile rendition
- No Pexels title, author, or source-page link displayed by Plexus

### Image strategy

- Zyro CDN creates many responsive renditions
- Unsplash images are loaded remotely
- Pexels poster and video are loaded remotely
- Several concept images have no alt text
- Some logo and concept alt text contains typos
- Generic stock imagery is sometimes presented beside project-specific text without a clear concept label
- Original high-resolution source captures are available in `media-originals/`

## HTML and heading observations

- Homepage contains two H1 elements: the brand statement and About Us
- Heading levels frequently jump to H5 and H6 for ordinary section content
- Concept labels are often embedded in images rather than accessible text
- Some images use empty alt text even when they convey project information
- The old site has no project-detail routes and therefore limited semantic project structure

These are reasons to use the archived material as content research, not as a template for the new markup.

## SEO strengths worth retaining as source material

- Clear sitemap
- Consistent canonical URLs
- HTTPS and `www` normalization
- Unique page titles
- Unique meta descriptions
- Relevant legacy keyword sets
- Local contact details
- Direct official Lifestyle Enclave link
- Publicly indexable content with no robots blocking

## SEO issues not to carry forward

- Empty social images
- Generic social links
- No privacy route
- No LocalBusiness or Organization schema
- No project schema or project detail pages
- No image sitemap entries
- Awkward keyword-heavy titles such as repeated “Experts”
- Broad claims unsupported by the page
- Missing or incorrect image alt text
- Two H1s on the homepage
- `lang="en"` instead of `en-CA`
- Generic platform template and AI-generated builder structure
- Large remote hero video without a mobile alternative
- No visible form privacy consent
- `© 2025` stale footer date
- No meaningful project status, approval, or availability qualifiers in several sections

## Current revamped-site implication

The new site should not copy the legacy technical implementation. It should use the legacy site only as a source archive for:

- Approved company positioning
- Legacy project names and descriptions
- Historical contact details
- Source media and concepts
- Audience and sector themes

The current revamped architecture, local media strategy, explicit noindex review state, factual qualifiers, and accessible page structure should remain the governing implementation.
