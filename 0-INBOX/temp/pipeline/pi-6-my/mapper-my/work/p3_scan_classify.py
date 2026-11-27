"""phase 3 consistency scan, classification: for every keyword (first letter case-insensitive) with more than one
value over the 44 *.mapped.md (copied from pi-5-my/mapper-my/work/scan_classify.py), every use whose segment ALSO has another of the keyword's values as a phrase
(presence + phrase_ok) is «alignable»; a keyword none of whose uses is alignable has, in every segment, only its own
value: a text / sense difference (the translation uses that word there).
usage: scan_classify.py OUT.tsv  (keyword, n values, alignable uses, values with counts, alignable detail)"""
import sys, pathlib, collections
D = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(D))
import map6_rules as R
own = {sid: ch for ch in R.CHAPTERS for sid in R.pali(ch)}
uses = collections.defaultdict(list)
for f in sorted(D.glob("*.mapped.md")):
    for l in f.read_text(encoding="utf-8").splitlines():
        sid, rest = l[1:].split("] ", 1)
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            uses[R.low(k)].append((sid, k, v))
rows = []
for k, lst in sorted(uses.items(), key=lambda x: (x[0].lower(), x[0])):
    vals = collections.Counter(v for _, _, v in lst)
    if len(vals) < 2:
        continue
    al = []
    for sid, kk, v in lst:
        my = R.burmese(own[sid])[sid]
        others = [w for w in vals if w != v and w != R.NONE and R.presence(w, my)[0] and R.phrase_ok(w, my)]
        if others:
            al.append(f"{sid}:{v}→{'|'.join(others)}")
    rows.append("\t".join([k, str(len(vals)), str(len(al)), " | ".join(f"{v} ({c})" for v, c in vals.most_common()),
                           " ; ".join(al[:12])]))
pathlib.Path(sys.argv[1]).write_text("\n".join(rows) + "\n", encoding="utf-8")
n_al = sum(1 for r in rows if r.split("\t")[2] != "0")
print("keywords >1 value", len(rows), "with alignable uses", n_al, "alignable uses",
      sum(int(r.split("\t")[2]) for r in rows))

