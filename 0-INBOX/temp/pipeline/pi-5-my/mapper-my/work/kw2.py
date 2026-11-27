"""KWIC: CH SID word [word …]: Pāli context and the Burmese at the same relative position (±W chars)."""
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import map5_rules as R
ch, sid = sys.argv[1], sys.argv[2]
W = 130
pa = R.strip_brackets(R.pali(ch)[sid]); my = re.sub(r"\s*\[[^\]]*\]", "", R.burmese(ch)[sid])
for w in sys.argv[3:]:
    i = pa.lower().find(w.lower())
    if i < 0:
        print(w, "NOT IN PALI"); continue
    j = int(i / len(pa) * len(my))
    print(f"--{w}: P: {pa[max(0,i-50):i+70]}\n   M: {my[max(0,j-W):j+W]}")
