"""Exploration helper: show Russian (and optionally Pāli) for lines whose Pāli matches a regex.

usage: python -I -X utf8 probe_ru.py <pali_regex> [--ru <ru_regex>] [--win N] [--pali] [--parts 2-0,4-01] [--max N] [--bak]
--ru: print only windows of N chars around matches of ru_regex on the Russian line (else whole line, cut at --win*4).
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ru_common as C

a = sys.argv[1:]
def opt(name, default=None):
    if name in a:
        i = a.index(name); v = a[i + 1]; del a[i:i + 2]; return v
    return default
ru = opt("--ru"); win = int(opt("--win", "60")); parts = opt("--parts"); mx = int(opt("--max", "400"))
showp = "--pali" in a
if "--bak" in a:
    C.CUR["rdir"] = C.BAK
a = [x for x in a if not x.startswith("--")]
rx = re.compile(a[0])
rr = re.compile(ru) if ru else None
n = 0
forms = collections.Counter()
for part in C.PARTS:
    if parts and not any(part.startswith(x) for x in parts.split(",")):
        continue
    for sid, ps, rs in C.segments(part):
        for p, r in zip(ps, rs):
            if not rx.search(p):
                continue
            if rr:
                for m in rr.finditer(r):
                    s = r[max(0, m.start() - win):m.end() + win]
                    forms[m.group(0)] += 1
                    if n < mx:
                        print(f"{C.short(part)}:{sid} | …{s}…")
                    n += 1
            else:
                if n < mx:
                    if showp:
                        pm = rx.search(p)
                        print(f"{C.short(part)}:{sid} P| {p[max(0, pm.start() - win):pm.end() + win]}")
                    print(f"{C.short(part)}:{sid} | {r[:win * 4]}")
                n += 1
print("TOTAL", n)
if forms:
    for k, v in forms.most_common(40):
        print(v, k)
