"""pi-7 Burmese keyword mapping, PHASE 1: preamble, 1-00-paccaya, 1-02-vedanattika.

Uses the shared module map7_rules.py (side-effect free). Writes <ch>.mapped.md for the three sample chapters, runs the
verifier (keyword preservation, presence, punctuation) and, with --table, writes map-table.md.
Run: /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 map_sample.py [--table] [--diff]

Phase 3 (2026-11-26): the module overrides and the book-wide group values moved into map7_rules.py (BOOK, the module
fixes 1-9); this script keeps only what is local to the group. phase3-changes.tsv lists every value that changed.
"""
import sys
import pathlib
import collections

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import map7_rules as R          # noqa: E402

# chapter tables: only what the module does not settle (none: every recurring keyword is in the module)
T_PRE = {}
T_00 = {}
T_02 = {}
TABLES = {"preamble": T_PRE, "1-00-paccaya": T_00, "1-02-vedanattika": T_02}
# per-segment overrides (sid -> {kw: value}): a keyword of ONE segment of the book
CTX = {
    # the note «(saddhāpañcamakesu "mānaṃ jappeti …"ti kātabbaṃ …)» «(ယုံကြည်မှု စသော ငါးပါးတို့၌ …)»: rule 1
    "7-3-53": {"saddhāpañcamakesu": "ယုံကြည်မှု စသော ငါးပါး"},
}


def mapper():
    return R.Mapper(chapter_tables=TABLES, ctx=CTX, stem=R.make_stem([R.FRAME, R.STOCK, R.LEXW]))


