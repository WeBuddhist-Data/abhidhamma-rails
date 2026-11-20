import re, sys
F = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\vietnamese\pi-1-vietnamese-plain.md'
t = open(F, encoding='utf-8').read()
lines = t.split('\n')
keys = sys.argv[1:]
for k in keys:
    hits = [l for l in lines if k in l]
    print('##', k, len(hits))
    for h in hits[:1]:
        i = h.find(k)
        print('   ', h[max(0, i - 250):i + 450])
