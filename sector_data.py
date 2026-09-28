# Legacy content model for the Plexus sector pages.
#
# Every value here traces to the public capture of the previous site stored in
# research/legacy-site-capture-2026-09-25/. Nothing in this file may assert an
# approval, ownership, address, unit count, price or delivery date that the
# capture does not support. Concept and earlier-name material stays labelled.

# ---------------------------------------------------------------------------
# Group structure
# ---------------------------------------------------------------------------
# Reproduces the legacy hierarchy graphic. Two corrections are applied and
# disclosed on the page: the source spells one branch "Cornwalis", and Two
# River, Mineville is added because it carries a full project page.

ROOT = 'Plexus Group'

BRANCHES = [
    {
        'id': 'residential',
        'label': 'Residential',
        'summary': 'Multi-unit housing, subdivisions, mixed communities and senior living.',
        'items': [
            ('Lifestyle Enclave', '/projects/lifestyle-enclave/', 'Under construction'),
            ('Two River, Mineville', '/projects/two-river-mineville/', 'Planned'),
            ('The Sables', '', 'Earlier name'),
            ('The Parks of Cole Harbour', '', 'Earlier name'),
            ('Novabella Retirement Home', '', 'Earlier name'),
            ('The Crownvale', '', 'Earlier name'),
            ('The Aralias', '', 'Earlier name'),
            ('The Chamelias', '', 'Earlier name'),
            ('The Sarnaaz Valley', '', 'Earlier name'),
            ('The Amiora', '', 'Earlier name'),
        ],
    },
    {
        'id': 'commercial',
        'label': 'Commercial',
        'summary': 'Plazas, retail centres, hospitality, mixed use and service retail.',
        'items': [
            ('Cornwallis', '/projects/cornwallis-park/', 'Planning review'),
            ('Greenwood', '', 'Earlier name'),
            ('The Sables', '', 'Earlier name'),
            ('The Evangeline', '', 'Earlier name'),
        ],
    },
    {
        'id': 'industrial',
        'label': 'Industrial',
        'summary': 'Industrial parks, warehousing, flex space, self-storage and logistics.',
        'items': [
            ('Plexus Storage', '', 'Earlier name'),
            ('Lucasville', '', 'Earlier name'),
            ('Wilmot', '', 'Earlier name'),
            ('Greenwood', '', 'Earlier name'),
            ('Cornwallis Park', '/projects/cornwallis-park/', 'Planning review'),
        ],
    },
    {
        'id': 'energy',
        'label': 'Clean Energy Initiative',
        'summary': 'Renewable wind and solar integration considered alongside land strategy.',
        'items': [],
        # The source graphic shows this branch with no children. Its only
        # appearance in published copy is among the potential uses on the
        # Cornwallis concept, so the chart says exactly that.
        'note': 'No project detail, scope, location or timeline was ever published for this initiative. '
                'It appears in published copy only as wind and solar integration among the potential '
                'uses on the Cornwallis Park concept plan.',
    },
]

STRUCTURE_NOTES = [
    'The source graphic spells the commercial branch "Cornwalis". It is shown here as Cornwallis.',
    'The Sables appears under both residential and commercial in the source and is repeated rather than merged.',
    'Two River, Mineville is not in the source graphic. It is added because it has a full project page.',
    'The source places Cornwallis Park under industrial. The project page describes broader mixed-use potential.',
]

# ---------------------------------------------------------------------------
# Residential
# ---------------------------------------------------------------------------

RESIDENTIAL_HERO = (
    'RESIDENTIAL',
    'Homes built for<br>the way Nova Scotia lives.',
    'Residential building shaped around how people live, from multi-unit homes to single-family '
    'neighbourhoods and mixed communities across Nova Scotia.',
)

RESIDENTIAL_INTRO = (
    'Demand is not a forecast here. It is arithmetic: population growth and job inflows have '
    'consistently outpaced supply, and the region keeps absorbing households faster than it '
    'builds for them. Plexus responds to that gap with a focus on livability rather than '
    'density alone, and with housing types matched to real demand rather than to a single template.',
)

RESIDENTIAL_TYPES = [
    ('01', 'Multi-unit apartment buildings', 'Rental and ownership communities planned for everyday comfort, shared amenities and sustained long-term use rather than short-term turnover.'),
    ('02', 'Single-family subdivisions', 'Master-planned, low-density neighbourhoods with generous lots, green space and walkable internal routes.'),
    ('03', 'Mixed residential communities', 'Places that bring different housing types together with shared open space and everyday amenities.'),
    ('04', 'Affordable-housing initiatives', 'A stated focus area. Stated as an intention and not tied to a verified approved project.'),
    ('05', 'Senior and retirement living', 'Senior-living and retirement-oriented housing, including the Novabella Retirement Home name carried from earlier material.'),
]

RESIDENTIAL_SERVICES = [
    'Multi-unit apartment buildings',
    'Single-family subdivisions and mixed residential communities',
    'Affordable-housing initiatives',
    'Senior living and retirement-oriented housing',
]

