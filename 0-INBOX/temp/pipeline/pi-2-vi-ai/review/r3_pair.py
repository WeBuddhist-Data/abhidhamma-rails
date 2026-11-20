import sys
base = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
ch = sys.argv[1]
a, b = int(sys.argv[2]), int(sys.argv[3])
P = open(base + r"\pali\pi-2_split_chapters\\" + ch, encoding="utf-8").read().split("\n")
V = open(base + r"\vietnamese\pi-2-vietnamese-plain-rails_split_chapters\\" + ch, encoding="utf-8").read().split("\n")
for i in range(a - 1, min(b, len(P))):
    if not P[i].strip() and not V[i].strip():
        continue
    print(f"{i+1} P: {P[i]}")
    print(f"{i+1} V: {V[i]}")
