# -*- coding: utf-8 -*-
"""Scratch lookup for chapters 4-5: print pi-1 Pāli + Vietnamese rails lines by block ID, or pi-1 lines whose Pāli
matches a regex (P:, V:). usage: python -I -X utf8 probe_4-5_vi.py id <bid> [<bid> ...] | rx <regex> [maxhits]"""
import os, re, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
P = os.path.join(ROOT, r"AI_translation\pali\pi-1_split_chapters")
V = os.path.join(ROOT, r"AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters")
ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def load(d):
    out = {}
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".md"):
            for l in open(os.path.join(d, fn), encoding="utf-8").read().split("\n"):
                m = ID.search(l)
                if m:
                    out[m.group(1)] = l
    return out


def main():
    pp, vv = load(P), load(V)
    if sys.argv[1] == "id":
        for b in sys.argv[2:]:
            print("==", b)
            print("P:", pp.get(b))
            print("V:", vv.get(b))
    else:
        rx = re.compile(sys.argv[2])
        mx = int(sys.argv[3]) if len(sys.argv) > 3 else 8
        n = 0
        for b, l in pp.items():
            if rx.search(l):
                print("==", b)
                print("P:", l[:1500])
                print("V:", vv.get(b, "")[:1500])
                n += 1
                if n >= mx:
                    break


if __name__ == "__main__":
    main()
