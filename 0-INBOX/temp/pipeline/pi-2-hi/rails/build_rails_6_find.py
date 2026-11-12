"""Helper for ch6: find a Pāli regex in the finished rails books and print the aligned Hindi line.

usage: python -I -X utf8 build_rails_6_find.py <regex> [books=1,3,4,5] [max_hits=3] [max_chars=1500]
Lines of AI_translation/pali/pi-N_split_chapters/<f> and
AI_translation/hindi/pi-N-hindi-plain-rails_split_chapters/<f> align one to one (non-empty lines).
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
pat = re.compile(sys.argv[1])
books = (sys.argv[2] if len(sys.argv) > 2 else "1,3,4,5").split(",")
max_hits = int(sys.argv[3]) if len(sys.argv) > 3 else 3
max_chars = int(sys.argv[4]) if len(sys.argv) > 4 else 1500


def lines(p):
    return [l for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


hits = 0
for b in books:
    pdir = ROOT / "AI_translation" / "pali" / f"pi-{b}_split_chapters"
    hdir = ROOT / "AI_translation" / "hindi" / f"pi-{b}-hindi-plain-rails_split_chapters"
    for pf in sorted(pdir.glob("*.md")):
        hf = hdir / pf.name
        if not hf.exists():
            continue
        pl, hl = lines(pf), lines(hf)
        for i, l in enumerate(pl):
            m = pat.search(l)
            if not m:
                continue
            s = max(0, m.start() - 150)
            print(f"== pi-{b} {pf.name} #{i} (pali len {len(l)}, hindi len {len(hl[i]) if i < len(hl) else -1})")
            print("P:", l[s:m.end() + 250])
            if i < len(hl):
                print("H:", hl[i][:max_chars])
            hits += 1
            if hits >= max_hits:
                sys.exit(0)
