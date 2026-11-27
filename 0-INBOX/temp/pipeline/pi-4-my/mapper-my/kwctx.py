"""read-only helper: for the keywords of segments, show the Pāli line / word containing each keyword, the aligned
Burmese line (same line index in the segment) and the TERMS value of the containing word.
usage: kwctx.py CH [--unmapped] [SID ...]"""
import sys, re, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.argv, args = sys.argv[:1], sys.argv[1:]
import map_all as M
ch = args[0]; rest = args[1:]
unm = "--unmapped" in rest
sids = [a for a in rest if not a.startswith("--")]
def seglines(path):
    out, buf = {}, []
    for l in path.read_text(encoding="utf-8-sig").splitlines():
        if not l.strip(): continue
        buf.append(re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", l))
        m = M.ID.search(l)
        if m: out[m.group(1)] = buf; buf = []
    return out
PL = seglines(M.PI / f"{ch}.md"); ML = seglines(M.MY / f"{ch}.md")
my, pa, rows = M.load(ch)
W = r"[\wāīūṃṅñṭḍṇḷ]+"
for sid, kws in rows:
    if sids and sid not in sids: continue
    for kw in [k.strip() for k in kws.split(", ")]:
        try:
            v = M.lookup(ch, sid, kw, pa.get(sid, ""), my[sid]); src = M.SRC.get((sid, kw))
        except KeyError:
            v, src = None, None
        if unm and v is not None: continue
        first = kw.split()[0]
        if len(first) > 4 and first[-1] in "aāiīuūoe": first = first[:-1]
        if first.endswith("ṃ"): first = first[:-2] if len(first) > 5 else first
        hit = None
        for i, l in enumerate(PL.get(sid, [])):
            for w in re.findall(W, l):
                if first.lower() in w.lower():
                    hit = (i, w); break
            if hit: break
        if hit:
            i, w = hit
            bl = ML[sid][i] if len(ML[sid]) == len(PL[sid]) else ""
            print(f"{sid}\t{kw}\t= {v} [{src}]\t<{w}> {M.TERMS.get(M.low(w).rstrip('.?'), '')}\t|{bl[:160] if len(PL[sid])>1 else ''}")
        else:
            print(f"{sid}\t{kw}\t= {v} [{src}]\t<not found>")
