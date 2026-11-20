import sys, re
ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
CH = "17-khuddakavatthuvibhango.md"
P = ROOT + r"\AI_translation\pali\pi-2_split_chapters\\" + CH
V = ROOT + r"\AI_translation\vietnamese\pi-2-vietnamese-plain-rails_split_chapters\\" + CH

def lines(p):
    with open(p, encoding="utf-8") as f:
        return [l.rstrip("\n") for l in f if l.strip()]

pl, vl = lines(P), lines(V)
start = int(sys.argv[1]); end = int(sys.argv[2])
print(len(pl), len(vl))
for i in range(start, min(end, len(pl))):
    print(f"[{i}] P: {pl[i]}")
    print(f"[{i}] V: {vl[i] if i < len(vl) else '<<MISSING>>'}")
