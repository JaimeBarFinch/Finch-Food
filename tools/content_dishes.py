# Staff notes for every dish, keyed by a short id with no hyphens (the app's links split on hyphens).
# The three files below hold the text, in menu order; this file only merges them.
from dishes_starters import D as _A
from dishes_mains import D as _B
from dishes_sides_desserts import D as _C

D = {}
for part in (_A, _B, _C):
    for k in part:
        assert k not in D, k
        assert '-' not in k, f'{k}: dish ids must not contain a hyphen'
    D.update(part)
