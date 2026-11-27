"""Book-wide alignments of the pi-2 Burmese keyword mapping (map-harmonise pass; reasons in map-harmonise-notes.md).

Imported by the seven chapter scripts (map_2-4.py, map_5-7-11.py, map_6.py, map_12-14.py, map_15-16.py, map_17.py,
map_18.py) and applied in their lookup(): a value V that a script computes for keyword K is replaced by FIX[(K, V)]
(first letter case-insensitive, as the tables). An entry may be limited to some segments. Nothing runs on import.
The approved sample script map_all.py does not import this module: the sample values stay as approved.

Rules
P  Persons (decision 3, pi-1 practice). «…သူ» is the value only for Pāli NOUNS of persons: agent nouns (-tar
   bhāsitā, saritā «one who remembers»; -aka; the taṇhā epithets janikā, sibbinī …), present participles in the
   genitive / dative («for one who is doing»: abhikkamantassa, manasikarontassa, pharantassa …), person nouns
   (ekacco, amanussa, cora, titthiya, pabbajita, vidhavā, napuṃsaka, jhāyī «a meditator»), and the pi-1 values
   hīno / sadiso (māna formulas), gāhī, aññātāvī, the approved sekha / asekha term. Every ADJECTIVE or PARTICIPLE
   (-vant, -mant, -in, -āvin, -ka adjectives, past participles, bahubbīhi compounds), attributive, predicative or
   used for the person in an oblique case, is «…သော» even where the text writes the person noun «…သူ»
   (pi-1 rule 3: saṃviggassa «သံဝေဂ ရသူ၏» = သံဝေဂ ရသော; pi-1 sato, sampajāno, upekkhako; the approved sample
   samāpannassa «ဈာန် ဝင်စားသူ၏» = ဈာန် ဝင်စားသော). The presence check accepts «Xသော» against the text's «Xသူ».
A  Same keyword, same kind of segment, same value (decision 2): the single alignments below.
R  Relative pronouns as approved (decision 4): yaṃ = (no direct equivalent) where the Burmese builds the clause
   with «ရှိသော / ရှိသမျှ» (Yaṃ loke piyarūpaṃ …, yaṃ etasmiṃ antare …).
"""
NONE = "(no direct equivalent)"


def low(w):
    return w[:1].lower() + w[1:]


def f_pitisukham(kw, v, my):
    """A: pītisukhaṃ in the jhāna formula qualifies jhānaṃ (bahubbīhi): «ပီတိနှင့် သာယာမှု ရှိသော» where the text
    has that phrase (pi-1 rule 3; ch4, ch11); the noun of the jhāna-factor list (^2-580) keeps «ပီတိနှင့် သာယာမှု»."""
    return "ပီတိနှင့် သာယာမှု ရှိသော" if "ပီတိနှင့် သာယာမှု ရှိသော" in my else v


