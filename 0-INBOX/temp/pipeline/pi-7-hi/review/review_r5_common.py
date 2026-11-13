import re, sys, os
ROOT = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
PDIR = os.path.join(ROOT, "pali", "pi-7_split_chapters")
HDIR = os.path.join(ROOT, "hindi", "pi-7-hindi-plain-rails_split_chapters")
EDIR = os.path.join(ROOT, "english", "pi-7-english-plain-zeroshot_split_chapters")
FILES = ["3-01-hetugocchaka.md", "3-02-culantaraduka.md", "3-10-upadanagocchaka.md"]
IDRE = re.compile(r"\s\^([0-9A-Za-z-]+)\s*$")


def load(path):
    with open(path, encoding="utf-8") as f:
        return f.read().split("\n")


def segments(lines):
    """Return list of (id, [non-empty lines with (fileLineNo, nonEmptyIdx)])"""
    segs = []
    cur = []
    ne = 0
    for i, l in enumerate(lines, 1):
        if l.strip() == "":
            continue
        ne += 1
        cur.append((i, ne, l))
        m = IDRE.search(l)
        if m:
            segs.append((m.group(1), cur))
            cur = []
    if cur:
        segs.append((None, cur))
    return segs


def pairs(fn):
    P = load(os.path.join(PDIR, fn))
    H = load(os.path.join(HDIR, fn))
    return P, H
