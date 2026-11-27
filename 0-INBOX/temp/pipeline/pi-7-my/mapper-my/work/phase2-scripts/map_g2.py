"""pi-7 Burmese keyword mapping, PHASE 2, group g2: the part-2 triads 2-01 vitakkattika … 2-17 sanidassanasappaṭighattika.

Imports the shared module map7_rules.py (never edits it) and holds only the g2 chapter tables, the g2 per-segment
overrides and two g2 context functions. Writes <ch>.mapped.md for the 17 chapters and prints the three verify checks
of the phase-1 brief per chapter (keyword preservation `bad`, presence failures, «, » / «၊» / « / » in a value), the
(no direct equivalent) count and the S1 (stem fallback) uses with their review status. Notes: notes-g2.md.
Run: /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 map_g2.py
"""
import sys
import re
import pathlib

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import map7_rules as R          # noqa: E402

GROUP = "g2"
CHAPTERS = ["2-01-vitakkattika", "2-02-pitittika", "2-03-dassanenapahatabbattika",
            "2-04-dassanenapahatabbahetukattika", "2-05-acayagamittika", "2-06-sekkhattika", "2-07-parittattika",
            "2-08-parittarammanattika", "2-09-hinattika", "2-10-micchattaniyatattika", "2-11-maggarammanattika",
            "2-12-uppannattika", "2-13-atitattika", "2-14-atitarammanattika", "2-15-ajjhattattika",
            "2-16-ajjhattarammanattika", "2-17-sanidassanasappatighattika"]

_SP = re.compile(r"(?<=[.)?])\s+")
_SB = re.compile(r"(?<=[။)?])\s+")


def aligned(kw, pali, my):
    """the Burmese sentences aligned (same index) with the Pāli sentences that hold the keyword as a word; None where
    the sentence counts differ or the keyword is not found."""
    ps, bs = _SP.split(pali), _SB.split(my)
    if len(ps) != len(bs):
        return None
    rx = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])" + re.escape(kw) + r"(?![\wāīūṃṅñṭḍṇḷ])")
    out = [bs[i] for i, s in enumerate(ps) if rx.search(s)]
    return out or None


def f_natthi_g2(kw, pali, my):
    """natthi (G2-1): the module's f_natthi takes «မရှိသည်» wherever the segment has it as a phrase; where every
    sentence that holds natthi has only the bare «မရှိ» (a note «(… paṭisandhikkhaṇe natthi)» «(… ခဏ၌ မရှိ)»), the value
    is the text's «မရှိ» (pi-5 Q5), as phase 1 decided for the notes. Everything else: the module unchanged."""
    v = R.f_natthi(kw, pali, my)
    if v == "မရှိသည်":
        ss = aligned(kw, pali, my)
        if ss and all("မရှိ" in s and not R.phrase_ok("မရှိသည်", s) for s in ss):
            return "မရှိ"
    return v


FUNCS = {"natthi_g2": f_natthi_g2}

