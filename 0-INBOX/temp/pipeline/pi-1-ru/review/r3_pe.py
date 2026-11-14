import os, re
B = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
for f in ["3-01-rupakandam.md", "3-02-rupakandam.md", "3-03-rupakandam.md"]:
    P = open(os.path.join(B, "pali", "pi-1_split_chapters", f), encoding="utf-8").read().split("\n")
    R = open(os.path.join(B, "russian", "pi-1-russian-plain-rails_split_chapters", f), encoding="utf-8").read().split("\n")
    for i, (p, r) in enumerate(zip(P, R)):
        a = p.count("…pe…"); b = r.count("…")
        if a != b:
            print(f, i + 1, "pe", a, b)
        qa = p.count("?"); qb = r.count("?")
        if qa != qb:
            print(f, i + 1, "?", qa, qb)
        ida = re.findall(r"\^[\w-]+", p); idb = re.findall(r"\^[\w-]+", r)
        if ida != idb:
            print(f, i + 1, "id", ida, idb)
