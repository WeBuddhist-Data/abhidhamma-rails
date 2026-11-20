"""Part 8 helper: compact prior lines (pi-1 vi, pi-2 ru) for agg-part8.tsv rows [start, end),
plus decision lines of earlier parts (sample, 1-7) whose headword has the same stem.
Usage: python -I -X utf8 part8_prior.py START END [en]"""
import os
import sys
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('stv', os.path.join(HERE, 'senses_tool_vi.py'))
stv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stv)

ENDINGS = sorted(['ṃ', 'o', 'ā', 'a', 'e', 'i', 'ī', 'u', 'ū', 'ehi', 'esu', 'ānaṃ', 'assa', 'āya', 'ena', 'āni',
                  'aṃ', 'ato', 'asmiṃ', 'amhi', 'āyo', 'āhi', 'āsu', 'iyā', 'iyo', 'inaṃ', 'īnaṃ', 'ino', 'ini',
                  'ehi', 'ūnaṃ', 'uno', 'ave', 'ena', 'ā', 'aso', 'ani', 'ttā'], key=len, reverse=True)


def stem(h):
    h = h.lower().split(' ')[0]
    for e in ENDINGS:
        if h.endswith(e) and len(h) - len(e) >= 3:
            return h[:-len(e)]
    return h


start, end = int(sys.argv[1]), int(sys.argv[2])
want_en = len(sys.argv) > 3 and sys.argv[3] == 'en'
rows = stv.read_agg(os.path.join(HERE, 'agg-part8.tsv'))
idx = stv._prior_index()
earlier = {}
for k in ['sample', '1', '2', '3', '4', '5', '6', '7']:
    p = stv.part_paths(k)[1]
    if not os.path.exists(p):
        continue
    for line in stv._lines(p):
        if line.startswith('#') or ': {' not in line:
            continue
        h = line.split(': {', 1)[0]
        earlier.setdefault(stem(h), []).append(f'p{k} {line}')
for i, (h, r) in enumerate(rows.items(), 1):
    if i < start or i >= end:
        continue
    out = []
    for label, d in idx:
        if label == 'pi-2 en' and not want_en:
            continue
        for line in d.get(h.lower(), []):
            out.append(f'   [{label}] {line}')
    for line in earlier.get(stem(h), [])[:3]:
        out.append(f'   [{line[:line.index(" ")]}] {line[line.index(" ") + 1:]}')
    vals = ' | '.join(f'{v}={c}' for v, c in r['vals'].items())
    print(f'== {i} {h}\t{vals}\t{r["eng"][:80]}')
    for o in out:
        print(o)
