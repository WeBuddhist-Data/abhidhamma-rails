"""Chapter 6 helper (prints only, writes nothing): for each Pāli substring given on the command line, print the first
pi-1 segment lines containing it, with the aligned approved pi-1 Vietnamese rails line (same file, same non-empty line).
usage: python -I -X utf8 probe_6.py [-n N] "<pāli substring>" ...
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation")
PDIR = ROOT / "pali" / "pi-1_split_chapters"
VDIR = ROOT / "vietnamese" / "pi-1-vietnamese-plain-rails_split_chapters"


def lines(p):
    return [ln for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()]


def main():
    args = sys.argv[1:]
    n = 2
    if args and args[0] == "-n":
        n, args = int(args[1]), args[2:]
    data = [(f.name, lines(f), lines(VDIR / f.name)) for f in sorted(PDIR.glob("*.md"))]
    for pat in args:
        found = 0
        print(f"######## {pat}")
        for name, P, V in data:
            for i, ln in enumerate(P):
                if pat in ln and found < n:
                    m = re.search(r"\^([0-9A-Za-z-]+)\s*$", ln)
                    j = i
                    while not m and j + 1 < len(P):
                        j += 1
                        m = re.search(r"\^([0-9A-Za-z-]+)\s*$", P[j])
                    print(f"== {name} line {i} (^{m.group(1) if m else '?'})")
                    print("PI:", ln)
                    print("VI:", V[i] if i < len(V) else "-")
                    found += 1
        if not found:
            print("NOT FOUND")
        print()


if __name__ == "__main__":
    main()
