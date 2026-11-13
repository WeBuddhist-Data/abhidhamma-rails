"""Parenthetical editorial notes: pair "(…)" segments of Pāli and Hindi lines (by order, when the counts match,
labels like (Ka)/(1) excluded) and group by the Pāli text. Imported by find_divergences_hi.py (section a5).
usage: python -I -X utf8 paren_scan6.py [--bak] [--all]
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hz6_common as C

PAR = re.compile(r"\(([^()]{6,})\)")


def scan():
    grp = collections.defaultdict(lambda: collections.defaultdict(list))
    for part in C.PARTS:
        for p, h in C.pairs(part):
            a = PAR.findall(C.norm(p, lab=False))
            b = PAR.findall(C.norm(h, lab=False))
            if a and len(a) == len(b):
                for x, y in zip(a, b):
                    k = re.sub(r"\s+", " ", x).strip().rstrip(".").lower()
                    grp[k][y.strip().rstrip("।")].append(C.short(part))
    return grp


def report(grp, show_all=False):
    out, n = [], 0
    for k, v in sorted(grp.items(), key=lambda kv: -sum(len(x) for x in kv[1].values())):
        if len(v) < 2 and not show_all:
            continue
        n += len(v) >= 2
        out.append(f"### ({k})")
        for h, locs in sorted(v.items(), key=lambda kv: -len(kv[1])):
            out.append(f"- [{len(locs)}] {','.join(sorted(set(locs)))} :: ({h})")
        out.append("")
    return out, n


if __name__ == "__main__":
    if "--bak" in sys.argv:
        C.CUR["hdir"] = C.BAK
    o, n = report(scan(), "--all" in sys.argv)
    print("\n".join(o)); print("groups", n)
