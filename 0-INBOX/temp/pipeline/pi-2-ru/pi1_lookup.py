"""Look up Pāli substrings in pi-1 and print the aligned Russian (rails) line.
Usage: python -I -X utf8 pi1_lookup.py "pattern" [maxhits] [--full]
"""
import sys, re, glob, os

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
PALI = os.path.join(ROOT, "pali", "pi-1_split_chapters")
RU = os.path.join(ROOT, "russian", "pi-1-russian-plain-rails_split_chapters")

def main():
    pat = re.compile(sys.argv[1])
    maxhits = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 5
    full = "--full" in sys.argv
    hits = 0
    for p in sorted(glob.glob(os.path.join(PALI, "*.md"))):
        name = os.path.basename(p)
        rp = os.path.join(RU, name)
        if not os.path.exists(rp):
            continue
        pl = open(p, encoding="utf-8").read().split("\n")
        rl = open(rp, encoding="utf-8").read().split("\n")
        for i, line in enumerate(pl):
            if pat.search(line):
                hits += 1
                if full:
                    print(f"== {name}:{i+1}\nPI: {line}\nRU: {rl[i]}\n")
                else:
                    m = pat.search(line)
                    s = max(0, m.start() - 150)
                    print(f"== {name}:{i+1}\nPI: ...{line[s:m.end()+250]}...\nRU: {rl[i][:900]}\n")
                if hits >= maxhits:
                    return

if __name__ == "__main__":
    main()
