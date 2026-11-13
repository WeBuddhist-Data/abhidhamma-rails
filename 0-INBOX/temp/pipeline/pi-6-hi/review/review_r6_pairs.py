import sys, re, os
base = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
here = os.path.dirname(os.path.abspath(__file__))
def ne(path):
    return [l.rstrip('\n') for l in open(path, encoding='utf-8') if l.strip()]
for f in ['8-cittayamaka.md', '9-01-dhammayamaka.md', '9-02-dhammayamaka.md', '9-03-dhammayamaka.md']:
    P = ne(base + '\\pali\\pi-6_split_chapters\\' + f)
    H = ne(base + '\\hindi\\pi-6-hindi-plain-rails_split_chapters\\' + f)
    out = []
    for i, (p, h) in enumerate(zip(P, H), 1):
        out.append(f'[{i}] P: {p}\n[{i}] H: {h}')
    open(os.path.join(here, 'review_r6_pairs_' + f.replace('.md', '.txt')), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print(f, len(P), len(H))
