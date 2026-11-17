"""Chapter-17 helper: look up a Pāli regex in pi-1/3/4/5 (and pi-2 ch1-16) and print the FULL aligned lines.
usage: python -I -X utf8 lookup_17.py "regex" [maxhits] [books=12345] [pali=1]
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
    books = sys.argv[3] if len(sys.argv) > 3 else "12345"
    show_pali = (sys.argv[4] != "0") if len(sys.argv) > 4 else True
    hits = 0
    for b in books:
        pd, rd = PAIRS[b]
        for p in sorted(glob.glob(os.path.join(ROOT, "pali", pd, "*.md"))):
            name = os.path.basename(p)
            if b == "2" and name.startswith("17-"):
                continue
            rp = os.path.join(ROOT, "russian", rd, name)
            if not os.path.exists(rp):
                continue
            pl = open(p, encoding="utf-8").read().split("\n")
            rl = open(rp, encoding="utf-8").read().split("\n")
            for i, line in enumerate(pl):
                if pat.search(line):
                    hits += 1
                    print(f"== pi-{b} {name}:{i+1}")
                    if show_pali:
                        print("PI: " + line)
                    print("RU: " + (rl[i] if i < len(rl) else "?") + "\n")
                    if hits >= maxhits:
                        return


if __name__ == "__main__":
    main()
