"""Part 3 helper: for headwords of agg-part3.tsv (index range), print the Vietnamese values, the English
hints, and the approved Russian senses line (to copy the English tags). Usage: part3_ru_lookup.py <start> <end> [full]"""
import os
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import senses_tool_vi as T  # noqa: E402

start, end = int(sys.argv[1]), int(sys.argv[2])
full = len(sys.argv) > 3
aggp, decp, _ = T.part_paths('3')
rows = T.read_agg(aggp)
with open(T.RU_SENSES, encoding='utf-8-sig') as f:
    ru = {}
    for l in f:
        l = unicodedata.normalize('NFC', l.rstrip('\n'))
        i = l.find(': {')
        if i > 0:
            ru[l[:i]] = l[i + 2:]
hws = [h for h in rows if rows[h]['vals']]
for n, h in enumerate(hws[start:end], start):
    vs = ' | '.join(f'{v}={c}' for v, c in rows[h]['vals'].items())
    print(f'#{n} {h} :: {vs}   [{rows[h]["eng"][:70]}]')
    r = ru.get(h, '(none)')
    if not full:
        # strip Russian values, keep tags only
        if r.startswith('{') and r.endswith('}'):
            r = ' ;; '.join(s.rsplit(': ', 1)[0] for s in r[1:-1].split('; '))
    print(f'   RU {r if len(r) < 400 else r[:400] + "..."}')
