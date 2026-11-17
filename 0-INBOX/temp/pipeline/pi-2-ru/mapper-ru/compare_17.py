"""Consistency check for chapter 17: keywords whose ch17 value differs from the value the approved pi-1 / pi-4 maps
(or the earlier pi-2 chapters) give, where that prior value is ALSO present in the ch17 segment's Russian.
usage: python -I -X utf8 compare_17.py [pi1|pi4|pi2]"""
import pathlib
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import draft_17 as D  # noqa: E402
from map_common_pi2_ru import NDE, lc, present, read_russian  # noqa: E402

tags = set(sys.argv[1:]) or {"pi1", "pi4", "pi2"}
ru = read_russian("17-khuddakavatthuvibhango")
seen = set()
for line in (HERE / "17-khuddakavatthuvibhango.mapped.md").read_text(encoding="utf-8").splitlines():
    bid, rest = line.split("] ", 1)
    bid = bid[1:]
    for pair in rest.split(", "):
        k, v = pair.split("=", 1)
        alts = [(t, pv, n) for (t, pv), n in D.PRIOR[lc(k)].items()
                if t in tags and pv != v and pv != NDE and present(pv, ru.get(bid, ""))]
        if alts and (k, v) not in seen:
            seen.add((k, v))
            print(f"{bid}\t{k}={v}\t<- " + " | ".join(f"{t}:{pv}({n})" for t, pv, n in sorted(alts, key=lambda x: -x[2])))
