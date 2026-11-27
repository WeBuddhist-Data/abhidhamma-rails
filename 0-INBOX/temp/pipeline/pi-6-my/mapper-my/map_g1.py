"""pi-6 Burmese keyword mapping, PHASE 2, group G1 (2-02 … 5-03).

Imports the shared module map6_rules.py; since phase 3 the group rules are book-wide in the module and this script
holds only the per-segment rules (CTX) of the group. Maps the G1 chapters in chapter order, writes <ch>.mapped.md, runs the three checks of the
phase-1 brief per chapter (keyword preservation `bad []`, presence, no «, » / «၊» / « / » in a value) and the S1
review (every use whose module-only value comes from the stem fallback: kept or corrected).
Run: /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 map_g1.py [ch …] [--pairs]
Notes: notes-g1.md.
"""
import re
import sys
import pathlib
import collections

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import map6_rules as R          # noqa: E402

NONE = R.NONE
G1 = ["2-02-khandhayamaka", "3-01-ayatanayamaka", "3-02-ayatanayamaka", "3-03-ayatanayamaka",
      "3-04-ayatanayamaka", "3-05-ayatanayamaka", "3-06-ayatanayamaka", "4-dhatuyamaka",
      "5-01-saccayamaka", "5-02-saccayamaka", "5-03-saccayamaka"]


# =====================================================================================================================
# phase 3: the group table T_ALL, the context functions FUNCS_G1 (f_rupam_g1, f_aka, f_saka, f_citta, f_nayatana) and
# the rules G1-G11 are now book-wide in map6_rules.py (BOOK, book_auto(), f_rupam, title_value()). Only the forms of
# ONE segment stay here, as per-segment rules (sid -> {kw: value}); notes-g1.md G9 / G11, map-harmonise-notes.md §D.
# =====================================================================================================================
TABLES = {}
CTX = {
    "6-3-201": {"vāresu": "ဖော်ပြချက်"},                        # «ဖော်ပြချက် သုံးပါးလုံး၌» (tīsupi vāresu; G1)
    "6-3-23": {"vārasaṅkhepo": "ဖော်ပြချက်တို့၌ အကျဉ်း ဖော်ပြထားသည်"},   # «(upari) vārasaṅkhepo» (G1; rule 1 inner «တို့၌»)
    # the past / present pairs of the note «paccuppannātītepi …» (Q4: the «လည်း» of pi goes; rule 1 the «၌»)
    "6-3-40": {"paccuppannātītepi": "ပစ္စုပ္ပန်နှင့် အတိတ်", "paccuppannānāgatepi": "ပစ္စုပ္ပန်နှင့် အနာဂတ်"},
    # X-sadiso «Xနှင့် တူညီသည်» (the note «(Saddo ghānasadiso)» «(အသံသည် နှာခေါင်းနှင့် တူညီသည်)»; rule 4; G9)
    "6-4-10": {"ghānasadiso": "နှာခေါင်းနှင့် တူညီသည်", "ghānadhātusadisā": "နှာခေါင်း ဓာတ်နှင့် တူညီသည်"},
    # Pāli slips of the source (G11; text inconsistencies): the intended word's value
    "6-2-185": {"vadanākkhandho": "ခံစားမှု အစုအဝေး"},          # vedanākkhandho
    "6-3-13": {"sotāyananti": "နား အာရုံခံ နယ်ပယ်"},              # sotāyatananti
    "6-3-172": {"parinibbāntānaṃ": "ပရိနိဗ္ဗာန် ပြုဆဲသူ"},          # parinibbantānaṃ
    "6-5-76": {"asaññattā": "အသညသတ် ဘုံ"},                      # asaññasattā «… ဘုံမှ စုတေဆဲသူ» (R5 plane)
    # uppajjittha rūpāyatanañca run together (U4 decided): both members' words, the finite verb last (Q3), « … » for
    # the «လည်း» of ca between them (Q4)
    "6-3-43": {"uppajjittharūpāyatanañca": "အဆင်းအရောင် အာရုံခံ နယ်ပယ် … ဖြစ်ပေါ်ခဲ့သည်"},
    # Pāli slip upapajjissati for uppajjissati: the text's word (the literal tier no longer assembles «ပြန်လည်
    # ဖြစ်ပေါ်လိမ့်မည်» from scattered chunks, mechanic 1, but the slip is still a different root)
    "6-3-212": {"upapajjissati": "ဖြစ်ပေါ်လိမ့်မည်"},
}


def mapper():
    return R.Mapper(chapter_tables=TABLES, ctx=CTX, stem=R.make_stem([R.FRAME, R.STOCK, R.BOOK]))


def module_only():
    return R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK, R.BOOK]))


