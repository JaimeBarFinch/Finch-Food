# The allergen record for every dish. THIS FILE IS SAFETY-CRITICAL.
#
# Rules:
#   - Copy allergens only from the kitchen's own document. Never work them out from a recipe,
#     and never fill a gap with a guess.
#   - `raw` is the kitchen's wording, word for word.
#   - `contains` = allergens the kitchen states plainly.
#   - `maybe`    = allergens the kitchen marks as "likely", "may apply" or "tbc".
#   - `open=True` = the kitchen has not confirmed the full list for this dish ("confirm with kitchen",
#     "confirm full current matrix", or no allergen line at all). The app then shows EVERY allergen
#     that is not in `contains` as "not confirmed" for that dish.
#   - `no` = allergens the kitchen has said in writing are NOT in the dish, where an earlier document listed them.
#     Quote the kitchen's words in `raw`. Never add to `no` on anyone else's say-so.
#   - `none=True` = the kitchen has said the dish has none of the 14 allergens. Quote them in `raw`.
#   - The build checks `raw` against `contains` + `maybe` + `no`, so they cannot drift apart.
#
# Allergen keys (the 14 UK allergens):
#   celery gluten crustaceans eggs fish lupin milk molluscs mustard nuts peanuts sesame soya sulphites

# Allergen lists come from the Food Bible PDF (November 2026), then from the answers Bar Finch gave on
# 10 November 2026 to the open questions (marked in each `raw`). A dish with no answer yet is open=True.
SOURCE = 'Bar Finch Food Bible'
SOURCE_DATE = 'November 2026'

A = {
    # ---- bar snacks
    'caviar': dict(raw='', contains=[], open=True),          # description sheet only: no allergen line
    # ---- starters
    'reuben': dict(raw='Milk/dairy, sulphites, gluten, egg, mustard.',
                   contains=['milk', 'sulphites', 'gluten', 'eggs', 'mustard']),
    'tartare': dict(raw='Gluten, eggs, fish, mustard, soya, sulphites. (Given by Bar Finch on 10 November 2026.)',
        contains=['gluten', 'eggs', 'fish', 'mustard', 'soya', 'sulphites']),
    'crabcakes': dict(raw='Shellfish/crustaceans, egg, mustard, milk and gluten.',
                      contains=['crustaceans', 'eggs', 'mustard', 'milk', 'gluten']),
    'artichoke': dict(raw='Tree Nuts, Sesame, Dairy, Gluten, Sulphites. (Given by Bar Finch on 10 November 2026.)',
        contains=['nuts', 'sesame', 'milk', 'gluten', 'sulphites']),
    'lobster': dict(raw='Crustaceans, milk, celery. (Given by Bar Finch on 10 November 2026.)',
        contains=['crustaceans', 'milk', 'celery']),
    'souffle': dict(raw='Milk, gluten, eggs. (Given by Bar Finch on 10 November 2026.)',
        contains=['milk', 'gluten', 'eggs']),
    'caesar': dict(raw='Fish, milk, egg, mustard, gluten, sulphites.',
                   contains=['fish', 'milk', 'eggs', 'mustard', 'gluten', 'sulphites']),
    # ---- mains
    'trout': dict(raw='Fish, sulphites. (Given by Bar Finch on 10 November 2026.)',
        contains=['fish', 'sulphites']),
    'hamburger': dict(raw='Gluten, milk, mustard, egg; sulphites. The kitchen\'s later description sheet says: DOES NOT CONTAIN EGG.',
                      contains=['gluten', 'milk', 'mustard', 'sulphites'], no=['eggs']),
    'potpie': dict(raw='Gluten, Milk, Eggs, Sulphites, Mustard. (Given by Bar Finch on 10 November 2026.)',
        contains=['gluten', 'milk', 'eggs', 'sulphites', 'mustard']),
    'steakfrites': dict(raw='Sulphites, Dairy. (Given by Bar Finch on 10 November 2026.)',
        contains=['sulphites', 'milk']),
    'piccata': dict(raw='Milk and sulphites.',
                    contains=['milk', 'sulphites']),
    'schnitzel': dict(raw='Gluten, Egg, Soya. (Given by Bar Finch on 10 November 2026.)',
        contains=['gluten', 'eggs', 'soya']),
    'fries': dict(raw='Sulphites. (Given by Bar Finch on 10 November 2026.)',
        contains=['sulphites']),
    'sweetheart': dict(raw='Nothing. (Given by Bar Finch on 10 November 2026.)',
        contains=[], none=True),
    'mixedleaf': dict(raw='Mustard, Sulphites. (Given by Bar Finch on 10 November 2026.)',
        contains=['mustard', 'sulphites']),
    'mash': dict(raw='Milk',
                 contains=['milk']),
    'greensbeans': dict(raw='Milk.',
                        contains=['milk']),
    # ---- sauces
    'bearnaise': dict(raw='Egg, milk, sulphites.',
                      contains=['eggs', 'milk', 'sulphites']),
    'peppercorn': dict(raw='Sulphites',
                       contains=['sulphites']),
    'holstein': dict(raw='Fish, sulphites, mustard, milk. (Given by Bar Finch on 10 November 2026.)',
        contains=['fish', 'sulphites', 'mustard', 'milk']),
    'tiramisu': dict(raw='Milk, egg, gluten, sulphites',
                     contains=['milk', 'eggs', 'gluten', 'sulphites']),
    'lemonpie': dict(raw='Gluten, Eggs, Milk. (Given by Bar Finch on 10 November 2026.)',
        contains=['gluten', 'eggs', 'milk']),
    'cremoso': dict(raw='Milk, Eggs.',
                    contains=['milk', 'eggs']),
    'semifreddo': dict(raw='Milk, egg; sulphites.',
                       contains=['milk', 'eggs', 'sulphites']),
    'beignet': dict(raw='Gluten, egg, milk. (Given by Bar Finch on 10 November 2026.)',
        contains=['gluten', 'eggs', 'milk']),
}

# Questions for the kitchen. The build stops if a dish's own text names an ingredient that points to an
# allergen its record does not list (butter without milk, soy without soya, a side dish's allergens ...).
# We do NOT fix the record ourselves. Each open question is written here; the app then shows that
# allergen as "not confirmed" on the dish until the kitchen answers. When the kitchen answers:
#   - if the allergen applies, add it to `contains` above and delete the question;
#   - if it does not, keep the question's line but start the note with 'KITCHEN CONFIRMED NO:' and the date.
QUERIES = {
    'caviar': [
        ('fish', 'Caviar is sturgeon roe.'),
        ('milk', 'Served with crème fraîche.'),
    ],
    'potpie': [
        ('nuts', 'The filling has chestnuts, and the list given on 10 November 2026 does not mention nuts.'),
    ],
    'steakfrites': [
        ('eggs', 'KITCHEN CONFIRMED NO (10 November 2026): mayonnaise is an extra on request, not part of the dish.'),
    ],
    'fries': [
        ('eggs', 'KITCHEN CONFIRMED NO (10 November 2026): mayonnaise is an extra, not part of the dish.'),
    ],
}
