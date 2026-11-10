"""List the unique '…pe…'-separated chunks of a Pāli part (helper for build_2-05 / build_3-01)."""
import sys, pathlib, re, collections

p = pathlib.Path(sys.argv[1])
cnt = collections.Counter()
order = []
for line in p.read_text(encoding="utf-8").splitlines():
    if not line.strip() or line.startswith("#"):
        continue
    line = re.sub(r"\s*\^[0-9A-Za-z-]+$", "", line)
    for ch in line.split("…pe…"):
        ch = ch.strip()
        if ch not in cnt:
            order.append(ch)
        cnt[ch] += 1
for ch in order:
    print(f"{cnt[ch]:3d} | {ch}")
