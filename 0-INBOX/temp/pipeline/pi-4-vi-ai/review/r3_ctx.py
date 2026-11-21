# r3 helper: print short contexts of patterns in one file (console only)
import re, sys
path = sys.argv[1]
width = int(sys.argv[2])
t = open(path, encoding="utf-8").read()
for pat in sys.argv[3:]:
    print("##### PATTERN:", pat)
    for m in list(re.finditer(pat, t))[:4]:
        s = max(0, m.start() - width); e = min(len(t), m.end() + width)
        print("   ...", t[s:e].replace("\n", " | "), "...")
