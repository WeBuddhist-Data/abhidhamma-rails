"""Final checks after the harmonise pass (pi-2 Vietnamese zero-shot).

- preamble.md byte-identical to the backup; first 77 non-empty lines of 1-khandhavibhango.md identical to the backup
  and to ch1-sample.md;
- per part: non-empty line count unchanged vs the backup; changed-line count;
- whole set: «—», «:-», «chánh niệm», «seed», «….», Latin letters outside [..] (Pāli diacritics, f j w z),
  CR, double blank lines, non-NFC text.

usage: python -I -X utf8 final_checks_vi.py
"""
import os, re, sys, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vi_common import VDIR, BAK, HERE, PARTS, PROTECTED_1, ID

bad = 0
pre_now = open(os.path.join(VDIR, "preamble.md"), "rb").read()
pre_bak = open(os.path.join(BAK, "preamble.md"), "rb").read()
print("preamble unchanged:", pre_now == pre_bak); bad += pre_now != pre_bak


def nel(path):
    return [l for l in open(path, encoding="utf-8").read().splitlines() if l.strip()]


c1, b1 = nel(os.path.join(VDIR, "1-khandhavibhango.md")), nel(os.path.join(BAK, "1-khandhavibhango.md"))
smp = nel(os.path.join(HERE, "ch1-sample.md"))
ok = c1[:PROTECTED_1] == b1[:PROTECTED_1]
print(f"1-khandhavibhango first {PROTECTED_1} lines unchanged vs backup:", ok); bad += not ok
print("  … and equal to ch1-sample.md non-empty lines:", c1[:PROTECTED_1] == smp[:PROTECTED_1], f"({len(smp)} sample lines)")
FOREIGN = re.compile(r"[āīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶfjwzFJWZ]")
tot = {}
for part in PARTS:
    path = os.path.join(VDIR, part + ".md")
    raw = open(path, "rb").read()
    t = raw.decode("utf-8")
    now, old = nel(path), nel(os.path.join(BAK, part + ".md"))
    probs = []
    if len(now) != len(old):
        probs.append(f"line count {len(old)} -> {len(now)}")
    if b"\r" in raw:
        probs.append("CR")
    if "\n\n\n" in t:
        probs.append("double blank line")
    if unicodedata.normalize("NFC", t) != t:
        probs.append("not NFC")
    for s in ["—", ":-", "….", "seed"]:
        if s in t:
            probs.append(f"«{s}» x{t.count(s)}")
    if "chánh niệm" in t.lower():
        probs.append("«chánh niệm»")
    for n, line in enumerate(t.splitlines(), 1):
        body = ID.sub("", re.sub(r"\[[^\]]*\]", "", line))
        m = FOREIGN.search(body)
        if m:
            probs.append(f"line {n}: foreign letter {m.group(0)!r}")
    diff = sum(a != b for a, b in zip(now, old))
    print(f"{part}: {len(now)} lines, {diff} changed", "OK" if not probs else "PROBLEMS " + "; ".join(probs[:8]))
    bad += bool(probs)
print("ALL OK" if not bad else f"PROBLEMS: {bad}")
