"""phase 3 task 4: the three checks of the phase-1 brief on all 75 *.mapped.md (preservation `bad`, presence failures,
«, » / «၊» / « / » in a value), plus the (no direct equivalent) count; writes work/p3_verify_all.txt."""
import sys, pathlib, hashlib, collections
D = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(D)); sys.dont_write_bytecode = True
import map7_rules as R
L, tot = [], collections.Counter()
for ch in R.chapters():
    n, bad, fails, punct, ruled = R.verify_file(ch)
    text = (D / f"{ch}.mapped.md").read_text(encoding="utf-8")
    nde = text.count("=" + R.NONE)
    kws = sum(len(k) for _, k in R.keyword_rows(ch))
    L.append(f"{ch}: lines {n} keywords {kws} bad {bad} presence-fails {len(fails)} punct {len(punct)} NDE {nde} "
             f"ruled {len(ruled)} md5 {hashlib.md5(text.encode('utf-8')).hexdigest()}")
    for f in fails:
        L.append(f"   FAIL {f}")
    for p in punct:
        L.append(f"   PUNCT {p}")
    tot.update(chapters=1, lines=n, keywords=kws, bad=len(bad), fails=len(fails), punct=len(punct), nde=nde,
               ruled=len(ruled))
L.append("TOTAL " + " ".join(f"{k} {v}" for k, v in tot.items()))
(D / "work/p3_verify_all.txt").write_text("\n".join(L) + "\n", encoding="utf-8")
print(L[-1])
