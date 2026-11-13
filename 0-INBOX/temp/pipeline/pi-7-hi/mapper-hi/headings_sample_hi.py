"""Helper for the pi-7 sample: print every heading (Pāli | Hindi) of the book, unique pairs, to settle heading values.
usage: python -I -B -X utf8 headings_sample_hi.py [filter-substring]
"""
import collections
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PI = ROOT / "AI_translation" / "pali" / "pi-7_split_chapters"
HI = ROOT / "AI_translation" / "hindi" / "pi-7-hindi-plain-zeroshot_split_chapters"


def heads(path):
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^#+\s*(.*?)\s*\^([0-9A-Za-z-]+)\s*$", line)
        if m:
            out[m.group(2)] = m.group(1).strip("* ")
    return out


def main():
    flt = sys.argv[1] if len(sys.argv) > 1 else ""
    seen = collections.Counter()
    for p in sorted(PI.glob("*.md")):
        a, b = heads(p), heads(HI / p.name)
        for bid, t in a.items():
            seen[(re.sub(r"^[\d\-.() ]+", "", t), re.sub(r"^[\d\-.() ]+", "", b.get(bid, "?")))] += 1
    for (pa, hi), c in sorted(seen.items()):
        if flt in pa or flt in hi:
            print(f"{c:4} {pa} | {hi}")


if __name__ == "__main__":
    main()
