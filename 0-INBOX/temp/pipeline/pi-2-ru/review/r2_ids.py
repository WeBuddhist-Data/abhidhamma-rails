import re, sys
P = 'D:\\Work\\OpenPecha\\abhidhamma-rails\\AI_translation\\pali\\pi-2_split_chapters\\'
ch = sys.argv[1]
want = [int(x) for x in sys.argv[2:]]
pl = [l for l in open(P + ch, encoding='utf-8').read().split('\n') if l.strip()]
for w in want:
    for j in range(w, len(pl)):
        m = re.search(r'\^([\w\-]+)$', pl[j])
        if m:
            print(w, '->', m.group(1)); break
