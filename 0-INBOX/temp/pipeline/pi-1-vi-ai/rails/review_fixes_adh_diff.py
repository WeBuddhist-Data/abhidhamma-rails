"""Diff two termbase_adherence_vi reports (pre / post review fixes): per keyword, miss counts that changed.

usage: python -I -X utf8 review_fixes_adh_diff.py <pre.md> <post.md>
"""
import re
import sys

LINE = re.compile(r"^\s*(\d+)\s+(.+?)\s+->\s+(.+?)\s+e\.g\.\s+(.*)$")


def load(path):
    out = {}
    for line in open(path, encoding="utf-8"):
        m = LINE.match(line.rstrip("\n"))
        if m:
            out[(m.group(2), m.group(3))] = (int(m.group(1)), m.group(4))
    return out


pre, post = load(sys.argv[1]), load(sys.argv[2])
print("total pre", sum(v[0] for v in pre.values()), "post", sum(v[0] for v in post.values()))
for k in sorted(set(pre) | set(post), key=lambda x: x[0]):
    a = pre.get(k, (0, ""))[0]
    b = post.get(k, (0, ""))[0]
    if a != b:
        print(f"{a:4d} -> {b:4d}  {k[0]}  ->  {k[1]}   e.g. {post.get(k, pre.get(k))[1]}")
