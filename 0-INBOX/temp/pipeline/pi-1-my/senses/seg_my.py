"""Print Pāli and Burmese text of segment ids, optionally only a window around a Pāli word.
usage: seg_my.py [-w pali_substring] id [id ...]"""
import sys, re, pathlib
R = pathlib.Path(__file__).resolve().parents[5] / 'AI_translation'
def load(d):
    m = {}
    for f in sorted(d.glob('*.md')):
        buf = []
        for l in f.read_text(encoding='utf-8').splitlines():
            if not l.strip() or l.startswith('---'):
                continue
            buf.append(l)
            mm = re.search(r'\^([0-9A-Za-z-]+)\s*$', l)
            if mm:
                m.setdefault(mm.group(1), ' '.join(buf)); buf = []
    return m
P = load(R / 'pali/pi-1_split_chapters'); B = load(R / 'burmese/pi-1-burmese-plain-zeroshot_split_chapters')
args = sys.argv[1:]; w = None
if args and args[0] == '-w': w = args[1]; args = args[2:]
for i in args:
    p = P.get(i, '?'); b = B.get(i, '?')
    if w and w.lower() in p.lower():
        k = p.lower().find(w.lower()); p = p[max(0, k-150):k+150]
        b = b[:600]
    else:
        p = p[:400]; b = b[:400]
    print(f'[{i}] PI: {p}\n      MY: {b}')
