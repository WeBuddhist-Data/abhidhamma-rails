"""pi-6 Hindi termbase helper (brief: ../hi-termbase-brief.md). Prints only.

usage: python -I -X utf8 tb6_cross.py scan            all pi-6 senses whose final term differs from a pi-1..5 term
                                                      for the same headword (key, uses, pi-6 term, prior)
       python -I -X utf8 tb6_cross.py stem            the same by stem (case endings, -ti, enclitics stripped),
                                                      rows not already in `scan`
       python -I -X utf8 tb6_cross.py enc             enclitic/quotative forms whose term differs from the base form
The cross-book report (cross-book-differences.md) is curated by hand from `scan` and `stem` (same meaning only).
"""
import collections, pathlib, re, sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
import tb_tool_pi6 as T  # noqa: E402

BOOKS = (1, 2, 3, 4, 5)


def final():
    dec = T.decisions()
    rows = []
    for hw, ss in T.senses():
        for i, (tag, c) in enumerate(ss):
            k = f"{hw}|{i}"
            rows.append((k, hw, tag, dec[k][0] if k in dec else c[0], c, k in dec))
    return rows


def prior_by_book():
    d = collections.defaultdict(list)
    for b in BOOKS:
        for l in T.PRIOR[b].read_text(encoding="utf-8").splitlines():
            if ": {" in l:
                hw, ss = T.parse(l)
                for tag, c in ss:
                    d[hw.lower()].append((b, tag, c[0]))
    return d


END = re.compile(r"(?:nti|ti|ñceva|ñca|mpi|pi|yeva)$")
CASE = re.compile(r"(?:ānaṃ|īnaṃ|ūnaṃ|assa|āya|āyaṃ|uyā|iyā|ehi|ebhi|esu|āsu|ena|āni|āni|uyo|iyo|aṃ|ā|o|e|ṃ|ī|ū|u|i|a|uṃ|iṃ)$")


def stem(hw):
    out = []
    for w in hw.lower().split():
        w = END.sub("", w)
        w2 = CASE.sub("", w)
        out.append(w2 if len(w2) >= 3 else w)
    return " ".join(out)


def prior_by_stem():
    d = collections.defaultdict(list)
    for hw, v in prior_by_book().items():
        for b, t, x in v:
            d[stem(hw)].append((b, f"{hw}: {t}", x))
    return d


def scan(by_stem=False):
    cnt = T.counts()
    pr = prior_by_stem() if by_stem else prior_by_book()
    out = []
    for k, hw, tag, term, cands, decided in final():
        p = pr.get(stem(hw) if by_stem else hw.lower(), [])
        if not p:
            continue
        diff = [(b, t, x) for b, t, x in p if x != term]
        if not diff:
            continue
        same = sorted({b for b, t, x in p if x == term})
        uses = sum(cnt.get(hw, {}).get(c, 0) for c in cands)
        out.append((uses, k, hw, tag, term, diff, same, decided))
    out.sort(key=lambda r: (-r[0], r[1]))
    return out


def enc():
    rows = final()
    by = {}
    for k, hw, tag, term, c, d in rows:
        by.setdefault(hw, []).append(term)
    suf = re.compile(r"(nti|ti|ñceva|ñca|mpi|pi|yeva)$")
    for hw, terms in by.items():
        m = suf.search(hw)
        if not m:
            continue
        base = hw[: m.start()]
        for cand in (base, base + "ṃ", base[:-1] + "aṃ" if base.endswith("a") else None, base + "a", base[:-1] + "ā" if base.endswith("a") else None, base[:-1] + "ī" if base.endswith("i") else None):
            if cand and cand in by and cand != hw:
                if set(terms) != set(by[cand]):
                    print(f"{hw} {terms}  <>  {cand} {by[cand]}")
                break


def fmt_prior(diff):
    g = collections.OrderedDict()
    for b, t, x in diff:
        g.setdefault((x, t[:50]), []).append(str(b))
    return "; ".join(f"{x} (pi-{','.join(bs)}: {t})" for (x, t), bs in g.items())


def main(a):
    if a == ["scan"]:
        for uses, k, hw, tag, term, diff, same, decided in scan():
            print(f"{uses}\t{k}\t{tag[:60]}\t{term}\t{fmt_prior(diff)}\tsame:{same}")
    elif a == ["stem"]:
        exact = {r[1] for r in scan()}
        for uses, k, hw, tag, term, diff, same, decided in scan(True):
            if k in exact:
                continue
            print(f"{uses}\t{k}\t{tag[:50]}\t{term}\t{fmt_prior(diff)[:400]}\tsame:{same}")
    elif a == ["enc"]:
        enc()
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
