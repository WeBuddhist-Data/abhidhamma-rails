"""g4_grep.py ch sid regex [width]: the matches of a regex in one segment's Burmese (or Pāli with 'pi:' prefix)."""
import sys, re, pathlib
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R
ch, sid, rx = sys.argv[1], sys.argv[2], sys.argv[3]
w = int(sys.argv[4]) if len(sys.argv) > 4 else 80
src = R.burmese(ch)
if rx.startswith("pi:"):
    rx = rx[3:]; src = R.pali(ch)
t = src.get(sid, "")
for m in re.finditer(rx, t):
    print(f"[{sid}] …{t[max(0, m.start()-w):m.end()+w]}…")
