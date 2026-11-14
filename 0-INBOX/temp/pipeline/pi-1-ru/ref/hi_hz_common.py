"""Shared helpers for the pi-1 Hindi harmonise pass (aligned Pāli/Hindi lines and segments)."""
import os, re

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-1_split_chapters")
HDIR = os.path.join(ROOT, r"AI_translation\hindi\pi-1-hindi-plain-zeroshot_split_chapters")
HERE = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-1-hi")
PARTS = ["preamble", "1-matika", "2-01-cittuppadakandam", "2-02-cittuppadakandam", "2-03-cittuppadakandam",
         "2-04-cittuppadakandam", "2-05-cittuppadakandam", "3-01-rupakandam", "3-02-rupakandam", "3-03-rupakandam",
         "4-01-nikkhepakandam", "4-02-nikkhepakandam", "4-03-nikkhepakandam", "5-atthakathakandam"]
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
BID = re.compile(r"\s*\^[\w-]+\s*$")
VAR = re.compile(r"\s*\[[^\]]*\]")


def lines(path):
    return [l for l in open(path, encoding="utf-8-sig").read().splitlines() if l.strip()]


CUR = {"hdir": HDIR}  # find_divergences_hi.py --bak points this at backup-pre-harmonise


def pairs(part, hdir=None):
    p = lines(os.path.join(PDIR, part + ".md"))
    h = lines(os.path.join(hdir or CUR["hdir"], part + ".md"))
    assert len(p) == len(h), (part, len(p), len(h))
    return list(zip(p, h))


def segments(part, hdir=None):
    out, bp, bh = [], [], []
    for p, h in pairs(part, hdir):
        bp.append(p); bh.append(h)
        m = ID.search(p)
        if m:
            out.append((m.group(1), bp, bh)); bp, bh = [], []
    return out


def norm(s):
    s = BID.sub("", s)
    s = VAR.sub("", s)
    return re.sub(r"\s+", " ", s).strip()
