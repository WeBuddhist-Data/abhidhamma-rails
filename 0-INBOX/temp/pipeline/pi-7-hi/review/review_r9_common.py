import os, re, sys
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails'
PDIR = os.path.join(ROOT, r'AI_translation\pali\pi-7_split_chapters')
HDIR = os.path.join(ROOT, r'AI_translation\hindi\pi-7-hindi-plain-rails_split_chapters')
EDIR = os.path.join(ROOT, r'AI_translation\english\pi-7-english-plain-zeroshot_split_chapters')
FILES = sorted(f for f in os.listdir(PDIR) if f.startswith('4-') and '4-02' <= f[:4] <= '4-15')

IDRE = re.compile(r'\s\^([0-9A-Za-z-]+)\s*$')


def load(path):
    with open(path, encoding='utf-8') as fh:
        return fh.read()


def lines_nonempty(text):
    """return list of (nonempty_index (1-based), raw_line_no, text)"""
    out = []
    n = 0
    for i, l in enumerate(text.split('\n'), 1):
        if l.strip():
            n += 1
            out.append((n, i, l))
    return out


def segments(text):
    """list of (id, [(ne_no, line_no, text_without_id), ...])"""
    segs = []
    cur = []
    for ne, ln, l in lines_nonempty(text):
        m = IDRE.search(l)
        if m:
            cur.append((ne, ln, l[:m.start()]))
            segs.append((m.group(1), cur))
            cur = []
        else:
            cur.append((ne, ln, l))
    if cur:
        segs.append((None, cur))
    return segs


def pairs():
    """yield (file, id, ne_no, pali_line, hindi_line) for aligned lines"""
    for f in FILES:
        P = lines_nonempty(load(os.path.join(PDIR, f)))
        H = lines_nonempty(load(os.path.join(HDIR, f)))
        if len(P) != len(H):
            print('LINECOUNT MISMATCH', f, len(P), len(H))
        # get id per line: id of the segment it ends in
        ids = []
        pend = []
        for ne, ln, l in P:
            pend.append(ne)
            m = IDRE.search(l)
            if m:
                ids.extend([m.group(1)] * len(pend))
                pend = []
        ids.extend([None] * len(pend))
        for (ne, ln, pl), (_, hln, hl), sid in zip(P, H, ids):
            pm = IDRE.search(pl)
            hm = IDRE.search(hl)
            yield f, sid, ne, (pl[:pm.start()] if pm else pl), (hl[:hm.start()] if hm else hl), (pm.group(1) if pm else None), (hm.group(1) if hm else None)