RESIDENTIAL_APPROACH = [
    ('Livability in every plan', 'Livability is the measure, not units per acre alone. Green space, walking routes and everyday services sit alongside the home count.'),
    ('Built for long-term use', 'Earlier company material names financial discipline and conservative leverage as priorities, with an intent to hold assets for the long term rather than flip them.'),
    ('Learn from every build', 'Measured growth and repeatable systems allow each community to inform the next.'),
]

RESIDENTIAL_PIPELINE_HEADING = ('RESIDENTIAL BUILDING PROGRAM', 'Homes now, and<br><em>homes ahead.</em>',
                                'One community under construction, one master-planned community in planning, '
                                'and a wider set of names carried forward from earlier public material.')

RESIDENTIAL_PIPELINE_NOTE = (
    'The previous site described the residential pipeline as "several hundred units". That aggregate is '
    'not repeated here because no supporting project schedule was ever published. Individual project '
    'scope and timing must be confirmed directly with Plexus.'
)

# ---------------------------------------------------------------------------
# Commercial
# ---------------------------------------------------------------------------

COMMERCIAL_HERO = (
    'COMMERCIAL',
    'Spaces built<br>for business.',
    'Commercial building supports the local businesses, services and employment that help a region grow.',
)

COMMERCIAL_INTRO = (
    'Commercial building is part of a community’s infrastructure. It starts with what a place needs rather '
    'than speculation: somewhere to work, shop, gather and stay. Each format is considered alongside local homes, '
    'jobs and infrastructure.',
)

COMMERCIAL_TYPES = [
    ('01', 'Commercial plazas and retail centres', 'Neighbourhood-serving retail supported by the residential density around it.'),
    ('02', 'Shopping centres and malls', 'Larger-format retail and destination shopping.'),
    ('03', 'Hotels and hospitality assets', 'Accommodation serving regional travel, tourism and employment activity.'),
    ('04', 'Mixed-use development', 'Residential living combined with professional and commercial space in one place.'),
    ('05', 'Medical and service retail', 'Pharmacy, dental, optical, veterinary and care-tenanted formats, shown as concepts.'),
]

COMMERCIAL_APPROACH = [
    ('Practical space', 'The legacy language is "practical, high-quality space for growing businesses", not speculative inventory.'),
    ('Blended districts', 'A modern hub blending residential living and professional space is described as the goal, not a single-use building.'),
    ('Growth-aligned', 'Commercial investment is positioned as a response to population and job growth in a region.'),
]

# Each commercial entry carries what the legacy text actually said.
COMMERCIAL_PROJECTS = [
    {
        'name': 'Wilmot',
        'status': 'Concept',
        'summary': 'A mixed-use, high-potential commercial and self-storage opportunity positioned for strong, stable growth.',
        'detail': 'The surviving concept visual labels a commercial plaza and a self-storage facility. No address, unit '
                  'programme, approval or delivery date was published. The source graphic carried a location typo, which '
                  'is not reproduced here.',
        'image': 'wilmot-concept.webp',
        'alt': 'Wilmot commercial plaza and self-storage concept visualization',
        'note': 'Concept only. Not an approved plan, construction record or statement of current status.',
    },
    {
        'name': 'Greenwood',
        'status': 'Earlier name',
        'summary': 'Described as a commercial building project underway in Lucasville, offering practical, high-quality space for growing businesses.',
        'detail': 'The same section described a modern hub blending residential living and professional spaces. Because the '
                  'text places Greenwood in Lucasville, the relationship between the Greenwood and Lucasville names is '
                  'unresolved in the source material.',
        'image': '',
        'alt': '',
        'note': 'Current stage, address, scope and relationship to the Lucasville name all require confirmation.',
    },
    {
        'name': 'Lucasville',
        'status': 'Coming soon concept',
        'summary': 'Paired with a medical-retail concept and a "coming soon" message in the previous site.',
        'detail': 'The concept visual carried these tenant labels: day care centre, pharmacy, optometrist, dental centre, '
                  'medical centre, veterinary, and a national pet retailer. They are illustrative labels from concept '
                  'artwork and are not lease or opening commitments.',
        'image': 'lucasville-concept.webp',
        'alt': 'Illustrative Lucasville medical-retail concept with labelled tenancies',
        'note': 'Concept only. Tenant labels are illustrative and are not commitments.',
    },
    {
        'name': 'The Evangeline',
        'status': 'Earlier name',
        'summary': 'Appears in the group structure graphic under the commercial branch with no supporting project copy.',
        'detail': 'No location, scope, stage or timeline was ever published alongside the name.',
        'image': '',
        'alt': '',
        'note': 'Preserves the earlier public record. Current scope and status require confirmation.',
    },
    {
        'name': 'Cornwallis',
        'status': 'Planning review',
        'summary': 'The 240-acre Cornwallis Park parcel includes commercial potential described across the previous site.',
        'detail': 'Concept-stage commercial uses include a retail plaza, grocery and essential services, tourism-focused '
                  'businesses, industrial or commercial warehousing, an RV resort, agri-tourism, and motel, lodge or cabin '
                  'hospitality.',
        'image': 'cornwallis.webp',
        'alt': 'Illustrative Cornwallis Park concept plan',
        'note': 'See the Cornwallis Park project page for the full record and planning caveats.',
        'href': '/projects/cornwallis-park/',
    },
    {
        'name': 'The Sables',
        'status': 'Earlier name',
        'summary': 'Appears under both the residential and commercial branches of the group structure graphic.',
        'detail': 'The duplication is reproduced rather than resolved, because the source material does not explain whether '
                  'this is one project with two uses or two separate references.',
        'image': '',
        'alt': '',
        'note': 'Preserves the earlier public record. Classification requires confirmation.',
    },
]

