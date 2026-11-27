"""row_g2.py: for each UNM / STEM line of work/dev_g2-out.txt (first use per keyword), the module's values of the
other keywords of the same Pāli sentence (read-only helper; g2)."""
import sys, re, pathlib
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R
M = R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK, R.LEXW]))
seen = set()
for l in (D / "work/dev_g2-out.txt").read_text(encoding="utf-8").splitlines():
    kind, ch, sid, kw = l.split("\t")[:4]
    if kw in seen:
        continue
    seen.add(kw)
    p = R.pali(ch).get(sid, ""); b = R.burmese(ch).get(sid, "")
    ps = re.split(r"(?<=[.)?])\s+", p)
    sent = next((s for s in ps if re.search(r"(?<![\wāīūṃṅñṭḍṇḷ])" + re.escape(kw) + r"(?![\wāīūṃṅñṭḍṇḷ])", s)), "")
    words = set(re.findall(r"[\wāīūṃṅñṭḍṇḷĀĪŪṄÑṬḌṆḶ]+", sent))
    kws = dict(R.keyword_rows(ch))[sid]
    out = []
    for k in dict.fromkeys(kws):
        if k in words:
            try:
                v = M.lookup(ch, sid, k, p, b)
            except KeyError:
                v = "?"
            out.append(f"{k}={v}")
    print(f"== {kw} | {ch} ^{sid}: " + ", ".join(out))
