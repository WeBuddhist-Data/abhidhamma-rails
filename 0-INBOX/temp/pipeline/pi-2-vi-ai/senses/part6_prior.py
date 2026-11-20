"""Part 6 helper: compact prior lines (pi-1 vi, pi-2 ru) for agg-part6.tsv rows [start, end).
Usage: python -I -X utf8 part6_prior.py START END [en]
Prints '== idx hw<TAB>values' and the prior lines only when they exist (en only when 'en' given)."""
import os
import sys
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('stv', os.path.join(HERE, 'senses_tool_vi.py'))
stv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stv)

start, end = int(sys.argv[1]), int(sys.argv[2])
want_en = len(sys.argv) > 3 and sys.argv[3] == 'en'
rows = stv.read_agg(os.path.join(HERE, 'agg-part6.tsv'))
idx = stv._prior_index()
for i, (h, r) in enumerate(rows.items(), 1):
    if i < start or i >= end:
        continue
    out = []
    for label, d in idx:
        if label == 'pi-2 en' and not want_en:
            continue
        for line in d.get(h.lower(), []):
            out.append(f'   [{label}] {line}')
    vals = ' | '.join(f'{v}={c}' for v, c in r['vals'].items())
    print(f'== {i} {h}\t{vals}')
    for o in out:
        print(o)
