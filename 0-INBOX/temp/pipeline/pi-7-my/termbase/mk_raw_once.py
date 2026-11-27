"""One-off writer of the first raw-multi.tsv / raw-align.tsv / raw-family.tsv / raw-textinc.tsv (pi-7 Burmese termbase).
The terms are taken from the files (a candidate of the senses file, a LOCKED pi-N term, or another pi-7 sense's term),
never typed, so no Burmese spelling can slip. After the first run the raw-*.tsv files are the source: build.py composes
them into decisions-A.tsv and later changes are made in the raw files. This script refuses to overwrite them unless
--force is given. usage: mk_raw_once.py [--force]"""
import pathlib, sys, collections
H = pathlib.Path(__file__).resolve().parent
B = H.parents[4]


def parse(p):
    d = {}
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.strip(): continue
        hw, body = line.split(": {", 1)
        d[hw] = [s.rsplit(": ", 1)[1].split(" / ") for s in body[:-1].split("; ")]
    return d


S7 = parse(B / "AI_translation/burmese/pi-7-pali-word-burmese-senses-plain.md")
LK = {n: parse(B / f"AI_translation/burmese/pi-{n}-pali-burmese-termbase-plain.md") for n in (1, 2, 3, 4, 5, 6)}


def L(n, hw, i=0):
    return LK[n][hw][i][0]


def S(hw, i=0):
    c = S7[hw][i]
    assert len(c) == 1, (hw, c)
    return c[0]


PRED = {
    "bare": lambda c: "ဟူသော အကြောင်း" not in c,
    "abl": lambda c: c.endswith("အကြောင်းကြောင့်"),
    "ablneg": lambda c: c.endswith("ကြောင့် မဟုတ်"),
    "nameneg": lambda c: c.endswith("အကြောင်း မဟုတ်ခြင်း"),
    "nogap": lambda c: "…" not in c,
    "tuu": lambda c: c.endswith("နှင့် တူသည်"),
}


def pick(key, how):
    hw, i = key.rsplit("|", 1)
    cl = S7[hw][int(i)]
    assert len(cl) > 1, key
    if how in PRED:
        hit = [c for c in cl if PRED[how](c)]
    elif isinstance(how, int):
        hit = [cl[how]]
    else:
        hit = [c for c in cl if c == how]
    assert len(hit) == 1, (key, how, cl)
    return hit[0]


R_BARE = ("the bare condition name N (map-table T1: lists, ghaṭanā and hyphen compounds; the dictionary form of the stem); "
          "family: the single-candidate stems Hetu / Ārammaṇa / adhipati / samanantara / āsevana / Kamma / vipāka / āhāra / indriya / "
          "Jhāna / sampayutta / vippayutta / purejāta / Vigata / Avigata have N; «Nဟူသော အကြောင်း» in a heading is the name by its frame (T1, grammar)")
R_ABL = ("T2 ablative «Nဟူသော အကြောင်းကြောင့်» (pi-2 avijjāpaccayā «…ကြောင့်»: the cause marker is the keyword's meaning); "
         "family: the single-candidate Xpaccayā (aññamañña-, nissaya-, vipāka-, āhāra-, indriya-, jhāna-, magga-, sampayutta-, vippayutta-, atthi-) "
         "have it; the name «…ဟူသော အကြောင်း» is the heading frame of the same word (T4, grammar)")
R_ABLNEG = ("T2 negative ablative «Nဟူသော အကြောင်းကြောင့် မဟုတ်» (the «ဘဲ» of «မဟုတ်ဘဲ» goes, rule 6); family: the single-candidate "
            "naXpaccayā (napurejāta-, naāsevana-, nakamma-, navipāka-, najhāna-, namagga- …); the name negative is the heading frame (T4, grammar)")
R_NAMENEG = ("the bare negative stem names the absent condition «Nဟူသော အကြောင်း မဟုတ်ခြင်း» (T1 negative, = Naxpaccayo, the headings); "
             "the same as the single-candidate heading stems Navipāka / Naāhāra / Nonatthi; «…ကြောင့် မဟုတ်» is the hyphen-chain part before -paccayā "
             "(^7-U265, T4: the compound's case, grammar)")
R_NOGAP = ("the contiguous term (pi-1 rule 3 dictionary form; family: the same item without «…» in the other cases); «… … …» is the R7 gap "
           "at the «လည်း» of ca / ceva in coordinated items (construction, map-harmonise §B kept)")
