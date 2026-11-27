"""pi-5 Burmese rails: the bilingual-review fixes (review/report-A.md A1 … A22, review/report-B.md B1 … B20; decisions in
review/fix-brief.md, results and the KEEP items A19 / B16 in review/fix-notes.md). Model: pi-4-my/rails/apply_fixes.py
(read only).

The fixes that change a repeated formula, proposition or term constant are rails-layer patches (my_formulas_rails.py,
families L40 … L51: A2 + A3, B4, B6, B7, B8, B9, B12, B13, B15, A16, B1, B5). Two existing residual rules follow the
decisions: R501 (mātaraṃ jīvitā voropetvā «အမိကို အသက်မှ သတ်၍», B5 / termbase change 2026-11-22) and R203 withdrawn
(A17). The single-segment fixes are the explicit rules F01 … here.

usage: python3 -I -X utf8 apply_fixes.py
Run by regen_rails.sh right after apply_termbase.py (build_rails.py rewrites every chapter first, so a rebuild always
starts from the same input). Reads and rewrites AI_translation/burmese/pi-5-burmese-plain-rails_split_chapters.

Every rule, applied line by line (Pāli and Burmese lines are aligned inside each segment):
  - scope: a list of segment IDs;
  - trigger: a regex the aligned Pāli line must match, else the line is not touched;
  - change: a list of exact Burmese old → new pairs;
  - hit: if True, each line must get exactly as many replacements as the Pāli trigger has hits;
  - expected replacement count over the whole book: the run fails (and writes nothing) if the count differs;
  - every changed line keeps its «[» / «…» / «–» / «“» / «”» counts, except the quote rules (Q: only quote marks
    may change) — check_marks.py then checks every line against the Pāli.
Book-wide checks (book_checks): every instance of each pattern is counted by script over all chapters (Pāli and
Burmese; layer families included), and old forms must be gone.
Every replacement is logged in rails/fixes-log.tsv (ch, id, line, old, new, rule); line = line number in the chapter file.
Deterministic: no randomness, files and rules in fixed order.
"""
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PALI = ROOT / "AI_translation/pali/pi-5_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-5-burmese-plain-rails_split_chapters"
LOG = HERE / "fixes-log.tsv"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
N = lambda s: unicodedata.normalize("NFC", s)  # noqa: E731

_V16 = ("[ပါဌ်ကွဲ (Syā.): mātughātakakammassa၊ (Ka.): mātughātikammassa၊ pitughāta-, arahantaghātakammassa ဟူသော "
        "ပုဒ်တို့၌လည်း ထို့အတူ]")
_J90 = "[စာလုံးပေါင်းကွဲ (Sī.): jānatāhaṃ၊ (Syā., Pī., Ka.): jānatvāhaṃ]"
_R138 = "[“ဒီဃနိကာယ်” 2.27၊ “မဇ္ဈိမနိကာယ်” 3.205၊ ဟောတော်မူချက်ကို ဘေးသို့ ကြည့်၍ မေးသည်]"
_R138N = "[“ဒီဃနိကာယ်” 2.27၊ “မဇ္ဈိမနိကာယ်” 3.205၊ ဟောတော်မူချက်ကို မြင်၍ မေးသည်]"
_AN72 = "[“အင်္ဂုတ္တရနိကာယ်” 10.72]"
_V190 = "[ပါဌ်ကွဲ (Sī., Syā., Ka.): gamissāmi၊ (Pī.): samīhāmi]"
_V191 = "[စာလုံးပေါင်းကွဲ (Ka.): kiñci]"

