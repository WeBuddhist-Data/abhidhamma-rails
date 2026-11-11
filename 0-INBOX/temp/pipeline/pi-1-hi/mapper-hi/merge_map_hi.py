"""Merge the per-part pi-1 Pāli→Hindi maps into AI_translation/hindi/pi-1-keywords-by-reference-pali-hindi-plain.md.

Coordinator fix before merging (identical Pāli, identical Hindi, different value): ^1-1066 caratīti = कर रहा (as ^1-1237).
Checks: line count and IDs equal the Pāli keyword file; keywords per line identical and in order.
"""
import pathlib, sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
D = ROOT / "0-INBOX/temp/pipeline/pi-1-hi/mapper-hi"
SRC = ROOT / "AI_translation/pali/pi-1-keywords-by-reference-pali-plain.md"
OUT = ROOT / "AI_translation/hindi/pi-1-keywords-by-reference-pali-hindi-plain.md"
PARTS = ["preamble", "1-matika", "2-01-cittuppadakandam", "2-02-cittuppadakandam", "2-03-cittuppadakandam",
         "2-04-cittuppadakandam", "2-05-cittuppadakandam", "3-01-rupakandam", "3-02-rupakandam", "3-03-rupakandam",
         "4-01-nikkhepakandam", "4-02-nikkhepakandam", "4-03-nikkhepakandam", "5-atthakathakandam"]
FIX = {("1-1066", "caratīti"): "कर रहा"}

mapped = {}
for p in PARTS:
    for line in (D / f"{p}.mapped.md").read_text(encoding="utf-8").splitlines():
        i, body = line.split("] ", 1)
        pairs = []
        for q in body.split(", "):
            k, v = q.split("=", 1)
            v = FIX.get((i[1:], k), v)
            pairs.append(f"{k}={v}")
        mapped[i[1:]] = ", ".join(pairs)
out, bad = [], []
for line in SRC.read_text(encoding="utf-8-sig").splitlines():
    if not line.strip():
        continue
    i, body = line.split("] ", 1)
    m = mapped.get(i[1:])
    if m is None or [k.strip() for k in body.split(", ")] != [q.split("=", 1)[0] for q in m.split(", ")]:
        bad.append(i)
    out.append(f"{i}] {m}")
if bad:
    sys.exit(f"mismatch: {bad[:10]}")
OUT.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
pairs = sum(len(l.split("] ", 1)[1].split(", ")) for l in out)
nde = sum(l.count("=(no direct equivalent)") for l in out)
print(OUT.name, "lines", len(out), "pairs", pairs, "no-equivalent", nde, "extra parts:", set(mapped) - {l[1:l.index("]")] for l in out})
