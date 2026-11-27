"""pi-7 phase 1, task 4: the recurring frames check for phase 2.

The 300 most frequent keywords of the WHOLE book (all 75 <ch>.keywords.md); for every use, the value the shared module
gives (map7_rules.Mapper with the module tables only: no chapter table, no CTX) and its presence in that segment's
Burmese (all 75 chapter files). Then the whole-book dry run: every keyword use mapped / unmapped / by stem fallback.
Writes frame-coverage.md (and work/dryrun-unmapped.tsv, work/dryrun-stem.tsv for phase 2). Nothing is mapped or
written besides these reports.
Run: /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 frame_coverage.py
"""
import sys
import pathlib
import collections

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import map7_rules as R          # noqa: E402

TOP = 300


# the suggested phase-2 groups: the book's parts kept together, cut to similar sizes (keyword uses)
GROUPS = [("g1", "part 1 triads (kusala … saṅkiliṭṭha)", lambda c: c[:2] == "1-"),
          ("g2", "part 2 triads (vitakka … sanidassana)", lambda c: c[:2] == "2-"),
          ("g3", "part 3 gocchakas 3-01 … 3-08", lambda c: c[:2] == "3-" and c < "3-09"),
          ("g4", "3-09 mahantaraduka, 3-10 upādāna, 4-01 kilesa", lambda c: c[:4] in ("3-09", "3-10", "4-01")),
          ("g5", "part 4 dukatika / tikaduka 4-02 … 4-21", lambda c: c[:2] == "4-" and c[:4] != "4-01"),
          ("g6", "part 5 (anuloma / paccanīya … 5-01 … 5-20)", lambda c: c[:2] == "5-")]


def groups(sizes, n=None):
    chs = [c for c in R.chapters() if c not in R.SAMPLE]
    return [(g, d, [c for c in chs if f(c)]) for g, d, f in GROUPS]


