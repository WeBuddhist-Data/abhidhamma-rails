"""Part 2 helper: for headwords of agg-part2.tsv (index range), print the Vietnamese values, the English
hints, and the approved Russian senses line (to copy the English tags). Also flags headwords already
decided in decisions-part1.txt (for family consistency). Usage: part2_ru_lookup.py <start> <end>"""
import os
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import senses_tool_vi as T  # noqa: E402

start, end = int(sys.argv[1]), int(sys.argv[2])
aggp, decp, _ = T.part_paths('2')
rows = T.read_agg(aggp)
p1 = T.read_decisions(T.part_paths('1')[1])
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
    print(f'#{n} {h} :: {vs}   [{rows[h]["eng"][:80]}]')
    r = ru.get(h, '(none)')
    print(f'   RU {r if len(r) < 400 else r[:400] + "..."}')
