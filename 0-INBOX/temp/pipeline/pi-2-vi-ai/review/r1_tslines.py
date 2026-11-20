import sys
# Print a line range of the Tinh Su file to the console only (never written to disk).
T = r"1-SOURCES\Translations\Vietnamese\vi-2-tinh_su.md"
lines = open(T, encoding="utf-8").read().split("\n")
a, b = int(sys.argv[1]), int(sys.argv[2])
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 100000
for i in range(a - 1, min(b, len(lines))):
    l = lines[i]
    if l.strip() and not l.startswith("![["):
        print(i + 1, l[:mx])