def run(write=True):
    M = mapper()
    out = {}
    for ch in R.SAMPLE:
        lines, problems, unmapped, nne = M.map_chapter(ch)
        out[ch] = (lines, problems, unmapped, nne)
        if write:
            (HERE / f"{ch}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return M, out


def compare_prior():
    """uses whose value equals / differs from a pi-1 … pi-6 value of the same keyword (or of its base form, R1)."""
    same = new = diff = 0
    diffs = collections.defaultdict(collections.Counter)
    same_kw = set()
    for ch in R.SAMPLE:
        for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
            sid, rest = l[1:].split("] ", 1)
            for kv in rest.split(", "):
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
                    same_kw.add(k)
                else:
                    diff += 1
                    diffs[(k, v)][pv.most_common(1)[0][0]] += 1
    return same, new, diff, diffs, same_kw


C_NAME = ("T1 / T2: the condition in the frame of the Paṭṭhāna (counting locative «Nဟူသော အကြောင်း၌ K», bare ghaṭanā "
          "name, ablative «…ကြောင့်»); the pi-1 … pi-6 value is the plain noun / verb of another kind of segment and stands "
          "in the pi-7 segment only as a part of the condition name")
REASONS = {
    "uppajjeyya": "T10: the optative of the pucchāvāra «Siyā … uppajjeyya» is the text's potential «ဖြစ်ပေါ်နိုင်သလော» "
                  "(dictionary «ဖြစ်ပေါ်နိုင်သည်», Q1 ending «သလော»); the pi-2 / pi-5 «ဖြစ်ပေါ်သည်» is not in the segment",
    "uppajjeyyuṃ": "as uppajjeyya (the plural «ကြ» by the ending rule, rule 4)",
    "vigate": C_NAME, "indriye": C_NAME, "ārammaṇe": C_NAME, "āhāre": C_NAME, "magge": C_NAME, "jhāne": C_NAME,
    "vippayutte": C_NAME, "aññamañña": C_NAME, "atthi": C_NAME, "anantara": C_NAME, "āhāra": C_NAME,
    "āsevana": C_NAME, "indriya": C_NAME, "sampayutta": C_NAME, "natthi": C_NAME + "; in a note the verb «မရှိ» (Q5)",
    "uppādeti": "the text's «… ကို ဖြစ်စေသည်» (my7 LEX); the pi-5 «ဖြစ်ပေါ်မှု» (a noun) is not in the segment",
    "assādeti": "T11: the text joins the two verbs «သာယာ နှစ်သက်သည်» with one «သည်»; the pi-5 «သာယာသည်» is not in the "
                "segment, the bare «သာယာ» is (unclear point U1)",
    "kusalākusalaṃ": "the text's «ကုသိုလ်နှင့် အကုသိုလ် ကံ» (my7 FIXED, pi-5 kusalākusale); the pi-1 «ကုသိုလ် အကုသိုလ်» is "
                     "not in the segment as a phrase",
    "datvā": "T11: «dānaṃ datvā» = «ပေးလှူခြင်းကို ပြု၍»: the verb is «ပြု၍»; the pi-4 «ပေးပြီးနောက်» is not in the segment",
    "deti": "T11: «dānaṃ deti» = «ပေးလှူခြင်းကို ပြုသည်»; the pi-4 «ပေးသည်» stands in the segment only inside «မပေးသည်ကို» "
            "(adinnaṃ), another phrase",
    "paccavekkhati": "the pi-7 text's word «ပြန်လည် ဆင်ခြင်» (my7 LEX, the prefix paṭi- «ပြန်လည်»); the pi-2 / pi-5 "
                     "«ဆင်ခြင်သည်» is only its second half",
    "ekamūlakaṃ": "T6: the counted mūlaka «အကြောင်း တစ်ခုကို အခြေခံခြင်း» (my7-zeroshot-terms §2); the pi-3 «တစ်မျိုးတွဲကို "
                  "အခြေခံသော» (Dhātukathā) is not in the segment",
    "vipassati": "the text's «ထိုးထွင်း၍ ရှုသည်» (my7 LEX); the pi-5 «ကြည့်ရှုသည်» is not in the segment",
    "kiñci": "«kiñci kāle» «အချို့သော အချိန်၌»; the pi-5 «တစ်စုံတစ်ရာ» is not in the segment",
    "katvā": "T11 / pi-2 harmonise (one Burmese word for two members): after the act compound uposathakammaṃ the verb "
             "«စောင့်ထိန်း၍» belongs to the compound's value; the pi-5 «အကြောင်းပြု၍» is not in the segment",
    "samanantarā": "the pi-7 text gives the adverb its condition's word «ကောင်းစွာ ချက်ချင်း နောက်၌» (notes-sample point 2; "
                   "rule 1: «၌» goes); the pi-5 «ချက်ချင်း နောက်၌» stands only as a part of it",
    "sahajāto": "my7-zeroshot-terms §4 link word «Xနှင့်အတူ ပေါ်ပေါက်သော»; the pi-2 «အတူတကွ ဖြစ်ပေါ်သော» is not in the segment",
    "nirodhā": "my7 LEX «nirodhā vuṭṭhahantassa» «ချုပ်ငြိမ်းခြင်း သမာပတ်မှ ထမြောက်နေသူ» (rule 1: «မှ» goes); the pi-5 "
               "«ချုပ်ငြိမ်းသော» is not in the segment",
    "vuṭṭhahantassa": "pi-4 P6 / pi-6 R3: a person participle is the agent noun «…သူ» (the text's «ထမြောက်နေသူ»); the "
                      "pi-5 attributive «ထမြောက်နေသော» stands only by an ending rule",
    "bhaṇati": "the text's «ပြောသည်»; the pi-5 «ပြောဆိုသည်» is not in the segment",
    "harati": "T11: «nillopaṃ harati» «ဥစ္စာကို လုယူသည်»; the pi-5 «ဆောင်သည်» is not in the segment",
    "tiṭṭhati": "T11: «paripanthe tiṭṭhati» «လမ်းခရီး၌ ဓားပြ တိုက်သည်»; the pi-5 «တည်သည်» stands in the segment only inside "
                "«ဆောက်တည်သည်» (samādiyati), another word",
    "mūlakaṃ": "the note «(mūlakaṃ saṃkhittaṃ)» «(အခြေခံ အကြောင်းများကို အကျဉ်းချုပ်)» (rule 1); the pi-5 «အခြေခံသော» is "
               "not in the segment",
}


def reason(k):
    for key in [k, R.low(k)] + R.base_forms(k) + [R.low(b) for b in R.base_forms(k)]:
        if key in REASONS:
            return REASONS[key]
    return "?"


def write_table(M, out):
    same, new, diff, diffs, same_kw = compare_prior()
    L = [HEAD, "## Numbers", ""]
    for ch in R.SAMPLE:
        n, bad, fails, punct, ruled = R.verify_file(ch)
        L.append(f"- `{ch}.mapped.md`: {n} lines, keyword preservation `bad {bad}`, presence failures {len(fails)}, "
                 f"«, » / «၊» / « / » in a value {len(punct)}, (no direct equivalent) {out[ch][3]}, chunks matched by an "
                 f"ending rule {len(ruled)}.")
    pairs = collections.Counter()
    src = {}
    for ch in R.SAMPLE:
        for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
            sid, rest = l[1:].split("] ", 1)
            for kv in rest.split(", "):
                k, v = kv.split("=", 1)
                pairs[(k, v)] += 1
                src.setdefault((k, v), M.SRC.get((sid, k)) or "?")
    srcs = collections.Counter()
    for (k, v), c in pairs.items():
        srcs[src[(k, v)].split(":")[0]] += c
    tot = same + new + diff
    L += [f"- Keyword uses {tot}: **taken unchanged from pi-1 … pi-6** (the same value as a pi-1 … pi-6 mapping of "
          f"that keyword or of its base form, R1) **{same}** (in {len(same_kw)} keywords); a keyword that pi-1 … pi-6 "
          f"never mapped {new}; a value different from pi-1 … pi-6 {diff} (in {len(diffs)} keyword / value pairs, "
          f"listed below with the reason).",
          "- Source of the values (uses): " + ", ".join(f"{x} {c}" for x, c in srcs.most_common()) +
          " (frame / stock = the module tables; cond / vara / order / count / samutthana / title = the Paṭṭhāna "
          "families T1-T6, T12; headlex = the heading lexicon T9; verb = T10; terms = my7-zeroshot-terms (T11); lex = "
          "LEXW (T11); pi-N = a pi-N value; base = R1 on a table value; term = T7 / T8 / T12 / T13; ctx = the one "
          "per-segment override).", "", RULES,
          "## Values different from pi-1 … pi-6 (same keyword)", "",
          "| keyword = pi-7 value | pi-1 … pi-6 value (uses here) | reason |", "|---|---|---|"]
    for (k, v), c in sorted(diffs.items(), key=lambda x: -sum(x[1].values())):
        L.append(f"| {k} = {v} | " + "; ".join(f"{p} ({n})" for p, n in c.items()) + f" | {reason(k)} |")
    rk = collections.Counter()
    ex = {}
    for ch in R.SAMPLE:
        for sid, k, c, r in R.verify_file(ch)[4]:
            rk[r] += 1
            ex.setdefault(r, f"^{sid} {k}: «{c}»")
    L += ["", "## Presence: chunks matched by an ending rule (no other exception)", "",
          "Every chunk of every value stands in its segment's Burmese, literally or by one of the approved ending rules "
          "of the verifier (pi-1 rules 3 / 4 / 8, pi-2 N11, pi-3 M7, pi-4 P3 / A2, pi-5 Q1, pi-6 phase 3): no presence "
          "failure and no exception outside these rules.", "", "| rule | chunks | example |", "|---|---|---|"]
    for r, c in rk.most_common():
        L.append(f"| {r} | {c} | {ex[r]} |")
    L += ["", FRAME_TABLE(), "", "## Keyword → Burmese (sample chapters; uses; source)", "",
          "| keyword | Burmese | uses | source |", "|---|---|---|---|"]
    for (k, v), c in sorted(pairs.items(), key=lambda x: (R.low(x[0][0]), x[0][1])):
        L.append(f"| {k} | {v} | {c} | {src[(k, v)]} |")
    (HERE / "map-table.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def FRAME_TABLE():
    """the frame keyword → Burmese table of the module (the 24 conditions in every case and polarity, the vāra names,
    the orders, the counts), generated from the module so that it cannot drift from it."""
    L = ["## Frame keywords → Burmese (the module's families; every phase-2 agent gets these)", "",
         "### T1-T4: the 24 conditions (X = the Pāli stem; N = the bare name)", "",
         "| X | N (bare, ghaṭanā) | Xpaccayo / -ena / -oti / -opi (name) | Xpaccayā (ablative) | Xe / Xyā (count) | "
         "naXpaccayo / naXe | naXpaccayā |", "|---|---|---|---|---|---|---|"]
    for s, n in R.CONDS:
        L.append(f"| {s} | {n} | {R.cname(s)} | {R.cabl(s)} | {R.cname(s)} | {R.cname(s, True)} | {R.cabl(s, True)} |")
    L += ["", "Other condition forms (the same N): X-mūlakaṃ «Nဟူသော အကြောင်းကို အခြေခံခြင်း»; X-dukaṃ «Nဟူသော အကြောင်း၏ "
          "နှစ်မျိုးတွဲ» (naX «… မဟုတ်ခြင်း၏ …»); X-paccayādi «… စသည်»; X-sabhāgaṃ «Nဟူသော အကြောင်းနှင့် တွဲဖက်သည်» "
          "(rule 1: «များ» goes); X-ghaṭanā «Nဟူသော အကြောင်း၏ ပေါင်းစပ်ချက်»; sa-X «Nဟူသော အကြောင်း ပါဝင်သော» (in a hyphen "
          "compound «Nဟူသော အကြောင်း … ပါဝင်သော»); X-paccayasadisaṃ «Nဟူသော အကြောင်းနှင့် တူသည်», a bare X-sadisaṃ "
          "«Nနှင့် တူသည်» (harmonise H19), the text's adverbial «…နှင့် တူအောင်» before «ပြုရမည် / ချဲ့ရမည်»; a hyphen-"
          "compound part «Napacchājāta-» takes the case of the whole compound (T4: name in a heading, ablative before "
          "«-paccayā», bare in a ghaṭanā list «-nti»).", "",
          "### T5: vāra names and orders", "", "| Pāli | Burmese |", "|---|---|"]
    for k, v in R.VARA.items():
        L.append(f"| {k}vāro (-vāre, -vārepi, -vārampi, -vāraṃ …) | {v}အလိုက် ဖော်ပြချက် |")
    L += ["| X-vārādi | Xအလိုက် ဖော်ပြချက် စသည် |", "| X-vārasadisaṃ / -ā / -o | Xအလိုက် ဖော်ပြချက်နှင့် တူသည် "
          "(adverbial «…နှင့် တူအောင်») |"]
    for k in ("anulomaṃ", "paccanīyaṃ", "anulomapaccanīyaṃ", "paccanīyānulomaṃ", "Paccayānulomaṃ",
              "Paccayapaccanīyaṃ", "Paccayānulomapaccanīyaṃ", "Paccayapaccanīyānulomaṃ", "Dhammānulome",
              "Dhammapaccanīye", "anulome", "Paccanīyagaṇanā", "anulomamātikā"):
        L.append(f"| {k} | {R.order_cands(k)[0]} |")
    L += ["", "### T6: counts and counting groups", "",
          "| Pāli | Burmese |", "|---|---|",
          "| ekaṃ … dasa, ekādasa … ekūnapaññāsa (answers) | the text's count + «ခု» (တစ်ခု … ဆယ်ခု, ဆယ့်တစ်ခု, "
          "နှစ်ဆယ့်တစ်ခု, သုံးဆယ့်ခုနစ်ခု …) |",
          "| eko / dve / tayo / cattāro (khandha, mahābhūta) | the text's count + «ပါး» |",
          "| dukaṃ, tikaṃ, catukkaṃ … catuvīsakaṃ | နှစ်မျိုးတွဲ, သုံးမျိုးတွဲ, လေးမျိုးတွဲ … နှစ်ဆယ့်လေးမျိုးတွဲ |",
          "| Paccayacatukkaṃ | အကြောင်း လေးမျိုးတွဲ |",
          "| Ekamūlakaṃ / Dumūlakaṃ … tevīsatimūlakaṃ / Sabbamūlakaṃ | အကြောင်း တစ်ခုကို / နှစ်ခုကို … နှစ်ဆယ့်သုံးခုကို / "
          "အားလုံးကို အခြေခံခြင်း |", "| Pañcamūlakādikā | အကြောင်း ငါးခုကို အခြေခံခြင်း စသည် |",
          "| tevīsatipaccayā | အကြောင်း နှစ်ဆယ့်သုံးပါး |",
          "| X-paṭṭhānaṃ (tika, duka, dukatika, tikaduka, tikatika, dukaduka) | Xတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ |", "",
          "### Stock frame words (FRAME / STOCK / LEXW; the full lists are in map7_rules.py)", "",
          "| Pāli | Burmese | Pāli | Burmese |", "|---|---|---|---|"]
    items = [(k, v) for k, v in list(R.FRAME.items()) + list(R.STOCK.items()) if k != R.NONE]
    rows = []
    for k, v in items:
        if isinstance(v, str) and v.startswith("@alt:"):
            v = " / ".join(x for x in v[5:].split("|") if x != "@prior") + " (alt)"
        elif isinstance(v, str) and v.startswith("@"):
            v = f"context function {v[1:]}"
        rows.append((k, v))
    for i in range(0, len(rows), 2):
        a = rows[i]
        b = rows[i + 1] if i + 1 < len(rows) else ("", "")
        L.append(f"| {a[0]} | {a[1]} | {b[0]} | {b[1]} |")
    return "\n".join(L)


def main():
    M, out = run()
    for ch in R.SAMPLE:
        lines, problems, unmapped, nne = out[ch]
        n, bad, fails, punct, ruled = R.verify_file(ch)
        print(f"{ch}: lines {n} bad {bad} presence-fails {len(fails)} punct {len(punct)} unmapped {len(unmapped)} "
              f"NDE {nne} ruled {len(ruled)}")
        for x in unmapped[:40]:
            print("   UNMAPPED", x)
        for x in fails[:40]:
            print("   FAIL", x)
        for x in punct[:10]:
            print("   PUNCT", x)
    src = collections.Counter((v or "?").split(":")[0] for v in M.SRC.values())
    print("sources", src.most_common())
    same, new, diff, diffs, same_kw = compare_prior()
    print("same", same, "new", new, "diff", diff)
    if "--table" in sys.argv:
        write_table(M, out)
    if "--diff" in sys.argv:
        for (k, v), c in sorted(diffs.items(), key=lambda x: -sum(x[1].values())):
            print(f"   {k} = {v}   prior {dict(c)}   {reason(k)[:60]}")


HEAD = """# pi-7 Burmese keyword mapping, PHASE 1: rules and review table (Paṭṭhāna «အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»: preamble, 1-00-paccaya, 1-02-vedanattika)

Written by `map_sample.py --table` with the shared module `map7_rules.py` (imported by the phase-2 agents; no work at
import). Burmese from the FINAL text of this track only (`AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters`),
its term list `my7-zeroshot-terms.md`, the term tables of its generators (`make_*.py`, `my7_formulas.py`: read as text,
never imported) and the final pi-1 … pi-6 Burmese mappings; no other Burmese source. The sample chapters need no
chapter table and one per-segment override (^7-3-53 saddhāpañcamakesu, a keyword of one segment of the book).
"""

RULES = """## Rules used (binding, unchanged)

The value is the word or phrase of THAT segment's Burmese (the FINAL pi-7 text) that carries the keyword, in the
dictionary form of the approved Burmese mappings:

- **pi-1** rules 1-11 (approved 2026-11-17): nouns without final case particles / plural markers (rule 1; inner
  particles stay: «အကြောင်းများ၏ အကျယ် ဖော်ပြချက်», «ထိုအရာနှင့် ယှဉ်တွဲသော»); a noun predicated = the noun (rule 2);
  adjectives / participles «…သော», gerundives «…မည့်» (rule 3: vitthāretabbaṃ «အကျယ် ချဲ့ရမည့်»); verbs «…သည်»
  (rule 4); «X dhammā» = «X သဘောတရား» (rule 5); sentence-final material and the «၊» inside a term dropped (rule 6:
  abyākata «ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော»); titles and headings whole (rule 7); particles (rule 9: ca, pi,
  ti, siyā = (no direct equivalent) where they stand alone); « … » for discontinuous parts, no « / », no «, » / «၊» in a
  value (rule 10); sense by context, one sense per segment (rule 11). The agreed later pi-1 rules: absolutives keep
  «…၍» (paṭicca «မှီ၍», ārabbha «အာရုံပြု၍»); counts keep the text's classifier.
- **pi-2** N1-N11 and the harmonise decisions: the ablative of cause keeps «ကြောင့်» (pi-2 avijjāpaccayā «အမှန်ကို
  မသိမှုကြောင့်»: here Xpaccayā «Nဟူသော အကြောင်းကြောင့်»); one Burmese word for two compound members: one member gets it,
  the other (no direct equivalent) (here karoti / katvā after an act compound).
- **pi-3** M1-M9 (the « … » gap; the presence endings of M7); **pi-4** P1-P8 (agent nouns «…သူ» P6: vuṭṭhahantassa
  «ထမြောက်နေသူ», vippaṭisārissa «နောင်တ ရသူ»; the presence endings P3; A2 «X၍» against «မXဘဲ»).
- **pi-5** Q1-Q8 (Q1 presence endings «…သလော / …ပါ / …ပြီး»: the pucchāvāra «ဖြစ်ပေါ်နိုင်သလော»; Q4 the «လည်း» of ca is
  not part of a keyword; Q5 negated verbs «မ + verb» without «သည်»), S1 (stem fallback, with the pi-7 guard M1 below).
- **pi-6** R1 («-ti» / «ca» / «pi» forms = the base form's value: Hetupaccayoti, taṃsampayuttakānañca, kusalañca,
  tikañca), R2 (verbs in every tense and polarity), R6 (headings), R7 (the «လည်း» gap inside one value), R8 (-samaṅgī
  «Xနှင့် ပြည့်စုံသူ», moments «… ခဏ» without «၌»), R9; the five phase-3 mechanics (the literal tier needs phrase_ok,
  base_forms skips a finite «-anti», …, the «Xပြီး မဟုတ်» ending); the pi-6 orders anuloma / paccanīka «အဟုတ်ပြ / အငြင်းပြ
  ပုံစံ» (reused by the pi-7 text, notes-sample).
- **pi-1 … pi-6 values**: a keyword the module tables and families do not settle is looked up in the FINAL pi-1 … pi-6
  mappings (`AI_translation/burmese/pi-{1,…,6}-keywords-by-reference-pali-burmese-plain.md`; order pi-2, pi-3, pi-4,
  pi-5, pi-6, pi-1): the most frequent value the segment has as a phrase, then one whose chunks are all literal and
  together, then one present by an ending rule. A pi-1 … pi-6 value that stands in the segment only inside another
  word or another phrase is not taken (it is not the keyword's word there; such cases are listed below).

## How the module is built (`map7_rules.py`)

Lookup per keyword (single-word keywords: the 75 keyword files have no multiword keyword): CTX[segment] → chapter table
→ FRAME → STOCK (a book-wide value is taken only where the segment has it) → the Paṭṭhāna families (T1-T6: conditions,
vāras, orders, counts, -samuṭṭhāna, titles) → the heading lexicon (T9) → verbs (T10) → the same for the base forms (R1)
→ pi-7 terms (T11) → a pi-1 … pi-6 value (contiguous) → LEXW (T11) → a pi-1 … pi-6 value (other tiers) → the term
family (T7 generator terms and case siblings, T8 na-X / no-X, T13 cluster dyads, T12 head compounds) → the heading rule
(R6) → the stem fallback (S1 with M1). Every family value is a list of candidates checked against the segment
(`pick_phrase`): the text's own form wins. A value «@name» calls a context function (FUNCS: f_rupam, f_paccayo,
f_natthi, f_karoti); a tuple = the first value the segment has (alt). Every value then gets R7 and loses a list comma
(rule 6). `Mapper(chapter_tables=…, ctx=…, stem=make_stem([FRAME, STOCK, LEXW, …]))` is the entry point,
`verify_file(ch)` the verifier, `frame_coverage.py` the whole-book check. Lookups are cached per segment.

## NEW rules (beyond pi-1 … pi-6), for review

T1. **The 24 condition names** (my7_formulas CONDS; notes-sample «The 24 names»): the bare name N (ghaṭanā lists and
    hyphen compounds: «Hetu-sahajāta-…-avigatanti tīṇi» «အမြစ်၊ အတူ ပေါ်ပေါက်ခြင်း၊ … ဟူသော ပေါင်းစပ်ချက်၌ သုံးခု»:
    sahajāta = အတူ ပေါ်ပေါက်ခြင်း); the name «Nဟူသော အကြောင်း» for Xpaccayo / Xpaccayoti / Xpaccayopi (R1, Q4: the
    «ကိုလည်း» goes) and for the instrumental Xpaccayena (pi-5 hetupaccayena «အမြစ်ဟူသော အကြောင်း», binding: the «ဖြင့်»
    goes, rule 1); the negative «Nဟူသော အကြောင်း မဟုတ်ခြင်း» (Nahetupaccayo); paccayo itself «အကြောင်း» (pi-5).
T2. **Cases of the counting frames**: the ablative Xpaccayā «Nဟူသော အကြောင်းကြောင့်» (pi-2: the cause marker «ကြောင့်»
    is the keyword's meaning and stays), naXpaccayā «Nဟူသော အကြောင်းကြောင့် မဟုတ်» (pi-1 rule 9 «… မဟုတ်»; the adverbial
    «ဘဲ» of «မဟုတ်ဘဲ» goes, rule 6); the counting locative Xe / Xyā «Nဟူသော အကြောင်း» (rule 1: «၌» goes), naXe / noXe
    «Nဟူသော အကြောင်း မဟုတ်ခြင်း». A locative that is not a condition in the segment (kamme, magge, jhāne in a deed)
    falls through to its plain value (one sense per segment: the condition wins where the segment has it).
T3. **«Xpaccayena paccayo»**: Xpaccayena = the name (T1), paccayo «အကြောင်း» (f_paccayo); the text's «ဖြင့် … ဖြစ်သည်»
    are case and sentence-final material.
T4. **Hyphen-compound parts take the compound's case** (compound_form): «Napacchājāta-naāsevanapaccayā» in a heading
    names the conditions (Napacchājāta «နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း»), before «-paccayā» in a body
    line it is the ablative («naārammaṇa-…-noatthipaccayā» naārammaṇa «အာရုံဟူသော အကြောင်းကြောင့် မဟုတ်»), in a ghaṭanā
    list the bare name; sa-X «(saupanissayaṃ)» «အားကြီးသော အမှီဟူသော အကြောင်း ပါဝင်သော», «Saindriya-maggaghaṭanā»
    Saindriya «စွမ်းရည်ဟူသော အကြောင်း … ပါဝင်သော» (rule 10: the text closes the compound with one «ပါဝင်သော»).
T5. **Vāras and orders** (my7-zeroshot-terms §2): a vāra in any case «Xအလိုက် ဖော်ပြချက်» (pi-2 / pi-6; rule 1 / Q4: the
    case particle and the «လည်း» of -pi go), -ādi «… စသည်», -sadisa «…နှင့် တူသည်» (rule 4; the text's «တူကြသည်» by the
    ending rule; its adverbial «…နှင့် တူအောင်» before an imperative); anuloma / paccanīya and their compounds with
    paccaya- / dhamma- (Paccayānulomaṃ «အကြောင်း အဟုတ်ပြ ပုံစံ», Dhammānulome «သဘောတရား အဟုတ်ပြ ပုံစံ»), -gaṇanā «…၏
    ရေတွက်ချက်», -mātikā «…၏ ခေါင်းစဉ်စာရင်း».
T6. **Counts**: an answer count = the text's number word + «ခု» (pi-1 decision 5: the text's classifier; Pāli
    compound numbers parsed: ekavīsa «နှစ်ဆယ့်တစ်ခု», sattatiṃsa «သုံးဆယ့်ခုနစ်ခု»), khandha / mahābhūta counts «… ပါး»;
    counting groups «Nမျိုးတွဲ» (pi-1 tika / duka); counted mūlakas «အကြောင်း Nခုကို အခြေခံခြင်း»; X-paṭṭhānaṃ titles
    «Xတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ».
T7. **Term qualifiers in any case**: the value of a triad / dyad term does not depend on its case (rule 1 / rule 3):
    the term tables of the pi-7 generators (the stems «upādinnupādāniy», «sanidassanasappaṭigh» … with a case ending;
    read as text), the pi-1 … pi-6 value of a case sibling (savitakkasavicāro ↔ -ā ↔ -aṃ; a-, i- and u-stems; pi-1's
    spelling «upādiṇṇ» for the pi-7 «upādinn»); the stacked qualifiers «A၊ B N» of the dukatika / tikaduka (harmonise
    H6) give each keyword its own attributive without the «၊» (rule 6).
T8. **na-X / no-X terms** (harmonise H21, the text's rule): na + an attributive «Xသော» = «Xသည် မဟုတ်သော» (naabyākato
    «ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သည် မဟုတ်သော»), na + a noun term «X» = «X မဟုတ်သော» (nakusalo «ကုသိုလ်
    မဟုတ်သော», nahetuṃ «အမြစ် မဟုတ်သော», nosaññojanaṃ «နှောင်ကြိုး မဟုတ်သော»).
T9. **The heading lexicon**: every heading line of the book whose Pāli and Burmese have the same number of parts gives
    its parts as a lexicon (rule 7: a heading keyword that is a whole heading part takes the whole part, in dictionary
    form: Vedanāttikaṃ «ခံစားမှု သုံးမျိုးတွဲ», Suddhaṃ «ရိုးရိုး», Paccanīyuddhāro «အငြင်းပြ ပုံစံအတွက် ထုတ်နုတ်ချက်»);
    the same keyword in a note takes the same value where the segment has it.
T10. **Verbs of the frames**: uppajjati / uppajjanti «ဖြစ်ပေါ်သည်» (pi-1 … pi-6; the plural «ကြ» by the ending rule);
    the optative uppajjeyya / uppajjeyyuṃ of «Siyā … uppajjeyya» = the text's potential «ဖြစ်ပေါ်နိုင်သည်» (Q1 ending
    «သလော»; siyā has no word: rule 9).
T11. **The pi-7 phrase lexicon word by word** (LEXW, reviewed; my7 LEX): each Pāli word of «dānaṃ datvā», «sīlaṃ
    samādiyitvā», «mātaraṃ jīvitā voropeti», «pariyiṭṭhimūlakaṃ dukkhaṃ paccanubhoti» … gets the part of the text's phrase
    that carries it; an act compound whose Burmese carries the verb («uposathakammaṃ» «ဥပုသ်ကို စောင့်ထိန်းသည်»,
    «gāmaghātaṃ» «ရွာကို ဖျက်ဆီး၍ လုယက်သည်», «ekāgārikaṃ») takes the verb, and karoti / katvā after it is (no direct
    equivalent) (pi-2 harmonise; f_karoti: only where every karoti / katvā of the segment follows such a compound);
    the kamma kinds sahajātā / nānākkhaṇikā = the adjective (the label's «ကံ» is the frame's head noun, harmonise H7).
T12. **Compound terms with a known head**: «X-samuṭṭhāna» «Xမှ ဖြစ်ပေါ်လာသော» (pi-2 cittasamuṭṭhāna; utu «ရာသီဥတု»,
    āhāra «အာဟာရ»; the text's supplied «ရုပ်» is not part of the keyword, harmonise H8 item 4); «X-adhipati» «X
    အကြီးအမှူး» (ārammaṇādhipati «အာရုံ အကြီးအမှူး», sampayuttādhipati «ယှဉ်တွဲသော အကြီးအမှူး»; the triad term
    maggādhipati «မဂ်ကို အကြီးအမှူးပြုသော»); «X-cittasamaṅgissa» «X စိတ်နှင့် ပြည့်စုံသူ» (pi-6 R8, pi-4 P6); «X-purejātaṃ»
    «X ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း» (vatthupurejātaṃ «မှီရာ ဝတ္ထု ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း»); «X-sahagata» «Xနှင့်အတူ ဖြစ်သော»
    (pi-1).
T13. **The cluster dyads of the gocchakas** (burmese-style cluster names; pi-1 rule 3): the item «N ဖြစ်သော»,
    X-sampayutta «Nနှင့် ယှဉ်တွဲသော», X-vippayutta «Nနှင့် ကင်းကွာသော», X-iya / sa-X «N၏ အာရုံ ဖြစ်နိုင်သော» (saññojano
    «နှောင်ကြိုး ဖြစ်သော», sāsavo «စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော»).
M1. **S1 guard** (mechanic): a stem donor's value must have the keyword's grammatical shape: a verb value «…သည် / …၍»
    never goes to a noun keyword (the dry run had nibbānaṃ «ဖြစ်ပေါ်သည်» from nibbattati), a finite verb keyword gets
    «…သည်» (passati «မြင်သည်» from the participle «မြင်သော»), an absolutive «…၍» (bhinditvā «ဖြိုခွဲ၍»), a gerundive
    «…ရမည့်»; otherwise no value.
M2. **A book-wide table value is taken only where the segment has it** (FRAME / STOCK): otherwise the chain goes on
    (a CTX or chapter-table value is final).

"""

if __name__ == "__main__":
    main()
