"""phase 3: the three checks over all 32 *.mapped.md: preservation (bad), presence failures, «, » / «၊» / « / » and pair
count (punct), the ending-rule chunks by rule; also every (no direct equivalent). usage: verify_all.py"""
import sys, pathlib, collections
D = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(D))
import map5_rules as R
tot = collections.Counter(); rules = collections.Counter()
for ch in R.CHAPTERS:
    n, bad, fails, punct, ruled = R.verify_file(ch)
    nne = sum(l.count("=" + R.NONE) for l in (D / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines())
    kw = sum(len(l.split("] ", 1)[1].split(", ")) for l in (D / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines())
    print(f"{ch}\tlines {n}\tkeywords {kw}\tbad {bad}\tpresence failures {len(fails)}\tpunct {punct}\tending-rule chunks {len(ruled)}\t(no direct equivalent) {nne}")
    tot.update(lines=n, kw=kw, bad=len(bad), fails=len(fails), punct=len(punct), ruled=len(ruled), nne=nne)
    rules.update(r for *_, r in ruled)
    for f in fails:
        print("   FAIL", f)
print("TOTAL", dict(tot)); print("ending rules", dict(rules))
