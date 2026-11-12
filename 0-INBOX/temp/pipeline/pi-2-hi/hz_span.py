"""Unique Hindi spans (matching <hindi-regex>) on lines whose Pāli matches <pali-regex>, with chapters.
usage: hz_span.py <pali-regex> <hindi-regex> [--bak]"""
import sys, os, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hz_common
from hz_common import PARTS, pairs, short

if "--bak" in sys.argv:
    hz_common.CUR["hdir"] = os.path.join(hz_common.HERE, "backup-pre-harmonise")
args = [a for a in sys.argv[1:] if not a.startswith("--")]
rp, rh = re.compile(args[0]), re.compile(args[1])
res = collections.defaultdict(collections.Counter)
for part in PARTS:
    for p, h in pairs(part):
        if rp.search(p):
            for m in rh.finditer(h):
                res[m.group(0)][short(part)] += 1
for s, c in sorted(res.items(), key=lambda kv: -sum(kv[1].values())):
    print(dict(c), "::", s)
