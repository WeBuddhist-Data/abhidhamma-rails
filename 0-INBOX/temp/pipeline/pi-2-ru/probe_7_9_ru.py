# -*- coding: utf-8 -*-
"""Scratch probe for chapters 7-9: print strings from earlier builders and pi-1 lines. Writes nothing."""
import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru")
import build_ch1_sample_ru as S
import build_1_ru as B
import build_2_3_ru as T
import build_4_5_ru as F
import build_6_ru as G

for a in sys.argv[1:]:
    if a.startswith("^"):
        print(a, T.PI1.get(a))
    else:
        print(a, "=", repr(eval(a)))
