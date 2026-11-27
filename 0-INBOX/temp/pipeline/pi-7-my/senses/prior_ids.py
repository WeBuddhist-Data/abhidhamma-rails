"""Where a Pāli keyword (case-insensitive) occurs in the pi-1 … pi-6 Burmese maps: book, value, count, first ids.
usage: prior_ids.py hw [hw ...]"""
import collections, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[5] / 'AI_translation/burmese'
want = {h.lower() for h in sys.argv[1:]}
res = collections.defaultdict(lambda: collections.defaultdict(list))
for n in range(1, 7):
    for l in (ROOT / f'pi-{n}-keywords-by-reference-pali-burmese-plain.md').read_text(encoding='utf-8').splitlines():
        m = re.match(r'\[([^\]]+)\] (.*)', l)
        if not m: continue
        for p in m.group(2).split(', '):
            k, _, v = p.partition('=')
            if k.lower() in want: res[k.lower()][(n, v)].append(m.group(1))
for h in sys.argv[1:]:
    for (n, v), ids in res[h.lower()].items():
        print(f'{h}\tpi-{n}\t{v}\t{len(ids)}\t{" ".join(ids[:6])}')
