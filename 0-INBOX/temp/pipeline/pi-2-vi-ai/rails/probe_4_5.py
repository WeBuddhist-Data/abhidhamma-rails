"""Find pi-1 Pāli lines containing a substring and print them with the approved pi-1 Vietnamese rails line
(helper for chapters 4-5). Reads only; writes nothing.

usage: python -I -X utf8 probe_4_5.py [-n N] "<pāli substring>" ...      (N = max hits per substring, default 1)
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PA = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
VI = ROOT / "AI_translation" / "vietnamese" / "pi-1-vietnamese-plain-rails_split_chapters"


def main():
    args = sys.argv[1:]
    n = 1
    if args[:1] == ["-n"]:
        n = int(args[1])
        args = args[2:]
    files = sorted(PA.glob("*.md"))
    for s in args:
        hits = 0
        for f in files:
            pa = f.read_text(encoding="utf-8").splitlines()
            vi = (VI / f.name).read_text(encoding="utf-8").splitlines()
            for i, ln in enumerate(pa):
                if s in ln:
                    print(f"== {f.stem}:{i + 1} [{s}]\nPA: {ln}\nVI: {vi[i]}\n")
                    hits += 1
                    if hits >= n:
                        break
            if hits >= n:
                break
        if not hits:
            print(f"== NOT FOUND: {s}\n")


if __name__ == "__main__":
    main()
