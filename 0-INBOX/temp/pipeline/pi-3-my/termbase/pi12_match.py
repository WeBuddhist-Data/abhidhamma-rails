"""pi-3 Burmese termbase helper: compare every pi-3 sense with the LOCKED pi-2 termbase, then pi-1's (same headword, same sense).
usage: pi12_match.py [category ...]   categories: MULTI_IN MULTI_OUT MULTI_OUT_ABSENT MULTI_NEW SINGLE_DIFF SINGLE_DIFF_ABSENT SINGLE_SAME SINGLE_NEW TAGDIFF
Writes pi12-match.tsv next to this script. Sense match: exact sense tag (pi-2, then pi-1); else, when
both files have one sense for the headword, that sense (TAGDIFF); else case-insensitive headword with exact tag.
'present' = the locked term (… as a gap) occurs in the pi-3 Burmese text."""
import re, sys, pathlib, collections
B = pathlib.Path(__file__).resolve().parents[5]
S3 = B / "AI_translation/burmese/pi-3-pali-word-burmese-senses-plain.md"
T2 = B / "AI_translation/burmese/pi-2-pali-burmese-termbase-plain.md"
T1 = B / "AI_translation/burmese/pi-1-pali-burmese-termbase-plain.md"
ZS = B / "AI_translation/burmese/pi-3-burmese-plain-zeroshot.md"
def parse(p):
    d = collections.OrderedDict()
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.strip(): continue
        hw, body = line.split(": {", 1)
        d[hw] = [tuple(s.rsplit(": ", 1)) for s in body[:-1].split("; ")]
    return d
s3 = parse(S3); locked = [("pi-2", parse(T2)), ("pi-1", parse(T1))]
low = {n: collections.defaultdict(list) for n, _ in locked}
for n, t in locked:
    for hw in t: low[n][hw.lower()].append(hw)
text = ZS.read_text(encoding="utf-8")
_pc = {}
def present(term):
    if term not in _pc:
        rx = r"\s*.{0,80}?\s*".join(re.escape(x.strip()) for x in term.split("…"))
        _pc[term] = re.search(rx, text) is not None
    return _pc[term]
def find(hw, tag, nsen):
    for n, t in locked:
        for h1 in [hw] + [h for h in low[n].get(hw.lower(), []) if h != hw]:
            if h1 not in t: continue
            for j, (tg1, tm1) in enumerate(t[h1]):
                if tg1 == tag: return (n, h1, j, tm1, "tag" if h1 == hw else "tag-ci")
    for n, t in locked:
        if hw in t and len(t[hw]) == 1 and nsen == 1:
            return (n, hw, 0, t[hw][0][1], "TAGDIFF")
    return None
rows = []
for hw, ss in s3.items():
    for i, (tag, c) in enumerate(ss):
        cl = [x.strip() for x in c.split(" / ")]
        p = find(hw, tag, len(ss))
        if not p:
            cat = "MULTI_NEW" if len(cl) > 1 else "SINGLE_NEW"
        else:
            tm = p[3]
            if len(cl) > 1: cat = "MULTI_IN" if tm in cl else ("MULTI_OUT" if present(tm) else "MULTI_OUT_ABSENT")
            else: cat = "SINGLE_SAME" if tm == cl[0] else ("SINGLE_DIFF" if present(tm) else "SINGLE_DIFF_ABSENT")
        rows.append((cat, f"{hw}|{i}", " / ".join(cl), p[3] if p else "", p[4] if p else "", f"{p[0]} {p[1]}|{p[2]}" if p else "", tag))
with open(pathlib.Path(__file__).with_name("pi12-match.tsv"), "w", encoding="utf-8") as f:
    for r in rows: f.write("\t".join(r) + "\n")
cnt = collections.Counter(r[0] for r in rows); print(dict(cnt), "TAGDIFF", sum(r[4] == "TAGDIFF" for r in rows),
      "by book", collections.Counter(r[5].split()[0] for r in rows if r[5]))
want = set(sys.argv[1:])
for r in rows:
    if r[0] in want or ("TAGDIFF" in want and r[4] == "TAGDIFF"):
        print(f"{r[0]:18s} {r[1]}  cands: {r[2]}  | locked: {r[3]} ({r[4]} {r[5]})  [{r[6][:90]}]")