# =====================================================================================================================
# run, verify, S1 review
# =====================================================================================================================
def s1_review(ch, base, lines):
    """the uses whose MODULE-ONLY value comes from the stem fallback (S1): kept (the final value is the stem value) or
    corrected (a G1 table / context value replaces it)."""
    kept, corr = collections.Counter(), collections.Counter()
    b_lines = base.map_chapter(ch)[0]
    for lb, lf in zip(b_lines, lines):
        sid, rb = lb[1:].split("] ", 1)
        rf = lf.split("] ", 1)[1]
        for kvb, kvf in zip(rb.split(", "), rf.split(", ")):
            k, vb = kvb.split("=", 1)
            vf = kvf.split("=", 1)[1]
            if base.SRC.get((sid, k)) == "stem":
                (kept if vb == vf else corr)[(k, vb, vf)] += 1
    return kept, corr


def diff_report(chs):
    """the values that differ from a pi-1 … pi-5 value of the same keyword (or of its base form, R1), and from the
    phase-1 sample (1-mulayamaka, 2-01-khandhayamaka) for the same keyword: keyword, value, the other value (uses)."""
    sample = collections.defaultdict(collections.Counter)
    for ch in R.SAMPLE:
        for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
            for kv in l.split("] ", 1)[1].split(", "):
                k, v = kv.split("=", 1)
                sample[k][v] += 1
    same = new = 0
    prior_diff, sample_diff = collections.defaultdict(collections.Counter), collections.defaultdict(collections.Counter)
    for ch in chs:
        for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
            for kv in l.split("] ", 1)[1].split(", "):
                k, v = kv.split("=", 1)
                pv = R.prev_vals(k)
                if not pv:
                    for b in R.base_forms(k):
                        pv = R.prev_vals(b)
                        if pv:
                            break
                if not pv:
                    new += 1
                elif v in pv:
                    same += 1
                else:
                    prior_diff[(k, v)][pv.most_common(1)[0][0]] += 1
                if sample.get(k) and v not in sample[k]:
                    sample_diff[(k, v)][sample[k].most_common(1)[0][0]] += 1
    print(f"PRIOR same {same} new {new} diff {sum(sum(c.values()) for c in prior_diff.values())} "
          f"({len(prior_diff)} pairs)")
    for (k, v), c in sorted(prior_diff.items(), key=lambda x: -sum(x[1].values())):
        print(f"   PRIORDIFF {k} = {v} | " + "; ".join(f"{p} ({n})" for p, n in c.items()))
    for (k, v), c in sorted(sample_diff.items(), key=lambda x: -sum(x[1].values())):
        print(f"   SAMPLEDIFF {k} = {v} | " + "; ".join(f"{p} ({n})" for p, n in c.items()))


def run(chs):
    M, B = mapper(), module_only()
    tot = collections.Counter()
    allkept, allcorr = collections.Counter(), collections.Counter()
    for ch in chs:
        lines, problems, unmapped, nne = M.map_chapter(ch)
        (HERE / f"{ch}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        n, bad, fails, punct, ruled = R.verify_file(ch)
        kept, corr = s1_review(ch, B, lines)
        allkept.update(kept)
        allcorr.update(corr)
        print(f"{ch}: lines {n} bad {bad} presence-fails {len(fails)} punct {len(punct)} unmapped {len(unmapped)} "
              f"NDE {nne} ruled {len(ruled)} S1 kept {sum(kept.values())} corrected {sum(corr.values())}")
        for x in unmapped:
            print("   UNMAPPED", x)
        for x in fails:
            print("   FAIL", x)
        for x in punct:
            print("   PUNCT", x)
        tot.update(lines=n, nne=nne, fails=len(fails), punct=len(punct), bad=len(bad), unmapped=len(unmapped),
                   kept=sum(kept.values()), corr=sum(corr.values()))
    print("TOTAL", dict(tot))
    if "--s1" in sys.argv:
        for (k, vb, vf), c in sorted(allkept.items()):
            print(f"   S1 KEPT {k} = {vb} ({c})")
        for (k, vb, vf), c in sorted(allcorr.items()):
            print(f"   S1 CORRECTED {k}: {vb} -> {vf} ({c})")
    if "--diff" in sys.argv:
        diff_report(chs)
    if "--pairs" in sys.argv:
        pairs = collections.Counter()
        src = {}
        for ch in chs:
            for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
                sid, rest = l[1:].split("] ", 1)
                for kv in rest.split(", "):
                    k, v = kv.split("=", 1)
                    pairs[(k, v)] += 1
                    src.setdefault((k, v), M.SRC.get((sid, k), "?"))
        for (k, v), c in sorted(pairs.items(), key=lambda x: (R.low(x[0][0]), x[0][1])):
            print(f"   PAIR {k} = {v} | {c} | {src[(k, v)]}")
    return M


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    run(args or G1)