# One table for every g2 chapter: only keywords the module leaves unmapped in g2, and the module overrides (tuples =
# the first value the segment has as a phrase, R.alt). Values: the text's phrase in dictionary form (pi-1 rules 1-11,
# pi-5 participles «…သော», pi-1 gerundives «…ရမည့်», absolutives «…၍», rule 10 « … » for discontinuous parts).
G2 = {
    # --- module overrides (listed in notes-g2.md «Module overrides»)
    "kāraṇena": ("နည်းလမ်း", "အကြောင်း"),        # «iminā kāraṇena» «ဤနည်းလမ်းဖြင့်» (rule 1); pi-5 «အကြောင်း» only elsewhere
    "natthi": "@natthi_g2",                        # G2-1
    "suciṇṇāni": ("ကောင်းစွာ ကျင့်ခဲ့ဖူးသော", "ကောင်းစွာ ပြုခဲ့ဖူးသော"),   # the frame value, else the text's «… ပြုခဲ့ဖူးသည်တို့»
    # sekkha / asekkha as a qualifier (of dhamma, khandha, phala): the pi-1 / pi-2 value «…၏» (Sekkhaṃ, Sekkho, sekkho,
    # Asekkho …, binding) for every case form, T7; the term family gave the bare person noun. The person nouns sekkhā /
    # Sekkhā / Sekkhānaṃ («ကျင့်ကြံဆဲသူတို့») keep the module's «ကျင့်ကြံဆဲသူ».
    "sekkhassa": ("ကျင့်ကြံဆဲသူ၏", "ကျင့်ကြံဆဲသူ"), "sekkhe": ("ကျင့်ကြံဆဲသူ၏", "ကျင့်ကြံဆဲသူ"),
    "Sekkhañca": ("ကျင့်ကြံဆဲသူ၏", "ကျင့်ကြံဆဲသူ"), "sekkhañca": ("ကျင့်ကြံဆဲသူ၏", "ကျင့်ကြံဆဲသူ"),
    "asekkhassa": ("ကျင့်ကြံမှု ပြီးဆုံးသူ၏", "ကျင့်ကြံမှု ပြီးဆုံးသူ"),
    "asekkhe": ("ကျင့်ကြံမှု ပြီးဆုံးသူ၏", "ကျင့်ကြံမှု ပြီးဆုံးသူ"),
    # plural verbs without the plural «ကြ» (rule 4, T10: «ကြ» by the ending rule), as samāpajjanti «ဝင်စားသည်» and
    # paccavekkhanti «ပြန်လည် ဆင်ခြင်သည်»; the term family gave «ဖြစ်စေကြသည် / ထိုးထွင်း၍ ရှုကြသည်»
    "uppādenti": "ဖြစ်စေသည်", "vipassanti": "ထိုးထွင်း၍ ရှုသည်",
    # gerundives in every case «…ရမည့်» (pi-1 rule 3, as the frame's gaṇetabbaṃ / vitthāretabbā); the term family gave
    # the text's finite «…ရမည်»
    "gaṇetabbā": "ရေတွက်ရမည့်", "gaṇetabbāni": "ရေတွက်ရမည့်", "gaṇetabbo": "ရေတွက်ရမည့်",
    "vitthāretabbāni": "အကျယ် ချဲ့ရမည့်",
    # paripuṇṇa: the frame's adjective «ပြည့်စုံသော» (rule 3; the text's «ပြည့်စုံသည် / ပြည့်စုံကြသည်» by the attr
    # ending) for every case form, the text's adverb «ပြည့်စုံစွာ» where it has only that; the terms stem «ပြည့်စုံ» last
    "paripuṇṇaṃ": ("ပြည့်စုံသော", "ပြည့်စုံစွာ", "ပြည့်စုံ"), "Paripuṇṇaṃ": ("ပြည့်စုံသော", "ပြည့်စုံစွာ", "ပြည့်စုံ"),
    "paripuṇṇā": ("ပြည့်စုံသော", "ပြည့်စုံစွာ", "ပြည့်စုံ"),
    # uposathakammaṃ cut off by …pe…: the text's noun «ဥပုသ် စောင့်ထိန်းခြင်း» where it has it (U2: the compound takes
    # its whole act), else the module's values
    "uposathakammaṃ": ("ဥပုသ်ကို စောင့်ထိန်းသည်", "ဥပုသ် စောင့်ထိန်းခြင်း", "ဥပုသ်"),
    # --- gerundives «…ရမည့်» (pi-1 rule 3; the text's «…ရမည်» by the attr-fut ending)
    "dassetabbo": "ပြသရမည့်",
    "uddharitabbā": "ထုတ်နုတ်ရမည့်",
    "dīpetabbā": "ဖော်ပြရမည့်", "dīpetabbo": "ဖော်ပြရမည့်",
    "niyāmetabbaṃ": "သတ်မှတ်ရမည့်", "niyāmetabbāni": "သတ်မှတ်ရမည့်",
    "kātabbāni": "ပြုရမည့်",
    "niddisitabbaṃ": "ညွှန်ပြရမည့်",
    # --- verbs, participles, absolutives
    "āgacchati": "ပါဝင်လာသည်",                    # «… ပါဝင်လာ၏» (verb ending «၏»)
    "gacchantena": "တွဲ၍ သွားစေလျက်",             # -antena = the text's adverbial «…လျက်» (as the frame's anumajjantena)
    "asammohantena": "မရောထွေးစေဘဲ",              # -antena: the text's «မရောထွေးစေဘဲ» (as anumajjantena)
    "passitvā": "ကြည့်၍",                          # «passitvā kātabbaṃ» «ကြည့်၍ ပြုရမည်»; pi-4 «မြင်၍» not in the segment
    "vibhajitvā": "ခွဲခြမ်းစိတ်ဖြာ၍",
    "likhitā": "ရေးထားသော",                       # «na likhitā» «မရေးထားသော» (na is no keyword)
    "gahite": "ယူသော",                            # «naārammaṇe gahite» «… ကို ယူသောအခါ» (rule 3)
    # --- nouns and terms
    "paṭhamaudāharaṇe": "ပထမ ဥပမာ",
    "sattasu": "ခုနစ်ခု",                          # «sattasu ṭhānesu» «နေရာ ခုနစ်ခု၌» (T6 classifier, rule 1)
    "vicākānaṃ": "ကံ၏ အကျိုး ဖြစ်သော",              # Pāli slip for vipākānaṃ (notes §text); the text has vipāka's value
    "gamanāni": "သွားပုံ",                         # «Tāniyeva ca gamanāni» «ထို သွားပုံများကိုပင်လည်း»
    "Sakabhaṇḍe": "မိမိ ပစ္စည်း",
    "pavattipaṭisandhi": ("ဘဝ ဖြစ်စဉ် … ပဋိသန္ဓေ", "ဘဝ ဖြစ်ဆဲ ကာလ … ပဋိသန္ဓေ"),   # dvandva, «…၌လည်း၊ …၌လည်း» (rule 10)
    "missagataṃ": "ရောစပ်ချက်",
    "missakapañhā": "ရောစပ် ပြဿနာ",
    "pāḷiyaṃ": "ပါဠိတော်",
    "ārammaṇaupanissayā": "အာရုံဖြင့် အားကြီးသော အမှီ",   # = the module's ārammaṇūpanissayo (terms)
    "viññāṇañcāyatanakiriyassa": "အဆုံး မရှိသော သိစိတ် နယ်ပယ် ပြုရုံမျှသာ ဖြစ်သော",   # kiriya adjective, no «စိတ်» (§A 5)
    "nevasaññānāsaññāyatanakiriyaṃ":
        "မှတ်သိမှု ရှိသည်လည်း မဟုတ် မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ် ပြုရုံမျှသာ ဖြစ်သော",
    "Paṭhamassa": "ပထမ",
    "kusalasamāpattiṃ": "ကုသိုလ် သမာပတ်",
    "kiriyasamāpattiṃ": "ပြုရုံမျှသာ ဖြစ်သော သမာပတ်",
    "atthappaṭisambhidāya": "အကျိုးအနက်ကို ပိုင်းခြားသိသော ဉာဏ်",          # pi-2 atthapaṭisambhidā
    "paṭibhānappaṭisambhidāya": "ဉာဏ်ပေါ်မှုကို ပိုင်းခြားသိသော ဉာဏ်",      # pi-2 paṭibhānapaṭisambhidā
    "ṭhānāṭhānakosallassa": ("ဖြစ်နိုင်ခြင်းနှင့် မဖြစ်နိုင်ခြင်း၌ ကျွမ်းကျင်ခြင်း",   # inner «၌» stays (rule 1); the text
                             "ဖြစ်နိုင်သော အကြောင်းနှင့် မဖြစ်နိုင်သော အကြောင်း၌ ကျွမ်းကျင်မှု"),   # has two forms (notes)
    "dassitanayena": "ပြထားသော နည်းအတိုင်း",       # «dve kātabbā dassitanayena» «ပြထားသော နည်းအတိုင်း နှစ်ခုကို ပြုရမည်»
    "paṭhamajjhānapaccavekkhaṇaṃ": "ပထမ ဈာန်ကို ပြန်လည် ဆင်ခြင်ခြင်း",
    "maggapaccavekkhaṇaṃ": "မဂ်ကို ပြန်လည် ဆင်ခြင်ခြင်း",
    "appamāṇārammaṇaappamāṇacittasamaṅgissa": "အတိုင်းအဆ မရှိသည်ကို အာရုံပြုသော အတိုင်းအဆ မရှိသော စိတ်နှင့် ပြည့်စုံသူ",
    "ajjhattārammaṇabahiddhācittasamaṅgissa": "မိမိ၌ ရှိသည်ကို အာရုံပြုသော မိမိ၏ ပြင်ပ၌ ရှိသော စိတ်နှင့် ပြည့်စုံသူ",
    "niyatamicchādiṭṭhiyā": "ကျိန်းသေသော မှားယွင်းသော အယူ",
    "paṭighātatthāya": "ချေဖျက်ရန်",               # dative of purpose «ထိုအမှုကို ချေဖျက်ရန်»
    "vaṇṇasampadaṃ": "အဆင်းအရောင် ပြည့်စုံခြင်း",    # X-sampadā «X ပြည့်စုံခြင်း» (pi-4 sīlasampadā)
    "saddasampadaṃ": "အသံ ပြည့်စုံခြင်း",
    "gandhasampadaṃ": "အနံ့ ပြည့်စုံခြင်း",
    "phoṭṭhabbasampadaṃ": "အထိအတွေ့ ပြည့်စုံခြင်း",
    "sotasampadaṃ": "နား ပြည့်စုံခြင်း",
    "cakkhusampadaṃ": "မျက်စိ ပြည့်စုံခြင်း",
    "ghānasampadaṃ": "နှာခေါင်း ပြည့်စုံခြင်း",
    "paṭisandhicittaṃ": "ပဋိသန္ဓေ စိတ်",
    "aniccānupassanā": "မမြဲဟု အဖန်ဖန် ရှုခြင်း",     # pi-2 anupassanā «အဖန်ဖန် ရှုခြင်း»; inner quotative «ဟု» stays
    "pañcāyatanāni": "အာရုံခံ နယ်ပယ် ငါးပါး",         # pi-1 … pi-5 āyatanāni «အာရုံခံ နယ်ပယ်» + the text's count
    "paro": "သူတစ်ပါး",                            # pi-5 «တစ်ဦး» not in the segment
    "mātikāpadāni": "ခေါင်းစဉ်စာရင်း ပုဒ်",           # pi-1 … pi-5 mātikā + pi-2 padāni
    "pariyosānapadā": "အဆုံးသတ် ပုဒ်",
    "tividharūpasaṅgaho": "ရုပ် သုံးမျိုးကို စုစည်းခြင်း", "tividharūpasaṅgahena": "ရုပ် သုံးမျိုးကို စုစည်းခြင်း",
    "sādhukaṃ": "ကောင်းစွာ",
    "ante": "အဆုံးတိုင်း",                          # «ante ante» «အဆုံးတိုင်း၌»: the distributive «တိုင်း» (rule 1: «၌» goes)
    "Natthivigatapaccayaṃ": "မရှိခြင်းဟူသော အကြောင်း ပျောက်ကွယ်ခြင်းဟူသော အကြောင်း",   # T1 names, rule 6 (no «၊»)
    # --- neva-X / X-mūlaka terms (G2-2, G2-3)
    "nevadassanena": "သစ္စာကို မြင်ခြင်း … မဟုတ်", "Nevadassanena": "သစ္စာကို မြင်ခြင်း … မဟုတ်",
    "Avitakkavicāramattamūlakā": "စတင်ကြံစည်မှု မရှိဘဲ ဆက်လက်သုံးသပ်မှုသာ ရှိသော … အခြေခံသော",
    "Anidassanasappaṭighamūlake": "မမြင်နိုင်သော်လည်း ထိခိုက်မှု ရှိသော … အခြေခံခြင်း",
    "Anidassanasappaṭighamūlakā": "မမြင်နိုင်သော်လည်း ထိခိုက်မှု ရှိသော … အခြေခံသော",
    "Anidassanaappaṭighamūlake": "မမြင်နိုင် ထိခိုက်မှုလည်း မရှိသော … အခြေခံခြင်း",
    "anidassanaappaṭighamūlake": "မမြင်နိုင် ထိခိုက်မှုလည်း မရှိသော … အခြေခံခြင်း",
    "Anidassanaappaṭighamūlakā": "မမြင်နိုင် ထိခိုက်မှုလည်း မရှိသော … အခြေခံသော",
}
TABLES = {ch: G2 for ch in CHAPTERS}

