import sys
BASE = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
ch, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
withen = len(sys.argv) > 4

def lines(p):
    with open(p, encoding="utf-8") as f:
        return [l.rstrip() for l in f.read().split("\n") if l.strip()]

P = lines(f"{BASE}\\pali\\pi-2_split_chapters\\{ch}.md")
H = lines(f"{BASE}\\hindi\\pi-2-hindi-plain-rails_split_chapters\\{ch}.md")
E = lines(f"{BASE}\\english\\pi-2-english-plain-zeroshot_split_chapters\\{ch}.md") if withen else None
for i in range(a, min(b, len(P)) + 1):
    print(f"[{i}] P: {P[i-1]}")
    if E:
        print(f"[{i}] E: {E[i-1]}")
    print(f"[{i}] H: {H[i-1]}")
