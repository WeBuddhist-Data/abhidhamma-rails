"""Cross-chapter audit for chapters 2/3/8/9 (+ the sample): keywords with more than one value.

usage: python -I -X utf8 xaudit_2-3-8-9_hi.py
"""
import collections
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
CHS = ["1-khandhavibhango", "2-ayatanavibhango", "3-dhatuvibhango", "8-sammappadhanavibhango", "9-iddhipadavibhango"]
vals = collections.defaultdict(lambda: collections.defaultdict(set))
for ch in CHS:
    for line in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
        bid, rest = line.split("] ", 1)
        for pair in rest.split(", "):
            k, v = pair.split("=", 1)
            vals[k[:1].lower() + k[1:]][v].add(ch.split("-")[0])
for k in sorted(vals):
    if len(vals[k]) > 1:
        print(k, "::", " | ".join(f"{v} [{','.join(sorted(c))}]" for v, c in vals[k].items()))
