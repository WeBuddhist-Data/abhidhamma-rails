"""Shared paths and aligned-line readers for the pi-2 Vietnamese review-fix scripts (rails output)."""
import os, re

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-2_split_chapters")
VDIR = os.path.join(ROOT, r"AI_translation\vietnamese\pi-2-vietnamese-plain-rails_split_chapters")
HERE = os.path.dirname(os.path.abspath(__file__))
BAK = os.path.join(HERE, "backup-pre-review")
PARTS = ["preamble", "1-khandhavibhango", "2-ayatanavibhango", "3-dhatuvibhango", "4-saccavibhango",
         "5-indriyavibhango", "6-paticcasamuppadavibhango", "7-satipatthanavibhango", "8-sammappadhanavibhango",
         "9-iddhipadavibhango", "10-bojjhangavibhango", "11-maggangavibhango", "12-jhanavibhango",
         "13-appamannavibhango", "14-sikkhapadavibhango", "15-patisambhidavibhango", "16-nanavibhango",
         "17-khuddakavatthuvibhango", "18-dhammahadayavibhango"]
P1_PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-1_split_chapters")
P1_VDIR = os.path.join(ROOT, r"AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters")
P1_PARTS = ["preamble", "1-matika", "2-01-cittuppadakandam", "2-02-cittuppadakandam", "2-03-cittuppadakandam",
            "2-04-cittuppadakandam", "2-05-cittuppadakandam", "3-01-rupakandam", "3-02-rupakandam", "3-03-rupakandam",
            "4-01-nikkhepakandam", "4-02-nikkhepakandam", "4-03-nikkhepakandam", "5-atthakathakandam"]
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def nonempty(path):
    return [l for l in open(path, encoding="utf-8-sig").read().splitlines() if l.strip()]


def aligned(part, vdir=VDIR, pdir=PDIR):
    pl = nonempty(os.path.join(pdir, part + ".md"))
    vl = nonempty(os.path.join(vdir, part + ".md"))
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
