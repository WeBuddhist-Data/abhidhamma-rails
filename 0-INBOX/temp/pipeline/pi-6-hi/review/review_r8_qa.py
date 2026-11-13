import sys, re
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\review')
from review_r8_check import load, FILES, pali_verbs, pitems
for f in FILES:
    P, H = load(f)
    for i in range(len(P) - 1):
        q, a = P[i], P[i + 1]
        if not q.rstrip().endswith('?') and '?' not in q[-5:]:
            continue
        qv = pali_verbs(q)
        if len(qv) != 2:
            continue
        qi = pitems(q)
        sents = re.split(r'(?<=\.)\s+(?=[A-ZĀĪŪ])', a)
        for s in sents:
            av = pali_verbs(s)
            ai = pitems(s)
            if len(av) < 2:
                continue
            av2 = av[-2:]
            ai2 = [x for x in ai][-2:] if len(ai) >= 2 else ai
            ok = (av2[0][1], av2[1][1]) == (qv[0][1], qv[1][1]) and ai2 == qi[-2:] if len(qi) >= 2 else True
            s2 = re.sub(r'\(\w+\)\s*(\^[\w-]+)?\s*$', '', s); ai = pitems(s2)
            if (av2[0][1], av2[1][1]) != (qv[0][1], qv[1][1]) or (len(ai) >= 2 and len(qi) >= 2 and [ai[0], ai[-1]] != [qi[0], qi[-1]]):
                print(f, 'Q-L%d' % (i + 1), qv, qi, '| A-L%d' % (i + 2), av2, ai2, '|', s[:160])
