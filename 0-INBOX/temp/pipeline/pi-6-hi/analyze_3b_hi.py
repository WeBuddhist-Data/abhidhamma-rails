r"""Helper for 3-0x-ayatanayamaka: distinct who/where phrases of the pavatti answers.
usage: python -I -X utf8 analyze_3b_hi.py
"""
import collections
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi")
import analyze_3_hi as A  # noqa: E402

AYV = A.AY + r" (?:ca )?(?:n?uppajj|nirujjh|na nirujjh|na uppajj)"


def main():
    c = collections.Counter()
    for n, i, l in A.lines(range(1, 7)):
        if l.startswith("(") or l.startswith("#"):
            continue
        for s in re.split(r"(?<=[.?]) ", l):
            m = re.match(r"(.+?) (?:tesaṃ|tattha|tasaṃ) ", s)
            if m and not s.startswith(("Yassa", "Yattha")):
                c[m.group(1)] += 1
            else:
                c["#SENT " + s[:90]] += 1
    for t, k in sorted(c.items()):
        print(k, t)


if __name__ == "__main__":
    main()
