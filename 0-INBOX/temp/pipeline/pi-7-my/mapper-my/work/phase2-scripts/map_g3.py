"""pi-7 Burmese keyword mapping, PHASE 2, group g3: the part-3 gocchakas 3-01 … 3-08.

Uses the shared module map7_rules.py (imported, never edited; md5 909bed2528b27eb55051c73f3ce28f81). Holds only the
chapter tables and the context functions of this group. Writes <ch>.mapped.md for the eight chapters and prints, per
chapter, the three checks of the phase-1 brief (keyword preservation, presence, punctuation), the (no direct
equivalent) count and the S1 (stem fallback) review counts. Notes: notes-g3.md.
Run: /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 map_g3.py
"""
import sys
import re
import pathlib
import collections

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import map7_rules as R          # noqa: E402

CHAPTERS = ["3-01-hetugocchaka", "3-02-culantaraduka", "3-03-asavagocchaka", "3-04-sannojanagocchaka",
            "3-05-ganthagocchaka", "3-06-oghayogagocchaka", "3-07-nivaranagocchaka", "3-08-paramasagocchaka"]

# ---------------------------------------------------------------------------------------------------------------------
# G1 (module override of T13's item value): the item term of a gocchaka dyad in any case, also with -ca / -ceva (R1),
# is the bare noun N (pi-1 rule 2 «a noun predicated = the noun»; the binding pi-1 mātikā values of the same kind of
# segment hetū «အမြစ်», āsavā «စိတ်အစွန်းအထင်း», saṃyojanā «နှောင်ကြိုး»; pi-2 āsavo / gantho / nīvaraṇaṃ / parāmāso;
# pi-5 oghaṃ). The text's «N ဖြစ်သော» is the copula of rule 2. no-X = «N မဟုတ်သော» (T8, the module's own form).
# ---------------------------------------------------------------------------------------------------------------------
ITEM_N = {k: v for k, v in R.CLUSTER.items() if k not in ("upādān", "kiles")}      # the gocchakas of this group
_ITEM = re.compile(r"^(no)?(" + "|".join(sorted(ITEM_N, key=len, reverse=True)) +
                   r")(o|aṃ|ā|assa|e|ānaṃ|añca|añceva|ānañca|āni|ova|ehi|esu)$")


def item_value(kw):
    m = _ITEM.match(R.low(kw))
    if not m:
        return None
    n = ITEM_N[m.group(2)]
    return f"{n} {R.NOT}သော" if m.group(1) else n


