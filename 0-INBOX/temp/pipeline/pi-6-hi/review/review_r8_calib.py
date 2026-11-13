import re, collections, sys
B = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
FILES = ['10-08', '10-09', '10-10', '10-11', '10-12', '10-13']

def lines(path):
    with open(path, encoding='utf-8') as f:
        return [l.rstrip('\n') for l in f if l.strip()]

def load(f):
    import glob
    p = glob.glob(B + r'\pali\pi-6_split_chapters\%s*.md' % f)[0]
    h = glob.glob(B + r'\hindi\pi-6-hindi-plain-rails_split_chapters\%s*.md' % f)[0]
    return lines(p), lines(h)

idre = re.compile(r'\^[\w-]+\s*$')
vcount = collections.Counter()
hitems = collections.Counter()
pitems = collections.Counter()
pwords = collections.Counter()
for f in FILES:
    P, H = load(f)
    print(f, len(P), len(H))
    for i, (p, h) in enumerate(zip(P, H)):
        ip = idre.search(p); ih = idre.search(h)
        if (ip and ip.group().strip()) != (ih and ih.group().strip()):
            print('  ID MISMATCH line', i + 1, ip and ip.group(), ih and ih.group())
    for h in H:
        for m in re.finditer(r'(उत्पन्न|निरुद्ध|समाप्त|नष्ट)( नहीं)? (\S+)( \S+)?', h):
            vcount[m.group(1) + ' ' + m.group(3) + (m.group(4) or '')] += 1
        for m in re.finditer(r'(\S+ की क्षमता|\S+-क्षमता)', h):
            hitems[m.group(1)] += 1
    for p in P:
        for m in re.finditer(r'(\w+?)(?:indriy|andriy)', p):
            pitems[m.group(1).lower()] += 1
        for w in re.findall(r'[\wāīūṃṅñṭḍṇḷ]+', p):
            pwords[w.lower()] += 1
print(vcount.most_common(60))
print(hitems.most_common(80))
print(pitems.most_common(80))
print([w for w, c in pwords.most_common(400)])
