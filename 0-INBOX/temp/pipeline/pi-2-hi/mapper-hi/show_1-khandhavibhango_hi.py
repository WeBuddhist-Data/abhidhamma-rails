"""Print Pāli, Hindi and keywords of given segment ids (pi-2).

usage: python -I -X utf8 show_1-khandhavibhango_hi.py <chapter> id [id ...]
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
HI = ROOT / "AI_translation" / "hindi" / "pi-2-hindi-plain-zeroshot_split_chapters"
PI = ROOT / "AI_translation" / "pali" / "pi-2_split_chapters"


def segs(path):
    out = {}
    for block in re.split(r"\n\s*\n", path.read_text(encoding="utf-8")):
        block = block.strip()
        m = re.search(r"\^([0-9A-Za-z-]+)\s*$", block)
        if m:
            out[m.group(1)] = block[: m.start()].strip()
    return out


def kws(ch):
    out = {}
    for line in (HERE / f"{ch}.keywords.md").read_text(encoding="utf-8").splitlines():
        if line.strip():
            b, r = line.split("] ", 1)
            out[b[1:]] = r
    return out


if __name__ == "__main__":
    ch = sys.argv[1]
    p, h, k = segs(PI / f"{ch}.md"), segs(HI / f"{ch}.md"), kws(ch)
    for i in sys.argv[2:]:
        print(f"=== {i}\nPI: {p.get(i)}\nHI: {h.get(i)}\nKW: {k.get(i)}\n")
