"""Scratch for chapters 10-12: print Pāli + aligned Russian (rails) lines of pi-N for a Pāli regex.
Usage: python -I -X utf8 lookup_10_12.py <book 1|3|4|5> "pattern" [maxhits]
"""
import sys, re, glob, os

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"


def main():
    book = sys.argv[1]
    pat = re.compile(sys.argv[2])
    maxhits = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    PALI = os.path.join(ROOT, "pali", f"pi-{book}_split_chapters")
    RU = os.path.join(ROOT, "russian", f"pi-{book}-russian-plain-rails_split_chapters")
    hits = 0
    for p in sorted(glob.glob(os.path.join(PALI, "*.md"))):
        name = os.path.basename(p)
        rp = os.path.join(RU, name)
        if not os.path.exists(rp):
            continue
        pl = open(p, encoding="utf-8").read().split("\n")
        rl = open(rp, encoding="utf-8").read().split("\n")
        if len(pl) != len(rl):
            pn = [l for l in pl if l.strip()]
            rn = [l for l in rl if l.strip()]
            pl, rl = pn, rn
        for i, line in enumerate(pl):
            if pat.search(line):
                hits += 1
                print(f"== {name}:{i+1}\nPI: {line}\nRU: {rl[i] if i < len(rl) else '?'}\n")
                if hits >= maxhits:
                    return


if __name__ == "__main__":
    main()
