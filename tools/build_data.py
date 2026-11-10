#!/usr/bin/env python3
"""Build js/data.js for the Bar Finch food app.

  python3 tools/build_data.py build
        Merge the dish notes (dishes_*.py), the allergen record (allergens.py), the guide
        (content_guide.py) and the courses (content_training.py), run every check, then write
        js/data.js and give sw.js a new version so phones pick up the change.
        If any check fails, NOTHING is written and the reasons are printed.

  python3 tools/build_data.py wines <path-to-the-wine-app's js/data.js>
        Refresh data/wine-list-snapshot.json (wine ids and names only, no prices), so the
        "wines to offer" on each dish can be checked against the current wine list.

The checks are the safety net. The important ones:
  - every dish has an allergen record, and every record belongs to a dish;
  - the record matches the kitchen's own wording (`raw`), word for word;
  - a dish whose text names an ingredient that implies an allergen the record does not list
    (butter without milk, soy without soya, anchovy without fish ...) stops the build until the
    question is written down in allergens.QUERIES for the kitchen to answer;
  - a dish served with another dish (steak with fries) must cover that dish's allergens too;
  - nobody has typed "gluten-free", "safe for ..." or similar anywhere;
  - every fact that is written in two places still agrees.
"""
import datetime, hashlib, html, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
WINE_SNAP = os.path.join(ROOT, 'data', 'wine-list-snapshot.json')
WINE_APP = 'https://7shb49djdk-spec.github.io/finch-wine/'

# Set to True once the wine pairings have been approved. Until then each dish page says they are a draft.
PAIRINGS_APPROVED = False

SECTIONS = [('snacks', 'Bar snacks & small plates'), ('starters', 'Starters'), ('salads', 'Salads'), ('mains', 'Mains'),
            ('sides', 'Sides'), ('sauces', 'Sauces'), ('desserts', 'Desserts')]

# How each allergen is named in the kitchen's own wording (used to check `raw` against the record).
RAW_WORDS = {
    'celery': r'celery|celeriac', 'gluten': r'gluten|wheat', 'crustaceans': r'crustacean|shellfish', 'eggs': r'\beggs?\b',
    'fish': r'\bfish\b', 'lupin': r'lupin', 'milk': r'\bmilk\b|dairy', 'molluscs': r'mollusc', 'mustard': r'mustard',
    'nuts': r'\bnuts?\b|almond|hazelnut|walnut|pistachio', 'peanuts': r'peanut', 'sesame': r'sesame', 'soya': r'\bsoya?\b',
    'sulphites': r'sulphite|sulfite|sulphur',
}
UNSURE = r'likely|may |tbc|confirm'

# Ingredient words that imply an allergen. If a dish's text has the word and its record does not list
# the allergen, the build stops until the question is written in allergens.QUERIES.
IMPLIES = {
    'milk': r'butter|cream|crème|creme|cheese|milk|dairy|yoghurt|yogurt|custard|gorgonzola|emmental|parmesan|mascarpone|mozzarella|ricotta|burrata',
    'eggs': r'eggs?|mayonnaise|mayo|meringue|custard|aioli|aïoli|hollandaise',
    'fish': r'anchovy|anchovies|tuna|trout|salmon|cod|hake|bass|bream|mackerel|sardines?|worcestershire',
    'crustaceans': r'crab|langoustines?|prawns?|lobster|shrimps?|crayfish',
    'molluscs': r'oysters?|mussels?|clams?|squid|octopus|scallops?|snails?|cuttlefish',
    'gluten': r'bread|sourdough|bun|buns|brioche|focaccia|croutons?|breadcrumbs?|crumbs|flour|batter|tempura|cake|cakes|biscuits?|ladyfingers|dough|doughnut|pastry|pasta(?! spoon)|noodles?|couscous|wheat|barley|rye|soy sauce',
    'mustard': r'mustard|dijon',
    'soya': r'soy|soya|miso|tofu|edamame|tamari',
    'sulphites': r'wine|vinegar|sherry|port|marsala|madeira|cider',
    'nuts': r'nuts?|almonds?|hazelnuts?|walnuts?|pistachios?|pecans?|cashews?|pesto|praline|frangipane|amaretti|marzipan|nougat',
    'peanuts': r'peanuts?|satay',
    'sesame': r'sesame|tahini',
    'celery': r'celery|celeriac',
    'lupin': r'lupin',
}
# Things nobody may type in dish notes, guest tips or the non-allergen courses.
CLAIMS = r'\b[a-z]+[- ]free\b|free from|safe for|suitable for'

