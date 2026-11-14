"""List pi-1 termbase terms that differ from what the approved pi-3/4/5 Hindi termbases give the same headword.
Only single-sense headwords on both sides, so that a difference is one of wording, not of meaning split.
Output: cross-book-differences.md (pali | pi-1 term | earlier term (books) | count in pi-1 map)
"""
import collections, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import tb_tool_pi1 as T

TB = T.ROOT / "AI_translation/hindi/pi-1-pali-hindi-termbase-plain.md"
OUT = pathlib.Path(__file__).parent / "cross-book-differences.md"
cnt = T.counts()
pr = collections.defaultdict(lambda: collections.defaultdict(list))
for b, p in T.PRIOR.items():
    for l in p.read_text(encoding="utf-8").splitlines():
        if ": {" in l:
            hw, ss = T.parse(l)
            if len(ss) == 1:
                pr[hw.lower()][ss[0][1][0]].append(b)
            else:
                pr[hw.lower()]["(split)"].append(b)
norm = lambda s: re.sub(r"(ा|ी|े|ों|एँ|ाएँ)(?=\s|$)", "", s)
rows = []
for l in TB.read_text(encoding="utf-8").splitlines():
    hw, ss = T.parse(l)
    if len(ss) != 1 or hw.lower() not in pr or "(split)" in pr[hw.lower()]:
        continue
    t = ss[0][1][0]
    if all(norm(x) != norm(t) for x in pr[hw.lower()]):
        n = sum(cnt.get(hw, {}).values())
        rows.append((n, hw, t, "; ".join(f"{x} (pi-{','.join(map(str, b))})" for x, b in pr[hw.lower()].items())))
rows.sort(key=lambda r: -r[0])
with OUT.open("w", encoding="utf-8", newline="\n") as f:
    f.write("# pi-1 vs pi-3/4/5 Hindi termbases: same headword, different term\n\nuses in pi-1 | pali | pi-1 term | earlier term (books)\n---|---|---|---\n")
    for n, hw, t, p in rows:
        f.write(f"{n} | {hw} | {t} | {p}\n")
print(len(rows), "differences;", sum(r[0] >= 10 for r in rows), "with 10+ uses in pi-1")
for r in rows[:30]:
    print(r[0], r[1], "|", r[2], "|", r[3], sep="  ")
