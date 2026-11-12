"""Compact termbase lookup for segment ranges, skipping keys seen in an exclusion range.

usage: python -I -X utf8 build_rails_12_tb.py <from-id> <to-id> [<excl-from> <excl-to>]
"""
import pathlib
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
KW = ROOT / "AI_translation" / "pali" / "pi-2-keywords-by-reference-pali-plain.md"
TB = ROOT / "AI_translation" / "hindi" / "pi-2-pali-hindi-termbase-plain.md"


def rng(a, b):
    p = a.rsplit("-", 1)[0]
    return {f"{p}-{n}" for n in range(int(a.rsplit("-", 1)[1]), int(b.rsplit("-", 1)[1]) + 1)}


ids = rng(sys.argv[1], sys.argv[2])
excl = set()
for j in range(3, len(sys.argv) - 1, 2):
    excl |= rng(sys.argv[j], sys.argv[j + 1])
tb = {}
for line in TB.read_text(encoding="utf-8").splitlines():
    w, body = line.split(": {", 1)
    tb[w] = body[:-1]
tb_ci = {k.lower(): v for k, v in tb.items()}


def keys(idset):
    out = []
    for line in KW.read_text(encoding="utf-8").splitlines():
        i, body = line.split("] ", 1)
        if i[1:] in idset:
            for k in body.split(", "):
                out += k.split(" / ")
    return out


skip = set(keys(excl))
seen = set()
for kk in keys(ids):
    if kk in seen or kk in skip:
        continue
    seen.add(kk)
    v = tb.get(kk) or tb_ci.get(kk.lower()) or "??"
    parts = []
    for s in v.split("; "):
        if ": " in s:
            tag, hi = s.rsplit(": ", 1)
            parts.append(f"{tag[:38]}={hi}" if ";" in v else hi)
        else:
            parts.append(s)
    print(f"{kk}: " + " | ".join(parts))
