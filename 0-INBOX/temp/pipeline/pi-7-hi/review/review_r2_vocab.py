import re, sys, collections
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
FILES = ['1-02-vedanattika.md', '1-03-vipakattika.md', '1-04-upadinnattika.md', '1-05-sankilitthattika.md']
pc = collections.Counter(); hc = collections.Counter()
for f in FILES:
    p = open(ROOT + r'\pali\pi-7_split_chapters\\' + f, encoding='utf8').read()
    h = open(ROOT + r'\hindi\pi-7-hindi-plain-rails_split_chapters\\' + f, encoding='utf8').read()
    for w in re.findall(r"[^\s,.;:()…–—?“”‘’\[\]{}^*#!-]+", p):
        pc[w.lower()] += 1
    for w in re.findall(r"[^\s,.;:()…–—?“”‘’\[\]{}^*#!।]+", h):
        hc[w] += 1
mode = sys.argv[1]
if mode == 'p':
    for w, c in sorted(pc.items()):
        print(c, w)
else:
    for w, c in sorted(hc.items(), key=lambda x: -x[1]):
        print(c, w)
