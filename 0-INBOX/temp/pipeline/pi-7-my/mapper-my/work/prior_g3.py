"""prior_g3.py kw [kw …]: the pi-1 … pi-6 values of keywords (and their case siblings / base forms), the pi-7 terms and
heading-lexicon values (read-only helper)."""
import sys, pathlib
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R
for kw in sys.argv[1:]:
    ks = [kw] + R.case_siblings(R.low(kw)) + R.base_forms(kw)
    print("==", kw)
    for k in dict.fromkeys(ks):
        for t in R.PRIOR_ORDER:
            c = R.prev_vals(k, t)
            if c:
                print(f"   {k} {t}: {c.most_common(5)}")
        if R.terms().get(R.low(k)):
            print(f"   {k} terms: {R.terms()[R.low(k)]}")
        if R.head_lex().get(R.low(k)):
            print(f"   {k} headlex: {R.head_lex()[R.low(k)].most_common(3)}")
        if R.low(k) in R.LEXW:
            print(f"   {k} LEXW: {R.LEXW[R.low(k)]}")
