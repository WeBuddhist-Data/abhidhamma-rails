"""G2 helper: frequency of keywords (lower-cased first letter) across pi-6 keyword files matching a regex.
usage: kwfreq_G2_ru.py REGEX [files-glob]"""
import collections
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
rx = re.compile(sys.argv[1])
glob = sys.argv[2] if len(sys.argv) > 2 else "*.keywords.md"
c = collections.Counter()
where = collections.defaultdict(set)
for f in sorted(HERE.glob(glob)):
    for line in f.read_text(encoding="utf-8").splitlines():
        if "] " not in line:
            continue
        for k in line.split("] ", 1)[1].split(", "):
            k = k.strip()
            if rx.fullmatch(k):
                c[k] += 1
                where[k].add(f.name.split(".")[0])
for k, n in c.most_common():
    print(n, k, " ".join(sorted(where[k]))[:150])