# (keyword, old value) -> new value | (new value, {segment IDs}) | function(kw, old, segment Burmese)
FIX = {
    # ---- P: adjectives / participles of persons = «…သော» (ch6, ch16, ch17, ch18)
    ("assaddho", "ယုံကြည်မှု မရှိသူ"): "ယုံကြည်မှု မရှိသော",
    ("ahiriko", "ဒုစရိုက်ကို မရှက်သူ"): "ဒုစရိုက်ကို မရှက်သော",
    ("anottappī", "ဒုစရိုက်ကို မကြောက်ရွံ့သူ"): "ဒုစရိုက်ကို မကြောက်ရွံ့သော",
    ("akhīṇāsavo", "စိတ်အစွန်းအထင်း မကုန်သေးသူ"): "စိတ်အစွန်းအထင်း မကုန်သေးသော",
    ("amanāpo", "မနှစ်သက်အပ်သူ"): "မနှစ်သက်အပ်သော",
    ("anattamano", "စိတ် မနှစ်သိမ့်သူ"): "စိတ် မနှစ်သိမ့်သော",
    ("antavā", "အဆုံး ရှိသူ"): "အဆုံး ရှိသော",
    ("anantavā", "အဆုံး မရှိသူ"): "အဆုံး မရှိသော",
    ("anariya", "အရိယာ မဟုတ်သူ"): "အရိယာ မဟုတ်သော",
    ("appassuto", "အကြားအမြင် နည်းသူ"): "အကြားအမြင် နည်းသော",
    ("bahussutoti", "အကြားအမြင် များသူ"): "အကြားအမြင် များသော",
    ("arūpī", "ရုပ် မရှိသူ"): "ရုပ် မရှိသော",
    ("asamāhito", "စိတ် မတည်ကြည်သူ"): "စိတ် မတည်ကြည်သော",
    ("samāhitoti", "စိတ် တည်ကြည်သူ"): "စိတ် တည်ကြည်သော",
    ("asantuṭṭhassa", "ရောင့်ရဲမှု မရှိသူ"): "ရောင့်ရဲမှု မရှိသော",
    ("asaññī", "မှတ်သိမှု မရှိသူ"): "မှတ်သိမှု မရှိသော",
    ("saññī", "မှတ်သိမှု ရှိသူ"): "မှတ်သိမှု ရှိသော",
    ("nevasaññīnāsaññī", "မှတ်သိမှု ရှိသည်လည်း မဟုတ် မရှိသည်လည်း မဟုတ်သူ"):
        "မှတ်သိမှု ရှိသည်လည်း မဟုတ် မရှိသည်လည်း မဟုတ်သော",
    ("nevasaññināsaññi", "မှတ်သိမှု ရှိသည်လည်း မဟုတ် မရှိသည်လည်း မဟုတ်သူ"):
        "မှတ်သိမှု ရှိသည်လည်း မဟုတ် မရှိသည်လည်း မဟုတ်သော",
    ("saññīnāsaññī", "မှတ်သိမှု ရှိသည်လည်း မဟုတ် မရှိသည်လည်း မဟုတ်သူ"):
        "မှတ်သိမှု ရှိသည်လည်း မဟုတ် မရှိသည်လည်း မဟုတ်သော",
    ("jaccandhānaṃ", "မွေးရာပါ မျက်စိ ကန်းသူ"): "မွေးရာပါ မျက်စိ ကန်းသော",
    ("badhirānaṃ", "နား ပင်းသူ"): "နား ပင်းသော",
    ("paripuṇṇāyatanānaṃ", "အာရုံခံ နယ်ပယ် ပြည့်စုံသူ"): "အာရုံခံ နယ်ပယ် ပြည့်စုံသော",
    ("bhuttāvissa", "စားပြီးသူ"): "စားပြီးသော",
    ("duppañño", "ပညာ နည်းသူ"): "ပညာ နည်းသော",
    ("paññavāti", "ပညာ ရှိသူ"): "ပညာ ရှိသော",
    ("dussīlo", "သီလ ပျက်သူ"): "သီလ ပျက်သော",
    ("sīlavāti", "သီလ ရှိသူ"): "သီလ ရှိသော",
    ("evaṃdiṭṭhi", "ဤသို့ အယူ ရှိသူ"): "ဤသို့ အယူ ရှိသော",
    ("evaṃdiṭṭhī", "ဤသို့ အယူ ရှိသူ"): "ဤသို့ အယူ ရှိသော",
    ("evaṃvādī", "ဤသို့ ဆိုလေ့ ရှိသူ"): "ဤသို့ ဆိုလေ့ ရှိသော",
    ("khilajāto", "ခက်ထန်သော စိတ် ဖြစ်ပေါ်သူ"): "ခက်ထန်သော စိတ် ဖြစ်ပေါ်သော",
    ("kupito", "အမျက်ထွက်သူ"): "အမျက်ထွက်သော",
    ("āhatacitto", "ထိခိုက်သော စိတ် ရှိသူ"): "ထိခိုက်သော စိတ် ရှိသော",
    ("kusīto", "ပျင်းရိသူ"): "ပျင်းရိသော",
    ("āraddhavīriyoti", "ဝီရိယ အားထုတ်ထားသူ"): "ဝီရိယ အားထုတ်ထားသော",
    ("muṭṭhassatī", "သတိ လစ်သူ"): "သတိ လစ်သော",
    ("upaṭṭhitassatīti", "သတိ တည်ထားသူ"): "သတိ တည်ထားသော",
    ("lābhiṃ", "ရသူ"): "ရသော",
    ("saṭho", "စဉ်းလဲသူ"): "စဉ်းလဲသော",
    ("parisaṭho", "အလွန် စဉ်းလဲသူ"): "အလွန် စဉ်းလဲသော",
    ("pavivittoti", "ကင်းဆိတ်စွာ နေသူ"): "ကင်းဆိတ်စွာ နေသော",
    ("ārāmo", "နှစ်သက်သူ"): "နှစ်သက်သော",
    ("sukhitesu", "ချမ်းသာသူ"): "ချမ်းသာသော",
    ("vuṭṭhitassa", "ထမြောက်သူ"): "ထမြောက်သော",
    ("phuṭṭhassa", "ထိခိုက်ခံရသူ"): "ထိခိုက်ခံရသော",                     # ch6 = ch4
    ("samannāgatassa", "ကြုံတွေ့နေရသူ"): "ကြုံတွေ့နေရသော",                # ch6 = ch4
    ("byasanena vā phuṭṭhassa", "ပျက်စီးခြင်းဖြင့် ထိခိုက်ခံရသူ၏ဖြစ်စေ"):    # ch6 = ch4 (vā has no word)
        "ပျက်စီးခြင်းဖြင့် ထိခိုက်ခံရသော",
    # ---- P: agent nouns (-tar) = «…သူ» (ch10 ^2-467 «saritā hoti anussaritā», as pi-1 bhāsitā)
    ("saritā", "အောက်မေ့သော"): "အောက်မေ့သူ",
    ("anussaritā", "အဖန်ဖန် အောက်မေ့သော"): "အဖန်ဖန် အောက်မေ့သူ",
    ("ajjhupekkhitā", "ဥပေက္ခာဖြင့် လွန်စွာ ရှုသော"): "ဥပေက္ခာဖြင့် လွန်စွာ ရှုသူ",
    # ---- A: single alignments
    ("dhammā kusalā", "သဘောတရား … ကုသိုလ်"): "ကုသိုလ် သဘောတရား",          # pi-1 (204 uses); ch12, ch13 = ch6 …
    ("anekaṃsa", "တစ်ထစ်ချ မယူနိုင်ခြင်း"): "တစ်ထစ်ချ",                    # gāho = ယူနိုင်ခြင်း in the same segment
    ("appaṭighā", "ထိခိုက်မှုလည်း မရှိသော"): "ထိခိုက်မှု မရှိသော",          # the pair's «လည်း» is not the fragment's
    ("vali", "တွန့်ခြင်း"): "တွန့်",                                    # ch6 = ch4; -tā «ခြင်း» is the compound's
    ("kappeti", "အသက်မွေးသည်"): "မွေးသည်",                               # ch4 = ch11, ch12 (jīvikaṃ kappeti)
    ("chando", "လိုလားမှု"): ("ဆန္ဒ", {"2-564"}),                         # «Chando kāmo» = «ဆန္ဒသည် ကာမ»
    ("nirodha", "ချုပ်ငြိမ်း"): ("ချုပ်ငြိမ်းခြင်း", {"2-803"}),            # first: saṅkhāranirodhe «…ချုပ်ငြိမ်းခြင်းကို»
    ("vibhava", "ဘဝ ပျောက်ကွယ်သည်"): ("ဘဝ ပျောက်ကွယ်ခြင်း", {"2-203"}),   # vibhavataṇhā, as ch17
    ("pathavīkasiṇaṃ", "မြေ ကသိုဏ်းကို အာရုံပြုသော"): "မြေ ကသိုဏ်း",         # ch12 = ch6, ch15 (rule 1)
    ("pītisukhaṃ", "ပီတိနှင့် သာယာမှု"): f_pitisukham,                       # ch12, ch13 formula = ch4, ch11
    ("ānupassī", "အဖန်ဖန် ရှုလျက်"): "အဖန်ဖန် ရှုသော",                       # ch4 = ch7, ch11 (rule 3)
    # ---- R: relative pronoun
    ("yaṃ", "ရှိသမျှ"): NONE,                                             # ch3 ^2-182, ch4 ^2-203, ^2-204
}

