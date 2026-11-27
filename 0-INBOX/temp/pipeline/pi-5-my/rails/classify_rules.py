"""INFLECTION / ARTEFACT rules of classify_misses.py (pi-5 Burmese rails):
(keyword regex, class, text-form regex that must match the segment, keyword-map forms (tuple) or None, reason,
Pāli check regex (a leading «!» = must NOT match) or None). The first matching rule classifies the row."""
NDE = ("(no direct equivalent)",)
GER = ("pahātabbaṃ|bhāvetabbaṃ|pariññeyyaṃ|sacchikātabbaṃ|vitthāretabbaṃ|cheditabbo|palapitabbaṃ|hantabbo|ṭhātabbaṃ|"
       "ekāgārikaṃ kātabbaṃ|bhaṇitabbā|paṭisevitabbo|ghātako")
OTHER = [
    # ---- INFLECTION: the same word, another grammatical form the loose test does not strip
    (GER, "INFLECTION", r"ရမည်(?!့)", None,
     "finite «…ရမည်» (the gerundive ends the sentence) of the attributive termbase form «…ရမည့်» (the keyword map's "
     "own value is the term)", None),
    (r"paṭilabheyya|kusalaṃ paṭilabheyya", "INFLECTION", r"ရရာ|ရခြင်း", None,
     "optative «…ရရာ» / verbal noun «…ရခြင်း» of the termbase «ရသည်» (the one-syllable verb «ရ» keeps «သည်» in the "
     "loose test)", r"paṭilabh"),
    (r"paṭilabhanti|gacchati|lābhī|suladdhaṃ|sotāpattiphalaṃ paṭiladdhaṃ|naccati|ādeyya|viññātāresu", "INFLECTION",
     r"ရ(?:ကြ|၏|သူ|ပြီ|ရာ|သော)|က(?:ကြ|၏|သလော|ရာ)|လက်ခံထိုက်|နားလည်(?:နိုင်)?", None,
     "the termbase word in another form (finite «…၏», plural «…ကြ», agent «…သူ»): the keyword map's own value is "
     "the term; the loose test cannot strip the ending of a one-syllable verb", None),
    (r"avasesaṃ|avaseso|avasesā", "INFLECTION", r"အကြွင်း|ကြွင်း", None,
     "the noun «(အ)ကြွင်း» (the remainder, in jīvitāvasesa / kappāvasesa / anavasesa «အကြွင်းမဲ့») of the attributive "
     "termbase «ကြွင်းကျန်သော»", r"vases"),
    # ---- ARTEFACT: approved frames and fixed wording (my5_formulas, the approved sample)
    (r"micchā", "ARTEFACT", r"ဟူသည် မှားသည်", ("မှားသည်",),
     "the verdict «… ဟူသည် မှားသည်» of the approved sample frame «…ti micchā» (decision micchā|0: «built by the formula "
     "module, not this term»)", r"micchā"),
    (r"niggahetabbe|niggahetabbā", "ARTEFACT", r"ချေပရ", None,
     "the approved frame sentence «hevaṃ niggahetabbe» «… ချေပရ…» (decision niggahetabbe|0: «the frame sentences keep "
     "the approved sample wording»)", r"niggahetabb"),
    (r"Tena hi|tena", "ARTEFACT", r"သို့ဖြစ်၍|သို့ဖြစ်လျှင်", None,
     "the approved frame (decision Tena hi|0: «သို့ဖြစ်၍» only in the frame «Na hevaṃ niggahetabbe. Tena hi …»; tena "
     "inside Tena hi has the phrase entry «သို့ဖြစ်လျှင်»)", r"(?i)tena hi"),
    (r"kathā", "ARTEFACT", r"အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း", None,
     "the approved BOOK TITLE «အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း» (book-title rule)", r"Kathāvatthu"),
    # ---- ARTEFACT: own entries of a compound / phrase (the keyword is its fragment)
    (r"paṭicca", "ARTEFACT", r"မှီ၍", ("မှီ၍",),
     "«X ca paṭicca Y ca uppajjati»: the absolutive is the phrase entry paṭicca uppajjati «မှီ၍ … ဖြစ်ပေါ်သည်» "
     "(decision paṭicca|0)", r"paṭicca .*uppajj"),
    (r"paccayatā", "ARTEFACT", r"ဤအကြောင်းကြောင့် ဤအကျိုး ဖြစ်ပုံ", None,
     "idappaccayatā has its own entry «ဤအကြောင်းကြောင့် ဤအကျိုး ဖြစ်ပုံ» (decision paccayatā|0)", r"idappaccayat"),
    (r"ñāṇaṃ|ñāṇa|ñāṇa niṭṭhitā", "ARTEFACT", r"မသိခြင်း", None,
     "aññāṇa has its own entries aññāṇa / aññāṇaṃ / Aññāṇe «မသိခြင်း»: ñāṇa is its fragment", r"(?i)aññāṇ"),
    (r"jātaṃ", "ARTEFACT", r"အတူ ပေါ်ပေါက်", None,
     "sahajātaṃ (co-arisen states): kept «… အတူ ပေါ်ပေါက်သော», the termbase's own sahajāta / sahajātā / sahajāto / "
     "sahajātānaṃ dhammānaṃ «အတူ ပေါ်ပေါက်…» in the same lists (jātaṃ «မွေးဖွားပြီးသော» would split one compound "
     "into two words; termbase doubt)", r"sahajāt"),
    (r"phalaṃ", "ARTEFACT", r"အကျိုး ကြီးမား", None,
     "approved rails-step note: mahapphalaṃ «အကျိုး ကြီးမားသော» (own entry), not phalaṃ «အသီးအပွင့်»", r"mahapphal"),
    (r"ṭhiti", "ARTEFACT", r"သိစိတ် တည်ရာ", None,
     "approved rails-step note: ṭhiti in viññāṇaṭṭhiti «သိစိတ် တည်ရာ» rendered by context (a station, not persistence)",
     r"viññāṇaṭṭhiti"),
    (r"ṭhiti", "ARTEFACT", r"စိတ်၏ တည်ခြင်း", None,
     "cittaṭṭhiti has its own entry «စိတ်၏ တည်ခြင်း» (decision ṭhiti|0 note)", r"(?i)cittaṭṭhit"),
    (r"dānaṃ", "ARTEFACT", r"အလှူ", None,
     "approved rails-step note: dānaṃ as the gift itself (dānaṃ deti / dadāti / datvā) «အလှူ», rendered by context",
     r"dānaṃ"),
    (r"uppādeyya", "ARTEFACT", r"ဖြစ်စေ", None,
     "approved rails-step note: methunaṃ uppādeyya «… ဖြစ်စေ» (bring about) by context", r"methun"),
    (r"eva", "ARTEFACT", r"သာ", ("သာ",),
     "approved rails-step note: the restrictive eva «သာ» (only) as a context sense", r"(?i)eva"),
    (r"aññā", "ARTEFACT", r"ကောင်းစွာ သိ၍|ရဟန္တာ ဖိုလ်ကို ထိုးဖောက်၍ သိ", None,
     "sammadaññāvimutto «ကောင်းစွာ သိ၍ လွတ်မြောက်ပြီးသူ» (approved arahant epithet) / aññāpaṭivedho (decision aññā|0: "
     "«သိ၍» only sammadaññāvimutto, «ရဟန္တာ ဖိုလ်» only aññāpaṭivedho)", r"sammadaññā|aññāpaṭivedh"),
    (r"anantarā", "ARTEFACT", r"ချက်ချင်း အကျိုးပေးသော", None,
     "anantarāpayutto has its own phrase entry Anantarāpayutto puggalo «ချက်ချင်း အကျိုးပေးသော ကံကို ပြုခဲ့သော "
     "ပုဂ္ဂိုလ်» (the deed of immediate result, not «right after»)", r"(?i)anantarāpayutt"),
    (r"bhāvitā|bhāvito", "ARTEFACT", r"ပွားများထား", None,
     "the formula bhāvitā bahulīkatā … «ပွားများထား…» keeps its own phrase-entry wording (decision bhāvitā|0)",
     r"bahulīkat"),
    (r"ṭhito", "ARTEFACT", r"တည်လျက်", None,
     "the phrase entry ṭhito parinibbāyati «တည်သော … ပရိနိဗ္ဗာန် ပြုသည်» (āneñje ṭhito parinibbāyati)",
     r"ṭhito parinibbāy"),
    (r"samāpannassa", "ARTEFACT", r"ဈာန်ကို ဝင်စားနေ", None,
     "jhānaṃ samāpannassa: the object is the segment's own jhāna «… ဈာန်ကို ဝင်စားနေသူ» (mapper §F5: the term «သမာပတ်ကို "
     "ဝင်စားနေသော» includes the object)", r"jhānaṃ samāpannassa"),
    (r"paṇīta", "ARTEFACT", r"မြတ်ခြင်း", None,
     "hīnapaṇītatā: paṇītatā has its own entry «မြတ်ခြင်း»", r"paṇītatā"),
    (r"parinibbuto", "ARTEFACT", r"ပရိနိဗ္ဗာန် ပြုတော်မူ", None,
     "the Buddha's uses add the honorific «တော်မူ» (decision parinibbuto|0: ^5-281, ^5-802, ^5-896)", r"parinibbuto"),
    (r"jāto", "ARTEFACT", r"ဖွားမြင်တော်မူ", None,
     "bhagavā jāto has its own entry «… ဖွားမြင်တော်မူသော» (decision jāto|0)", r"jāto"),
    (r"kiñci", "ARTEFACT", r"မည်သည့် .*မဆို", None,
     "yaṃ kiñci has its own entry Yaṃ kiñci «မည်သည့် … မဆို»", r"yaṃ kiñci"),
    (r"satta|sattānaṃ", "ARTEFACT", r"အသညသတ်", None,
     "the realm name asaññasatta «အသညသတ်» (proper names stay names; decision satta|0)", r"(?i)asaññasatt"),
    (r"citta", "ARTEFACT", r"စိတ္တ", None,
     "the iddhipāda name «စိတ္တ» (decision citta|0: «စိတ္တ» only the iddhipāda name at ^5-911)", r"iddhipād"),
    (r"dhamma", "ARTEFACT", r"ဓမ္မစကြာ", None,
     "the fixed name dhammacakka «ဓမ္မစကြာ» (own phrase entry, §A12)", r"dhammacakk"),
    (r"vādī", "ARTEFACT", r"မိမိဘက်|တစ်ဖက်သား|ပြောသော|ပြောသူ", None,
     "sakavādī «မိမိဘက်» (own approved entry) / musāvādī «… ပြောသော» (decision vādī|0: the honorific term is only for "
     "the Buddha)", r"sakavād|musāvād|paravād"),
    (r"kareyya", "ARTEFACT", r"လုယက်", None,
     "ekāgārikaṃ kareyya: the robbery phrase entry «… ဝိုင်းဝန်း၍ လုယက်သည်» (decision kareyya|0)", r"ekāgārik"),
    (r"pariññātaṃ", "INFLECTION", r"ပိုင်းခြား သိခြင်း", None,
     "dukkhapariññātaṃ is a nominal compound «ဒုက္ခကို ပိုင်းခြား သိခြင်း» (the verbal noun of the termbase participle "
     "«ပိုင်းခြား သိပြီးသော»)", r"dukkhapariññāt"),
    (r"paṭiladdho", "INFLECTION", r"ရရှိပြီ(?!း)", None,
     "the perfect predicate «… ရရှိပြီ» of the termbase participle «ရရှိပြီးသော» (khaṇo vo paṭiladdho)", r"paṭiladdh"),
    (r"samāpajjantassa", "INFLECTION", r"ဝင်စားနေ", None,
     "the present participle (samāpajjanta) «ဝင်စားနေသူ» of the termbase «ဝင်စားသူ»", r"samāpajjant"),
    (r"ṭhiti", "ARTEFACT", r"တည်နေသည့် အချိန်", None,
     "ṭhitikāla 'the moment of standing' rendered with the verb «တည်နေသည့် အချိန်» (the noun «တည်တံ့ခြင်း» does not fit "
     "the time phrase; decision ṭhiti|0 note)", r"ṭhitikāl"),
    (r"sabbattha", "ARTEFACT", r"ဘုံ အားလုံးသို့ ရောက်စေသော", None,
     "sabbatthagāminī paṭipadā: the witnessed pi-2 ^2-760 ten-powers phrase «ဘုံ အားလုံးသို့ ရောက်စေသော ကျင့်စဉ်» (kept "
     "for pi-1 … pi-4 identity; Sabbattha «နေရာတိုင်း» is the free adverb)", r"sabbatthagāmin"),
    (r"mātu", "ARTEFACT", r"မယ်တော်", None,
     "the Bodhisatta's mother: the honorific «မယ်တော်» (decision mātu|0 names ^5-401 as an honorific context)", r"mātu"),
    (r"mātā", "ARTEFACT", r"မိဘ", None,
     "the dvanda mātāpitaro «မိဘ» (parents, one Burmese word)", r"mātāpitar"),
    (r"vipākā", "ARTEFACT", r"အကျိုး ရှိသော", None,
     "sukhavipākā (bahubbīhi, 'having a pleasant result') «ချမ်းသာသော အကျိုး ရှိသော»; vipākā «ကံ၏ အကျိုး ဖြစ်သော» is the "
     "resultant states", r"sukhavipāk"),
    (r"karaṇaṃ", "ARTEFACT", r"ကွဲပြား", None,
     "nānākaraṇaṃ 'diversity' «… ကွဲပြား…», another sense than karaṇaṃ «ပြုတတ်သော» (aññāṇakaraṇa)", r"nānākaraṇ"),
    (r"dassana", "ARTEFACT", r"သိမြင်သော ဉာဏ်", None,
     "ñāṇadassana «… သိမြင်သော ဉာဏ်» as pi-4 vimuttiñāṇadassana (decision dassana|0 names it), not the noun «အမြင်»",
     r"ñāṇadassan"),
    (r"kareyya", "ARTEFACT", r"လက်ယာရစ်", None,
     "padakkhiṇaṃ kareyya: the idiom «လက်ယာရစ် …» (one Burmese verb for the phrase)", r"dakkhiṇaṃ"),
    (r"naccati", "INFLECTION", r"ကခုန်|ကပြ|က၏|ကသ|က၊", None,
     "the one-syllable verb «က» in another form (the keyword map's own value is the term)", r"naccat"),
    (r"abhisametuṃ", "ARTEFACT", r"ထင်ထင်ရှားရှား မသိမြင်", None,
     "nābhisametuṃ (negated): «… ထင်ထင်ရှားရှား မသိမြင်ဘဲ», the negative of the termbase «ထင်ထင်ရှားရှား သိမြင်ရန်» (fixed "
     "by rule R607)", r"nābhisamet"),
    (r"tiṭṭheyya", "ARTEFACT", r"ဓားပြ တိုက်", None,
     "paripanthe tiṭṭheyya «လမ်း၌ ဓားပြ တိုက်…» (decision tiṭṭheyya|0 sense 1 §A27)", r"paripanthe tiṭṭhe"),
    (r"gacchati", "INFLECTION", r"ရောက်|ရ", None,
     "the termbase verb in another form or sense entry of the same headword (saṅkhaṃ gacchati «… ရ…» / goes «ရောက်»; "
     "the one-syllable verb «ရ» keeps «သည်» in the loose test)", r"gacch"),
    (r"adhippāya", "ARTEFACT", r"တူညီသော ရည်ရွယ်ချက်", None,
     "ekādhippāya has its own entry «တူညီသော ရည်ရွယ်ချက်» (the heading Ekādhippāyakathā); adhippāya «အလိုအတိုင်း» is "
     "the wish of adhippāya-iddhi", r"(?i)ekādhipp"),
    (r"sattama", "ARTEFACT", r"ခုနစ်ကြိမ်မြောက် ဘဝ၌", None,
     "sattamabhavika has its own locked entry «ခုနစ်ကြိမ်မြောက် ဘဝ၌ ရှိသော» (coordinator 2026-11-22: the ordinal «သတ္တမ» "
     "is for the vagga headings only)", r"(?i)sattamabhavik"),
    # ---- ARTEFACT: no Burmese word of its own in the segment (the mapper's «(no direct equivalent)»)
    (r"(?!duppañño$|elamūgo$|jīvitā$).*", "ARTEFACT", r".", NDE,
     "the keyword map has no Burmese word for this keyword in the segment: a compound fragment, a particle or a relative "
     "pronoun absorbed in the Burmese construction (mapper rules Q7, rule 8, decision 4)", None),
    # ---- ARTEFACT: privative fragments (style rule a- / an- = «မ» + verb, «… မ…သေး…»)
    (r"uppannassa|niruddhe|pariññāta|paṭividdha|sacchikata|sacchikato|sacchikataṃ|sañjātaṃ|nibbattaṃ|pātubhūtaṃ|"
     r"abhinibbattaṃ|manasikārā|nipphanna|parinipphanna|parinipphannaṃ|viññātāresu|ādeyya|byāyiko|paṭiladdho", "ARTEFACT", r"မ\S*သေး|\S+ မ\S*သေး|နှလုံး မသွင်း|ပြုဖူး|ပြည့်စုံစွာ မဖြစ်ပေါ်|နား ?မလည်|လက်မခံထိုက်|မပျက်စီးတတ်|မရ", None,
     "privative fragment: the keyword is the positive part of an-uppanna / a-niruddha / a-pariññāta / a-ppaṭividdha / "
     "a-sacchikata / a-sañjāta / a-nibbatta / a-pātubhūta / an-abhinibbatta / a-manasikāra, rendered «မ … (သေး)» "
     "(style rule)", r"(?i)(?:^|[^a-zāīūṃṅñṭḍṇḷ])(?:an|a)(?:uppann|niruddh|pariññ|ppaṭivid|paṭivid|sacchik|sañjāt|"
     r"nibbatt|pātubh|abhinibbat|manasik|parinipphann|nipphann|viññāt|ppaṭiladdh|ādeyy|byāyik)"),
    # ---- ARTEFACT: senses the term does not cover (kept, termbase doubts)
    (r"uppajjati", "ARTEFACT", r"ပွင့်ထွန်းတော်မူ", None,
     "buddho loke uppajjati: the Buddha's arising «ပွင့်ထွန်းတော်မူ» (decision uppajjati|0: pi-4's context form "
     "«tathāgato loke uppajjati»)", r"buddh"),
    (r"du|su", "ARTEFACT", r"မွှေးသော|နံစော်သော", None,
     "sugandha / duggandha in the smell list: the plain words «မွှေးသော / နံစော်သော» (decision du|0: «Burmese speaker "
     "to check»; doubt)", r"(?:su|dug)gandh"),
    (r"para", "ARTEFACT", r"ပရနိမ္မိတ", None,
     "the proper name Paranimmitavasavattī «ပရနိမ္မိတဝသဝတ္တီ» (proper names stay names; decision para|0)", r"(?i)paranimmit"),
    (r"Añño|añño|aññaṃ", "ARTEFACT", r"အခြား", None,
     "the reciprocal «añño … aññassa» «တစ်ယောက် … အခြားတစ်ယောက်» / «aññaṃ … aññaṃ» (decision añño|0: «Burmese speaker "
     "to check the last three»; the term «တခြားစီ» (separate) would misread the reciprocal; doubt)", r"(?i)añño aññass|aññaṃ"),
    (r"vācāya", "ARTEFACT", r"စကား", None,
     "the speech itself «… စကား», not the door of speech «နှုတ်» (as pi-4 doubt 3; decision vācāya|0)", r"vācāy"),
]

