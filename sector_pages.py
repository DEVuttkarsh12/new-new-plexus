# Sector page builders and the group-structure chart.
#
# Imported by generate_site.py. Every string here derives from sector_data.py,
# which in turn is sourced from the legacy capture. Nothing asserts an approval,
# ownership, address, unit count, price or delivery date the capture lacks.

from sector_data import (
    BRANCHES, ROOT, STRUCTURE_NOTES,
    RESIDENTIAL_HERO, RESIDENTIAL_INTRO, RESIDENTIAL_TYPES, RESIDENTIAL_APPROACH,
    RESIDENTIAL_PIPELINE_HEADING, RESIDENTIAL_PIPELINE_NOTE,
    COMMERCIAL_HERO, COMMERCIAL_INTRO, COMMERCIAL_TYPES, COMMERCIAL_APPROACH, COMMERCIAL_PROJECTS,
    INDUSTRIAL_HERO, INDUSTRIAL_INTRO, INDUSTRIAL_TYPES, INDUSTRIAL_PROJECTS,
    ASSET_CLASSES,
)

INDUSTRIAL_APPROACH = [
    ('Space that keeps working', 'The legacy position is space built for businesses that operate rather than trade, and that stays useful across a full asset cycle.'),
    ('Planned alongside housing', 'Employment land and residential land are considered together as one connected system, not as separate transactions.'),
    ('Phased and serviced', 'Industrial and storage projects are described in terms of phasing, servicing and infrastructure rather than single completions.'),
]

SECTOR_CROSS_LINKS = [
    ('01', '/projects/', 'The full project picture', 'Every project with a detail page, the group-structure chart and the earlier-name register.'),
    ('02', '/residential/', 'Residential', 'Multi-unit buildings, subdivisions, mixed communities and senior living.'),
    ('03', '/commercial/', 'Commercial', 'Plazas, retail centres, hospitality, mixed use and service retail.'),
    ('04', '/industrial/', 'Industrial', 'Industrial parks, warehousing, flex space, self-storage and logistics.'),
    ('05', '/community/', 'Community', 'The community record carried forward from the earlier site.'),
]


SECTOR_ROUTES = {
    '/residential/': 'Residential',
    '/commercial/': 'Commercial',
    '/industrial/': 'Industrial',
    '/projects/': 'The full project picture',
}


def cross_links(current_route):
    """Sector hub rows, excluding the destination the current page already is.

    One row is removed on every page and the rest are renumbered, so a reader
    is never shown a link back to where they already are.
    """
    current = SECTOR_ROUTES.get(current_route)
    items = [r for r in SECTOR_CROSS_LINKS if r[2] != current]
    return [(f"{i:02d}", href, title, desc)
            for i, (_, href, title, desc) in enumerate(items, 1)]
