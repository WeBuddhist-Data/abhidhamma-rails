"""Compact view of family_scan part B: groups with at least one member whose term is not pi-1's term for that headword.
usage: famB_new.py <family-scan.txt>"""
import re, sys, pathlib
B = pathlib.Path(__file__).resolve().parents[5]
t1 = {}
for l in (B / 'AI_translation/burmese/pi-1-pali-burmese-termbase-plain.md').read_text(encoding='utf-8').splitlines():
    h, b = l.split(': {', 1); t1[h] = [s.rsplit(': ', 1)[1] for s in b[:-1].split('; ')]
txt = open(sys.argv[1], encoding='utf-8').read().split('== B.')[1].split('== C.')[0].splitlines()[1:]
groups, cur = [], None
for l in txt:
    if l.startswith('-- '): cur = [l, []]; groups.append(cur)
    elif cur and l.startswith('   '):
        m = re.match(r'   (.+)\|(\d+): (.*)$', l); cur[1].append(m.groups())
n = 0
for head, mem in groups:
    if all(h in t1 and t in t1[h] for h, i, t in mem): continue
    n += 1
    print(head + '  ' + ' ; '.join(f"{h}|{i}={t}{'' if (h in t1 and t in t1[h]) else '*'}" for h, i, t in mem))
print(n, 'groups', file=sys.stderr)
