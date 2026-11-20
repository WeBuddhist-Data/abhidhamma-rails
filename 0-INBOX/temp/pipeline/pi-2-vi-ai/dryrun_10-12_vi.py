# -*- coding: utf-8 -*-
"""Scratch: run build_10-12_vi.build() without writing; print slips, or the Vietnamese lines whose Pāli matches
argv[1] (regex) for chapter argv[2] (10/11/12).
usage: python -I -X utf8 dryrun_10-12_vi.py [pali-rx chapter]"""
import importlib
import os
import re
import sys

HERE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-vi-ai"
sys.path.insert(0, HERE)
M = importlib.import_module("build_10-12_vi")
res, n = M.build()
print("ok", n)
if len(sys.argv) > 2:
    fn = [k for k in res if os.path.basename(k).startswith(sys.argv[2] + "-")][0]
    pali = open(os.path.join(M.S.PALI_DIR, os.path.basename(fn)), encoding="utf-8").read().rstrip("\n").split("\n")
    for p, v in zip(pali, res[fn]):
        if re.search(sys.argv[1], p):
            print("P:", p)
            print("V:", v)
            print()
else:
    for s in sorted(set(M.SLIPS)):
        print("slip:", s)