R_TUU = ("§A 4 decided: -sadisa «…နှင့် တူသည်» (map-table T5, rule 4 dictionary form; H19 / H24; = the single-candidate -sadisa terms); "
         "the text's «…နှင့် တူအောင်» before kātabbā / vitthāretabbā is the adverbial construction (T5), the rails keep it as INFLECTION")

MULTI = [  # key, how, reason
    ("Anantara|0", "bare", R_BARE + "; kept apart from samanantara «ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း» (approved sample)"),
    ("Natthi|0", "မရှိသည်", "locked pi-6 / pi-5 / pi-4 / pi-3 / pi-2 / pi-1 natthi «မရှိသည်» (dictionary verb form, rule 4; pi-6 the same with its «မရှိပါ။» answers); "
                         "«မရှိ» is the Q5 negated verb before another word in the notes (grammar)"),
    ("Natthi|1", "bare", R_BARE + "; sense 0 the verb «မရှိသည်» stays apart (NEW_SENSE)"),
    ("Atthi|1", "bare", R_BARE + "; sense 0 the verb «ရှိသည်» stays apart (NEW_SENSE)"),
    ("Nissaya|0", "bare", R_BARE),
    ("Sahajāta|0", 0, R_BARE + "; 119 of 120 uses; «အတူ ပေါ်ပေါက်သော» is the adjective in one heading (^7-1-1-1-4-57-10-0, grammar)"),
    ("Aññamañña|0", "bare", R_BARE + "; approved sample name (NEW); the pi-5 «အချင်းချင်း» is the adverb aññamaññaṃ (another sense, TAGDIFF), "
                             "a part of the name"),
    ("Upanissaya|0", "bare", R_BARE),
    ("Pacchājāta|0", "bare", R_BARE),
    ("hetupaccayā|0", "abl", R_ABL + "; 7098 of 7108 uses"),
    ("ārammaṇapaccayā|0", "abl", R_ABL),
    ("adhipatipaccayā|0", "abl", R_ABL),
    ("anantarapaccayā|0", "abl", R_ABL),
    ("samanantarapaccayā|0", "abl", R_ABL),
    ("sahajātapaccayā|0", "abl", R_ABL),
    ("upanissayapaccayā|0", "abl", R_ABL),
    ("purejātapaccayā|0", "abl", R_ABL),
    ("āsevanapaccayā|0", "abl", R_ABL),
    ("kammapaccayā|0", "abl", R_ABL),
    ("natthipaccayā|0", "abl", R_ABL),
    ("vigatapaccayā|0", "abl", R_ABL),
    ("avigatapaccayā|0", "abl", R_ABL),
    ("naadhipatipaccayā|0", "ablneg", R_ABLNEG),
    ("naārammaṇapaccayā|0", "ablneg", R_ABLNEG),
    ("Naanantara|0", "nameneg", R_NAMENEG),
    ("Napacchājāta|0", "nameneg", R_NAMENEG),
    ("Naadhipati|0", "nameneg", R_NAMENEG),
    ("naindriya|0", "nameneg", R_NAMENEG),
    ("namagga|0", "nameneg", R_NAMENEG),
    ("Paripuṇṇaṃ|0", 0, "locked pi-4 paripuṇṇaṃ «ပြည့်စုံသော» (same sense); 36 of 40 uses; «ပြည့်စုံစွာ» is the adverbial use (grammar, map-harmonise §B)"),
    ("uposathakammaṃ|0", 0, "§A 8 decided: map-table T11, an act compound carries its verb «ဥပုသ်ကို စောင့်ထိန်းသည်» (karoti / katvā then no direct "
                            "equivalent); 264 of 328 uses; = gāmaghātaṃ / nigamaghātaṃ / ekāgārikaṃ; «ဥပုသ် စောင့်ထိန်းခြင်း» and «ဥပုသ်…» are the "
                            "noun form and the …pe… cut (g2 G5); pi-2 uposatha «ဥပုသ်» (member) is a part of it"),
    ("suciṇṇāni|0", 0, "§A 15 decided: «ကောင်းစွာ ကျင့်ခဲ့ဖူးသော» (well practised, carati), 78 of 92 uses (1-01, 2-03, 2-05, 2-06, 2-13, 2-15 … 4-01); "
                       "the rails write «ကောင်းစွာ ကျင့်ခဲ့ဖူးသော အမှုတို့» for the 14 «ကောင်းစွာ ပြုခဲ့ဖူးသည်တို့» of 1-03 … 2-10"),
    ("assādeti|0", "သာယာသည်", "locked pi-5 assādeti «သာယာသည်» (same sense, rule 4 verb form); §A 7: «သာယာ» is the first of two verbs sharing one "
                              "«သည်» («သာယာ နှစ်သက်သည်», U1, construction)"),
    ("niruddhe|0", "ချုပ်ငြိမ်းသွားသော", "§A 35 decided: «ချုပ်ငြိမ်းသွားသော» (has ceased), 30 of 33 uses (1-03 … 1-05, 3-01, 3-09); the locked pi-5 / pi-6 / "
                                        "pi-1 «ချုပ်ငြိမ်းပြီးသော» never occurs in the pi-7 text (0 of 28 segments): kept and reported (brief), «…သွား…» is the "
                                        "candidate closest to its completed sense"),
    ("vipāko|0", "ကံ၏ အကျိုး ဖြစ်သော", "family: vipākā / vipākaṃ|0 / vipākānaṃ «ကံ၏ အကျိုး ဖြစ်သော» (pi-1 / pi-2 / pi-5 locked vipākā, vipākaṃ); 68 of 69 uses"),
    ("vipākassa|0", "ကံ၏ အကျိုး", "the noun of «kammaṃ vipākassa» (the tag: kamma is a condition for its result), 4 of 8 uses (^7-2-423, ^7-6-14, ^7-25-156, "
                                  "^7-32-452; phase-3 family alignment); the same word as vipāko «ကံ၏ အကျိုး ဖြစ်သော», whose «ဖြစ်သော» is the attributive "
                                  "(grammar); the noun stands in the attributive form too"),
    ("vipāke|1", "ကံ၏ အကျိုး", "the noun, 3 of 4 uses (= vipākassa|0); «ကံ၏ အကျိုး ဖြစ်သော» is the attributive before khandhe (grammar); sense 0 the "
                               "count locative «ကံ၏ အကျိုးဟူသော အကြောင်း» stays apart"),
    ("tadārammaṇatā|0", 0, "§A 16 decided: «ထိုအာရုံကိုပင် အာရုံပြုသော အဖြစ်» (tad- 'that same' = «ပင်», -tā 'state' = «အဖြစ်»), 25 of 28 uses "
                           "(1-03 … 1-05, 3-01, 3-09); the rails change the three «…အာရုံပြုသည့် အနေဖြင့်» of 1-01 / 2-05"),
    ("ṭhānāṭhānakosallassa|0", 0, "§A 14 decided: «ဖြစ်နိုင်ခြင်းနှင့် မဖြစ်နိုင်ခြင်း၌ ကျွမ်းကျင်ခြင်း», 7 of 12 uses (1-01, 2-05, 2-06, 3-02, 4-01), the plainer "
                                  "and shorter reading of ṭhāna / aṭṭhāna (what can and cannot be); no locked entry"),
    ("ekāgārikaṃ|0", 1, "§A 8 decided: T11 act compound with its verb «အိမ်တစ်လုံးတည်းကို ဝိုင်း၍ တိုက်သည်» (= gāmaghātaṃ, nigamaghātaṃ, uposathakammaṃ); "
                        "«အိမ်တစ်လုံးတည်း» is the …pe… cut of 4-01 (g4)"),
    ("gāmaghātaṃ|0", 0, "§A 8 decided: T11 act compound with its verb «ရွာကို ဖျက်ဆီး၍ လုယက်သည်» (= nigamaghātaṃ single, pi-5 rails «ရွာကို ဖျက်ဆီး၍ "
                        "လုယက်ရာ»); «ရွာ» is the …pe… cut of 4-01 (g4)"),
    ("sahajātaṃ|0", "အတူ ပေါ်ပေါက်ခြင်း", "the bare name as the label of the co-arising kind (H7 label, T1), 241 of 242 uses; «အတူ ပေါ်ပေါက်သော» is the "
                                         "adjective of «“sahajātaṃ kāmupādāna”nti» (^7-U409, grammar); the pi-2 «အတူ ဖြစ်ပေါ်သော» (another sense, "
                                         "TAGDIFF) never occurs in the pi-7 text"),
    ("nevavipākanavipākadhammadhammo|0", 0, "locked pi-2 (same sense), with its head noun «သဘောတရား» (dhammo), 463 of 527 uses; the shorter form is the "
                                            "attributive before a noun (grammar)"),
    ("saññojanādidukāni|0", 0, "§A 36 decided: «နှောင်ကြိုး စသည်တို့၏ နှစ်မျိုးတွဲ» (the dyads of the fetters and the rest), 6 of 7 headings (5-02, 5-08, "
                               "5-11, 5-12); the rails change 4-17 ^7-4-3-3-12-4-0"),
    ("paṭiccavārasadisā|0", "tuu", R_TUU + "; the plural «တူကြသည်» by the ending rule"),
    ("paṭiccavārasadiso|0", "tuu", R_TUU),
    ("paṭiccavārasadisaṃ|0", "tuu", R_TUU),
    ("dutiyagamanasadisaṃ|0", "tuu", R_TUU),
    ("sappītikadukasadisaṃ|0", "tuu", R_TUU),
    ("arūpadukasadisā|0", "tuu", R_TUU),
    ("Cittadukakusalasadisaṃ|0", "tuu", R_TUU),
    ("Lokiyadukaabyākatasadisaṃ|0", "tuu", R_TUU),
    ("pavattipaṭisandhi|0", 0, "§A 19 decided: pavatti «ဘဝ ဖြစ်စဉ်» (the process of existence), 10 of 12 uses, = pavattipaṭisandhiyā / pavatteyeva; "
                               "the rails change «ဘဝ ဖြစ်ဆဲ ကာလ» (2-01, 2-07); pi-6 pavatte «ဘဝ တည်နေစဉ်» is another headword (lemma level, not binding, "
                               "its words not in the pi-7 text)"),
    ("vibhajantena|0", "ခွဲခြမ်းစိတ်ဖြာလျက်", "§A 37 decided: the instrumental participle of a note = the adverbial «…လျက်», as anumajjantena «ပြန်လည် "
                                            "စိစစ်လျက်» (H10) and asammuyhantena «မရောထွေးစေဘဲ»; «ခွဲခြမ်းစိတ်ဖြာသူ» (^7-U409) is the agent-noun reading"),
    ("pahātabbahetukādhipati|0", "nogap", R_NOGAP + "; «ရှိသော» the attributive (rule 3)"),
]
for k in ["sahetuko|0", "sahetukassa|0", "sahetukañca|0", "Āsavasampayuttaṃ|0", "Āsavasampayutto|0", "sāsavañca|0", "sāsavo|0", "saññojaniyo|0",
          "saññojanasampayutto|0", "saññojaniyañca|0", "ganthasampayutto|0", "ganthaniyo|0", "nīvaraṇiyo|0", "nīvaraṇasampayutto|0",
          "nīvaraṇiyañca|0", "nīvaraṇasampayuttañca|0", "parāmaṭṭho|0", "Saṃkiliṭṭhañca|0", "saṃkiliṭṭho|0", "saṃkilesiko|0", "kilesasampayutto|0"]:
    MULTI.append((k, "nogap", R_NOGAP))

