from pathlib import Path
import json,html,hashlib
import sector_data as SD
import sector_pages as SP
ROOT=Path(__file__).parent;OUT=ROOT/'dist';DATA=json.loads((ROOT/'projects.json').read_text())
def esc(s):return html.escape(str(s),quote=True)
def arrow():return '<span class="button-arrow" aria-hidden="true">→</span>'
def button(text,href,style='dark'):return f'<a class="button {style}" href="{href}"><span>{text}</span>{arrow()}</a>'
def label(text):return f'<span class="section-label">{text}</span>'
def image(name,alt,cls='',lazy=True):return f'<img class="{cls}" src="/assets/{name}" alt="{esc(alt)}" width="1600" height="1000"'+(' loading="lazy"' if lazy else ' fetchpriority="high"')+'>'
def heading(kicker,title,desc):return f'<div class="section-heading reveal"><div>{label(kicker)}<h2>{title}</h2></div><p>{desc}</p></div>'

# Navigation mirrors the seven destinations the previous site exposed.
NAV_LINKS=[
 ('/','Home'),
 ('/projects/','Projects'),
 ('/residential/','Residential'),
 ('/commercial/','Commercial'),
 ('/industrial/','Industrial'),
 ('/community/','Community'),
 ('/contact/','Contact'),
]
NAV_KEYS=('home','projects','residential','commercial','industrial','community','contact')
def navlink(href,text,current):
 cur=' aria-current="page"' if current else ''
 return f'<a{cur} href="{href}">{text}</a>'

def header(active='',home=False):
 brand='<a class="brand" href="/" aria-label="Plexus Development Group home"><img src="/assets/logo.png" alt="" width="48" height="48"><span>Plexus<small>DEVELOPMENT GROUP</small></span></a>'
 nav=f'''<nav class="desktop-nav" aria-label="Main navigation">{''.join(navlink(h,l,active==key) for key,(h,l) in zip(NAV_KEYS,NAV_LINKS))}{'' if home else button('Let’s talk','/contact/')}</nav>'''
 contents=nav+brand+'<a class="home-enquiry" href="/contact/">Let’s talk <span aria-hidden="true">↗</span></a>' if home else brand+nav
 mobile=''.join(navlink(h,l,active==key) for key,(h,l) in zip(NAV_KEYS,NAV_LINKS))
 return f'''<a class="skip-link" href="#main">Skip to content</a><header class="site-header {'estate-header' if home else ''}"><div class="nav-inner">{contents}<button class="menu-toggle" aria-label="Open navigation" aria-controls="mobile-menu" aria-expanded="false"><span></span><span></span></button></div></header><div class="mobile-menu" id="mobile-menu" hidden><nav aria-label="Mobile navigation">{mobile}</nav><p>Building with the long view.<br>Rooted in Nova Scotia.</p></div>'''

def footer():return f'''<section class="footer-cta"><div class="footer-cta-copy container"><div><span class="section-label">THE NEXT OPPORTUNITY</span><h2>Let’s build<br>what’s next.</h2></div><a href="/contact/" class="contact-orbit" aria-label="Start a conversation with Plexus"><span aria-hidden="true">↗</span></a></div></section><footer class="site-footer"><div class="footer-main container"><div class="footer-brand"><a class="brand" href="/"><img src="/assets/logo.png" alt="Plexus Development Group" width="50" height="50"><span>Plexus<small>DEVELOPMENT GROUP</small></span></a><p>Building. Development. Investment. Land.<br>Halifax, Nova Scotia.</p></div><div><h3>Explore</h3><a href="/projects/">Projects</a><a href="/residential/">Residential</a><a href="/commercial/">Commercial</a><a href="/industrial/">Industrial</a><a href="/community/">Community</a><a href="/about/">The group</a><a href="/contact/">Contact us</a></div><div><h3>Get in touch</h3><a href="mailto:info@plexusdevelopmentgroup.ca">info@plexusdevelopmentgroup.ca</a><a href="tel:+19028099399">+1 902 809 9399</a><address>3845 Joseph Howe Drive, Suite 100<br>Halifax, Nova Scotia</address></div></div><div class="footer-signature container" aria-hidden="true"><div class="footer-word">Plexus</div></div><div class="footer-bottom container"><span>© <span data-year>2026</span> Plexus Development Group</span><button class="motion-preference" aria-pressed="false">Pause motion</button><a href="/privacy/">Privacy</a><a href="#top">Back to top ↑</a></div></footer>'''

def dialogs(include_film=False):
 photo='''<dialog class="photo-dialog" aria-labelledby="photo-title"><div class="dialog-top"><span id="photo-title">Project image</span><button data-close-photo aria-label="Close image preview">Close ×</button></div><img class="photo-full" alt=""><div class="photo-caption"><p></p><div><button data-photo-prev aria-label="Previous image">←</button><span class="photo-count" aria-live="polite"></span><button data-photo-next aria-label="Next image">→</button></div></div></dialog>'''
 film='''<dialog class="film-dialog" aria-labelledby="film-title"><div class="dialog-top"><span id="film-title">Lifestyle Enclave · On site</span><button data-close-film aria-label="Close film">Close ×</button></div><video class="overview-film" controls playsinline preload="none" poster="/assets/lifestyle-drone.webp" aria-label="Silent construction film of Lifestyle Enclave"></video><p>Official construction footage · Upper Hammonds Plains · Silent film</p></dialog>'''
 return photo+(film if include_film else '')
