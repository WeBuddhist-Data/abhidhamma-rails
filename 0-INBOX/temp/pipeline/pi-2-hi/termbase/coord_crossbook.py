"""Coordinator: list pi-2 termbase senses whose term differs from the term the approved pi-1/3/4/5 Hindi termbases give the
same Pāli headword in the same meaning. Same meaning = the only sense on both sides, or the prior sense whose English
tag is closest (difflib ratio >= 0.6). A rough Hindi normalisation (final vowel/oblique, gap marker) hides pure
grammatical variants. Output: cross-book-differences.md, grouped by the pi-2 map count (>= 10 uses first).
"""
import collections, difflib, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import tb_tool_pi2 as T

HERE = pathlib.Path(__file__).parent
TB = T.ROOT / "AI_translation/hindi/pi-2-pali-hindi-termbase-plain.md"
OUT = HERE / "cross-book-differences.md"


def norm(s):
    s = s.replace(" … ", " ").replace("…", "")
    s = re.sub(r"(ा|ी|े|ों|एँ|ाएँ|ओं|ें)(?=\s|$)", "", s)
    return re.sub(r"\s+", " ", s).strip()


def sim(a, b):
    a, b = (re.sub(r"\([^)]*\)", "", x).strip().lower() for x in (a, b))
    return difflib.SequenceMatcher(None, a, b).ratio()


prior = collections.defaultdict(lambda: collections.defaultdict(list))   # hw -> book -> [(tag, term)]
for b, p in T.PRIOR.items():
    for l in p.read_text(encoding="utf-8").splitlines():
        if ": {" in l:
            hw, ss = T.parse(l)
            for tag, c in ss:
                prior[hw.lower()][b].append((tag, c[0]))
cnt = T.counts()
dec = T.decisions()
rows = []
for l in TB.read_text(encoding="utf-8").splitlines():
    hw, ss = T.parse(l)
    if hw.lower() not in prior:
        continue
    for i, (tag, c) in enumerate(ss):
        t = c[0]
        diff = collections.defaultdict(list); ptags = {}
        same = False
        for b, ps in prior[hw.lower()].items():
            if len(ss) == 1 and len(ps) == 1:
                ptag, pt = ps[0]
                if sim(ptag, tag) < 0.3:   # one sense each but plainly a different meaning (e.g. 'expert' vs 'wholesome')
                    continue
            else:
                ptag, pt = max(ps, key=lambda x: sim(x[0], tag))
                # mutual best: this pi-2 sense must also be the closest pi-2 sense to that prior sense
                best_here = max(range(len(ss)), key=lambda j: sim(ptag, ss[j][0]))
                if best_here != i or sim(ptag, tag) < 0.6:
                    continue
            if norm(pt) == norm(t):
                same = True
            else:
                diff[pt].append(b); ptags[pt] = ptag
        if diff:
            n = sum(cnt.get(hw, {}).values())
            src = dec.get(f"{hw}|{i}", ("", "-"))[1]
            rows.append((n, hw, tag, t, "; ".join(f"{x} (pi-{','.join(map(str, bs))}: {ptags[x][:45]})" for x, bs in diff.items()),
                         "partly" if same else "", src))
rows.sort(key=lambda r: (-r[0], r[1]))
hi = [r for r in rows if r[0] >= 10]
lo = [r for r in rows if r[0] < 10]
with OUT.open("w", encoding="utf-8", newline="\n") as f:
    f.write("# pi-2 vs pi-1/3/4/5 Hindi termbases: same Pāli word and meaning, different term\n\n"
            "Report only: the pi-2 term is kept; the user decides. 'uses' = pi-2 map count; 'also same in' = another prior "
            "book agrees with pi-2; 'pi-2 source' = decision file (or '-' for the single candidate).\n"
            f"\n{len(rows)} differences ({len(hi)} with 10+ uses in pi-2).\n")
    for title, rs in (("## High-frequency (10+ uses in pi-2)", hi), ("## Lower-frequency", lo)):
        f.write(f"\n{title}\n\nuses | pali | sense | pi-2 | prior (books) | also same in another book | pi-2 source\n"
                "---|---|---|---|---|---|---\n")
        for n, hw, tag, t, p, s, src in rs:
            f.write(f"{n} | {hw} | {tag} | {t} | {p} | {s} | {src}\n")
print(len(rows), "differences;", len(hi), "with 10+ uses")
for r in rows[:45]:
    print(r[0], r[1], "|", r[3], "|", r[4], "|", r[5], r[6], sep="  ")

