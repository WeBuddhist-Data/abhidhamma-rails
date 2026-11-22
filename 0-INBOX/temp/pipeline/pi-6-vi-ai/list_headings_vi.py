"""Helper: print the first heading of every pi-6 Pāli split chapter, and all heading lines of the files named
on the command line, each with the English rails heading of the same line (meaning cross-check only).

usage: python -I -X utf8 -B list_headings_vi.py [file.md ...]
"""
import pathlib
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI = ROOT / "AI_translation/pali/pi-6_split_chapters"
EN = ROOT / "AI_translation/english/pi-6-english-plain-rails_split_chapters"


def nonempty(p):
    return [l for l in p.read_text(encoding="utf-8").splitlines() if l.strip()] if p.exists() else []


def main():
    for pf in sorted(PALI.glob("*.md")):
        pl, el = nonempty(pf), nonempty(EN / pf.name)
        for i, l in enumerate(pl):
            if l.startswith("#"):
                print(f"{pf.name:26} {l}   || {el[i] if i < len(el) else ''}")
                break
    for name in sys.argv[1:]:
        print(f"===== {name}")
        pl, el = nonempty(PALI / name), nonempty(EN / name)
        seen = set()
        for i, l in enumerate(pl):
            if l.startswith("#"):
                key = l.split(" ^")[0]
                if key in seen:
                    continue
                seen.add(key)
                print(f"{l}   || {el[i] if i < len(el) else ''}")


if __name__ == "__main__":
    main()
