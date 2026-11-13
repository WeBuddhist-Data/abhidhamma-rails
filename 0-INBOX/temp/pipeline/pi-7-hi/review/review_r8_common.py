import re, sys
F = '4-01-kilesagocchaka.md'
P = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-7_split_chapters\\' + F
H = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-7-hindi-plain-rails_split_chapters\\' + F
E = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\english\pi-7-english-plain-zeroshot_split_chapters\\' + F

def lines(path):
    with open(path, encoding='utf-8') as f:
        raw = f.read().split('\n')
    return [l for l in raw if l.strip()]

def load():
    p, h = lines(P), lines(H)
    # attach segment id: the id of the segment the line belongs to (next block id at line end)
    ids = [None] * len(p)
    cur = None
    for i in range(len(p) - 1, -1, -1):
        m = re.search(r'\^(\S+)\s*$', p[i])
        if m:
            cur = m.group(1)
        ids[i] = cur
    return p, h, ids
