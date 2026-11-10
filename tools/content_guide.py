# The Info half of the app, apart from the dishes: the 14 allergens, what to offer guests,
# how the menu works, the allergy steps and the glossary.
# {d:id} in text becomes the dish's short name. Never type an allergen fact about a dish here:
# use needs=[...] so the build checks it against allergens.py.

# ---------- The 14 UK allergens: (key, full name, short name, two-letter code for the grid, examples) ----------
ALLERGENS = [
    ('celery', 'Celery', 'Celery', 'Ce', 'Celery stalks, leaves and seeds, and celeriac.'),
    ('gluten', 'Cereals containing gluten', 'Gluten', 'Gl', 'Wheat, rye, barley and oats: bread, flour, batter, breadcrumbs.'),
    ('crustaceans', 'Crustaceans', 'Crustaceans', 'Cr', 'Prawns, crab, lobster and langoustines.'),
    ('eggs', 'Eggs', 'Eggs', 'Eg', 'Eggs, and things made with them such as mayonnaise and meringue.'),
    ('fish', 'Fish', 'Fish', 'Fi', 'All fish, including anchovies.'),
    ('lupin', 'Lupin', 'Lupin', 'Lu', 'Lupin flour and seeds, sometimes used in bread and pastry.'),
    ('milk', 'Milk', 'Milk', 'Mi', 'Milk, butter, cream, cheese and yoghurt.'),
    ('molluscs', 'Molluscs', 'Molluscs', 'Mo', 'Mussels, oysters, clams, squid, octopus and snails.'),
    ('mustard', 'Mustard', 'Mustard', 'Mu', 'Mustard seed, powder and prepared mustard; common in dressings.'),
    ('nuts', 'Tree nuts', 'Nuts', 'Nu', 'Almonds, hazelnuts, walnuts, pistachios, cashews, pecans and other tree nuts.'),
    ('peanuts', 'Peanuts', 'Peanuts', 'Pe', 'Peanuts. They are a separate allergen from tree nuts.'),
    ('sesame', 'Sesame', 'Sesame', 'Se', 'Sesame seeds, sesame oil and tahini.'),
    ('soya', 'Soya', 'Soya', 'So', 'Soy sauce, tofu, miso and edamame.'),
    ('sulphites', 'Sulphur dioxide and sulphites', 'Sulphites', 'Su', 'A preservative found in wine, vinegar and dried fruit.'),
]

# ---------- Guests: what they say -> what to offer ----------
# q = what the guest says; dishes = what to offer; tip = one line of advice.
# auto='alcohol' fills the row with every dish whose notes name alcohol.
# needs=[(allergen, [dish ids])] makes the build check that a tip's allergen-related claim still matches allergens.py.
STEER = [
    dict(q='“Something light”', dishes=['tomatosalad', 'choppedsalad', 'tuna', 'trout', 'sweetheart'],
         tip='The salads and the cold fish plates are the lightest things on the menu. The sweetheart cabbage is the lightest side.'),
    dict(q='“Something for the table” or “to share”', dishes=['gildas', 'langoustines', 'roastchicken', 'fries', 'beignet'],
         tip='The Gildas come as two skewers, the langoustines as three and the beignets as three pieces. The roast chicken can be ordered whole.'),
    dict(q='“Just a snack with a drink”', dishes=['gildas', 'reuben', 'fries'],
         tip='The Gildas and the Reuben are the bar snacks.'),
    dict(q='“No meat”', dishes=['tomatosalad', 'choppedsalad', 'melanzane', 'sweetheart', 'mixedleaf', 'mash', 'greensbeans'],
         tip='These have no meat or fish in their Food Bible description, but the kitchen has not yet marked any dish as vegetarian or vegan. Check with the kitchen before you promise anything, and ask what the fries are cooked in.'),
    dict(q='“Fish” or “seafood”', dishes=['crabcakes', 'tuna', 'trout', 'langoustines'],
         tip='There is also anchovy in the Gildas, the tartare, the Caesar and the Holstein sauce.',
         needs=[('fish', ['gildas', 'tartare', 'caesar', 'holstein', 'tuna', 'trout']), ('crustaceans', ['crabcakes', 'langoustines'])]),
    dict(q='“Something rich” or “comfort food”', dishes=['reuben', 'hamburger', 'steakfrites', 'melanzane', 'mash'],
         tip='A sauce can be added: Béarnaise, peppercorn or Holstein.'),
    dict(q='“Chicken”', dishes=['caesar', 'roastchicken', 'piccata'],
         tip='Three very different plates: a salad, a honey-brined roast (half or whole) and a poussin in a caper and wine sauce.'),
    dict(q='“Beef”', dishes=['tartare', 'reuben', 'hamburger', 'steakfrites'],
         tip='Beef fat is also used to toast the Reuben’s bread and to cook the hamburger and the steak.'),
    dict(q='“No beef” or “no pork”', dishes=[],
         tip='Beef: the tartare, the Reuben, the hamburger and the steak frites. Beef fat is used for the Reuben’s bread, the hamburger and the steak. Pork: the schnitzel. The Food Bible does not say what the fries are cooked in, so ask the kitchen.'),
    dict(q='“Is anything raw?”', dishes=['tartare', 'tuna', 'trout'],
         tip='The tartare beef is seared, chilled and diced, and its egg yolk is cured, not cooked. The tuna is described as sashimi. The trout is smoked. If a guest must avoid raw or lightly cooked food, check each dish with the kitchen.'),
    dict(q='“Is there alcohol in it?”', dishes=[], auto='alcohol',
         tip='These dishes name alcohol in their recipe. If it matters to the guest, check with the kitchen.'),
    dict(q='“A sauce with that”', dishes=['bearnaise', 'peppercorn', 'holstein'],
         tip='Béarnaise is the egg, butter and herb one. Peppercorn is finished with brandy and port. Holstein is brown butter with capers and anchovies.'),
    dict(q='“Something sweet”', dishes=['tiramisu', 'lemonpie', 'cremoso', 'semifreddo', 'beignet'],
         tip='Chocolate: the cremoso. Sharp and fruity: the lemon meringue pie. To share: the beignets, three pieces.'),
    dict(q='“We’re in a hurry”', dishes=[],
         tip='The Food Bible has no cooking times yet. Ask the kitchen what is quickest right now, and tell them the table is short of time when you put the order in.'),
]

