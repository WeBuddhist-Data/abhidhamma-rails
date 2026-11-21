"""List the builder lines (build_<N>_vi.py) that hold the old string of each harmonise rule (best effort:
f-string builders may assemble a string from parts, then nothing is found and the rule is listed as 'assembled').

usage: python -I -X utf8 builder_hits_vi.py
"""
import os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harmonise_vi as H

HERE = os.path.dirname(os.path.abspath(__file__))
seen = collections.OrderedDict()
for rid, part, sid, old, new, n, why in H.R:
    ch = part.split("-")[0]
    f = os.path.join(HERE, f"build_{ch}_vi.py")
    lines = open(f, encoding="utf-8").read().splitlines()
    probe = old.strip(" ,.?”")
    # try the full string, then its longest comma-free piece
    hits = [i + 1 for i, l in enumerate(lines) if probe in l]
    if not hits:
        piece = max(probe.replace("…", ",").split(","), key=len).strip()
        hits = [i + 1 for i, l in enumerate(lines) if len(piece) > 8 and piece in l]
    key = (ch, rid)
    seen.setdefault(key, set()).update(hits)
for (ch, rid), hits in seen.items():
    print(f"build_{ch}_vi.py {rid}: " + (", ".join(map(str, sorted(hits))) if hits else "assembled (no literal)"))
