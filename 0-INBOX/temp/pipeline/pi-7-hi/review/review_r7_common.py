import re, sys
F = '3-09-mahantaraduka.md'
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
P = ROOT + r'\pali\pi-7_split_chapters\\' + F
H = ROOT + r'\hindi\pi-7-hindi-plain-rails_split_chapters\\' + F
E = ROOT + r'\english\pi-7-english-plain-zeroshot_split_chapters\\' + F

def load(path):
    with open(path, encoding='utf-8') as f:
        raw = f.read().split('\n')
    out = []  # (nonempty_no, physical_no, text)
    n = 0
    for i, l in enumerate(raw, 1):
        if l.strip():
            n += 1
            out.append((n, i, l))
    return raw, out

IDRE = re.compile(r'\^([\w-]+)\s*$')

def segs(lines):
    """assign each nonempty line the block id of its segment (id at end of the segment's last line)"""
    res = []
    pending = []
    for t in lines:
        pending.append(t)
        m = IDRE.search(t[2])
        if m:
            for x in pending:
                res.append((x, m.group(1)))
            pending = []
    for x in pending:
        res.append((x, None))
    return res

def dyad_of(lines):
    """map nonempty line no -> current dyad heading (Pali, level 6 '...dukaṃ')"""
    cur = None
    d = {}
    for n, i, t in lines:
        m = re.match(r'^###### (\S*duka\S*) \^', t)
        if m:
            cur = m.group(1)
        d[n] = cur
    return d
