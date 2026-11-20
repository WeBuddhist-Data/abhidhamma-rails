"""Shared helpers for the pi-2 Vietnamese harmonise pass (aligned Pāli/Vietnamese lines and segments).

pi-2 parts: AI_translation/pali/pi-2_split_chapters <-> AI_translation/vietnamese/pi-2-vietnamese-plain-zeroshot_split_chapters
pi-1 (final, reviewed): AI_translation/pali/pi-1_split_chapters <-> AI_translation/vietnamese/pi-1-vietnamese-plain-rails_split_chapters
"""
import os, re, unicodedata

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-2_split_chapters")
VDIR = os.path.join(ROOT, r"AI_translation\vietnamese\pi-2-vietnamese-plain-zeroshot_split_chapters")
HERE = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-2-vi-ai")
BAK = os.path.join(HERE, "backup-pre-harmonise")
PARTS = ["preamble", "1-khandhavibhango", "2-ayatanavibhango", "3-dhatuvibhango", "4-saccavibhango",
         "5-indriyavibhango", "6-paticcasamuppadavibhango", "7-satipatthanavibhango", "8-sammappadhanavibhango",
         "9-iddhipadavibhango", "10-bojjhangavibhango", "11-maggangavibhango", "12-jhanavibhango",
         "13-appamannavibhango", "14-sikkhapadavibhango", "15-patisambhidavibhango", "16-nanavibhango",
         "17-khuddakavatthuvibhango", "18-dhammahadayavibhango"]
PROTECTED_PARTS = {"preamble"}
PROTECTED_1 = 77  # first 77 non-empty lines of 1-khandhavibhango (approved sample = ch1-sample.md)

P1_PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-1_split_chapters")
P1_VDIR = os.path.join(ROOT, r"AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters")
P1_PARTS = ["preamble", "1-matika", "2-01-cittuppadakandam", "2-02-cittuppadakandam", "2-03-cittuppadakandam",
            "2-04-cittuppadakandam", "2-05-cittuppadakandam", "3-01-rupakandam", "3-02-rupakandam", "3-03-rupakandam",
            "4-01-nikkhepakandam", "4-02-nikkhepakandam", "4-03-nikkhepakandam", "5-atthakathakandam"]

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


def pairs1(part):
    p = lines(os.path.join(P1_PDIR, part + ".md"))
    v = lines(os.path.join(P1_VDIR, part + ".md"))
    assert len(p) == len(v), (part, len(p), len(v))
    return list(zip(p, v))


def _segs(pv):
    out, bp, bv = [], [], []
    for p, v in pv:
        bp.append(p); bv.append(v)
        m = ID.search(p)
        if m:
            out.append((m.group(1), bp, bv)); bp, bv = [], []
    return out


def segments(part, vdir=None):
    return _segs(pairs(part, vdir))


def segments1(part):
    return _segs(pairs1(part))


def norm(s):
    """strip ^id and variant brackets, collapse spaces, drop the space before punctuation"""
    s = unicodedata.normalize("NFC", s)
    s = BID.sub("", s)
    s = VAR.sub("", s)
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"\s+([,.;:?!])", r"\1", s)
    return s


def short(part):
    return part.split("-")[0] if part[0].isdigit() else part[:3]
