import sys
P = 'AI_translation/pali/pi-6_split_chapters/'
R = 'AI_translation/russian/pi-6-russian-plain-rails_split_chapters/'
f = sys.argv[1]
a = int(sys.argv[2]) if len(sys.argv) > 2 else 1
b = int(sys.argv[3]) if len(sys.argv) > 3 else 10**9
pl = open(P + f, encoding='utf-8').read().split('\n')
rl = open(R + f, encoding='utf-8').read().split('\n')
for i, (p, r) in enumerate(zip(pl, rl), 1):
    if i < a or i > b:
        continue
    if not p.strip() and not r.strip():
        continue
    print(f'{i}P {p}')
    print(f'{i}R {r}')
