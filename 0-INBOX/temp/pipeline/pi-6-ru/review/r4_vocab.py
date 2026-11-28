import re, sys, collections
base = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
files = ['6-02-sankharayamaka.md','7-01-anusayayamaka.md','7-02-anusayayamaka.md','7-03-anusayayamaka.md','7-04-anusayayamaka.md','7-05-anusayayamaka.md']
sel = sys.argv[1] if len(sys.argv) > 1 else 'pali'
c = collections.Counter()
for f in files:
    if sel == 'pali':
        p = base + r'\pali\pi-6_split_chapters\\' + f
    else:
        p = base + r'\russian\pi-6-russian-plain-rails_split_chapters\\' + f
    t = open(p, encoding='utf-8').read()
    t = re.sub(r'\^[\d-]+', '', t)
    for w in re.findall(r'\w+', t):
        c[w.lower()] += 1
for w, n in sorted(c.items()):
    print(n, w)
