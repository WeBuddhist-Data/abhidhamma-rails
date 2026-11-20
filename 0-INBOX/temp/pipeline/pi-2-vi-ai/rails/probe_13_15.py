"""Print the pi-1 Pāli line and the approved pi-1 Vietnamese line for the given block ids (read-only probe).

usage: python -I -X utf8 probe_13_15.py 1-431 1-443 ...
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PA = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
VI = ROOT / "AI_translation" / "vietnamese" / "pi-1-vietnamese-plain-rails_split_chapters"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def main():
    want = set(sys.argv[1:])
    for f in sorted(PA.glob("*.md")):
        pa = f.read_text(encoding="utf-8").splitlines()
        vi = (VI / f.name).read_text(encoding="utf-8").splitlines()
        for p, v in zip(pa, vi):
            m = ID.search(p)
            if m and m.group(1) in want:
                print(f"== {m.group(1)}\nP: {p}\nV: {v}\n")


if __name__ == "__main__":
    main()