# member changes of the layer / rules (zero-shot wording -> decided wording), used for the STALE phrase-entry check
STALE_SUBS = [
    ("ချုပ်ငြိမ်းရာ ဈာန် ဝင်စားခြင်း", "ချုပ်ငြိမ်းခြင်း သမာပတ်"), ("ချုပ်ငြိမ်းရာ ဈာန်", "ချုပ်ငြိမ်းခြင်း သမာပတ်"),
    ("မိမိ၏ အစွမ်းဖြင့်", "အစိုးရခြင်းဖြင့်"), ("တစ်ပြိုင်နက်", "အတူ"), ("အမြတ်ဆုံး", "ထိုထက် သာလွန်သည် မရှိသော"),
    ("သုခ ဒုက္ခ", "ချမ်းသာနှင့် ဆင်းရဲ"), ("သုခ", "ချမ်းသာ"), ("ကို ရရှိထားသော", "နှင့် ပြည့်စုံသော"),
    ("လမ်းကြောင်း သေချာပြီး", "ကျိန်းသေ"), ("ထိုးထွင်း သိ", "ခွဲခြား သိ"), ("သို့ ပို့ဆောင်တတ်", "ကို ဖြစ်စေတတ်"),
    ("ပို့ဆောင်တတ်", "ဖြစ်စေတတ်"), ("မှတ်ထင်", "မှတ်သိ"), ("သိမ်မွေ့သော ရုပ် ဓာတ်", "သိမ်မွေ့သော ရုပ်ဘုံ"),
    ("ရုပ်မရှိသော ဓာတ်", "ရုပ်မရှိသော ဘုံ"), ("ဖြန့်ကျက်", "ဖြန့်ကြဲ"), ("ဖြစ်ပေါ်သော", "မွေးဖွားပြီးသော"),
    ("ဈာန် ဝင်စားရာ", "သမာပတ်"), ("ထိုးထွင်း သိမြင်", "ထိုးဖောက်၍ သိ"), ("ပြည့်စုံစွာ ဝင်ရောက်၍", "ဝင်စား၍"),
    ("ယခုဘဝ", "မျက်မှောက်ဘဝ"), ("လူတို့၏", "လူ့"), ("ပြုပြီးသော", "ပြုခဲ့သော"), ("ယုတ်ခြင်း", "ယုတ်ညံ့ခြင်း"),
    ("ရောက်သော", "ရောက်သွားသော"), ("မှန်သမျှ", "မည်သည့် … မဆို"), ("စိမ်းစေသူ", "ထွက်စေသူ"), ("ဘုရား", "ဘုရားရှင်"),
    ("ချုပ်ငြိမ်းသွား", "ချုပ်ငြိမ်းပြီး"), ("တည်သည်", "တည်နေသည်"), ("မတုန်မလှုပ်", "မတုန်လှုပ်"),
    ("အမှန်တကယ် ဖြစ်ပေါ်ပြီး", "ပြည့်စုံစွာ ဖြစ်ပေါ်ပြီး"), ("ပြည့်စုံစွာ ပြီးမြောက်", "ပြည့်စုံစွာ ဖြစ်ပေါ်ပြီး"),
    ("ကုန်းချောစကား", "ကုန်းတိုက်သော စကား"), ("ခဏမျှသာ တည်", "ခဏ၌သာ ဖြစ်"), ("စိတ် တစ်ခု၏", "စိတ် တစ်"),
    ("တရား၏ တည်ရှိခြင်း", "သဘောတရားတို့၏ တည်နေခြင်း သဘော"), ("တရား၏ သေချာခြင်း", "သဘောတရားတို့၏ သေချာခြင်း"),
    ("ကဲ့ရဲ့အပ်", "ကန့်ကွက်အပ်"), ("ရပြီး", "ရရှိပြီး"), ("ယောကျ်ား", "ယောက်ျား"), ("ခုနစ်ကြိမ်မြောက်", "သတ္တမ"),
    ("အခါခပ်သိမ်း", "အလုံးစုံ"), ("ကျင့်ခဲ့", "ပြုခဲ့"), ("အစာ", "အာဟာရ"), ("နှစ်သက်ဖွယ် ကောင်းသော", "စိတ်နှင့် တွေ့သော"),
    ("လိုလားဖွယ် ကောင်း", "လိုလားဖွယ်ကောင်း"), ("ချစ်ခင်ဖွယ် ကောင်း", "ချစ်ခင်ဖွယ်ကောင်း"),
    ("တပ်မက်ဖွယ် ကောင်း", "တပ်မက်ဖွယ်ကောင်း"), ("အခြားသူ", "သူတစ်ပါး"), ("ဖြစ်ခြင်း", "ဖြစ်ပေါ်ခြင်း"),
    ("ရောနှောခြင်း မရှိ", "မရောယှက်"), ("ရောနှော", "ရောယှက်"), ("ဝဋ်", "သံသရာ စက်ဝန်း"), ("ကျင့်ကြံမှု", "အကျင့်"),
    ("လူ့လောက", "လူ့ပြည်"), ("ပြုသည်", "ပေးသည်"), ("ရသော", "ရရှိပြီးသော"), ("လူ အတွဲ", "လူ အစုံ"), ("ဒါန ပြု", "အလှူကို ပေး"), ("ဟောကြား", "ပြောကြား"), ("ဘဝ", "မွေးဖွားရာ အမျိုးအစား"),
]

