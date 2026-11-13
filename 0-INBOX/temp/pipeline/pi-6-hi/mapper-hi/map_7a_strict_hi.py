"""Strict check for map_7a_hi.py: values that pass only through a pi-6 / Anusaya tolerance, and keywords whose
form does not occur in the segment's Pāli. Prints only.
usage: python -I -X utf8 map_7a_strict_hi.py <file> [...]"""
import collections
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_7_common_hi import HERE, NDE, read_hindi, read_pali, present, present7  # noqa: E402
from map_common_hi import present as present_pi1  # noqa: E402

for f in sys.argv[1:]:
    hi, pi = read_hindi(f), read_pali(f)
    only7, onlymod, nopali = collections.Counter(), collections.Counter(), []
    for line in (HERE / f"{f}.mapped.md").read_text(encoding="utf-8").splitlines():
        bid, _, rest = line.partition("] ")
        bid = bid[1:]
        if not rest:
            continue
        for pair in rest.split(", "):
            kw, v = pair.split("=", 1)
            if kw != NDE and kw.lower() not in (pi.get(bid) or "").lower():
                nopali.append((bid, kw))
            if v == NDE:
                continue
            t = hi.get(bid)
            if not present_pi1(v, t):
                (onlymod if present(v, t) else only7)[(kw, v)] += 1
    print(f, "| pass only via present7 (सोया~सोई):", dict(only7))
    print("   pass only via the pi-6 module tolerances:", dict(onlymod))
    print("   keyword not in the segment's Pāli:", nopali)
