"""Shared helpers for the pi-6 Hindi harmonise pass (aligned Pāli/Hindi lines and segments)."""
import os, re, glob

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-6_split_chapters")
HDIR = os.path.join(ROOT, r"AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters")
HERE = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-6-hi")
BAK = os.path.join(HERE, "backup-pre-harmonise")


def _key(n):
    a = n.split("-")
    return (int(a[0]), int(a[1]) if len(a) > 2 and a[1].isdigit() else 0)


PARTS = ["preamble"] + sorted([os.path.basename(p)[:-3] for p in glob.glob(os.path.join(PDIR, "*.md"))
                               if not p.endswith("preamble.md")], key=_key)
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
BID = re.compile(r"\s*\^[\w-]+\s*$")
VAR = re.compile(r"\s*\[[^\]]*\]")
LAB = re.compile(r"^\((Ka|Kha|Ga|Gha|Ṅa|Ca|क|ख|ग|घ|ङ|च)\)\s*")


def short(part):
    if part == "preamble":
        return "pre"
    a = part.split("-")
    return a[0] + ("." + a[1] if a[1].isdigit() else "")


def lines(path):
    return [l for l in open(path, encoding="utf-8-sig").read().splitlines() if l.strip()]


CUR = {"hdir": HDIR}


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


def norm(s, lab=True):
    s = BID.sub("", s)
    s = VAR.sub("", s)
    s = re.sub(r"\s+", " ", s).strip()
    if lab:
        s = LAB.sub("", s)
    return s
