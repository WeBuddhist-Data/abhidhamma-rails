import collections
bad = collections.Counter()
for name in X.NAMES:
    src = (X.PALI / name).read_text(encoding="utf-8-sig")
    for d, t in X.parts_of(src):
        X.set_dyad(F, d)
        t = X.prep(t, d)
        t = re.sub(r"\{[^{}]*\}", "", t)
        for m in re.finditer(r"\(([^()]*)\)", t):
            k = m[0]
            if re.fullmatch(r"\(\d+\)", k) or k in F.NOTES: continue
            if X.K.note_unit(k) is None:
                bad[(name[:4], d, k)] += 1
for k, v in sorted(bad.items()):
    print(v, k)
