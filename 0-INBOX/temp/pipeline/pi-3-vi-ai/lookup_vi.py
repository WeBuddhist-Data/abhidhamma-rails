# -*- coding: utf-8 -*-
"""Find pi-1 / pi-2 Pāli lines matching a regex and print the aligned Vietnamese rails line.
usage: python -I -X utf8 lookup_vi.py <book 1|2> <regex> [maxchars] [maxhits] [file-substring]"""
import os, re, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"


def dirs(book):
    return (os.path.join(ROOT, rf"AI_translation\pali\pi-{book}_split_chapters"),
            os.path.join(ROOT, rf"AI_translation\vietnamese\pi-{book}-vietnamese-plain-rails_split_chapters"))


def lines(path):
    return [l for l in open(path, encoding="utf-8").read().split("\n") if l.strip()]


def main():
    book = sys.argv[1]
    rx = re.compile(sys.argv[2])
    mx = int(sys.argv[3]) if len(sys.argv) > 3 else 600
    hits = int(sys.argv[4]) if len(sys.argv) > 4 else 6
    fsub = sys.argv[5] if len(sys.argv) > 5 else ""
    P, V = dirs(book)
    n = 0
    for fn in sorted(os.listdir(P)):
        if not fn.endswith(".md") or fsub not in fn:
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
