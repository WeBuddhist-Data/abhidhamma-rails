# -*- coding: utf-8 -*-
"""Scratch lookup for chapter 17: Pāli regex -> aligned Vietnamese line in pi-1 rails and pi-2 ch1-16 zero-shot.
usage: python -I -X utf8 probe_17_vi.py <regex> [maxchars] [maxhits] [vi_regex]
If vi_regex is given, only the Vietnamese part around its first match is printed (±maxchars/2)."""
import os
import re
import sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
SETS = [
    (os.path.join(ROOT, r"AI_translation\pali\pi-1_split_chapters"),
     os.path.join(ROOT, r"AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters")),
    (os.path.join(ROOT, r"AI_translation\pali\pi-2_split_chapters"),
     os.path.join(ROOT, r"AI_translation\vietnamese\pi-2-vietnamese-plain-zeroshot_split_chapters")),
]


def lines(path):
    return [l for l in open(path, encoding="utf-8").read().split("\n") if l.strip()]


def main():
    rx = re.compile(sys.argv[1])
    mx = int(sys.argv[2]) if len(sys.argv) > 2 else 600
    hits = int(sys.argv[3]) if len(sys.argv) > 3 else 6
    vrx = re.compile(sys.argv[4]) if len(sys.argv) > 4 else None
    n = 0
    for pdir, vdir in SETS:
        for fn in sorted(os.listdir(pdir)):
            if not fn.endswith(".md") or fn.startswith("17-") or not os.path.exists(os.path.join(vdir, fn)):
                continue
            pl, vl = lines(os.path.join(pdir, fn)), lines(os.path.join(vdir, fn))
            for i, l in enumerate(pl):
                m = rx.search(l)
                if not m:
                    continue
                v = vl[i] if i < len(vl) else ""
                print(f"== {fn}:{i}")
                s = max(0, m.start() - mx // 4)
                print("P:", l[s:s + mx])
                if vrx and vrx.search(v):
                    vs = max(0, vrx.search(v).start() - mx // 2)
                    print("V:", v[vs:vs + mx])
                else:
                    print("V:", v[:mx])
                n += 1
                if n >= hits:
                    return


if __name__ == "__main__":
    main()
