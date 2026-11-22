"""Shared helpers for the pi-6 Vietnamese harmonise pass (aligned Pāli/Vietnamese lines and segments).

Adapted from pi-5-vi-ai/vi_common.py (pi-5 files untouched).
pi-6 chapters: AI_translation/pali/pi-6_split_chapters <-> AI_translation/vietnamese/pi-6-vietnamese-plain-zeroshot_split_chapters
"""
import os, re, shutil, unicodedata

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-6_split_chapters")
VDIR = os.path.join(ROOT, r"AI_translation\vietnamese\pi-6-vietnamese-plain-zeroshot_split_chapters")
HERE = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-6-vi-ai")
BAK = os.path.join(HERE, "backup-pre-harmonise")
PARTS = ["preamble", "1-mulayamaka",
         "2-01-khandhayamaka", "2-02-khandhayamaka",
         "3-01-ayatanayamaka", "3-02-ayatanayamaka", "3-03-ayatanayamaka", "3-04-ayatanayamaka",
         "3-05-ayatanayamaka", "3-06-ayatanayamaka",
         "4-dhatuyamaka",
         "5-01-saccayamaka", "5-02-saccayamaka", "5-03-saccayamaka",
         "6-01-sankharayamaka", "6-02-sankharayamaka",
         "7-01-anusayayamaka", "7-02-anusayayamaka", "7-03-anusayayamaka", "7-04-anusayayamaka",
         "7-05-anusayayamaka", "7-06-anusayayamaka", "7-07-anusayayamaka", "7-08-anusayayamaka",
         "7-09-anusayayamaka", "7-10-anusayayamaka", "7-11-anusayayamaka",
         "8-cittayamaka",
         "9-01-dhammayamaka", "9-02-dhammayamaka", "9-03-dhammayamaka",
         "10-01-indriyayamaka", "10-02-indriyayamaka", "10-03-indriyayamaka", "10-04-indriyayamaka",
         "10-05-indriyayamaka", "10-06-indriyayamaka", "10-07-indriyayamaka", "10-08-indriyayamaka",
         "10-09-indriyayamaka", "10-10-indriyayamaka", "10-11-indriyayamaka", "10-12-indriyayamaka",
         "10-13-indriyayamaka"]
# the user-approved sample: never changed by the pass
PROTECTED_PARTS = {"preamble", "1-mulayamaka"}

ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
BID = re.compile(r"\s*\^[\w-]+\s*$")
VAR = re.compile(r"\s*\[[^\]]*\]")

CUR = {"vdir": VDIR}  # find_divergences_vi.py --bak points this at backup-pre-harmonise


def ensure_backup():
    """copy the 44 pre-pass files to backup-pre-harmonise/ ONCE (never overwritten afterwards)"""
    if os.path.isdir(BAK) and all(os.path.exists(os.path.join(BAK, p + ".md")) for p in PARTS):
        return False
    os.makedirs(BAK, exist_ok=True)
    for p in PARTS:
        dst = os.path.join(BAK, p + ".md")
        if not os.path.exists(dst):
            shutil.copyfile(os.path.join(VDIR, p + ".md"), dst)
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
    """strip ^id and variant brackets, collapse spaces, drop the space before punctuation and before «…»"""
    s = unicodedata.normalize("NFC", s)
    s = BID.sub("", s)
    s = VAR.sub("", s)
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"\s+([,.;:?!…])", r"\1", s)
    return s


def short(part):
    """'2-01-khandhayamaka' -> '2-01', '4-dhatuyamaka' -> '4', 'preamble' -> 'pre'"""
    if not part[0].isdigit():
        return part[:3]
    m = re.match(r"\d+(?:-\d+)?(?=-[a-z])", part)
    return m.group(0) if m else part
