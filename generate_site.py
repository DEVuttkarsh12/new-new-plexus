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
 return f'''<a class="skip-link" href="#main">Skip to content</a><header class="site-header {'estate-header' if home else ''}"><div class="nav-inner">{contents}<button class="menu-toggle" aria-label="Open navigation" aria-controls="mobile-menu" aria-expanded="false"><span></span><span></span></button></div></header><div class="mobile-menu" id="mobile-menu" hidden><nav aria-label="Mobile navigation">{mobile}</nav><p>Development with the long view.<br>Rooted in Nova Scotia.</p></div>'''

FAQ=[
 ('What is Plexus Development Group?','Plexus is a Halifax-based development, investment and land acquisition company. The group evaluates and advances opportunities across residential, commercial, industrial and mixed-use real estate in Nova Scotia.'),
 ('Where does Plexus operate?','Plexus is based in Halifax and focuses on Nova Scotia, with a broader Atlantic Canada outlook. Current portfolio locations include Upper Hammonds Plains, Mineville and Cornwallis Park.'),
 ('What kinds of projects does the group pursue?','The platform considers multi-unit housing, mixed-use and commercial space, industrial and logistics facilities, self-storage, strategic land and opportunities for renewable energy integration.'),
 ('Are all projects already built?','No. The project list includes work at different stages, from active construction to planning and longer-term development. Concept plans and architectural renderings describe a vision and may change through approvals and delivery.'),
 ('What is the difference between the projects page and the sector pages?','The projects page lists every project with a detail page and shows the group-structure chart. The residential, commercial and industrial pages carry the fuller record from the previous site for each branch, including opportunities that never had a project page.'),
 ('Why do some project names appear as earlier names?','Names such as The Sables, The Amiora, Novabella Retirement Home, The Evangeline, Plexus Storage, Greenwood, Wilmot and Lucasville were published on the previous site as logos or in a structure graphic, without supporting project detail. They are preserved as part of the record and are not presented as active or approved projects.'),
 ('How do I know which information is confirmed?','Every detail page and sector page carries a note stating what is confirmed and what requires confirmation. Concept values are shown with a neutral marker rather than a confirmation tick, and earlier names are listed separately from projects with their own pages.'),
 ('What is planned for Mineville?','The Mineville concept brings fourplex homes together with green space, walking trails and places for neighbours to gather. Published plans include community gardens, pocket parks and a clubhouse, with access to Highway 107 and Dartmouth. These are proposed features.'),
 ('What is the vision for Cornwallis Park?','The 240-acre Cornwallis Park property offers scope for phased residential, commercial and complementary uses between Digby and Annapolis Royal. Parcel-specific zoning, ownership and the address shown in concept artwork all require direct confirmation.'),
 ('How can I learn more about Lifestyle Enclave?','Lifestyle Enclave is one community within the Plexus portfolio. Visit <a href="https://lifestyleenclave.ca/" target="_blank" rel="noopener noreferrer">the project website</a> for layouts, availability and tour enquiries.'),
 ('Can I discuss a site, investment or partnership?','Yes. Plexus welcomes conversations with landowners, brokers, capital partners and municipalities. Email <a href="mailto:info@plexusdevelopmentgroup.ca">info@plexusdevelopmentgroup.ca</a> or call <a href="tel:+19028099399">+1 902 809 9399</a>.')
]
def faq():return f'''<section class="faq section container" id="questions">{heading('FAQ','A few things<br>worth knowing.','Clear answers about the group, its projects and how to start a conversation.')}<div class="faq-list">'''+''.join(f'<details class="faq-item reveal"><summary>{q}<span class="plus" aria-hidden="true"></span></summary><div class="faq-answer"><p>{a}</p></div></details>' for q,a in FAQ)+'</div></section>'
def footer():return f'''<section class="footer-cta"><div class="footer-cta-copy container"><div><span class="section-label">THE NEXT OPPORTUNITY</span><h2>Let’s build value<br>that <em>lasts.</em></h2></div><a href="/contact/" class="contact-orbit" aria-label="Start a conversation with Plexus"><span aria-hidden="true">↗</span></a></div></section><footer class="site-footer"><div class="footer-main container"><div class="footer-brand"><a class="brand" href="/"><img src="/assets/logo.png" alt="Plexus Development Group" width="50" height="50"><span>Plexus<small>DEVELOPMENT GROUP</small></span></a><p>Development. Investment. Land.<br>Halifax, Nova Scotia.</p></div><div><h3>Explore</h3><a href="/projects/">Projects</a><a href="/residential/">Residential</a><a href="/commercial/">Commercial</a><a href="/industrial/">Industrial</a><a href="/community/">Community</a><a href="/about/">The group</a><a href="/contact/">Contact us</a></div><div><h3>Get in touch</h3><a href="mailto:info@plexusdevelopmentgroup.ca">info@plexusdevelopmentgroup.ca</a><a href="tel:+19028099399">+1 902 809 9399</a><address>3845 Joseph Howe Drive, Suite 100<br>Halifax, Nova Scotia</address></div></div><div class="footer-word container" aria-hidden="true">Plexus</div><div class="footer-bottom container"><span>© <span data-year>2026</span> Plexus Development Group</span><button class="motion-preference" aria-pressed="false">Pause motion</button><a href="/privacy/">Privacy</a><a href="#top">Back to top ↑</a></div></footer>'''

def dialogs(include_film=False):
 photo='''<dialog class="photo-dialog" aria-labelledby="photo-title"><div class="dialog-top"><span id="photo-title">Project image</span><button data-close-photo aria-label="Close image preview">Close ×</button></div><img class="photo-full" alt=""><div class="photo-caption"><p></p><div><button data-photo-prev aria-label="Previous image">←</button><span class="photo-count" aria-live="polite"></span><button data-photo-next aria-label="Next image">→</button></div></div></dialog>'''
 film='''<dialog class="film-dialog" aria-labelledby="film-title"><div class="dialog-top"><span id="film-title">Lifestyle Enclave · On site</span><button data-close-film aria-label="Close film">Close ×</button></div><video class="overview-film" controls playsinline preload="none" poster="/assets/lifestyle-drone.webp" aria-label="Silent construction film of Lifestyle Enclave"></video><p>Official construction footage · Upper Hammonds Plains · Silent film</p></dialog>'''
 return photo+(film if include_film else '')
