"""Part 1 helper: for each headword still without a decision, print the Vietnamese values and the
approved Russian senses line (to copy the English tags). Usage: part1_ru_lookup.py <start> <end>"""
import os
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import senses_tool_vi as T  # noqa: E402

start, end = int(sys.argv[1]), int(sys.argv[2])
aggp, decp, _ = T.part_paths('1')
rows = T.read_agg(aggp)
dec = T.read_decisions(decp)
with open(T.RU_SENSES, encoding='utf-8-sig') as f:
    ru = {}
    for l in f:
        l = unicodedata.normalize('NFC', l.rstrip('\n'))
        i = l.find(': {')
        if i > 0:
            ru[l[:i]] = l[i + 2:]
left = [h for h in rows if h not in dec and rows[h]['vals']]
for n, h in enumerate(left[start:end], start):
    vs = ' | '.join(f'{v}={c}' for v, c in rows[h]['vals'].items())
    print(f'#{n} {h} :: {vs}')
    print(f'   RU {ru.get(h, "(none)")}')
