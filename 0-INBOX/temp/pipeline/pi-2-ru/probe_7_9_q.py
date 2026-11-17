# -*- coding: utf-8 -*-
"""Scratch: try F.q_line chunk by chunk on the Pañhāpucchaka lines of chapters 7-9, print unknown chunks. Writes nothing."""
import os, re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru")
import build_ch1_sample_ru as S
import build_1_ru as B
import build_2_3_ru as T
import build_4_5_ru as F

PE = "\x01"
for fn in ("7-satipatthanavibhango.md", "8-sammappadhanavibhango.md", "9-iddhipadavibhango.md"):
    pali = open(os.path.join(S.PALI_DIR, fn), encoding="utf-8").read().split("\n")
    on = False
    for l in pali:
        l = S.ID.sub("", l).rstrip()
        if l.startswith("##### Tikaṃ"):
            on = True
            continue
        if not on or not l or l.startswith("#"):
            continue
        for sent in re.split(r"(?<=\.) (?=[A-ZĀ])", l):
            body = sent.rstrip(".").replace("…pe…", PE)
            for x in re.split(r", |; |\x01 ?", body):
                if not x:
                    continue
                st = {"num": "pl" if "--pl" in sys.argv else None, "g": None}
                try:
                    r = F.chunk(x, st)
                    if "--all" in sys.argv:
                        print("ok ", x, "=>", r)
                except Exception as e:
                    print("ERR", fn[:2], repr(x), "|", str(e)[:80])
