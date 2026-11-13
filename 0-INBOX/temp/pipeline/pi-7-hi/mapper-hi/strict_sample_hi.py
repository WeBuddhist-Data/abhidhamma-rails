"""Helper for the pi-7 sample: list the mapped values that do NOT occur literally in their segment's Hindi
(they pass the presence check only through inflection tolerance) so they can be read by eye. Unique pairs.
usage: python -I -B -X utf8 strict_sample_hi.py <file> [<file> ...]
"""
import collections
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import HERE, NDE, read_hindi  # noqa: E402

for f in sys.argv[1:]:
    hi = read_hindi(f)
    seen = collections.Counter()
    for line in (HERE / f"{f}.mapped.md").read_text(encoding="utf-8").splitlines():
        bid, _, rest = line.partition("] ")
        text = hi.get(bid[1:], "").replace(",", "")
        for pair in rest.split(", "):
            kw, v = pair.split("=", 1)
            if v != NDE and not all(part in text for part in v.split(" … ")):
                seen[(kw, v)] += 1
    print("=====", f, len(seen))
    for (kw, v), c in sorted(seen.items()):
        print(f"  {c:3} {kw} = {v}")
