"""List the termbase entries for every keyword of the segments 7-42 .. 7-49 (files 4-08 .. 4-15).
usage: python -I -B -X utf8 lookup_4-08_4-15.py [prefix ...]
"""
import re, sys, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parents[5]
KW = ROOT / "AI_translation" / "pali" / "pi-7-keywords-by-reference-pali-plain.md"
TB = ROOT / "AI_translation" / "hindi" / "pi-7-pali-hindi-termbase-plain.md"
prefixes = sys.argv[1:] or [f"7-{n}-" for n in range(42, 50)]

tb = {}
for line in TB.read_text(encoding="utf-8").splitlines():
    w, body = line.split(": {", 1)
    tb[w] = body[:-1]
tb_ci = {k.lower(): v for k, v in tb.items()}

cnt = collections.Counter()
for line in KW.read_text(encoding="utf-8").splitlines():
    i, body = line.split("] ", 1)
    i = i[1:]
    if not any(i.startswith(p) for p in prefixes):
        continue
    for k in body.split(", "):
        for kk in k.split(" / "):
            cnt[kk] += 1
for k, n in sorted(cnt.items(), key=lambda x: x[0].lower()):
    t = tb.get(k) or tb_ci.get(k.lower())
    print(f"{n:4d} {k}: {t}")