def main():
    uses = collections.Counter()
    where = collections.defaultdict(list)          # kw -> [(ch, sid)]
    sizes = collections.Counter()
    for ch in R.chapters():
        for sid, kws in R.keyword_rows(ch):
            for k in kws:
                uses[k] += 1
                sizes[ch] += 1
                where[k].append((ch, sid))
    M = R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK, R.LEXW]))
    # whole-book dry run (every use; the lookups are cached per segment, so the top-300 table reuses them)
    tot = ok_all = unm = wrong = 0
    unm_kw, stem_kw, wrong_kw = collections.Counter(), collections.Counter(), collections.Counter()
    per_ch = {}
    val = {}
    for ch in R.chapters():
        B, P = R.burmese(ch), R.pali(ch)
        c_tot = c_unm = c_wrong = c_stem = 0
        for sid, kws in R.keyword_rows(ch):
            for k in kws:
                tot += 1
                c_tot += 1
                try:
                    v = M.lookup(ch, sid, k, P.get(sid, ""), B.get(sid, ""))
                except KeyError:
                    unm += 1
                    c_unm += 1
                    unm_kw[k] += 1
                    val[(ch, sid, k)] = None
                    continue
                src = M.SRC.get((sid, k)) or ""
                val[(ch, sid, k)] = (v, src)
                if src == "stem":
                    stem_kw[(k, v)] += 1
                    c_stem += 1
                if R.presence(v, B.get(sid, ""))[0]:
                    ok_all += 1
                else:
                    wrong += 1
                    c_wrong += 1
                    wrong_kw[(k, v)] += 1
        per_ch[ch] = (c_tot, c_unm, c_stem, c_wrong)
    top = [k for k, _ in uses.most_common(TOP)]
    rows = []
    for k in top:
        vals = collections.Counter()
        ok = 0
        fails = collections.defaultdict(list)      # ch -> [(sid, reason)]
        srcs = collections.Counter()
        for ch, sid in where[k]:
            r = val[(ch, sid, k)]
            if r is None:
                fails[ch].append((sid, "no value"))
                continue
            v, src = r
            vals[v] += 1
            srcs[src.split(":")[0]] += 1
            if R.presence(v, R.burmese(ch).get(sid, ""))[0]:
                ok += 1
            else:
                fails[ch].append((sid, f"«{v}» not in the text"))
        rows.append((k, uses[k], vals, ok, fails, srcs))
    full = sum(1 for r in rows if r[3] == r[1])
    out = ["# pi-7 phase 1: recurring frames check (the 300 most frequent keywords of the whole book)", "",
           "Written by `frame_coverage.py` with the shared module `map7_rules.py` alone (no chapter table, no per-segment "
           "override): for every use of the keyword in the 75 `*.keywords.md`, the value the module gives in that "
           "segment and its presence in that segment's FINAL Burmese (the presence verifier of the module). "
           "«uses» = keyword uses; «values» = the values given (most frequent first, with uses); «presence» = uses whose "
           "value is in the segment's text; «source» = where the value came from (frame / stock = module tables; cond / "
           "vara / order / count / samutthana = the Paṭṭhāna families T1-T6, T12; headlex = the heading lexicon T9; verb "
           "= T10; terms = my7-zeroshot-terms; lex = LEXW (T11); pi-N = a pi-N value; base = R1; term = T7 / T8 / T12; "
           "heading = R6; stem = S1).", "",
           f"**{full} of {len(rows)} keywords reach 100% presence**; "
           f"{sum(r[3] for r in rows)} of {sum(r[1] for r in rows)} uses present.", "",
           "| # | keyword | uses | values (uses) | presence | source | chapters where it fails (why) |",
           "|---|---|---|---|---|---|---|"]
    for i, (k, n, vals, ok, fails, srcs) in enumerate(rows, 1):
        vs = "; ".join(f"{v} ({c})" for v, c in vals.most_common(3)) + (" …" if len(vals) > 3 else "")
        fs = "; ".join(f"{ch} {len(x)}× (e.g. ^{x[0][0]}: {x[0][1]})" for ch, x in sorted(fails.items())[:4])
        fs = (fs + (" …" if len(fails) > 4 else "")) or "-"
        src = ", ".join(f"{s} {c}" for s, c in srcs.most_common(3))
        out.append(f"| {i} | {k} | {n} | {vs} | {ok}/{n} ({100 * ok / n:.1f}%) | {src} | {fs} |")
    out += ["", "## Whole-book dry run (module only)", "",
            f"All {tot} keyword uses of the 75 files: **{ok_all} mapped and present** "
            f"({100 * ok_all / tot:.2f}%), **{unm} without a value** ({len(unm_kw)} keywords), "
            f"**{wrong} with a value not in the text**; by the stem fallback (S1): {sum(stem_kw.values())} uses "
            f"({len({k for k, _ in stem_kw})} keywords).", "",
            "| chapter | uses | unmapped | stem | value not present |", "|---|---|---|---|---|"]
    for ch in R.chapters():
        t, u, s, w = per_ch[ch]
        out.append(f"| {ch} | {t} | {u} | {s} | {w} |")
    out += ["", "### The most frequent unmapped keywords (uses)", "",
            "; ".join(f"{k} {n}" for k, n in unm_kw.most_common(80)), ""]
    out += ["### Stem-fallback values (most frequent; to be checked by eye in phase 2)", "",
            "; ".join(f"{k} = {v} ({n})" for (k, v), n in stem_kw.most_common(40)), ""]
    if wrong_kw:
        out += ["### Values not present", "", "; ".join(f"{k} = {v} ({n})" for (k, v), n in wrong_kw.most_common(30)), ""]
    gs = groups(sizes)
    assert sum(len(x[2]) for x in gs) == len([c for c in R.chapters() if c not in R.SAMPLE])
    out += ["## Suggested phase-2 groups (the 72 remaining chapters; the book's parts kept together, similar size)", "",
            "| group | part | chapters | files | keyword uses | unmapped now | stem now |", "|---|---|---|---|---|---|---|"]
    for g, d, cs in gs:
        out.append(f"| {g} | {d} | {cs[0]} … {cs[-1]} | {len(cs)} | {sum(sizes[c] for c in cs)} | "
                   f"{sum(per_ch[c][1] for c in cs)} | {sum(per_ch[c][2] for c in cs)} |")
    out += ["", NOTES]
    (HERE / "frame-coverage.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    w = HERE / "work"
    w.mkdir(exist_ok=True)
    (w / "dryrun-unmapped.tsv").write_text("".join(f"{k}\t{n}\n" for k, n in unm_kw.most_common()), encoding="utf-8")
    (w / "dryrun-stem.tsv").write_text("".join(f"{k}\t{v}\t{n}\n" for (k, v), n in stem_kw.most_common()),
                                       encoding="utf-8")
    print("full", full, "of", len(rows), "| dry run", tot, "ok", ok_all, "unmapped", unm, len(unm_kw), "wrong", wrong,
          "stem", sum(stem_kw.values()))
    for k, n, vals, ok, fails, srcs in rows:
        if ok < n:
            print(f"  {k} {ok}/{n} {vals.most_common(2)} {[(c, x[:1]) for c, x in list(fails.items())[:3]]}")
    for g, d, cs in gs:
        print("  group", g, cs[0], "…", cs[-1], len(cs), sum(sizes[c] for c in cs))


NOTES = open(HERE / "work" / "frame-notes.md", encoding="utf-8").read() if (HERE / "work" / "frame-notes.md").exists() \
    else ""


if __name__ == "__main__":
    main()