def card(p):
 return f'''<article class="listing-card reveal" data-project-card data-sector="{esc(p['sector'])}" data-region="{esc(p['region'])}" data-status="{esc(p['status'])}" data-search="{esc((p['title']+' '+p['location']+' '+p['description']).lower())}"><a class="listing-image" href="/projects/{p['slug']}/" aria-label="Explore {esc(p['title'])}">{image(p['image'],p['imageNote']+' of '+p['title'])}<span class="status-badge">{p['status']}</span><span class="image-note">{p['imageNote']}</span></a><div class="listing-title"><h3><a href="/projects/{p['slug']}/">{p['title']}</a></h3><a class="card-arrow" href="/projects/{p['slug']}/" aria-label="View {esc(p['title'])}">↗</a></div><p class="listing-location">{p['location']}</p><div class="listing-facts"><span>{p['sector']}</span><strong>{p['scale']}</strong></div></article>'''
def group_scope():return '''<section class="group-scope section" id="about"><div class="container"><div class="scope-intro reveal"><div><span class="section-label">THE PLEXUS PLATFORM</span><h2>A development platform<br>with <em>room to grow.</em></h2></div><p>Plexus takes a connected view of housing, business space, infrastructure and long-term land value.</p></div><div class="scope-grid"><a class="scope-item reveal" href="/residential/"><span>01</span><div><small>RESIDENTIAL</small><h3>Homes &amp;<br>communities</h3><p>Multi-unit housing, neighbourhoods and senior living shaped around Nova Scotia’s growth.</p></div></a><a class="scope-item reveal" href="/commercial/"><span>02</span><div><small>COMMERCIAL</small><h3>Plazas &amp;<br>mixed use</h3><p>Business and mixed-use opportunities aligned with people, employment and infrastructure.</p></div></a><a class="scope-item reveal" href="/industrial/"><span>03</span><div><small>INDUSTRIAL</small><h3>Logistics &amp;<br>storage</h3><p>Industrial parks, warehousing, self-storage and practical space for a working region.</p></div></a><a class="scope-item reveal" href="/projects/"><span>04</span><div><small>LAND</small><h3>Long-term<br>opportunity</h3><p>Strategic acquisition, land banking, forestry and renewable energy opportunities.</p></div></a></div></div></section>'''

def register_link(name,href):
 return f'<a href="{href}">{esc(name)}</a>' if href else f'<span>{esc(name)}</span>'
def portfolio_register():
 lanes=[
  ('01','RESIDENTIAL','Named communities',[('Lifestyle Enclave','/projects/lifestyle-enclave/'),('Two River, Mineville','/projects/two-river-mineville/'),('The Sables',''),('The Parks of Cole Harbour',''),('Crownvale',''),('Sarnaaz Valley',''),('The Amiora',''),('The Chamelias',''),('Novabella Retirement Homes',''),('The Aralias',''),('The Evangeline','')],'A current community, a planned community and residential names carried forward from earlier public materials.'),
  ('02','COMMERCIAL','Business opportunities',[('Wilmot',''),('Greenwood',''),('Lucasville','')],'Earlier concept material referenced plazas, mixed-use space, self-storage and medical-retail ideas.'),
  ('03','INDUSTRIAL','Working-space opportunities',[('Plexus Storage',''),('Lucasville',''),('Wilmot',''),('Greenwood',''),('Cornwallis Park','/projects/cornwallis-park/')],'Storage, logistics, industrial and mixed-use names recorded across earlier group materials.'),
  ('04','LAND & FUTURE GROWTH','Long-range possibilities',[('Cornwallis Park','/projects/cornwallis-park/'),('Clean Energy Initiative','')],'Strategic land, forestry and renewable-energy opportunities considered over a longer horizon.')]
 s='<section class="portfolio-register section" aria-labelledby="register-title"><div class="container"><div class="register-heading reveal"><div><span class="section-label">THE WIDER PICTURE</span><h2 id="register-title">One platform.<br><em>Many avenues.</em></h2></div><p>Detailed portfolio pages sit alongside earlier opportunity names preserved from the group’s previous public materials.</p></div><div class="register-grid">'
 for number,sector,title,names,description in lanes:
  s+=f'<article class="register-lane reveal"><span class="register-number">{number}</span><small>{sector}</small><h3>{title}</h3><div class="register-names">{"".join(register_link(name,href) for name,href in names)}</div><p>{description}</p></article>'
 return s+'</div><div class="register-key"><span><i></i> Detailed portfolio page</span><span><i></i> Earlier name or concept</span><p>Names shown here record earlier areas of interest. Inclusion does not mean every project is currently active, approved, owned or available.</p></div></div></section>'

def legacy_opportunities():
 return f'''<section class="legacy-opportunities section" aria-labelledby="legacy-opportunities-title"><div class="container">{heading('OPPORTUNITY REGISTER','Earlier concepts,<br><em>carried forward carefully.</em>','The previous website contained commercial and industrial ideas that were not supported by complete project records. They are preserved here as clearly qualified concepts.')}</div><div class="opportunity-feature container reveal"><button class="opportunity-visual" data-photo="wilmot-concept.webp" data-photo-title="Wilmot commercial and storage concept" data-photo-note="Legacy concept visualization · Not an approved plan" aria-label="Enlarge the Wilmot commercial and storage concept">{image('wilmot-concept.webp','Wilmot commercial plaza and self-storage concept visualization')}<span class="image-note">LEGACY CONCEPT · WILMOT</span></button><div class="opportunity-copy"><span class="section-label">COMMERCIAL CONCEPT</span><h3>Wilmot</h3><p>Earlier material described a mixed-use commercial and self-storage opportunity positioned for growth. The surviving concept visual labels a commercial plaza and self-storage. No address, unit program, approval or delivery date was published.</p><div class="opportunity-meta"><span>Earlier status</span><strong>Concept only</strong></div>{button('Discuss a commercial site','/contact/?subject=Commercial%20and%20industrial%20opportunities')}</div></div><div class="opportunity-feature container reveal reverse"><div class="opportunity-copy"><span class="section-label">COMMERCIAL CONCEPT</span><h3>Lucasville</h3><p>The earlier site paired Lucasville with a medical-retail concept and a “coming soon” message. Visible labels included a pharmacy, dental centre, medical centre, veterinary use, day care and other retail tenancies. These are illustrative labels, not lease or opening commitments.</p><div class="opportunity-meta"><span>Earlier status</span><strong>Coming soon concept</strong></div>{button('Ask about Lucasville','/contact/?subject=Lucasville%20opportunity')}</div><button class="opportunity-visual" data-photo="lucasville-concept.webp" data-photo-title="Lucasville medical-retail concept" data-photo-note="Legacy concept visualization · Tenant labels are illustrative" aria-label="Enlarge the Lucasville medical-retail concept">{image('lucasville-concept.webp','Illustrative Lucasville medical-retail concept with labelled tenancies')}<span class="image-note">LEGACY CONCEPT · LUCASVILLE</span></button></div><div class="legacy-band container"><div><span class="section-label">ADDITIONAL EARLIER NAMES</span><h3>Greenwood &amp; Plexus Storage</h3></div><p>Earlier materials described Greenwood as a commercial project in Lucasville and Plexus Storage as a storage platform across multiple Nova Scotia locations. The relationship between Greenwood and Lucasville, current ownership, operating status and facility locations were not published and require confirmation.</p>{button('Speak with the team','/contact/?subject=Greenwood%20and%20Plexus%20Storage')}</div></section>'''

