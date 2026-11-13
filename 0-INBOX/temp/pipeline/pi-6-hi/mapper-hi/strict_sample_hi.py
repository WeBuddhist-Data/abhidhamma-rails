"""List the values of a mapped file that pass the presence check only through the pi-6 tolerances
(«नहीं» as a dropped negative, gender/number of the tense endings), i.e. fail pi-1's plain present().
usage: python -I -X utf8 strict_sample_hi.py <file>"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import HERE, NDE, read_hindi, _present_pi1  # noqa: E402

f = sys.argv[1]
hi = read_hindi(f)
n = 0
for line in (HERE / f"{f}.mapped.md").read_text(encoding="utf-8").splitlines():
    if "] " not in line:
        continue
    bid, rest = line.split("] ", 1)
    text = hi.get(bid[1:], "").replace("सबमें", "सब में")
    for pair in rest.split(", "):
        kw, v = pair.split("=", 1)
        if v != NDE and not _present_pi1(v, text):
            n += 1
            print(bid[1:], kw, v)
print(f, "tolerance-only passes:", n)
