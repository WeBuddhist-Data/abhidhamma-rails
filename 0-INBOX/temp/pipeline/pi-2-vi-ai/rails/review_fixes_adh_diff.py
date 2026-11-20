"""Diff of the termbase-adherence miss lists before / after the review fixes (headword: pre -> post)."""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))


def read(name):
    out = {}
    for l in open(os.path.join(HERE, name), encoding="utf-8"):
        m = re.match(r"\s*(\d+)\s+(.+?)\s+->\s+(.+?)\s+e\.g\.", l)
        if m:
            out[m.group(2)] = (int(m.group(1)), m.group(3))
    return out


pre, post = read("review_fixes_adherence_pre.md"), read("review_fixes_adherence_post.md")
for k in sorted(set(pre) | set(post), key=lambda k: -(post.get(k, (0,))[0] - pre.get(k, (0,))[0])):
    a, b = pre.get(k, (0, ""))[0], post.get(k, (0, ""))[0]
    if a != b:
        print(f"{b - a:+4d}  {k}  ({a} -> {b})  termbase: {post.get(k, pre.get(k))[1]}")
