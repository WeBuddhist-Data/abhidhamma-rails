import sys, re
P = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-2_split_chapters\\'
R = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\russian\pi-2-russian-plain-rails_split_chapters\\'
ch = sys.argv[1]
start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
end = int(sys.argv[3]) if len(sys.argv) > 3 else 10**9
mode = sys.argv[4] if len(sys.argv) > 4 else 'pairs'
pl = [l for l in open(P + ch, encoding='utf-8').read().split('\n') if l.strip()]
rl = [l for l in open(R + ch, encoding='utf-8').read().split('\n') if l.strip()]
assert len(pl) == len(rl), (len(pl), len(rl))
idre = re.compile(r'\s*\^[\d\-a-z]+$')
seen = {}
for i, (p, r) in enumerate(zip(pl, rl)):
    pk = idre.sub('', p)
    rk = idre.sub('', r)
    if pk in seen:
        if seen[pk][1] != rk:
            if start <= i < end:
                print(f'### INCONSISTENT {i} vs {seen[pk][0]}')
                print('P', p); print('R', r); print('R0', seen[pk][1]); print()
        elif start <= i < end and mode == 'pairs':
            print(f'[{i}] = dup of [{seen[pk][0]}] {p[:50]}')
        continue
    seen[pk] = (i, rk)
    if start <= i < end and mode == 'pairs':
        print(f'[{i}] P', p)
        print(f'[{i}] R', r)
        print()