# (rule, segment ids, Pāli trigger regex, [(old, new)], expected, hit, quotes may change)
RULES = [
    # ---------------------------------------------------------------- meaning (B1 and B5 are layer L50 / L51 + R501)
    ("F01 B2 ^5-491 Bhaṭo vā no bharissati = «ငါတို့ ကျွေးမွေးခဲ့သူသည် ငါတို့ကို ပြန်လည် ကျွေးမွေးလိမ့်မည်» (termbase Bhaṭo "
     "«ကျွေးမွေးခဲ့သူ», change 2026-11-22; no added «သား»): AN 5.39 prose and verse",
     ["5-491"], r"Bhaṭo vā no bharissati",
     [("ဝေယျာဝစ္စ ပြုသူသည် ငါတို့ကို ကျွေးမွေးလိမ့်မည်", "ငါတို့ ကျွေးမွေးခဲ့သူသည် ငါတို့ကို ပြန်လည် ကျွေးမွေးလိမ့်မည်")],
     2, True, False),
    ("F02 B3 ^5-867 Na vessabhū … Somo yamo vessavaṇo ca rājā: the negation reaches the second line «… မင်းလည်း မဟုတ်၊»",
     ["5-867"], r"Somo yamo vessavaṇo ca rājā",
     [("သောမ၊ ယမ၊ ဝေဿဝဏ် မင်းလည်း၊", "သောမ၊ ယမ၊ ဝေဿဝဏ် မင်းလည်း မဟုတ်၊")], 1, True, False),
    ("F03 A1 ^5-60 atthi na sabbo puggalo / natthi na sabbo puggalo = «not all is»: «… အားလုံးသည် ပုဂ္ဂိုလ် ဖြစ်သည်ကား "
     "မဟုတ်သလော»",
     ["5-60"], r"na sabbo puggalo",
     [("အားလုံးသည် ပုဂ္ဂိုလ် မဟုတ်သလော", "အားလုံးသည် ပုဂ္ဂိုလ် ဖြစ်သည်ကား မဟုတ်သလော")], 2, True, False),
    ("F04 A4 ^5-273 appaṭividdhākuppo = «မပျက်ယွင်းတတ်သော အရာကို ထိုးဖောက်၍ မသိရသေးသော» (termbase paṭividdha «ထိုးဖောက်၍ "
     "သိပြီးသော», L25 paṭivedha family; «ထိုးထွင်း» is vipassanā's word)",
     ["5-273"], r"(?i)appaṭividdhākuppo",
     [("အရာကို ထိုးထွင်း မသိမြင်ရသေး", "အရာကို ထိုးဖောက်၍ မသိရသေး")], 3, True, False),
    ("F05 A5 ^5-403 abhisambuddhāni = «ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူခဲ့…» (termbase abhisambuddhāni, change 2026-11-22; "
     "= ^5-270 abhisambuddho)",
     ["5-403"], r"abhisambuddhān[iī]",
     [("ထိုးထွင်း သိတော်မူခဲ့", "ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူခဲ့")], 3, True, False),
    ("F06 A5 ^5-450 abhisambujjhati «ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူ…», Abhisambujjhitvā «ကိုယ်တိုင် အပြည့်အဝ သိမြင်၍» "
     "(termbase, change 2026-11-22): SN 2.20",
     ["5-450"], r"abhisambujjhati|Abhisambujjhitvā",
     [("ထိုးထွင်း သိတော်မူ၏", "ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူ၏"), ("ထိုးထွင်း သိ၍", "ကိုယ်တိုင် အပြည့်အဝ သိမြင်၍")],
     2, True, False),
    ("F07 A6 ^5-405 Dhammacakkaṃ pavattetuṃ = «ဓမ္မစကြာကို လည်စေရန်» (termbase dhammacakkaṃ pavattitaṃ «ဓမ္မစကြာကို "
     "လည်စေ…»; dhamma- was omitted)",
     ["5-405"], r"Dhammacakkaṃ pavattetuṃ", [("“စကြာကို လည်စေရန်", "“ဓမ္မစကြာကို လည်စေရန်")], 1, True, False),
    ("F08 A7 ^5-325 Sn 1070 line 1 «Nāhaṃ sahissāmi [variant] pamocanāya,»: the Burmese of this line on this line, the "
     "variant after its word sahissāmi «မတတ်နိုင်»",
     ["5-325"], r"Nāhaṃ sahissāmi",
     [(f"“ဓောတက၊ ငါသည် {_V190} လောက၌ ယုံမှားသံသယ ရှိသူ", f"“ငါသည် လွတ်မြောက်စေရန် မတတ်နိုင် {_V190}၊")], 1, True, False),
    ("F09 A7 ^5-325 Sn 1070 line 2 «Kathaṅkathiṃ dhotaka kañci [variant] loke;»: «ဓောတက၊ လောက၌ ယုံမှားသံသယ ရှိသူ "
     "တစ်စုံတစ်ယောက်ကိုမျှ [variant]၊»",
     ["5-325"], r"Kathaṅkathiṃ dhotaka kañci",
     [(f"တစ်စုံတစ်ယောက်ကိုမျှ {_V191} လွတ်မြောက်စေရန် မတတ်နိုင်၊",
       f"ဓောတက၊ လောက၌ ယုံမှားသံသယ ရှိသူ တစ်စုံတစ်ယောက်ကိုမျှ {_V191}၊")], 1, True, False),
    # ---------------------------------------------------------------- consistency
    ("F10 B5 / B18 ^5-653 uddāna «sañcicca pāṇaṃ jīvitā voropeyya» = the verbal noun «… အသက်မှ သတ်ခြင်း» (was «… "
     "သတ်ရာခြင်း»)",
     ["5-653"], r"sañcicca pāṇaṃ jīvitā voropeyya, diṭṭhisampannassa",
     [("ရည်ရွယ်၍ သတ္တဝါကို အသက်မှ သတ်ရာခြင်း", "ရည်ရွယ်၍ သတ္တဝါကို အသက်မှ သတ်ခြင်း")], 1, True, False),
    ("F11 B9 ^5-917 yadaniccaṃ taṃ dukkhaṃ [saṃ. ni. 3.15] vuttaṃ: the reference bracket after «ဟု» (= ^5-787)",
     ["5-917"], r"yadaniccaṃ taṃ dukkhaṃ \[saṃ\. ni\. 3\.15\]",
     [("“မမြဲသော အရာသည် ဒုက္ခ”ဟု မြတ်စွာဘုရား ဟောတော်မူသည် မဟုတ်လော – “ရုပ်သည် မမြဲ” [“သံယုတ္တနိကာယ်” 3.15]။",
       "“မမြဲသော အရာသည် ဒုက္ခ”ဟု [“သံယုတ္တနိကာယ်” 3.15] မြတ်စွာဘုရား ဟောတော်မူသည် မဟုတ်လော – “ရုပ်သည် မမြဲ”။")],
     1, True, False),
    ("F43 B9 ^5-338 the same SN 3.15 quotation «yadaniccaṃ taṃ dukkhaṃ» = «“မမြဲသော အရာသည် ဒုက္ခ”ဟု» (one wording book-wide, "
     "identical Pāli; was «“အကြင်အရာသည် မမြဲ၊ ထိုအရာသည် ဒုက္ခ”ဟု»), its reference bracket after «ဟု» as ^5-787",
     ["5-338"], r"yadaniccaṃ taṃ dukkhaṃ",
     [("“အကြင်အရာသည် မမြဲ၊ ထိုအရာသည် ဒုက္ခ”ဟု မြတ်စွာဘုရား ဟောတော်မူ၍ “ပြုပြင်ဖန်တီးမှု အားလုံးတို့သည် မမြဲ”ဟုလည်း "
       "ဟောတော်မူသည် မဟုတ်လော [“သံယုတ္တနိကာယ်” 3.15] [",
       "“မမြဲသော အရာသည် ဒုက္ခ”ဟု [“သံယုတ္တနိကာယ်” 3.15] မြတ်စွာဘုရား ဟောတော်မူ၍ “ပြုပြင်ဖန်တီးမှု အားလုံးတို့သည် "
       "မမြဲ”ဟုလည်း ဟောတော်မူသည် မဟုတ်လော ["),
      ("“အကြင်အရာသည် မမြဲ၊ ထိုအရာသည် ဒုက္ခ”ဟု", "“မမြဲသော အရာသည် ဒုက္ခ”ဟု")], 2, True, False),
    ("F12 B10 ^5-782 AN 10.217 nāhaṃ … byantībhāvaṃ vadāmi … apare vā pariyāye = the wording of ^5-628 (20:29)",
     ["5-782"], r"byantībhāvaṃ vadāmi",
     [("“ရဟန်းတို့၊ စေ့ဆော်၍", "“ရဟန်းတို့၊ ငါသည် စေ့ဆော်၍"), ("ကုန်ဆုံးခြင်းကို ငါ မဟော၊", "ကုန်ဆုံးခြင်းကို မဟော၊"),
      ("နောက်ထပ် အလှည့်၌ဖြစ်စေ", "ထို့နောက် အခြား ဘဝ အလှည့်၌ဖြစ်စေ")], 3, False, False),
    ("F13 B11 ^5-546 adinnādānakammassa hetu = «မပေးသည်ကို ယူခြင်း ကံကြောင့်» (adinnādāna «မပေးသည်ကို ယူ…» book-wide)",
     ["5-546"], r"adinnādānakammassa hetu", [("မပေးသည်ကို ကိုင်ခြင်း ကံကြောင့်", "မပေးသည်ကို ယူခြင်း ကံကြောင့်")],
     1, True, False),
    ("F14 B13 ch15 / ch20 «X (kamma)vipāko, X (na) sukhavedaniyo …» = ch24 ^5-766 «Xသည် ကံ၏ အကျိုး ဖြစ်၍ Xသည် …» (one "
     "frame book-wide)",
     ["5-492", "5-495", "5-636", "5-638", "5-639"], r"\b\w+ (?:kamma)?vipāko, \w+ (?:na )?(?:sukha|dukkha)",
     [("ကံ၏ အကျိုး ဖြစ်သည်၊ ", "ကံ၏ အကျိုး ဖြစ်၍ ")], 20, True, False),
    ("F15 A15 ^5-338 khaṇo vo paṭiladdho = «ခဏကို ရရှိပြီ» both times (termbase paṭiladdho «ရရှိပြီးသော»); A22 the variant "
     "[paṭividdho] after its word paṭiladdho «ရရှိပြီ»",
     ["5-338"], r"khaṇo vo paṭiladdho",
     [("ခဏ [ပါဌ်ကွဲ (အများစု၌): paṭividdho]ကို ရရှိပြီ", "ခဏကို ရရှိပြီ [ပါဌ်ကွဲ (အများစု၌): paṭividdho]"),
      ("ခဏကို ရပြီ", "ခဏကို ရရှိပြီ")], 2, True, False),
    ("F17 A18 ^5-378 appaṭiladdho anadhigato asacchikato = «မရသေးသော၊ မပိုင်ဆိုင်ရသေးသော၊ မျက်မှောက် မပြုရသေးသော» "
     "(adhigato «ပိုင်ဆိုင်», termbase adhigato sacchikato)",
     ["5-378"], r"appaṭiladdho anadhigato asacchikato",
     [("မရသေးသော၊ မရောက်သေးသော၊ မျက်မှောက် မပြုရသေးသော", "မရသေးသော၊ မပိုင်ဆိုင်ရသေးသော၊ မျက်မှောက် မပြုရသေးသော")],
     2, True, False),
    ("F18 B14 ^5-653 Na vattabbaṃ \"…\"ti? = «…”ဟု ဤသို့ မဆိုသင့်သလော» (as ^5-505)",
     ["5-653"], r'^Na vattabbaṃ "sattamabhavikassa',
     [("ပယ်ပြီးသည်”ဟု မဆိုသင့်သလော", "ပယ်ပြီးသည်”ဟု ဤသို့ မဆိုသင့်သလော")], 1, True, False),
    ("F19 B19 ^5-906 na āpāthaṃ āgacchanti = «နယ်ပယ်သို့ မရောက်လာကြ» (one form ×3; the Pāli has no cakkhussa / kāyassa)",
     ["5-906"], r"na āpāthaṃ āgacchanti",
     [("အဆင်းအရောင်တို့သည်လည်း မျက်စိ၏ နယ်ပယ်သို့", "အဆင်းအရောင်တို့သည်လည်း နယ်ပယ်သို့"),
      ("အထိအတွေ့တို့သည်လည်း ကိုယ်၏ နယ်ပယ်သို့", "အထိအတွေ့တို့သည်လည်း နယ်ပယ်သို့")], 2, True, False),
    # ---------------------------------------------------------------- minor
    ("F20 A8 ^5-94 no ce bhijjati = «… မပျက် ဆိုလျှင်» (one verb, = so ce bhijjati «ပျက်»)",
     ["5-94"], r"no ce bhijjati", [("ပုဂ္ဂိုလ်သည် မပြိုကွဲ ဆိုလျှင်", "ပုဂ္ဂိုလ်သည် မပျက် ဆိုလျှင်")], 1, True, False),
    ("F21 A9 ^5-401 [… vuttaṃ dissāya pucchati] = «… ဟောတော်မူချက်ကို မြင်၍ မေးသည်», in place after «pacchā manussā»",
     ["5-401"], r"vuttaṃ dissāya pucchati",
     [("နောက်မှ လူတို့က ခံယူကြသကဲ့သို့ ထို့အတူပင်", f"နောက်မှ လူတို့က ခံယူကြသကဲ့သို့ {_R138N} ထို့အတူပင်"),
      (f"ခံယူကြသလော {_R138}။", "ခံယူကြသလော။")], 2, False, False),
    ("F22 A10 ^5-401 sabbā ca disā viloketi = «အရပ် အားလုံးကိုလည်း ကြည့်ရှု၏» (surveys every quarter)",
     ["5-401"], r"sabbā ca disā viloketi",
     [("အရပ် အားလုံးကိုလည်း ဘေးသို့ ကြည့်၏", "အရပ် အားလုံးကိုလည်း ကြည့်ရှု၏")], 2, True, False),
    ("F23 A11 ^5-269 abhabbā niyāmaṃ okkamituṃ = «… သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းရန် မထိုက်တန်ကြ» (= ^5-269 bhabbā "
     "«… သက်ဆင်းနိုင်ကြ»)",
     ["5-269"], r"abhabbā niyāmaṃ okkamituṃ",
     [("သေချာသော လမ်းကြောင်းသို့ မထိုက်တန်ကြ", "သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းရန် မထိုက်တန်ကြ")], 1, True, False),
    ("F24 A12 ^5-269 na buddhe pasannā = «ဘုရားရှင်၌ မကြည်ညိုကြ» (L19 buddha «ဘုရားရှင်», = ^5-269 buddhe pasannā)",
     ["5-269"], r"na buddhe pasannā",
     [("နတ်အားလုံးတို့သည် ဘုရား၌ မကြည်ညိုကြ", "နတ်အားလုံးတို့သည် ဘုရားရှင်၌ မကြည်ညိုကြ")], 1, True, False),
    ("F25 A13 ^5-268 «…ti, …ti, …ti?» coordinate questions = «… ရောက်သည်၊ … ရောက်သည်၊ … ရောက်သလော» (no «ဟူ၍»)",
     ["5-268"], r"upacayaṃ gacchatīti,",
     [("တိုးပွားခြင်းသို့ ရောက်သည်ဟူ၍၊", "တိုးပွားခြင်းသို့ ရောက်သည်၊")], 5, True, False),
    ("F26 A14 ^5-342 … na akaniṭṭhagāmīti? = «… မရောက်သူ ဖြစ်သလော»",
     ["5-342"], r"na akaniṭṭhagāmīti\?",
     [("အကနိဋ္ဌ ဘုံသို့ မရောက်သူသလော", "အကနိဋ္ဌ ဘုံသို့ မရောက်သူ ဖြစ်သလော")], 1, True, False),
    ("F27 A20 ^5-296 akiriyavādā natthikavādā = «ပြုခြင်း၏ အကျိုး မရှိဟု …၊ ကံ၏ အကျိုး မရှိဟု …» (the decision A20)",
     ["5-296"], r"akiriyavādā natthikavādā",
     [("ကံ၏ အကျိုး မရှိဟု ဆိုသော ဝါဒ ရှိသူ၊ ဘာမျှ မရှိဟု ဆိုသော ဝါဒ ရှိသူ",
       "ပြုခြင်း၏ အကျိုး မရှိဟု ဆိုသော ဝါဒ ရှိသူ၊ ကံ၏ အကျိုး မရှိဟု ဆိုသော ဝါဒ ရှိသူ")], 1, True, False),
    ("F28 B17 ^5-546 mātughātakammassa [variant] hetu: the variant right after «အမိကို သတ်ခြင်း ကံကြောင့်»",
     ["5-546"], r"mātughātakammassa \[mātughātakakammassa",
     [("အမိကို သတ်ခြင်း ကံကြောင့် ဖြစ်သလော…", f"အမိကို သတ်ခြင်း ကံကြောင့် {_V16} ဖြစ်သလော…"),
      (f"သံဃာကို သင်းခွဲခြင်း ကံကြောင့် ဖြစ်သလော {_V16}။", "သံဃာကို သင်းခွဲခြင်း ကံကြောင့် ဖြစ်သလော။")], 2, False, False),
    ("F29 A22 ^5-317 jānatohaṃ [variant]: the variant right after «ငါသည် သိသူ»",
     ["5-317"], r"jānatohaṃ \[jānatāhaṃ",
     [("“ရဟန်းတို့၊ ငါသည် သိသူ၊ မြင်သူ၏", f"“ရဟန်းတို့၊ ငါသည် သိသူ {_J90}၊ မြင်သူ၏"),
      (f"ဖြစ်၏” {_J90} [“သံယုတ္တနိကာယ်” 3.101", "ဖြစ်၏” [“သံယုတ္တနိကာယ်” 3.101")], 2, False, False),
    ("F30 A22 ^5-333 the two [a. ni. 10.72] references each after its «… kaṇṭako vutto bhagavatā» (were both at the end)",
     ["5-333"], r"kaṇṭako vutto bhagavatā \[a\. ni\. 10\.72\]",
     [("ဝင်လေ ထွက်လေသည် ဆူးငြောင့်ဟု မြတ်စွာဘုရား ဟောတော်မူ…",
       f"ဝင်လေ ထွက်လေသည် ဆူးငြောင့်ဟု မြတ်စွာဘုရား ဟောတော်မူ {_AN72}…"),
      (f"ဆူးငြောင့်ဟု မြတ်စွာဘုရား ဟောတော်မူသည်၊ ထိုသူ၌ မှတ်သိမှုနှင့် ခံစားမှု ရှိသလော {_AN72} {_AN72}။",
       f"ဆူးငြောင့်ဟု မြတ်စွာဘုရား ဟောတော်မူသည် {_AN72}၊ ထိုသူ၌ မှတ်သိမှုနှင့် ခံစားမှု ရှိသလော။")], 2, True, False),
    ("F31 A22 ^5-386 na vattabbaṃ [variant]: the variant after the whole word «မဆိုသင့်သလော» (it split the word)",
     ["5-386"], r"na vattabbaṃ \[nevasaññānāsaññāyatane vattabbaṃ",
     [("ဤသို့ မဆိုသင့် [ပါဌ်ကွဲ (မသေချာ): nevasaññānāsaññāyatane vattabbaṃ]သလော",
       "ဤသို့ မဆိုသင့်သလော [ပါဌ်ကွဲ (မသေချာ): nevasaññānāsaññāyatane vattabbaṃ]")], 1, True, False),
    ("F32 A22 ^5-405 āhañchaṃ [āhaññiṃ]: the variant right after its word «တီးမည်»",
     ["5-405"], r"āhañchaṃ \[āhaññiṃ",
     [("အမြိုက် စည်ကို [ပါဌ်ကွဲ (Ka.): āhaññiṃ] တီးမည်”", "အမြိုက် စည်ကို တီးမည် [ပါဌ်ကွဲ (Ka.): āhaññiṃ]”")], 1, True, False),
    ("F33 A22 ^5-335 yamidaṃ [yadidaṃ]: the variant after the whole word «ဤအရာသည်» (it split the word)",
     ["5-335"], r"yamidaṃ \[yadidaṃ",
     [("ဤအရာ [ပါဌ်ကွဲ (အများစု၌): yadidaṃ]သည်", "ဤအရာသည် [ပါဌ်ကွဲ (အများစု၌): yadidaṃ]")], 1, True, False),
    ("F34 A22 ^5-424 samāpattiṃ [variant]: the variant after the whole word «သမာပတ်ကို»",
     ["5-424"], r"samāpattiṃ \[pathavīkasiṇasamāpattiṃ",
     [("သမာပတ် [စာလုံးပေါင်းကွဲ (Sī., Ka.): pathavīkasiṇasamāpattiṃ]ကို",
       "သမာပတ်ကို [စာလုံးပေါင်းကွဲ (Sī., Ka.): pathavīkasiṇasamāpattiṃ]")], 1, True, False),
    ("F35 A22 ^5-441 Paṭuppanne [variant]: the variant after the whole word «ပစ္စုပ္ပန်ကို»",
     ["5-441"], r"Paṭuppanne \[paccuppanne",
     [("ပစ္စုပ္ပန် [စာလုံးပေါင်းကွဲ (Sī., Syā.): paccuppanne]ကို", "ပစ္စုပ္ပန်ကို [စာလုံးပေါင်းကွဲ (Sī., Syā.): paccuppanne]")],
     1, True, False),
    ("F36 A22 ^5-251 thinaṃ [variant]: the variant after the whole word «ထိုင်းမှိုင်းမှုကို»",
     ["5-251"], r"thinaṃ \[thīnaṃ",
     [("ထိုင်းမှိုင်းမှု [စာလုံးပေါင်းကွဲ (Sī., Syā., Kaṃ., Pī.): thīnaṃ]ကို",
       "ထိုင်းမှိုင်းမှုကို [စာလုံးပေါင်းကွဲ (Sī., Syā., Kaṃ., Pī.): thīnaṃ]")], 1, True, False),
    ("F44 A22 ^5-333 kaṇḍako [kaṇṭako (syā.) a. ni. 10.72]: the variant right after its word «ဆူးငြောင့်ဟု» (same segment "
     "as F30)",
     ["5-333"], r"saddo kaṇḍako \[kaṇṭako",
     [("ပထမ ဈာန်၏ အသံသည် ဆူးငြောင့်ဟု မြတ်စွာဘုရား ဟောတော်မူသည် မဟုတ်လော [ပါဌ်ကွဲ (Syā.): kaṇṭako၊ “အင်္ဂုတ္တရနိကာယ်” 10.72] [",
       "ပထမ ဈာန်၏ အသံသည် ဆူးငြောင့်ဟု [ပါဌ်ကွဲ (Syā.): kaṇṭako၊ “အင်္ဂုတ္တရနိကာယ်” 10.72] မြတ်စွာဘုရား ဟောတော်မူသည် မဟုတ်လော [")],
     1, True, False),
    # ---------------------------------------------------------------- coordinator follow-up 2026-11-22 (open points 1-2)
    ("F45 B5 follow-up ^5-859 the passive «pitā / arahā jīvitā voropito» = «အဖသည် / ရဟန္တာသည် အသက်မှ ချခံရပြီး…» as "
     "28:10 «အမိသည် အသက်မှ ချခံရပြီး…» (R618; termbase jīvitā voropitā «အသက်မှ ချခံရသော»; the passive keeps «ချခံရ»)",
     ["5-859"], r"(?:pitā|arahā) jīvitā voropito",
     [("အဖကို သတ်ခဲ့ပြီး", "အဖသည် အသက်မှ ချခံရပြီး"), ("ရဟန္တာကို သတ်ခဲ့ပြီး", "ရဟန္တာသည် အသက်မှ ချခံရပြီး")],
     4, True, False),
    ("F46 R623 follow-up ^5-906 ajjhattiko (ceva) kāyo = «အတွင်းပိုင်း ကိုယ်» (termbase ajjhattika / ajjhattikaṃ «အတွင်းပိုင်း»; "
     "one wording inside the quotation, = «အတွင်းပိုင်း မျက်စိ» 30:80)",
     ["5-906"], r"ajjhattiko ceva",
     [("မိမိ၏ ကိုယ်သည်", "အတွင်းပိုင်း ကိုယ်သည်")], 3, True, False),
    # ---------------------------------------------------------------- quote rule (A21 + B20)
    ("F37 A21 ^5-192 Kalyāṇavaggo paṭhamo: no quote mark where the Pāli has none (vagga colophon)",
     ["5-192"], r"Kalyāṇavaggo paṭhamo", [("ပထမ “ကောင်းမွန်သော” ဝဂ်", "ပထမ ကောင်းမွန်သော ဝဂ်")], 1, True, True),
    ("F38 A21 ^5-238 the uddāna «… pañcamaṃ kalyāṇaṃ …»: the vagga name without quote marks",
     ["5-238"], r"pañcamaṃ kalyāṇaṃ", [("ဖြစ်သော “ကောင်းမွန်သော” ဝဂ်", "ဖြစ်သော ကောင်းမွန်သော ဝဂ်")], 1, True, True),
    ("F39 A21 ^5-306 Mahāvaggo: the vagga colophon without quote marks",
     ["5-306"], r"^Mahāvaggo", [("“ကြီးမြတ်သော” ဝဂ်", "ကြီးမြတ်သော ဝဂ်")], 1, True, True),
    ("F40 A21 ^5-333 10:258 the stray «’» (the Pāli closes no quote on this line)",
     ["5-333"], r"naḷāgāraṃva kuñjaro\.$", [("ဖြိုဖျက်ကြလော့’။", "ဖြိုဖျက်ကြလော့။")], 1, True, True),
    ("F41 B20 ^5-19-4-1-0 the kathā heading «Idaṃ dukkhantikathā» without quote marks",
     ["5-19-4-1-0"], r"Idaṃ dukkhantikathā",
     [("“ဤကား ဒုက္ခ”ဟူသော ဆွေးနွေးချက်", "ဤကား ဒုက္ခဟူသော ဆွေးနွေးချက်")], 1, True, True),
    ("F42 B20 ^5-620 «Idaṃ dukkhantikathā niṭṭhitā»: the section-end form «“X” ပြီးဆုံးပြီ» keeps its quotes, X = the "
     "heading without inner quotes",
     ["5-620"], r"Idaṃ dukkhantikathā niṭṭhitā",
     [("“‘ဤကား ဒုက္ခ’ဟူသော ဆွေးနွေးချက်”", "“ဤကား ဒုက္ခဟူသော ဆွေးနွေးချက်”")], 1, True, True),
]


