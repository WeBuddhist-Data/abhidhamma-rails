"""Identical Pāli line -> identical Hindi line, across 7-01 .. 7-11 (IDs stripped)."""
import re, collections
P = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-6_split_chapters"
H = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters"
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
m = collections.defaultdict(set)
for i in range(1, 12):
    f = "7-%02d-anusayayamaka.md" % i
    try:
        pl = [l for l in open(P + "\\" + f, encoding="utf-8").read().splitlines() if l.strip()]
        hl = [l for l in open(H + "\\" + f, encoding="utf-8").read().splitlines() if l.strip()]
    except FileNotFoundError:
        continue
    for a, b in zip(pl, hl):
        m[ID.sub("", a)].add((ID.sub("", b), f))
bad = 0
for k, v in m.items():
    hs = {h for h, _ in v}
    if len(hs) > 1:
        bad += 1
        if bad <= 6:
            print("PALI:", k[:200])
            for h, f in sorted(v):
                print("   ", f, h[:200])
print("conflicts", bad)
