import re, sys, os
R = r'D:\Work\OpenPecha\abhidhamma-rails'
PI = os.path.join(R, r'AI_translation\pali\pi-5_split_chapters')
VI = os.path.join(R, r'AI_translation\vietnamese\pi-5-vietnamese-plain-rails_split_chapters')
FILES = ['23-pannarasamavaggo', '24-solasamavaggo', '25-sattarasamavaggo', '26-attharasamavaggo',
         '27-ekunavisatimavaggo', '28-visatimavaggo', '29-ekavisatimavaggo', '30-bavisatimavaggo',
         '31-tevisatimavaggo']


def segs(path):
    lines = [l.rstrip('\n') for l in open(path, encoding='utf-8')]
    out = []
    cur = []
    for l in lines:
        if not l.strip():
            continue
        cur.append(l)
        m = re.search(r'\^([\w-]+)\s*$', l)
        if m:
            out.append((m.group(1), cur))
            cur = []
    if cur:
        out.append(('TAIL', cur))
    return out


def cnt(pat, s):
    return len(re.findall(pat, s))


def main():
    files = sys.argv[1:] or FILES
    total = 0
    for f in files:
        p = segs(os.path.join(PI, f + '.md'))
        v = segs(os.path.join(VI, f + '.md'))
        if [a for a, _ in p] != [a for a, _ in v]:
            print(f, 'ID MISMATCH')
        for (pid, pl), (vid, vl) in zip(p, v):
            total += 1
            if len(pl) != len(vl):
                print(f, pid, 'LINECOUNT', len(pl), len(vl))
            for i, (a, b) in enumerate(zip(pl, vl)):
                issues = []
                am = cnt(r'Āmantā', a); dv = cnt(r'Đúng vậy', b)
                nh = cnt(r'Na hevaṃ', a); kn = cnt(r'Không nên nói như (?:thế|vậy)', b)
                nt = cnt(r'\bNatthi\b', a); kc = cnt(r'Không có\.|Không tồn tại\.', b)
                if am != dv: issues.append('amanta %d/%d' % (am, dv))
                if nh != kn: issues.append('nahevam %d/%d' % (nh, kn))
                if nt != kc: issues.append('natthi %d/%d' % (nt, kc))
                qa = a.count('?'); qb = b.count('?')
                if qa != qb: issues.append('q %d/%d' % (qa, qb))
                pe = a.count('…pe…') + a.count('...pe...'); el = b.count('…')
                if pe > el: issues.append('pe %d/%d' % (pe, el))
                if '….' in b: issues.append('dots-period')
                if a.count('–') != b.count('–'): issues.append('dash %d/%d' % (a.count('–'), b.count('–')))
                if issues:
                    print(f, pid, 'L%d' % i, '; '.join(issues))
    print('segments', total)


if __name__ == '__main__':
    main()
