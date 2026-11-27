"""read-only helper (g2): occurrences of a Burmese / Pāli string in the group's chapter texts. usage: g2_grep.py STR [my|pa] [ch-prefix] [width]"""
import sys, re, pathlib
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import map6_rules as R
s = sys.argv[1]; which = sys.argv[2] if len(sys.argv) > 2 else "my"; pre = sys.argv[3] if len(sys.argv) > 3 else ""
w = int(sys.argv[4]) if len(sys.argv) > 4 else 30
for ch in R.CHAPTERS:
    if not ch.startswith(pre) or ch == "preamble":
        continue
    segs = R.burmese(ch) if which == "my" else R.pali(ch)
    n = 0
    for sid, t in segs.items():
        for m in re.finditer(re.escape(s), t):
            n += 1
            if n <= 3:
                print(f"{ch} ^{sid}: …{t[max(0, m.start()-w):m.end()+w]}…")
    if n:
        print(f"  {ch}: {n}")
