"""Helper: find a Pāli regex in the pi-1 … pi-5 Pāli split chapters and print the same non-empty line of the
approved Russian RAILS translation.

usage: python -I -X utf8 -B find_pi12345r_ru.py <regex> [books: any of 1..5, e.g. 12345] [max_hits] [maxchars]
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
BOOKS = {
    b: (ROOT / f"AI_translation/pali/pi-{b}_split_chapters",
        ROOT / f"AI_translation/russian/pi-{b}-russian-plain-rails_split_chapters")
    for b in "12345"
}


def lines(p):
    return [ln for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()]


def main():
    pat = re.compile(sys.argv[1])
    books = sys.argv[2] if len(sys.argv) > 2 else "12345"
    maxhits = int(sys.argv[3]) if len(sys.argv) > 3 else 6
    maxc = int(sys.argv[4]) if len(sys.argv) > 4 else 600
    hits = 0
    for b in books:
        pdir, rdir = BOOKS[b]
        for pf in sorted(pdir.glob("*.md")):
            rf = rdir / pf.name
            if not rf.exists():
                continue
            pl, rl = lines(pf), lines(rf)
            for i, ln in enumerate(pl):
                m = pat.search(ln)
                if not m:
                    continue
                s = max(0, m.start() - 120)
                print(f"[pi-{b} {pf.name} line {i + 1}]")
                print("  PI:", ln[s:s + 360])
                r = rl[i] if i < len(rl) else "<missing>"
                print("  RU:", r[:maxc])
                hits += 1
                if hits >= maxhits:
                    return


if __name__ == "__main__":
    main()
