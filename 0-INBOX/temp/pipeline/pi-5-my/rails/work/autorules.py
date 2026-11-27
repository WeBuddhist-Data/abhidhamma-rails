"""work helper (authoring only, not part of the build): for every remaining rails miss (id, keyword) not in SKIP,
propose a segment rule old_core -> new_core (stems of the keyword-map form and of the termbase term), count it in the
current rails segment and test whether the keyword then passes. Prints a review table; the accepted rows are copied
by hand into residual_rules.py."""
import collections
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parents[1]
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE))
sys.dont_write_bytecode = True
import adherence_my as A  # noqa: E402

N = lambda s: unicodedata.normalize("NFC", s)  # noqa: E731
SKIP = set(sys.argv[1].split(",")) if len(sys.argv) > 1 and sys.argv[1] else set()
tb = A.parse_termbase(ROOT / "AI_translation/burmese/pi-5-pali-burmese-termbase-plain.md")
R = A.segments(ROOT / "AI_translation/burmese/pi-5-burmese-plain-rails_split_chapters")
kv = {}
for l in open(ROOT / "AI_translation/burmese/pi-5-keywords-by-reference-pali-burmese-plain.md", encoding="utf-8"):
    m = re.match(r"^\[([^\]]+)\] (.*)$", N(l.strip()))
    if m:
        for x in m.group(2).split(", "):
            if "=" in x:
                k, v = x.split("=", 1)
                kv[(m.group(1), k)] = v


def core(x):
    """the form with only the final ending / particle of its last word stripped (earlier words kept exactly)."""
    ws = [w for w in x.replace(" … ", " ").split(" ") if w]
    return " ".join(ws[:-1] + [A.stem(ws[-1])]) if ws else ""


for l in open(HERE / "adherence-rails.txt", encoding="utf-8"):
    f = N(l).strip().split("\t")
    if len(f) != 3 or not f[0][:1].isdigit() or f[1] in SKIP:
        continue
    i, kw, _ = f
    old = kv.get((i, kw), "")
    terms = tb.get(kw.lower(), [])
    if not old or old.startswith("(") or " … " in old:
        print(f"MANUAL\t{i}\t{kw}\t«{old}»\t{' | '.join(terms)}")
        continue
    seg = R[i]
    oc = core(old)
    best = None
    for t in terms:
        tt = t.replace(" … ", " ")
        if old in seg and (old.endswith(tuple(A.STRIP)) or not tt.endswith(tuple(A.STRIP))):
            o2, n2 = old, tt            # the whole form (keeps the ending relation exact)
        elif old != oc and tt == core(tt):
            continue                    # the old form has an ending the term lacks: no safe stem rule
        else:
            o2, n2 = oc, core(tt)
        n = seg.count(o2)
        ok = n and A.occurs(t, seg.replace(o2, n2))
        if ok and (best is None):
            best = (n2, n, o2)
    if best:
        k = seg.find(best[2])
        print(f"AUTO\t{i}\t{kw}\t{best[2]}\t{best[0]}\t{best[1]}\t…{seg[max(0, k - 14):k + len(best[2]) + 10]}…")
    else:
        print(f"MANUAL\t{i}\t{kw}\t«{old}» core «{oc}» ×{seg.count(oc)}\t{' | '.join(terms)}")