def services():
 entries=[('Residential development','Homes for the way we live.','From multi-unit apartments to master-planned neighbourhoods, we bring homes, shared spaces and community needs into the same conversation.','lifestyle-back.webp','/projects/?sector=Residential','Explore communities'),('Commercial & industrial','Spaces for the way we work.','Commercial opportunities in Wilmot, Greenwood and Lucasville, alongside industrial, logistics and Plexus Storage interests across Nova Scotia.','lifestyle-drone.webp','/contact/?subject=Commercial%20and%20industrial%20opportunities','Discuss an opportunity'),('Land & future growth','Potential for what comes next.','Strategic land acquisition, forestry and phased development shaped by a long-term perspective on each site and the community around it.','cornwallis.webp','/projects/cornwallis-park/','Explore Cornwallis Park')]
 s=f'<section class="services section container" id="services">{heading("OUR SERVICES","A connected approach<br>to the places we build.","Homes, workplaces and future opportunities. One considered vision, from the ground up.")}<div class="service-panels">'
 for i,(name,title,desc,img,url,cta) in enumerate(entries):
  s+=f'''<article class="service-panel {'active' if i==0 else ''}"><div class="service-back">{image(img,'Plexus portfolio '+('construction photograph' if i==1 else 'concept imagery'))}</div><button class="service-selector" aria-expanded="{'true' if i==0 else 'false'}" aria-controls="service-content-{i}"><span class="service-number">0{i+1}</span><h3>{name}</h3><span aria-hidden="true">↗</span></button><div class="service-content" id="service-content-{i}" {'inert' if i else ''}><h4>{title}</h4><p>{desc}</p>{button(cta,url,'light')}<small>{'Lifestyle Enclave construction photograph' if i==1 else 'Plexus portfolio architectural concept'}</small></div></article>'''
 return s+'</div></section>'
def featured():
 selected=[DATA[1],DATA[2],DATA[3]]
 s=f'<section class="featured" id="projects"><div class="container section">{heading("SELECTED OPPORTUNITIES","A portfolio<br>with <em>range.</em>","Current communities, planning opportunities and the next generation of Plexus projects.")}</div><div class="project-journey"><div class="journey-sticky"><div class="journey-window"><div class="journey-track">'
 for p in selected:s+=f'''<article class="journey-card">{image(p['image'],p['imageNote']+' of '+p['title'])}<span class="journey-note">{p['imageNote']}</span><div class="journey-glass"><span class="journey-scale">{p['scale']}</span><h3>{p['title']}</h3><p>{p['location']}</p>{button('Explore','/projects/'+p['slug']+'/','light')}</div></article>'''
 return s+f'''</div></div><div class="journey-controls"><button data-slide="0" aria-label="Show {esc(selected[0]['title'])}" aria-current="true">01</button><span class="journey-progress"><i></i></span><button data-slide="1" aria-label="Show {esc(selected[1]['title'])}">02</button><button data-slide="2" aria-label="Show {esc(selected[2]['title'])}">03</button><span class="journey-hint">Scroll to explore →</span></div></div></div></section>'''
def film():return f'''<section class="film-section living-section"><div class="film-scroll"><div class="film-sticky"><div class="film-frame">{image('lifestyle-lobby.webp','Lifestyle Enclave lobby, architectural rendering')}<div class="film-overlay"></div><div class="film-copy">{label('LIFESTYLE ENCLAVE')}<h2>The life<br><em>inside.</em></h2><p>More than somewhere to live.<br>Somewhere to belong.</p><button class="button light" data-photo="lifestyle-lobby.webp" data-photo-title="Inside Lifestyle Enclave" data-photo-note="Lifestyle Enclave · Architectural rendering"><span>Look inside</span>{arrow()}</button></div><span class="image-note">ARCHITECTURAL RENDERING</span></div></div></div></section>'''

def partners():return f'''<section class="partners section container">{heading('BETTER TOGETHER','Shared ambition.<br>Lasting relationships.','Great development brings the site, the community and the long-term opportunity into one conversation.')}<div class="partner-grid"><article class="partner-card reveal"><span class="partner-symbol" aria-hidden="true">01</span><p>A disciplined approach to development, supported by clear priorities and a relationship built around long-term value.</p><div><h3>Capital partners</h3><span>Investing with perspective</span></div></article><article class="partner-card reveal"><span class="partner-symbol" aria-hidden="true">02</span><p>A professional process, considered planning and open communication about the potential of your property.</p><div><h3>Brokers & landowners</h3><span>Seeing what comes next</span></div></article><a class="partner-card reveal" href="/community/"><span class="partner-symbol" aria-hidden="true">03</span><p>Collaboration with municipalities, local trades and the people who understand a place and its everyday needs.</p><div><h3>Our communities</h3><span>Building stronger connections</span></div></a></div></section>'''
def opening():return '<div class="page-intro" aria-hidden="true"><div class="intro-signature"><div class="intro-word">Plexus</div><p class="intro-descriptor">Development Group</p></div><span class="intro-origin">Development · Investment · Land</span><button tabindex="-1" class="intro-skip">Enter site</button></div>'

