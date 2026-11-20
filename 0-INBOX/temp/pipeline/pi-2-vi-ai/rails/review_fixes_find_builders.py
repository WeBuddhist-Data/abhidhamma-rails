"""Which rails builder scripts (rails/build_rails_*_vi.py) carry the old wording of each review-fix rule.
Prints rule id, the searched string and the builder files (with line numbers) where it occurs; when the full old
string is not found (constants are often assembled from pieces), the longest piece between punctuation is tried.
"""
import glob, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import review_fixes_vi as F

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = {os.path.basename(p): open(p, encoding="utf-8").read().splitlines()
       for p in sorted(glob.glob(os.path.join(HERE, "build_rails_*_vi.py")))}


def where(s):
    out = []
    for f, lines in SRC.items():
        ln = [str(i + 1) for i, l in enumerate(lines) if s in l]
        if ln:
            out.append(f"{f}:{','.join(ln[:6])}{'…' if len(ln) > 6 else ''}")
    return out


seen = set()
for r in F.R:
    key = (r["rid"], r["old"] if not r["line"] else r["rid"])
    if key in seen:
        continue
    seen.add(key)
    if r["line"]:
        print(f"{r['rid']:20s} [whole line, pi-1 copy] must={r['old']!r}: {where(r['old']) or '-'}")
        continue
    old = r["old"].strip("”“;., ")
    hit = where(old)
    probe = old
    if not hit:
        pieces = sorted(re.split(r"[,;.:“”…–]\s*", old), key=len, reverse=True)
        for pc in pieces:
            if len(pc) >= 12:
                hit = where(pc)
                probe = pc
                if hit:
                    break
    print(f"{r['rid']:20s} {probe[:70]!r}: {', '.join(hit) if hit else '- (not in a builder constant)'}")
