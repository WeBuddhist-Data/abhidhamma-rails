"""Chapter-16 helper: look up a Pāli regex in pi-1/3/4/5 (and pi-2 ch1-15) and print the aligned Russian line.
usage: python -I -X utf8 lookup_16.py "regex" [maxhits] [books=1345 2]
"""
import glob, os, re, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
PAIRS = {
    "1": ("pi-1_split_chapters", "pi-1-russian-plain-rails_split_chapters"),
    "2": ("pi-2_split_chapters", "pi-2-russian-plain-zeroshot_split_chapters"),
    "3": ("pi-3_split_chapters", "pi-3-russian-plain-rails_split_chapters"),
    "4": ("pi-4_split_chapters", "pi-4-russian-plain-rails_split_chapters"),
    "5": ("pi-5_split_chapters", "pi-5-russian-plain-rails_split_chapters"),
}


def main():
    pat = re.compile(sys.argv[1])
    maxhits = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    books = sys.argv[3] if len(sys.argv) > 3 else "13452"
    hits = 0
    for b in books:
        pd, rd = PAIRS[b]
        for p in sorted(glob.glob(os.path.join(ROOT, "pali", pd, "*.md"))):
            name = os.path.basename(p)
            if b == "2" and name.startswith("16-"):
                continue
            rp = os.path.join(ROOT, "russian", rd, name)
            if not os.path.exists(rp):
                continue
            pl = open(p, encoding="utf-8").read().split("\n")
            rl = open(rp, encoding="utf-8").read().split("\n")
            for i, line in enumerate(pl):
                m = pat.search(line)
                if m:
                    hits += 1
                    s = max(0, m.start() - 120)
                    print(f"== pi-{b} {name}:{i+1}\nPI: ...{line[s:m.end()+200]}...\nRU: {rl[i][:700] if i < len(rl) else '?'}\n")
                    if hits >= maxhits:
                        return


if __name__ == "__main__":
    main()
