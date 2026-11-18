"""Part 4 helper: for headwords of agg-part4.tsv (index range), print the Vietnamese values, the English
hints, and the approved Russian senses line (tags only unless 'full'). Usage: part4_ru_lookup.py <start> <end> [full|multi]
'multi' prints only headwords with >1 Vietnamese value or a multi-sense / missing Russian line."""
import os
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import senses_tool_vi as T  # noqa: E402

start, end = int(sys.argv[1]), int(sys.argv[2])
mode = sys.argv[3] if len(sys.argv) > 3 else ''
aggp, decp, _ = T.part_paths('4')
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
    r = ru.get(h, '(none)')
    nsen = len(r[1:-1].split('; ')) if r.startswith('{') else 0
    if mode == 'multi' and len(rows[h]['vals']) < 2 and nsen == 1:
        continue
    vs = ' | '.join(f'{v}={c}' for v, c in rows[h]['vals'].items())
    print(f'#{n} {h} :: {vs}   [{rows[h]["eng"][:70]}]')
    if mode != 'full' and r.startswith('{') and r.endswith('}'):
        r = ' ;; '.join(s.rsplit(': ', 1)[0] for s in r[1:-1].split('; '))
    print(f'   RU {r if len(r) < 400 else r[:400] + "..."}')
print(f'-- total headwords with values: {len(hws)}; NDE-only: {len(rows) - len(hws)}')
