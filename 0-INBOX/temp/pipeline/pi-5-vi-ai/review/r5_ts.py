import os, re, sys
# Console-only comparison helper. Never writes Tinh Su text to any file.
R = r'D:\Work\OpenPecha\abhidhamma-rails'
TS = os.path.join(R, r'1-SOURCES\Translations\Vietnamese\vi-5-tinh_su.md')
VI = os.path.join(R, r'AI_translation\vietnamese\pi-5-vietnamese-plain-rails_split_chapters')
PI = os.path.join(R, r'AI_translation\pali\pi-5_split_chapters')
FILES = ['23-pannarasamavaggo', '24-solasamavaggo', '25-sattarasamavaggo', '26-attharasamavaggo',
         '27-ekunavisatimavaggo', '28-visatimavaggo', '29-ekavisatimavaggo', '30-bavisatimavaggo',
         '31-tevisatimavaggo']


def segs_text(text):
    out = {}
    order = []
    cur = []
    for l in text.split('\n'):
        if not l.strip():
            continue
        cur.append(l)
        m = re.search(r'\^([\w-]+)\s*$', l)
        if m:
            out[m.group(1)] = cur
            order.append(m.group(1))
            cur = []
    return out, order


def load(path):
    return segs_text(open(path, encoding='utf-8').read())


def neg(s):
    s = s.lower()
    return len(re.findall(r'\b(không|chẳng|chưa|chớ|đừng)\b', s))


def main():
    mode = sys.argv[1]
    ts, tso = load(TS)
    if mode == 'head':
        print(len(tso), tso[:5], tso[-5:])
        return
    if mode == 'show':
        for i in sys.argv[2:]:
            print('==', i)
            for l in ts.get(i, ['<missing>']):
                print('TS:', l)
        return
    if mode == 'range':
        a, b = int(sys.argv[2]), int(sys.argv[3])
        for i in tso:
            m = re.match(r'5-(\d+)$', i)
            if m and a <= int(m.group(1)) <= b:
                print('==', i)
                for l in ts[i]:
                    print(l)
        return
    if mode == 'stats':
        for f in FILES:
            v, vo = load(os.path.join(VI, f + '.md'))
            for i in vo:
                a = ' '.join(v[i]); b = ' '.join(ts.get(i, []))
                if not b:
                    print(f, i, 'TS MISSING'); continue
                na, nb = neg(a), neg(b)
                qa, qb = a.count('?'), b.count('?')
                la, lb = len(a), len(b)
                flag = []
                if abs(na - nb) > max(2, 0.25 * max(na, nb)): flag.append('neg %d/%d' % (na, nb))
                if qa != qb: flag.append('q %d/%d' % (qa, qb))
                r = lb / max(la, 1)
                if r < 0.6 or r > 1.5: flag.append('len %.2f' % r)
                if flag:
                    print(f, i, '; '.join(flag))


main()
