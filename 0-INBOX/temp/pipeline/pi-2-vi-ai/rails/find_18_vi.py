"""Find Pāli phrases of pi-2 chapter 18 in the pi-1 Pāli split chapters and in the finished pi-2 Pāli chapters 1-17,
and print (writes nothing) the approved Vietnamese line of the same position (same file name, same non-empty line).
Reads only AI_translation/pali/pi-1_split_chapters/*.md, AI_translation/vietnamese/pi-1-vietnamese-plain-rails_split_chapters/*.md,
AI_translation/pali/pi-2_split_chapters/<ch 1-17>.md and the same-named files of
AI_translation/vietnamese/pi-2-vietnamese-plain-rails_split_chapters/.

usage: python -I -X utf8 find_18_vi.py [-n MAXHITS] [-w WIDTH] [-c pi-1|pi-2] "phrase one" "phrase two" ...
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PI1 = ["1-matika.md", "2-01-cittuppadakandam.md", "2-02-cittuppadakandam.md", "2-03-cittuppadakandam.md",
       "2-04-cittuppadakandam.md", "2-05-cittuppadakandam.md", "3-01-rupakandam.md", "3-02-rupakandam.md",
       "3-03-rupakandam.md", "4-01-nikkhepakandam.md", "4-02-nikkhepakandam.md", "4-03-nikkhepakandam.md",
       "5-atthakathakandam.md"]
PI2 = ["1-khandhavibhango.md", "2-ayatanavibhango.md", "3-dhatuvibhango.md", "4-saccavibhango.md",
       "5-indriyavibhango.md", "6-paticcasamuppadavibhango.md", "7-satipatthanavibhango.md",
       "8-sammappadhanavibhango.md", "9-iddhipadavibhango.md", "10-bojjhangavibhango.md",
       "11-maggangavibhango.md", "12-jhanavibhango.md", "13-appamannavibhango.md",
       "14-sikkhapadavibhango.md", "15-patisambhidavibhango.md", "16-nanavibhango.md",
       "17-khuddakavatthuvibhango.md"]
PAIRS = [("pi-1", ROOT / "AI_translation" / "pali" / "pi-1_split_chapters",
          ROOT / "AI_translation" / "vietnamese" / "pi-1-vietnamese-plain-rails_split_chapters", PI1),
         ("pi-2", ROOT / "AI_translation" / "pali" / "pi-2_split_chapters",
          ROOT / "AI_translation" / "vietnamese" / "pi-2-vietnamese-plain-rails_split_chapters", PI2)]


def nonempty(p):
    return [ln for ln in p.read_text(encoding="utf-8").split("\n") if ln.strip()]


def main():
    args = sys.argv[1:]
    maxhits, width, only = 1, 900, None
    while args and args[0] in ("-n", "-w", "-c"):
        if args[0] == "-n":
            maxhits = int(args[1])
        elif args[0] == "-w":
            width = int(args[1])
        else:
            only = args[1]
        args = args[2:]
    data = []
    for tag, pa_dir, vi_dir, names in PAIRS:
        if only and tag != only:
            continue
        for n in names:
            pa, vi = nonempty(pa_dir / n), nonempty(vi_dir / n)
            data.append((tag + "/" + n, pa, vi))
    for phrase in args:
        print(f"### {phrase}")
        k = 0
        for name, pa, vi in data:
            for i, ln in enumerate(pa):
                if phrase in ln:
                    bid = re.search(r"\^([0-9A-Za-z-]+)\s*$", ln)
                    j = ln.index(phrase)
                    print(f"[{name}:{i + 1}{' ^' + bid.group(1) if bid else ''}] PA: "
                          f"{ln[max(0, j - 150):j + len(phrase) + 250]}")
                    print(f"VI: {vi[i][:width] if i < len(vi) else '(no line)'}")
                    k += 1
                    if k >= maxhits:
                        break
            if k >= maxhits:
                break
        if not k:
            print("(no hit)")


if __name__ == "__main__":
    main()