# ---------- How the menu works: (title, body). {count}, {alcohol} are filled in by the build ----------
RULES = [
    ('The menu', '{count} dishes in seven sections: bar snacks and small plates, starters, salads, mains, sides, sauces and desserts.'),
    ('Portions', 'Gildas: two skewers. Langoustines: three. Beignets: three pieces. Roast chicken: half or whole.'),
    ('Questions to ask', 'Steak: pink or well done. Roast chicken: half or whole. Fries: ketchup, mayonnaise or both.'),
    ('Things guests don’t expect', 'Anchovy in the Gildas, the tartare, the Caesar dressing and the Holstein sauce. Beef fat on the Reuben’s bread, the hamburger and the steak. Honey in the roast chicken brine, the schnitzel brine and the semifreddo.'),
    ('Alcohol in the food', '{alcohol}'),
    ('Changes to a dish', 'The Food Bible does not say what can and cannot be changed. Do not promise a change: ask the kitchen first.'),
    ('Allergens', 'Use the Allergens tab to look a dish up, then confirm with the kitchen before the order goes in. Every time.'),
]

# ---------- When a guest has an allergy ----------
ALLERGY = dict(
    intro='This app helps you find the right dishes quickly. It does not replace the kitchen. Recipes and suppliers change, so the kitchen always has the final word.',
    steps=[
        ('Listen and write it down.', 'Note exactly what the guest cannot have, and which guest it is.'),
        ('Look it up.', 'Use the Allergens tab to see what the Food Bible lists for each dish. Remember the sauce, the side and anything offered on request, such as mayonnaise.'),
        ('Confirm with the kitchen.', 'Every time, before the order goes in.'),
        ('Tell the guest what you know, not what you assume.', 'Say “the kitchen has confirmed” or “I will check”. Never say a dish is free from something because it is not listed here.'),
        ('If you are not sure, stop.', 'Do not guess and do not send the order. Ask the kitchen.'),
    ],
    marks=[
        ('●', 'Listed', 'The Food Bible lists this allergen for the dish.'),
        ('?', 'Not confirmed', 'The Food Bible says “likely”, “may apply” or “to be confirmed”, has no confirmed list for the dish, or the description names an ingredient the list does not cover. Treat it as present until the kitchen tells you otherwise.'),
        ('–', 'Not listed', 'The Food Bible does not list it. That is not the same as “free from”: confirm with the kitchen.'),
    ],
)

