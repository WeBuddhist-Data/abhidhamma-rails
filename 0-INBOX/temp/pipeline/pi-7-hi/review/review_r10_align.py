import os, re, sys
ROOT = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
P = os.path.join(ROOT, "pali", "pi-7_split_chapters")
H = os.path.join(ROOT, "hindi", "pi-7-hindi-plain-rails_split_chapters")
FILES = sorted(f for f in os.listdir(P) if f.endswith('.md') and (f[:4] in ('4-16','4-17','4-18','4-19','4-20','4-21') or f.startswith('5-')))
IDRE = re.compile(r'\^([0-9a-z\-]+)\s*$')

def lines(path):
    with open(path, encoding='utf-8') as fh:
        raw = fh.read()
    return raw, [l for l in raw.split('\n') if l.strip()]

def pairs():
    for f in FILES:
        _, pl = lines(os.path.join(P, f))
        _, hl = lines(os.path.join(H, f))
        yield f, pl, hl

if __name__ == '__main__':
    tot = 0
    for f, pl, hl in pairs():
        rawh, _ = lines(os.path.join(H, f))
        dbl = rawh.count('\n\n\n')
        mism = 0
        for i, (a, b) in enumerate(zip(pl, hl)):
            ia = IDRE.search(a); ib = IDRE.search(b)
            if (ia and ia.group(1)) != (ib and ib.group(1)):
                mism += 1
                if mism < 4:
                    print('  MISMATCH', f, i+1, a[-40:], '|', b[-40:])
        nid = sum(1 for a in pl if IDRE.search(a))
        tot += nid
        print(f, len(pl), len(hl), 'ids', nid, 'mism', mism, 'dblblank', dbl)
    print('total ids', tot, 'files', len(FILES))
