# -*- coding: utf-8 -*-
"""Latin words outside variant brackets, double blank lines, CR, ':-', em dash, 'seed' words; per-line dash counts.
usage: python -I -X utf8 check_latin_3_14_15_hi.py <chapter.md> ...
"""
import os, re, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
HI = os.path.join(ROOT, r"AI_translation\hindi\pi-2-hindi-plain-zeroshot_split_chapters")
PA = os.path.join(ROOT, r"AI_translation\pali\pi-2_split_chapters")
bad = 0
for ch in sys.argv[1:]:
    raw = open(os.path.join(HI, ch), "rb").read()
    t = raw.decode("utf-8")
    errs = []
    if b"\r" in raw:
        errs.append("CR")
    if "\n\n\n" in t:
        errs.append("double blank line")
    for w in (":-", "—", "seed", "unseeded"):
        if w in t:
            errs.append(f"found {w!r}")
    for n, line in enumerate(t.splitlines(), 1):
        s = re.sub(r"\[[^\]]*\]", "", line)
        s = re.sub(r"\^[0-9A-Za-z-]+\s*$", "", s)
        lat = re.findall(r"[A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]{2,}", s)
        if lat:
            errs.append(f"line {n}: latin {lat[:5]}")
    P = [l for l in open(os.path.join(PA, ch), encoding="utf-8").read().splitlines() if l.strip()]
    H = [l for l in t.splitlines() if l.strip()]
    for k, (p, h) in enumerate(zip(P, H)):
        if p.count("–") + p.count("—") != h.count("–"):
            errs.append(f"dash mismatch at non-empty line {k + 1}")
    print(ch, "OK" if not errs else "ERRORS", errs[:20])
    bad += bool(errs)
sys.exit(1 if bad else 0)
