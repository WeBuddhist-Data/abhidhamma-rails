"""Part 1 helper: for headwords of agg-part1.tsv lacking a decision, print prior-book (pi-1..pi-6) senses, compact. Writes nothing."""
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import senses_tool_pi7 as T  # noqa: E402
import sample_grep as G  # noqa: E402

agg, dec, start, end = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
rows = T.read_agg(agg)
d = T.read_decisions(dec)
left = [h for h in rows if h not in d and rows[h]['vals']]
prior = G.load()
for h in left[start:end]:
    hits = prior.get(h.lower(), [])
    vals = ' | '.join(rows[h]['vals'])
    if not hits:
        print(f'{h}  [{vals}]  --')
        continue
    seen = set()
    out = []
    for b, s in hits:
        s2 = s[1:-1]
        if s2 in seen:
            continue
        seen.add(s2)
        out.append(f'pi-{b}: {s2[:170]}')
    print(f'{h}  [{vals}]')
    for x in out[:2]:
        print('    ' + x)
