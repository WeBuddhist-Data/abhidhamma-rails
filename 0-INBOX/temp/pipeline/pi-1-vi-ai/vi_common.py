"""Shared helpers for the pi-1 Vietnamese harmonise pass (aligned Pāli/Vietnamese lines and segments)."""
import os, re

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-1_split_chapters")
VDIR = os.path.join(ROOT, r"AI_translation\vietnamese\pi-1-vietnamese-plain-zeroshot_split_chapters")
HERE = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-1-vi-ai")
BAK = os.path.join(HERE, "backup-pre-harmonise")
PARTS = ["preamble", "1-matika", "2-01-cittuppadakandam", "2-02-cittuppadakandam", "2-03-cittuppadakandam",
         "2-04-cittuppadakandam", "2-05-cittuppadakandam", "3-01-rupakandam", "3-02-rupakandam", "3-03-rupakandam",
         "4-01-nikkhepakandam", "4-02-nikkhepakandam", "4-03-nikkhepakandam", "5-atthakathakandam"]
PROTECTED_PARTS = {"preamble", "1-matika"}
PROTECTED_2_01 = 122  # first 122 non-empty lines of 2-01 (approved sample; brief wording)
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
BID = re.compile(r"\s*\^[\w-]+\s*$")
VAR = re.compile(r"\s*\[[^\]]*\]")

CUR = {"vdir": VDIR}  # find_divergences_vi.py --bak points this at backup-pre-harmonise


def ensure_backup():
    """copy the pre-pass part files to backup-pre-harmonise/ ONCE (never overwritten afterwards)"""
    if os.path.isdir(BAK) and all(os.path.exists(os.path.join(BAK, p + ".md")) for p in PARTS):
        return False
    os.makedirs(BAK, exist_ok=True)
    for p in PARTS:
        dst = os.path.join(BAK, p + ".md")
        if not os.path.exists(dst):
            data = open(os.path.join(VDIR, p + ".md"), "rb").read()
            open(dst, "wb").write(data)
    return True


def lines(path):
    return [l for l in open(path, encoding="utf-8-sig").read().splitlines() if l.strip()]


def pairs(part, vdir=None):
    p = lines(os.path.join(PDIR, part + ".md"))
    v = lines(os.path.join(vdir or CUR["vdir"], part + ".md"))
    assert len(p) == len(v), (part, len(p), len(v))
    return list(zip(p, v))


def segments(part, vdir=None):
    out, bp, bv = [], [], []
    for p, v in pairs(part, vdir):
        bp.append(p); bv.append(v)
        m = ID.search(p)
        if m:
            out.append((m.group(1), bp, bv)); bp, bv = [], []
    return out


def norm(s):
    s = BID.sub("", s)
    s = VAR.sub("", s)
    return re.sub(r"\s+", " ", s).strip()


def short(part):
    return part[:4] if part[0].isdigit() and part[1] == "-" else part[:3]
