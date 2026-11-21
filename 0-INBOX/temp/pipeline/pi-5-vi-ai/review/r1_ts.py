import sys, re
# console only: prints the reference segments for the given block IDs (no file output)
# usage: r1_ts.py <id> [<id> ...]   or   r1_ts.py <from_id> : <to_id>
SRC = r"D:\Work\OpenPecha\abhidhamma-rails\1-SOURCES\Translations\Vietnamese\vi-5-tinh_su.md"
lines = open(SRC, encoding="utf8").read().split("\n")
segs, cur = [], []
for l in lines:
    cur.append(l)
    m = re.search(r"\^([\w-]+)\s*$", l)
    if m:
        segs.append((m.group(1), [x for x in cur if x.strip()]))
        cur = []
ids = [a.lstrip("^") for a in sys.argv[1:]]
if len(ids) == 3 and ids[1] == ":":
    on = False
    for i, s in segs:
        if i == ids[0]:
            on = True
        if on:
            print("=== ^" + i); print("\n".join(s))
        if i == ids[2]:
            break
else:
    d = dict(segs)
    for i in ids:
        print("=== ^" + i); print("\n".join(d.get(i, ["(missing)"])))
