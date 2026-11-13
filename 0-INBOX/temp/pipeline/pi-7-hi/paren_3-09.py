"""Helper for build_3-09_hi.py: list parentheticals of 3-09-mahantaraduka.md with the English zero-shot's
parenthetical at the same position (meaning cross-check only)."""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation")
P = ROOT / "pali" / "pi-7_split_chapters" / "3-09-mahantaraduka.md"
E = ROOT / "english" / "pi-7-english-plain-zeroshot_split_chapters" / "3-09-mahantaraduka.md"
pl = [l for l in P.read_text(encoding="utf-8").splitlines() if l.strip()]
el = [l for l in E.read_text(encoding="utf-8").splitlines() if l.strip()]
seen = {}
for a, b in zip(pl, el):
    pa = [m for m in re.findall(r"\(([^()]*)\)", a) if not re.fullmatch(r"\d+", m)]
    pb = [m for m in re.findall(r"\(([^()]*)\)", b) if not re.fullmatch(r"\d+", m)]
    for i, x in enumerate(pa):
        seen.setdefault(x, pb[i] if i < len(pb) and len(pa) == len(pb) else "?? " + " | ".join(pb))
if len(sys.argv) > 1 and sys.argv[1] == "--lines":
    for a, b in zip(pl, el):
        if sys.argv[2] in a:
            print("P:", a)
            print("E:", b)
            print()
    sys.exit()
for k in sorted(seen):
    print(repr(k), "=>", seen[k])
