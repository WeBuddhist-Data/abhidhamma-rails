"""Inspection helper (read only): rails lines whose Burmese has more quote marks than the Pāli (outside brackets)."""
import pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PALI = ROOT / "AI_translation/pali/pi-5_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-5-burmese-plain-rails_split_chapters"
N = lambda s: unicodedata.normalize("NFC", s)
q = lambda s: sum(re.sub(r"\[[^\]]*\]", "", s).count(c) for c in "\"“”‘’'")
for p in sorted(PALI.glob("*.md")):
    pl = N(p.read_text(encoding="utf-8-sig")).split("\n")
    ml = N((OUT / p.name).read_text(encoding="utf-8")).split("\n")
    for k, (a, b) in enumerate(zip(pl, ml)):
        if q(b) > q(a):
            print(f"{p.name[:-3]}:{k+1}\tP{q(a)} B{q(b)}\t{a[:90]}\t|\t{b[:140]}")
