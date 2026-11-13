"""Post-pass checks for the pi-7 Hindi harmonise pass.
- protected text unchanged vs backup (preamble, 1-00-paccaya, 1-01 sample lines 1-190, 1235-1262)
- line counts unchanged vs backup
- grep the whole set for «—», «:-», «धर्म», «seed», Latin letters outside [..], CR, double blank lines, quotes
usage: python -I -B -X utf8 post_checks_hi.py
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hz7_common import PARTS, HDIR, BAK

prot = {"preamble": None, "1-00-paccaya": None, "1-01-kusalattika": [(1, 190), (1235, 1262)]}
issues = []
tot = {"—": 0, ":-": 0, "धर्म": 0, "seed": 0, "latin": 0, "CR": 0, "double-blank": 0, "“": 0}
for part in PARTS:
    a = open(os.path.join(BAK, part + ".md"), encoding="utf-8").read()
    b = open(os.path.join(HDIR, part + ".md"), encoding="utf-8").read()
    if a.count("\n") != b.count("\n"):
        issues.append(f"{part}: line count {a.count(chr(10))} -> {b.count(chr(10))}")
    if part in prot:
        na = [l for l in a.splitlines() if l.strip()]
        nb = [l for l in b.splitlines() if l.strip()]
        rng = prot[part]
        for i, (x, y) in enumerate(zip(na, nb)):
            if (rng is None or any(s <= i + 1 <= e for s, e in rng)) and x != y:
                issues.append(f"{part}: protected line {i + 1} changed")
    tot["—"] += b.count("—")
    tot[":-"] += b.count(":-")
    tot["धर्म"] += b.count("धर्म")
    tot["seed"] += b.lower().count("seed")
    tot["CR"] += b.count("\r")
    tot["double-blank"] += len(re.findall(r"\n[ \t]*\n[ \t]*\n", b))
    tot["“"] += b.count("“")
    for i, l in enumerate(b.splitlines()):
        s = re.sub(r"\[[^\]]*\]", "", l)
        s = re.sub(r"\^[\w-]+\s*$", "", s)
        if re.search(r"[A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]", s):
            tot["latin"] += 1
            if tot["latin"] <= 10:
                issues.append(f"{part}:{i + 1} latin outside brackets: {s[:120]}")
print("totals:", tot)
print("issues:", len(issues))
for x in issues[:40]:
    print(" ", x)