# single words whose term only looks like a stale phrase (a generic verb or noun; classified by the OTHER rules)
STALE_NO = {"gacchati", "phalaṃ", "kareyya", "tiṭṭheyya", "voropetvā"}

# CONTEXT senses (termbase change 2026-11-22 «review fix round 2», APPROVED.md: not added as senses; the rails keep the
# review wording at these segments only): (keyword regex, segment ids, text-form regex that must match the rails
# segment, reason). A row is CONTEXT only in the listed segments.
CONTEXT = [
    (r"viloketi", ["5-401"], r"အရပ် အားလုံးကိုလည်း ကြည့်ရှု",
     "context sense (APPROVED.md round 2): sabbā ca disā viloketi «အရပ် အားလုံးကိုလည်း ကြည့်ရှု၏» (review A10, F22); "
     "the termbase sense «ဘေးသို့ ကြည့်သည်» stays for ^5-336, ^5-852"),
    (r"ādāna", ["5-546"], r"မပေးသည်ကို ယူခြင်း",
     "context sense (APPROVED.md round 2): adinnādāna «မပေးသည်ကို ယူခြင်း» (review B11, F13; = termbase ādānaṃ in "
     "adinnādānaṃ); the stem sense «ကိုင်ခြင်း» stays for ādānanikkhepanaṃ ^5-293"),
    (r"añño", ["5-89", "5-90"], r"အခြား မဖြစ်ဘဲ",
     "context sense (APPROVED.md round 2): anañño avigato «အခြား မဖြစ်ဘဲ မကွယ်ပျောက်ဘဲ» (review A17, R203 withdrawn; "
     "= the sample ^5-78); the termbase sense «တခြားစီ» stays elsewhere"),
]
