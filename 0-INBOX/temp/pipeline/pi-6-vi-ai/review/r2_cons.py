import re, os, sys
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\vietnamese'
BOOKS = ['pi-%d-vietnamese-plain.md' % i for i in range(1, 6)]
MINE = os.path.join(ROOT, 'pi-6-vietnamese-plain-rails_split_chapters')
FILES = ['3-06-ayatanayamaka.md', '4-dhatuyamaka.md', '5-01-saccayamaka.md', '5-02-saccayamaka.md',
         '5-03-saccayamaka.md', '6-01-sankharayamaka.md', '6-02-sankharayamaka.md', '7-01-anusayayamaka.md',
         '1-mulayamaka.md']
texts = {}
for b in BOOKS:
    with open(os.path.join(ROOT, b), encoding='utf-8') as f:
        texts[b[:4]] = f.read().lower()
mine = ''
for fn in FILES:
    with open(os.path.join(MINE, fn), encoding='utf-8') as f:
        texts[fn[:8]] = f.read().lower()
for term in sys.argv[1:]:
    r = re.compile(term.lower())
    print(term, ' '.join('%s:%d' % (k, len(r.findall(v))) for k, v in texts.items()))
