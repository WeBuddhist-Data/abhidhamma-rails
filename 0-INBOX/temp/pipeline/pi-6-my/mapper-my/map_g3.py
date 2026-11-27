"""pi-6 Burmese keyword mapping, PHASE 2, group G3: 9-01 … 9-03 dhammayamaka, 10-01 … 10-13 indriyayamaka.

Imports the shared module map6_rules.py; since phase 3 the group rules are book-wide in the module and this script
holds only the per-segment rules (CTX) of the group. Maps the G3 chapters in chapter order, writes
<ch>.mapped.md, prints the three checks of the phase-1 brief per chapter (keyword preservation `bad []`, presence,
no «, » / «၊» / « / » in a value), and with --report the S1 review (every use whose module-only value comes from the
stem fallback: kept or corrected), the values that differ from pi-1 … pi-5 / the sample, and the phrase scan.
Run: /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 map_g3.py [chapter-prefix …] [--report] [-v]
Notes: notes-g3.md.
"""
import re
import sys
import pathlib
import collections

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import map6_rules as R          # noqa: E402

NONE = R.NONE
G3 = ["9-01-dhammayamaka", "9-02-dhammayamaka", "9-03-dhammayamaka"] + \
     [f"10-{i:02d}-indriyayamaka" for i in range(1, 14)]


# =====================================================================================================================
# phase 3: the group table T_ALL, the context functions FUNCS_G3 (f_citta, f_saka, f_fem, f_vara; f_sacchi dropped,
# U4 decided: the verifier's «neg-verb-sp» ending) and the rules W1-W7, O1-O7 are now book-wide in map6_rules.py (BOOK,
# book_auto()). Only the forms of ONE segment stay here, as per-segment rules (sid -> {kw: value}); notes-g3.md,
# map-harmonise-notes.md §D.
# =====================================================================================================================
TABLES = {}
CTX = {
    # Pāli slips (harmonise A3): the intended word, the text's form
    "6-10-3": {"anaññātaññāssāmīti": "မသိရသေးသည်ကို သိရတော့မည်ဟူသော"},   # anaññātaññassāmīti (W4)
    "6-10-309": {"upapajjissati": "ဖြစ်ပေါ်လိမ့်မည်"},                # for uppajjissati («… မဖြစ်ပေါ်လိမ့်မည်ကား မဟုတ်»)
    "6-10-398": {"uppajjantānaṃ": "ပြန်လည် ဖြစ်ပေါ်ဆဲ"},              # for upapajjantānaṃ («ပြန်လည် ဖြစ်ပေါ်ဆဲ … ယောက်ျားတို့»)
    "6-10-206": {"uppajjantīnaṃ": "ပြန်လည် ဖြစ်ပေါ်ဆဲ"},              # for upapajjantīnaṃ («ပြန်လည် ဖြစ်ပေါ်ဆဲ မိန်းမတို့»)
    "6-10-336": {"Ghānandriyamūlakaṃ": "နှာခေါင်း၏ စွမ်းရည်ကို အခြေခံသော"},  # Ghānindriyamūlakaṃ
    "6-10-361": {"cavantāna": "စုတေဆဲသူ"},                            # cavantānaṃ
    # the book colophon «Yamakapakaraṇaṃ niṭṭhitaṃ» «“အတွဲလိုက် မေးဖြေခြင်း” ကျမ်း ပြီးဆုံးပြီ» (U8 decided: «ကျမ်း» is
    # pakaraṇa, as pi-2 Vibhaṅgapakaraṇaṃ «ခွဲခြမ်းစိတ်ဖြာခြင်း ကျမ်း»)
    "6-10-482": {"Yamakapakaraṇaṃ": "အတွဲလိုက် မေးဖြေခြင်း ကျမ်း"},
}


def mapper():
    return R.Mapper(chapter_tables=TABLES, ctx=CTX, stem=R.make_stem([R.FRAME, R.STOCK, R.BOOK]))


def module_only():
    return R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK, R.BOOK]))


