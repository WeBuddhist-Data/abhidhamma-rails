"""Check bare condition stems used as standalone words (not inside a hyphen list) in 1-01 / 1-02.
usage: python -I -B -X utf8 check_1-01_1-02_hi.py <f>
"""
import sys, pathlib, re; sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_keywords, read_pali, read_hindi, CONDITIONS, lc  # noqa: E402

f = sys.argv[1]
pa, hi = read_pali(f), read_hindi(f)
stems = {c[0] for c in CONDITIONS} | {"na" + c[0] for c in CONDITIONS} | {"no" + c[0] for c in CONDITIONS}
mapped = {}
for line in (pathlib.Path(__file__).resolve().parent / f"{f}.mapped.md").read_text(encoding="utf-8").splitlines():
    bid, _, rest = line.partition("] ")
    mapped[bid[1:]] = rest
for bid, kws in read_keywords(f):
    for k in sorted(set(kws)):
        if lc(k) in stems:
            p = pa.get(bid, "")
            # standalone: preceded by start/space/( and followed by space/./)/,
            if re.search(r"(?:^|[\s(])" + re.escape(k) + r"(?=[\s.,;)])", p):
                m = re.search(r"(?:^|[\s(])" + re.escape(k) + r"(?=[\s.,;)])", p)
                val = [x for x in mapped[bid].split(", ") if x.startswith(k + "=")][:1]
                print(bid, k, val, "|", p[max(0, m.start() - 60): m.end() + 60].replace("\n", " "))
