"""Inspection helper: dedupe case_check --list rows (cc-out.txt) -> cc-distinct.txt"""
import collections, re, sys
rows = [l.rstrip("\n").split("\t") for l in open("cc-out.txt", encoding="utf-8") if l.count("\t") >= 4]
d = collections.OrderedDict()
for f in rows:
    b = re.split(r"(?:ကြ၏|ကြသည်|သည်)၊ ", f[4])[-1]
    key = (f[3][-150:], b.strip()[-230:])
    d.setdefault(key, []).append(f[0][:4] + ":" + f[1] + ":" + f[2])
with open("cc-distinct.txt", "w", encoding="utf-8") as fh:
    for (p, b), v in d.items():
        fh.write(f"{' '.join(sorted(set(v)))} | {p} || {b}\n")
print(len(d))
