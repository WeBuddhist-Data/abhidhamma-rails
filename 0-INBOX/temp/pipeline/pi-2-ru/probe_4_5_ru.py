# -*- coding: utf-8 -*-
"""Scratch probe for build_4_5_ru.py: print pi-1 Russian by block ID or by Russian/Pāli regex.
usage: python -I -X utf8 probe_4_5_ru.py id ^1-277 | ru "regex" [n] | pi "regex" [n]
"""
import os, re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru")
import build_2_3_ru as T  # noqa: E402

mode = sys.argv[1]
if mode == "id":
    for b in sys.argv[2:]:
        print(b, "::", T.PI1.get(b))
elif mode == "ru":
    pat = re.compile(sys.argv[2])
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    for k, v in T.PI1.items():
        for m in pat.finditer(v):
            print(k, "::", v[max(0, m.start() - 200):m.end() + 300])
            n -= 1
            break
        if n <= 0:
            break