# ---------------------------------------------------------------------------------------------------------------------
# Group table (every chapter of g3): keywords the module leaves unmapped, and module values that are wrong here.
# A tuple = the first value the segment has (alt); a plain value is final (checked by the verifier).
# ---------------------------------------------------------------------------------------------------------------------
_SAR = "သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှု"
_ISA = "ဤအရာသာ အမှန်ဟု သက်ဝင်ယုံကြည်ခြင်း"
_DLS = "အယူမှားနှင့် ကင်းကွာသော လောဘနှင့်အတူ ဖြစ်သော"      # the stacked qualifiers «A၊ B» without the «၊» (T7)
T_G3 = {
    # module overrides (notes-g3 «Module overrides»)
    "cakkaṃ": ("စက်ဝိုင်း", "@prior"),                  # the text's word «(စက်ဝိုင်း)»; the module's «စက်» is part of it
    "tadārammaṇatā": "ထိုအာရုံကိုပင် အာရုံပြုသော အဖြစ်",   # the text's phrase (rule 1: «ဖြင့်» goes); module «စိတ်သည်»
    "pañcaviññāṇaṃ": ("သိစိတ် ငါးပါး", "@prior"),         # the text's «သိစိတ် ငါးပါး»; module «သိစိတ်»
    "paripuṇṇo": ("ပြည့်စုံသော", "ပြည့်စုံ"),             # rule 3 as FRAME paripuṇṇaṃ (text «ပြည့်စုံသည်»)
    "paripuṇṇā": ("ပြည့်စုံသော", "ပြည့်စုံ"),
    "gaṇetabbā": "ရေတွက်ရမည့်",                          # rule 3 gerundive, as FRAME gaṇetabbaṃ; module «ရေတွက်ရမည်»
    "uppādenti": "ဖြစ်စေသည်",                            # rule 4 (plural «ကြ» by the ending rule), as uppādeti
    "Nahetuṃ": "အမြစ် မဟုတ်သော", "nahetuṃ": "အမြစ် မဟုတ်သော",   # T8 term; module cond «…ကြောင့် မဟုတ်» once
    # S1 corrections (stem values checked by eye)
    "suddhake": "ရိုးရိုး အပိုင်း",                      # «… ရိုးရိုး အပိုင်း၌» (rule 1); stem «ရိုးရိုး»
    "assādanā": "သာယာ နှစ်သက်ခြင်း",                     # the noun «(… သာယာ နှစ်သက်ခြင်း မရှိ)»; stem verb «သာယာ»
    "paccavekkhitvā": ("ပြန်လည် ဆင်ခြင်၍", "@prior"),     # U3: the pi-7 word «ပြန်လည် ဆင်ခြင်»; stem «ဆင်ခြင်၍»
    # keywords the module leaves unmapped: the text's phrase in dictionary form
    "utu": "ရာသီဥတု",                                   # «… ရာသီဥတု …» (utuṃ «ရာသီဥတု», utusamuṭṭhāna)
    "pavatteyeva": "ဘဝ ဖြစ်စဉ်",                        # «ဘဝ ဖြစ်စဉ်၌ပင်» (rule 1 «၌», rule 9 eva «ပင်»)
    "pavattipaṭisandhi": "ဘဝ ဖြစ်စဉ် … ပဋိသန္ဓေ",          # «ဘဝ ဖြစ်စဉ်၌လည်း၊ ပဋိသန္ဓေ၌လည်း» (rule 10 / R7)
    "Pañcāyatanāni": "အာရုံခံ နယ်ပယ် ငါးပါး", "pañcāyatanāni": "အာရုံခံ နယ်ပယ် ငါးပါး",   # rule 1: «တို့ကို» goes
    "kātabbāni": "ပြုရမည့်",                             # rule 3 gerundive (as kātabbā / kātabbaṃ)
    "vajjetabbā": "ဖယ်ရှားရမည့်", "niyāmetabbaṃ": "သတ်မှတ်ရမည့်", "dassetabbāni": "ပြသရမည့်",
    "dassetabbaṃ": "ပြသရမည့်", "bandhitabbaṃ": "ဖွဲ့ရမည့်", "uddharitabbā": "ထုတ်နုတ်ရမည့်",
    "ninnetabbaṃ": "ထည့်သွင်းရမည့်", "parivattetabbā": "လှည့်ပြောင်းရမည့်",
    "jānitvā": "သိ၍",                                   # «… သိ၍ ပြုရမည်» (pi-1: absolutives keep «၍»)
    "vibhajantena": "ခွဲခြမ်းစိတ်ဖြာလျက်",                # the text's adverbial, as FRAME anumajjantena (H10)
    "agge": "ရှေ့ဆုံး",                                 # «… ရှေ့ဆုံးတွင် ပြုရမည်» (rule 1: «တွင်» goes)
    "ekasadisā": "တူညီသည်",                             # «သုံးခုလုံး တူညီကြသည်» (rule 4; «ကြ» by the ending rule)
    "garukārammaṇā": "လေးစားဖွယ်ရာ အာရုံ",                # «လေးစားဖွယ်ရာ အာရုံ(အဖြစ်)» (rule 1)
    "upanissayā": "အားကြီးသော အမှီ",                     # «(… အားကြီးသော အမှီ သုံးခုလုံး)»: the kind, not the name
    "nahetucittasamaṅgissa": "အမြစ် မဟုတ်သော စိတ်နှင့် ပြည့်စုံသူ",   # T12 «X-cittasamaṅgissa»
    "naviññeyyo": "မသိနိုင်သော", "naviññeyyaṃ": "မသိနိုင်သော",   # the text's «… စိတ်ဖြင့် မသိနိုင်သော» (T8 text form)
    "vaṇṇasampadaṃ": "အဆင်းအရောင် ပြည့်စုံခြင်း",
    "ṭhānāṭhānakosallassa": "ဖြစ်နိုင်ခြင်းနှင့် မဖြစ်နိုင်ခြင်း၌ ကျွမ်းကျင်ခြင်း",   # rule 1: «အား» goes
    "Dvikkhattuṃ": "နှစ်ကြိမ်", "catukkhattuṃ": "လေးကြိမ်", "ubhopete": "ထိုနှစ်ပါးလုံး",
    # -sadisa notes (T5: «…နှင့် တူသည်»; the adverbial «…နှင့် တူအောင်» before «ပြုရမည်»)
    "dutiyagamanasadisaṃ": "ဒုတိယ သွားပုံနှင့် တူအောင်",
    "lokiyadukasadisaṃ": "လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲနှင့် တူသည်",
    "paṭhamadukasadisaṃ": "ပထမ နှစ်မျိုးတွဲနှင့် တူသည်",
    "ganthadukasadisaṃ": "အထုံး နှစ်မျိုးတွဲနှင့် တူသည်",
    "parāmāsadukasadisaṃ": "မှားယွင်းသော ယူဆမှု နှစ်မျိုးတွဲနှင့် တူသည်",
    # the named saññojanas and ganthas (the text's «X နှောင်ကြိုး / X … ကိုယ် အထုံး»; rule 1: «များ / ကို / တို့အား» go)
    "kāmarāgasaññojanaṃ": "ကာမရာဂ နှောင်ကြိုး",
    "diṭṭhisaññojanaṃ": "အယူ နှောင်ကြိုး", "diṭṭhisaññojanassa": "အယူ နှောင်ကြိုး",
    "avijjāsaññojanaṃ": "အမှန်ကို မသိမှု နှောင်ကြိုး", "avijjāsaññojanassa": "အမှန်ကို မသိမှု နှောင်ကြိုး",
    "vicikicchāsaññojanaṃ": "ယုံမှားမှု နှောင်ကြိုး", "mānasaññojanaṃ": "မာန နှောင်ကြိုး",
    "sīlabbataparāmāsasaññojanaṃ": f"{_SAR} နှောင်ကြိုး",
    "saññojanasampayuttakā": "နှောင်ကြိုးနှင့် ယှဉ်တွဲသော",   # T13 X-sampayutta
    "idaṃsaccābhinivesaṃ": _ISA, "idaṃsaccābhiniveso": _ISA,  # «…ခြင်းဟူသော ကိုယ် အထုံး» (kāyaganthaṃ its own keyword)
    "idaṃsaccābhinivesakāyaganthaṃ": f"{_ISA}ဟူသော ကိုယ် အထုံး",   # as pi-1 abhijjhākāyagantho «…ခြင်းဟူသော ကိုယ် အထုံး»
    "noganthādhipati": "အထုံး မဟုတ်သော အကြီးအမှူး",           # T12 «X-adhipati»
    **{f"diṭṭhigatavippayuttalobhasahagat{e}": _DLS for e in ("ā", "e", "ānaṃ", "aṃ", "o")},
    "diṭṭhigatavippayuttalobhasahagatādhipati": f"{_DLS} အကြီးအမှူး",
}
# per-segment overrides (sid -> {kw: value}): a keyword of ONE segment
CTX = {
    # «(Ārammaṇañca sahajātañca upanissayañca … parivattetabbaṃ)» «(အာရုံဟူသော အကြောင်းကိုလည်းကောင်း …)»: the
    # condition name (T1, R1: «ကိုလည်းကောင်း» goes); the module's bare «အာရုံ» is only part of it
    "7-28-116": {"Ārammaṇañca": "အာရုံဟူသော အကြောင်း"},
}


