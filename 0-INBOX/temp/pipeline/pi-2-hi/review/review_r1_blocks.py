import re, sys, difflib
sys.argv = sys.argv
exec(open(r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi\review\review_r1_align.py', encoding='utf-8').read().split("mode = sys.argv")[0])

heads = [i for i, l in enumerate(pl) if l.startswith('#')]
for i in heads: print(i + 1, pl[i], '|', hl[i])

# block ranges for abhidhamma section
def block(name):
    idx = [i for i in heads if pl[i].startswith('##### ' + name)]
    return idx

PSUB = {'vedanā': ['vedanā', 'Vedanā'], 'saññā': ['saññā', 'Saññā'], 'saṅkhāra': ['saṅkhāra', 'Saṅkhāra'], 'viññāṇa': ['viññāṇa', 'Viññāṇa']}
HSUB = {'vedanā': 'अनुभूति का समूह', 'saññā': 'पहचान का समूह', 'saṅkhāra': 'मानसिक रचनाओं का समूह', 'viññāṇa': 'चेतना का समूह'}

def norm_p(l, k):
    l = idre.sub('', l)
    return l.replace(k + 'kkhandh', 'XKH').replace(k[0].upper() + k[1:] + 'kkhandh', 'XKH').replace('saṅkhārakkhandh', 'XKH')

def norm_h(l, k):
    return idre.sub('', l).replace(HSUB[k], 'XKH')

if __name__ == '__main__' and len(sys.argv) > 1:
    a1, a2, b1, b2, k1, k2 = sys.argv[1:7]
    A = list(range(int(a1) - 1, int(a2))); B = list(range(int(b1) - 1, int(b2)))
    pa = [norm_p(pl[i], k1) for i in A]; pb = [norm_p(pl[i], k2) for i in B]
    ha = [norm_h(hl[i], k1) for i in A]; hb = [norm_h(hl[i], k2) for i in B]
    sm = difflib.SequenceMatcher(None, pa, pb, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            for x, y in zip(range(i1, i2), range(j1, j2)):
                if ha[x] != hb[y]:
                    print(f'HDIFF {A[x]+1} vs {B[y]+1}')
                    for d in difflib.ndiff([ha[x]], [hb[y]]):
                        pass
                    s = difflib.SequenceMatcher(None, ha[x], hb[y], autojunk=False)
                    for t, p1, p2, q1, q2 in s.get_opcodes():
                        if t != 'equal': print('   ', t, repr(ha[x][max(0,p1-30):p2+30]), '=>', repr(hb[y][max(0,q1-30):q2+30]))
        else:
            print(f'PDIFF {tag} A{[A[i]+1 for i in range(i1,i2)]} B{[B[j]+1 for j in range(j1,j2)]}')