def card(p):
 return f'''<article class="listing-card reveal" data-project-card data-sector="{esc(p['sector'])}" data-region="{esc(p['region'])}" data-status="{esc(p['status'])}" data-search="{esc((p['title']+' '+p['location']+' '+p['description']).lower())}"><a class="listing-image" href="/projects/{p['slug']}/" aria-label="Explore {esc(p['title'])}">{image(p['image'],p['imageNote']+' of '+p['title'])}<span class="status-badge">{p['status']}</span><span class="image-note">{p['imageNote']}</span></a><div class="listing-title"><h3><a href="/projects/{p['slug']}/">{p['title']}</a></h3><a class="card-arrow" href="/projects/{p['slug']}/" aria-label="View {esc(p['title'])}">↗</a></div><p class="listing-location">{p['location']}</p><div class="listing-facts"><span>{p['sector']}</span><strong>{p['scale']}</strong></div></article>'''



def featured():
 return f'''<section class="featured section" id="projects"><div class="container">{heading('OUR PROJECTS','Building Nova Scotia’s future.','Residential communities, commercial opportunities and land for long-term development.')}<div class="listing-grid three">{''.join(card(p) for p in DATA[:3])}</div><div class="center-action">{button('View all projects','/projects/','light')}</div></div></section>'''

def opening():return '<div class="page-intro" aria-hidden="true"><div class="intro-signature"><div class="intro-word">Plexus</div><p class="intro-descriptor">Development Group</p></div><span class="intro-origin">Building · Development · Investment · Land</span><button tabindex="-1" class="intro-skip">Enter site</button></div>'


def leadership():return f'''<section class="leadership section" id="leadership"><div class="leadership-layout container"><figure class="leadership-portrait reveal">{image('pavneet-singh.webp','Pavneet Singh, real estate developer in Halifax')}<figcaption>HALIFAX, NOVA SCOTIA</figcaption></figure><div class="leadership-copy reveal">{label('BUILDING LEADERSHIP')}<h2>Local knowledge.<br><em>A builder’s mindset.</em></h2><p>Pavneet Singh brings a Halifax-based perspective across real estate advisory, investment opportunities, land development and building. Within Plexus, his focus is practical planning, trusted relationships and disciplined project growth, with a long view of each place and its community.</p><div class="leader-name"><strong>Pavneet Singh</strong><span>Real Estate Developer · Halifax, Nova Scotia</span></div><a class="text-link" href="/about/">Meet Plexus <span aria-hidden="true">↗</span></a></div></div></section>'''

def residential_hero():return '''<section class="hero estate-hero group-hero" aria-labelledby="estate-title">
  <figure class="estate-panorama" aria-hidden="true">
    <div class="estate-media">
      <div class="hero-media">
        <picture><source media="(max-width:809px)" srcset="/assets/halifax-waterfront-mobile.webp"><img class="estate-video-poster" src="/assets/halifax-waterfront.webp" alt="" width="1600" height="900" fetchpriority="high"></picture>
        <video class="site-film estate-film" muted loop playsinline preload="auto" poster="/assets/halifax-waterfront.webp" data-desktop-src="/assets/halifax-waterfront.mp4" data-mobile-src="/assets/halifax-waterfront-mobile.mp4" aria-hidden="true"></video>
      </div>
    </div>
  </figure>
  <div class="estate-shade" aria-hidden="true"></div>
  <div class="estate-copy">
    <p class="estate-overline estate-reveal">BUILDING · DEVELOPMENT · NOVA SCOTIA</p>
    <h1 id="estate-title"><span class="estate-title-line"><span class="estate-reveal">Building</span></span><span class="estate-title-line"><span class="estate-reveal"><em>Nova Scotia.</em></span></span></h1>
    <p class="estate-description estate-reveal">From the ground up, Plexus brings land, planning and project delivery together to shape homes, workplaces and lasting places across Nova Scotia.</p><a class="estate-link estate-reveal" href="/projects/">See what we’re building <span aria-hidden="true">↗</span></a>
  </div>
  <div class="estate-foot estate-reveal">
    <div class="estate-project"><small>Halifax, Nova Scotia</small><span>Plexus Development Group</span><small>Atlantic Canada outlook</small></div>
    <a class="estate-discover" href="#introduction"><span class="estate-down" aria-hidden="true">↓</span><span>Discover Plexus</span></a>
    <span class="estate-credit">Halifax waterfront · Nova Scotia</span>
  </div>
</section>'''
def home():
 return (opening()+residential_hero()+home_introduction()+home_services()+featured()
  +home_commitments()+home_partners())



