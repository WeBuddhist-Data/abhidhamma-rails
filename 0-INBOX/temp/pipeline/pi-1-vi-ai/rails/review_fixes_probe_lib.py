"""Shared paths and aligned-line reader for the review-fix scripts."""
import os, re

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-1_split_chapters")
VDIR = os.path.join(ROOT, r"AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters")
HERE = os.path.dirname(os.path.abspath(__file__))
BAK = os.path.join(HERE, "backup-pre-review")
PARTS = ["preamble", "1-matika", "2-01-cittuppadakandam", "2-02-cittuppadakandam", "2-03-cittuppadakandam",
         "2-04-cittuppadakandam", "2-05-cittuppadakandam", "3-01-rupakandam", "3-02-rupakandam", "3-03-rupakandam",
         "4-01-nikkhepakandam", "4-02-nikkhepakandam", "4-03-nikkhepakandam", "5-atthakathakandam"]
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def aligned(part, vdir=VDIR):
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
