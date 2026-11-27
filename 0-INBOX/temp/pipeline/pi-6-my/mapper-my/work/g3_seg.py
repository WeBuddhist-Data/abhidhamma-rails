"""read-only helper (g3): print KW / PA / MY of one segment, or only the Pāli and Burmese sentences that contain a
Pāli word (KWIC). usage: g3_seg.py CH SID [pali-word]"""
import sys, re, pathlib
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import map6_rules as R
ch, sid = sys.argv[1], sys.argv[2]
w = sys.argv[3] if len(sys.argv) > 3 else None
kws = dict(R.keyword_rows(ch))[sid]
print("KW:", ", ".join(kws))
pa, my = R.pali(ch)[sid], R.burmese(ch)[sid]
if not w:
    print("PA:", pa); print("MY:", my); sys.exit()
ps = re.split(r"(?<=[.?])\s+", pa); ms = re.split(r"(?<=။)\s*", my)
for i, s in enumerate(ps):
    if w in s:
        print(f"PA[{i}]:", s)
for i, s in enumerate(ms):
    if len(sys.argv) > 4 and sys.argv[4] in s:
        print(f"MY[{i}]:", s)