def segs(lines):
    """[(id, [line indexes])] in file order."""
    out, buf = [], []
    for k, l in enumerate(lines):
        if not l.strip():
            continue
        buf.append(k)
        m = ID.search(l)
        if m:
            out.append((m.group(1), buf))
            buf = []
    return out


def marks(s, quotes=True):
    return tuple(s.count(c) for c in ("[…–“”‘’" if quotes else "[…–"))


def book_checks(files, pali, text):
    """every instance by script; returns (errors, info lines)."""
    err, info = [], []
    pairs = [(f, k, N(re.sub(r"\[[^\]]*\]", "", p)), N(text[f][k])) for f in files
             for k, p in enumerate(pali[f]) if p.strip()]
    praw = [(f, k, N(p), N(text[f][k])) for f in files for k, p in enumerate(pali[f]) if p.strip()]

    def count(rx_p, rx_m, label, ge=False, pali_br=False):
        src = praw if pali_br else pairs
        np_ = sum(len(re.findall(rx_p, p)) for f, k, p, m in src)
        nm = sum(len(re.findall(rx_m, m)) for f, k, p, m in src if re.search(rx_p, p))
        short = [f"{f[:-3]}:{k + 1}" for f, k, p, m in src if len(re.findall(rx_m, m)) < len(re.findall(rx_p, p))]
        info.append(f"{label}: Pāli {np_}, Burmese {nm}")
        if (np_ != nm and not ge) or short:
            err.append(f"{label}: Pāli {np_} ≠ Burmese {nm} {short[:6]}")

    def gone(rx_m, label):
        left = [f"{f[:-3]}:{k + 1}" for f, k, p, m in pairs if re.search(rx_m, m)]
        if left:
            err.append(f"{label}: old form left on {left[:8]}")

    # L40 A2 + A3 identity formula
    count(r"appiyaṃ karitvā", r"ဟူသော စကားကို မခွဲခြားဘဲ", "L40 A2 appiyaṃ karitvā «မခွဲခြားဘဲ»")
    count(r"\besese ekaṭṭhe", r"ဤစကားတို့သည် တစ်ခုတည်း ဖြစ်သော၊ အနက် တူသော၊", "L40 A3 esese ekaṭṭhe «တစ်ခုတည်း ဖြစ်သော၊ အနက် တူသော»")
    gone(r"ဦးစားမပေး|သည် အနက် တူသော", "L40 A2 / A3")
    # F03 A1
    count(r"na sabbo puggalo", r"ပုဂ္ဂိုလ် ဖြစ်သည်ကား မဟုတ်", "F03 A1 na sabbo puggalo")
    # F04 A4, F05 / F06 A5
    count(r"(?i)appaṭividdhākuppo", r"ထိုးဖောက်၍ မသိရသေး", "F04 A4 appaṭividdhākuppo")
    count(r"abhisambuddhān[iī]|abhisambujjhati|Abhisambujjhitvā", r"ကိုယ်တိုင် အပြည့်အဝ သိမြင်", "F05/F06 A5 abhisambuddhāni family")
    gone(r"ထိုးထွင်း (?:မ)?သိမြင်|ထိုးထွင်း (?:မ)?သိတော်မူ|ထိုးထွင်း သိ၍", "A4 / A5 «ထိုးထွင်း …»")
    # F07 A6
    count(r"(?i)dhammacakkaṃ pavatt", r"ဓမ္မစကြာကို လည်စေ", "F07 A6 dhammacakkaṃ pavatt-")
    # F08 / F09 A7: each Sn 1070 line holds its own words
    count(r"Nāhaṃ sahissāmi", r"^“ငါသည် လွတ်မြောက်စေရန် မတတ်နိုင် \[", "F08 A7 line 1")
    count(r"Kathaṅkathiṃ dhotaka", r"^ဓောတက၊ လောက၌ ယုံမှားသံသယ ရှိသူ", "F09 A7 line 2")
    # L50 B1: na ca arahā … every verb negative
    for f, k, p, m in pairs:
        if re.search(r"na ca arahā āpāyike sadde.*methunaṃ dhammaṃ paṭiseveyya", p):
            seg = m[m.find("ရဟန္တာသည်ကား အပါယ်နှင့် ဆိုင်သော အသံ"):]
            seg = seg[:seg.find("ဟုတ်ပါသည်")]
            if re.search(r"(?<!မ)(?:မှီဝဲရာ|ခံယူရာ)", seg):
                err.append(f"L50 B1 {f[:-3]}:{k + 1}: a positive verb left in the «na ca arahā …» list")
            info.append("L50 B1 na ca arahā … paṭiggaṇheyya: " + str(len(re.findall(r"မ(?:မှီဝဲ|ခံယူ)ရာ", seg))) + " negative verbs")
    # F01 B2 Bhaṭo
    count(r"Bhaṭo vā no bharissati", r"ငါတို့ ကျွေးမွေးခဲ့သူသည် ငါတို့ကို ပြန်လည် ကျွေးမွေးလိမ့်မည်", "F01 B2 Bhaṭo")
    gone(r"ဝေယျာဝစ္စ ပြုသူ", "F01 B2")
    # F02 B3
    count(r"Somo yamo vessavaṇo ca rājā", r"ဝေဿဝဏ် မင်းလည်း မဟုတ်၊", "F02 B3 Somo yamo vessavaṇo")
    # L41 B4 paṇidahantassa / appaṇidahantassa
    count(r"(?<![a-z])paṇidahantassa", r"(?<!မ)ဆုတောင်းသူ", "L41 B4 paṇidahantassa «ဆုတောင်းသူ»")
    count(r"appaṇidahantassa", r"မဆုတောင်းသူ", "L41 B4 appaṇidahantassa «မဆုတောင်းသူ»")
    gone(r"ဆု မတောင်း|ထားရှိသူ|ဦး(?:မ)?တည်ထားသူ", "L41 B4")
    # L51 + R501 + F10 B5 active voropeti; passive keeps «ချခံရ»
    count(r"jīvitā vorope(?:t[iī]|tvā|yya)", r"အသက်မှ သတ်", "L51/R501/F10 B5 active jīvitā voropeti «အသက်မှ သတ်…» (…pe… lines may hold more)", ge=True)
    for f, k, p, m in pairs:
        if re.search(r"jīvitā vorope(?:t[iī]|tvā|yya)", p) and re.search(r"အသက်မှ ချ(?!ခံ)", m):
            err.append(f"B5 {f[:-3]}:{k + 1}: active voropeti still «အသက်မှ ချ»")
    count(r"jīvitā voropit[āo] hoti|mātā jīvitā voropitā", r"အသက်မှ ချခံရ", "B5 passive jīvitā voropitā keeps «ချခံရ»")
    count(r"(?:mātā|pitā|arahā) jīvitā voropit[āo]", r"(?:အမိ|အဖ|ရဟန္တာ)သည် အသက်မှ ချခံရ", "F45 B5 passive mātā / pitā / arahā jīvitā voropito (…pe… lines may hold more)", ge=True)
    gone(r"(?:အဖ|ရဟန္တာ)ကို သတ်ခဲ့ပြီး", "F45")
    count(r"ajjhattik", r"အတွင်းပိုင်း", "F46 ajjhattika «အတွင်းပိုင်း»", ge=True)
    for f, k, p, m in pairs:
        if re.search(r"ajjhattik", p) and "မိမိ၏" in m:
            err.append(f"F46 {f[:-3]}:{k + 1}: ajjhattika line keeps «မိမိ၏»")
    # L42 B6 ānantariko / ānantariyassa
    count(r"\bānantarik[oā]", r"ချက်ချင်း အကျိုးပေးသော ကံ ရှိသူ", "L42 B6 ānantariko")
    count(r"\bānantariyassa", r"ချက်ချင်း အကျိုးပေးသော ကံကို ပြုသော", "L42 B6 ānantariyassa (…pe… lines may hold more)", ge=True)
    gone(r"အနန္တရိယ", "L42 B6")
    # L43 B7
    count(r"(?i)ariyo aṭṭhaṅgiko maggo", r"အင်္ဂါ ရှစ်ပါး ရှိသော အရိယာ မဂ်|အရိယာ မဂ်သည် အင်္ဂါ ရှစ်ပါး ရှိ", "L43 B7 ariyo aṭṭhaṅgiko maggo")
    gone(r"မဂ်၊ အရိယာ မဂ်", "L43 B7")
    # L44 B8
    count(r"(?i)pettivisay", r"ပြိတ္တာ ဘုံ", "L44 B8 pettivisaya «ပြိတ္တာ ဘုံ»")
    gone(r"ပြိတ္တာ နယ်", "L44 B8")
    # L45 + F11 B9
    count(r"yadaniccaṃ taṃ dukkhaṃ", r"“မမြဲသော အရာသည် ဒုက္ခ”ဟု", "L45 B9 yadaniccaṃ taṃ dukkhaṃ")
    count(r"(?i)dukkhaññeva parinipphann", r"ဒုက္ခသည်သာ ပြည့်စုံစွာ", "L45 B9 dukkhaññeva parinipphanna")
    gone(r"ဆင်းရဲ ဒုက္ခ|အရာသည် ဆင်းရဲ၏|ဒုက္ခ” \[[^\]]*\]ဟု|ထိုအရာသည် ဒုက္ခ”", "L45 / F11 / F43 B9")
    count(r"yadaniccaṃ taṃ dukkhaṃ \[saṃ\. ni\. 3\.15\]", r"ဒုက္ခ”ဟု \[“သံယုတ္တနိကာယ်” 3\.15\]", "F11 / F43 B9 the SN 3.15 bracket after «ဟု»", pali_br=True)
    # F12 B10: the AN 10.217 quotation, one wording
    q20 = [m for f, k, p, m in pairs if "byantibhāvaṃ vadāmi" in p or "byantībhāvaṃ vadāmi" in p]
    core = [re.sub(r" \[[^\]]*\]", "", x[x.find("“ရဟန်းတို့၊ ငါသည် စေ့ဆော်၍"):x.find("ခံစားရ၏”")]) for x in q20]
    info.append(f"F12 B10 AN 10.217 quotations: {len(q20)}, wordings: {len(set(core))}")
    if len(q20) != 2 or len(set(core)) != 1 or not core[0]:
        err.append("F12 B10: the AN 10.217 quotations differ")
    # F13 B11
    count(r"adinnādān", r"မပေးသည်ကို ယူ", "F13 B11 adinnādāna «မပေးသည်ကို ယူ…»")
    gone(r"မပေးသည်ကို ကိုင်", "F13 B11")
    # L46 B12
    count(r"samphaṃ palap|samphappalāp", r"အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား", "L46 B12 samphaṃ palapati / samphappalāpa")
    gone(r"အကျိုးမဲ့ စကား", "L46 B12")
    # L47 + F14 B13
    count(r"na sukhavedaniy\w* na dukkhavedaniy\w* ?…pe…", r"သာယာသော ခံစားမှုကို ဖြစ်စေတတ်သော အရာ မဟုတ်၊ နာကျင်သော ခံစားမှုကို ဖြစ်စေတတ်သော အရာ မဟုတ်…",
          "L47 B13 na sukhavedaniyaṃ na dukkhavedaniyaṃ…pe…")
    count(r"\b\w+ (?:kamma)?vipāko, \w+ (?:na )?(?:sukha|dukkha)", r"ကံ၏ အကျိုး ဖြစ်၍ ", "F14 B13 X vipāko, X …")
    gone(r"ကံ၏ အကျိုး ဖြစ်သည်၊ \S+သည် (?:သာယာ|နာကျင်)", "F14 B13")
    count(r"\b(?:a)?kusal[oaā]ṃ? (?:sārammaṇ|anārammaṇ)", r"ကုသိုလ် ဖြစ်၍ အာရုံ", "L47 B13 X kusalo sārammaṇo")
    gone(r"ကုသိုလ် ဖြစ်သော၊ အာရုံ", "L47 B13")
    # F18 B14
    count(r'^Na vattabbaṃ "', r"”ဟု ဤသို့ မဆိုသင့်သလော", "F18 B14 Na vattabbaṃ \"…\"ti?")
    gone(r"”ဟု မဆိုသင့်သလော", "F18 B14")
    # L48 B15
    count(r"saḷāyataniko attabhāvo", r"ခြောက်ပါး ရှိသော ကိုယ်ခန္ဓာ(?! ရရှိခြင်း)", "L48 B15 saḷāyataniko attabhāvo")
    count(r"attabhāva?p?paṭilābh", r"ကိုယ်ခန္ဓာ ရရှိခြင်း", "L48 B15 attabhāvapaṭilābho keeps «ရရှိခြင်း»")
    # F19 B19
    count(r"(?<!cakkhussa )āpāthaṃ āgacchanti", r"နယ်ပယ်သို့ (?:မ)?ရောက်လာကြ", "F19 B19 āpāthaṃ āgacchanti")
    gone(r"(?:မျက်စိ|ကိုယ်)၏ နယ်ပယ်သို့", "F19 B19")
    # L49 A16 Handa hi
    count(r"\bHanda hi\b", r"ကဲ၊ ", "L49 A16 Handa hi «ကဲ၊»")
    # A17 (R203 withdrawn): anañño avigato = the sample's «အခြား မဖြစ်ဘဲ»
    count(r"(?i)\banañño\b", r"အခြား မဖြစ်ဘဲ", "A17 anañño «အခြား မဖြစ်ဘဲ»")
    gone(r"တခြားစီ မဖြစ်ဘဲ", "A17")
    # F15 A15
    count(r"khaṇo vo paṭiladdho", r"ခဏကို ရရှိပြီ", "F15 A15 khaṇo vo paṭiladdho")
    # F17 A18
    count(r"appaṭiladdho anadhigato asacchikato", r"မရသေးသော၊ မပိုင်ဆိုင်ရသေးသော၊ မျက်မှောက် မပြုရသေးသော", "F17 A18")
    # A21 + B20: no quote mark in a vagga colophon / heading line whose Pāli has none (section-end «“X” ပြီးဆုံးပြီ» kept)
    nq = 0
    for f in files:
        for k, p in enumerate(pali[f]):
            m = text[f][k]
            bare = re.sub(r"\[[^\]]*\]", "", m)
            if re.search(r"vaggo\b|^#+ ", p) and not re.search(r"[\"“”‘’']", re.sub(r"\[[^\]]*\]", "", p)):
                nq += 1
                if re.search(r"[“”‘’]", bare):
                    err.append(f"A21/B20 {f[:-3]}:{k + 1}: quote mark in a heading / vagga line")
            if re.search(r"kathā(?: \[[^\]]*\])? niṭṭhitā", p) and re.search(r"[‘’]", bare):
                err.append(f"A21/B20 {f[:-3]}:{k + 1}: inner quote in a section-end line")
    info.append(f"A21/B20 heading / vagga lines without Pāli quotes: {nq}, with Burmese quotes: 0")
    # A22: no bracket glued to a following Burmese word, no duplicated bracket
    gl = [f"{f[:-3]}:{k + 1}" for f, k, p, m in pairs if re.search(r"\][က-၉ၐ-႟]", m) or re.search(r"(\[[^\]]*\]) \1", m)]
    info.append(f"A22 glued / duplicated brackets left: {len(gl)}")
    if gl:
        err.append(f"A22: glued / duplicated brackets on {gl}")
    return err, info