def pagehero(kicker,title,desc):return f'<section class="page-hero container">{label(kicker)}<h1>{title}</h1><p>{desc}</p></section>'
# --- Group structure chart -------------------------------------------------
def group_chart():
 branches=''
 for b in SD.BRANCHES:
  n=len(b['items'])
  if b['items']:
   items='<ul class="chart-items">'+''.join(
    (f'<li><a class="chart-item is-linked" href="{href}"><span class="chart-name">{esc(name)}</span><em class="chart-tag">{esc(tag)}</em></a></li>' if href
     else f'<li><span class="chart-item"><span class="chart-name">{esc(name)}</span><em class="chart-tag">{esc(tag)}</em></span></li>')
    for name,href,tag in b['items'])+'</ul>'
  else:
   items=('<div class="chart-leaf">'
          f'<p>{esc(b["note"])}</p>'
          '<a class="chart-leaf-link" href="/projects/cornwallis-park/">See the Cornwallis Park record</a></div>')
  count=(f'<span class="chart-count">{n:02d}</span>' if n
         else '<span class="chart-count is-none">00</span>')
  branches+=(f'<article class="chart-branch reveal" id="branch-{b["id"]}">'
   f'<header class="chart-head"><h3><span class="chart-dot" aria-hidden="true"></span>{esc(b["label"])}</h3>{count}</header>'
   f'<p class="chart-summary">{esc(b["summary"])}</p>{items}</article>')
 notes=''.join(f'<li>{n}</li>' for n in SD.STRUCTURE_NOTES)
 return f'''<section class="structure section" id="structure" aria-labelledby="structure-heading"><div class="container">{heading('PLEXUS DEVELOPMENT GROUP','Our group structure.','Residential, commercial, industrial and clean energy.')}<div class="chart-root reveal"><span class="chart-root-label">{esc(SD.ROOT)}</span></div><div class="chart-stem" aria-hidden="true"></div><div class="chart-branches">{branches}</div><details class="chart-notes content-details"><summary>About the project names &amp; source chart <span aria-hidden="true">+</span></summary><div><ul>{notes}</ul><p>Every name shown as an earlier name was published without supporting project detail. Inclusion records the group&rsquo;s earlier public record. It does not mean each project is currently active, approved or owned.</p><button class="text-link" data-photo="group-structure-source.webp" data-photo-title="Original Plexus group structure" data-photo-note="Original published hierarchy graphic">View original chart <span aria-hidden="true">↗</span></button></div></details></div></section>'''


def asset_classes():
 items=''.join(f'<li>{esc(a)}</li>' for a in SD.ASSET_CLASSES)
 return f'''<section class="asset-classes section" id="asset-classes"><div class="container"><div class="asset-classes-inner reveal"><div>{label('ASSET CLASSES')}<h2>Our project &amp; asset classes.</h2></div><div><p>Development interests across Nova Scotia.</p><ul>{items}</ul></div></div></div></section>'''

# --- Sector page sections --------------------------------------------------



def sector_project_list(entries,empty_note=''):
 out='<div class="sector-projects">'
 for e in entries:
  filename=e['image'] or ('plexus-storage.webp' if e['name']=='Plexus Storage' else '')
  if filename:
   note=e.get('note') or 'Concept visualization'
   visual=f'<button class="sector-visual" data-photo="{filename}" data-photo-title="{esc(e["name"])}" data-photo-note="{esc(note)}" aria-label="Enlarge {esc(e["name"])}">{image(filename,e.get("alt") or e["name"]+" brand artwork")}<span class="image-note">{"BRAND ARTWORK" if filename=="plexus-storage.webp" else "CONCEPT VISUALIZATION"}</span></button>'
  else: visual=''
  name=f'<a href="{e["href"]}">{esc(e["name"])}</a>' if e.get('href') else esc(e['name'])
  extra=(f'<details class="content-details"><summary>Project information <span aria-hidden="true">+</span></summary><div><p>{esc(e["detail"])}</p><p class="source-note">{esc(e.get("note", ""))}</p></div></details>' if e.get('detail') else '')
  out+=f'''<article class="sector-project {'has-image' if filename else 'text-only'}">{visual}<div class="sector-project-copy"><div class="sector-project-head"><h3>{name}</h3><span class="sector-status">{esc(e['status'])}</span></div><p class="sector-project-summary">{esc(e['summary'])}</p>{extra}{button('View project',e['href']) if e.get('href') else ''}</div></article>'''
 return out+'</div>'

def sector_work(kicker,title,desc,entries,empty_note=''):
 return f'<section class="sector-work section container">{heading(kicker,title,desc)}{sector_project_list(entries,empty_note)}</section>'


def sector_hub(self_route, title, body):
    """Index of the sector destinations, excluding the page you are already on.

    Rendered as a table with a header row so the columns read as an index
    rather than as scattered links with gaps between them.
    """
    links = SP.cross_links(self_route)
    rows = ''.join(
        f'<a class="sector-hub-row reveal" href="{href}">'
        f'<span class="sector-hub-index">{n}</span>'
        f'<span class="sector-hub-name">{esc(t)}</span>'
        f'<span class="sector-hub-desc">{esc(d)}</span>'
        f'<span class="sector-hub-arrow" aria-hidden="true">\u2197</span></a>'
        for n, href, t, d in links)
    word = 'destination' if len(links) == 1 else 'destinations'
    return (
        f'<section class="sector-hub section" id="by-sector"><div class="container">'
        f'<div class="sector-hub-top reveal"><span class="section-label">SECTORS</span>'
        f'<span class="sector-hub-count">{len(links)} {word}</span></div>'
        f'<div class="sector-hub-heading reveal"><h2>{title}</h2>'
        f'<p class="sector-hub-intro">{body}</p></div>'
        f'<div class="sector-hub-list">'
        f'<div class="sector-hub-columns" aria-hidden="true">'
        f'<span>No.</span><span>Sector</span><span>What it covers</span><span></span>'
        f'</div>{rows}</div>'
        f'</div></section>')


