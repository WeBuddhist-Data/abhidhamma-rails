"""Show Pāli lines matching a regex and the aligned FINAL Burmese line (rails) of pi-1 … pi-6.

usage: python3 -I -X utf8 kwic.py <regex> [books e.g. 1,2,5] [max]
Read-only: it never writes anything.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
AI = ROOT / "AI_translation"


def main():
    rx = re.compile(sys.argv[1])
    books = sys.argv[2].split(",") if len(sys.argv) > 2 else ["1", "2", "3", "4", "5", "6"]
    mx = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    for b in books:
        pd = AI / f"pali/pi-{b}_split_chapters"
        md = AI / f"burmese/pi-{b}-burmese-plain-rails_split_chapters"
        n = 0
        for pf in sorted(pd.glob("*.md")):
            mf = md / pf.name
            if not mf.exists():
                continue
            pl = pf.read_text(encoding="utf-8-sig").splitlines()
            ml = mf.read_text(encoding="utf-8-sig").splitlines()
            for i, line in enumerate(pl):
                if rx.search(line):
                    print(f"[pi-{b} {pf.name}:{i + 1}] {line[:600]}")
                    print(f"   MY: {ml[i][:600] if i < len(ml) else '??'}")
                    n += 1
                    if n >= mx:
                        break
            if n >= mx:
                break


main()
