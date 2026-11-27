"""phase 3 task 2: every stem-fallback (S1) use left in the 75 chapters (the mappers run in-process, nothing written),
with its value, the phase-2 value at the same place (work/phase2-mapped) and whether it changed.
writes work/p3_s1_after.tsv: segment, keyword, value, phase-2 value, changed, Pāli / Burmese context."""
import sys, re, pathlib, importlib, collections
D = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(D)); sys.dont_write_bytecode = True
import map7_rules as R
GROUPS = [("map_sample", R.SAMPLE)]
for g, attr in (("map_g1", "G1"), ("map_g2", "CHAPTERS"), ("map_g3", "CHAPTERS"), ("map_g4", "CHAPTERS"),
                ("map_g5", "CHAPTERS"), ("map_g6", "G6")):
    GROUPS.append((g, None if attr is None else attr))


def old_vals():
    out = {}
    for f in sorted((D / "work/phase2-mapped").glob("*.mapped.md")):
        for l in f.read_text(encoding="utf-8").splitlines():
            sid, rest = l[1:].split("] ", 1)
            for i, kv in enumerate(rest.split(", ")):
                out[(sid, i)] = kv.split("=", 1)
    return out


old = old_vals()
rows = []
for g, attr in GROUPS:
    m = importlib.import_module(g)
    chs = attr if isinstance(attr, list) else getattr(m, attr)
    M = m.mapper()
    for ch in chs:
        if g == "map_g6":
            m.map_chapter(M, ch)
        else:
            M.map_chapter(ch)
        my, pa = R.burmese(ch), R.pali(ch)
        for sid, kws in R.keyword_rows(ch):
            for i, k in enumerate(kws):
                if M.SRC.get((sid, k)) == "stem":
                    v = M.cache[(ch, sid, k)][0]
                    ov = old.get((sid, i), ("?", "?"))[1]
                    p = pa.get(sid, ""); j = p.find(k)
                    b = my[sid]; jb = b.find(v.split(" … ")[0])
                    rows.append((ch, sid, k, v, ov, "changed" if ov != v else "same",
                                 p[max(0, j - 40):j + 50].replace("\t", " "), b[max(0, jb - 30):jb + 50].replace("\t", " ")))
(D / "work/p3_s1_after.tsv").write_text("chapter\tsegment\tkeyword\tvalue\tphase-2 value\tchanged\tPāli\tBurmese\n" +
                                        "".join("\t".join(r) + "\n" for r in rows), encoding="utf-8")
pairs = collections.Counter((r[2], r[3]) for r in rows)
print("S1 uses", len(rows), "pairs", len(pairs), "changed", sum(r[5] == "changed" for r in rows))
for (k, v), n in sorted(pairs.items(), key=lambda x: -x[1]):
    print(f"   {n:4d} {k} = {v}")
for r in rows:
    if r[5] == "changed":
        print("CHANGED", r[1], r[2], r[4], "->", r[3], "|", r[6], "|", r[7])
