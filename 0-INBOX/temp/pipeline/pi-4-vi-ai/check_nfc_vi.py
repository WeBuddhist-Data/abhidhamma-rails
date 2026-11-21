"""Check the 12 pi-4 Vietnamese zero-shot files: NFC, no CR, no BOM, no double blank lines.

usage: python -I -X utf8 check_nfc_vi.py
"""
import os, sys, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vi_common import PARTS, VDIR

bad = 0
for p in PARTS:
    raw = open(os.path.join(VDIR, p + ".md"), "rb").read()
    t = raw.decode("utf-8")
    probs = []
    if t != unicodedata.normalize("NFC", t):
        probs.append("not NFC")
    if "\r" in t:
        probs.append("CR")
    if t.startswith("﻿"):
        probs.append("BOM")
    if "\n\n\n" in t:
        probs.append("double blank line")
    bad += bool(probs)
    print(p, "OK" if not probs else probs)
print("files with problems:", bad)
