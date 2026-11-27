"""g2 dev helper: list unmapped and stem-fallback uses of the g2 chapters, with segment text."""
import sys, pathlib
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import map7_rules as R
CH = [c for c in R.chapters() if c.startswith("2-")]
M = R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK, R.LEXW]))
show = "-s" in sys.argv
for ch in CH:
    B, P = R.burmese(ch), R.pali(ch)
    for sid, kws in R.keyword_rows(ch):
        for k in kws:
            try:
                v = M.lookup(ch, sid, k, P.get(sid, ""), B.get(sid, ""))
            except KeyError:
                print(f"UNM\t{ch}\t{sid}\t{k}")
                if show:
                    print("   P:", P.get(sid, "")[:400]); print("   B:", B.get(sid, "")[:500])
                continue
            if M.SRC.get((sid, k)) == "stem":
                print(f"STEM\t{ch}\t{sid}\t{k}\t{v}")
                if show:
                    print("   P:", P.get(sid, "")[:400]); print("   B:", B.get(sid, "")[:500])
