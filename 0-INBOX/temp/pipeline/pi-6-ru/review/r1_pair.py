import sys, re
base = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
ch = sys.argv[1]
start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
end = int(sys.argv[3]) if len(sys.argv) > 3 else 10**9
p = open(base + r"\pali\pi-6_split_chapters\\" + ch, encoding="utf-8").read().split("\n")
r = open(base + r"\russian\pi-6-russian-plain-rails_split_chapters\\" + ch, encoding="utf-8").read().split("\n")
print("lines", len(p), len(r))
for i, (a, b) in enumerate(zip(p, r)):
    if i < start or i >= end:
        continue
    if not a.strip() and not b.strip():
        continue
    print(f"{i+1}P: {a}")
    print(f"{i+1}R: {b}")
