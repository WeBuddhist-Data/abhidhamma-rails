"""Print the locked termbase entries for every keyword of the given segment ids (deduplicated).

usage: python -I -X utf8 rails_sample_lookup.py <id> [<id> ...]   (or a range like 2-2..2-33)
"""
import pathlib
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
KW = ROOT / "AI_translation" / "pali" / "pi-2-keywords-by-reference-pali-plain.md"
TB = ROOT / "AI_translation" / "hindi" / "pi-2-pali-hindi-termbase-plain.md"

ids = []
for a in sys.argv[1:]:
    if ".." in a:
        x, y = a.split("..")
        p = x.rsplit("-", 1)[0]
        ids += [f"{p}-{n}" for n in range(int(x.rsplit("-", 1)[1]), int(y.rsplit("-", 1)[1]) + 1)]
    else:
        ids.append(a)

tb = {}
for line in TB.read_text(encoding="utf-8").splitlines():
    w, body = line.split(": {", 1)
    tb[w] = body[:-1]
tb_ci = {k.lower(): v for k, v in tb.items()}

seen = set()
for line in KW.read_text(encoding="utf-8").splitlines():
    i, body = line.split("] ", 1)
    i = i[1:]
    if i not in ids:
        continue
    for k in body.split(", "):
        for kk in k.split(" / "):
            if kk in seen:
                continue
            seen.add(kk)
            v = tb.get(kk) or tb_ci.get(kk.lower())
            print(f"[{i}] {kk}: {v}")
