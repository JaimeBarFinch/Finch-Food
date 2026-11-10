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
#   - The build checks `raw` against `contains` + `maybe` + `no`, so they cannot drift apart.
#
# Allergen keys (the 14 UK allergens):
#   celery gluten crustaceans eggs fish lupin milk molluscs mustard nuts peanuts sesame soya sulphites

# Allergen lists come from the Food Bible PDF (November 2026). The later description sheet (a Word file, also
# November 2026) has no allergen lines, so dishes that appear only on that sheet are open=True with no list.
SOURCE = 'Bar Finch Food Bible'
SOURCE_DATE = 'November 2026'

A = {
    # ---- bar snacks
    'caviar': dict(raw='', contains=[], open=True),          # description sheet only: no allergen line
    # ---- starters
    'reuben': dict(raw='Milk/dairy, sulphites, gluten, egg, mustard.',
                   contains=['milk', 'sulphites', 'gluten', 'eggs', 'mustard']),
    'tartare': dict(raw='Fish, egg, mustard, gluten; soy and sulphites may apply from the cure/condiments - confirm against the live allergen matrix.',
                    contains=['fish', 'eggs', 'mustard', 'gluten'], maybe=['soya', 'sulphites']),
    'crabcakes': dict(raw='Shellfish/crustaceans, egg, mustard, milk and gluten.',
                      contains=['crustaceans', 'eggs', 'mustard', 'milk', 'gluten']),
    'artichoke': dict(raw='', contains=[], open=True),       # description sheet only: no allergen line
    'lobster': dict(raw='', contains=[], open=True),         # description sheet only: no allergen line
    'souffle': dict(raw='', contains=[], open=True),         # description sheet only: no allergen line
    'caesar': dict(raw='Fish, milk, egg, mustard, gluten, sulphites.',
                   contains=['fish', 'milk', 'eggs', 'mustard', 'gluten', 'sulphites']),
    # ---- mains
    'trout': dict(raw='Fish; sulphites may apply from capers - confirm current matrix.',
                  contains=['fish'], maybe=['sulphites']),
    'hamburger': dict(raw='Gluten, milk, mustard, egg; sulphites. The kitchen\'s later description sheet says: DOES NOT CONTAIN EGG.',
                      contains=['gluten', 'milk', 'mustard', 'sulphites'], no=['eggs']),
    'potpie': dict(raw='', contains=[], open=True),          # description sheet only: no allergen line
    'steakfrites': dict(raw='Milk.',
                        contains=['milk']),
    'piccata': dict(raw='Milk and sulphites.',
                    contains=['milk', 'sulphites']),
    'schnitzel': dict(raw='Gluten and egg likely from schnitzel coating; confirm full current matrix.',
                      contains=[], maybe=['gluten', 'eggs'], open=True),
    # ---- sides
    'fries': dict(raw='Sulphites',
                  contains=['sulphites']),
    'sweetheart': dict(raw='',   # the Food Bible has no allergen line for this dish
                       contains=[], open=True),
    'mixedleaf': dict(raw='Mustard',
                      contains=['mustard']),
    'mash': dict(raw='Milk',
                 contains=['milk']),
    'greensbeans': dict(raw='Milk.',
                        contains=['milk']),
    # ---- sauces
    'bearnaise': dict(raw='Egg, milk, sulphites.',
                      contains=['eggs', 'milk', 'sulphites']),
    'peppercorn': dict(raw='Sulphites',
                       contains=['sulphites']),
    'holstein': dict(raw='Fish, milk; sulphites may apply from capers - confirm current matrix.',
                     contains=['fish', 'milk'], maybe=['sulphites']),
    # ---- desserts
    'tiramisu': dict(raw='Milk, egg, gluten, sulphites',
                     contains=['milk', 'eggs', 'gluten', 'sulphites']),
    'lemonpie': dict(raw='Milk, egg, gluten likely from cake base - confirm full current matrix.',
                     contains=['milk', 'eggs'], maybe=['gluten'], open=True),
    'cremoso': dict(raw='Milk, Eggs.',
                    contains=['milk', 'eggs']),
    'semifreddo': dict(raw='Milk, egg; sulphites.',
                       contains=['milk', 'eggs', 'sulphites']),
    'beignet': dict(raw='Gluten, egg and milk likely; sulphites may apply from brandy per previous chef note - confirm current matrix.',
                    contains=[], maybe=['gluten', 'eggs', 'milk', 'sulphites'], open=True),
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
    'artichoke': [
        ('nuts', 'Dressed with a walnut mole.'),
        ('sesame', 'Finished with sesame oil.'),
    ],
    'lobster': [
        ('crustaceans', 'The dish is lobster.'),
        ('milk', 'The kitchen\'s notes mention monté au beurre, a butter sauce.'),
    ],
    'souffle': [
        ('milk', 'Made with butter and Parmesan, with a béchamel-style sauce.'),
        ('gluten', 'The roux is made with flour.'),
        ('eggs', 'A soufflé is normally made with egg.'),
    ],
    'potpie': [
        ('gluten', 'Topped with puff pastry.'),
        ('milk', 'Puff pastry is made with butter.'),
        ('nuts', 'The filling has chestnuts.'),
    ],
    'steakfrites': [
        ('sulphites', 'Served with fries, and the fries entry lists sulphites.'),
        ('eggs', 'Mayonnaise is offered on request.'),
    ],
    'fries': [
        ('eggs', 'Mayonnaise is offered with the fries.'),
    ],
    'mixedleaf': [
        ('sulphites', 'The house dressing is described as mustard, lemon, sherry and olive oil.'),
    ],
    'schnitzel': [
        ('soya', 'The brine is described as honey, sugar, soy and salt.'),
    ],
}