# ---------------------------------------------------------------------------
# Industrial
# ---------------------------------------------------------------------------

INDUSTRIAL_HERO = (
    'INDUSTRIAL',
    'Space to build<br>a working region.',
    'Industrial parks, warehousing, flex space, self-storage and logistics for the businesses that keep Nova Scotia moving.',
)

INDUSTRIAL_INTRO = (
    'Industrial building is part of the same connected system as housing and commerce. Employment lands, '
    'logistics and homes are considered together, with practical spaces that help regional businesses keep moving.',
)

INDUSTRIAL_TYPES = [
    ('01', 'Industrial parks', 'Serviced, phased employment lands with room to grow and infrastructure to support business activity.'),
    ('02', 'Warehousing and distribution', 'Facilities planned to serve regional supply chains and distribution needs.'),
    ('03', 'Flex-industrial space', 'Smaller-format spaces for trades, suppliers and light assembly.'),
    ('04', 'Self-storage', 'Storage buildings planned for efficient use of space and straightforward access.'),
    ('05', 'Logistics', 'Logistics space that supports the industrial sector and the wider region.'),
]

INDUSTRIAL_PROJECTS = [
    {
        'name': 'Plexus Storage',
        'status': 'Earlier name',
        'summary': 'Described as a hub designed for efficient storage and said to be executed across multiple Nova Scotia locations.',
        'detail': 'A Plexus Storage logo was published with no accompanying location list, facility count, operating '
                  'status, dimensions or supporting detail. The relationship between Plexus Storage and Plexus '
                  'Development Group is also unstated in the source.',
        'image': '',
        'alt': '',
        'note': 'Ownership, operating relationship, facility names and addresses all require confirmation.',
    },
    {
        'name': 'Cornwallis Park',
        'status': 'Planning review',
        'summary': 'The 240-acre parcel is described as supporting industrial or commercial warehousing alongside mixed uses.',
        'detail': 'A warehouse facility appears on the concept plan. The surrounding strategy also references industrial '
                  'and residential interfaces in the wider district.',
        'image': 'cornwallis.webp',
        'alt': 'Illustrative Cornwallis Park concept plan',
        'note': 'See the Cornwallis Park project page for the full record and planning caveats.',
        'href': '/projects/cornwallis-park/',
    },
    {
        'name': 'Lucasville',
        'status': 'Earlier name',
        'summary': 'Listed in the industrial branch of the group structure graphic.',
        'detail': 'The same name also appears in the commercial branch and in the commercial page text, where it is paired '
                  'with a medical-retail concept.',
        'image': '',
        'alt': '',
        'note': 'The duplication across sectors is unresolved in the source material.',
    },
    {
        'name': 'Wilmot',
        'status': 'Concept',
        'summary': 'Listed in the industrial branch of the group structure graphic, and described commercially elsewhere.',
        'detail': 'The commercial description of Wilmot centres on a self-storage facility, which is the industrial element '
                  'of that concept.',
        'image': 'wilmot-concept.webp',
        'alt': 'Wilmot commercial plaza and self-storage concept visualization',
        'note': 'Concept only. See the commercial page for the full description.',
    },
    {
        'name': 'Greenwood',
        'status': 'Earlier name',
        'summary': 'Listed in the industrial branch of the group structure graphic.',
        'detail': 'The commercial page describes Greenwood as a commercial building project in Lucasville.',
        'image': '',
        'alt': '',
        'note': 'Current stage, address and scope require confirmation.',
    },
]

# ---------------------------------------------------------------------------
# Cross-sector content used on the projects hub
# ---------------------------------------------------------------------------

ASSET_CLASSES = [
    'Multi-unit residential buildings, existing and value-add',
    'Commercial plazas and retail centres',
    'Shopping centres and malls',
    'Hotels and hospitality assets',
    'Industrial parks',
    'Warehouses and flex-industrial facilities',
    'Large developable land parcels',
]

LOCATION_MAP_NOTE = (
    'The previous site included a map of Nova Scotia with markers around Amherst, New Glasgow, Kentsville, '
    'Windsor, Greenwood, Digby, Annapolis Royal, Bedford and Halifax. It carried no legend tying markers to '
    'named projects, so no location has been assigned on this site.'
)
