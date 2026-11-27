"""usage: stemcheck.py N [N…] — for the numbered rows of work/stem-uniq.txt: every segment, the Pāli around the keyword
and the Burmese around the value"""
import sys, re, pathlib
D = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(D))
import map5_rules as R
own = {sid: ch for ch in R.CHAPTERS for sid in R.pali(ch)}
uniq = {l.split("\t")[0]: l.split("\t") for l in (D / "work/stem-uniq.txt").read_text(encoding="utf-8").splitlines()}
uses = [l.split("\t") for l in (D / "work/stem-uses.tsv").read_text(encoding="utf-8").splitlines()]
for n in sys.argv[1:]:
    _, k, v = uniq[n][:3]
    print(f"### {n} {k} = {v}")
    for ch, sid, kk, vv, *_ in uses:
        if kk == k and vv == v:
            pa, my = R.strip_brackets(R.pali(ch)[sid]), R.burmese(ch)[sid]
            m = re.search(re.escape(R.low(k)[:max(3, len(k) - 2)]), pa, flags=re.I)
            st = v.split(" … ")[0]
            st = st[:-3] if st.endswith(("သော", "သည်")) else st
            b = my.find(st)
            print("  ", sid, "PI:", pa[max(0, m.start() - 50): m.start() + 60] if m else "-")
            print("        MY:", my[max(0, b - 50): b + len(st) + 40] if b >= 0 else "-")
