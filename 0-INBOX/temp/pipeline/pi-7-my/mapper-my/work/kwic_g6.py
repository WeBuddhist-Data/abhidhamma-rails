"""kwic_g6.py: for each distinct U/S keyword of dev-g6.txt (first segment), a Pāli window around the keyword and a
Burmese window at the same relative position."""
import sys, pathlib
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import map7_rules as R
rows, seen = [], set()
for l in (HERE / "work/dev-g6.txt").read_text(encoding="utf-8").splitlines():
    if l.startswith("  U\t") or l.startswith("  S\t"):
        _, ch, sid, kw = l.strip().split("\t")
        k = kw.split("=")[0]
        if R.low(k) in seen:
            continue
        seen.add(R.low(k))
        rows.append((ch, sid, kw))
W = int(sys.argv[1]) if len(sys.argv) > 1 else 160
for ch, sid, kw in rows:
    k = kw.split("=")[0]
    pa = R.pali(ch)[sid]; my = R.burmese(ch)[sid]
    i = pa.find(k)
    r = i / max(1, len(pa))
    j = int(r * len(my))
    print(f"== {ch} {sid} {kw}")
    print("  P:", pa[max(0, i - W // 2): i + W])
    print("  M:", my[max(0, j - W): j + 2 * W])
