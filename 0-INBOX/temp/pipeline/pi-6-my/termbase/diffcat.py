"""Categorise the senses whose final term differs from the matched locked term (pi12345-match.tsv + the assembled termbase).
usage: diffcat.py  -> diff-categories.txt"""
import pathlib, collections
H = pathlib.Path(__file__).resolve().parent; B = H.parents[4]
T = {}
for line in (B / "AI_translation/burmese/pi-6-pali-burmese-termbase-plain.md").read_text(encoding="utf-8").splitlines():
    hw, body = line.split(": {", 1)
    for i, s in enumerate(body[:-1].split("; ")): T[f"{hw}|{i}"] = s.rsplit(": ", 1)[1]
dec = set()
for l in (H / "decisions-A.tsv").read_text(encoding="utf-8").splitlines():
    if l and not l.startswith("#"): dec.add(l.split("\t")[0])
cats = collections.defaultdict(list)
for r in (H / "pi12345-match.tsv").read_text(encoding="utf-8").splitlines():
    cat, key, cands, lt, how, src, tag = r.split("\t")
    if not src or T[key] == lt: continue
    if how == "TAGDIFF": c = "other sense (TAGDIFF)"
    elif cat.endswith("ABSENT"): c = "locked term absent from the pi-6 text, pi-6 form kept" if key not in dec else "locked term absent, decided (multi / family)"
    else: c = "locked term present, departure decided and explained" if key in dec else "locked term present, pi-6 form kept (explained in part 5)"
    cats[c].append(f"{key}: {T[key]}  | {src.split()[0]} {lt}")
with open(H / "diff-categories.txt", "w", encoding="utf-8") as f:
    for c, v in cats.items():
        f.write(f"## {c} ({len(v)})\n" + "\n".join(v) + "\n\n")
print({c: len(v) for c, v in cats.items()})
