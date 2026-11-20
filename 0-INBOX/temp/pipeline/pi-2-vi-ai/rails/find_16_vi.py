"""Find Pāli phrases of pi-2 chapter 16 in the pi-1 Pāli split chapters and in the finished pi-2 Pāli chapters 1-15,
and show the approved Vietnamese line of the same position (same file name, same line number). Reads only
AI_translation/pali/pi-1_split_chapters/*.md, AI_translation/vietnamese/pi-1-vietnamese-plain-rails_split_chapters/*.md,
AI_translation/pali/pi-2_split_chapters/<ch 1-15>.md and the same-named files of
AI_translation/vietnamese/pi-2-vietnamese-plain-rails_split_chapters/. Writes rails/find-16-vi.txt.

usage: python -I -X utf8 find_16_vi.py "phrase one" "phrase two" ...
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PAIRS = [(ROOT / "AI_translation" / "pali" / "pi-1_split_chapters",
          ROOT / "AI_translation" / "vietnamese" / "pi-1-vietnamese-plain-rails_split_chapters", None),
         (ROOT / "AI_translation" / "pali" / "pi-2_split_chapters",
          ROOT / "AI_translation" / "vietnamese" / "pi-2-vietnamese-plain-rails_split_chapters",
          ["1-khandhavibhango.md", "2-ayatanavibhango.md", "3-dhatuvibhango.md", "4-saccavibhango.md",
           "5-indriyavibhango.md", "6-paticcasamuppadavibhango.md", "7-satipatthanavibhango.md",
           "8-sammappadhanavibhango.md", "9-iddhipadavibhango.md", "10-bojjhangavibhango.md",
           "11-maggangavibhango.md", "12-jhanavibhango.md", "13-appamannavibhango.md",
           "14-sikkhapadavibhango.md", "15-patisambhidavibhango.md"])]
OUT = ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-2-vi-ai" / "rails" / "find-16-vi.txt"
MAXHITS = 1
WIDTH = 1800


def main():
    data = []
    for pa_dir, vi_dir, names in PAIRS:
        files = [pa_dir / n for n in names] if names else sorted(pa_dir.glob("*.md"))
        for f in files:
            pa = f.read_text(encoding="utf-8").splitlines()
            vi = (vi_dir / f.name).read_text(encoding="utf-8").splitlines()
            data.append((pa_dir.name[:4] + "/" + f.name, pa, vi))
    out = []
    for phrase in sys.argv[1:]:
        out.append(f"### {phrase}")
        n = 0
        for corpus in ("pi-1", "pi-2"):
            k = 0
            for name, pa, vi in data:
                if not name.startswith(corpus):
                    continue
                for i, ln in enumerate(pa):
                    if phrase in ln:
                        bid = re.search(r"\^([0-9A-Za-z-]+)\s*$", ln)
                        j = ln.index(phrase)
                        out.append(f"[{name}:{i + 1}{' ^' + bid.group(1) if bid else ''}] PA: "
                                   f"{ln[max(0, j - 200):j + len(phrase) + 300]}")
                        out.append(f"VI: {vi[i][:WIDTH]}")
                        k += 1
                        n += 1
                        if k >= MAXHITS:
                            break
                if k >= MAXHITS:
                    break
        if not n:
            out.append("(no hit)")
    OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"wrote {OUT.name}: {len(sys.argv) - 1} phrases")


if __name__ == "__main__":
    main()
