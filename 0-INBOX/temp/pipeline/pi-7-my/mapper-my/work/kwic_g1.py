"""g1 helper: kwic_g1.py CH SID PALIWORD [BURMESE...]: Pāli context of the word, Burmese context of each given string."""
import sys, pathlib, re
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import map7_rules as R
ch, sid, w = sys.argv[1:4]
my, pa = R.burmese(ch)[sid], R.pali(ch).get(sid, "")
W = int(80)
for m in list(re.finditer(re.escape(w), pa))[:2]:
    print("PA:", pa[max(0, m.start()-W):m.end()+W].replace("\n", " "))
for b in sys.argv[4:]:
    for m in list(re.finditer(re.escape(b), my))[:2]:
        print("MY:", my[max(0, m.start()-W):m.end()+W].replace("\n", " "))
    print("presence", b, R.presence(b, my))
