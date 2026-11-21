"""Helper: compact view of the pi-4 termbase, lines a..b: 'head = viet [tag≤N] ; viet2 [tag]'.

usage: python -I -X utf8 tb_compact_vi.py <a> <b> [taglen]
"""
import pathlib
import re
import sys

TB = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\vietnamese\pi-4-pali-vietnamese-termbase-plain.md")


def main():
    a, b = int(sys.argv[1]), int(sys.argv[2])
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 30
    lines = TB.read_text(encoding="utf-8").splitlines()
    for i in range(a - 1, min(b, len(lines))):
        ln = lines[i]
        head, _, body = ln.partition(": {")
        body = body.rstrip("}")
        senses = []
        for s in re.split(r"; (?=[^;:]*: )", body):
            tag, _, vi = s.rpartition(": ")
            senses.append(f"{vi} [{tag[:n]}]" if n else vi)
        print(f"{i + 1} {head} = " + " ; ".join(senses))


if __name__ == "__main__":
    main()
