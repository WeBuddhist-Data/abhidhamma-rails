"""Exploration helper for the harmonise pass: heading inventory and KWIC by Pāli regex.
usage: python -I -B -X utf8 hz7_explore.py heads [regex]   -> headings whose Pāli matches regex
       python -I -B -X utf8 hz7_explore.py kwic <pali-regex> [hindi-regex] [max]
"""
import sys, re, collections, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hz7_common import PARTS, pairs, pnorm, hnorm, short


def heads(rx=None):
    g = collections.defaultdict(lambda: collections.defaultdict(list))
    for part in PARTS:
        for i, (p, h) in enumerate(pairs(part)):
            if not p.startswith("#"):
                continue
            kp = pnorm(p).lstrip("#").strip().strip("*").strip()
            if rx and not re.search(rx, kp):
                continue
            kh = hnorm(h).lstrip("#").strip().strip("*").strip()
            g[kp][kh].append(f"{short(part)}:{i+1}")
    for kp in sorted(g):
        v = g[kp]
        if os.environ.get("DIVONLY") and len(v) < 2:
            continue
        print(f"## {kp}")
        for kh, locs in sorted(v.items(), key=lambda kv: -len(kv[1])):
            print(f"   [{len(locs)}] {kh}   {' '.join(sorted(set(l.split(':')[0] for l in locs)))} {locs[0]}")


def kwic(prx, hrx=None, mx=60):
    pr = re.compile(prx)
    hr = re.compile(hrx) if hrx else None
    n = 0
    cnt = collections.Counter()
    for part in PARTS:
        for i, (p, h) in enumerate(pairs(part)):
            if pr.search(p):
                if hr:
                    for m in hr.finditer(h):
                        cnt[m.group(0)] += 1
                    if not hr.search(h):
                        cnt["<none>"] += 1
                n += 1
                if n <= mx:
                    print(f"{short(part)}:{i+1}\n  P: {p[:600]}\n  H: {h[:700]}")
    print("matching lines:", n)
    for k, v in cnt.most_common(80):
        print(f"  {v:6d}  {k}")


def show(part, a, b, which="ph"):
    for i, (p, h) in enumerate(pairs(part)):
        if a <= i + 1 <= b:
            if "p" in which:
                print(f"{i+1} P: {p}")
            if "h" in which:
                print(f"{i+1} H: {h}")


if __name__ == "__main__":
    if sys.argv[1] == "show":
        show(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5] if len(sys.argv) > 5 else "ph")
    elif sys.argv[1] == "heads":
        heads(sys.argv[2] if len(sys.argv) > 2 else None)
    else:
        kwic(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] else None,
             int(sys.argv[4]) if len(sys.argv) > 4 else 60)