# --- Sector pages ----------------------------------------------------------
def residential_page():
 detailed=[p for p in DATA if p['sector']=='Residential']
 return (pagehero('RESIDENTIAL','Our Residential Projects','Showcasing our residential builds across Nova Scotia.')
  +f'''<section class="sector-work section container">{heading('CURRENT & PLANNED','Homes across Nova Scotia.','Multi-unit housing, single-family subdivisions and mixed residential communities.')}<div class="listing-grid three">{''.join(card(p) for p in detailed)}</div></section>'''
  +residential_names()
  +compact_sector_focus('UPCOMING PROJECTS','Active &amp; planned focus areas.',SD.RESIDENTIAL_TYPES,
   'Crafting comfortable living spaces with care and precision.','residential')
  +sector_hub('/residential/','Explore the group.','Discover our other sectors and community priorities.'))

def commercial_page():
 return (pagehero('COMMERCIAL','Our Commercial Projects','Practical, high-quality space for growing businesses.')
  +sector_work('COMMERCIAL & MIXED USE','Projects &amp; opportunities.','Commercial plazas, self-storage and spaces for local services.',SD.COMMERCIAL_PROJECTS[:3])
  +sector_additional(SD.COMMERCIAL_PROJECTS[3:],'More commercial names &amp; opportunities')
  +compact_sector_focus('OUR APPROACH','Built around local needs.',SD.COMMERCIAL_TYPES,
   'Aligning commercial projects with population growth, employment hubs, and infrastructure investment.','commercial')
  +sector_hub('/commercial/','Explore the group.','Discover our other sectors and community priorities.'))

def industrial_page():
 return (pagehero('INDUSTRIAL','Our Industrial Projects','Showcasing our industrial builds across Nova Scotia.')
  +sector_work('STORAGE & LOGISTICS','Plexus Storage','Industrial parks, warehouses, flex-industrial and self-storage.',SD.INDUSTRIAL_PROJECTS[:1])
  +sector_additional(SD.INDUSTRIAL_PROJECTS[1:],'More industrial names &amp; opportunities')
  +compact_sector_focus('OUR APPROACH','Space for a working region.',SD.INDUSTRIAL_TYPES,
   'Strategic industrial development projects built for efficiency, scalability, and growth.','industrial')
  +sector_hub('/industrial/','Explore the group.','Discover our other sectors and community priorities.'))

def community_page():
 pillars=[('01','Housing That Supports Community Stability','Affordability, accessibility and long-term sustainability in residential development.'),
  ('02','Local Economic Growth','Construction, contractor engagement and regional economic activity.'),
  ('03','Responsible Land Development','Thoughtful land use, community integration and infrastructure planning.'),
  ('04','Financial Awareness &amp; Education','Financial literacy, homeownership awareness and investment guidance.')]
 future=['Affordable & Workforce Housing Expansion','Community-Integrated Developments','Local Partnerships & Community Collaboration','Sustainable Development Practices']
 community_details=community_source_details()
 return (pagehero('COMMUNITY','Building more than spaces.','Where every voice matters and community thrives together.')
  +f'''<section class="community-overview section container"><figure>{image('community.webp','Community and neighbourhood life')}<figcaption>Community perspective</figcaption></figure><div>{label('COMMUNITY COMMITMENT')}<h2>What community<br>means to us.</h2><p>Our projects across Nova Scotia are guided by a commitment to long-term social value, responsible growth, and community partnership.</p>{button('Connect with Plexus','/contact/?subject=Community%20partnership')}</div></section><section class="community-pillars section container">{''.join(f'<article class="community-pillar"><span>{n}</span><h3>{t}</h3><p>{d}</p></article>' for n,t,d in pillars)}</section><section class="community-record section"><div class="container">{label('COMMUNITY PARTNERSHIP')}<h2>Canadian Homeless Support<br>&amp; Development Foundation</h2><p>CHSDF is named in Plexus’s community material.</p><details class="content-details"><summary>About this partnership <span aria-hidden="true">+</span></summary><div><p>Contribution dates, amounts and programme details should be confirmed directly with Plexus.</p></div></details></div></section><section class="community-next section container">{heading('LOOKING AHEAD','What we intend to do next.','Quality, community connectivity and responsible growth.')}<ul class="focus-list">{''.join(f'<li><span>{i:02d}</span>{esc(t)}</li>' for i,t in enumerate(future,1))}</ul>{community_details}{button('Discuss a community opportunity','/contact/?subject=Community%20partnership')}</section>''')