ALIGN = [  # part 2: single-candidate, same headword and sense as a LOCKED term that occurs in the pi-7 text
    ("samphaṃ|0", L(5, "samphaṃ"), "locked pi-5 review change B12 (pi-1 … pi-4 samphappalāpa); in all 9 segments (the text has «အကျိုးမဲ့ ပြိန်ဖျင်းသော "
                                    "စကားကို ပြောသည်»: the map split it after «အကျိုးမဲ့»); palapati keeps «ပြောသည်» (= pi-5 palapeyya)"),
    ("nillopaṃ|0", L(5, "nillopaṃ"), "locked pi-5 (same tag, the same deeds list, pi-5 rails «လုယက်ပစ္စည်းကို လုယူရာ»); harati keeps «လုယူသည်» (= pi-5 "
                                      "hareyya); the rails write «လုယက်ပစ္စည်းကို လုယူသည်» for «ဥစ္စာကို လုယူသည်» (9 segments)"),
    ("paripanthe|0", L(5, "paripanthe"), "locked pi-5 (same tag; pi-5 rails «လမ်း၌ ဓားပြ တိုက်…»); in all 9 segments, inside «လမ်းခရီး၌»"),
    ("vattabbaṃ|0", L(2, "vattabbaṃ"), "locked pi-2 / pi-1 vattabbaṃ «ခေါ်ဆို၍ ရ» (same tag, the same 'na vattabbaṃ' use); the pi-7 value «ခေါ်ဆို၍ "
                                       "မရသော» carried the negation of na (the only use, ^7-58-56), which the rails render as the negated verb «… မရသော» "
                                       "(Q5, INFLECTION), as pi-1 / pi-2 did"),
    ("nānākaraṇaṃ|0", L(5, "nānākaraṇaṃ"), "§A 27 decided: locked pi-5 «ကွဲပြားမှု» (same tag; in the pi-7 text at ^7-33-98 ninnānā); one noun for "
                                             "nānā(karaṇa): family ninnānākaraṇaṃ / ninnānākaraṇā / ninnānā «ကွဲပြားမှု မရှိ» (part 3)"),
]

