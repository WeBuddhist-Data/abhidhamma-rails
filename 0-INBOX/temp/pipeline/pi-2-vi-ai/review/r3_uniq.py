import sys, re
# print only pairs whose Pali line (block id stripped) has not been seen; report if a repeated Pali line got a different Vietnamese
base = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
ch = sys.argv[1]
a, b = int(sys.argv[2]), int(sys.argv[3])
P = open(base + r"\pali\pi-2_split_chapters\\" + ch, encoding="utf-8").read().split("\n")
V = open(base + r"\vietnamese\pi-2-vietnamese-plain-rails_split_chapters\\" + ch, encoding="utf-8").read().split("\n")
strip = lambda s: re.sub(r"\s*\^[\w-]+\s*$", "", s).strip()
seen = {}
for i in range(len(P)):
    p, v = strip(P[i]), strip(V[i])
    if not p:
        continue
    if p in seen:
        if seen[p][0] != v and a - 1 <= i < b:
            print(f"!! DIFF for repeated pali at {i+1} (first {seen[p][1]})")
            print("   V now :", v[:600])
            print("   V first:", seen[p][0][:600])
        continue
    seen[p] = (v, i + 1)
    if a - 1 <= i < b:
        print(f"{i+1} P: {P[i]}")
        print(f"{i+1} V: {V[i]}")
