"""Show Hindi pi-3/4/5 zero-shot blocks whose Pāli block contains a pattern (read-only helper, part 2-03).

usage: python -I -X utf8 kwic_2-03_hi.py <book pi-3|pi-4|pi-5> <regex> [max]
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
book, pat = sys.argv[1], re.compile(sys.argv[2])
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 3
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def blocks(d):
    out = {}
    for f in sorted(d.glob("*.md")):
        buf = []
        for line in f.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            buf.append(line)
            m = ID.search(line)
            if m:
                out[m.group(1)] = "\n".join(buf)
                buf = []
    return out


P = blocks(ROOT / "AI_translation" / "pali" / f"{book}_split_chapters")
H = blocks(ROOT / "AI_translation" / "hindi" / f"{book}-hindi-plain-zeroshot_split_chapters")
n = 0
for bid, txt in P.items():
    if pat.search(txt):
        print("=== ^" + bid)
        print("PI:", txt[:700])
        print("HI:", H.get(bid, "?")[:900])
        n += 1
        if n >= mx:
            break
