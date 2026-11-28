"""Coordinator: compare tag wording across part1 and part2 senses (pi-6 Russian). For every Russian value that has
senses in BOTH parts, list the distinct tag glosses (the tag with its final "(grammar)" label and the -ti / ca / ceva /
pi particle clauses removed). Values whose gloss differs between the parts are printed for review.
usage: python -I -X utf8 -B compare_parts_ru.py [max]
"""
import collections
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
LINE = re.compile(r"^(.*?): \{(.*)\}$")


def senses(path):
    out = []
    for l in path.read_text(encoding="utf-8").splitlines():
        m = LINE.match(l)
        if not m:
            continue
        hw, body = m.groups()
        for s in body.split("; "):
            tag, vals = s.rsplit(": ", 1)
            out.append((hw, tag, [v.strip() for v in vals.split(" / ")]))
    return out


def gloss(tag):
    t = re.sub(r"\s*\([^()]*\)\s*$", "", tag)
    t = re.sub(r",? ?(quoted with -ti|with ca 'and'|with ceva 'both … and'|with pi 'also')", "", t)
    return t.strip(" ,")


def main():
    mx = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    by = collections.defaultdict(lambda: collections.defaultdict(set))
    for part in ("part1", "part2"):
        for hw, tag, vals in senses(HERE / f"{part}-senses.md"):
            by[vals[0]][part].add((gloss(tag), hw))
    n = 0
    for v, parts in sorted(by.items()):
        if len(parts) < 2:
            continue
        g1 = {g for g, _ in parts["part1"]}
        g2 = {g for g, _ in parts["part2"]}
        if g1 & g2:
            continue
        n += 1
        if n <= mx:
            print(f"[{v}]")
            for p in ("part1", "part2"):
                for g, hw in sorted(parts[p])[:3]:
                    print(f"   {p} {hw}: {g}")
    print("values in both parts with no shared gloss:", n)


if __name__ == "__main__":
    main()
