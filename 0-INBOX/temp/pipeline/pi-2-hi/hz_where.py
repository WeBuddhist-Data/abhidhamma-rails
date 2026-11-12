"""Print aligned Pāli/Hindi lines whose Pāli matches a regex.
usage: hz_where.py <pali-regex> [chapter-numbers comma-separated] [--bak] [--h=<hindi-regex>] [--w=<maxchars>]"""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hz_common
from hz_common import PARTS, pairs, short

if "--bak" in sys.argv:
    hz_common.CUR["hdir"] = os.path.join(hz_common.HERE, "backup-pre-harmonise")
opts = {a.split("=")[0]: a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--") and "=" in a}
args = [a for a in sys.argv[1:] if not a.startswith("--")]
rx = re.compile(args[0])
chs = set(args[1].split(",")) if len(args) > 1 else None
hx = re.compile(opts["--h"]) if "--h" in opts else None
w = int(opts.get("--w", "100000"))
for part in PARTS:
    if chs and part.split("-")[0] not in chs:
        continue
    for i, (p, h) in enumerate(pairs(part)):
        if rx.search(p) and (not hx or hx.search(h)):
            print(f"[{short(part)} #{i}] P: {p[:w]}")
            print(f"[{short(part)} #{i}] H: {h[:w]}")
