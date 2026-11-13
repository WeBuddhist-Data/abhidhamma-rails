"""Shared helpers for the pi-7 Hindi harmonise pass (aligned Pāli/Hindi non-empty lines)."""
import os, re, glob

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-7_split_chapters")
HDIR = os.path.join(ROOT, r"AI_translation\hindi\pi-7-hindi-plain-zeroshot_split_chapters")
HERE = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-7-hi")
BAK = os.path.join(HERE, "backup-pre-harmonise")


def _key(n):
    a = n.split("-")
    return (int(a[0]), int(a[1]))


PARTS = ["preamble"] + sorted([os.path.basename(p)[:-3] for p in glob.glob(os.path.join(PDIR, "*.md"))
                               if not p.endswith("preamble.md")], key=_key)
BID = re.compile(r"\s*\^[\w-]+\s*$")
VAR = re.compile(r"\s*\{[^}]*\}")
HVAR = re.compile(r"\s*\[[^\]]*\]")
CNT = re.compile(r"\s*\((\d+|\d+\.)\)\s*")


def short(part):
    return "pre" if part == "preamble" else part[:4]


def lines(path):
    return [l for l in open(path, encoding="utf-8-sig").read().splitlines() if l.strip()]


CUR = {"hdir": HDIR}


def pairs(part, hdir=None):
    p = lines(os.path.join(PDIR, part + ".md"))
    h = lines(os.path.join(hdir or CUR["hdir"], part + ".md"))
    assert len(p) == len(h), (part, len(p), len(h))
    return list(zip(p, h))


def pnorm(s):
    """Pāli key: strip ^id, {…} variants, count markers like "(3)", collapse spaces"""
    s = BID.sub("", s)
    s = VAR.sub("", s)
    s = CNT.sub(" ", s)
    return re.sub(r"\s+", " ", s).strip()


def hnorm(s):
    s = BID.sub("", s)
    s = HVAR.sub("", s)
    s = CNT.sub(" ", s)
    return re.sub(r"\s+", " ", s).strip()
