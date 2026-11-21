import sys, re
base = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\vietnamese"
files = {"pi1": base + r"\pi-1-vietnamese-plain.md", "pi2": base + r"\pi-2-vietnamese-plain.md"}
texts = {k: open(v, encoding="utf-8").read() for k, v in files.items()}
phrases = [l.strip() for l in open(sys.argv[1], encoding="utf-8") if l.strip()]
for p in phrases:
    row = [p]
    for k, t in texts.items():
        row.append(f"{k}={len(re.findall(re.escape(p), t, flags=re.I))}")
    print(" | ".join(row))