FAMILY = [  # part 3: family re-alignments of single-candidate senses
    ("assādenti|0", L(5, "assādeti"), "family of assādeti (locked pi-5 «သာယာသည်», part 1): the same verb; «သာယာ» before «နှစ်သက်ကြသည်» is the shared "
                                       "ending (construction, §A 7)"),
    ("ninnānākaraṇaṃ|0", S("ninnānā"), "§A 27: family of nānākaraṇaṃ (locked pi-5 «ကွဲပြားမှု», part 2) and ninnānā «ကွဲပြားမှု မရှိ»; the rails change "
                                       "«ကွဲပြားချက် မရှိ» (57 uses)"),
    ("ninnānākaraṇā|0", S("ninnānā"), "§A 27: as ninnānākaraṇaṃ (13 uses)"),
    ("maggapaccaya|0", S("maggapaccayā"), "source slip for maggapaccayā (^7-12-5, written without the final -ā; map-harmonise §A 12): the intended "
                                         "word's term (pi-6 rule for slips); the text already has «မဂ်ဟူသော အကြောင်းကြောင့်» there"),
    ("sāsavassa|0", pick("sāsavo|0", "nogap"), "family of sāsavo / Sāsavaṃ / sāsavañca (part 1, locked pi-5 sāsavo): the contiguous term; the text's "
                                               "«… … …» gap at «လည်း» is the R7 construction"),
]

