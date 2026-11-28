"""Print the Pāli and Russian lines of the given block ids (pi-6), side by side.

usage: python -I -X utf8 -B show_block.py <id> [<id> ...] [--grep <regex>] [--max N]
  ids like 6-2-36 (no caret). --grep prints every Russian line matching the regex with its Pāli line.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PDIR = ROOT / "AI_translation/pali/pi-6_split_chapters"
RDIR = ROOT / "AI_translation/russian/pi-6-russian-plain-zeroshot_split_chapters"


def lines(p):
    return [ln for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()]


def main():
    args = sys.argv[1:]
    mx = 20
    if "--max" in args:
        i = args.index("--max"); mx = int(args[i + 1]); del args[i:i + 2]
    pat = None
    if "--grep" in args:
        i = args.index("--grep"); pat = re.compile(args[i + 1]); del args[i:i + 2]
    ids = set(args)
    n = 0
    for pf in sorted(PDIR.glob("*.md")):
        pl, rl = lines(pf), lines(RDIR / pf.name)
        for i, (p, r) in enumerate(zip(pl, rl)):
            m = re.search(r"\^([0-9A-Za-z-]+)\s*$", p)
            hit = (m and m.group(1) in ids) or (pat and (pat.search(r) or pat.search(p)))
            if hit:
                n += 1
                if n > mx:
                    return
                print(f"[{pf.stem}:{i + 1}]")
                print("  PI:", p)
                print("  RU:", r)


if __name__ == "__main__":
    main()
