# -*- coding: utf-8 -*-
"""Helper for chapters 16 and 9: find a Pāli string in pi-1/3/4/5 and print the aligned Hindi line.

usage: python -I -X utf8 lookup_16_9_hi.py "<regex>" [books=1,3,4,5] [maxhits=5] [maxchars=1500]
"""
import os, re, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
PAIRS = {
    "1": (r"pali\pi-1_split_chapters", r"hindi\pi-1-hindi-plain-rails_split_chapters"),
    "3": (r"pali\pi-3_split_chapters", r"hindi\pi-3-hindi-plain-rails_split_chapters"),
    "4": (r"pali\pi-4_split_chapters", r"hindi\pi-4-hindi-plain-rails_split_chapters"),
    "5": (r"pali\pi-5_split_chapters", r"hindi\pi-5-hindi-plain-rails_split_chapters"),
}


def main():
    pat = re.compile(sys.argv[1])
    books = (sys.argv[2] if len(sys.argv) > 2 else "1,3,4,5").split(",")
    maxhits = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    maxchars = int(sys.argv[4]) if len(sys.argv) > 4 else 1500
    hits = 0
    for b in books:
        pd, hd = (os.path.join(ROOT, x) for x in PAIRS[b])
        for f in sorted(os.listdir(pd)):
            if not f.endswith(".md"):
                continue
            hp = os.path.join(hd, f)
            if not os.path.exists(hp):
                continue
            P = open(os.path.join(pd, f), encoding="utf-8-sig").read().split("\n")
            H = open(hp, encoding="utf-8-sig").read().split("\n")
            for i, line in enumerate(P):
                m = pat.search(line)
                if not m:
                    continue
                s = max(0, m.start() - 120)
                print(f"=== pi-{b} {f}:{i+1}  (P {len(P)} / H {len(H)} lines)")
                print("P:", line[s:m.end() + 200])
                print("H:", H[i][:maxchars] if i < len(H) else "<none>")
                hits += 1
                if hits >= maxhits:
                    return


if __name__ == "__main__":
    main()
