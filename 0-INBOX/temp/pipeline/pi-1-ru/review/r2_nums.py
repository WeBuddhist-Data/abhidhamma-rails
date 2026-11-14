import re
from collections import Counter
base = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
files = ['2-03-cittuppadakandam.md', '2-04-cittuppadakandam.md', '2-05-cittuppadakandam.md']
pmap = [
    (r'\beka[ṃmo]?\b|\bekā\b|\bekaṃ\b|\beko\b', 1), (r'\bdve\b|\bdvā(?=yatan)|\bduvaṅg', 2), (r'\btayo\b|\btīṇi|\btiv', 3),
    (r'\bcattāro\b|\bcattāri\b|\bcatur|\bcatūhi', 4), (r'\bpañc(?!am)', 5), (r'\bsatta\b', 7), (r'\baṭṭh(?!a\b)', 8), (r'\bnav', 9),
    (r'\bdvādasa\b', 12), (r'\bvīsati\b', 20), (r'\btīhi\b', 3),
    (r'paṭham', 'o1'), (r'dutiy', 'o2'), (r'tatiy', 'o3'), (r'catutth', 'o4'), (r'pañcam', 'o5'),
]
rmap = [
    (r'\bод(?:ин|на|но|ного|ной)\b', 1), (r'\bдв(?:а|е|ух)\b|\bдвухчаст', 2), (r'\bтр(?:и|ёх)\b|\bтрёхчаст', 3),
    (r'\bчетыр(?:е|ёх)\b|\bчетырёхчаст', 4), (r'\bпят(?:ь|и)\b|\bпятичаст', 5), (r'\bсемь\b', 7), (r'\bвосьм|\bвосемь', 8), (r'\bдевят', 9),
    (r'\bдвенадцать\b', 12), (r'\bдвадцать\b', 20),
    (r'\bперв', 'o1'), (r'\bвтор', 'o2'), (r'\bтрет', 'o3'), (r'\bчетвёрт', 'o4'), (r'\bпят(?:ое|ого|ом|ый)\b', 'o5'),
]
def cnt(s, mp):
    c = Counter()
    for pat, v in mp:
        c[v] += len(re.findall(pat, s, flags=re.I))
    return +c
for f in files:
    P = open(base + r'\pali\pi-1_split_chapters\\' + f, encoding='utf-8').read().split('\n')
    R = open(base + r'\russian\pi-1-russian-plain-rails_split_chapters\\' + f, encoding='utf-8').read().split('\n')
    for i, (p, r) in enumerate(zip(P, R)):
        if not p.strip():
            continue
        p2 = re.sub(r'\^[\w-]+', '', p)
        r2 = re.sub(r'\^[\w-]+', '', r)
        cp, cr = cnt(p2, pmap), cnt(r2, rmap)
        if cp != cr:
            idm = re.search(r'\^([\w-]+)', p)
            print(f[:4], i + 1, idm.group(1) if idm else '', dict(cp), dict(cr))
