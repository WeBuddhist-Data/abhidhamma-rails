# -*- coding: utf-8 -*-
"""Scratch lookup for ch. 16: find Pāli lines matching a regex in pi-1 (rails) and pi-2 ch. 1-15 (zero-shot) and
print the aligned Vietnamese line (optionally only the window around the match).
usage: python -I -X utf8 probe_16_vi.py <regex> [maxhits] [window]"""
import os, re, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PAIRS = [
    (os.path.join(ROOT, r"AI_translation\pali\pi-1_split_chapters"),
     os.path.join(ROOT, r"AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters"), None),
    (os.path.join(ROOT, r"AI_translation\pali\pi-2_split_chapters"),
     os.path.join(ROOT, r"AI_translation\vietnamese\pi-2-vietnamese-plain-zeroshot_split_chapters"), 15),
]


def lines(path):
    return [l for l in open(path, encoding="utf-8").read().split("\n") if l.strip()]


def main():
    rx = re.compile(sys.argv[1])
    hits = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    win = int(sys.argv[3]) if len(sys.argv) > 3 else 700
    n = 0
    for pdir, vdir, maxch in PAIRS:
        for fn in sorted(os.listdir(pdir)):
            if not fn.endswith(".md"):
                continue
            if maxch is not None:
                try:
                    if int(fn.split("-")[0]) > maxch:
                        continue
                except ValueError:
                    continue
            vp = os.path.join(vdir, fn)
            if not os.path.exists(vp):
                continue
            pl, vl = lines(os.path.join(pdir, fn)), lines(vp)
            for i, l in enumerate(pl):
                m = rx.search(l)
                if m:
                    print(f"== {os.path.basename(pdir)}/{fn}:{i}")
                    s = max(0, m.start() - 100)
                    print("P:", l[s:s + win])
                    print("V:", vl[i][:win * 2] if len(vl[i]) < win * 2 else vl[i][:win * 2] + " …")
                    n += 1
                    if n >= hits:
                        return


if __name__ == "__main__":
    main()
