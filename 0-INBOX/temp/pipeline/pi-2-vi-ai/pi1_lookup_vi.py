# -*- coding: utf-8 -*-
"""Find pi-1 Pāli lines matching a regex and print the aligned pi-1 Vietnamese rails line.
usage: python -I -X utf8 pi1_lookup_vi.py <regex> [maxchars] [maxhits]"""
import os, re, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
P = os.path.join(ROOT, r"AI_translation\pali\pi-1_split_chapters")
V = os.path.join(ROOT, r"AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters")


def lines(path):
    return [l for l in open(path, encoding="utf-8").read().split("\n") if l.strip()]


def main():
    rx = re.compile(sys.argv[1])
    mx = int(sys.argv[2]) if len(sys.argv) > 2 else 600
    hits = int(sys.argv[3]) if len(sys.argv) > 3 else 6
    n = 0
    for fn in sorted(os.listdir(P)):
        if not fn.endswith(".md"):
            continue
        pl, vl = lines(os.path.join(P, fn)), lines(os.path.join(V, fn))
        for i, l in enumerate(pl):
            if rx.search(l):
                print(f"== {fn}:{i}")
                print("P:", l[:mx])
                print("V:", vl[i][:mx])
                n += 1
                if n >= hits:
                    return


if __name__ == "__main__":
    main()
