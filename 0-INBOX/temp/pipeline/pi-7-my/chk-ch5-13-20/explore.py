import re, pathlib, collections, sys
P = pathlib.Path(__file__).resolve().parents[5] / "AI_translation/pali/pi-7_split_chapters"
names = sorted(p.name for p in P.iterdir() if p.name[:4] in ("5-13","5-14","5-15","5-16","5-17","5-18","5-19","5-20"))
H = collections.Counter(); N = collections.Counter()
for n in names:
    t = (P/n).read_text(encoding="utf-8-sig")
    for l in t.splitlines():
        if l.startswith("#"):
            H[re.sub(r" \^[\d-]+$","",l).lstrip("# ")] += 1
        else:
            for m in re.finditer(r"\([^()]*\)", l):
                if not re.fullmatch(r"\(\d+\)", m[0]): N[m[0]] += 1
mode = sys.argv[1]
for k,v in (H if mode=="h" else N).most_common():
    print(v, k)
