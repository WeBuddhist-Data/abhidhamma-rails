"""Shared helpers for the pi-5 Vietnamese harmonise pass (aligned Pāli/Vietnamese lines and segments).

Adapted from pi-4-vi-ai/vi_common.py (pi-4 files untouched).
pi-5 chapters: AI_translation/pali/pi-5_split_chapters <-> AI_translation/vietnamese/pi-5-vietnamese-plain-zeroshot_split_chapters
"""
import os, re, shutil, unicodedata

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-5_split_chapters")
VDIR = os.path.join(ROOT, r"AI_translation\vietnamese\pi-5-vietnamese-plain-zeroshot_split_chapters")
HERE = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-5-vi-ai")
BAK = os.path.join(HERE, "backup-pre-harmonise")
PARTS = ["preamble", "1-puggalakatha", "2-parihanikatha", "3-brahmacariyakatha", "4-jahatikatha",
         "5-sabbamatthitikatha", "6-atitakkhandhadikatha", "7-ekaccam-atthitikatha", "8-satipatthanakatha",
         "9-hevatthikatha", "10-dutiyavaggo", "11-tatiyavaggo", "12-catutthavaggo", "13-pancamavaggo",
         "14-chatthavaggo", "15-sattamavaggo", "16-atthamavaggo", "17-navamavaggo", "18-dasamavaggo",
         "19-ekadasamavaggo", "20-dvadasamavaggo", "21-terasamavaggo", "22-cuddasamavaggo",
         "23-pannarasamavaggo", "24-solasamavaggo", "25-sattarasamavaggo", "26-attharasamavaggo",
         "27-ekunavisatimavaggo", "28-visatimavaggo", "29-ekavisatimavaggo", "30-bavisatimavaggo",
         "31-tevisatimavaggo"]
# the user-approved sample: changed only where harmonise-brief.md names it (none named)
PROTECTED_PARTS = {"preamble", "1-puggalakatha"}

ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
BID = re.compile(r"\s*\^[\w-]+\s*$")
VAR = re.compile(r"\s*\[[^\]]*\]")

CUR = {"vdir": VDIR}  # find_divergences_vi.py --bak points this at backup-pre-harmonise


def ensure_backup():
    """copy the 32 pre-pass chapter files to backup-pre-harmonise/ ONCE (never overwritten afterwards)"""
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
    return part.split("-")[0] if part[0].isdigit() else part[:3]
