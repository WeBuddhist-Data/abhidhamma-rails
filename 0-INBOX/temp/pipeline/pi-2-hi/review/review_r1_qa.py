import re, sys
exec(open(r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi\review\review_r1_align.py', encoding='utf-8').read().split("mode = sys.argv")[0])
a, b = int(sys.argv[1]), int(sys.argv[2])
PN = {'rūpakkhandho': 'R', 'cattāro': '4', 'dve': '2', 'tayo': '3', 'eko': '1', 'pañca': '5', 'khandho': '1'}
HN = {'भौतिक रूप का समूह': 'R', 'चार': '4', 'दो': '2', 'तीन': '3', 'एक': '1', 'पाँचों': '5', 'पाँच': '5'}
for i in range(a - 1, b):
    p = idre.sub('', pl[i]); h = idre.sub('', hl[i])
    ps = [s.strip() for s in re.split(r'(?<=[.?])\s+', p) if s.strip()]
    hs = [s.strip() for s in re.split(r'(?<=[।?])\s+', h) if s.strip()]
    print(f'=== line {i+1} {pid(pl[i])}  sentences P{len(ps)} H{len(hs)}')
    for k in range(max(len(ps), len(hs))):
        x = ps[k] if k < len(ps) else ''
        y = hs[k] if k < len(hs) else ''
        si = len(re.findall(r'\bsiyā\b', x, re.I)); ka = y.count('कभी')
        na = len(re.findall(r'\bna vattabb', x)); nv = y.count('नहीं कहा जा सकता') + y.count('नहीं कहे जा सकते') + y.count('न कहा जा सकता')
        flag = '' if (si == ka and na == nv) else f'  <<< siyā{si}/कभी{ka} nv{na}/{nv}'
        if '-v' in sys.argv or flag:
            print(f'  P{k+1}: {x}{flag}')
            print(f'  H{k+1}: {y}')
