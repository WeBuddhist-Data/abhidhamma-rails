"""Helper: find a Pāli regex in the pi-1 / pi-2 / pi-3 Pāli split chapters and print the same non-empty
line of the approved Vietnamese rails (adapted copy of pi-3-vi-ai\\rails\\find_pi12_vi.py).

usage: python -I -X utf8 find_pi123_vi.py <regex> [books: any of 1 2 3, e.g. 123] [max_hits] [maxchars] [ctx]
ctx = characters of Pāli context shown around the hit (default 360).
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
BOOKS = {
    b: (ROOT / f"AI_translation/pali/pi-{b}_split_chapters",
        ROOT / f"AI_translation/vietnamese/pi-{b}-vietnamese-plain-rails_split_chapters")
    for b in "123"
}


def lines(p):
    return [ln for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()]


def main():
    pat = re.compile(sys.argv[1])
    books = sys.argv[2] if len(sys.argv) > 2 else "123"
    maxhits = int(sys.argv[3]) if len(sys.argv) > 3 else 6
    maxc = int(sys.argv[4]) if len(sys.argv) > 4 else 600
    ctx = int(sys.argv[5]) if len(sys.argv) > 5 else 360
    hits = 0
    for b in books:
        pdir, vdir = BOOKS[b]
        for pf in sorted(pdir.glob("*.md")):
            vf = vdir / pf.name
            if not vf.exists():
                continue
            pl, vl = lines(pf), lines(vf)
            for i, ln in enumerate(pl):
                m = pat.search(ln)
                if not m:
                    continue
                s = max(0, m.start() - 120)
                print(f"[pi-{b} {pf.name} line {i + 1}]")
                print("  PI:", ln[s:s + ctx])
                print("  VI:", (vl[i] if i < len(vl) else "<missing>")[:maxc])
                hits += 1
                if hits >= maxhits:
                    return


if __name__ == "__main__":
    main()