# Facts that the guide and the courses state in words. Each word must appear in the notes of exactly
# these dishes; if a recipe changes, the build stops and the guide has to be rewritten.
MENTIONS = [
    (r'anchov', {'gildas', 'tartare', 'caesar', 'holstein'}, 'anchovy'),
    (r'beef fat', {'reuben', 'hamburger', 'steakfrites'}, 'beef fat'),
    (r'honey', {'roastchicken', 'schnitzel', 'semifreddo'}, 'honey'),
    (r'\bbrin', {'caesar', 'roastchicken', 'schnitzel'}, 'brine'),
]


def refresh_wines(path):
    s = open(path, encoding='utf-8').read()
    d = json.loads(s[s.index('{'):s.rindex('}') + 1])
    out = dict(source='Bar Finch wine app (finch-wine js/data.js)', takenAt=d['takenAt'],
               wines=[dict(id=w['id'], short=w['short'], section=w['section'], glass=bool(w.get('glass'))) for w in d['wines']])
    json.dump(out, open(WINE_SNAP, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f"wine snapshot: {len(out['wines'])} wines, taken {out['takenAt']} -> {WINE_SNAP}")


def build():
    from content_dishes import D
    from allergens import A, QUERIES, SOURCE, SOURCE_DATE
    from content_guide import ALLERGENS, STEER, RULES, ALLERGY, GLOSS
    from content_training import COURSES
    WINES = {w['id']: w for w in json.load(open(WINE_SNAP, encoding='utf-8'))['wines']}
    wine_at = json.load(open(WINE_SNAP, encoding='utf-8'))['takenAt']
    KEYS = [a[0] for a in ALLERGENS]
    LABEL = {a[0]: a[1] for a in ALLERGENS}
    SEC = [s[0] for s in SECTIONS]
    GL = {g[0]: g for g in GLOSS}
    problems = []

    def need(cond, msg):
        if not cond:
            problems.append(msg)

    # ------------------------------------------------------------------ 1. every dish has an allergen record
    need(set(D) == set(A), f'dishes and allergen records differ: no allergen record for {sorted(set(D) - set(A))}; '
                           f'allergen records with no dish {sorted(set(A) - set(D))}')
    need(len(GL) == len(GLOSS), 'the glossary has a term twice')
    if problems:
        sys.exit('NOT BUILT, fix these first:\n- ' + '\n- '.join(problems))

    def note_no(note):          # the kitchen has answered "no" to a question
        return note.upper().startswith('KITCHEN CONFIRMED NO')

    def queries(did):           # open questions only
        return [(a, n) for a, n in QUERIES.get(did, []) if not note_no(n)]

    def covered(did):           # everything the app shows as listed or not confirmed for this dish
        return set(A[did]['contains']) | set(A[did].get('maybe', [])) | {a for a, _ in QUERIES.get(did, [])}

    # ------------------------------------------------------------------ 2. the record itself
    for did, r in A.items():
        has, maybe, opn, raw = r['contains'], r.get('maybe', []), r.get('open', False), r.get('raw', '')
        for a in has + maybe:
            need(a in KEYS, f'{did}: "{a}" is not one of the 14 allergen keys')
        need(not set(has) & set(maybe), f'{did}: an allergen is in both contains and maybe')
        need(has or opn, f'{did}: no allergen is stated. Copy the kitchen\'s list, or set open=True so the app shows "not confirmed"')
        need(raw or opn, f'{did}: there is no kitchen wording (raw). Set open=True so the app shows "not confirmed"')
        low = raw.lower()
        for a in KEYS:
            named = bool(re.search(RAW_WORDS[a], low))
            need(named == (a in has or a in maybe), f'{did}: the kitchen wording and the record disagree about {a} (wording: "{raw}")')
        unsure = bool(re.search(UNSURE, low))
        need(unsure == bool(maybe or (opn and raw)), f'{did}: the kitchen wording is {"" if unsure else "not "}hedged ("{raw}") but the record says otherwise')

    # ------------------------------------------------------------------ 3. the dish notes
    def text_of(d, with_terms=True):
        parts = [d.get(k, '') for k in ('name', 'sell', 'plate', 'making', 'portion', 'service', 'flag', 'alcohol')]
        if with_terms:
            parts += [GL[t][2] for t in d.get('terms', []) if t in GL]
        return ' '.join(parts)

    for did, d in D.items():
        for k in ('section', 'name', 'short', 'sell', 'plate'):
            need(d.get(k), f'{did}: no {k}')
        need(d.get('section') in SEC, f'{did}: unknown section {d.get("section")}')
        for t in d.get('terms', []):
            need(t in GL, f'{did}: the glossary has no entry for "{t}"')
        for c in d.get('with_', []):
            need(c in D, f'{did}: served with {c}, which is not a dish')
        seen = set()
        for wid, why in d.get('wines', []):
            need(wid in WINES, f'{did}: wine {wid} is not on the wine list (refresh data/wine-list-snapshot.json or change the pairing)')
            need(wid not in seen, f'{did}: wine {wid} is suggested twice')
            seen.add(wid)
        m = re.search(CLAIMS + r'|vegan|vegetarian|allerg', text_of(d, False).lower())
        need(not m, f'{did}: the notes say "{m.group(0) if m else ""}". Allergen and dietary claims belong in allergens.py only')
    if problems:
        sys.exit('NOT BUILT, fix these first:\n- ' + '\n- '.join(problems))

    # ------------------------------------------------------------------ 4. ingredients that imply an allergen
    triggered = {did: {} for did in D}        # dish -> {allergen: why}
    for did, d in D.items():
        low = text_of(d).lower()
        for a, pat in IMPLIES.items():
            m = re.search(r'\b(?:' + pat + r')\b', low)
            if m:
                triggered[did][a] = f'the notes mention "{m.group(0)}"'
    for did, d in D.items():
        for c in d.get('with_', []):
            for a in sorted(covered(c) - {a for a, n in QUERIES.get(c, []) if note_no(n)}):
                triggered[did].setdefault(a, f'it is served with {D[c]["short"]}, which has {a} listed or in question')
    for did in D:
        for a, why in triggered[did].items():
            need(a in covered(did),
                 f'ALLERGEN QUESTION, {did}: {why}, but {LABEL[a]} is not in its allergen record. Ask the kitchen. '
                 f'Until they answer, add ({a!r}, "<why>") to QUERIES[{did!r}] in allergens.py so the app shows it as not confirmed')
    for did, qs in QUERIES.items():
        need(did in D, f'QUERIES: {did} is not a dish')
        for a, note in qs:
            need(a in KEYS, f'QUERIES {did}: "{a}" is not an allergen key')
            if did in D and a in KEYS:
                need(a not in A[did]['contains'] and a not in A[did].get('maybe', []),
                     f'QUERIES {did}: {a} is now in the record, so delete the question')
                need(note_no(note) or a in triggered[did],
                     f'QUERIES {did}: nothing in the notes points to {a} any more, so delete the question')

    # ------------------------------------------------------------------ 5. facts written in two places
    for pat, ids, word in MENTIONS:
        found = {did for did, d in D.items() if re.search(pat, text_of(d, False).lower())}
        need(found == ids, f'the guide and courses say {word} is in {sorted(ids)}, but the dish notes mention it in {sorted(found)}')

    def has(did, key, *words):
        v = D.get(did, {}).get(key, '')
        for w in words:
            need(w.lower() in v.lower(), f'{did}.{key} no longer says "{w}": the guide and the courses still do')
    has('gildas', 'portion', 'Two skewers')
    has('langoustines', 'portion', 'Three')
    has('beignet', 'portion', 'Three')
    has('roastchicken', 'portion', 'Half or whole')
    has('steakfrites', 'flag', 'pink or well done')
    has('steakfrites', 'plate', '40-day')
    has('steakfrites', 'service', 'Steak knife and fork', 'ketchup', 'mayonnaise')
    has('schnitzel', 'service', 'Steak knife and main fork')
    has('fries', 'service', 'ketchup', 'mayonnaise')
    has('fries', 'plate', 'vinegar')
    has('mash', 'service', 'Pasta spoon')
    has('mixedleaf', 'service', 'Starter fork')
    has('greensbeans', 'service', 'Starter fork')
    for did in ('tiramisu', 'lemonpie', 'beignet'):
        has(did, 'service', 'Dessert spoon and starter fork')
    for did in ('cremoso', 'semifreddo'):
        need(D[did].get('service') == 'Dessert spoon.', f'{did}: no longer "Dessert spoon." only: the table lesson says spoon only')
    has('tiramisu', 'alcohol', 'Disaronno and marsala')
    has('peppercorn', 'alcohol', 'brandy and port')
    has('semifreddo', 'alcohol', 'brandy')
    need(len(SECTIONS) == 7, 'the guide says "seven sections"')
    need(all(any(d['section'] == s for d in D.values()) for s in SEC), 'a section has no dishes')

    # ------------------------------------------------------------------ 6. status and tokens
    def status(did):
        r = A[did]
        return 'check' if (r.get('open') or r.get('maybe') or queries(did)) else 'ok'

    def dlink(t, where, plain=False):
        def rep(m):
            did = m.group(1)
            if did not in D:
                problems.append(f'{where}: names the dish {did}, which is not on the menu')
                return '?'
            nm = D[did]['short']
            return nm if plain else f'<a class="wl" href="#info-dish-{did}">{html.escape(nm)}</a>'
        return re.sub(r'\{d:([a-z0-9]+)\}', rep, t)

    def links(ids):
        return ', '.join(f'<a class="wl" href="#info-dish-{i}">{html.escape(D[i]["short"])}</a>' for i in ids)

    order = [did for s in SEC for did in D if D[did]['section'] == s]
    unconfirmed = [did for did in order if status(did) == 'check']
    absent = [a for a in KEYS if not any(a in covered(did) for did in D)]
    source = f'{SOURCE}, {SOURCE_DATE}'

    def tokens(t, where):
        def al(m):
            a = m.group(1)
            if a not in KEYS:
                problems.append(f'{where}: unknown allergen {a}')
                return '?'
            yes = [d for d in order if a in A[d]['contains']]
            q = [d for d in order if a not in A[d]['contains'] and (a in A[d].get('maybe', []) or a in [x for x, _ in queries(d)])]
            out = ('Listed for: ' + links(yes) + '.') if yes else 'Not listed for any dish.'
            if q:
                out += ' <b>Not confirmed</b> for: ' + links(q) + '.'
            return out
        t = re.sub(r'\{al:([a-z]+)\}', al, t)
        if '{unconfirmed}' in t:
            t = t.replace('{unconfirmed}', (
                'The Food Bible does not yet give a full, confirmed list for: ' + links(unconfirmed) +
                '. Each dish page shows what is in question. For these, ask the kitchen every time.')
                if unconfirmed else 'Every dish currently has a confirmed list. Still check with the kitchen.')
        if '{absent}' in t:
            names = [LABEL[a].lower() for a in absent]
            t = t.replace('{absent}', (', '.join(names[:-1]) + ' or ' + names[-1]) if len(names) > 1 else (names[0] if names else 'none of the fourteen'))
        return t.replace('{source}', html.escape(source))

    # ------------------------------------------------------------------ 7. guide
    alcohol_ids = [did for did in order if D[did].get('alcohol')]
    steer = []
    for s in STEER:
        ids = alcohol_ids if s.get('auto') == 'alcohol' else s['dishes']
        for x in ids:
            need(x in D, f'guests "{s["q"]}": {x} is not a dish')
        for a, dids in s.get('needs', []):
            for x in dids:
                need(x in D and a in A[x]['contains'], f'guests "{s["q"]}": the tip relies on {x} listing {a}, and it no longer does')
        m = re.search(CLAIMS, s['tip'].lower())
        need(not m, f'guests "{s["q"]}": the tip says "{m.group(0) if m else ""}"')
        steer.append(dict(q=s['q'], dishes=ids, tip=s['tip']))
    alcohol_txt = 'Named in the recipe: ' + '; '.join(f'{D[d]["short"]} ({D[d]["alcohol"]})' for d in alcohol_ids) + '. If it matters to the guest, check with the kitchen.'
    rules = [dict(t=t, b=b.replace('{count}', str(len(D))).replace('{alcohol}', alcohol_txt)) for t, b in RULES]

    # ------------------------------------------------------------------ 8. courses
    ids_seen = set()
    courses = []
    for c in COURSES:
        need('-' not in c['id'] and c['id'] not in ids_seen, f'course id {c["id"]} is repeated or has a hyphen')
        ids_seen.add(c['id'])
        lessons, lseen = [], set()
        for l in c['lessons']:
            where = f"course {c['id']}/{l['id']}"
            need('-' not in l['id'] and l['id'] not in lseen, f'{where}: lesson id is repeated or has a hyphen')
            lseen.add(l['id'])
            if c['id'] != 'allergens':
                blob = ' '.join(b for _, b in l['cards']) + ' ' + ' '.join(q + ' ' + ' '.join(o) + ' ' + w for q, o, _, w in l['quiz'])
                m = re.search(CLAIMS + r'|allerg', blob.lower())
                need(not m, f'{where}: says "{m.group(0) if m else ""}". Allergen teaching belongs in the allergen course, built from allergens.py')
            quiz = []
            for q, opts, a, why in l['quiz']:
                o = [dlink(x, where, True) for x in opts]
                need(len(set(o)) == len(o), f'{where}: duplicate options in "{q}"')
                need(0 <= a < len(o), f'{where}: bad answer index in "{q}"')
                quiz.append(dict(q=dlink(q, where, True), o=o, a=o[a], why=dlink(why, where, True)))
            need(quiz or l.get('auto'), f'{where}: no quiz')
            lessons.append(dict(id=l['id'], title=l['title'], auto=l.get('auto', 0),
                                cards=[dict(h=h, b=tokens(dlink(b, where), where)) for h, b in l['cards']], quiz=quiz))
        courses.append(dict(id=c['id'], title=c['title'], blurb=c['blurb'], **{'pass': c.get('pass_mark', 0.8)}, lessons=lessons))
    need(any(c['id'] == 'allergens' and c['pass'] == 1.0 for c in courses), 'the allergen course must exist and need 100%')

    if problems:
        sys.exit('NOT BUILT, fix these first:\n- ' + '\n- '.join(problems))

    # ------------------------------------------------------------------ 9. write
    dishes = []
    for did in order:
        d, r = D[did], A[did]
        out = dict(id=did, section=d['section'], name=d['name'], short=d['short'], sell=d['sell'], plate=d['plate'])
        for k in ('making', 'portion', 'service', 'flag', 'alcohol'):
            if d.get(k):
                out[k] = d[k]
        out['terms'] = d.get('terms', [])
        out['withs'] = d.get('with_', [])
        out['wines'] = [dict(id=w, short=WINES[w]['short'], glass=WINES[w]['glass'], why=why) for w, why in d.get('wines', [])]
        out['al'] = dict(has=[a for a in KEYS if a in r['contains']], maybe=[a for a in KEYS if a in r.get('maybe', [])],
                         open=bool(r.get('open')), raw=r.get('raw', ''), q=[dict(a=a, note=n) for a, n in queries(did)])
        dishes.append(out)

    today = datetime.date.today().isoformat()
    data = dict(builtAt=today, source=SOURCE, sourceDate=SOURCE_DATE, wineApp=WINE_APP, wineListAt=wine_at,
                pairingsApproved=PAIRINGS_APPROVED,
                sections=[dict(key=k, label=v) for k, v in SECTIONS],
                allergens=[dict(key=k, label=l, short=s, code=c, eg=e) for k, l, s, c, e in ALLERGENS],
                dishes=dishes, steer=steer, rules=rules, allergy=ALLERGY,
                gloss=[dict(t=t, k=k, d=d) for t, k, d in sorted(GLOSS, key=lambda g: g[0].lower())], courses=courses)
    js = '/* Generated by tools/build_data.py from the Bar Finch Food Bible. Do not edit by hand. */\n'
    js += 'window.FINCH = ' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ';\n'
    open(os.path.join(ROOT, 'js', 'data.js'), 'w', encoding='utf-8').write(js)
    # a new cache version for the service worker, so installed phones pick up the change
    h = hashlib.sha1()
    for f in ('index.html', 'css/app.css', 'js/app.js', 'js/data.js', 'manifest.webmanifest'):
        h.update(open(os.path.join(ROOT, f), 'rb').read())
    swp = os.path.join(ROOT, 'sw.js')
    sw = re.sub(r"var VERSION = '[^']*';", f"var VERSION = 'finch-food-{today}-{h.hexdigest()[:8]}';", open(swp, encoding='utf-8').read())
    open(swp, 'w', encoding='utf-8').write(sw)

    print(f'built js/data.js: {len(dishes)} dishes, {len(steer)} guest rows, {len(GLOSS)} glossary terms, '
          f'{sum(len(c["lessons"]) for c in courses)} lessons')
    if unconfirmed:
        print(f'\n{len(unconfirmed)} dishes are shown as NOT FULLY CONFIRMED until the kitchen answers:')
        for did in unconfirmed:
            r = A[did]
            bits = []
            if r.get('open'):
                bits.append('no confirmed list')
            if r.get('maybe'):
                bits.append('unsure: ' + ', '.join(r['maybe']))
            for a, n in queries(did):
                bits.append(f'question on {a}: {n}')
            print(f'  - {D[did]["name"]}: ' + '; '.join(bits))
    if not PAIRINGS_APPROVED:
        print('\nWine pairings are marked as a draft (PAIRINGS_APPROVED = False in tools/build_data.py).')


if __name__ == '__main__':
    if len(sys.argv) >= 3 and sys.argv[1] == 'wines':
        refresh_wines(sys.argv[2])
    elif len(sys.argv) >= 2 and sys.argv[1] == 'build':
        build()
    else:
        print(__doc__)