TEXTINC = [  # part 4: §A items decided by a term (single-candidate senses re-aligned)
    ("pacchājātasadisaṃ|0", S("pacchājātasadisaṃ").replace("နှင့် တူအောင်", "နှင့် တူသည်"),
     "§A 4 decided: -sadisa «…နှင့် တူသည်» (T5, H19; = the multi-candidate -sadisa decisions); the text's «…နှင့် တူအောင်» before the imperative is "
     "the adverbial construction, kept by the rails"),
]

if __name__ == "__main__":
    out = {"raw-multi.tsv": ("# Part 1: the 76 multi-candidate senses (hw|sense_index <TAB> term <TAB> reason); uses = multi-view.txt (whole book, "
                             "headwords case-insensitive)", [(k, pick(k, how), why) for k, how, why in MULTI]),
           "raw-align.tsv": ("# Part 2: single-candidate senses re-aligned to the LOCKED pi-6 / pi-5 / pi-4 / pi-3 / pi-2 / pi-1 term (same headword, "
                             "same sense; the locked term occurs in the pi-7 text)", ALIGN),
           "raw-family.tsv": ("# Part 3: family re-alignments of single-candidate senses (one Burmese word per Pāli lemma and sense; "
                              "family-scan-before.txt)", FAMILY),
           "raw-textinc.tsv": ("# Part 4: text inconsistencies of mapper-my/map-harmonise-notes.md §A decided by a term (single-candidate senses "
                               "re-aligned)", TEXTINC)}
    for f in out:
        if (H / f).exists() and "--force" not in sys.argv:
            sys.exit(f"{f} exists; the raw files are the source now (use --force only to start over)")
    keys = collections.Counter(k for _, (_, rows) in out.items() for k, _, _ in rows)
    assert all(n == 1 for n in keys.values()), [k for k, n in keys.items() if n > 1]
    for f, (hdr, rows) in out.items():
        (H / f).write_text(hdr + "\n" + "".join(f"{k}\t{t}\t{w}\n" for k, t, w in rows), encoding="utf-8", newline="\n")
        print(f, len(rows))
