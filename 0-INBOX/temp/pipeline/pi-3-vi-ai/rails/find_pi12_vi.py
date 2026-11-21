"""Helper: find a Pāli regex in the pi-1 / pi-2 Pāli split chapters and print the same non-empty
line of the approved Vietnamese rails.

usage: python -I -X utf8 find_pi12_vi.py <regex> [book: 1|2|12] [max_hits] [maxchars]
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
BOOKS = {
    "1": (ROOT / "AI_translation/pali/pi-1_split_chapters",
          ROOT / "AI_translation/vietnamese/pi-1-vietnamese-plain-rails_split_chapters"),
    "2": (ROOT / "AI_translation/pali/pi-2_split_chapters",
          ROOT / "AI_translation/vietnamese/pi-2-vietnamese-plain-rails_split_chapters"),
}


def lines(p):
    return [ln for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()]


def main():
    pat = re.compile(sys.argv[1])
    books = sys.argv[2] if len(sys.argv) > 2 else "12"
    maxhits = int(sys.argv[3]) if len(sys.argv) > 3 else 6
    maxc = int(sys.argv[4]) if len(sys.argv) > 4 else 600
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
                print("  PI:", ln[s:s + 360])
                print("  VI:", (vl[i] if i < len(vl) else "<missing>")[:maxc])
                hits += 1
                if hits >= maxhits:
                    return


if __name__ == "__main__":
    main()
