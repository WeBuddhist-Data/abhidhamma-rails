import os, re, sys
ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-6_split_chapters")
VDIR = os.path.join(ROOT, r"AI_translation\vietnamese\pi-6-vietnamese-plain-rails_split_chapters")
FILES = ["7-09-anusayayamaka.md", "7-10-anusayayamaka.md", "7-11-anusayayamaka.md",
         "8-cittayamaka.md", "9-01-dhammayamaka.md", "9-02-dhammayamaka.md",
         "9-03-dhammayamaka.md", "10-01-indriyayamaka.md", "10-02-indriyayamaka.md"]
IDRE = re.compile(r"\^([0-9a-z-]+)\s*$")


def load(d, f):
    import unicodedata
    with open(os.path.join(d, f), encoding="utf-8") as fh:
        return unicodedata.normalize("NFC", fh.read()).split("\n")


def pairs(files=None):
    """yield (file, lineno, segid, pali, viet) for non-empty aligned lines."""
    for f in files or FILES:
        P = load(PDIR, f)
        V = load(VDIR, f)
        if len(P) != len(V):
            print("LINECOUNT MISMATCH", f, len(P), len(V))
        # segment id: the id at the end of the block (look forward)
        ids = [None] * len(P)
        cur = None
        for i in range(len(P) - 1, -1, -1):
            m = IDRE.search(P[i])
            if m:
                cur = m.group(1)
            if P[i].strip() == "":
                pass
            ids[i] = cur
        # better: id is the next id at or after line within same block
        nxt = None
        for i in range(len(P) - 1, -1, -1):
            if P[i].strip() == "":
                nxt = None
                continue
            m = IDRE.search(P[i])
            if m:
                nxt = m.group(1)
            ids[i] = nxt
        for i, (p, v) in enumerate(zip(P, V)):
            if p.strip() == "" and v.strip() == "":
                continue
            if (p.strip() == "") != (v.strip() == ""):
                print("BLANK MISMATCH", f, i + 1)
            yield f, i + 1, ids[i], p, v
