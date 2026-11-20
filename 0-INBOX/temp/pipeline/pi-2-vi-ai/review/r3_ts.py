import sys
# console-only viewer of the reference translation by line range; never writes anything
L = open(r"D:\Work\OpenPecha\abhidhamma-rails\1-SOURCES\Translations\Vietnamese\vi-2-tinh_su.md", encoding="utf-8").read().split("\n")
a, b = int(sys.argv[1]), int(sys.argv[2])
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 100000
if len(sys.argv) > 4 and sys.argv[4] == "size":
    print(sum(len(x) for x in L[a - 1:b]))
    sys.exit()
for i in range(a - 1, min(b, len(L))):
    if L[i].strip():
        print(i + 1, L[i][:mx])
