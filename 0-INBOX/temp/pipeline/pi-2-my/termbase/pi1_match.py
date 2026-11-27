"""pi-2 Burmese termbase helper: compare every pi-2 sense with pi-1's LOCKED termbase (same headword, same sense).
usage: pi1_match.py [category ...]   categories: MULTI_IN MULTI_OUT MULTI_NEW SINGLE_DIFF SINGLE_DIFF_ABSENT TAGDIFF
Writes pi1-match.tsv (all senses) next to this script and prints the requested categories.
Sense match: exact sense tag; else, when both files have one sense for the headword, that sense (TAGDIFF noted);
else case-insensitive headword with exact tag. 'present' = the pi-1 term (… as a gap) occurs in the pi-2 Burmese text."""
import re, sys, pathlib, collections
B = pathlib.Path(__file__).resolve().parents[5]
S2 = B / "AI_translation/burmese/pi-2-pali-word-burmese-senses-plain.md"
T1 = B / "AI_translation/burmese/pi-1-pali-burmese-termbase-plain.md"
ZS = B / "AI_translation/burmese/pi-2-burmese-plain-zeroshot.md"
def parse(p):
    d = collections.OrderedDict()
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.strip(): continue
        hw, body = line.split(": {", 1)
        d[hw] = [tuple(s.rsplit(": ", 1)) for s in body[:-1].split("; ")]
    return d
s2, t1 = parse(S2), parse(T1)
t1l = collections.defaultdict(list)
for hw, ss in t1.items(): t1l[hw.lower()].append(hw)
text = ZS.read_text(encoding="utf-8")
_pc = {}
def present(term):
    if term not in _pc:
        rx = r"\s*.{0,80}?\s*".join(re.escape(x.strip()) for x in term.split("…"))
        _pc[term] = re.search(rx, text) is not None
    return _pc[term]
rows = []
for hw, ss in s2.items():
    for i, (tag, c) in enumerate(ss):
        cl = [x.strip() for x in c.split(" / ")]
        p1, how = None, ""
        cands1 = [hw] + [h for h in t1l.get(hw.lower(), []) if h != hw]
        for h1 in cands1:
            if h1 not in t1: continue
            for j, (tg1, tm1) in enumerate(t1[h1]):
                if tg1 == tag: p1, how = (h1, j, tm1), "tag" if h1 == hw else "tag-ci"; break
            if p1: break
        if not p1 and hw in t1 and len(t1[hw]) == 1 and len(ss) == 1:
            p1, how = (hw, 0, t1[hw][0][1]), "TAGDIFF"
        if not p1:
            cat = "MULTI_NEW" if len(cl) > 1 else "SINGLE_NEW"
        else:
            tm = p1[2]
            if len(cl) > 1: cat = "MULTI_IN" if tm in cl else "MULTI_OUT"
            else: cat = "SINGLE_SAME" if tm == cl[0] else ("SINGLE_DIFF" if present(tm) else "SINGLE_DIFF_ABSENT")
            if cat == "MULTI_OUT" and not present(tm): cat = "MULTI_OUT_ABSENT"
        rows.append((cat, f"{hw}|{i}", " / ".join(cl), p1[2] if p1 else "", how, f"{p1[0]}|{p1[1]}" if p1 else "", tag))
with open(pathlib.Path(__file__).with_name("pi1-match.tsv"), "w", encoding="utf-8") as f:
    for r in rows: f.write("\t".join(r) + "\n")
cnt = collections.Counter(r[0] for r in rows); print(dict(cnt), "TAGDIFF", sum(r[4] == "TAGDIFF" for r in rows))
want = set(sys.argv[1:])
for r in rows:
    if r[0] in want or ("TAGDIFF" in want and r[4] == "TAGDIFF"):
        print(f"{r[0]:18s} {r[1]}  cands: {r[2]}  | pi1: {r[3]} ({r[4]} {r[5]})  [{r[6][:90]}]")
