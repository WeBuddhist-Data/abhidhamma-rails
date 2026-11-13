"""KWIC for 10-07..10-13: for a keyword (exact Pāli spelling, as a word or word start), print the aligned Pāli and
Hindi lines of the segments that list it as a keyword.
usage: python -I -X utf8 kwic_10b_hi.py <file|all> <keyword> [max]"""
import pathlib
import re
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_keywords, read_hindi, read_pali  # noqa: E402

FILES = [f"10-{n:02d}-indriyayamaka" for n in range(7, 14)]
which, kw = sys.argv[1], sys.argv[2]
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 4
files = FILES if which == "all" else [which]
n = 0
for f in files:
    pi, hi = read_pali(f), read_hindi(f)
    for bid, kws in read_keywords(f):
        if kw not in kws:
            continue
        pl, hl = pi.get(bid, "").splitlines(), hi.get(bid, "").splitlines()
        hits = [i for i, l in enumerate(pl) if re.search(r"(?<![^\W\d_])" + re.escape(kw), l)]
        print(f"=== {f} {bid} (pali lines {len(pl)}, hindi lines {len(hl)})")
        for i in hits[:2]:
            print("  PI:", pl[i])
            print("  HI:", hl[i] if i < len(hl) else "?")
        if not hits:
            print("  (keyword not found verbatim in the Pāli)")
        n += 1
        if n >= mx:
            sys.exit()
