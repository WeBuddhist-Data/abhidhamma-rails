"""grep_g3.py ch sid regex: the Burmese matches (with 60 chars of context) of a segment; with --p the Pāli (read-only)."""
import sys, re, pathlib
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R
ch, sid, rx = sys.argv[1:4]
t = (R.pali(ch) if "--p" in sys.argv else R.burmese(ch))[sid]
w = int(sys.argv[4]) if len(sys.argv) > 4 and sys.argv[4].isdigit() else 60
for m in re.finditer(rx, t):
    print("…" + t[max(0, m.start() - w):m.end() + w] + "…")
