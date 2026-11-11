"""Merge the pi-1 split parts into one zero-shot file (no frontmatter), as the English pi-1 merge.

usage: python -I -X utf8 merge_zeroshot_hi.py [--check-english]
--check-english: apply the same procedure to the English parts and compare with the existing English merged file.
"""
import pathlib, sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PARTS = ["preamble", "1-matika", "2-01-cittuppadakandam", "2-02-cittuppadakandam", "2-03-cittuppadakandam",
         "2-04-cittuppadakandam", "2-05-cittuppadakandam", "3-01-rupakandam", "3-02-rupakandam", "3-03-rupakandam",
         "4-01-nikkhepakandam", "4-02-nikkhepakandam", "4-03-nikkhepakandam", "5-atthakathakandam"]


def merge(d):
    return "\n\n".join((d / f"{p}.md").read_text(encoding="utf-8-sig").strip("\n") for p in PARTS) + "\n"


if "--check-english" in sys.argv:
    e = merge(ROOT / "AI_translation/english/pi-1-english-plain-zeroshot_split_chapters")
    old = (ROOT / "AI_translation/english/pi-1-english-plain-zeroshot.md").read_text(encoding="utf-8-sig")
    print("english procedure identical:", e == old)
    sys.exit()

out = ROOT / "AI_translation/hindi/pi-1-hindi-plain-zeroshot.md"
text = merge(ROOT / "AI_translation/hindi/pi-1-hindi-plain-zeroshot_split_chapters")
out.write_text(text, encoding="utf-8", newline="\n")
print(out.name, "lines", text.count("\n"), "segments", sum(1 for l in text.splitlines() if l.rstrip().split(" ")[-1].startswith("^")))