def mandate():return '''<section class="mandate" id="services" aria-labelledby="mandate-title" data-scene="0"><div class="mandate-sticky"><div class="mandate-frame container"><div class="mandate-top"><span class="section-label">WHAT WE BUILD</span><span class="mandate-count">01 / 04</span></div><div class="mandate-word" aria-hidden="true">Build.</div><div class="mandate-copy"><h2 id="mandate-title">One platform.<br><em>Many ways to build value.</em></h2><p>From housing to employment space and strategic land, Plexus considers how each opportunity can serve a wider regional future.</p></div><div class="mandate-scenes"><article class="mandate-scene" data-mandate-scene="0"><span>01</span><div><small>RESIDENTIAL COMMUNITIES</small><h3>Places to live<br>and belong.</h3><p>Multi-unit housing, neighbourhoods and senior living shaped around the way Nova Scotia is growing.</p><a class="mandate-link" href="/residential/">Explore residential <span aria-hidden="true">↗</span></a></div></article><article class="mandate-scene" data-mandate-scene="1"><span>02</span><div><small>COMMERCIAL &amp; MIXED USE</small><h3>Space for local<br>economies.</h3><p>Plazas and mixed-use opportunities aligned with population, employment and infrastructure.</p><a class="mandate-link" href="/commercial/">Explore commercial <span aria-hidden="true">↗</span></a></div></article><article class="mandate-scene" data-mandate-scene="2"><span>03</span><div><small>INDUSTRIAL &amp; LOGISTICS</small><h3>Capacity that<br>keeps things moving.</h3><p>Industrial parks, warehousing, self-storage and logistics assets built for practical demand.</p><a class="mandate-link" href="/industrial/">Explore industrial <span aria-hidden="true">↗</span></a></div></article><article class="mandate-scene" data-mandate-scene="3"><span>04</span><div><small>LAND &amp; FUTURE GROWTH</small><h3>Potential viewed<br>over generations.</h3><p>Strategic acquisition, land banking, forestry and renewable energy opportunities considered over the long term.</p><a class="mandate-link" href="/projects/cornwallis-park/">Explore Cornwallis Park <span aria-hidden="true">↗</span></a></div></article></div><div class="mandate-nav" aria-label="Development sectors"><button data-mandate-target="0" aria-current="true"><span>01</span>Residential</button><button data-mandate-target="1"><span>02</span>Commercial</button><button data-mandate-target="2"><span>03</span>Industrial</button><button data-mandate-target="3"><span>04</span>Land</button></div><div class="mandate-progress" aria-hidden="true"><i></i></div></div></div></section>'''

def leadership():return f'''<section class="leadership section" id="leadership"><div class="leadership-layout container"><figure class="leadership-portrait reveal">{image('pavneet-singh.webp','Pavneet Singh, real estate developer in Halifax')}<figcaption>HALIFAX, NOVA SCOTIA</figcaption></figure><div class="leadership-copy reveal">{label('DEVELOPMENT LEADERSHIP')}<h2>Local perspective.<br><em>Long-term intent.</em></h2><p>Pavneet Singh brings a Halifax-based perspective across real estate advisory, investment opportunities and land development. Within Plexus, his focus is on relationships, local market understanding and disciplined project growth.</p><div class="leader-name"><strong>Pavneet Singh</strong><span>Real Estate Developer · Halifax, Nova Scotia</span></div><a class="text-link" href="/about/">Meet Plexus <span aria-hidden="true">↗</span></a></div></div></section>'''

def architecture():return f'''<section class="architecture" id="perspective"><div class="architecture-sticky"><div class="architecture-top container"><span class="section-label">01 / A DIFFERENT PERSPECTIVE</span><span class="architecture-location">Upper Hammonds Plains, Nova Scotia</span></div><div class="architecture-word" aria-hidden="true">Belong.</div><div class="architecture-copy"><div data-chapter="0"><h2>Every place starts<br>with <em>a possibility.</em></h2><p>A thoughtful vision for the way we live.</p></div><div data-chapter="1" hidden><h2>A considered arrival.<br><em>A new beginning.</em></h2><p>Lifestyle Enclave. 102 homes, one connected community.</p></div><div data-chapter="2" hidden><h2>Life happens<br><em>in the details.</em></h2><p>Spaces to meet, unwind and feel at home.</p></div></div><div class="building-stage"><div class="building-plane"><img class="building-context" src="/assets/lifestyle-arrival.webp" alt="" width="2048" height="1152" loading="lazy"><img class="building-cutout" src="/assets/lifestyle-arrival.webp" alt="Lifestyle Enclave north elevation, original architectural rendering" width="2048" height="1152" loading="lazy"></div></div><button class="architecture-interior" data-photo="lifestyle-lobby.webp" data-photo-title="Inside Lifestyle Enclave" data-photo-note="Lifestyle Enclave · Architectural rendering" aria-label="Enlarge the Lifestyle Enclave lobby rendering">{image('lifestyle-lobby.webp','Lifestyle Enclave lobby, architectural rendering')}<span>A place to connect <i aria-hidden="true">↗</i></span></button><div class="architecture-bottom container"><div class="architecture-tabs" aria-label="Architectural perspectives"><button data-perspective="0" aria-current="true"><span>01</span> Vision</button><button data-perspective="1"><span>02</span> Architecture</button><button data-perspective="2"><span>03</span> Inside</button></div><a class="text-link" href="/projects/lifestyle-enclave/">Discover Lifestyle Enclave <span aria-hidden="true">↗</span></a><span class="architecture-credit">ARCHITECTURAL RENDERINGS</span></div></div></section>'''
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
    <p class="estate-overline estate-reveal">DEVELOPMENT · INVESTMENT · LAND</p>
    <h1 id="estate-title"><span class="estate-title-line"><span class="estate-reveal">Building tomorrow’s</span></span><span class="estate-title-line"><span class="estate-reveal"><em>Nova Scotia.</em></span></span></h1>
    <p class="estate-description estate-reveal">Plexus brings land, capital and execution together to create lasting value across Nova Scotia.</p><a class="estate-link estate-reveal" href="/projects/">Explore the projects <span aria-hidden="true">↗</span></a>
  </div>
  <div class="estate-foot estate-reveal">
    <div class="estate-project"><small>Halifax, Nova Scotia</small><span>Plexus Development Group</span><small>Atlantic Canada outlook</small></div>
    <a class="estate-discover" href="#introduction"><span class="estate-down" aria-hidden="true">↓</span><span>Discover Plexus</span></a>
    <span class="estate-credit">Halifax waterfront · Nova Scotia</span>
  </div>
