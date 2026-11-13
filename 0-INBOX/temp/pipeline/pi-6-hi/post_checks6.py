"""Post-pass checks: protected lines unchanged vs backup, raw line counts unchanged, greps (—, :-, धर्म, seed,
Latin letters outside [..] brackets; counted before and after so pre-existing hits are visible)."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hz6_common as C
from harmonise_hi import PROTECTED

bad = 0
for part in C.PARTS:
    a = open(os.path.join(C.BAK, part + ".md"), encoding="utf-8").read()
    b = open(os.path.join(C.HDIR, part + ".md"), encoding="utf-8").read()
    if a.count("\n") != b.count("\n"):
        print("RAW LINE COUNT CHANGED", part); bad += 1
    if part in PROTECTED:
        na = [l for l in a.lstrip("﻿").split("\n") if l.strip()]
        nb = [l for l in b.lstrip("﻿").split("\n") if l.strip()]
        rng = PROTECTED[part] or [(1, len(na))]
        diffs = [k for s, e in rng for k in range(s, e + 1) if na[k - 1] != nb[k - 1]]
        print(f"protected {part}: {sum(e - s + 1 for s, e in rng)} lines, changed {len(diffs)}")
        bad += len(diffs)

PATS = {"em dash": "—", ":-": ":-", "धर्म": "धर्म", "seed": "seed"}
LAT = re.compile(r"[A-Za-zĀāĪīŪūṬṭḌḍṆṇÑñṄṅṂṃḶḷ]")


def latin_outside(line):
    t = re.sub(r"\[[^\]]*\]", "", line)
    t = re.sub(r"\^[\w-]+\s*$", "", t)
    return LAT.findall(t)


for label, d in (("before", C.BAK), ("after", C.HDIR)):
    cnt = {k: 0 for k in PATS}
    lat = []
    for part in C.PARTS:
        for i, l in enumerate(open(os.path.join(d, part + ".md"), encoding="utf-8-sig").read().split("\n"), 1):
            for k, p in PATS.items():
                cnt[k] += l.count(p)
            if latin_outside(l):
                lat.append(f"{part}:{i}: {''.join(latin_outside(l))[:40]}")
    print(label, cnt, "latin-outside-brackets lines:", len(lat))
    for x in lat[:10]:
        print("   ", x)
print("BAD" if bad else "OK")
