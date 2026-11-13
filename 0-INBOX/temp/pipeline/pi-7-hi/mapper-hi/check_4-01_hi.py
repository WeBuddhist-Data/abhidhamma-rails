"""Targeted checks for 4-01 (values whose presence check is weak).
usage: python -I -B -X utf8 check_4-01_hi.py"""
import sys, pathlib; sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_hindi, HERE

F = "4-01-kilesagocchaka"
hi = read_hindi(F)
NEED = {   # value -> literal string that must be in the segment's Hindi
    "सत्य-दर्शन … न": "सत्य-दर्शन से न ",
    "मानसिक अभ्यास … न": "मानसिक अभ्यास से न ",
    "सत्य-दर्शन … रहित": "सत्य-दर्शन से छोड़े जाने वाले मूलों से रहित",
    "मानसिक अभ्यास … रहित": "मानसिक अभ्यास से छोड़े जाने वाले मूलों से रहित",
    "भी": "भी",
}
bad = []
for line in (HERE / f"{F}.mapped.md").read_text(encoding="utf-8").splitlines():
    bid, _, rest = line.partition("] ")
    bid = bid[1:]
    for pair in rest.split(", ") if rest else []:
        kw, v = pair.split("=", 1)
        if v in NEED and NEED[v] not in hi.get(bid, ""):
            bad.append((bid, kw, v))
print("weak-value check:", len(bad), bad[:20])
