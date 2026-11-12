"""Shared helpers for the pi-2 Hindi harmonise pass (aligned Pāli/Hindi lines and segments)."""
import os, re

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-2_split_chapters")
HDIR = os.path.join(ROOT, r"AI_translation\hindi\pi-2-hindi-plain-zeroshot_split_chapters")
HERE = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-2-hi")
PI1 = os.path.join(ROOT, r"AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters")
PARTS = ["preamble", "1-khandhavibhango", "2-ayatanavibhango", "3-dhatuvibhango", "4-saccavibhango",
         "5-indriyavibhango", "6-paticcasamuppadavibhango", "7-satipatthanavibhango", "8-sammappadhanavibhango",
         "9-iddhipadavibhango", "10-bojjhangavibhango", "11-maggangavibhango", "12-jhanavibhango",
         "13-appamannavibhango", "14-sikkhapadavibhango", "15-patisambhidavibhango", "16-nanavibhango",
         "17-khuddakavatthuvibhango", "18-dhammahadayavibhango"]
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
BID = re.compile(r"\s*\^[\w-]+\s*$")
VAR = re.compile(r"\s*\[[^\]]*\]")


def short(part):
    return "pre" if part == "preamble" else "ch" + part.split("-")[0]


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
