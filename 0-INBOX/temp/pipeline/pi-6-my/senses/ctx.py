"""Pāli context of a headword in given pi-6 segments: the Pāli words containing it (case-insensitive) and the
Burmese value mapped there. usage: ctx.py <headword> [id ...]   (no ids: every segment where it is a keyword)"""
import pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[5]
PALI = ROOT / 'AI_translation/pali/pi-6_split_chapters'
MAP = ROOT / 'AI_translation/burmese/pi-6-keywords-by-reference-pali-burmese-plain.md'
seg = {}
for f in sorted(PALI.glob('*.md')):
    buf = ''
    for l in f.read_text(encoding='utf-8').splitlines():
        buf += ' ' + l
        m = re.search(r'\^([\w-]+)\s*$', l)
        if m:
            seg[m.group(1)] = buf
            buf = ''
mp = {}
for l in MAP.read_text(encoding='utf-8').splitlines():
    m = re.match(r'\[([^\]]+)\] (.*)', l)
    if m:
        mp[m.group(1)] = [p.partition('=')[::2] for p in m.group(2).split(', ')]
hw = sys.argv[1]
ids = sys.argv[2:] or [i for i, ps in mp.items() if any(k.lower() == hw.lower() for k, _ in ps)]
first = hw.split()[0]
for i in ids:
    vals = [v for k, v in mp.get(i, []) if k.lower() == hw.lower()]
    words = sorted(set(w for w in re.findall(r"[\wāīūṃṅñṭḍṇḷ]+", seg.get(i, ''))
                       if first.lower() in w.lower()))
    print(f'{i}: {vals} | {" ".join(words)[:300]}')
