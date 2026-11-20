import sys, re
# usage: r3_pi1.py <regex> [max] [p|v]  -> prints matching pi-1 line and the corresponding line of the other language (same block, same offset)
P = open(r"D:\Work\OpenPecha\abhidhamma-rails\1-SOURCES\Text\pi-1.md", encoding="utf-8").read().split("\n")
V = open(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\vietnamese\pi-1-vietnamese-plain.md", encoding="utf-8").read().split("\n")
pat = re.compile(sys.argv[1])
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 3
mode = sys.argv[3] if len(sys.argv) > 3 else "p"
src, other = (P, V) if mode == "p" else (V, P)
idx = {}
for k, ol in enumerate(other):
    m = re.search(r"\^([\w-]+)\s*$", ol)
    if m:
        idx[m.group(1)] = k
n = 0
for i, l in enumerate(src):
    if pat.search(l):
        j = i
        while j < len(src) and not re.search(r"\^[\w-]+\s*$", src[j]):
            j += 1
        m = re.search(r"\^([\w-]+)\s*$", src[j]) if j < len(src) else None
        bid = m.group(1) if m else None
        print("==", bid, "line", i + 1)
        print("S:", l[:2500])
        if bid in idx:
            k = idx[bid] - (j - i)
            print("O:", other[k][:2500])
        n += 1
        if n >= mx:
            break