# per-segment overrides (sid -> {kw: value}): module values that are present in the segment only as another word
CTX = {
    # «(idhāpi ārammaṇaupanissayā atthi)» «(… အမှီ ရှိသည်)»: the verb, not the condition «ရှိခြင်း» of atthipaccaye
    "7-10-112": {"atthi": "ရှိသည်"},
    # «pariyiṭṭhimūlakaṃ dukkhaṃ paccanubhoti» «ရှာမှီးခြင်းကို အရင်းခံသော ဆင်းရဲကို ခံစားသည်» (the segment has no
    # kāyikaṃ dukkhaṃ; pi-2 «နာကျင်မှု» stands only in «kāyikassa dukkhassa»)
    "7-11-54": {"dukkhaṃ": "ဆင်းရဲ"},
}

# S1 review: every stem-fallback value of g2, checked by eye against the segment and the keyword's sense
S1_KEPT = {
    ("passati", "မြင်သည်"): "«rūpaṃ passati» «အဆင်းအရောင်ကို မြင်သည်»",
    ("vibhajitabbaṃ", "ခွဲခြမ်းစိတ်ဖြာရမည့်"): "«iminā kāraṇena vibhajitabbaṃ» «… ခွဲခြမ်းစိတ်ဖြာရမည်»",
    ("Gaṇanāya", "ရေတွက်ချက်"): "«Gaṇanāya upadhāretvā» «ရေတွက်ချက်၌ သေချာ စဉ်းစား၍»",
    ("gaṇanāni", "ရေတွက်ချက်"): "«cattāripi gaṇanāni» «ရေတွက်ချက် လေးခုလုံး»",
    ("bhinditvā", "ဖြိုခွဲ၍"): "«saṅghaṃ bhinditvā» «သံဃာကို ဖြိုခွဲ၍»",
    ("uppādetvā", "ထွက်စေ၍"): "«lohitaṃ uppādetvā» «သွေးကို ထွက်စေ၍»",
    ("ninnānākaraṇā", "ကွဲပြားချက် မရှိ"): "«ninnānākaraṇā» «ကွဲပြားချက် မရှိ» (Q5)",
    ("patthayamāno", "တောင့်တသော"): "-amāno «…သော» (pi-5 vediyamāno); the text's «တောင့်တလျက်» by the attr ending",
    ("samenti", "ညီသည်"): "«na samenti» «မညီကြ»: na is no keyword, the verb in dictionary form (neg-verb ending)",
}
S1_CORRECTED = {}


