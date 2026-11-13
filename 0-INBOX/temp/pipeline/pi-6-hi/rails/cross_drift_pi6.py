"""Find identical Pāli lines rendered differently across the pi-6 Hindi rails files.

usage: python -I -X utf8 cross_drift_pi6.py [min_files]
Lines align one to one (non-empty lines, block IDs stripped). Prints groups where one Pāli line has
2+ Hindi renderings, with the files using each; sorted by how many files are involved.
Writes cross-drift.md next to this script.
"""
import pathlib, re, sys
from collections import defaultdict

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
P = ROOT / "AI_translation/pali/pi-6_split_chapters"
H = ROOT / "AI_translation/hindi/pi-6-hindi-plain-rails_split_chapters"
OUT = pathlib.Path(__file__).with_name("cross-drift.md")
ID = re.compile(r"\s*\^[\w-]+\s*$")

def lines(f):
    return [ID.sub("", l).strip() for l in f.read_text(encoding="utf-8-sig").splitlines() if l.strip()]

groups = defaultdict(lambda: defaultdict(set))
for pf in sorted(P.glob("*.md")):
    hf = H / pf.name
    pl, hl = lines(pf), lines(hf)
    if len(pl) != len(hl):
        print("LINE COUNT", pf.name, len(pl), len(hl)); continue
    for a, b in zip(pl, hl):
        if a.startswith("#"):
            a = a.lstrip("#").strip(); b = b.lstrip("#").strip()
        if len(a) < 4:
            continue
        groups[a][b].add(pf.stem)

rows = []
for pali, hs in groups.items():
    if len(hs) > 1:
        files = set().union(*hs.values())
        if len(files) > 1:
            rows.append((len(files), pali, hs))
rows.sort(key=lambda r: (-r[0], r[1]))
out = [f"# Cross-file drift: {len(rows)} Pāli lines with 2+ Hindi renderings in 2+ files\n"]
for n, pali, hs in rows:
    out.append(f"## {pali}  ({n} files)")
    for h, fs in sorted(hs.items(), key=lambda kv: -len(kv[1])):
        out.append(f"- {h}  [{', '.join(sorted(fs))}]")
    out.append("")
OUT.write_text("\n".join(out), encoding="utf-8", newline="\n")
print(OUT.name, "groups", len(rows))
