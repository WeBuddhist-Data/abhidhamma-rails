import sys, re
base = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
ch = sys.argv[1]
a = int(sys.argv[2]) if len(sys.argv) > 2 else 0
b = int(sys.argv[3]) if len(sys.argv) > 3 else 10**9
P = open(base + r'\pali\pi-1_split_chapters\\' + ch, encoding='utf-8').read().split('\n')
R = open(base + r'\russian\pi-1-russian-plain-rails_split_chapters\\' + ch, encoding='utf-8').read().split('\n')
print('lines', len(P), len(R))
for i, (p, r) in enumerate(zip(P, R)):
    if i < a or i >= b:
        continue
    if not p.strip() and not r.strip():
        continue
    print(f'{i+1}P: {p}')
    print(f'{i+1}R: {r}')
