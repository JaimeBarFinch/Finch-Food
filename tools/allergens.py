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
#   - The build checks `raw` against `contains` + `maybe`, so the two cannot drift apart.
#
# Allergen keys (the 14 UK allergens):
#   celery gluten crustaceans eggs fish lupin milk molluscs mustard nuts peanuts sesame soya sulphites

SOURCE = 'Bar Finch Food Bible'
SOURCE_DATE = 'November 2026'

A = {
    # ---- bar snacks / small plates
    'gildas': dict(raw='Fish, gluten, milk, sulphites.',
                   contains=['fish', 'gluten', 'milk', 'sulphites']),
    'reuben': dict(raw='Milk/dairy, sulphites, gluten, egg, mustard.',
                   contains=['milk', 'sulphites', 'gluten', 'eggs', 'mustard']),
    # ---- starters
    'tartare': dict(raw='Fish, egg, mustard, gluten; soy and sulphites may apply from the cure/condiments - confirm against the live allergen matrix.',
                    contains=['fish', 'eggs', 'mustard', 'gluten'], maybe=['soya', 'sulphites']),
    'crabcakes': dict(raw='Shellfish/crustaceans, egg, mustard, milk and gluten.',
                      contains=['crustaceans', 'eggs', 'mustard', 'milk', 'gluten']),
    'tomatosalad': dict(raw='Mustard, sulphites.',
                        contains=['mustard', 'sulphites']),
    # ---- salads
    'choppedsalad': dict(raw='Sulphites.',
                         contains=['sulphites']),
    'caesar': dict(raw='Fish, milk, egg, mustard, gluten, sulphites.',
                   contains=['fish', 'milk', 'eggs', 'mustard', 'gluten', 'sulphites']),
    'tuna': dict(raw='Fish, sulphites, (may include gluten later, tbc)',
                 contains=['fish', 'sulphites'], maybe=['gluten']),
    # ---- mains
    'trout': dict(raw='Fish; sulphites may apply from capers - confirm current matrix.',
                  contains=['fish'], maybe=['sulphites']),
    'langoustines': dict(raw='Crustaceans, milk, sulphites; soy.',
                         contains=['crustaceans', 'milk', 'sulphites', 'soya']),
    'hamburger': dict(raw='Gluten, milk, mustard, egg; sulphites.',
                      contains=['gluten', 'milk', 'mustard', 'eggs', 'sulphites']),
    'roastchicken': dict(raw='Confirm with kitchen; honey is not one of the UK 14 declarable allergens.',
                         contains=[], open=True),
    'steakfrites': dict(raw='Milk.',
                        contains=['milk']),
    'piccata': dict(raw='Milk and sulphites.',
                    contains=['milk', 'sulphites']),
    'melanzane': dict(raw='Milk',
                      contains=['milk']),
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
    'steakfrites': [
        ('sulphites', 'Served with fries, and the fries entry lists sulphites.'),
        ('eggs', 'Mayonnaise is offered on request.'),
    ],
    'fries': [
        ('eggs', 'Mayonnaise is offered with the fries.'),
    ],
    'melanzane': [
        ('mustard', 'Served with the mixed leaf salad, and that entry lists mustard.'),
        ('sulphites', 'Served with the mixed leaf salad, whose house dressing includes sherry.'),
    ],
    'mixedleaf': [
        ('sulphites', 'The house dressing is described as mustard, lemon, sherry and olive oil.'),
    ],
    'schnitzel': [
        ('soya', 'The brine is described as honey, sugar, soy and salt.'),
    ],
}
