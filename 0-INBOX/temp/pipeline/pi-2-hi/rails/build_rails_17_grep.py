"""Find a Pali substring in pi-1 (and optionally pi-3/4/5 not aligned) and print the aligned pi-1 rails Hindi line.

usage: python -I -X utf8 build_rails_17_grep.py <pali substring> [maxhits] [hindi-window]
Prints Pali line (window around the match) and the full aligned Hindi line (or truncated to hindi-window chars).
"""
import pathlib
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PD = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
HD = ROOT / "AI_translation" / "hindi" / "pi-1-hindi-plain-rails_split_chapters"

pat = sys.argv[1]
maxhits = int(sys.argv[2]) if len(sys.argv) > 2 else 3
hw = int(sys.argv[3]) if len(sys.argv) > 3 else 100000

hits = 0
for pf in sorted(PD.glob("*.md")):
    hf = HD / pf.name
    if not hf.exists():
        continue
    p = [l for l in pf.read_text(encoding="utf-8").splitlines() if l.strip()]
    h = [l for l in hf.read_text(encoding="utf-8").splitlines() if l.strip()]
    for i, line in enumerate(p):
        k = line.find(pat)
        if k < 0:
            continue
        print(f"== {pf.name}:{i}  P: ...{line[max(0, k - 150):k + 250]}...")
        print(f"   H: {h[i][:hw] if i < len(h) else '(no line)'}")
        hits += 1
        if hits >= maxhits:
            sys.exit(0)
print(f"({hits} hits)")
