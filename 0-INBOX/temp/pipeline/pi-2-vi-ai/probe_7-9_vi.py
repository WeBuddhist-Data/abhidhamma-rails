# -*- coding: utf-8 -*-
"""Scratch lookup for chapters 7-9: pi-1 lines whose Pāli matches <pali-rx>; prints a window of the Pāli around
the match and a window of the aligned Vietnamese around <vi-rx> (or its start).
usage: python -I -X utf8 probe_7-9_vi.py <pali-rx> [vi-rx] [maxhits] [window]"""
import os, re, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
P = os.path.join(ROOT, r"AI_translation\pali\pi-1_split_chapters")
V = os.path.join(ROOT, r"AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters")
ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def main():
    prx = re.compile(sys.argv[1])
    vrx = re.compile(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] else None
    mx = int(sys.argv[3]) if len(sys.argv) > 3 else 4
    w = int(sys.argv[4]) if len(sys.argv) > 4 else 220
    n = 0
    for fn in sorted(os.listdir(P)):
        if not fn.endswith(".md"):
            continue
        pl = [l for l in open(os.path.join(P, fn), encoding="utf-8").read().split("\n") if l.strip()]
        vl = [l for l in open(os.path.join(V, fn), encoding="utf-8").read().split("\n") if l.strip()]
        for a, b in zip(pl, vl):
            m = prx.search(a)
            if not m:
                continue
            mid = ID.search(a)
            print("==", fn, mid.group(1) if mid else "")
            print("P:", a[max(0, m.start() - w // 2):m.end() + w])
            mv = vrx.search(b) if vrx else None
            if mv:
                print("V:", b[max(0, mv.start() - w // 2):mv.end() + w])
            else:
                print("V:", b[:w * 2])
            n += 1
            if n >= mx:
                return


if __name__ == "__main__":
    main()
