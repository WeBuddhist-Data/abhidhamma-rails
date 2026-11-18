"""Probe aligned Pāli / Vietnamese rails lines for the review fixes.

usage: python -I -X utf8 review_fixes_probe.py (p|v|id) <regex> [part-prefix] [--max N] [--bak]
  p  = regex on the Pāli line, v = regex on the Vietnamese line, id = regex on the segment ID (full match)
Prints part, non-empty line number, segment ID, Pāli, Vietnamese.
"""
import os, re, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-1_split_chapters")
VDIR = os.path.join(ROOT, r"AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters")
HERE = os.path.dirname(os.path.abspath(__file__))
BAK = os.path.join(HERE, "backup-pre-review")
PARTS = ["preamble", "1-matika", "2-01-cittuppadakandam", "2-02-cittuppadakandam", "2-03-cittuppadakandam",
         "2-04-cittuppadakandam", "2-05-cittuppadakandam", "3-01-rupakandam", "3-02-rupakandam", "3-03-rupakandam",
         "4-01-nikkhepakandam", "4-02-nikkhepakandam", "4-03-nikkhepakandam", "5-atthakathakandam"]
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def aligned(part, vdir):
    pl = [l for l in open(os.path.join(PDIR, part + ".md"), encoding="utf-8-sig").read().splitlines() if l.strip()]
    vl = [l for l in open(os.path.join(vdir, part + ".md"), encoding="utf-8-sig").read().splitlines() if l.strip()]
    assert len(pl) == len(vl), (part, len(pl), len(vl))
    sid, cur = {}, []
    for k, p in enumerate(pl):
        cur.append(k)
        m = ID.search(p)
        if m:
            for kk in cur:
                sid[kk] = m.group(1)
            cur = []
    return pl, vl, sid


def main():
    a = sys.argv[1:]
    mx = 60
    if "--max" in a:
        i = a.index("--max"); mx = int(a[i + 1]); del a[i:i + 2]
    vdir = VDIR
    if "--bak" in a:
        a.remove("--bak"); vdir = BAK
    mode, rx = a[0], re.compile(a[1])
    pref = a[2] if len(a) > 2 else ""
    n = 0
    for part in PARTS:
        if pref and not part.startswith(pref):
            continue
        pl, vl, sid = aligned(part, vdir)
        for k, (p, v) in enumerate(zip(pl, vl)):
            s = sid.get(k, "?")
            ok = (mode == "p" and rx.search(p)) or (mode == "v" and rx.search(v)) or (mode == "id" and rx.fullmatch(s))
            if ok:
                n += 1
                if n <= mx:
                    print(f"[{part[:4]} L{k + 1} ^{s}]\n  P: {p}\n  V: {v}")
    print("matches:", n)


main()
