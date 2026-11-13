import re, sys
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\review')
from review_r8_check import load, FILES

# ordered sequences of place+event tokens, per sentence
PT = [('K', r'kāmāvacar', r'इंद्रिय-सुखों'), ('R', r'(?<![aA])rūpāvacar', r'सूक्ष्म भौतिक'), ('A', r'arūpāvacar|arūpān|arūpe\b|arūpaṃ|\barūpa', r'अभौतिक'),
      ('S', r'suddhāvās', r'शुद्ध निवास'), ('N', r'asaññasatt', r'पहचान-रहित'), ('5', r'(?<!catuvokāraṃ )(?<!catuvokārā )(?<!catuvokārānaṃ )pañcavokār', r'(?<!चार या )पाँच समूहों'),
      ('4', r'catuvokār', r'चार या पाँच|चार समूहों'),
      ('c', r'cavant', r'मरने वाल'), ('u', r'upapajjant|uppajjantānaṃ', r'जन्म लेने वाल'), ('p', r'parinibbant', r'निर्वाण पाने वाल'),
      ('b', r'bhaṅgakkhaṇ', r'भंग होने के क्षण'), ('o', r'uppādakkhaṇ', r'उत्पन्न होने के क्षण'), ('L', r'pacchimabhavik', r'अंतिम जन्म')]

def seq(s, idx):
    toks = []
    for name, pp, hp in PT:
        for m in re.finditer(pp if idx == 0 else hp, s, re.I if idx == 0 else 0):
            toks.append((m.start(), name))
    toks.sort()
    return ''.join(n for _, n in toks)

def sents(s, idx):
    s = re.sub(r'\s*(\([^)]*\))?\s*(\^[\w-]+)?\s*$', '', s)
    if idx == 0:
        parts = re.split(r'(?<=[.?])\s+', s)
    else:
        parts = re.split(r'(?<=[।?])\s+', s)
    return [p for p in parts if p.strip()]

n = 0
for f in FILES:
    P, H = load(f)
    for i, (p, h) in enumerate(zip(P, H)):
        sp, sh = sents(p, 0), sents(h, 1)
        if len(sp) != len(sh):
            print('SENTCOUNT', f, i + 1, len(sp), len(sh))
            continue
        for a, b in zip(sp, sh):
            qa, qb = seq(a, 0), seq(b, 1)
            # normalise: treat 'L' (pacchimabhavika) movable
            if qa != qb:
                n += 1
                print('%s L%d  P=%s  H=%s\n   P: %s\n   H: %s' % (f, i + 1, qa, qb, a[:400], b[:400]))
print('mismatch', n)
