# r3 helper: print reference-translation segments by block ID to the console only (never writes files)
import re, sys
path = r"D:\Work\OpenPecha\abhidhamma-rails\1-SOURCES\Translations\Vietnamese\vi-4-tinh_su.md"
t = open(path, encoding="utf-8").read()
blocks = re.split(r"\n\s*\n", t)
idx = {}
for b in blocks:
    m = re.search(r"\^([\w-]+)\s*$", b.strip())
    if m:
        idx[m.group(1)] = b.strip()
lo, hi = int(sys.argv[1]), int(sys.argv[2])
extra = sys.argv[3:]
for k in extra:
    print("=== ^" + k); print(idx.get(k, "(missing)")); print()
for n in range(lo, hi + 1):
    k = "4-%d" % n
    print("=== ^" + k); print(idx.get(k, "(missing)")); print()
