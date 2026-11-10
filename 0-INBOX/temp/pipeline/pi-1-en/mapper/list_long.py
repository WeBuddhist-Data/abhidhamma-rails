import collections, sys
pairs = collections.Counter()
for line in open(sys.argv[1], encoding="utf-8-sig"):
    i, body = line.rstrip("\n").split("] ", 1)
    for p in body.split(", "):
        pali, en = p.rsplit("=", 1)
        if pali != "(no direct equivalent)" and any(len(q.split()) >= 4 for q in pali.split(" / ")):
            pairs[(pali, en.lower())] += 1
for (p, e), n in sorted(pairs.items(), key=lambda x: (-len(x[0][0].split()), x[0])):
    print(f"{n:3} | {e} | {p}")
print(len(pairs), "distinct")