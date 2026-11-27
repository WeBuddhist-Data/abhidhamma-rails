"""For each headword: pi-7 senses entry (tags shortened) and every Burmese value with up to 6 segment ids.
usage: hwinfo.py hw [hw ...]"""
import re, sys, pathlib, collections
B = pathlib.Path(__file__).resolve().parents[5]
S = {l.split(': {', 1)[0]: l.split(': {', 1)[1][:-1] for l in (B / 'AI_translation/burmese/pi-7-pali-word-burmese-senses-plain.md').read_text(encoding='utf-8').splitlines()}
idx = collections.defaultdict(lambda: collections.defaultdict(list))
for l in (B / 'AI_translation/burmese/pi-7-keywords-by-reference-pali-burmese-plain.md').read_text(encoding='utf-8').splitlines():
    m = re.match(r'\[([^\]]+)\] (.*)', l)
    if not m: continue
    for p in m.group(2).split(', '):
        k, _, v = p.partition('='); idx[k.lower()][v].append(m.group(1))
for hw in sys.argv[1:]:
    ss = S.get(hw, '?').split('; ')
    print(hw + ': ' + ' || '.join(s.rsplit(': ', 1)[0][:75] + ' = ' + s.rsplit(': ', 1)[-1] for s in ss))
    print('     ' + ' | '.join(f"{v} {len(i)} {' '.join(i[:5])}" for v, i in idx[hw.lower()].items()))
