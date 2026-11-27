"""read-only helper (g3): module-only dry run of the G3 chapters: per (kw, value, source) counts, unmapped,
values not a phrase of the segment. usage: dry_g3.py [--pairs] [--unmapped] [--nophrase] [--stem]"""
import sys, re, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import map6_rules as R
G3 = ["9-01-dhammayamaka", "9-02-dhammayamaka", "9-03-dhammayamaka"] + [f"10-{i:02d}-indriyayamaka" for i in range(1, 14)]
M = R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK]))
pairs = collections.Counter(); ex = {}
unm = collections.Counter(); unm_ex = {}
nop = collections.Counter()
for ch in G3:
    my, pa = R.burmese(ch), R.pali(ch)
    for sid, kws in R.keyword_rows(ch):
        t = my[sid]
        vs = [t, R.flat(t), re.sub("[“”]", "", t), R.flat(re.sub("[“”]", "", t))]
        for kw in kws:
            try:
                v = M.lookup(ch, sid, kw, pa.get(sid, ""), t)
            except KeyError:
                unm[kw] += 1; unm_ex.setdefault(kw, (ch, sid)); continue
            s = M.SRC.get((sid, kw), "?")
            pairs[(kw, v, s)] += 1; ex.setdefault((kw, v, s), (ch, sid))
            if v != R.NONE and not any(R.phrase_ok(v, x) for x in vs):
                nop[(kw, v, s)] += 1; ex.setdefault(("NP", kw, v), (ch, sid))
a = sys.argv[1:]
if "--pairs" in a:
    for (k, v, s), c in sorted(pairs.items(), key=lambda x: (R.low(x[0][0]), x[0][1])):
        print(f"{k} = {v} | {c} | {s} | {ex[(k, v, s)]}")
if "--stem" in a:
    for (k, v, s), c in sorted(pairs.items()):
        if s == "stem": print(f"STEM {k} = {v} | {c} | {ex[(k, v, s)]}")
if "--unmapped" in a:
    for k, c in sorted(unm.items()):
        print(f"UNM {k} | {c} | {unm_ex[k]}")
if "--nophrase" in a:
    for (k, v, s), c in sorted(nop.items()):
        print(f"NOPHRASE {k} = {v} | {c} | {s} | {ex[('NP', k, v)]}")
print("pairs", len(pairs), "uses", sum(pairs.values()), "unmapped", sum(unm.values()), len(unm), "nophrase", sum(nop.values()))
