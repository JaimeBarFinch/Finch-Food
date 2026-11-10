# Training courses for the food app. Only what is relevant to the Bar Finch menu.
#
# In a card:  {d:reuben}      becomes a link to that dish (its short name); in a quiz it becomes the plain name.
#             {al:fish}       becomes the list of dishes whose allergen record lists fish (built from allergens.py).
#             {unconfirmed}   becomes the list of dishes whose allergens are not fully confirmed.
#             {absent}        becomes the allergens that no dish lists.
#             {source}        becomes the name and date of the allergen source.
# quiz entries: (question, [options], index of the right option, why)
# A course can set pass_mark (default 0.8). The allergen course needs 1.0: every question right.
# A lesson can set auto=N to add N allergen questions built from allergens.py each time the quiz is played.
#
# Do not type allergen facts about a dish in the menu, kitchen or floor courses. Use the tokens in the
# allergen course so a menu change can never leave stale text behind.

COURSES = [
  # =====================================================================================================
  dict(id='allergens', title='Allergens', pass_mark=1.0,
       blurb='The 14 allergens, how we handle an allergy, and what is listed on our menu. You need every question right.', lessons=[
    dict(id='fourteen', title='The 14 allergens', cards=[
      ('Fourteen by law', 'UK food law names <b>14 allergens</b>. Whenever one of them is an ingredient in a dish, we must be able to tell the guest. You need to know all fourteen by name.'),
      ('The fourteen', '<b>Celery</b> · <b>Cereals containing gluten</b> (wheat, rye, barley, oats) · <b>Crustaceans</b> (prawns, crab, langoustines) · <b>Eggs</b> · <b>Fish</b> · <b>Lupin</b> · <b>Milk</b> · <b>Molluscs</b> (mussels, oysters, squid) · <b>Mustard</b> · <b>Tree nuts</b> · <b>Peanuts</b> · <b>Sesame</b> · <b>Soya</b> · <b>Sulphur dioxide and sulphites</b>.'),
      ('Pairs that get confused', '<b>Peanuts and tree nuts</b> are two separate allergens. So are <b>crustaceans and molluscs</b>. A guest may react to one and not the other, so never treat them as the same thing.'),
      ('Where they hide', '<b>Milk</b> covers butter, cream and cheese. <b>Eggs</b> are in mayonnaise and meringue. <b>Fish</b> includes anchovy, which turns up in dressings and sauces. <b>Mustard</b> is common in dressings. <b>Sulphites</b> are in wine and vinegar. <b>Gluten</b> is in bread, batter and crumb coatings.'),
      ('Outside the fourteen', 'Guests can be allergic to things that are not on the list. Honey, for example, is not one of the fourteen, and it is in some of our dishes. Treat any allergy a guest tells you about in the same way: write it down and ask the kitchen.'),
    ], quiz=[
      ('How many allergens does UK law require us to be able to tell guests about?', ['14', '8', '10', '20'], 0, 'Fourteen. Learn them all by name.'),
      ('Which of these is NOT one of the 14?', ['Honey', 'Celery', 'Lupin', 'Mustard'], 0, 'Honey is not one of the fourteen. A guest can still be allergic to it, so ask the kitchen.'),
      ('Butter, cream and cheese all come under which allergen?', ['Milk', 'Eggs', 'Soya', 'Sulphites'], 0, 'Milk covers everything made from it.'),
      ('Prawns, crab and langoustines are…', ['Crustaceans', 'Molluscs', 'Fish', 'Lupin'], 0, 'Crustaceans. Mussels, oysters and squid are molluscs, which is a separate allergen.'),
      ('Peanuts and tree nuts are…', ['Two separate allergens', 'The same allergen', 'Both kinds of sesame', 'Not on the list'], 0, 'They are listed separately. A guest may react to one and not the other.'),
      ('A guest is allergic to fish. Which ingredient should make you stop and check?', ['Anchovy', 'Capers', 'Cornichons', 'Fennel'], 0, 'Anchovy is a fish, and it hides in dressings and sauces.'),
      ('Where are sulphites most often found?', ['Wine and vinegar', 'Butter and cream', 'Bread and batter', 'Eggs and mayonnaise'], 0, 'Sulphites are a preservative, common in wine, vinegar and dried fruit.'),
    ]),
    dict(id='rules', title='When a guest has an allergy', cards=[
      ('The one rule', '<b>Always confirm allergens with the kitchen before ordering.</b> This app helps you find the right dishes quickly, but recipes and suppliers change, so the kitchen always has the final word.'),
      ('What the app shows', 'Each dish has one of three marks for each allergen. <b>● Listed</b>: the Food Bible lists it. <b>? Not confirmed</b>: the Food Bible says “likely”, “may apply” or has no confirmed list; treat it as present until the kitchen tells you otherwise. <b>Not listed</b>: the Food Bible does not list it. That is <b>not</b> the same as “free from”.'),
      ('Never guess', 'Never tell a guest a dish is safe from memory, from the description, or because it “shouldn’t” have something in it. Say “I’ll check with the kitchen”, and then check.'),
      ('Check the whole order', 'Sauces, sides and extras have their own allergens. A steak with a sauce is two things to check. So is anything offered on request, such as mayonnaise.'),
      ('Dishes not fully confirmed yet', '{unconfirmed}'),
      ('If you are not sure, stop', 'Do not send the order. Ask the kitchen first.'),
    ], quiz=[
      ('A guest tells you they have an allergy. What must always happen before the order goes in?', ['Confirm with the kitchen', 'Check the app and send the order', 'Ask a colleague on the floor', 'Suggest the guest chooses a salad'], 0, 'Always confirm allergens with the kitchen before ordering.'),
      ('In the app, a “?” against an allergen means…', ['Not confirmed: treat it as present until the kitchen says otherwise', 'The dish does not contain it', 'The guest should decide', 'It is only a trace'], 0, 'The Food Bible is not certain, so we are not either.'),
      ('The app shows nothing listed for nuts on a dish. What can you tell the guest?', ['“It isn’t listed. I’ll confirm with the kitchen.”', '“It’s nut-free.”', '“It’s safe for you.”', '“It probably has none.”'], 0, '“Not listed” is not the same as “free from”.'),
      ('Why does the kitchen have the final word?', ['Recipes and suppliers change', 'The app is always wrong', 'It is quicker', 'Guests prefer it'], 0, 'The app is a copy of the Food Bible on one date. The kitchen knows what is on the plate today.'),
      ('A guest with an egg allergy orders a steak with a sauce. What do you check?', ['The steak, the sauce and anything else on the order', 'Only the steak', 'Only the sauce', 'Nothing: steak has no egg'], 0, 'Every part of the order has its own allergens.'),
      ('You are not sure whether a dish is right for a guest with an allergy. You…', ['Stop, and ask the kitchen before sending the order', 'Send the order and mention it later', 'Tell the guest it should be fine', 'Take your best guess'], 0, 'If you are not sure, stop.'),
    ]),
    dict(id='ours', title='Allergens on our menu', auto=8, cards=[
      ('How to use this lesson', 'These lists are built from the allergen record in this app, which is copied from the {source}. They are here to help you remember. They do not replace checking with the kitchen.'),
      ('Fish', '{al:fish}'),
      ('Crustaceans', '{al:crustaceans}'),
      ('Milk', '{al:milk}'),
      ('Eggs', '{al:eggs}'),
      ('Cereals containing gluten', '{al:gluten}'),
      ('Mustard', '{al:mustard}'),
      ('Soya', '{al:soya}'),
      ('Sulphites', '{al:sulphites}'),
      ('Not listed for any dish so far', 'The Food Bible does not list {absent} for any dish. That can change with a new dish or a new supplier, so still check.'),
      ('Dishes not fully confirmed yet', '{unconfirmed}'),
    ], quiz=[]),
  ]),

  # =====================================================================================================
  dict(id='menu', title='Know the menu', blurb='Every dish, section by section: what is on the plate and what to say about it.', lessons=[
    dict(id='snacks', title='Snacks and starters', cards=[
      ('Oscietra caviar', '{d:caviar}: 30 g of Oscietra caviar with crème fraîche and chives. Oscietra is a variety of sturgeon caviar with a delicate, nutty flavour. One caviar spoon per table for up to four guests, two for more than four.'),
      ('The Reuben', '{d:reuben}: pulled pastrami, made from beef brisket, and Emmental in multigrain sourdough toasted in beef fat. It is served over fennel kraut dressed with Thousand Island.'),
      ('Longhorn rump tartare', '{d:tartare}: rump (picanha), seared, chilled and finely diced, mixed with capers, shallots, Dijon mustard, cornichons, olive oil, anchovies and chilli crisp. Finished with a herb salad and an egg yolk cured in soy and mirin. Game chips on the side.'),
      ('Dorset crab cakes', '{d:crabcakes}: brown and white crab meat with herbs, on a dry mashed-potato base. Served with preserved-lemon tartare sauce and a herb salad.'),
      ('Artichoke salad', '{d:artichoke}: Jerusalem artichokes, halved and roasted, dressed with walnut mole on a bed of black garlic purée. Mixed with Castelfranco, a lightly bitter Italian chicory, and finished with artichoke crisps and sesame oil.'),
      ('Thermidor lobster', '{d:lobster}: half or whole. The meat is carved out and put back in the shell. The kitchen has not yet written up the sauce, so ask before you describe it.'),
      ('Parmesan soufflé', '{d:souffle}: a roux-based soufflé with Parmesan and fresh truffle, finished with a béchamel-style sauce with more Parmesan and truffle. Double-baked: cooked once, then baked again for service.'),
      ('Bar Finch Caesar', '{d:caesar}: a chicken Caesar. Brined chicken, romaine and focaccia croutons, in a Caesar dressing finished with anchovy and Parmesan.'),
      ('Smoked trout', '{d:trout}: smoked chalk-stream trout, thinly sliced, with dill, parsley, crisp capers and lemon zest. Fresh and lightly smoky.'),
    ], quiz=[
      ('How many caviar spoons go down for a table of four?', ['One', 'Two', 'Four', 'None'], 0, 'One spoon per table for up to four guests, two for more than four.'),
      ('What are the artichokes in the artichoke salad dressed with?', ['Walnut mole', 'House dressing', 'Caesar dressing', 'Brown butter'], 0, 'A walnut mole, on a bed of black garlic purée.'),
      ('What does “double-baked” mean for the soufflé?', ['Cooked once, then baked again for service', 'Baked at twice the heat', 'Two soufflés per portion', 'Baked in two layers'], 0, 'It is cooked once, then baked again for service.'),
      ('What is the Reuben’s bread toasted in?', ['Beef fat', 'Brown butter', 'Olive oil', 'Clarified butter'], 0, 'Beef fat. Worth knowing for a guest who does not eat beef.'),
      ('What comes on the side of the tartare?', ['Game chips', 'Fries', 'Focaccia croutons', 'Sourdough'], 0, 'Game chips: thin slices of potato, fried until crisp.'),
      ('What is the base of the crab cakes?', ['Dry mashed potato', 'Rice', 'Polenta', 'Chickpeas'], 0, 'Dry mashed potato binds the crab and herbs.'),
      ('What is the egg yolk on the tartare cured in?', ['Soy and mirin', 'Salt and sugar', 'Sherry vinegar', 'Honey'], 0, 'Soy and mirin, a sweet Japanese rice seasoning.'),
      ('Which starter comes with chicken?', ['{d:caesar}', '{d:artichoke}', '{d:crabcakes}', '{d:trout}'], 0, 'The Bar Finch Caesar is a chicken Caesar.'),
      ('What are the Caesar’s croutons made from?', ['Focaccia', 'Sourdough', 'Potato bun', 'Ladyfingers'], 0, 'Focaccia croutons.'),
      ('What finishes the smoked trout?', ['Dill, parsley, crisp capers and lemon zest', 'Basil, chive and parsley', 'Tarragon and parsley', 'Capers, anchovies and parsley'], 0, 'Dill, parsley, capers fried until crunchy, and lemon zest.'),
      ('How can the Thermidor lobster be ordered?', ['Half or whole', 'Whole only', 'Half only', 'By weight'], 0, 'Ask the guest: half or whole.'),
    ]),
    dict(id='mains', title='Mains', cards=[
      ('Bar Finch hamburger', '{d:hamburger}: aged beef, a blend of rib cap and chuck, seared in beef fat. In a potato bun with American cheese, slow-cooked onions, pickles, ketchup and American mustard.'),
      ('Chicken pot pie', '{d:potpie}: topped with puff pastry and filled with a rich, reduced chicken stock with chestnut mushrooms and carrots. It takes 25 minutes, so tell the guest when you take the order.'),
      ('Steak frites', '{d:steakfrites}: 40-day-aged ribeye cooked in beef fat, finished with herb-infused brown butter and smoked bone-marrow butter. Served with fries. Cooked pink or well done.'),
      ('Chicken piccata', '{d:piccata}: poussin, pan-roasted and finished in the oven, with a reduction of roasted chicken stock and wine, capers and parsley.'),
      ('Mangalitsa pork schnitzel', '{d:schnitzel}: a Mangalitsa pork chop, brined in honey, sugar, soy and salt, cooked schnitzel-style and served with a fresh fennel salad.'),
    ], quiz=[
      ('Which two cuts are in the hamburger?', ['Rib cap and chuck', 'Rump and brisket', 'Picanha and chuck', 'Brisket and rib cap'], 0, 'Aged rib cap and chuck, seared in beef fat.'),
      ('How long does the chicken pot pie take?', ['25 minutes', '10 minutes', '15 minutes', '45 minutes'], 0, 'Twenty-five minutes. Tell the guest when you take the order.'),
      ('What do you ask a guest who orders the steak frites?', ['Pink or well done', 'Half or whole', 'With or without the bone', 'Grilled or fried'], 0, 'The steak is cooked pink or well done.'),
      ('What is a poussin?', ['A young chicken', 'A small lobster', 'A cut of pork', 'A kind of caper'], 0, 'A young chicken. Ours is pan-roasted and finished in the oven.'),
      ('The pork for the schnitzel is…', ['Mangalitsa', 'Longhorn', 'Dorset', 'Oscietra'], 0, 'Mangalitsa: a heritage Hungarian breed known for rich, marbled pork.'),
    ]),
    dict(id='sides', title='Sides and sauces', cards=[
      ('Fries and mash', '{d:fries}: soaked overnight in vinegar, served crisp and golden. {d:mash}: smooth and rich, made with reduced double cream and butter.'),
      ('The green sides', '{d:sweetheart}: sweetheart cabbage, refreshed until crisp and dressed with olive oil, lemon juice, salt and pepper. {d:mixedleaf}: soft leaves in the house dressing, finished with mint, parsley and dill. {d:greensbeans}: green beans and spinach, blanched and warmed in a butter emulsion.'),
      ('Béarnaise', '{d:bearnaise}: egg yolks and clarified butter, emulsified with a reduction of white wine vinegar and herbs: tarragon and parsley.'),
      ('Peppercorn sauce', '{d:peppercorn}: made from the pan flavours and crushed peppercorns, deglazed with brandy and port.'),
      ('Holstein sauce', '{d:holstein}: brown butter with capers, anchovies and parsley. Savoury, nutty and bright.'),
    ], quiz=[
      ('What are the fries soaked in overnight?', ['Vinegar', 'Brine', 'Milk', 'Beef fat'], 0, 'Vinegar.'),
      ('Which sauce is brown butter with capers, anchovies and parsley?', ['Holstein', 'Béarnaise', 'Peppercorn', 'Thousand Island'], 0, 'Holstein.'),
      ('What is the peppercorn sauce deglazed with?', ['Brandy and port', 'White wine', 'Marsala', 'Sherry vinegar'], 0, 'Brandy and port.'),
      ('Which herbs are in the Béarnaise?', ['Tarragon and parsley', 'Basil, chive and parsley', 'Mint, parsley and dill', 'Rosemary and thyme'], 0, 'Tarragon and parsley. Mint, parsley and dill finish the mixed leaf salad.'),
      ('“Greens & beans” is…', ['Green beans and spinach', 'Sweetheart cabbage and peas', 'Broad beans and kale', 'Mixed leaves and fennel'], 0, 'Green beans and spinach in a butter emulsion.'),
    ]),
    dict(id='desserts', title='Desserts', cards=[
      ('Tiramisu', '{d:tiramisu}: made in house. Coffee-soaked ladyfingers layered with mascarpone cream and finished with grated chocolate. It contains alcohol: Disaronno and marsala.'),
      ('Lemon meringue pie', '{d:lemonpie}: a smooth lemon custard made with double cream and eggs, set over a blond cake base and finished with French meringue.'),
      ('Chocolate cremoso', '{d:cremoso}: a rich, dense chocolate cream made with eggs, double cream and milk, finished with olive oil and sea salt.'),
      ('Honey & brandy semifreddo', '{d:semifreddo}: a semi-frozen Italian-style dessert flavoured with honey and brandy, with the texture of a soft frozen mousse.'),
      ('Beignet', '{d:beignet}: three pieces of deep-fried, squared doughnut dough, crisp outside and soft within, with crème fraîche and homemade jam.'),
    ], quiz=[
      ('Which two drinks are in the tiramisu?', ['Disaronno and marsala', 'Brandy and port', 'Rum and coffee liqueur', 'Sherry and brandy'], 0, 'Disaronno and marsala. Tell a guest who avoids alcohol.'),
      ('How many beignets are in a portion?', ['Three', 'Two', 'Four', 'Five'], 0, 'Three pieces.'),
      ('What finishes the chocolate cremoso?', ['Olive oil and sea salt', 'Grated chocolate', 'French meringue', 'Crème fraîche'], 0, 'Olive oil and sea salt.'),
      ('The semifreddo is flavoured with…', ['Honey and brandy', 'Lemon and cream', 'Coffee and chocolate', 'Jam and crème fraîche'], 0, 'Honey and brandy.'),
      ('What is the base of the lemon meringue pie?', ['A blond cake base', 'Shortcrust pastry', 'Ladyfingers', 'A biscuit crumb'], 0, 'The custard is set over a traditional blond cake base.'),
    ]),
    dict(id='table', title='At the table', cards=[
      ('Portions', 'Caviar: 30 g. Beignets: three pieces. Thermidor lobster: half or whole.'),
      ('Questions to ask', 'Steak: pink or well done. Lobster: half or whole. Fries: ketchup, mayonnaise or both. The chicken pot pie takes 25 minutes: say so when you take the order. Ketchup and mayonnaise are also available with the steak frites on request.'),
      ('Cutlery: mains and sides', 'Steak frites: steak knife and fork. Schnitzel: steak knife and main fork. Mash: a pasta spoon. Mixed leaf salad and greens & beans: a starter fork.'),
      ('Caviar spoons', 'One caviar spoon per table for up to four guests, two for more than four. The spoons never go to the kitchen porters. Wash them carefully by hand and put them back in their drawer.'),
      ('Cutlery: desserts', 'Every dessert takes a dessert spoon. The tiramisu, the lemon meringue pie and the beignets also take a starter fork. The cremoso and the semifreddo are spoon only.'),
    ], quiz=[
      ('What happens to a caviar spoon after service?', ['It is washed by hand and returned to its drawer', 'It goes to the kitchen porters with the cutlery', 'It is thrown away', 'It stays on the table'], 0, 'Caviar spoons are washed carefully by hand and put back in their drawer.'),
      ('What goes down with the mash?', ['A pasta spoon', 'A starter fork', 'A dessert spoon', 'A steak knife'], 0, 'A pasta spoon.'),
      ('Which desserts take a dessert spoon only?', ['Chocolate cremoso and semifreddo', 'Tiramisu and beignet', 'Lemon meringue pie and tiramisu', 'Beignet and semifreddo'], 0, 'The other three also take a starter fork.'),
      ('What do you offer with fries?', ['Ketchup, mayonnaise or both', 'Béarnaise', 'American mustard', 'Tartare sauce'], 0, 'Ask if they would like ketchup, mayonnaise or both.'),
      ('What cutlery goes down for the schnitzel?', ['Steak knife and main fork', 'Starter fork', 'Pasta spoon', 'Dessert spoon and starter fork'], 0, 'Steak knife and main fork.'),
    ]),
  ]),

  # =====================================================================================================
  dict(id='kitchen', title='Kitchen words', blurb='The techniques, cuts and ingredients behind the menu, in plain English.', lessons=[
    dict(id='cure', title='Brining, curing and smoking', cards=[
      ('Brine', 'A brine is a seasoned salt-water solution. Meat is soaked in it before cooking to add flavour and help it stay moist. The chicken in the {d:caesar} is brined. The pork for the {d:schnitzel} is brined in honey, sugar, soy and salt.'),
      ('Cure', 'To cure is to season and firm food with salt, sugar or a seasoned liquid, without heat. Pastrami, in the {d:reuben}, is seasoned, cured beef. The egg yolk on the {d:tartare} is cured in soy and mirin. Preserved lemon is lemon cured in salt.'),
      ('Smoke', 'The trout in the {d:trout} is smoked chalk-stream trout, sliced thin. The steak in the {d:steakfrites} is finished with a smoked bone-marrow butter.'),
      ('Ferment and pickle', 'The kraut under the {d:reuben} is a fermented or pickled preparation, made here with fennel. Cornichons are small pickled gherkins. The {d:fries} are soaked overnight in vinegar.'),
    ], quiz=[
      ('What does brining do?', ['Adds flavour and helps the meat stay moist', 'Makes the skin crisp', 'Removes the fat', 'Cooks the meat through'], 0, 'A brine seasons the meat and helps it hold its moisture.'),
      ('Which of these is NOT brined?', ['{d:hamburger}', '{d:schnitzel}', '{d:caesar}'], 0, 'The burger is seared in beef fat. The chicken in the Caesar and the pork for the schnitzel are brined.'),
      ('What is pastrami?', ['Seasoned, cured beef', 'Smoked pork', 'Air-dried ham', 'Salted fish'], 0, 'Ours is made from brisket and pulled.'),
      ('The kraut under the Reuben is made with…', ['Fennel', 'White cabbage', 'Sweetheart cabbage', 'Red onion'], 0, 'Fennel kraut, dressed with Thousand Island.'),
    ]),
    dict(id='butter', title='Butter, emulsions and sauces', cards=[
      ('Emulsion', 'An emulsion is a smooth mixture of fat and liquid. The {d:greensbeans} are warmed in a butter emulsion, which is what makes them glossy.'),
      ('Béarnaise', 'The {d:bearnaise} is an emulsion of egg yolks and clarified butter, with a reduction of white wine vinegar and herbs. Clarified butter is butter heated and strained so that only the clear butterfat is left.'),
      ('Monte', '“Monte” is short for “monter au beurre”: a sauce enriched and emulsified with butter. The kitchen’s notes for the {d:lobster} mention it.'),
      ('Brown butter', 'Butter cooked until the milk solids toast and it tastes nutty. It finishes the {d:steakfrites} and is the base of the {d:holstein}.'),
      ('Reduce and deglaze', 'A reduction is a liquid simmered to concentrate its flavour: the {d:piccata} is served with a reduction of roasted chicken stock and wine. To deglaze is to lift the caramelised flavours from a pan with liquid: the {d:peppercorn} is deglazed with brandy and port.'),
    ], quiz=[
      ('What is an emulsion?', ['A smooth mixture of fat and liquid', 'A liquid simmered until thick', 'A seasoned salt-water solution', 'A light batter'], 0, 'Fat and liquid, brought together until smooth.'),
      ('Brown butter tastes…', ['Nutty', 'Sour', 'Smoky', 'Sweet'], 0, 'The milk solids toast, which gives a nutty flavour.'),
      ('“Monte” means a sauce that is…', ['Enriched and emulsified with butter', 'Thickened with flour', 'Set with egg', 'Sharpened with vinegar'], 0, 'From “monter au beurre”.'),
      ('To deglaze is to…', ['Lift the caramelised flavours from a pan with liquid', 'Brown the top under heat', 'Boil briefly, then cool', 'Soak in salt water'], 0, 'The peppercorn sauce is deglazed with brandy and port.'),
      ('Which sauce is an emulsion of egg yolk and clarified butter?', ['Béarnaise', 'Peppercorn', 'Holstein', 'Thousand Island'], 0, 'Béarnaise, with a reduction of white wine vinegar and herbs.'),
    ]),
    dict(id='heat', title='Frying, grilling and finishing', cards=[
      ('Schnitzel', 'Meat coated in crumbs and fried. Ours is a Mangalitsa pork chop: the {d:schnitzel}.'),
      ('Sear', 'To brown the outside quickly over high heat. The beef for the {d:tartare} is seared, then chilled and diced. The {d:hamburger} is seared in beef fat.'),
      ('Pan-roast', 'The poussin for the {d:piccata} is pan-roasted, then finished in the oven.'),
      ('Gratinate and blanch', '<b>Gratinated</b>: browned on top under heat, the traditional finish for a Thermidor. <b>Blanch</b>: to boil briefly, then cool, like the vegetables in the {d:greensbeans}.'),
    ], quiz=[
      ('“Gratinated” means…', ['Browned on top under heat', 'Grated finely', 'Cooked slowly in fat', 'Fried in crumbs'], 0, 'A Thermidor is traditionally finished this way.'),
      ('A schnitzel is…', ['A thin cut of meat coated in breadcrumbs and fried', 'Meat cooked slowly in fat', 'A grilled chop', 'A cured sausage'], 0, 'Ours is a Mangalitsa pork chop.'),
      ('What happens to the beef for the tartare before it is diced?', ['It is seared, then chilled', 'It is smoked', 'It is brined', 'It is minced'], 0, 'Seared, chilled and finely diced.'),
      ('To blanch is to…', ['Boil briefly, then cool', 'Fry until golden', 'Soak overnight', 'Brown under the grill'], 0, 'The green beans and spinach are blanched first.'),
    ]),
    dict(id='beef', title='The beef on the menu', cards=[
      ('Longhorn and picanha', 'The {d:tartare} is made with Longhorn rump. Longhorn is a traditional English breed of beef cattle. Picanha is the rump cap.'),
      ('Brisket and pastrami', 'Pastrami is seasoned, cured beef. Ours, in the {d:reuben}, is made from brisket and pulled.'),
      ('Rib cap and chuck', 'The {d:hamburger} is aged beef, a blend of rib cap and chuck. Rib cap is the highly marbled outer muscle of the rib. Chuck is a flavourful cut from the shoulder.'),
      ('The steak', 'The steak in the {d:steakfrites} is ribeye, aged for 40 days. Dry-aged beef is matured under controlled conditions to intensify its flavour. It is cooked in beef fat and finished with herb-infused brown butter and smoked bone-marrow butter. Bone marrow is the rich centre of beef bones.'),
      ('Beef fat', 'Beef fat is used to toast the bread for the {d:reuben}, to sear the {d:hamburger} and to cook the steak. Remember it for guests who do not eat beef.'),
    ], quiz=[
      ('Picanha is…', ['The rump cap', 'The shoulder', 'The brisket', 'The outer muscle of the rib'], 0, 'The rump cap, used for the tartare.'),
      ('Our pastrami is made from which cut?', ['Brisket', 'Chuck', 'Rump', 'Rib cap'], 0, 'Brisket, cured and pulled.'),
      ('How long is the steak aged?', ['40 days', '14 days', '28 days', '60 days'], 0, 'Forty days.'),
      ('Which two butters finish the steak?', ['Herb brown butter and smoked bone-marrow butter', 'Clarified butter and garlic butter', 'Anchovy butter and brown butter', 'Tarragon butter and peppercorn butter'], 0, 'Herb-infused brown butter and smoked bone-marrow butter.'),
      ('Chuck comes from the…', ['Shoulder', 'Rump', 'Rib', 'Leg'], 0, 'A flavourful cut from the shoulder, in the burger blend.'),
    ]),
    dict(id='where', title='Where the dishes come from', cards=[
      ('Italy', 'Piccata, {d:tiramisu} (“pick me up”), {d:semifreddo} (“half cold”) and cremoso are Italian. So are Parmesan, mascarpone, marsala, focaccia and Castelfranco.'),
      ('France', '{d:bearnaise}, frites, {d:beignet}, poussin and cornichons are French words. A beignet is a French fried pastry or doughnut. Thermidor, soufflé, béchamel and roux are French too.'),
      ('Mexico', 'Mole is a Mexican-style sauce or paste, traditionally made by blending chillies, spices, seeds or nuts. Ours, in the {d:artichoke}, is a walnut mole.'),
      ('America', 'The {d:reuben}, with its pastrami and Thousand Island, and the {d:hamburger}, with American cheese and American mustard in a potato bun.'),
      ('Central Europe', 'A schnitzel is meat coated in crumbs and fried. Mangalitsa is a heritage Hungarian pig breed. Emmental is a Swiss-style cheese.'),
      ('Japan', 'Mirin is a sweet Japanese rice seasoning. It is used to cure the egg yolk on the {d:tartare}.'),
      ('Britain', 'Longhorn beef, Dorset crab and chalk-stream trout.'),
    ], quiz=[
      ('Which is a Hungarian breed of pig?', ['Mangalitsa', 'Longhorn', 'Picanha', 'Poussin'], 0, 'Mangalitsa, known for rich, marbled pork.'),
      ('Mirin comes from which kitchen?', ['Japanese', 'Italian', 'Spanish', 'French'], 0, 'Mirin is a sweet Japanese rice seasoning.'),
      ('“Semifreddo” means…', ['Half cold', 'Half sweet', 'Soft cream', 'Frozen honey'], 0, 'A soft, semi-frozen dessert.'),
      ('“Tiramisu” means…', ['Pick me up', 'Little cake', 'Coffee cream', 'In layers'], 0, 'Italian for “pick me up”.'),
    ]),
  ]),

  # =====================================================================================================
  dict(id='floor', title='Talking about food', blurb='How to describe a dish, and how to work out what a guest wants.', lessons=[
    dict(id='describe', title='Describing a dish', cards=[
      ('Three things', 'A good description covers three things: <b>what it is</b>, <b>how it is cooked</b>, and <b>what comes with it</b>. “Poussin, pan-roasted and finished in the oven, with a caper, parsley and wine sauce.”'),
      ('Use the “Sell it” line', 'Every dish page starts with one line you can say out loud. Learn it, then put it in your own words.'),
      ('Plain words', 'Words that work: <b>crisp</b>, <b>fresh</b>, <b>rich</b>, <b>smoky</b>, <b>sharp</b>, <b>soft</b>, <b>salty</b>. Leave out the words that say nothing, such as “exquisite” or “amazing”.'),
      ('Mention the surprise', 'Tell the guest what they may not expect: the anchovy in the {d:caesar}, the beef fat on the {d:reuben}, the alcohol in the {d:tiramisu}, the cured egg yolk on the {d:tartare}.'),
      ('When you don’t know', 'Say “I’ll check”, and ask the kitchen. That is always better than guessing.'),
    ], quiz=[
      ('A good description of a dish covers…', ['What it is, how it is cooked and what comes with it', 'Every ingredient, in order', 'How long it has been on the menu', 'What other guests think of it'], 0, 'Three things, in one or two sentences.'),
      ('Which word is best left out?', ['“Exquisite”', '“Crisp”', '“Smoky”', '“Rich”'], 0, 'It tells the guest nothing about the dish.'),
      ('A guest orders the Caesar. What is worth mentioning?', ['It comes with chicken, and the dressing is finished with anchovy', 'It is served warm', 'It has no dressing', 'It is the smallest salad'], 0, 'Tell the guest what they may not expect.'),
      ('You don’t know the answer to a guest’s question about a dish. You…', ['Say you will check, and ask the kitchen', 'Give your best guess', 'Tell them it is probably fine', 'Change the subject'], 0, 'Checking is always better than guessing.'),
    ]),
    dict(id='read', title='Reading the guest', cards=[
      ('Ask before you suggest', 'Two questions do most of the work: <b>how hungry are you?</b> and <b>is there anything you don’t eat?</b> Then offer one or two dishes, not five.'),
      ('Light or rich', 'Light: the {d:trout}, the {d:artichoke} and the {d:caesar}. Rich: the {d:souffle}, the {d:reuben}, the {d:hamburger} and the {d:steakfrites}.'),
      ('For the table', 'The {d:caviar} is for the table. The {d:beignet} comes as three pieces, so it shares easily. The {d:lobster} can be ordered whole.'),
      ('Sides and sauces', 'When a guest orders a main, mention a side. With the steak, mention the sauces: {d:bearnaise}, {d:peppercorn} or {d:holstein}.'),
      ('Changes', 'The Food Bible does not say what can and cannot be changed. Do not promise a change: ask the kitchen first.'),
      ('The Guests tab', 'In Info, the Guests tab lists what guests commonly say and what to offer.'),
    ], quiz=[
      ('A guest wants something light. Which would you offer?', ['{d:trout}', '{d:reuben}', '{d:steakfrites}', '{d:mash}'], 0, 'The smoked trout and the salads are the lightest things on the menu.'),
      ('A table wants something to share while they decide. Offer…', ['{d:caviar}', '{d:lemonpie}', '{d:mash}', '{d:peppercorn}'], 0, 'The caviar is 30 g for the table.'),
      ('A guest asks whether a dish can be changed. You…', ['Ask the kitchen before promising anything', 'Say yes', 'Say no', 'Offer a different dish straight away'], 0, 'Do not promise a change: ask the kitchen first.'),
      ('How many dishes should you suggest at once?', ['One or two', 'As many as possible', 'The whole section', 'None: let the guest choose'], 0, 'One or two, once you know what the guest wants.'),
    ]),
  ]),
]
