"""Print aligned non-empty lines of two files (Pāli | Hindi), optional line range.
usage: python -I -B -X utf8 pairs_4-16_5-04.py <pali> <hindi> [start] [end]"""
import sys

a = [l for l in open(sys.argv[1], encoding="utf-8").read().splitlines() if l.strip()]
b = [l for l in open(sys.argv[2], encoding="utf-8").read().splitlines() if l.strip()]
s = int(sys.argv[3]) if len(sys.argv) > 3 else 1
e = int(sys.argv[4]) if len(sys.argv) > 4 else len(a)
print(len(a), len(b))
for i in range(s - 1, min(e, len(a))):
    print(f"{i + 1}: {a[i]}\n    {b[i] if i < len(b) else '-'}")