def item_table():
    """G1 values for every item keyword of the group's keyword files (sorted: deterministic)."""
    out = {}
    for ch in CHAPTERS:
        for _, kws in R.keyword_rows(ch):
            for k in kws:
                v = item_value(k)
                if v is not None and k not in T_G3:
                    out[k] = v
    return dict(sorted(out.items()))


def tables():
    tab = {**item_table(), **T_G3}
    return {ch: dict(tab) for ch in CHAPTERS}


def mapper():
    return R.Mapper(chapter_tables=tables(), ctx=CTX, stem=R.make_stem([R.FRAME, R.STOCK, R.LEXW]))


def base_mapper():
    """the module alone (as the phase-1 dry run): for the S1 review and the override counts."""
    return R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK, R.LEXW]))


def pairs(lines):
    for l in lines:
        sid, rest = l[1:].split("] ", 1)
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            yield sid, k, v


def main():
    M, B = mapper(), base_mapper()
    tot = collections.Counter()
    s1 = collections.Counter()
    over = collections.Counter()
    newly = collections.Counter()
    for ch in CHAPTERS:
        lines, problems, unmapped, nne = M.map_chapter(ch)
        (HERE / f"{ch}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        n, bad, fails, punct, ruled = R.verify_file(ch)
        blines, _, bun, _ = B.map_chapter(ch)
        bsrc = dict(B.SRC)
        bun = set(bun)
        for (sid, k, v), (_, _, bv) in zip(pairs(lines), pairs(blines)):
            if (sid, k) in bun:
                newly[ch] += 1
            elif bsrc.get((sid, k)) == "stem":
                s1["kept" if v == bv else "corrected"] += 1
            elif v != bv:
                over[(k, bv, v)] += 1
        print(f"{ch}: lines {n} bad {bad} presence-fails {len(fails)} punct {len(punct)} unmapped {len(unmapped)} "
              f"NDE {nne} ruled {len(ruled)}")
        for x in unmapped:
            print("   UNMAPPED", x)
        for x in fails:
            print("   FAIL", x)
        for x in punct:
            print("   PUNCT", x)
        tot.update(lines=n, nde=nne, fails=len(fails), unmapped=len(unmapped), ruled=len(ruled))
    print("total", dict(tot))
    print("S1 stem uses: kept", s1["kept"], "corrected", s1["corrected"])
    print("newly mapped uses", sum(newly.values()), dict(newly))
    print("module values overridden (uses)", sum(over.values()), "in", len(over), "keyword / value pairs")
    if "--over" in sys.argv:
        for (k, bv, v), c in sorted(over.items(), key=lambda x: (R.low(x[0][0]), x[0][1], x[0][2])):
            print(f"   {k}: {bv} -> {v} ({c})")


if __name__ == "__main__":
    main()
