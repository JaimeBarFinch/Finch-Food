# Bar Finch Food: the floor team's food app

A phone app for the Bar Finch floor team, and the sister of the wine app. It holds every dish on the menu, what is on the plate, one line to sell it, the allergens the kitchen lists, and what to offer when a guest describes what they feel like. It also has courses, quizzes and flashcards. Staff can install it on their phones, and it works without a connection once it has been opened.

The dishes and allergens are copied from the Bar Finch Food Bible (November 2026). **There are no prices, costs or supplier details anywhere in this project.**

## Allergens: how the app handles them

- Allergens live in one file only: `tools/allergens.py`. Each record keeps the kitchen's own wording next to the list, and the build checks that the two agree.
- The app can show three things for a dish and an allergen: **listed**, **not confirmed** (the kitchen says "likely", "may apply", or has no confirmed list), or **not listed**. It never says "free from".
- Every dish page, the allergen grid and every allergen page say "Always confirm allergens with the kitchen before ordering", with the source and its date.
- The build refuses to run if a dish has no allergen record, or if a dish's text names an ingredient that points to an allergen its record does not list (butter without milk, soy without soya). The question then has to be written down in `QUERIES` in `tools/allergens.py`, and the app shows that allergen as "not confirmed" until the kitchen answers.
- The allergen course needs every question right.

## What's in it

**Info**
- **Dishes:** all dishes in menu order, with search, section filters and a "without this allergen" filter.
- **Each dish page:** the Sell it line, anything a guest may not expect, allergens, what is on the plate, cutlery and service, wines to offer (links to the wine app) and the kitchen words used.
- **Allergens:** the grid of every dish against the 14 allergens, and a page per allergen.
- **Guests:** "When a guest says…" for the common requests.
- **Reference:** the allergy steps, how the menu works, cutlery, kitchen terms, ingredients.

**Training**
- **Courses:** Allergens (100% to pass), Know the menu, Kitchen words, Talking about food.
- **Quizzes and flashcards**, built from the menu as it is today. Progress is kept on each phone.

## Putting it on GitHub (one time)

1. Create a **new, public** repository, for example `finch-food`.
2. Upload **everything inside this folder** (not the folder itself) in **one commit**. `index.html` must sit at the top level.
3. Check that `.nojekyll` is there. The Mac hides it; if it is missing, use Add file → Create new file, name it `.nojekyll`, leave it empty and commit.
4. Settings → Pages → Deploy from a branch → `main`, folder `/ (root)` → Save.
5. Wait for the green tick in the Actions tab (1–5 minutes). The address will be like `https://your-name.github.io/finch-food/`.

To see which version is live, open `<site>/sw.js` and read the `VERSION` line.

## Updating the menu

1. Change the dish notes in `tools/dishes_starters.py`, `dishes_mains.py` or `dishes_sides_desserts.py`.
2. Change the allergen record in `tools/allergens.py`, copying the kitchen's wording into `raw`.
3. Run `python3 tools/build_data.py build`. If it prints "NOT BUILT", fix what it lists and run it again.
4. Upload the whole folder again in one commit (at least `js/data.js` and `sw.js` change every time).

The guide is in `tools/content_guide.py` and the courses in `tools/content_training.py`. When the wine list changes, run `python3 tools/build_data.py wines <path to the wine app's js/data.js>` so the pairings are checked against it. When the pairings are approved, set `PAIRINGS_APPROVED = True` in `tools/build_data.py`.

## Privacy

GitHub Pages sites are public: anyone with the link can open the app. Training progress is stored only on each person's phone.

## Technical notes

- Plain HTML, CSS and JavaScript, with no build step in the browser and no outside services.
- The food app and the wine app share one web address, so this app keeps its progress under its own name (`finchfood.`) and its service worker only touches its own cache (`finch-food-…`).
- Fonts: Poppins (Indian Type Foundry), SIL Open Font License 1.1. See `fonts/OFL.txt`.
