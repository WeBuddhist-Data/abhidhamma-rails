"""Helper for the pi-7 sample: for each chapter file, print the first N sentences of the Paṭicca frame
(Pāli «paṭicca» sentence | Hindi sentence) so the triad/dyad item wording can be read off.
usage: python -I -B -X utf8 frames_sample_hi.py <file-glob> [N]
"""
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PI = ROOT / "AI_translation" / "pali" / "pi-7_split_chapters"
HI = ROOT / "AI_translation" / "hindi" / "pi-7-hindi-plain-zeroshot_split_chapters"


def segs(path):
    out = {}
    for block in re.split(r"\n\s*\n", path.read_text(encoding="utf-8")):
        m = re.search(r"\^([0-9A-Za-z-]+)\s*$", block.strip())
        if m:
            out[m.group(1)] = block.strip()[: m.start()].strip()
    return out


def main():
    pat, n = sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 3
    for p in sorted(PI.glob(pat + ".md")):
        a, b = segs(p), segs(HI / p.name)
        shown = 0
        for bid, t in a.items():
            if "paṭicca" in t and not t.startswith("#") and bid in b:
                ps = [s for s in re.split(r"(?<=[.?])\s+", t) if "paṭicca" in s]
                hs = [s for s in re.split(r"(?<=[।?])\s+", b[bid]) if "निर्भर" in s]
                for x, y in list(zip(ps, hs))[:n]:
                    print(f"{p.stem} {bid}\n  P: {x}\n  H: {y}")
                shown += 1
                if shown >= 1:
                    break


if __name__ == "__main__":
    main()
