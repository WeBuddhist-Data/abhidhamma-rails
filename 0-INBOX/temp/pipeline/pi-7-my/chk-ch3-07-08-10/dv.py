import re, sys
t = open(sys.argv[1], encoding="utf-8").read().split("\n")
for i in range(0, len(t) - 1, 2):
    a, b = t[i], t[i + 1]
    m = re.match(r"\[(\d+)\]", a)
    why = re.findall(r"(lex: \S+|noun: \S+|np word: \S+|term tail[^\\\\]*|HEADING)", a)
    print(m[1] if m else "?", why[:1], "|", b.strip()[:300])
