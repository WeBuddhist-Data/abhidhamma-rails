"""Merge the per-file pi-6 Pāli→Hindi maps into AI_translation/hindi/pi-6-keywords-by-reference-pali-hindi-plain.md.

usage: python -I -X utf8 merge_map_hi.py
Checks: line count, IDs and order equal the Pāli keyword file; keywords per line identical and in order;
the artefact keyword «(no direct equivalent)» never carries a Hindi value; values contain no Latin letters
(other than the (no direct equivalent) marker), no ", " and no em/en dash. Prints keywords whose values differ
across files (for information).
"""
import pathlib, re, sys
from collections import defaultdict

sys.dont_write_bytecode = True
ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
D = ROOT / "0-INBOX/temp/pipeline/pi-6-hi/mapper-hi"
SRC = ROOT / "AI_translation/pali/pi-6-keywords-by-reference-pali-plain.md"
OUT = ROOT / "AI_translation/hindi/pi-6-keywords-by-reference-pali-hindi-plain.md"
NDE = "(no direct equivalent)"
LATIN = re.compile(r"[A-Za-zāīūṃṅñṭḍṇḷ]")

mapped, origin = {}, {}
parts = sorted(p.name[:-len(".keywords.md")] for p in D.glob("*.keywords.md"))
for p in parts:
    f = D / f"{p}.mapped.md"
    if not f.exists():
        sys.exit(f"missing {f.name}")
    for line in f.read_text(encoding="utf-8-sig").splitlines():
        if not line.strip():
            continue
        i, body = line.split("] ", 1)
        mapped[i[1:]] = body
        origin[i[1:]] = p

out, bad, nde_bad, val_bad = [], [], [], []
values = defaultdict(lambda: defaultdict(set))
for line in SRC.read_text(encoding="utf-8-sig").splitlines():
    if not line.strip():
        continue
    i, body = line.split("] ", 1)
    sid = i[1:]
    m = mapped.get(sid)
    kws = [k.strip() for k in body.split(", ")]
    if m is None:
        bad.append(sid); continue
    pairs = [q.split("=", 1) for q in m.split(", ")]
    if kws != [k for k, _ in pairs]:
        bad.append(sid); continue
    for k, v in pairs:
        if k == NDE and v != NDE:
            nde_bad.append((sid, v))
        if v != NDE and (LATIN.search(v) or "—" in v or "–" in v):
            val_bad.append((sid, k, v))
        if k != NDE and v != NDE:
            values[k][v].add(origin[sid])
    out.append(f"{i}] {m}")
if bad or nde_bad or val_bad:
    sys.exit(f"keyword mismatch: {bad[:10]}\nNDE keyword with a value: {nde_bad[:10]}\nbad values: {val_bad[:10]}")
OUT.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
npairs = sum(len(l.split("] ", 1)[1].split(", ")) for l in out)
nde = sum(l.count("=" + NDE) for l in out)
multi = {k: v for k, v in values.items() if len(v) > 1}
print(OUT.name, "files", len(parts), "lines", len(out), "pairs", npairs, "no-equivalent", nde,
      "extra ids:", sorted(set(mapped) - {l[1:l.index("]")] for l in out})[:5])
print("keywords with more than one value across the book:", len(multi))
for k in sorted(multi, key=lambda k: -sum(len(f) for f in multi[k].values()))[:25]:
    print(" ", k, "|", " / ".join(f"{v} ({len(fs)})" for v, fs in multi[k].items()))
