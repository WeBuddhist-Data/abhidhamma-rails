import re, sys, os
B = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
FILES = ['2-01-vitakkattika.md', '2-02-pitittika.md', '2-03-dassanenapahatabbattika.md',
         '2-04-dassanenapahatabbahetukattika.md', '2-05-acayagamittika.md', '2-06-sekkhattika.md',
         '2-07-parittattika.md', '2-08-parittarammanattika.md']
IDRE = re.compile(r'\^([0-9A-Za-z\-]+)\s*$')
DEV = {'०':'0','१':'1','२':'2','३':'3','४':'4','५':'5','६':'6','७':'7','८':'8','९':'9'}


def load(path):
    with open(path, encoding='utf-8') as f:
        raw = f.read()
    lines = [l.rstrip('\n') for l in raw.split('\n')]
    return raw, [l for l in lines if l.strip()]


def nums(s):
    s = ''.join(DEV.get(c, c) for c in s)
    s = IDRE.sub('', s)
    return re.findall(r'\d+', s)


out = []
for f in FILES:
    praw, P = load(os.path.join(B, 'pali', 'pi-7_split_chapters', f))
    hraw, H = load(os.path.join(B, 'hindi', 'pi-7-hindi-plain-rails_split_chapters', f))
    out.append(f'=== {f}: pali {len(P)} hindi {len(H)}')
    if '\n\n\n' in hraw:
        out.append('  DOUBLE BLANK in hindi')
    for i, (p, h) in enumerate(zip(P, H), 1):
        pid = IDRE.search(p); hid = IDRE.search(h)
        pid = pid.group(1) if pid else None; hid = hid.group(1) if hid else None
        tag = f'{f}:{i}:{pid}'
        if pid != hid:
            out.append(f'  IDMISMATCH {tag} hi={hid}')
        hs = IDRE.sub('', h)
        # numbers
        pn, hn = nums(p), nums(h)
        if sorted(pn) != sorted(hn):
            out.append(f'  NUM {tag} p={pn} h={hn}')
        # dashes
        pd = p.count('–') + p.count('—'); hd = h.count('–') + h.count('—')
        if pd != hd:
            out.append(f'  DASH {tag} p={pd} h={hd}')
        # heading
        if p.startswith('#') != h.startswith('#') or (p.startswith('#') and p.split(' ')[0] != h.split(' ')[0]):
            out.append(f'  HEAD {tag}')
        # latin outside brackets
        hb = re.sub(r'\[[^\]]*\]', '', hs)
        hb = re.sub(r'\([^)]*\)', lambda m: m.group(0) if not re.search('[A-Za-z]', m.group(0)) else m.group(0), hb)
        lat = re.findall(r'[A-Za-zāīūṃṅñṭḍṇḷ]{2,}', hb)
        if lat:
            out.append(f'  LATIN {tag} {lat[:6]}')
        # end punctuation
        if not h.startswith('#'):
            e = hs.rstrip()
            if not (e.endswith('।') or e.endswith('?') or e.endswith('…') or e.endswith('”') or e.endswith(')') or e.endswith(']')):
                out.append(f'  END {tag} ...{e[-25:]}')
            if '?' in p and '?' not in h:
                out.append(f'  QMISS {tag}')
        if '"' in h or "'" in h:
            out.append(f'  STRAIGHTQ {tag}')
        if 'siyā' in p.lower() and not hs.rstrip().endswith('?'):
            out.append(f'  SIYAQ {tag}')
        # pe
        pe = re.sub(r'…\s*pe\s*…', '…', p).count('…')
        if pe != h.count('…'):
            out.append(f'  ELL {tag} p={pe} h={h.count("…")}')
open(os.path.join(os.path.dirname(__file__), 'review_r3_align.out'), 'w', encoding='utf-8').write('\n'.join(out))
print(len(out))
