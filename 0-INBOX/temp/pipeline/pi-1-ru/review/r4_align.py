import sys, re, os
base = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
P = os.path.join(base, 'pali', 'pi-1_split_chapters')
R = os.path.join(base, 'russian', 'pi-1-russian-plain-rails_split_chapters')
files = ['4-01-nikkhepakandam.md', '4-02-nikkhepakandam.md', '4-03-nikkhepakandam.md', '5-atthakathakandam.md']

def lines(path):
    with open(path, encoding='utf-8') as f:
        return [l.rstrip('\n') for l in f]

mode = sys.argv[1] if len(sys.argv) > 1 else 'stats'
out = []
for fn in files:
    pl = lines(os.path.join(P, fn)); rl = lines(os.path.join(R, fn))
    pn = [l for l in pl if l.strip()]; rn = [l for l in rl if l.strip()]
    out.append(f'== {fn}: pali lines {len(pl)} nonempty {len(pn)}; ru lines {len(rl)} nonempty {len(rn)}')
    # double blank check
    for i in range(1, len(rl)):
        if not rl[i].strip() and not rl[i-1].strip():
            out.append(f'  double blank at ru line {i+1}')
    for i, (a, b) in enumerate(zip(pn, rn)):
        ia = re.findall(r'\^[\w-]+\s*$', a); ib = re.findall(r'\^[\w-]+\s*$', b)
        if ia != ib:
            out.append(f'  ID mismatch at nonempty {i}: {ia} vs {ib}')
            break
    if mode == 'dump':
        dfn = os.path.join(os.path.dirname(__file__), 'r4_dump_' + fn.replace('.md', '.txt'))
        with open(dfn, 'w', encoding='utf-8') as f:
            for a, b in zip(pn, rn):
                f.write('P: ' + a + '\nR: ' + b + '\n\n')
print('\n'.join(out))
