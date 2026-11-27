"""pi-2 context helper. For a headword: each segment id with its Burmese value and the Pāli words of that segment
matching stem_regex; with -s also a window of the Pāli and Burmese text.
usage: ctx_my.py [-s] headword stem_regex [value_substring]
       ctx_my.py -id id [id ...]          (Pāli + Burmese text of segments)"""
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
P = load(R / 'pali/pi-2_split_chapters'); B = load(R / 'burmese/pi-2-burmese-plain-zeroshot_split_chapters')
a = sys.argv[1:]
if a[0] == '-id':
    for i in a[1:]:
        print(f'[{i}] PI: {P.get(i, "?")[:700]}\n      MY: {B.get(i, "?")[:900]}')
    sys.exit()
show = a[0] == '-s'
if show: a = a[1:]
hw, stem = a[0], a[1]; vsub = a[2] if len(a) > 2 else None
M = R / 'burmese/pi-2-keywords-by-reference-pali-burmese-plain.md'
for l in M.read_text(encoding='utf-8').splitlines():
    m = re.match(r'\[([^\]]+)\] (.*)', l)
    if not m: continue
    for p in m.group(2).split(', '):
        k, _, v = p.partition('=')
        if k.lower() == hw.lower() and (vsub is None or vsub in v):
            i = m.group(1); pt = P.get(i, '')
            words = sorted(set(w for w in re.findall(r"[\w’']+", pt) if re.search(stem, w, re.I)))
            print(i, v, words)
            if show:
                k2 = pt.lower().find(stem.lower().strip('^$'))
                print('   PI:', pt[max(0, k2 - 120):k2 + 160])
                b = B.get(i, ''); k3 = b.find(v)
                print('   MY:', b[max(0, k3 - 150):k3 + 150])