</section>'''
def home():return f'''{opening()}{residential_hero()}<section class="introduction section container" id="introduction"><div class="intro-overline"><span class="section-label">THE PLEXUS PLATFORM</span><span class="intro-index">HALIFAX, NOVA SCOTIA</span></div><div class="intro-layout"><h2>One group.<br><em>A wider vision.</em></h2><div><p>We develop more than homes. Plexus brings residential communities, commercial opportunities, industrial capacity and strategic land into one long-term platform.</p><p>Every project begins with its setting, its economic role and the people it can serve.</p>{button('Meet the group','/about/')}</div></div></section>{mandate()}{group_scope()}{featured()}{development_approach()}<section class="listings section container">{heading('THE PORTFOLIO','Different places.<br><em>One long view.</em>','Explore current communities, planning opportunities and the wider residential pipeline across Nova Scotia.')}<div class="listing-grid">{''.join(card(p) for p in DATA)}</div><div class="center-action">{button('Explore all projects','/projects/')}</div></section>{leadership()}{partners()}{faq()}'''

def development_approach():return f'''<section class="development-story section" aria-labelledby="development-title"><div class="container development-layout"><div class="development-heading reveal">{label('THE LONG VIEW')}<h2 id="development-title">Good places.<br><em>Considered from <br>the beginning.</em></h2><p>Land acquisition, investment and development. Three connected disciplines, shaped by one ambition: lasting value for the places we call home.</p><a class="text-link" href="/about/">Our perspective <span aria-hidden="true">↗</span></a></div><div class="development-chapters"><article class="development-chapter reveal"><span class="chapter-number">01</span><div><h3>See the wider picture.</h3><p>Every opportunity begins with its setting. We consider the relationship between a site, local housing needs, business activity and the infrastructure around it.</p><span class="chapter-note">Land &amp; opportunity</span></div></article><article class="development-chapter reveal"><span class="chapter-number">02</span><div><h3>Build strong connections.</h3><p>Local knowledge matters. Our approach brings municipalities, trades, suppliers and community priorities into the development conversation.</p><span class="chapter-note">People &amp; place</span></div></article><article class="development-chapter reveal"><span class="chapter-number">03</span><div><h3>Think beyond today.</h3><p>Measured growth and considered land use guide the long view. We look at how homes, workplaces and future phases can contribute to a community over time.</p><span class="chapter-note">Investment &amp; lasting value</span></div></article></div></div></section>'''

def everyday_life():return f'''<section class="everyday-life section container" aria-labelledby="everyday-title"><div class="everyday-intro reveal">{label('LIFE AT LIFESTYLE ENCLAVE')}<h2 id="everyday-title">Room for the<br><em>everyday.</em></h2><p>A quieter setting in Upper Hammonds Plains. Thoughtful spaces for the routines, company and small moments that make a place feel like home.</p></div><div class="everyday-layout"><figure class="everyday-image reveal">{image('lifestyle-front.webp','Garden-facing elevation of Lifestyle Enclave, architectural rendering')}<figcaption><span>Lifestyle Enclave</span><span>Architectural rendering</span></figcaption></figure><div class="everyday-details"><article class="everyday-feature reveal"><span>AT HOME</span><h3>A little more room.</h3><p>One-bedroom + den and two-bedroom + den layouts offer flexibility for daily life, with in-suite laundry and ducted heating and air conditioning.</p></article><article class="everyday-feature reveal"><span>IN GOOD COMPANY</span><h3>Spaces that bring us together.</h3><p>A fitness centre, resident lounge and community room are planned as shared places to stay active, spend time with neighbours and unwind.</p></article><article class="everyday-feature reveal"><span>BEYOND THE FRONT DOOR</span><h3>A connection to the outdoors.</h3><p>Green spaces form part of the community vision, with access to Bedford, Sackville and Halifax for the things you need further afield.</p></article><a class="text-link" href="https://lifestyleenclave.ca/" target="_blank" rel="noopener noreferrer">Explore life at the Enclave <span aria-hidden="true">↗</span></a><p class="everyday-note">Planned features shown. Confirm amenities, availability and move-in timing with the leasing team.</p></div></div></section>'''

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
 return f'''<section class="structure section" id="structure" aria-labelledby="structure-heading"><div class="container">{heading('GROUP STRUCTURE','How the group<br><em>is organised.</em>','The previous site published a group-structure graphic. It is rebuilt here as a readable chart, with its corrections disclosed rather than quietly applied.')}<div class="chart-root reveal"><span class="chart-root-label">{esc(SD.ROOT)}</span></div><div class="chart-stem" aria-hidden="true"></div><div class="chart-branches">{branches}</div><div class="chart-notes reveal"><h3>About this chart</h3><ul>{notes}</ul><p>Every name shown as an earlier name was published without supporting project detail. Inclusion records the group&rsquo;s earlier public record. It does not mean each project is currently active, approved or owned.</p></div></div></section>'''


def asset_classes():
 items=''.join(f'<li>{esc(a)}</li>' for a in SD.ASSET_CLASSES)
 return f'''<section class="asset-classes section"><div class="container"><div class="asset-classes-inner reveal"><div>{label('ASSET CLASSES')}<h2>The full range<br>of the platform.</h2></div><div><p>The previous projects page named these asset classes. They describe what the group considers, not what is currently active.</p><ul>{items}</ul></div></div><p class="map-note">{esc(SD.LOCATION_MAP_NOTE)}</p></div></section>'''

# --- Sector page sections --------------------------------------------------
def sector_statement(kicker,title,body):
 return f'<section class="sector-statement section container"><div>{label(kicker)}<h2>{title}</h2></div><p>{body}</p></section>'

def sector_types(kicker,title,desc,items):
 cards=''.join(f'<article class="sector-type reveal"><span>{n}</span><h3>{esc(t)}</h3><p>{esc(d)}</p></article>' for n,t,d in items)
 return f'<section class="sector-types section container">{heading(kicker,title,desc)}<div class="sector-type-grid">{cards}</div></section>'

def sector_approach(kicker,title,items):
 cards=''.join(f'<article class="sector-approach-item reveal"><h3>{esc(t)}</h3><p>{esc(d)}</p></article>' for t,d in items)
 return f'<section class="sector-approach section"><div class="container">{heading(kicker,title,"Stated principles from earlier company material. They are carried forward as direction, not as verified performance.")}<div class="sector-approach-grid">{cards}</div></div></section>'

def sector_project_list(entries,empty_note=''):
 out='<div class="sector-projects">'
 for e in entries:
  if e['image']:
   visual=(f'<button class="sector-visual" data-photo="{e["image"]}" data-photo-title="{esc(e["name"])} concept" data-photo-note="{esc(e["note"])}" '
    f'aria-label="Enlarge the {esc(e["name"])} concept">{image(e["image"],e["alt"])}<span class="image-note">CONCEPT · {esc(e["name"].upper())}</span></button>')
  else:
   visual='<div class="sector-visual is-empty" aria-hidden="true"><span>No verified project imagery<br>was ever published.</span></div>'
  name=f'<a href="{e["href"]}">{esc(e["name"])}</a>' if e.get('href') else esc(e['name'])
  note=f'<p class="sector-project-note">{esc(e["note"])}</p>' if e.get('note') else ''
  cta=button('Open the project page',e['href']) if e.get('href') else ''
  out+=(f'<article class="sector-project reveal">{visual}'
   f'<div class="sector-project-copy"><div class="sector-project-head"><h3>{name}</h3>'
   f'<span class="sector-status">{esc(e["status"])}</span></div>'
   f'<p class="sector-project-summary">{esc(e["summary"])}</p><p>{esc(e["detail"])}</p>{note}{cta}</div></article>')
 out+='</div>'
 if empty_note: out+=f'<p class="sector-empty-note">{esc(empty_note)}</p>'
 return out

def sector_work(kicker,title,desc,entries,empty_note=''):
 return f'<section class="sector-work section container">{heading(kicker,title,desc)}{sector_project_list(entries,empty_note)}</section>'

def sector_pipeline(kicker,title,desc,detail_projects,earlier,note):
 cards=''.join(card(p) for p in detail_projects)
 tags=''.join(f'<span>{esc(n)}</span>' for n in earlier)
 return f'<section class="sector-pipeline section container">{heading(kicker,title,desc)}<div class="listing-grid">{cards}</div><div class="earlier-names reveal"><h3>Named in earlier public material</h3><div class="earlier-tags">{tags}</div><p>{esc(note)}</p></div></section>'

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
 titles=[p['title'] for p in detailed]
 earlier=[n for n,h,_ in SD.BRANCHES[0]['items'] if not h and n not in titles]
 return (pagehero(*SD.RESIDENTIAL_HERO)
  +sector_statement('THE CASE FOR MORE HOUSING','Housing demand is<br><em>arithmetic, not hype.</em>',SD.RESIDENTIAL_INTRO)
  +sector_types('WHAT THE GROUP BUILDS','Every housing type,<br><em>not a single template.</em>','The previous residential page described each of these development types. They are carried as descriptions of focus, not as a claim that every type is currently active.',SD.RESIDENTIAL_TYPES)
  +sector_approach('HOW THE GROUP APPROACHES IT','Livability over<br><em>density alone.</em>',SD.RESIDENTIAL_APPROACH)
  +sector_pipeline(*SD.RESIDENTIAL_PIPELINE_HEADING,detailed,earlier,SD.RESIDENTIAL_PIPELINE_NOTE)
  +sector_hub('/residential/','Where residential sits<br>in the wider group.','Housing is one branch of a connected platform. These are the pages that show how it relates to the rest of the group.')
  +faq())

def commercial_page():
 return (pagehero(*SD.COMMERCIAL_HERO)
  +sector_statement('ENABLING GROWTH','Commercial space is<br><em>infrastructure.</em>',SD.COMMERCIAL_INTRO)
  +sector_types('WHAT THE GROUP BUILDS','Every commercial format,<br><em>from plaza to plaza.</em>','The previous commercial page and projects page named these commercial and hospitality formats. They describe what the group considers, not what is currently active.',SD.COMMERCIAL_TYPES)
  +sector_approach('HOW THE GROUP APPROACHES IT','Practical space,<br><em>blended districts.</em>',SD.COMMERCIAL_APPROACH)
  +sector_work('THE COMMERCIAL RECORD','Earlier concepts,<br><em>clearly framed.</em>','These are the commercial and mixed-use opportunities named across the previous site and its group-structure graphic. Where the source conflicted with itself, the conflict is stated rather than resolved.',SD.COMMERCIAL_PROJECTS,
    'The previous commercial page also carried a generic mixed-use concept showing 100 townhouses, a hotel, six-storey apartments and a store. It is not tied to a named project and is not reproduced here.')
  +sector_hub('/commercial/','Where commercial sits<br>in the wider group.','Commercial work is planned alongside the housing and employment land that supports it, not in isolation from it.')
  +faq())

def industrial_page():
 return (pagehero(*SD.INDUSTRIAL_HERO)
  +sector_statement('EMPLOYMENT LAND','A working region needs<br><em>somewhere to work.</em>',SD.INDUSTRIAL_INTRO)
  +sector_types('WHAT THE GROUP BUILDS','Every industrial format,<br><em>from park to pallet.</em>','The previous industrial page and projects page named these industrial, warehousing and storage formats. They describe what the group considers, not what is currently active.',SD.INDUSTRIAL_TYPES)
  +sector_approach('HOW THE GROUP APPROACHES IT','Space that<br><em>keeps working.</em>',SP.INDUSTRIAL_APPROACH)
  +sector_work('THE INDUSTRIAL RECORD','Names carried forward,<br><em>honestly labelled.</em>','These are the industrial, storage and logistics opportunities named across the previous site. Most were published as names only, with no facility list, address or operating status.',SD.INDUSTRIAL_PROJECTS,
    'Plexus Storage was the only dedicated industrial name on the previous site. It was described as executed across multiple Nova Scotia locations, with no location list, facility count or operating status published.')
  +sector_hub('/industrial/','Where industrial sits<br>in the wider group.','Industrial and storage capacity is the piece most often overlooked in a growth story, and the piece most directly tied to job creation.')
  +faq())

def community_page():
 pillars=[('01','HOUSING STABILITY','Homes that support daily life','Earlier materials described a focus on affordability, accessibility and long-term sustainability in residential development.'),('02','LOCAL ECONOMIC GROWTH','Work and regional activity','Construction, contractor engagement, partnerships and real-estate investment are described as ways to support local economic activity.'),('03','RESPONSIBLE LAND','Land use that belongs','Thoughtful land use, community integration and infrastructure planning are presented as long-term priorities.'),('04','FINANCIAL AWARENESS','Knowledge that creates confidence','Earlier materials referenced financial literacy, homeownership awareness and investment guidance for newcomers and residents.')]
 future=[('Affordable &amp; workforce housing','A stated ambition to respond to housing shortages while protecting quality, connectivity and affordability.'),('Community-integrated development','Future phases are described as combining residential, commercial and everyday lifestyle infrastructure.'),('Local partnerships','Closer collaboration with municipalities, community organizations, trades and local stakeholders.'),('Sustainable practice','Renewable energy, responsible building practices and resilient infrastructure described as priorities for upcoming work.')]
 p='<section class="community-pillars section container">'+''.join(f'<article class="community-pillar reveal"><span>{number}</span><small>{kicker}</small><h3>{title}</h3><p>{text}</p></article>' for number,kicker,title,text in pillars)+'</section>'
 f='<section class="community-future section container">'+''.join(f'<article class="future-row reveal"><span>{str(i).zfill(2)}</span><h3>{title}</h3><p>{text}</p></article>' for i,(title,text) in enumerate(future,1))+'</section>'
 return pagehero('COMMUNITY','Built around<br>the people who call it home.','Plexus sees community as a long-term relationship: homes, local work, responsible land use and partnerships that continue after a development is finished.')+f'''<section class="community-statement section container"><div><span class="section-label">ROOTED IN PLACE</span><h2>More than a building.<br><em>A lasting relationship.</em></h2></div><div><p>Responsible development should strengthen the communities around it. That means considering affordability, local economic activity, land use, infrastructure and the people who know a place best.</p><p>The themes on this page consolidate the group’s earlier community material. Where programme details were not published, they are identified as earlier statements and should be confirmed directly with Plexus.</p></div></section>'''+p+f'''<section class="community-record section" aria-labelledby="community-record-title"><div class="container"><div class="record-heading"><span class="section-label">AN HONEST COMMUNITY RECORD</span><h2 id="community-record-title">Earlier stories,<br><em>clearly framed.</em></h2></div><div class="record-grid"><article><span>01</span><h3>Canadian Homeless Support &amp; Development Foundation</h3><p>Earlier public materials identified the Canadian Homeless Support &amp; Development Foundation, abbreviated CHSDF, within Plexus’s community story. Contribution dates, amounts, events and photographs were not published and are being confirmed before a fuller account is presented.</p><small>COMMUNITY ORGANIZATION NAMED IN EARLIER MATERIALS</small></article><article><span>02</span><h3>Financial and housing education</h3><p>Earlier copy described participation in financial literacy, homeownership awareness and investment guidance for newcomers and residents. The events, partners and outcomes were not documented publicly.</p><small>PROGRAMME DETAILS REQUIRE CONFIRMATION</small></article></div><div class="record-action"><p>Ask about a current community programme, partnership or initiative.</p>{button('Start a conversation','/contact/?subject=Community%20partnership')}</div></div></section>'''+f+'<section class="community-close section container"><span class="section-label">THE LONG VIEW</span><h2>Measure a development<br><em>by what it leaves behind.</em></h2>'+button('Discuss a community opportunity','/contact/?subject=Land%20and%20community%20partnership')+'</section>'

def projects_page():return pagehero('PROJECTS','Every project,<br>clearly placed.','Current communities, planning opportunities and the wider platform, with the group structure that connects them.')+f'''<section class="project-browser container"><aside class="filters" aria-label="Project filters"><div class="filter-heading"><h2>Find a project</h2><button class="clear-filters">Clear all</button></div><label>Search projects<input type="search" id="project-search" placeholder="Name or location"></label><label>Location<select id="filter-region"><option value="">All locations</option><option>Halifax region</option><option>Annapolis County</option><option>Nova Scotia</option></select></label><label>Development stage<select id="filter-status"><option value="">All stages</option><option>Under construction</option><option>Planned</option><option>Planning review</option><option>Pipeline</option></select></label><fieldset><legend>Project type</legend><label class="check-label"><input type="radio" name="sector" value="" checked>All projects</label><label class="check-label"><input type="radio" name="sector" value="Residential">Residential</label><label class="check-label"><input type="radio" name="sector" value="Land & mixed-use">Land &amp; mixed-use</label></fieldset><p>For commercial, industrial or storage opportunities, <a href="/contact/">speak with our team</a>.</p></aside><div class="project-results"><div class="result-bar"><span class="result-count" role="status">{len(DATA)} projects</span><span>Nova Scotia, Canada</span></div><div class="listing-grid">'''+''.join(card(p) for p in DATA)+'''</div><div class="empty-state" hidden><h2>No matching projects.</h2><p>Try another location or clear your filters to explore the full project list.</p><button class="button dark clear-filters">Reset filters</button></div></div></section>'''+group_chart()+asset_classes()+portfolio_register()+legacy_opportunities()+sector_hub('/projects/','Explore by<br><em>sector.</em>','Every name on this page belongs to a branch of the platform. Each branch has its own page with the full record from the previous site.')+faq()
def about_page():return pagehero('ABOUT PLEXUS','A vision beyond<br>the building.','We are a Halifax-based development, investment and land acquisition company focused on the places people live, work and grow.')+f'''<div class="about-cover container">{image('halifax-waterfront.webp','Halifax waterfront seen across the harbour')}<span class="image-note">HALIFAX WATERFRONT · NOVA SCOTIA</span></div><div class="sector-strip container"><span>RESIDENTIAL</span><span>COMMERCIAL</span><span>INDUSTRIAL</span><span>LAND</span></div><section class="about-story section container">{heading('THE GROUP','Good places begin<br>with a greater purpose.','Responsible development. Disciplined execution. Value that lasts.')}<div class="story-columns"><p>From places to call home to spaces where businesses grow, Plexus takes the long view. We connect thoughtful planning, investment and land strategy with a particular focus on Halifax and Nova Scotia’s growth communities.</p><div><h3>Our perspective</h3><p>Each site sits within a wider picture of housing, business activity and infrastructure. Clear priorities help us understand how a development can contribute over time.</p><h3>Our commitment</h3><p>Community-aligned planning, local partnerships and disciplined land use guide our approach. Municipalities, trades and people who understand a place are part of the conversation.</p></div></div></section>{group_scope()}<section class="about-values section container"><div class="values-photo">{image('cornwallis.webp','Cornwallis Park long-term development concept')}<span class="image-note">CORNWALLIS PARK · CONCEPT PLAN</span></div><div>{label('BUILT FOR THE LONG VIEW')}<h2>Value measured<br>beyond the building.</h2><div class="value-item"><span>01</span><div><h3>Community aligned</h3><p>Housing, business space and infrastructure are considered in relation to the people and region a project can serve.</p></div></div><div class="value-item"><span>02</span><div><h3>Responsible by design</h3><p>Considered land use, resilient infrastructure and opportunities for renewable energy integration inform future development.</p></div></div><div class="value-item"><span>03</span><div><h3>Disciplined growth</h3><p>Financial discipline, lasting relationships and measured execution shape our decisions.</p></div></div>{button('Let’s talk','/contact/')}</div></section>{leadership()}{partners()}{faq()}'''
def contact_page():return pagehero('CONTACT US','Let’s start a conversation.','Tell us about a promising site, development opportunity or shared ambition.')+f'''<section class="contact-layout container" id="contact"><div class="contact-intro"><h2>Good places start<br>with the right people.</h2><p>Connect with our Halifax team to discuss land, investment, a community or a development partnership.</p><div class="contact-photo">{image('halifax-waterfront.webp','Halifax waterfront seen across the harbour')}<span class="image-note">HALIFAX WATERFRONT · NOVA SCOTIA</span></div><a href="mailto:info@plexusdevelopmentgroup.ca">info@plexusdevelopmentgroup.ca</a><a href="tel:+19028099399">+1 902 809 9399</a><address>3845 Joseph Howe Drive, Suite 100<br>Halifax, Nova Scotia</address><div class="contact-hours"><span>Office hours</span><strong>Monday–Friday · 9am–5pm</strong></div></div><form class="enquiry-form"><label>Full name <span>*</span><input name="name" autocomplete="name" placeholder="Your full name" required maxlength="120"></label><label>Email address <span>*</span><input name="email" type="email" autocomplete="email" placeholder="Your email address" required maxlength="200"></label><label>Subject<input name="subject" placeholder="What would you like to discuss?" maxlength="180"></label><label>Message <span>*</span><textarea name="message" rows="5" placeholder="Tell us a little about your enquiry" required maxlength="3000"></textarea></label><button class="button dark" type="submit"><span>Prepare enquiry</span>{arrow()}</button><p class="form-note">Opens your email app with a draft for you to review and send.</p><p class="form-status" role="status"></p></form></section>{faq()}'''
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
 return f'''<section class="detail-heading container"><a class="breadcrumb" href="/projects/">← All projects</a><div><div><span class="detail-status">{p['status']}</span><h1>{p['title']}</h1><p>{p['location']}</p></div><strong>{p['scale']}</strong></div></section><div class="detail-gallery container {'single' if len(p['gallery'])==1 else ''}">{gallery}</div><section class="detail-body container"><div class="detail-main"><h2>{detail_heading}</h2><p class="detail-lead">{p['lead']}</p><p>{p['description']}</p><p>{p['detail']}</p><div class="detail-facts">{''.join(f'<div><span>{a}</span><strong>{b}</strong></div>' for a,b in p['facts'])}</div><h2>{feature_heading}</h2><ul class="amenity-list">{''.join(f'<li><span aria-hidden="true">{"·" if p.get("conceptSource") else "✓"}</span>{f}</li>' for f in p['features'])}</ul>{use_groups}{legacy_names}<p class="project-note">{p['note']}</p>{('<button class="button outline" data-open-film><span>Watch the construction film</span>'+arrow()+'</button>') if p['slug']=='lifestyle-enclave' else ''}</div><aside class="enquiry-card"><h2>Want to know more?</h2><p>Let’s talk about {p['title']} and the next step for you.</p>{button('Enquire about this project','/contact/?subject='+p['slug'])}{button('Visit Lifestyle Enclave',p['external'],'outline') if p.get('external') else ''}<a href="tel:+19028099399">+1 902 809 9399</a><small>Project details and availability are confirmed directly by the team.</small></aside></section><section class="related section container">{heading('MORE TO EXPLORE','A broader perspective.','Discover more from the Plexus project list.')}<div class="listing-grid three">{''.join(card(x) for x in DATA[:3] if x['slug']!=p['slug'])}</div></section>{faq()}'''
def privacy():return pagehero('WEBSITE PRIVACY','Your enquiry.<br>Your choice.','How this website handles the information you choose to share.')+'''<section class="privacy-copy container section"><h2>Enquiries</h2><p>This website’s contact form prepares an email draft in your chosen email app. Completing the form does not send information through a website form service. You review and send the draft yourself. When you email Plexus, your email provider and the receiving email system process the message.</p><h2>Website functions</h2><p>The website uses locally hosted fonts, images and video. It does not include third-party advertising analytics in its authored code. Your browser keeps session settings to remember the opening animation and your motion preference during a visit. Hosting and access providers may process technical information needed to deliver and secure the site.</p><h2>Other websites</h2><p>Links to Lifestyle Enclave or other external websites lead to services governed by their own privacy practices.</p><h2>Contact</h2><p>For questions about information you have sent to Plexus, contact <a href="mailto:info@plexusdevelopmentgroup.ca">info@plexusdevelopmentgroup.ca</a>.</p></section>'''
def asset_url(name):return '/'+name+'?v='+hashlib.sha256((OUT/name).read_bytes()).hexdigest()[:12]
# One flag controls search indexing for the whole site. Leave it False for the
# private review build. Set True only when a public domain launch is approved.
LAUNCH = False
SITE_ORIGIN = 'https://plexus-development.criyx-ai.chatgpt.site'
SITE_NAME = 'Plexus Development Group'

ROUTES = [
    ('', 'Building tomorrow\u2019s Nova Scotia', 'Development, investment and land. A Halifax-based platform building residential, commercial and industrial value across Nova Scotia.'),
    ('projects', 'Projects', 'Every Plexus project with a detail page, the group-structure chart, and the commercial and industrial opportunities recorded in earlier public material.'),
    ('residential', 'Residential', 'Multi-unit buildings, single-family subdivisions, mixed communities, affordable-housing initiatives and senior living across Nova Scotia.'),
    ('commercial', 'Commercial', 'Commercial plazas, retail centres, shopping centres, hospitality and mixed-use opportunities, including the Wilmot, Lucasville and Greenwood records.'),
    ('industrial', 'Industrial', 'Industrial parks, warehousing, flex-industrial space, self-storage and logistics, including the Plexus Storage record.'),
    ('community', 'Community', 'How Plexus approaches housing stability, local economic growth, responsible land use and financial awareness, with an honest record of earlier material.'),
    ('contact', 'Contact us', 'Talk to the Plexus team about land, investment, a development partnership or a community opportunity in Nova Scotia.'),
    ('about', 'About Plexus', 'Plexus Development Group is a Nova Scotia development, investment and land acquisition platform. Our perspective, commitment and leadership.'),
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
    target.write_text(f'''<!doctype html><html lang="en-CA"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{esc(title)} | {SITE_NAME}</title><meta name="description" content="{esc(desc)}"><meta name="robots" content="{robots}"><meta name="theme-color" content="#132822"><link rel="canonical" href="{url}"><meta property="og:site_name" content="{SITE_NAME}"><meta property="og:locale" content="en_CA"><meta property="og:title" content="{esc(title)} | {SITE_NAME}"><meta property="og:description" content="{esc(desc)}"><meta property="og:type" content="website"><meta property="og:url" content="{url}"><meta property="og:image" content="{og_img}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Plexus Development Group — development, investment and land in Nova Scotia"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)} | {SITE_NAME}"><meta name="twitter:description" content="{esc(desc)}"><meta name="twitter:image" content="{og_img}"><link rel="icon" href="/assets/logo.png"><link rel="preload" href="/assets/serif.ttf" as="font" type="font/ttf" crossorigin><link rel="stylesheet" href="{asset_url('styles.css')}"><link rel="stylesheet" href="{asset_url('experience.css')}"><script src="{asset_url('script.js')}" defer></script></head><body id="top" class="{'home-page' if not route else 'inner-page'}">{header(active,home=not route)}<main id="main">{body}</main>{footer()}{dialogs(route=='projects/lifestyle-enclave')}</body></html>''')

def write_index_files():
    today = '2026-09-26'
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
write('', 'Building tomorrow\u2019s Nova Scotia', home(), 'home')
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
