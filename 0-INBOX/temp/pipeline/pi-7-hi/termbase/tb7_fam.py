"""pi-7 Hindi termbase helper (brief: ../hi-termbase-brief.md). Prints only.

usage: python -I -B -X utf8 tb7_fam.py groups [minsize]   stem families (case endings, -ti, enclitics stripped) whose
                                                         final terms differ; one line per distinct term
       python -I -B -X utf8 tb7_fam.py cross              pi-7 final terms that differ from a pi-1..6 term for the
                                                         same headword (exact) or stem (approximate)
       python -I -B -X utf8 tb7_fam.py dash               final terms with an em/en dash or a forbidden separator
"""
import collections, pathlib, re, sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
import tb_tool_pi7 as T  # noqa: E402

END = re.compile(r"(?:nti|ti|ñceva|ñca|mpi|pi|yeva|ceva|eva)$")
CASE = re.compile(r"(?:ānaṃ|īnaṃ|ūnaṃ|assa|āya|āyaṃ|uyā|iyā|ehi|ebhi|esu|āsu|ena|āni|uyo|iyo|aṃ|ā|o|e|ṃ|ī|ū|u|i|a|uṃ|iṃ)$")


def stem(hw):
    out = []
    for w in hw.lower().split():
        w = END.sub("", w)
        w2 = CASE.sub("", w)
        out.append(w2 if len(w2) >= 3 else w)
    return " ".join(out)


def final():
    dec = T.decisions()
    rows = []
    for hw, ss in T.senses():
        for i, (tag, c) in enumerate(ss):
            k = f"{hw}|{i}"
            rows.append((k, hw, tag, dec[k][0] if k in dec else c[0], c, k in dec))
    return rows


def groups(minsize=2):
    cnt = T.counts()
    g = collections.defaultdict(list)
    for k, hw, tag, term, c, d in final():
        g[stem(hw)].append((k, hw, tag, term, sum(cnt.get(hw, {}).get(x, 0) for x in c)))
    for s, rows in sorted(g.items()):
        terms = collections.OrderedDict()
        for k, hw, tag, term, n in rows:
            terms.setdefault(term, []).append((k, n, tag))
        if len(terms) < 2 or len(rows) < minsize:
            continue
        print(f"== {s}")
        for term, ks in terms.items():
            print(f"   {term}  <=  " + " ; ".join(f"{k}×{n} [{tag[:55]}]" for k, n, tag in ks))


def cross():
    pr = collections.defaultdict(list)
    prs = collections.defaultdict(list)
    for b, p in T.PRIOR.items():
        for l in p.read_text(encoding="utf-8").splitlines():
            if ": {" in l:
                hw, ss = T.parse(l)
                for tag, c in ss:
                    pr[hw.lower()].append((b, tag, c[0]))
                    prs[stem(hw)].append((b, f"{hw}: {tag}", c[0]))
    cnt = T.counts()
    out = []
    for k, hw, tag, term, c, d in final():
        exact = pr.get(hw.lower())
        p = exact or prs.get(stem(hw), [])
        if not p:
            continue
        diff = [(b, t, x) for b, t, x in p if x != term]
        if not diff:
            continue
        same = sorted({b for b, t, x in p if x == term})
        uses = sum(cnt.get(hw, {}).get(x, 0) for x in c)
        out.append((uses, k, tag, term, diff, same, "E" if exact else "S"))
    out.sort(key=lambda r: (-r[0], r[1]))
    for uses, k, tag, term, diff, same, how in out:
        g = collections.OrderedDict()
        for b, t, x in diff:
            g.setdefault((x, t[:45]), []).append(str(b))
        pf = "; ".join(f"{x} (pi-{','.join(bs)}: {t})" for (x, t), bs in g.items())
        print(f"{uses}\t{how}\t{k}\t{tag[:55]}\t{term}\t{pf[:300]}\tsame:{same}")


def dash():
    for k, hw, tag, term, c, d in final():
        if any(x in term for x in ("—", "–", ", ", " / ", "; ")):
            print(k, term)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "groups":
        groups(int(a[1]) if len(a) > 1 else 2)
    elif a == ["cross"]:
        cross()
    elif a == ["dash"]:
        dash()
    elif a == ["tags"]:
        # senses whose tags agree (grammar and enclitic notes stripped) but whose final terms differ
        g = collections.defaultdict(list)
        for k, hw, tag, term, c, d in final():
            t = re.sub(r"\s*\([^()]*\)\s*$", "", tag)
            t = re.sub(r",? with (enclitic|quotative|emphatic|the particle|-)[^,]*", "", t)
            t = re.sub(r"^and ", "", t).strip(" ,").lower()
            g[t].append((k, term))
        for t, rows in sorted(g.items()):
            if len({x for _, x in rows}) > 1:
                print(f"== {t[:90]}")
                for k, x in rows:
                    print(f"   {x}  <=  {k}")
    elif len(a) >= 2 and a[0] in ("grep", "tgrep"):
        # grep <regex on headword> | tgrep <regex on final term>: compact one line per sense
        rx = re.compile(a[1], re.I)
        cnt = T.counts()
        for k, hw, tag, term, c, d in final():
            if rx.search(hw if a[0] == "grep" else term):
                n = sum(cnt.get(hw, {}).get(x, 0) for x in c)
                print(f"{k}\t×{n}\t{term}\t{'(DEC) ' if d else ''}{'[' + ' / '.join(c) + '] ' if len(c) > 1 else ''}{tag[:70]}")
    else:
        sys.exit(__doc__)
