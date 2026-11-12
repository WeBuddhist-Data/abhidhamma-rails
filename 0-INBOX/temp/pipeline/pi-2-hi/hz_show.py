"""Show aligned Pāli/Hindi lines of given segments.  usage: hz_show.py <chapter-prefix> <segid> [<segid> ...] [--bak]"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hz_common
from hz_common import PARTS, segments

if "--bak" in sys.argv:
    hz_common.CUR["hdir"] = os.path.join(hz_common.HERE, "backup-pre-harmonise")
args = [a for a in sys.argv[1:] if not a.startswith("--")]
part = [p for p in PARTS if p.split("-")[0] == args[0]][0]
for sid, ps, hs in segments(part):
    if sid in args[1:]:
        for p, h in zip(ps, hs):
            print("P:", p)
            print("H:", h)
        print("-----")
