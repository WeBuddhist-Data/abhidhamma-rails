# -*- coding: utf-8 -*-
"""Scratch probe for chapters 10-12: imports the earlier builders (nothing is written) and evaluates the Python
code given as argv[1] with S, B, T, F, G, H (build_7-9) in scope; or, with --pi1 <pali-rx> [maxhits] [width],
prints pi-1 Pāli lines matching the regex with the aligned pi-1 Vietnamese line.
usage: python -I -X utf8 probe_10-12_vi.py "<code>"
       python -I -X utf8 probe_10-12_vi.py --pi1 <pali-rx> [maxhits] [width]"""
import importlib
import os
import re
import sys

HERE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-vi-ai"
sys.path.insert(0, HERE)


def pi1(rx, mx=6, w=900):
    import build_ch1_sample_vi as S
    P = os.path.join(S.ROOT, r"AI_translation\pali\pi-1_split_chapters")
    n = 0
    for fn in sorted(os.listdir(P)):
        if not fn.endswith(".md"):
            continue
        pl = [l for l in open(os.path.join(P, fn), encoding="utf-8").read().split("\n") if l.strip()]
        vl = [l for l in open(os.path.join(S.PI1_VI_DIR, fn), encoding="utf-8").read().split("\n") if l.strip()]
        for a, b in zip(pl, vl):
            if re.search(rx, a):
                print("==", fn)
                print("P:", a[:w])
                print("V:", b[:w])
                n += 1
                if n >= mx:
                    return


def main():
    if sys.argv[1] == "--pi1":
        pi1(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 6, int(sys.argv[4]) if len(sys.argv) > 4 else 900)
        return
    import build_ch1_sample_vi as S  # noqa: F401
    import build_1_vi as B  # noqa: F401
    T = importlib.import_module("build_2-3_vi")  # noqa: F841
    F = importlib.import_module("build_4-5_vi")  # noqa: F841
    G = importlib.import_module("build_6_vi")  # noqa: F841
    H = importlib.import_module("build_7-9_vi")  # noqa: F841
    exec(sys.argv[1])


if __name__ == "__main__":
    main()
