import re, os
ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-7_split_chapters")
HDIR = os.path.join(ROOT, r"AI_translation\hindi\pi-7-hindi-plain-rails_split_chapters")
EDIR = os.path.join(ROOT, r"AI_translation\english\pi-7-english-plain-zeroshot_split_chapters")
OUT = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-7-hi\review")
FILES = ["preamble.md", "1-00-paccaya.md", "1-01-kusalattika.md"]


def load(d, f):
    with open(os.path.join(d, f), encoding="utf-8") as fh:
        raw = fh.read()
    lines = raw.split("\n")
    ne = [(i + 1, l) for i, l in enumerate(lines) if l.strip()]
    return raw, lines, ne


def segments(ne):
    """list of (id, [(n, lineno, text)]) ; n is non-empty line number (1-based)"""
    segs = []
    cur = []
    for k, (ln, l) in enumerate(ne):
        cur.append((k + 1, ln, l))
        m = re.search(r"\^([\w-]+)\s*$", l)
        if m:
            segs.append((m.group(1), cur))
            cur = []
    if cur:
        segs.append((None, cur))
    return segs


def pairs(f):
    _, _, pn = load(PDIR, f)
    _, _, hn = load(HDIR, f)
    assert len(pn) == len(hn), (f, len(pn), len(hn))
    out = []
    cid = None
    # assign id to each line = id of segment it belongs to
    ps = segments(pn)
    ids = {}
    for sid, ls in ps:
        for n, ln, l in ls:
            ids[n] = sid
    for k in range(len(pn)):
        out.append((k + 1, ids.get(k + 1), pn[k][1], hn[k][1]))
    return out
