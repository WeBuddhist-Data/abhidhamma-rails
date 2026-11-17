"""Shared helpers for the pi-2 Russian harmonise pass (aligned Pāli/Russian lines and segments)."""
import os, re

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-2_split_chapters")
RDIR = os.path.join(ROOT, r"AI_translation\russian\pi-2-russian-plain-zeroshot_split_chapters")
HERE = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-2-ru")
BAK = os.path.join(HERE, "backup-pre-harmonise")
# pi-1 (final, reviewed Russian)
P1DIR = os.path.join(ROOT, r"AI_translation\pali\pi-1_split_chapters")
R1DIR = os.path.join(ROOT, r"AI_translation\russian\pi-1-russian-plain-rails_split_chapters")
PARTS1 = ["preamble", "1-matika", "2-01-cittuppadakandam", "2-02-cittuppadakandam", "2-03-cittuppadakandam",
          "2-04-cittuppadakandam", "2-05-cittuppadakandam", "3-01-rupakandam", "3-02-rupakandam", "3-03-rupakandam",
          "4-01-nikkhepakandam", "4-02-nikkhepakandam", "4-03-nikkhepakandam", "5-atthakathakandam"]

PARTS = ["preamble", "1-khandhavibhango", "2-ayatanavibhango", "3-dhatuvibhango", "4-saccavibhango",
         "5-indriyavibhango", "6-paticcasamuppadavibhango", "7-satipatthanavibhango", "8-sammappadhanavibhango",
         "9-iddhipadavibhango", "10-bojjhangavibhango", "11-maggangavibhango", "12-jhanavibhango",
         "13-appamannavibhango", "14-sikkhapadavibhango", "15-patisambhidavibhango", "16-nanavibhango",
         "17-khuddakavatthuvibhango", "18-dhammahadayavibhango"]
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
BID = re.compile(r"\s*\^[\w-]+\s*$")
VAR = re.compile(r"\s*\[[^\]]*\]")

CUR = {"rdir": RDIR}  # find_divergences_ru.py --bak points this at backup-pre-harmonise


def lines(path):
    return [l for l in open(path, encoding="utf-8-sig").read().splitlines() if l.strip()]


def pairs(part, rdir=None, pdir=None):
    p = lines(os.path.join(pdir or PDIR, part + ".md"))
    r = lines(os.path.join(rdir or CUR["rdir"], part + ".md"))
    assert len(p) == len(r), (part, len(p), len(r))
    return list(zip(p, r))


def segments(part, rdir=None, pdir=None):
    out, bp, br = [], [], []
    for p, r in pairs(part, rdir, pdir):
        bp.append(p); br.append(r)
        m = ID.search(p)
        if m:
            out.append((m.group(1), bp, br)); bp, br = [], []
    return out


def segments1(part):
    """pi-1 (reviewed rails Russian)"""
    return segments(part, R1DIR, P1DIR)


def norm(s):
    """strip ^id and variant brackets, collapse spaces, drop the space before punctuation"""
    s = BID.sub("", s)
    s = VAR.sub("", s)
    s = re.sub(r"\s+", " ", s).strip()
    return re.sub(r"\s+([,.;:?!])", r"\1", s)


def short(part):
    return "ch" + part.split("-")[0] if part[0].isdigit() else part[:3]
