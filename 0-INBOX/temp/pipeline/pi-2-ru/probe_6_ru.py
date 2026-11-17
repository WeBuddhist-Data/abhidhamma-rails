# -*- coding: utf-8 -*-
"""Scratch lookup for chapter 6: grep the Pāli of finished pi-2 chapters (or pi-3/4/5) and print the aligned Russian line.
usage: python -I -X utf8 probe_6_ru.py "regex" [maxhits] [book: pi-2 | pi-3 | pi-4 | pi-5] [--full]
"""
import glob, os, re, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
RU = {"pi-2": "pi-2-russian-plain-zeroshot_split_chapters", "pi-3": "pi-3-russian-plain-rails_split_chapters",
      "pi-4": "pi-4-russian-plain-rails_split_chapters", "pi-5": "pi-5-russian-plain-rails_split_chapters",
      "pi-1": "pi-1-russian-plain-rails_split_chapters"}


def main():
    pat = re.compile(sys.argv[1])
    args = [a for a in sys.argv[2:] if not a.startswith("--")]
    maxhits = int(args[0]) if args and args[0].isdigit() else 5
    book = next((a for a in args if a.startswith("pi-")), "pi-2")
    full = "--full" in sys.argv
    hits = 0
    for p in sorted(glob.glob(os.path.join(ROOT, "pali", book + "_split_chapters", "*.md"))):
        rp = os.path.join(ROOT, "russian", RU[book], os.path.basename(p))
        if not os.path.exists(rp):
            continue
        pl = open(p, encoding="utf-8").read().split("\n")
        rl = open(rp, encoding="utf-8").read().split("\n")
        for i, line in enumerate(pl):
            m = pat.search(line)
            if m:
                hits += 1
                if full:
                    print(f"== {os.path.basename(p)}:{i+1}\nPI: {line}\nRU: {rl[i] if i < len(rl) else ''}\n")
                else:
                    s = max(0, m.start() - 120)
                    print(f"== {os.path.basename(p)}:{i+1}\nPI: ...{line[s:m.end()+200]}...\nRU: {(rl[i] if i < len(rl) else '')[:700]}\n")
                if hits >= maxhits:
                    return


if __name__ == "__main__":
    main()
