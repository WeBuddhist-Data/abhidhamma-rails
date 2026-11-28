"""r6: template grouping for pi-6 RU review (9-01..9-03 dhammayamaka).
Usage: python r6_tpl.py <mode> [files...]
mode: tpl  -> unique Pāli sentence templates (K/A/B normalised) with their Russian templates
      seq  -> per line, compare K/A/B member sequences
      tense -> per line, Pāli tense sequence vs Russian tense sequence
      show <file> <from> <to> -> interleave lines
"""
import re, sys, collections

BASE = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
FILES = ['9-01-dhammayamaka.md', '9-02-dhammayamaka.md', '9-03-dhammayamaka.md']

def load(f):
    p = open(BASE + '\\pali\\pi-6_split_chapters\\' + f, encoding='utf-8').read().split('\n')
    r = open(BASE + '\\russian\\pi-6-russian-plain-rails_split_chapters\\' + f, encoding='utf-8').read().split('\n')
    return p, r

def pali_norm(s):
    seq = []
    def rep(m):
        t = m.group(0).lower()
        c = 'B' if t.startswith('aby') else 'A' if t.startswith('akus') else 'K'
        seq.append(c)
        return c + '·'
    s = re.sub(r'abyākat|akusal|kusal', rep, s, flags=re.I)
    return s, seq

def ru_norm(s):
    seq = []
    def rep(m):
        t = m.group(0).lower()
        c = 'B' if t.startswith('эти') else 'A' if t.startswith('небл') else 'K'
        seq.append(c)
        return c + '·'
    s = re.sub(r'этически неопределённ|неблаг|благ', rep, s, flags=re.I)
    return s, seq

def sentences(s):
    s = re.sub(r'\s*\^[\w-]+\s*$', '', s)
    parts = re.split(r'(?<=[.?!])\s+(?=[A-ZĀĪŪṄÑṬḌṆḶṂ(А-ЯЁ«])', s)
    return [x for x in parts if x.strip()]

P_T = [('uppajjissa', 'F'), ('uppajjitth', 'P'), ('uppajja', 'N'), ('uppajji', 'N'),
       ('nirujjhissa', 'F'), ('nirujjhitth', 'P'), ('nirujjha', 'N'),
       ('bhāvessa', 'F'), ('bhāvayittha', 'P'), ('bhāveti', 'N'), ('bhāvent', 'N'), ('bhāvesi', 'P'), ('bhāvayi', 'P'),
       ('pajahissa', 'F'), ('pajahitth', 'P'), ('pajahi', 'P'), ('pajaha', 'N'), ('pajahat', 'N'),
       ]

def pali_tense(s):
    out = []
    for m in re.finditer(r'\b(?:uppajj|nirujjh|bhāv|pajah)\w*', s):
        w = m.group(0)
        for k, t in P_T:
            if w.startswith(k):
                out.append(t); break
        else:
            out.append('?' + w)
    return out

def ru_tense(s):
    out = []
    for m in re.finditer(r'\b(?:возни\w*|прекрат\w*|прекращ\w*|разви\w*|развив\w*|устран\w*|отбрасыв\w*|отброс\w*)', s):
        w = m.group(0)
        if re.match(r'(возникнут|возникнет|прекратятся|прекратится|разовь|устранит|устранят)', w) or w.startswith('разов'):
            out.append('F')
        elif re.match(r'возникал|прекращал|развивал|устранял', w):
            out.append('P')
        elif re.match(r'возникают|возникает|прекращают|прекращает|развивает|развивают|устраняет|устраняют', w):
            out.append('N')
        elif w.startswith('возникнов') or w.startswith('прекращени') or w.startswith('развити') or w.startswith('устранени'):
            continue
        else:
            out.append('?' + w)
    return out

def main():
    mode = sys.argv[1]
    if mode == 'show':
        p, r = load(sys.argv[2])
        for i in range(int(sys.argv[3]) - 1, int(sys.argv[4])):
            if p[i].strip():
                print(i + 1, 'P', p[i]); print(i + 1, 'R', r[i])
        return
    files = sys.argv[2:] or FILES
    if mode == 'tpl':
        d = collections.defaultdict(collections.Counter)
        first = {}
        for f in files:
            p, r = load(f)
            for i, (a, b) in enumerate(zip(p, r)):
                if not a.strip():
                    continue
                pa, _ = pali_norm(a); rb, _ = ru_norm(b)
                ps, rs = sentences(pa), sentences(rb)
                if len(ps) != len(rs):
                    print('SENTCOUNT', f, i + 1, len(ps), len(rs))
                    ps, rs = [pa], [rb]
                for x, y in zip(ps, rs):
                    d[x][y] += 1
                    first.setdefault((x, y), f'{f[:4]}:{i+1}')
        for x in sorted(d, key=lambda k: -sum(d[k].values())):
            print('P', sum(d[x].values()), x)
            for y, n in d[x].most_common():
                print('   R', n, first[(x, y)], y)
    elif mode == 'seq':
        bad = 0
        for f in files:
            p, r = load(f)
            for i, (a, b) in enumerate(zip(p, r)):
                if not a.strip():
                    continue
                _, s1 = pali_norm(a); _, s2 = ru_norm(b)
                if s1 != s2:
                    bad += 1
                    print('SEQ', f, i + 1, ''.join(s1), ''.join(s2))
        print('seq mismatches', bad)
    elif mode == 'tense':
        bad = 0
        for f in files:
            p, r = load(f)
            for i, (a, b) in enumerate(zip(p, r)):
                if not a.strip() or a.startswith('#'):
                    continue
                t1 = pali_tense(a); t2 = ru_tense(b)
                dd=lambda t:[x for k,x in enumerate(t) if k==0 or t[k-1]!=x]
                if dd(t1) != dd(t2):
                    bad += 1
                    print('TENSE', f, i + 1, ''.join(t1), ''.join(t2))
        print('tense mismatches', bad)

main()
