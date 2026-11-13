"""Print Hindi sentence contexts (split at । ? ;) containing a Hindi regex, on lines whose Pāli matches a regex.
usage: python -I -B -X utf8 hz7_ctx.py <pali-regex> <hindi-regex> [max] [file-prefix]
Also prints the aligned Pāli sentence (same index) when the sentence counts match.
"""
import sys, re, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hz7_common import PARTS, pairs, short

pr, hr = re.compile(sys.argv[1]), re.compile(sys.argv[2])
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 80
pref = sys.argv[4] if len(sys.argv) > 4 else ""
n = 0
for part in PARTS:
    if not part.startswith(pref):
        continue
    for i, (p, h) in enumerate(pairs(part)):
        if not pr.search(p):
            continue
        hs = re.split(r"(?<=[।?;])\s+", h)
        ps = re.split(r"(?<=[.?;])\s+", p)
        for j, s in enumerate(hs):
            if hr.search(s):
                n += 1
                if n <= mx:
                    print(f"{short(part)}:{i+1}  H: {s[:500]}")
                    if len(ps) == len(hs):
                        print(f"          P: {ps[j][:400]}")
print("hits:", n)
