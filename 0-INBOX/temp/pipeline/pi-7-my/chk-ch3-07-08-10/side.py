import sys
p=[l for l in open(sys.argv[1],encoding='utf-8-sig').read().splitlines() if l.strip()]
m=[l for l in open(sys.argv[2],encoding='utf-8').read().splitlines() if l.strip()]
a, b = int(sys.argv[3]), int(sys.argv[4])
for i in range(a-1, min(b, len(p))):
    if p[i].startswith("#"): continue
    print(f"{i+1} P: {p[i][:int(sys.argv[5]) if len(sys.argv)>5 else 400]}\n   M: {m[i][:int(sys.argv[5]) if len(sys.argv)>5 else 400]}")
