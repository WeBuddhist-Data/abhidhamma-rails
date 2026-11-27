"""phase 3 scan: uses whose value is NOT the keyword's most frequent value while the segment also has the most frequent
value as a phrase (the candidates for alignment). usage: scan_minor.py OUT.tsv"""
import sys, pathlib, collections
D = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(D))
import map5_rules as R
own = {sid: ch for ch in R.CHAPTERS for sid in R.pali(ch)}
uses = collections.defaultdict(list)
for f in sorted(D.glob("*.mapped.md")):
    for l in f.read_text(encoding="utf-8").splitlines():
        sid, rest = l[1:].split("] ", 1)
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            uses[R.low(k)].append((sid, k, v))
out = []
for k, lst in sorted(uses.items(), key=lambda x: (x[0].lower(), x[0])):
    vals = collections.Counter(v for _, _, v in lst)
    if len(vals) < 2:
        continue
    top = vals.most_common(1)[0][0]
    if top == R.NONE:
        continue
    for sid, kk, v in lst:
        if v == top:
            continue
        my = R.burmese(own[sid])[sid]
        for part in sorted(v.split(" … "), key=len, reverse=True):   # the top value must stand OUTSIDE this
            if part != R.NONE and top not in part:                       # use's own words (not «ရဟန္တာ» of
                continue                                                 # «ရဟန္တာ အဖြစ်»)
            my = my.replace(part, " ¶ ") if part != R.NONE else my
        if R.presence(top, my)[0] and R.phrase_ok(top, my):
            out.append("\t".join([k, own[sid], sid, kk, v, top, f"{vals[v]}/{vals[top]}"]))
pathlib.Path(sys.argv[1]).write_text("\n".join(out) + "\n", encoding="utf-8")
print("minority uses alignable to the top value", len(out), "keywords", len({o.split(chr(9))[0] for o in out}))