# =====================================================================================================================
# reports
# =====================================================================================================================
def s1_review(ch, base, lines):
    """the uses whose MODULE-ONLY value comes from the stem fallback (S1): kept (the final value is the stem value) or
    corrected (a G3 table / context value replaces it)."""
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
    """values that differ from a pi-1 … pi-5 value of the same keyword (or its base form, R1), and from the phase-1
    sample and the G1 / G2 mapped files for the same keyword."""
    other = collections.defaultdict(collections.Counter)
    for ch in R.CHAPTERS:
        if ch in G3 or not (HERE / f"{ch}.mapped.md").exists():
            continue
        for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
            for kv in l.split("] ", 1)[1].split(", "):
                k, v = kv.split("=", 1)
                other[k][v] += 1
    same = new = 0
    prior_diff, other_diff = collections.defaultdict(collections.Counter), collections.defaultdict(collections.Counter)
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
                if other.get(k) and v not in other[k]:
                    other_diff[(k, v)][other[k].most_common(1)[0][0]] += 1
    print(f"PRIOR same {same} new {new} diff {sum(sum(c.values()) for c in prior_diff.values())} "
          f"({len(prior_diff)} pairs)")
    for (k, v), c in sorted(prior_diff.items(), key=lambda x: -sum(x[1].values())):
        print(f"   PRIORDIFF {k} = {v} | " + "; ".join(f"{p} ({n})" for p, n in c.items()))
    for (k, v), c in sorted(other_diff.items(), key=lambda x: -sum(x[1].values())):
        print(f"   GROUPDIFF {k} = {v} | " + "; ".join(f"{p} ({n})" for p, n in c.items()))


def phrase_scan(chs):
    """values that the segment's Burmese does not have as a phrase (every « … » part, its final «သည် / သော» by an
    ending rule; also without quotation marks / the list comma): present only chunk by chunk or by an ending rule."""
    c = collections.Counter()
    for ch in chs:
        my = R.burmese(ch)
        for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
            sid, rest = l[1:].split("] ", 1)
            t = my[sid]
            vs = [t, R.flat(t), re.sub("[“”]", "", t), R.flat(re.sub("[“”]", "", t))]
            for kv in rest.split(", "):
                k, v = kv.split("=", 1)
                if v != NONE and not any(R.phrase_ok(v, x) for x in vs):
                    c[(ch, k, v)] += 1
    print(f"PHRASE not a phrase: {sum(c.values())} uses ({len(c)} pairs)")
    for (ch, k, v), n in sorted(c.items()):
        print(f"   NOPHRASE {ch} {k} = {v} ({n})")


def run(chs):
    M, B = mapper(), module_only()
    tot = collections.Counter()
    allkept, allcorr = collections.Counter(), collections.Counter()
    for ch in chs:
        lines, problems, unmapped, nne = M.map_chapter(ch)
        (HERE / f"{ch}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        n, bad, fails, punct, ruled = R.verify_file(ch)
        rules = collections.Counter(r for _, _, _, r in ruled)
        kept, corr = s1_review(ch, B, lines)
        allkept.update(kept)
        allcorr.update(corr)
        print(f"{ch}: lines {n} bad {bad} presence-fails {len(fails)} punct {len(punct)} unmapped {len(unmapped)} "
              f"NDE {nne} ending-rule chunks {dict(sorted(rules.items()))} S1 kept {sum(kept.values())} "
              f"corrected {sum(corr.values())}")
        for x in unmapped:
            print("   UNMAPPED", x)
        for x in fails:
            print("   FAIL", x)
        for x in punct:
            print("   PUNCT", x)
        tot.update(lines=n, nde=nne, fails=len(fails), punct=len(punct), bad=len(bad), unmapped=len(unmapped),
                   kept=sum(kept.values()), corr=sum(corr.values()), ruled=len(ruled))
    print("TOTAL", dict(sorted(tot.items())))
    if "--report" in sys.argv:
        for (k, vb, vf), c in sorted(allkept.items()):
            print(f"   S1 KEPT {k} = {vb} ({c})")
        for (k, vb, vf), c in sorted(allcorr.items()):
            print(f"   S1 CORRECTED {k}: {vb} -> {vf} ({c})")
        diff_report(chs)
        phrase_scan(chs)
    return M


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    run([ch for ch in G3 if not args or any(ch.startswith(a) for a in args)])
