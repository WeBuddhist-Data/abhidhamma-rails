import re, os
B = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
FILES = ['2-01-vitakkattika.md', '2-02-pitittika.md', '2-03-dassanenapahatabbattika.md',
         '2-04-dassanenapahatabbahetukattika.md', '2-05-acayagamittika.md', '2-06-sekkhattika.md',
         '2-07-parittattika.md', '2-08-parittarammanattika.md']

def load(path):
    with open(path, encoding='utf-8') as f:
        return [l for l in f.read().split('\n') if l.strip()]

for f in FILES:
    P = load(os.path.join(B, 'pali', 'pi-7_split_chapters', f)); H = load(os.path.join(B, 'hindi', 'pi-7-hindi-plain-rails_split_chapters', f))
    for i, (p, h) in enumerate(zip(P, H), 1):
        if p.startswith('#') or p.startswith('('):
            continue
        p1 = re.split(r' – |\. ', p)[0]
        h1 = re.split(r' – |। ', h)[0]
        # pañhāvāra main clause
        m = re.search(r'\b(dhammo|dhammā)\b.*\bdhammassa\b.*paccayo', p1)
        if m:
            pl = m.group(1) == 'dhammā'
            if pl:
                ok = 'परिघटनाएँ' in h1 and re.search(r'कारण होती हैं', h1)
            else:
                ok = 'परिघटनाएँ' not in h1.split(',')[0] and re.search(r'कारण होती है(?!ं)', h1)
            if not ok and '…' not in h1[-3:]:
                print(f'{f[:4]}:{i} PANHA pl={pl} | {h1[:200]}')
            continue
        m = re.search(r'\b(dhammo|dhammā)\s+uppajj', p1)
        if m:
            pl = m.group(1) == 'dhammā'
            if pl:
                ok = 'परिघटनाएँ' in h1 and ('उत्पन्न होती हैं' in h1 or 'उत्पन्न' not in h1)
            else:
                ok = re.search(r'उत्पन्न होती है(?!ं)', h1) or 'उत्पन्न' not in h1
            if not ok:
                print(f'{f[:4]}:{i} PATICCA pl={pl} | {h1[:200]}')
    # masculine/feminine slips in example clauses
    for i, h in enumerate(H, 1):
        for m in re.finditer(r'(\S+ \S+ \S+) (समूह|आधार|मोह|राग|इरादा|फल|मार्ग|ध्यान) (होती है|होती हैं|उत्पन्न होती)', h):
            print(f'{f[:4]}:{i} GENDER? {m.group(0)}')
        for m in re.finditer(r'परिघटना (\S+ ){0,3}(होता है|होते हैं)', h):
            print(f'{f[:4]}:{i} GENDER-F? {m.group(0)}')