def main():
    files = sorted(p.name for p in PALI.glob("*.md"))
    pali = {f: N((PALI / f).read_text(encoding="utf-8-sig")).split("\n") for f in files}
    text = {f: N((OUT / f).read_text(encoding="utf-8")).split("\n") for f in files}
    pseg = {f: segs(pali[f]) for f in files}
    mseg = {f: dict(segs(text[f])) for f in files}
    log, errors, counts = [], [], {}
    for rule, ids, trig, pairs, expect, hit, qok in RULES:
        trig_re = re.compile(trig)
        done, found = 0, set()
        for f in files:
            for i, pidx in pseg[f]:
                if i not in ids:
                    continue
                found.add(i)
                midx = mseg[f].get(i)
                if midx is None or len(midx) != len(pidx):
                    errors.append(f"{rule[:3]}: {f} {i}: segment missing or not line-aligned")
                    continue
                for pk, mk in zip(pidx, midx):
                    np_ = len(trig_re.findall(pali[f][pk]))
                    if not np_:
                        continue
                    before, got = text[f][mk], 0
                    for old, new in pairs:
                        n = text[f][mk].count(old)
                        if n:
                            text[f][mk] = text[f][mk].replace(old, new)
                            got += n
                            log += [(f[:-3], i, str(mk + 1), old, new, rule.split(" ")[0])] * n
                    if hit and got != np_:
                        errors.append(f"{rule[:3]}: {f[:-3]} {i} line {mk + 1}: {got} replacements, Pāli {np_}")
                    if marks(before, not qok) != marks(text[f][mk], not qok):
                        errors.append(f"{rule[:3]}: {f[:-3]} {i} line {mk + 1}: «[ … – “ ”» counts changed")
                    done += got
        if found != set(ids):
            errors.append(f"{rule[:3]}: segments not found: {sorted(set(ids) - found)}")
        counts[rule] = done
        if done != expect:
            errors.append(f"{rule[:3]}: {done} replacements, expected {expect}")
    berr, info = book_checks(files, pali, text)
    errors += berr
    for rule, n in counts.items():
        print(f"{n:6d}  {rule[:110]}")
    for x in info:
        print(f"        check: {x}")
    if errors:
        print("\n".join(errors))
        print(f"{len(errors)} errors")
        sys.exit(1)
    for f in files:
        (OUT / f).write_text("\n".join(text[f]), encoding="utf-8")
    with open(LOG, "w", encoding="utf-8") as fh:
        fh.write("ch\tid\tline\told\tnew\trule\n")
        for row in log:
            fh.write("\t".join(row) + "\n")
    print(f"{len(RULES)} rules; {len(log)} replacements; {len({(r[0], r[2]) for r in log})} lines changed")


main()
