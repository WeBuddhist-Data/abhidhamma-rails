import re, sys
# Print Tinh Su blocks for given IDs to the console only (never written to disk).
T = r"1-SOURCES\Translations\Vietnamese\vi-2-tinh_su.md"
txt = open(T, encoding="utf-8").read()
lines = txt.split("\n")
blocks = {}
cur = []
for l in lines:
    cur.append(l)
    m = re.search(r"\^(\S+)\s*$", l)
    if m:
        blocks.setdefault(m.group(1), "\n".join(x for x in cur if x.strip()))
        cur = []
ids = sys.argv[1:]
maxc = 2500
for i in ids:
    if i.startswith("max="):
        maxc = int(i[4:]); continue
    b = blocks.get(i)
    print(f"=== {i} ===")
    print(b[:maxc] if b else "(missing)")
