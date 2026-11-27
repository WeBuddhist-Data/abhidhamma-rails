"""read-only helper: first N segments (whole book) that have keyword K: Pāli and Burmese (cut). usage: kw6.py K [N] [width]"""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import map6_rules as R
k = sys.argv[1]; n = int(sys.argv[2]) if len(sys.argv) > 2 else 2; w = int(sys.argv[3]) if len(sys.argv) > 3 else 700
c = 0
for ch in R.CHAPTERS:
    for sid, kws in R.keyword_rows(ch):
        if k in kws:
            print(f"== {ch} ^{sid}\n PA: {R.pali(ch)[sid][:w]}\n MY: {R.burmese(ch)[sid][:w]}")
            c += 1
            if c >= n: sys.exit()
