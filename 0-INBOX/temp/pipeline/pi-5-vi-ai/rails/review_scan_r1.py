import sys, re
B = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\vietnamese\pi-5-vietnamese-plain-rails_split_chapters"
pats = sys.argv[1:]
for f in ["preamble.md", "1-puggalakatha.md", "2-parihanikatha.md"]:
    t = open(B + "\\" + f, encoding="utf-8").read()
    segs = t.split("\n\n")
    for p in pats:
        for s in segs:
            m = re.search(r"\^(\S+)\s*$", s.strip())
            sid = m.group(1) if m else "?"
            for mm in re.finditer(p, s):
                a = max(0, mm.start() - 80)
                print(f"{f} ^{sid} [{p}]: ...{s[a:mm.end()+80]}...".replace("\n", " / "))
