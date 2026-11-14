import re, os
from collections import Counter
base = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
P = os.path.join(base, 'pali', 'pi-1_split_chapters')
R = os.path.join(base, 'russian', 'pi-1-russian-plain-rails_split_chapters')
files = ['4-01-nikkhepakandam.md', '4-02-nikkhepakandam.md', '4-03-nikkhepakandam.md', '5-atthakathakandam.md']
pnum = [(r'\bekādasa\b', 11), (r'\bdvādas', 12), (r'\baṭṭhārasa\b', 18), (r'\beko\b', 1), (r'\bdve\b|\bdvīsu\b', 2),
        (r'\btayo\b|\btīṇi\b|\btisso\b|\btīsu\b', 3), (r'\bcattāro\b|\bcattāri\b|\bcatūsu\b', 4), (r'\bpañca\b', 5),
        (r'\bcha\b|\bchannaṃ\b', 6), (r'\bsatta\b|\bsattapi\b', 7), (r'\baṭṭha\b|\baṭṭhasu\b', 8), (r'\bnava\b', 9), (r'\bdasa\b', 10),
        (r'\bpañcapi\b', 5),
        (r'ekaka', 1), (r'duka(?=duka|tika|jjh)', 2), (r'(?<=duka)duka', 2), (r'tika(?=tika|catukka|jjh)', 3), (r'(?<=tika)tika', 3), (r'(?<=tika)catukka', 4), (r'(?<=ekaka)duka', 2),
        (r'catukkapañcaka', 0)]
rnum = [(r'\bодиннадцать\b', 11), (r'\bдвенадцать\b', 12), (r'\bвосемнадцать\b', 18), (r'\bодин\b|\bодно\b', 1),
        (r'\bдва\b|\bдве\b|\bдвух\b|\bдвое\b', 2), (r'\bтри\b|\bтрёх\b|\bтрое\b', 3), (r'\bчетыре\b|\bчетырёх\b', 4),
        (r'\bпять\b|\bпяти\b', 5), (r'\bшесть\b|\bшести\b', 6), (r'\bсемь\b', 7), (r'\bвосемь\b|\bвосьми\b', 8), (r'\bдевять\b', 9), (r'\bдесять\b', 10)]
def count(s, pats):
    c = Counter()
    for p, v in pats:
        n = len(re.findall(p, s, flags=re.I))
        if n and v:
            c[v] += n
    return c
for fn in files:
    pn = [l for l in open(os.path.join(P, fn), encoding='utf-8') if l.strip()]
    rn = [l for l in open(os.path.join(R, fn), encoding='utf-8') if l.strip()]
    for a, b in zip(pn, rn):
        a2 = re.sub(r'\[[^\]]*\]', '', a); b2 = re.sub(r'\[[^\]]*\]', '', b)
        a2 = a2.replace('catukkapañcakajjhānā', 'CP')
        ca, cb = count(a2, pnum), count(b2, rnum)
        if 'CP' in a2:
            ca[4] += 1; ca[5] += 1
        if ca != cb:
            m = re.search(r'\^([\w-]+)\s*$', a)
            print(fn, m.group(1) if m else '?', dict(ca), dict(cb))
