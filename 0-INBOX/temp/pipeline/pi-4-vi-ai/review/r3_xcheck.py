# r3 helper: print short contexts of patterns in the approved pi-1/2/3 Vietnamese (console only)
import re, sys
base = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\vietnamese"
files = ["pi-1-vietnamese-plain.md", "pi-2-vietnamese-plain.md", "pi-3-vietnamese-plain.md"]
texts = {f: open(base + "\\" + f, encoding="utf-8").read() for f in files}
maxhits = int(sys.argv[1])
width = int(sys.argv[2])
for pat in sys.argv[3:]:
    print("##### PATTERN:", pat)
    for f in files:
        t = texts[f]
        hits = list(re.finditer(pat, t))
        print("  --", f, "hits:", len(hits))
        for m in hits[:maxhits]:
            s = max(0, m.start() - width); e = min(len(t), m.end() + width)
            snippet = t[s:e].replace("\n", " | ")
            print("    ...", snippet, "...")
