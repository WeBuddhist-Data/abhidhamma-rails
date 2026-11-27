"""read-only helper (g1): for keyword KW in chapter CH: each segment's sid, the Pāli window around KW, the Burmese
window around the Burmese string B (optional; default: the Burmese parentheses and the last 200 chars).
usage: kwic_g1.py CH KW [B] [N]"""
import sys, re, pathlib
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import map6_rules as R
ch, kw = sys.argv[1], sys.argv[2]
b = sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] else None
n = int(sys.argv[4]) if len(sys.argv) > 4 else 6
c = 0
for sid, ks in R.keyword_rows(ch):
    if kw not in ks:
        continue
    pa, my = R.pali(ch).get(sid, ""), R.burmese(ch)[sid]
    i = pa.find(kw)
    print(f"== ^{sid} ({len(ks)} kw)\n PA: …{pa[max(0,i-150):i+150]}…")
    if b:
        for m in list(re.finditer(re.escape(b), my))[:3]:
            print(f" MY: …{my[max(0,m.start()-120):m.end()+120]}…")
        if b not in my:
            print(" MY: (not found)", my[-250:])
    else:
        print(" MY()", re.findall(r"\([^()]{4,}\)", my)[:4], "\n MYend:", my[-250:])
    c += 1
    if c >= n:
        break
