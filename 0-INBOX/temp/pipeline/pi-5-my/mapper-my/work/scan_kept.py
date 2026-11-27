"""phase 3: the kept differences of the after-scan, one row per keyword with more than one value, with a category:
construction  the same members, glued with the text's particle in one segment and separated « … » / in another order
              in another (rule 1 / rule 10, Q3 / G2, mechanic 2): each segment's own construction
none          one value is (no direct equivalent) in some segments (pi-2 decision 4 one word one member, M2 Roman
              variant, Q7 relative pronoun, one Burmese verb for two keywords)
form          the values share their word and differ in ending / spacing / an added word (the text's form in each
              segment: participle vs perfect, noun vs attributive, the text's spacing)
sense         different words: a different sense or construction of the keyword (one sense per segment, the first in
              the Pāli) or the text's different word for the same sense (text inconsistency, §A)
reviewed      the column «minority alignable» > 0: the top value also stands in that segment; reviewed by hand
              (phase-3 notes §B), kept for the reason of the category
usage: scan_kept.py OUT.tsv"""
import sys, re, pathlib, collections
W = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(W.parent))
import map5_rules as R
minor = collections.Counter(l.split("\t")[0] for l in (W / "scan-minor.tsv").read_text(encoding="utf-8").splitlines() if l)
PART = re.compile(r"(ကို|သည်|၏|၌|နှင့်|တို့|ဖြင့်|မှ|သို့)(?= |$)")
def norm(v):
    return sorted(PART.sub("", p).replace(" ", "") for p in re.split(r" … | ", v))
def cat(vals):
    if R.NONE in vals:
        return "none"
    ns = {tuple(norm(v)) for v in vals}
    if len(ns) == 1 or len({"".join(sorted(n)) for n in ns}) == 1:
        return "construction"
    cores = [v.replace(" … ", " ").split()[0][:3] for v in vals]
    if len(set(cores)) == 1:
        return "form"
    return "sense"
rows, cnt = [], collections.Counter()
for l in (W / "scan-after.tsv").read_text(encoding="utf-8").splitlines():
    k, n, rest = l.split("\t")
    vals = [re.sub(r" \(\d+;[^)]*\)$", "", x) for x in rest.split(" | ")]
    c = cat(vals)
    cnt[c] += 1
    rows.append("\t".join([k, c, str(minor.get(k, 0)), rest]))
(W / sys.argv[1]).write_text("keyword\tcategory\tminority uses alignable (reviewed)\tvalues (uses; chapters)\n"
                             + "\n".join(rows) + "\n", encoding="utf-8")
print(dict(cnt), "reviewed", sum(1 for r in rows if r.split("\t")[2] != "0"))
