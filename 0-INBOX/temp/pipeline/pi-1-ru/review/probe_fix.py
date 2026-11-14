"""Exploration helper for the review fixes: grep the Russian rails chapters (or the backup) and print aligned Pāli.

usage: python -I -X utf8 probe_fix.py <ru_regex> [--pali <pali_regex>] [--bak] [--nop] [--max N] [--part PREFIX]
"""
import os, re, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-1_split_chapters")
RDIR = os.path.join(ROOT, r"AI_translation\russian\pi-1-russian-plain-rails_split_chapters")
BAK = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-1-ru\review\backup-pre-fixes")
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
PARTS = ["preamble", "1-matika", "2-01-cittuppadakandam", "2-02-cittuppadakandam", "2-03-cittuppadakandam",
         "2-04-cittuppadakandam", "2-05-cittuppadakandam", "3-01-rupakandam", "3-02-rupakandam", "3-03-rupakandam",
         "4-01-nikkhepakandam", "4-02-nikkhepakandam", "4-03-nikkhepakandam", "5-atthakathakandam"]

args = sys.argv[1:]
rdir = BAK if "--bak" in args else RDIR
nop = "--nop" in args
mx = int(args[args.index("--max") + 1]) if "--max" in args else 10 ** 9
pp = re.compile(args[args.index("--pali") + 1]) if "--pali" in args else None
prt = args[args.index("--part") + 1] if "--part" in args else ""
rr = re.compile(args[0])
n = 0
for part in PARTS:
    if not part.startswith(prt):
        continue
    pl = [l for l in open(os.path.join(PDIR, part + ".md"), encoding="utf-8-sig").read().splitlines() if l.strip()]
    rl = [l for l in open(os.path.join(rdir, part + ".md"), encoding="utf-8").read().splitlines() if l.strip()]
    sids, cur = [None] * len(pl), []
    for k, l in enumerate(pl):
        cur.append(k)
        m = ID.search(l)
        if m:
            for kk in cur:
                sids[kk] = m.group(1)
            cur = []
    for k, (p, r) in enumerate(zip(pl, rl)):
        if rr.search(r) and (pp is None or pp.search(p)):
            n += 1
            if n <= mx:
                print(f"== {part[:4]} ^{sids[k]} L{k + 1}")
                if not nop:
                    print("P:", p)
                print("R:", r)
print("matches:", n)