def projects_page():
 return (pagehero('BUILDING ACROSS NOVA SCOTIA','Our Projects','Residential, commercial and industrial development. One group, a long-term view.')
  +'<nav class="page-index container" aria-label="On this page"><a href="#current-projects">Current projects ↓</a><a href="#structure">Group structure ↓</a><a href="#asset-classes">Asset classes ↓</a><a href="#project-location">Project locations ↓</a></nav>'
  +f'''<section class="project-browser container" id="current-projects"><aside class="filters" aria-label="Project filters"><div class="filter-heading"><h2>Current projects</h2><button class="clear-filters">Clear all</button></div><label>Search projects<input type="search" id="project-search" placeholder="Name or location"></label><details class="filter-options"><summary>Filter by location, stage or type <span aria-hidden="true">+</span></summary><div class="filter-fields"><label>Location<select id="filter-region"><option value="">All locations</option><option>Halifax region</option><option>Annapolis County</option><option>Nova Scotia</option></select></label><label>Development stage<select id="filter-status"><option value="">All stages</option><option>Under construction</option><option>Planned</option><option>Planning review</option><option>Pipeline</option></select></label><fieldset><legend>Project type</legend><label class="check-label"><input type="radio" name="sector" value="" checked>All projects</label><label class="check-label"><input type="radio" name="sector" value="Residential">Residential</label><label class="check-label"><input type="radio" name="sector" value="Land & mixed-use">Land &amp; mixed-use</label></fieldset></div></details></aside><div class="project-results"><div class="result-bar"><span class="result-count" role="status">{len(DATA)} projects</span><span>Nova Scotia, Canada</span></div><div class="listing-grid">{''.join(card(p) for p in DATA)}</div><div class="empty-state" hidden><h2>No matching projects.</h2><p>Try another location or clear your filters.</p><button class="button dark clear-filters">Reset filters</button></div></div></section>'''
  +group_chart()+asset_classes()+project_location()
  +sector_hub('/projects/','Explore by sector.','Residential, commercial, industrial and community.'))
def about_page():
 return (pagehero('ABOUT PLEXUS','Development with a long view.','A Nova Scotia–based development, investment and land-acquisition company.')
  +home_introduction(about=True)+company_statement()+leadership()+home_commitments()+home_partners())
def contact_page():return pagehero('CONTACT US','Let’s build something<br>that lasts.','Talk with Plexus about a building project, development opportunity, land or partnership in Nova Scotia.')+f'''<section class="contact-layout container" id="contact"><div class="contact-intro"><h2>Strong projects<br>start with a conversation.</h2><p>Connect with our Halifax team about building, land, a community or a development partnership.</p><div class="contact-photo">{image('halifax-waterfront.webp','Halifax waterfront seen across the harbour')}<span class="image-note">HALIFAX WATERFRONT · NOVA SCOTIA</span></div><a href="mailto:info@plexusdevelopmentgroup.ca">info@plexusdevelopmentgroup.ca</a><a href="tel:+19028099399">+1 902 809 9399</a><address>3845 Joseph Howe Drive, Suite 100<br>Halifax, Nova Scotia</address><div class="contact-hours"><span>Office hours</span><strong>Monday–Friday · 9am–5pm</strong></div></div><form class="enquiry-form"><label>Full name <span>*</span><input name="name" autocomplete="name" placeholder="Your full name" required maxlength="120"></label><label>Email address <span>*</span><input name="email" type="email" autocomplete="email" placeholder="Your email address" required maxlength="200"></label><label>Subject<input name="subject" placeholder="What would you like to discuss?" maxlength="180"></label><label>Message <span>*</span><textarea name="message" rows="5" placeholder="Tell us a little about your enquiry" required maxlength="3000"></textarea></label><button class="button dark" type="submit"><span>Prepare enquiry</span>{arrow()}</button><p class="form-note">Opens your email app with a draft for you to review and send.</p><p class="form-status" role="status"></p></form></section>'''
def detail(p):
 gallery=''
 for i,img in enumerate(p['gallery']):
  note='Construction photograph' if img=='lifestyle-drone.webp' else p['imageNote']
  title='Inside Lifestyle Enclave' if img=='lifestyle-lobby.webp' else p['title']
  gallery+=f'<button class="gallery-image" data-photo="{img}" data-photo-title="{esc(title)}" data-photo-note="{esc(note)}" aria-label="Enlarge {esc(title)} {note.lower()}">{image(img,title+", "+note,lazy=i>0)}<span>↗</span></button>'
 detail_heading=p.get('detailHeading','A place with a purpose.')
 feature_heading='Places in the pipeline' if p['slug']=='residential-pipeline' else ('Concept features' if p.get('conceptSource') else 'A closer look')
 use_groups=''
 if p.get('useGroups'):
  use_groups='<div class="use-groups">'+''.join(f'<article><span>0{i}</span><h3>{esc(title)}</h3><ul>{"".join(f"<li>{esc(item)}</li>" for item in items)}</ul></article>' for i,(title,items) in enumerate(p['useGroups'].items(),1))+'</div>'
 legacy_names=''
 if p.get('legacyNames'):
  legacy_names='<div class="legacy-names"><h3>Additional names in earlier materials</h3><div>'+''.join(f'<span>{esc(name)}</span>' for name in p['legacyNames'])+'</div><p>These names preserve the group’s earlier public record. They are not presented as active or approved projects until their scope and status are confirmed.</p></div>'
 return f'''<section class="detail-heading container"><a class="breadcrumb" href="/projects/">← All projects</a><div><div><span class="detail-status">{p['status']}</span><h1>{p['title']}</h1><p>{p['location']}</p></div><strong>{p['scale']}</strong></div></section><div class="detail-gallery container {'single' if len(p['gallery'])==1 else ''}">{gallery}</div><section class="detail-body container"><div class="detail-main"><h2>{detail_heading}</h2><p class="detail-lead">{p['lead']}</p><details class="content-details project-description"><summary>About this development <span aria-hidden="true">+</span></summary><div><p>{p['description']}</p><p>{p['detail']}</p></div></details><div class="detail-facts">{''.join(f'<div><span>{a}</span><strong>{b}</strong></div>' for a,b in p['facts'])}</div><h2>{feature_heading}</h2><ul class="amenity-list">{''.join(f'<li><span aria-hidden="true">{"·" if p.get("conceptSource") else "✓"}</span>{f}</li>' for f in p['features'])}</ul>{use_groups}{legacy_names}<p class="project-note">{p['note']}</p>{('<button class="button outline" data-open-film><span>Watch the construction film</span>'+arrow()+'</button>') if p['slug']=='lifestyle-enclave' else ''}</div><aside class="enquiry-card"><h2>Build the next step.</h2><p>Let’s talk about {p['title']} and the next step for you.</p>{button('Enquire about this project','/contact/?subject='+p['slug'])}{button('Visit Lifestyle Enclave',p['external'],'outline') if p.get('external') else ''}<a href="tel:+19028099399">+1 902 809 9399</a><small>Project details and availability are confirmed directly by the team.</small></aside></section><section class="related section container">{heading('MORE TO EXPLORE','A broader perspective.','Discover more from the Plexus project list.')}<div class="listing-grid three">{''.join(card(x) for x in DATA[:3] if x['slug']!=p['slug'])}</div></section>'''
