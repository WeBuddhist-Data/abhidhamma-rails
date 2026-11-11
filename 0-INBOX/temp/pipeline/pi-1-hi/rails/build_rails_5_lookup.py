"""Print the locked termbase entries for every keyword (Pali side) in chapter 5 and for every word in its text."""
import pathlib, re, sys, collections

R = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation")
tb = {}
for l in (R / "hindi" / "pi-1-pali-hindi-termbase-plain.md").read_text(encoding="utf-8").splitlines():
    w, body = l.split(": {", 1)
    tb[w] = body[:-1]
tbl = {k.lower(): k for k in tb}
src = (R / "pali" / "pi-1_split_chapters" / "5-atthakathakandam.md").read_text(encoding="utf-8")
ids = set(re.findall(r"\^([0-9A-Za-z-]+)\s*$", src, re.M))
seen = collections.Counter()
for l in (R / "pali" / "pi-1-keywords-by-reference-pali-plain.md").read_text(encoding="utf-8").splitlines():
    i, body = l.split("] ", 1)
    if i[1:] not in ids:
        continue
    for k in body.split(", "):
        for kk in k.split(" / "):
            seen[kk] += 1
for w in re.findall(r"[^\W\d_]+", src):
    if w.lower() in tbl:
        seen[tbl[w.lower()]] += 0
for k, n in sorted(seen.items(), key=lambda x: x[0].lower()):
    key = k if k in tb else tbl.get(k.lower())
    print(f"{n:4d} {k} = {tb[key] if key else '(none)'}")