# ---------- Glossary: (term, kind, meaning). kind: t = technique, d = dish or sauce, i = ingredient ----------
GLOSS = [
    # techniques
    ('Blanch', 't', 'To boil briefly, then cool.'),
    ('Brine', 't', 'A seasoned salt-water solution. Food is soaked in it before cooking to add flavour and help it stay moist.'),
    ('Clarified butter', 't', 'Butter heated and strained so that only the clear butterfat is left.'),
    ('Confit', 't', 'Cooked slowly and gently until soft. Our confit garlic is cooked slowly until soft and mellow.'),
    ('Cure', 't', 'To season and firm food with salt, sugar or a seasoned liquid, without heat.'),
    ('Custard', 't', 'An egg-and-dairy mixture, gently set with heat.'),
    ('Deglaze', 't', 'To lift the caramelised flavours from a pan with liquid.'),
    ('Dry-aged', 't', 'Beef matured under controlled conditions to intensify its flavour.'),
    ('Emulsion', 't', 'A smooth mixture of fat and liquid.'),
    ('French meringue', 't', 'The uncooked meringue method: sugar is gradually whipped into egg whites.'),
    ('Gratinated', 't', 'Browned on top under heat.'),
    ('Monte', 't', 'Short for “monter au beurre”: a sauce enriched and emulsified with butter.'),
    ('Reduction', 't', 'A liquid simmered to concentrate its flavour.'),
    ('Sashimi', 't', 'A Japanese way of serving fish: sliced, to be eaten raw.'),
    ('Tempura', 't', 'A light batter. Food is dipped in it and fried until crisp.'),
    # dishes and sauces
    ('Alla parmigiana', 'd', 'A layered, baked preparation with tomato and cheese.'),
    ('Beignet', 'd', 'A French fried pastry or doughnut.'),
    ('Caesar dressing', 'd', 'A creamy dressing traditionally built around egg, anchovy, cheese and acidity.'),
    ('Cremoso', 'd', 'A silky, set chocolate cream.'),
    ('Frites', 'd', 'The French word for fries.'),
    ('Game chips', 'd', 'Thin slices of potato, fried until crisp.'),
    ('Gilda', 'd', 'A classic Basque pintxo (a bar snack on a skewer), traditionally combining olive, anchovy and chilli.'),
    ('Gravy', 'd', 'A savoury sauce made from cooking juices and stock.'),
    ('House dressing', 'd', 'Mustard, lemon, sherry and olive oil.'),
    ('Kraut', 'd', 'A fermented or pickled cabbage-style preparation. Ours is made with fennel.'),
    ('Piccata', 'd', 'A preparation with a bright sauce, typically involving butter, lemon or wine, and capers.'),
    ('Pomodoro', 'd', 'Italian for tomato: a simple tomato sauce.'),
    ('Schnitzel', 'd', 'Meat coated in crumbs and fried.'),
    ('Semifreddo', 'd', 'Italian for “half cold”: a soft, semi-frozen dessert.'),
    ('Tartare', 'd', 'Finely diced, seasoned meat.'),
    ('Tartare sauce', 'd', 'A mayonnaise-based sauce with pickled elements.'),
    ('Thousand Island', 'd', 'A mayonnaise-based dressing.'),
    ('Tiramisu', 'd', 'Italian for “pick me up”: a layered dessert of coffee-soaked sponge fingers and mascarpone cream.'),
    # ingredients
    ('Bone marrow', 'i', 'The rich centre of beef bones.'),
    ('Brown and white crab meat', 'i', 'Brown meat is the richer, darker meat from the body. White meat is sweeter and comes mainly from the claws and legs.'),
    ('Brown butter', 'i', 'Butter cooked until the milk solids toast and it tastes nutty.'),
    ('Chalk-stream trout', 'i', 'Trout raised in clear, mineral-rich chalk-stream water.'),
    ('Chilli crisp', 'i', 'A crunchy condiment of chilli in oil.'),
    ('Chuck', 'i', 'A flavourful cut of beef from the shoulder.'),
    ('Cornichons', 'i', 'Small pickled gherkins.'),
    ('Crisp capers', 'i', 'Capers fried until crunchy.'),
    ('Datterini', 'i', 'Small, sweet Italian plum tomatoes.'),
    ('Disaronno', 'i', 'An Italian amaretto liqueur.'),
    ('Emmental', 'i', 'A mild Swiss-style cheese.'),
    ('Gordal olive', 'i', 'A large Spanish green olive.'),
    ('Gorgonzola', 'i', 'An Italian blue cheese.'),
    ('Guindilla', 'i', 'A mild-to-medium Spanish (Basque) chilli.'),
    ('Kalamata olives', 'i', 'Dark Greek olives.'),
    ('Ladyfingers', 'i', 'Light, dry sponge fingers.'),
    ('Langoustine', 'i', 'A small, lobster-like shellfish.'),
    ('Longhorn', 'i', 'A traditional English breed of beef cattle.'),
    ('Mangalitsa', 'i', 'A heritage Hungarian pig breed, known for rich, marbled pork.'),
    ('Marsala', 'i', 'A fortified wine from Sicily.'),
    ('Mascarpone', 'i', 'A rich Italian fresh cheese.'),
    ('Melanzane', 'i', 'Italian for aubergines.'),
    ('Mirin', 'i', 'A sweet Japanese rice seasoning.'),
    ('Pastrami', 'i', 'Seasoned, cured beef. Ours is made from brisket and pulled.'),
    ('Picanha', 'i', 'The rump cap cut of beef.'),
    ('Potato bun', 'i', 'A soft, enriched burger bun.'),
    ('Poussin', 'i', 'A young chicken.'),
    ('Preserved lemon', 'i', 'Lemon cured in salt.'),
    ('Rib cap', 'i', 'The highly marbled outer muscle of the rib.'),
    ('Sherry vinegar', 'i', 'A Spanish wine vinegar with rounded, nutty acidity.'),
    ('Shio koji', 'i', 'A fermented rice seasoning made with salt and koji culture.'),
    ('Sweetheart cabbage', 'i', 'A compact, pointed cabbage, also called hispi.'),
    ('Yellowfin tuna', 'i', 'A large species of tuna.'),
]
