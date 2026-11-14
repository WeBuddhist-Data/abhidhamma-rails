"""Shared helpers for the pi-1 Russian harmonise pass (aligned Pāli/Russian lines and segments)."""
import os, re

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-1_split_chapters")
RDIR = os.path.join(ROOT, r"AI_translation\russian\pi-1-russian-plain-zeroshot_split_chapters")
HERE = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-1-ru")
BAK = os.path.join(HERE, "backup-pre-harmonise")
PARTS = ["preamble", "1-matika", "2-01-cittuppadakandam", "2-02-cittuppadakandam", "2-03-cittuppadakandam",
         "2-04-cittuppadakandam", "2-05-cittuppadakandam", "3-01-rupakandam", "3-02-rupakandam", "3-03-rupakandam",
         "4-01-nikkhepakandam", "4-02-nikkhepakandam", "4-03-nikkhepakandam", "5-atthakathakandam"]
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
BID = re.compile(r"\s*\^[\w-]+\s*$")
VAR = re.compile(r"\s*\[[^\]]*\]")

CUR = {"rdir": RDIR}  # find_divergences_ru.py --bak points this at backup-pre-harmonise


def lines(path):
    return [l for l in open(path, encoding="utf-8-sig").read().splitlines() if l.strip()]


def pairs(part, rdir=None):
    p = lines(os.path.join(PDIR, part + ".md"))
    r = lines(os.path.join(rdir or CUR["rdir"], part + ".md"))
    assert len(p) == len(r), (part, len(p), len(r))
    return list(zip(p, r))


def segments(part, rdir=None):
    out, bp, br = [], [], []
    for p, r in pairs(part, rdir):
        bp.append(p); br.append(r)
        m = ID.search(p)
        if m:
            out.append((m.group(1), bp, br)); bp, br = [], []
    return out


def norm(s):
    s = BID.sub("", s)
    s = VAR.sub("", s)
    return re.sub(r"\s+", " ", s).strip()


def short(part):
    return part[:4] if part[0].isdigit() and part[1] == "-" else part[:3]
