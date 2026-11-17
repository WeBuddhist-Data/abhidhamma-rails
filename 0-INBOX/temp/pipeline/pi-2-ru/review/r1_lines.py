import sys, re
from collections import defaultdict
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\review')
from r1_align import load
m = defaultdict(lambda: defaultdict(list))
PK = re.compile(r'(vedanā|saññā|saṅkhāra|viññāṇa)kkhandh')
RK = re.compile(r'([Сс]овокупност\w*) (чувств|восприятия|формирующих факторов|сознания)')
SUB = [(r'(cakkhu|sota|ghāna|jivhā|kāya|mano)samphassajā (vedanā|saññā|cetanā)', 'XJ'),
       (r'рождённое контактом (глаза|уха|носа|языка|тела|ума|элемента ума|элемента умственного сознания) (чувство|восприятие|намерение)', 'XJ')]
for ch in ['1-khandhavibhango.md']:
    p, r, pt, rt = load(ch)
    for (pid, pl), (rid, rl) in zip(p, r):
        for a, b in zip(pl, rl):
            a2 = re.sub(r'\^[\w-]+\s*$', '', a)
            b2 = re.sub(r'\^[\w-]+\s*$', '', b)
            a2 = PK.sub('K', a2)
            b2 = RK.sub(lambda mm: mm.group(1) + ' K', b2)
            a2 = re.sub(SUB[0][0], 'XJ', a2)
            b2 = re.sub(SUB[1][0], 'XJ', b2)
            a2 = re.sub(r'(phassa|citta)sampayutt', 'SAMP', a2)
            b2 = re.sub(r'связана с (контактом|умом)', 'SAMP', b2)
            for w in ['cakkhuviññāṇaṃ', 'sotaviññāṇaṃ', 'ghānaviññāṇaṃ', 'jivhāviññāṇaṃ', 'kāyaviññāṇaṃ', 'manoviññāṇaṃ', 'manodhātu', 'manoviññāṇadhātu']:
                pass
            m[a2][b2].append(pid)
n = 0
for a, d in m.items():
    if len(d) > 1:
        n += 1
        print('PALI:', a[:200])
        for b, ids in d.items():
            print('   ', ids[:5], b[:300])
print('inconsistent groups', n, 'of', len(m))
