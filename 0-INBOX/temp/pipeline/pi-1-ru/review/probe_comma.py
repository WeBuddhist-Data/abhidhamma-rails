"""Exploration helper: list every «X, – это» answer X (text after the last «? » / «. » / «; » / «: » / line start).

usage: python -I -X utf8 probe_comma.py [--all] [--bak]
Without --all, answers containing a relative / participial / «кроме» marker are skipped.
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
MARK = re.compile(r"котор|(?<![А-Яа-яЁё])что(?![А-Яа-яЁё])|кроме|какая бы|будь|(?<![А-Яа-яЁё])это(?![А-Яа-яЁё])|\]")
rdir = BAK if "--bak" in sys.argv else RDIR
allm = "--all" in sys.argv
for part in PARTS:
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
    for k, r in enumerate(rl):
        for m in re.finditer(r", – это", r):
            pre = r[:m.start()]
            cut = max(pre.rfind("? "), pre.rfind(". "), pre.rfind("; "))
            ans = pre[cut + 2:] if cut >= 0 else pre
            if not allm and MARK.search(ans):
                continue
            print(f"{part[:4]}\t^{sids[k]}\tL{k + 1}\t{ans[:220]}")
