import re, os, sys
ROOT = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
PDIR = os.path.join(ROOT, "pali", "pi-7_split_chapters")
HDIR = os.path.join(ROOT, "hindi", "pi-7-hindi-plain-rails_split_chapters")
FILES = ["3-03-asavagocchaka.md", "3-04-sannojanagocchaka.md", "3-05-ganthagocchaka.md",
         "3-06-oghayogagocchaka.md", "3-07-nivaranagocchaka.md", "3-08-paramasagocchaka.md"]
IDRE = re.compile(r"\^([0-9][0-9A-Za-z-]*)\s*$")


def raw(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def nonempty(path):
    """list of (physical_line_no, nonempty_idx, text)"""
    out = []
    k = 0
    for i, l in enumerate(raw(path).split("\n"), 1):
        if l.strip():
            k += 1
            out.append((i, k, l.rstrip("\r")))
    return out


def pairs(f):
    """aligned list of dicts: id (segment block id), k, pl, hl, p, h"""
    P = nonempty(os.path.join(PDIR, f))
    H = nonempty(os.path.join(HDIR, f))
    if len(P) != len(H):
        print("LINECOUNT MISMATCH", f, len(P), len(H))
    res = []
    # assign segment id: id of the line itself or next id-bearing line
    ids = [None] * len(P)
    cur = None
    for j in range(len(P) - 1, -1, -1):
        m = IDRE.search(P[j][2])
        if m:
            cur = m.group(1)
        ids[j] = cur
    for j in range(min(len(P), len(H))):
        res.append(dict(id=ids[j], k=P[j][1], pl=P[j][0], hl=H[j][0], p=P[j][2], h=H[j][2]))
    return res