def privacy():return pagehero('WEBSITE PRIVACY','Your enquiry.<br>Your choice.','How this website handles the information you choose to share.')+'''<section class="privacy-copy container section"><h2>Enquiries</h2><p>This website’s contact form prepares an email draft in your chosen email app. Completing the form does not send information through a website form service. You review and send the draft yourself. When you email Plexus, your email provider and the receiving email system process the message.</p><h2>Website functions</h2><p>The website uses locally hosted fonts, images and video. It does not include third-party advertising analytics in its authored code. Your browser keeps session settings to remember the opening animation and your motion preference during a visit. Hosting and access providers may process technical information needed to deliver and secure the site.</p><h2>Other websites</h2><p>Links to Lifestyle Enclave or other external websites lead to services governed by their own privacy practices.</p><h2>Contact</h2><p>For questions about information you have sent to Plexus, contact <a href="mailto:info@plexusdevelopmentgroup.ca">info@plexusdevelopmentgroup.ca</a>.</p></section>'''

# Compact presentation of the legacy site's content. Exact full-page captures
# remain in research/; additional project detail uses native disclosure controls.
def community_source_details():
 content=json.loads((ROOT/'legacy_content.json').read_text())
 future=''.join('<h3>'+esc(title)+'</h3><p>'+esc(text)+'</p>' for title,text in content['community_future'])
 vision=''.join('<p>'+esc(text)+'</p>' for text in content['community_vision'])
 moments=''.join('<figure>'+image(file,alt)+'<figcaption>'+esc(caption)+'</figcaption></figure>' for file,alt,caption in [('community-moments-bags.webp','Green bags arranged on tables and the floor','Prepared bags'),('community-moments-meals.webp','Prepared meal containers in a food-service setting','Prepared meals')])
 return '<div class="community-disclosures"><details class="content-details"><summary>Our vision &amp; future commitments <span aria-hidden="true">+</span></summary><div>'+vision+future+'</div></details><details class="content-details"><summary>Moments from our shared journey <span aria-hidden="true">+</span></summary><div><div class="moments-grid">'+moments+'</div><p class="source-note">Photographs published on Plexus’s community page. Event dates and programme details are not specified in the source.</p></div></details></div>'

def company_statement():
 content=json.loads((ROOT/'legacy_content.json').read_text())
 paragraphs=''.join('<p>'+esc(text)+'</p>' for text in content['statement'])
 return '<section class="company-statement container"><details class="content-details"><summary>Our story: the full company statement <span aria-hidden="true">+</span></summary><div>'+paragraphs+'</div></details></section>'

def home_introduction(about=False):
 return f'''<section class="introduction section container" id="introduction"><div class="intro-overline">{label('WELCOME TO PLEXUS DEVELOPMENT GROUP')}<span class="intro-index">HALIFAX, NOVA SCOTIA</span></div><div class="intro-layout"><h2>Building sustainable,<br>scalable communities.</h2><div><p>Plexus Development Group is a Nova Scotia–based development, investment, and land-acquisition company.</p><p>Our mission is to build sustainable, community-driven assets that create long-term value for our investors and Nova Scotian communities.</p>{button('View our projects' if about else 'About Plexus','/projects/' if about else '/about/')}</div></div></section>'''

def home_services():
 sectors=[('01','Residential','Multi-unit residential housing','Homes, mixed residential communities and senior living.','/residential/'),
  ('02','Commercial','Commercial plazas & mixed-use','Retail, professional space and places for growing businesses.','/commercial/'),
  ('03','Industrial','Industrial parks & logistics','Self-storage, warehousing and employment space.','/industrial/')]
 return f'''<section class="home-services section container" id="services">{heading('OUR SERVICES','Built around the way we live &amp; work.','Building tailored spaces across residential, commercial, and industrial sectors.')}<div class="service-index">{''.join(f'<a href="{href}" class="service-index-row"><span class="index-no">{n}</span><h3>{title}</h3><div><strong>{sub}</strong><p>{desc}</p></div><span class="index-arrow" aria-hidden="true">↗</span></a>' for n,title,sub,desc,href in sectors)}</div><p class="service-footnote">Strategic land, forestry and renewable energy integration form part of the group’s long-term development interests.</p></section>'''

