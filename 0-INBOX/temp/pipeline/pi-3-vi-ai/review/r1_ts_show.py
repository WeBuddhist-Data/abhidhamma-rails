"""r1: print (console only) reference-translation segments for given block IDs. Writes nothing."""
import re, sys
TS = r"D:\Work\OpenPecha\abhidhamma-rails\1-SOURCES\Translations\Vietnamese\vi-3-tinh_su.md"
IDRE = re.compile(r"\^([\w-]+)\s*$")
segs, buf = {}, []
for line in open(TS, encoding="utf-8"):
    line = line.rstrip("\n")
    if not line.strip():
        continue
    buf.append(line)
    m = IDRE.search(line)
    if m:
        segs[m.group(1)] = buf
        buf = []
for a in sys.argv[1:]:
    if ".." in a:
        pre, rng = a.rsplit("-", 1)[0], a
        lo, hi = a.split("..")
        base = lo.rsplit("-", 1)[0]
        ids = [f"{base}-{i}" for i in range(int(lo.rsplit('-', 1)[1]), int(hi) + 1)]
    else:
        ids = [a]
    for i in ids:
        print(f"[{i}]", " / ".join(segs.get(i, ["<MISSING>"])))
