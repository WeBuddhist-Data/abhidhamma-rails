"""pi-7 Burmese keyword mapping, PHASE 2, group g2: the part-2 triads 2-01 vitakkattika … 2-17 sanidassanasappaṭighattika.

Imports the shared module map7_rules.py (never edits it) and holds only the g2 chapter tables, the g2 per-segment
overrides and two g2 context functions. Writes <ch>.mapped.md for the 17 chapters and prints the three verify checks
of the phase-1 brief per chapter (keyword preservation `bad`, presence failures, «, » / «၊» / « / » in a value), the
(no direct equivalent) count and the S1 (stem fallback) uses with their review status. Notes: notes-g2.md.
Run: /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 map_g2.py

Phase 3 (2026-11-26): the module overrides and the book-wide group values moved into map7_rules.py (BOOK, the module
fixes 1-9); this script keeps only what is local to the group. phase3-changes.tsv lists every value that changed.
"""
import sys
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

FUNCS = {}   # phase 3: G2-1 (f_natthi_g2) dropped: the coordinator keeps the module natthi value

# One table for every g2 chapter: only keywords the module leaves unmapped in g2, and the module overrides (tuples =
# the first value the segment has as a phrase, R.alt). Values: the text's phrase in dictionary form (pi-1 rules 1-11,
# pi-5 participles «…သော», pi-1 gerundives «…ရမည့်», absolutives «…၍», rule 10 « … » for discontinuous parts).
G2 = {
    # --- module overrides (listed in notes-g2.md «Module overrides»)
    # sekkha / asekkha as a qualifier (of dhamma, khandha, phala): the pi-1 / pi-2 value «…၏» (Sekkhaṃ, Sekkho, sekkho,
    # Asekkho …, binding) for every case form, T7; the term family gave the bare person noun. The person nouns sekkhā /
    # Sekkhā / Sekkhānaṃ («ကျင့်ကြံဆဲသူတို့») keep the module's «ကျင့်ကြံဆဲသူ».
    # plural verbs without the plural «ကြ» (rule 4, T10: «ကြ» by the ending rule), as samāpajjanti «ဝင်စားသည်» and
    # paccavekkhanti «ပြန်လည် ဆင်ခြင်သည်»; the term family gave «ဖြစ်စေကြသည် / ထိုးထွင်း၍ ရှုကြသည်»
    # gerundives in every case «…ရမည့်» (pi-1 rule 3, as the frame's gaṇetabbaṃ / vitthāretabbā); the term family gave
    # the text's finite «…ရမည်»
    # paripuṇṇa: the frame's adjective «ပြည့်စုံသော» (rule 3; the text's «ပြည့်စုံသည် / ပြည့်စုံကြသည်» by the attr
    # ending) for every case form, the text's adverb «ပြည့်စုံစွာ» where it has only that; the terms stem «ပြည့်စုံ» last
    # uposathakammaṃ cut off by …pe…: the text's noun «ဥပုသ် စောင့်ထိန်းခြင်း» where it has it (U2: the compound takes
    # its whole act), else the module's values
    # --- gerundives «…ရမည့်» (pi-1 rule 3; the text's «…ရမည်» by the attr-fut ending)
    "dīpetabbā": "ဖော်ပြရမည့်", "dīpetabbo": "ဖော်ပြရမည့်",
    "niddisitabbaṃ": "ညွှန်ပြရမည့်",
    # --- verbs, participles, absolutives
    "āgacchati": "ပါဝင်လာသည်",                    # «… ပါဝင်လာ၏» (verb ending «၏»)
    "gacchantena": "တွဲ၍ သွားစေလျက်",             # -antena = the text's adverbial «…လျက်» (as the frame's anumajjantena)
    "vibhajitvā": "ခွဲခြမ်းစိတ်ဖြာ၍",
    "likhitā": "ရေးထားသော",                       # «na likhitā» «မရေးထားသော» (na is no keyword)
    # --- nouns and terms
    "paṭhamaudāharaṇe": "ပထမ ဥပမာ",
    "sattasu": "ခုနစ်ခု",                          # «sattasu ṭhānesu» «နေရာ ခုနစ်ခု၌» (T6 classifier, rule 1)
    "vicākānaṃ": "ကံ၏ အကျိုး ဖြစ်သော",              # Pāli slip for vipākānaṃ (notes §text); the text has vipāka's value
    "gamanāni": "သွားပုံ",                         # «Tāniyeva ca gamanāni» «ထို သွားပုံများကိုပင်လည်း»
    "missagataṃ": "ရောစပ်ချက်",
    "missakapañhā": "ရောစပ် ပြဿနာ",
    "pāḷiyaṃ": "ပါဠိတော်",
    "ārammaṇaupanissayā": "အာရုံဖြင့် အားကြီးသော အမှီ",   # = the module's ārammaṇūpanissayo (terms)
    "Paṭhamassa": "ပထမ",
    "kusalasamāpattiṃ": "ကုသိုလ် သမာပတ်",
    "paṭhamajjhānapaccavekkhaṇaṃ": "ပထမ ဈာန်ကို ပြန်လည် ဆင်ခြင်ခြင်း",
    "maggapaccavekkhaṇaṃ": "မဂ်ကို ပြန်လည် ဆင်ခြင်ခြင်း",
    "appamāṇārammaṇaappamāṇacittasamaṅgissa": "အတိုင်းအဆ မရှိသည်ကို အာရုံပြုသော အတိုင်းအဆ မရှိသော စိတ်နှင့် ပြည့်စုံသူ",
    "ajjhattārammaṇabahiddhācittasamaṅgissa": "မိမိ၌ ရှိသည်ကို အာရုံပြုသော မိမိ၏ ပြင်ပ၌ ရှိသော စိတ်နှင့် ပြည့်စုံသူ",
    "paṭisandhicittaṃ": "ပဋိသန္ဓေ စိတ်",
    "aniccānupassanā": "မမြဲဟု အဖန်ဖန် ရှုခြင်း",     # pi-2 anupassanā «အဖန်ဖန် ရှုခြင်း»; inner quotative «ဟု» stays
    "paro": "သူတစ်ပါး",                            # pi-5 «တစ်ဦး» not in the segment
    "mātikāpadāni": "ခေါင်းစဉ်စာရင်း ပုဒ်",           # pi-1 … pi-5 mātikā + pi-2 padāni
    "pariyosānapadā": "အဆုံးသတ် ပုဒ်",
    "tividharūpasaṅgaho": "ရုပ် သုံးမျိုးကို စုစည်းခြင်း", "tividharūpasaṅgahena": "ရုပ် သုံးမျိုးကို စုစည်းခြင်း",
    "sādhukaṃ": "ကောင်းစွာ",
    "ante": "အဆုံးတိုင်း",                          # «ante ante» «အဆုံးတိုင်း၌»: the distributive «တိုင်း» (rule 1: «၌» goes)
    "Natthivigatapaccayaṃ": "မရှိခြင်းဟူသော အကြောင်း ပျောက်ကွယ်ခြင်းဟူသော အကြောင်း",   # T1 names, rule 6 (no «၊»)
    # --- neva-X / X-mūlaka terms (G2-2, G2-3)
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