# reasons for values that now differ from pi-1 (merged into the scripts' REASONS for their map-table files)
REASONS = {
    "saññī": "map-harmonise rule P: adjective «…သော» (pi-1 «မှတ်သိသော» is the ālokasaññī form; here «မှတ်သိမှု ရှိသော»)",
    "saritā": "map-harmonise rule P: the agent noun «saritā hoti» «အောက်မေ့သူ» (pi-1 «စီးဆင်းတတ်သူ» is the taṇhā epithet)",
    "chando": "map-harmonise A: «Chando kāmo» = «ဆန္ဒသည် ကာမ» (pi-1 «လိုလားမှု» is kāmacchanda «ကာမကို လိုလားမှု»)",
    "vibhava": "map-harmonise A: vibhavataṇhā «ဘဝ ပျောက်ကွယ်ခြင်းကို တပ်မက်မှု» (the pi-2 text's noun; pi-1 «ဘဝ ပြတ်စဲခြင်း» "
               "is not in the segment, «ဘဝ ပျောက်ကွယ်သည်» is the vibhavadiṭṭhi clause)",
}

REASONS.update({k[:1].upper() + k[1:]: r for k, r in list(REASONS.items())})


def apply(kw, sid, v, my):
    """-> the aligned value of keyword kw in segment sid (v unchanged when no rule applies)."""
    r = FIX.get((low(kw), v))
    if r is None:
        return v
    if callable(r):
        return r(kw, v, my)
    if isinstance(r, tuple):
        new, sids = r
        return new if sid in sids else v
    return r
