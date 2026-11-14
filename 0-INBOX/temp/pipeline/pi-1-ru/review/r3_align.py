import sys
base = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
ch = sys.argv[1]
start = int(sys.argv[2]); end = int(sys.argv[3])
P = open(base + r"\pali\pi-1_split_chapters\\" + ch, encoding="utf-8").read().split("\n")
R = open(base + r"\russian\pi-1-russian-plain-rails_split_chapters\\" + ch, encoding="utf-8").read().split("\n")
print(len(P), len(R))
for i in range(start - 1, min(end, len(P))):
    if not P[i].strip() and not R[i].strip():
        continue
    print(f"[{i+1}] P: {P[i]}")
    print(f"[{i+1}] R: {R[i]}")
