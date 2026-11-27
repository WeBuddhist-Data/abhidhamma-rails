"""read-only helper (g1): values in the G1 mapped files that the segment's Burmese does not have as a phrase (every
« … » part, its final «သည် / သော» by an ending rule; also without quotes / the list comma): present only chunk by chunk."""
import sys, re, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import map6_rules as R
from map_g1 import G1
c = collections.Counter()
for ch in sys.argv[1:] or G1:
    my = R.burmese(ch)
    for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
        sid, rest = l[1:].split("] ", 1)
        t = my[sid]
        vs = [t, R.flat(t), re.sub("[“”]", "", t), R.flat(re.sub("[“”]", "", t)), re.sub(r" ?\[[^\]]*\]", "", t)]
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            if v == R.NONE:
                continue
            if not any(R.phrase_ok(v, x) for x in vs):
                c[(ch, k, v)] += 1
for (ch, k, v), n in sorted(c.items()):
    print(ch, k, "=", v, n)
