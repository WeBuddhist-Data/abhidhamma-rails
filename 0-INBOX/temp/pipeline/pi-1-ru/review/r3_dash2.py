import sys, re, os
base = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\russian\pi-1-russian-plain-rails_split_chapters"
f = sys.argv[1]
lines = open(os.path.join(base, f), encoding="utf-8").read().split("\n")
for i, l in enumerate(lines):
    for m in re.finditer(r", – это", l):
        start = l.rfind("?", 0, m.start())
        seg = l[start + 1:m.start()].strip()
        clause = ("То, что" in seg) or (" ни " in seg) or ("котор" in seg) or ("кроме" in seg) or ("являющ" in seg)
        tag = "CLAUSE?" if clause else "PLAIN"
        idm = re.search(r"\^[\w-]+\s*$", l)
        print(i + 1, idm.group(0) if idm else "", tag, "...", seg[-90:])