def home_commitments():
 approach=['Energy-efficient design and green building standard','Environmentally responsible land use','Support for renewable energy integration','Community consultation and engagement.','Long-term asset durability and resilience']
 impact=['Affordable housing for growing communities','Employment opportunities during and after construction','Local partnerships with trades, suppliers, and municipalities','Economic growth through strategic investments in underdeveloped regions']
 return f'''<section class="home-commitments section"><div class="container commitments-grid"><div>{label('OUR DEVELOPMENT PHILOSOPHY')}<h2>Execution over hype.</h2><p>Focused on delivery. Measured growth. Repeatable systems.</p><div class="commitment-detail"><details class="content-details"><summary>Our Commitment to Sustainability <span aria-hidden="true">+</span></summary><div><ul>{''.join('<li>'+esc(t)+'</li>' for t in approach)}</ul></div></details><details class="content-details"><summary>Community Impact <span aria-hidden="true">+</span></summary><div><ul>{''.join('<li>'+esc(t)+'</li>' for t in impact)}</ul>{button('Our community','/community/')}</div></details><details class="content-details"><summary>Our Priorities <span aria-hidden="true">+</span></summary><div><ul><li>Long-term value creation</li><li>Practical, community-aligned development</li><li>Financial discipline &amp; conservative leverage</li><li>Strong partnerships with brokers, advisors, municipalities and capital partners</li></ul></div></details></div></div><figure>{image('lifestyle-drone.webp','Lifestyle Enclave during construction in Upper Hammonds Plains')}<figcaption>On site · Lifestyle Enclave · Construction photograph</figcaption></figure></div></section>'''

def home_partners():
 partners=[('01','Capital partners','Strong financial discipline. A vertically integrated approach.'),('02','Communities','Housing, employment and sustainable growth.'),('03','Brokers & sellers','A professional process and long-term relationships.')]
 return f'''<section class="home-partners section container">{heading('BRINGING VALUE','Our partners &amp; community.','Building lasting value through practical development and trusted relationships.')}<div class="compact-partners">{''.join(f'<article><span>{n}</span><h3>{title}</h3><p>{desc}</p></article>' for n,title,desc in partners)}</div></section>'''

def compact_sector_focus(kicker,title,items,desc,sector):
 return f'''<section class="compact-focus section"><div class="container">{heading(kicker,title,desc)}<ul class="focus-list">{''.join(f'<li><span>{n}</span>{esc(t)}</li>' for n,t,d in items)}</ul><details class="content-details"><summary>Our development approach <span aria-hidden="true">+</span></summary><div>{''.join(f'<h3>{esc(t)}</h3><p>{esc(d)}</p>' for n,t,d in items)}</div></details></div></section>'''

def sector_additional(entries,title):
 rows=''.join('<article><h3>'+(f'<a href="{e["href"]}">{esc(e["name"])}</a>' if e.get('href') else esc(e['name']))+'</h3><p>'+esc(e['summary'])+'</p><p>'+esc(e['detail'])+'</p><p class="source-note">'+esc(e.get('note',''))+'</p></article>' for e in entries)
 return '<section class="additional-opportunities container"><details class="content-details"><summary>'+title+' <span aria-hidden="true">+</span></summary><div>'+rows+'</div></details></section>'

def residential_names():
 names=[('The Sables','sables-logo.webp'),('The Parks of Cole Harbour','cole-harbour-logo.webp'),('Novabella Retirement Home','novabella-logo.webp'),('The Crownvale','crownvale-logo.webp'),('The Sarnaaz Valley','sarnaaz-logo.webp'),('The Amiora','amiora-logo.webp'),('The Chamelias','chamelias-logo.webp')]
 return f'''<section class="residential-names section"><div class="container">{heading('UPCOMING PROJECTS','Our residential communities.','Names and brand artwork published by Plexus. Project scope and timing are confirmed directly by the team.')}<div class="community-brand-grid">{''.join(f'<figure>{image(file,name+" brand artwork")}<figcaption>{esc(name)}</figcaption></figure>' for name,file in names)}</div><p class="source-note">Additional name in the group structure: The Aralias.</p></div></section>'''

def project_location():
 return f'''<section class="project-location section container" id="project-location"><div>{label('ACROSS NOVA SCOTIA')}<h2>Project locations.</h2><p>Showcasing our projects across Nova Scotia.</p><details class="content-details"><summary>About the location map <span aria-hidden="true">+</span></summary><div><p>{esc(SD.LOCATION_MAP_NOTE)}</p></div></details></div><button class="location-map" data-photo="project-locations.webp" data-photo-title="Plexus project locations" data-photo-note="Published location overview. Marker colours are not linked to named projects by a source legend." aria-label="Enlarge the project location map">{image('project-locations.webp','Published Plexus Development Group Nova Scotia project location map')}<span aria-hidden="true">View map ↗</span></button></section>'''

def asset_url(name):return '/'+name+'?v='+hashlib.sha256((OUT/name).read_bytes()).hexdigest()[:12]
# One flag controls search indexing for the whole site. Leave it False for the
# private review build. Set True only when a public domain launch is approved.
LAUNCH = False
SITE_ORIGIN = 'https://plexus-development.criyx-ai.chatgpt.site'
SITE_NAME = 'Plexus Development Group'

