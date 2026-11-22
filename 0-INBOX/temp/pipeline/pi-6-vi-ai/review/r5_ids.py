import sys, re
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
from r5_lib import *
pat = re.compile(sys.argv[1])
side = sys.argv[2] if len(sys.argv) > 2 else "v"
ids = OrderedDict(); n = 0
for fn, ln, sid, P, V in pairs():
    t = V if side == "v" else P
    k = len(pat.findall(t))
    if k:
        n += k
        ids.setdefault(fn[3:5], OrderedDict())[sid] = 1
print("hits", n)
for f, d in ids.items():
    nums = [int(x.split("-")[-1]) for x in d]
    print(f, "^6-10-%d..%d (%d segs)" % (min(nums), max(nums), len(nums)))
