import sys
L = open(sys.argv[0].replace("view.py", "pair.txt"), encoding="utf-8").read().split("\n")
a, b = int(sys.argv[1]), int(sys.argv[2])
w = int(sys.argv[3]) if len(sys.argv) > 3 else 700
for i in range(a, b + 1):
    p, m = L[2 * i - 2], L[2 * i - 1]
    print(f"{i} P: {p[:w]}\n   M: {m[:w]}")