ROUTES = [
    ('', 'Building Nova Scotia | Plexus Development Group', 'A Halifax building and development group shaping residential, commercial and industrial places across Nova Scotia.'),
    ('projects', 'Projects', 'Every Plexus project with a detail page, the group-structure chart, and the commercial and industrial opportunities recorded in earlier public material.'),
    ('residential', 'Residential Building', 'Residential building across Nova Scotia, including multi-unit homes, single-family subdivisions, mixed communities, affordable-housing initiatives and senior living.'),
    ('commercial', 'Commercial Building', 'Commercial building and development opportunities, from plazas and retail to hospitality and mixed use.'),
    ('industrial', 'Industrial Building', 'Industrial building and development opportunities across warehousing, flex space, self-storage and logistics.'),
    ('community', 'Community', 'How Plexus approaches housing stability, local economic growth, responsible land use and financial awareness, with an honest record of earlier material.'),
    ('contact', 'Contact us', 'Talk to the Plexus team about building, land, investment, a development partnership or a community opportunity in Nova Scotia.'),
    ('about', 'About Plexus', 'Meet the Halifax building and development group bringing local perspective to projects across Nova Scotia.'),
    ('privacy', 'Website privacy', 'How the Plexus website handles the information you choose to share, and how the contact form works.'),
    ('projects/lifestyle-enclave', 'Lifestyle Enclave', 'A 102-unit residential community under construction in Upper Hammonds Plains, Nova Scotia.'),
    ('projects/two-river-mineville', 'Two River, Mineville', 'A planned 73-acre, 216-unit low-density residential community in Mineville, Nova Scotia. Concept stage.'),
    ('projects/cornwallis-park', 'Cornwallis Park', 'A 240-acre land opportunity in Annapolis County with potential for phased residential, commercial and complementary uses. Concept stage.'),
    ('projects/residential-pipeline', 'The next communities', 'The wider Plexus residential pipeline, including the community names carried forward from earlier public material.'),
]
ROUTE_META = {r: (t, d) for r, t, d in ROUTES}

def share_image():
    return asset_url('assets/og-image.png')

def write(route, title, body, active='', description=None):
    target = OUT / route / 'index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    url = SITE_ORIGIN + ('/' + route + '/' if route else '/')
    _, default_desc = ROUTE_META.get(route, (title, ''))
    desc = description or default_desc
    robots = 'index,follow,max-image-preview:large' if LAUNCH else 'noindex,nofollow'
    og_img = SITE_ORIGIN + share_image()
    target.write_text(f'''<!doctype html><html lang="en-CA"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{esc(title)} | {SITE_NAME}</title><meta name="description" content="{esc(desc)}"><meta name="robots" content="{robots}"><meta name="theme-color" content="#132822"><link rel="canonical" href="{url}"><meta property="og:site_name" content="{SITE_NAME}"><meta property="og:locale" content="en_CA"><meta property="og:title" content="{esc(title)} | {SITE_NAME}"><meta property="og:description" content="{esc(desc)}"><meta property="og:type" content="website"><meta property="og:url" content="{url}"><meta property="og:image" content="{og_img}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Plexus Development Group — development, investment and land in Nova Scotia"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)} | {SITE_NAME}"><meta name="twitter:description" content="{esc(desc)}"><meta name="twitter:image" content="{og_img}"><link rel="icon" href="/assets/logo.png"><link rel="preload" href="/assets/manrope-600.ttf" as="font" type="font/ttf" crossorigin><link rel="stylesheet" href="{asset_url('styles.css')}"><link rel="stylesheet" href="{asset_url('experience.css')}"><link rel="stylesheet" href="{asset_url('refinement.css')}"><script src="{asset_url('script.js')}" defer></script></head><body id="top" class="{'home-page' if not route else 'inner-page'}">{header(active,home=not route)}<main id="main">{body}</main>{footer()}{dialogs(route=='projects/lifestyle-enclave')}</body></html>''')

def write_index_files():
    today = '2026-09-28'
    urls = '\n'.join(
        f'  <url><loc>{SITE_ORIGIN}/{r+"/" if r else ""}</loc><lastmod>{today}</lastmod>'
        f'{"<changefreq>monthly</changefreq>" if not r else ""}'
        f'<priority>{"1.0" if not r else "0.8"}</priority></url>'
        for r, _, _ in ROUTES)
    (OUT / 'sitemap.xml').write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
    if LAUNCH:
        robots = f'User-agent: *\nAllow: /\n\nSitemap: {SITE_ORIGIN}/sitemap.xml\n'
    else:
        robots = ('User-agent: *\nDisallow: /\n\n'
                  '# This is a private review build. Set LAUNCH = True in generate_site.py\n'
                  '# and change SITE_ORIGIN to the production domain before going live.\n')
    (OUT / 'robots.txt').write_text(robots)

write_index_files()
write('', 'Building Nova Scotia', home(), 'home')
write('projects', 'Projects', projects_page(), 'projects')
write('residential', 'Residential', residential_page(), 'residential')
write('commercial', 'Commercial', commercial_page(), 'commercial')
write('industrial', 'Industrial', industrial_page(), 'industrial')
write('community', 'Community', community_page(), 'community')
write('contact', 'Contact us', contact_page(), 'contact')
write('about', 'About Plexus', about_page())
write('privacy', 'Website privacy', privacy())
for p in DATA:
    write('projects/' + p['slug'], p['title'], detail(p), 'projects', description=p.get('metaDescription'))

print('Generated 13 complete pages.')
