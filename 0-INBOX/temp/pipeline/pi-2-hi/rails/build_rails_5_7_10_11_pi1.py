"""Lookup helper: grep the pi-1 Pali split chapters for a regex and print the aligned pi-1 rails Hindi line.

usage: python -I -X utf8 build_rails_5_7_10_11_pi1.py <regex> [maxhits] [context_chars]
Prints for each hit: file:line, a Pali window around the match, and the full Hindi line (or a window).
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PA = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
HI = ROOT / "AI_translation" / "hindi" / "pi-1-hindi-plain-rails_split_chapters"

pat = re.compile(sys.argv[1])
maxhits = int(sys.argv[2]) if len(sys.argv) > 2 else 3
win = int(sys.argv[3]) if len(sys.argv) > 3 else 0
hits = 0
for pf in sorted(PA.glob("*.md")):
    hf = HI / pf.name
    if not hf.exists():
        continue
    pl = pf.read_text(encoding="utf-8").splitlines()
    hl = hf.read_text(encoding="utf-8").splitlines()
    if len(pl) != len(hl):
        print("LINECOUNT MISMATCH", pf.name, len(pl), len(hl))
    for i, line in enumerate(pl):
        m = pat.search(line)
        if m:
            hits += 1
            a = max(0, m.start() - 80)
            print(f"== {pf.name}:{i + 1}")
            print("PA:", line[a:m.end() + 300] if win else line)
            h = hl[i] if i < len(hl) else ""
            print("HI:", h if not win else h[:win])
            if hits >= maxhits:
                sys.exit(0)
