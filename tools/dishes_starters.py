# Bar snacks and starters, in the order of the kitchen's sheet. Staff notes for each dish, written from the Food Bible.
#
# Fields (the same pattern as the wine app's wines_*.py):
#   section  which part of the menu
#   name     the dish as it is named on the menu
#   short    a short name for chips and quizzes
#   sell     ONE honest line a waiter can say out loud
#   plate    what is on the plate
#   making   how it is made, in front-of-house language (optional)
#   portion  how many pieces, or the sizes (optional)
#   service  cutlery and what to offer (optional)
#   flag     anything a guest may not expect (optional)
#   alcohol  the alcohol named in the recipe (optional)
#   terms    glossary entries (from content_guide.GLOSS) worth knowing for this dish
#   wines    suggested wines: (wine app id, why). Checked against data/wine-list-snapshot.json
#   with_    other dishes on the menu that are served as part of this one (their allergens are checked too)
#
# NEVER write allergens here. They live in allergens.py and nowhere else.
# Do not write "gluten-free", "dairy-free", "safe for ..." or anything like it: the build refuses.

D = {
    # ------------------------------------------------------------ bar snacks
    'caviar': dict(section='snacks', name='Oscietra caviar (30 g)', short='Oscietra caviar',
        sell='30 g of Oscietra caviar, served with crème fraîche and chives.',
        plate='30 g of Oscietra caviar, served with crème fraîche and chives.',
        portion='30 g.',
        service='One caviar spoon per table for up to four guests. Two spoons for more than four.',
        flag='Caviar spoons must not be sent to the kitchen porters. Wash them carefully by hand and put them back in their drawer.',
        terms=['Oscietra', 'Crème fraîche'],
        wines=[('w060', 'A crisp Blanc de Blancs Champagne.'),
               ('w067', 'For a table that wants the grandest bottle with caviar.')]),

    # ------------------------------------------------------------ starters
    'reuben': dict(section='starters', name='The Reuben', short='The Reuben',
        sell='Pulled pastrami and Emmental in sourdough toasted in beef fat, on fennel kraut with Thousand Island.',
        plate='Pulled pastrami, made from beef brisket, and Emmental cheese between slices of multigrain sourdough toasted in beef fat. It is served over fennel kraut dressed with Thousand Island.',
        flag='The bread is toasted in beef fat.',
        terms=['Pastrami', 'Emmental', 'Kraut', 'Thousand Island'],
        wines=[('w036', 'A juicy, savoury red that stands up to pastrami.'),
               ('w006', 'A textured natural white for cured meat and pickles. Offer a taste first.')]),
    'tartare': dict(section='starters', name='Longhorn rump tartare', short='Rump tartare',
        sell='Finely diced Longhorn rump with capers, cornichons, Dijon and chilli crisp, a cured egg yolk and game chips on the side.',
        plate='Longhorn rump (picanha), seared, chilled and finely diced, then mixed with capers, shallots, Dijon mustard, cornichons, olive oil, anchovies and chilli crisp. It is finished with a herb salad of basil, chive and parsley and an egg yolk cured in soy and mirin.',
        service='Game chips are served on the side.',
        flag='There are anchovies in the mix. The beef is seared, then chilled and diced, and the egg yolk is cured, not cooked. If a guest avoids raw or lightly cooked meat or egg, check with the kitchen.',
        terms=['Tartare', 'Longhorn', 'Picanha', 'Cornichons', 'Mirin', 'Chilli crisp', 'Game chips', 'Cure'],
        wines=[('w036', 'Gamay with some grip: a classic with beef tartare.'),
               ('w026', 'A light, fresh red that will not swamp the beef.')]),
    'crabcakes': dict(section='starters', name='Dorset crab cakes', short='Crab cakes',
        sell='Crab cakes of brown and white Dorset crab with a preserved-lemon tartare sauce.',
        plate='Crab cakes made with brown and white Dorset crab meat, herbs and a dry mashed-potato base. Served with preserved-lemon tartare sauce and a herb salad.',
        making='Dry mashed potato is used as the binding base.',
        terms=['Brown and white crab meat', 'Tartare sauce', 'Preserved lemon'],
        wines=[('w001', 'Light, salty and very fresh: made for crab.'),
               ('w004', 'An aromatic Riesling with a touch of sweetness.')]),
    'artichoke': dict(section='starters', name='Artichoke salad', short='Artichoke salad',
        sell='Roasted Jerusalem artichokes in a walnut mole on black garlic purée, with Castelfranco leaves, artichoke crisps and sesame oil.',
        plate='Jerusalem artichokes, halved and roasted, dressed with walnut mole and served on a bed of black garlic purée. Mixed with Castelfranco lettuce and finished with artichoke crisps and a drizzle of sesame oil.',
        flag='The mole is made with walnuts and the salad is finished with sesame oil. The kitchen asks us to confirm the exact mole recipe with them.',
        terms=['Jerusalem artichoke', 'Mole', 'Black garlic', 'Castelfranco'],
        wines=[('w018', 'A textured Spanish white that the wine list suggests with artichokes.')]),
    'caesar': dict(section='starters', name='Bar Finch Caesar', short='Caesar',
        sell='Our chicken Caesar: brined chicken, romaine, focaccia croutons and a Caesar dressing finished with anchovy and Parmesan.',
        plate='Brined chicken with romaine lettuce and focaccia croutons, in Caesar dressing finished with anchovy and Parmesan.',
        flag='It comes with chicken, and the dressing is finished with anchovy.',
        terms=['Brine', 'Caesar dressing', 'Romaine'],
        wines=[('w007', 'Unoaked Chardonnay: fresh enough for the dressing.'),
               ('w076', 'The house Champagne is very good with chicken.')]),
    'trout': dict(section='starters', name='Smoked trout', short='Smoked trout',
        sell='Thin slices of smoked chalk-stream trout with dill, parsley, crisp capers and lemon zest: fresh and lightly smoky.',
        plate='Smoked chalk-stream trout, thinly sliced and finished with dill, parsley, crisp capers and lemon zest.',
        terms=['Chalk-stream trout', 'Crisp capers'],
        wines=[('w056', 'Sparkling Chenin with enough fruit for smoked fish.'),
               ('w005', 'A light, aromatic English white.')]),
    'lobster': dict(section='starters', name='Half/whole Thermidor lobster', short='Thermidor lobster',
        sell='Lobster Thermidor, half or whole, with the meat carved out and put back in the shell.',
        plate='Lobster Thermidor. The meat is carved out and then put back in the shell.',
        portion='Half or whole.',
        flag='Ask whether the guest would like a half or a whole lobster. The kitchen has not yet written up how our Thermidor is made, so ask them before you describe the sauce.',
        terms=['Thermidor', 'Gratinated', 'Monte', 'Green garlic'],
        wines=[('w025', 'A rich, oaked white Burgundy.'),
               ('w022', 'A rich, oaked white Burgundy, by the bottle.')]),
    'souffle': dict(section='starters', name='Double-baked Parmesan soufflé with seasonal truffle', short='Parmesan soufflé',
        sell='A double-baked Parmesan soufflé with fresh truffle, finished with a Parmesan and truffle sauce.',
        plate='A roux-based soufflé mixed with Parmesan and fresh truffle, finished with a béchamel-style sauce with freshly grated Parmesan and truffle.',
        making='The base is a roux: equal parts flour and butter. Double-baked means it is cooked once, then baked again for service.',
        terms=['Soufflé', 'Roux', 'Béchamel', 'Truffle'],
        wines=[('w076', 'The house Champagne: rich and toasty with cheese.'),
               ('w015', 'A crisp white Burgundy.')]),
}
