"""Print full Pāli/Hindi of segment lines. usage: hz_show.py <part-prefix>:<id>[:k] ... [--bak]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hz_common import PARTS, HERE, segments

hdir = os.path.join(HERE, "backup-pre-harmonise") if "--bak" in sys.argv else None
for arg in [a for a in sys.argv[1:] if not a.startswith("--")]:
    bits = arg.split(":")
    part = next(p for p in PARTS if p.startswith(bits[0]))
    for sid, ps, hs in (segments(part, hdir) if hdir else segments(part)):
        if sid == bits[1]:
            ks = [int(bits[2])] if len(bits) > 2 else range(len(ps))
            for k in ks:
                print(f"--- {part[:4]}:{sid}:{k}\nP: {ps[k]}\nH: {hs[k]}")
