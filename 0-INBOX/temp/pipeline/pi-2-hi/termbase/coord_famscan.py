"""Coordinator: whole-book lemma-family scan of the pi-2 effective termbase (senses file + all decisions*.tsv).

Groups one-word headwords by a rough Pāli base (clitics and case endings stripped, case merged) and writes the bases whose
senses carry more than one Hindi term after a rough Hindi normalisation. Each row: line, key, term, map count, decision
file (or '-'), tag. Output: coord-famscan.txt; prints the number of families.
"""
import collections, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import tb_tool_pi2 as T

OUT = pathlib.Path(__file__).parent / "coord-famscan.txt"
ENDS = sorted(("assāpi ānañca esuceva anti assa ānaṃ ehi esu āya ena ato smiṃ mhi ānī āni āyo iyo iyā iyaṃ ataṃ"
               " ṃ ā o e ī ū i u a").split(), key=len, reverse=True)
CLIT = ("meva", "ñceva", "ceva", "ñca", "nti", "ti", "pi", "ca", "vā")


def base(hw):
    w = hw.lower()
    changed = True
    while changed:
        changed = False
        for c in CLIT:
            if w.endswith(c) and len(w) - len(c) >= 4:
                w = w[: -len(c)]; changed = True; break
    for e in ENDS:
        if w.endswith(e) and len(w) - len(e) >= 3:
            return w[: -len(e)]
    return w


def norm(t):
    t = re.sub(r"(ा|ी|े|ों|एँ|ाएँ|ओं)(?=\s|$)", "", t)
    return re.sub(r"\s+", " ", t).strip()


def effective():
    ss, cnt, dec = T.senses(), T.counts(), T.decisions()
    rows = []
    for n, (hw, s) in enumerate(ss, 1):
        for i, (tag, c) in enumerate(s):
            k = f"{hw}|{i}"
            t, src = dec.get(k, (c[0], "-"))
            rows.append((n, hw, i, tag, c, t, src, sum(cnt.get(hw, {}).values())))
    return rows


if __name__ == "__main__":
    fam = collections.defaultdict(list)
    for r in effective():
        if " " in r[1]:
            continue
        fam[base(r[1])].append(r)
    blocks = [(len(xs), b, xs) for b, xs in fam.items() if len({norm(x[5]) for x in xs}) > 1]
    blocks.sort(key=lambda x: (-sum(r[7] for r in x[2]), x[1]))
    with OUT.open("w", encoding="utf-8", newline="\n") as f:
        for n, b, xs in blocks:
            f.write(f"== {b} ({n})\n")
            for (ln, hw, i, tag, c, t, src, k) in xs:
                f.write(f"  {ln}\t{hw}|{i}\t{t}\t×{k}\t{src}\t{'/'.join(c) if len(c) > 1 else ''}\t{tag[:60]}\n")
    print(f"families with >1 Hindi term: {len(blocks)} of {len(fam)} -> {OUT.name}")
