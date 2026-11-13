import re, sys, collections
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review')
from review_r8_common import load
p, h, ids = load()
MASC = r'(समूह|समूहों|मोह|राग|लोभ|द्वेष|इरादा|आधार|महाभूत|मन|क्लेश|क्लेशों|अहंकार|संशय|ध्यान|मार्ग|फल|सदाचार)'
FEM = r'(परिघटना|परिघटनाएँ|परिघटनाओं|चेतना|श्रद्धा|प्रज्ञा|दृष्टि|प्रधानता|बेचैनी|उदासी|कामना|निर्लज्जता)'
pats = {
    'fem-adj+masc': re.compile(r'(\S*(?:वाली|जुड़ी|हुई|छोड़ी|बनने वाली))(?:, पर स्वयं [^,।;]*?)? ' + MASC + r'(?=[\s,।;…)])'),
    'masc-adj+fem': re.compile(r'(\S*(?:वाले|वाला|जुड़े|जुड़ा|हुए|हुआ))(?:, पर स्वयं [^,।;]*?)? ' + FEM + r'(?=[\s,।;…)])'),
    'ceva-fem-masc': re.compile(r'वाली, पर स्वयं [^,।;]*? (?:वाले|वाला) (समूह|समूहों|मोह|राग|क्लेश)'),
}
res = collections.defaultdict(list)
for i, b in enumerate(h):
    if b.startswith('#'):
        continue
    for k, r in pats.items():
        for m in r.finditer(b):
            s = b[max(0, m.start() - 30): m.end() + 5]
            res[k].append((i + 1, s))
for k, v in res.items():
    print('==', k, len(v))
    c = collections.Counter(s[-60:] for _, s in v)
    for i, s in v[:40]:
        print('  ', i, s)
