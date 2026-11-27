"""KWIC of a Pāli word (case-insensitive substring) in given pi-5 segments, with the Burmese segment text near the
mapped value. usage: kw.py <word> <id> [id ...]"""
import pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[5]
def segs(d):
    seg = {}
    for f in sorted(d.glob('*.md')):
        buf = ''
        for l in f.read_text(encoding='utf-8').splitlines():
            buf += ' ' + l
            m = re.search(r'\^([\w-]+)\s*$', l)
            if m:
                seg[m.group(1)] = buf; buf = ''
    return seg
P = segs(ROOT / 'AI_translation/pali/pi-5_split_chapters')
bd = [p for p in (ROOT / 'AI_translation/burmese').glob('pi-5*split_chapters') if p.is_dir()]
B = segs(bd[0]) if bd else {}
w = sys.argv[1].lower()
for i in sys.argv[2:]:
    s = P.get(i, '')
    j = s.lower().find(w)
    print(f'{i} PI: …{s[max(0, j - 120):j + 120] if j >= 0 else s[:240]}…')
    if B:
        print(f'{i} MY: {B.get(i, "")[:400]}')