def mapper():
    return R.Mapper(chapter_tables=TABLES, ctx=CTX, funcs=FUNCS, stem=R.make_stem([R.FRAME, R.STOCK, R.LEXW]))


def main():
    M = mapper()
    tot = {"lines": 0, "bad": 0, "fails": 0, "punct": 0, "nne": 0, "unmapped": 0, "stem": 0}
    stem_uses = []
    for ch in CHAPTERS:
        lines, problems, unmapped, nne = M.map_chapter(ch)
        (HERE / f"{ch}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        n, bad, fails, punct, ruled = R.verify_file(ch)
        for sid, kws in R.keyword_rows(ch):
            for k in kws:
                if M.SRC.get((sid, k)) == "stem":
                    stem_uses.append((ch, sid, k, M.cache[(ch, sid, k)][0]))
        print(f"{ch}: lines {n}, bad {bad}, presence failures {len(fails)}, «, » / «၊» / « / » {len(punct)}, "
              f"(no direct equivalent) {nne}, unmapped {len(unmapped)}, ending-rule chunks {len(ruled)}")
        for f in fails[:5]:
            print("   FAIL", f)
        for u in unmapped[:5]:
            print("   UNMAPPED", u)
        tot["lines"] += n
        tot["bad"] += len(bad)
        tot["fails"] += len(fails)
        tot["punct"] += len(punct)
        tot["nne"] += nne
        tot["unmapped"] += len(unmapped)
    stem_uses = sorted(stem_uses)
    kept = sum(1 for u in stem_uses if (u[2], u[3]) in S1_KEPT)
    unrev = [u for u in stem_uses if (u[2], u[3]) not in S1_KEPT]
    print(f"TOTAL {GROUP}: " + ", ".join(f"{k} {v}" for k, v in tot.items() if k != "stem") +
          f"; S1 stem uses {len(stem_uses)} (reviewed kept {kept}, corrected by table {len(S1_CORRECTED)}, "
          f"unreviewed {len(unrev)})")
    for u in unrev:
        print("   S1 UNREVIEWED", u)


if __name__ == "__main__":
    main()
