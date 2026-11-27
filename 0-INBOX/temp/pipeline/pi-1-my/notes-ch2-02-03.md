# pi-1 Burmese zero-shot, chapters 2-02 and 2-03 (Cittuppādakaṇḍa: fine-material, immaterial, three-plane and world-transcending wholesome cittas): notes

Status 2026-11-16: done, all checks pass. Not committed. Translated from the Pāli only
(AI_translation/pali/pi-1_split_chapters/2-02-…, 2-03-…). The English zero-shot was read for meaning only. No
Burmese translation, nissaya or web source was used.

## Files
- AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters/2-02-cittuppadakandam.md (143 segments, 174 lines)
- AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters/2-03-cittuppadakandam.md (96 segments, 109 lines)
- make_ch2-02-03.py: generator (`python3 -I -X utf8 make_ch2-02-03.py [2-02] [2-03] [--notes]`). It imports
  my_formulas.py and only ADDS entries in memory (extend(); add() refuses to change an existing value); my_formulas.py
  and my-zeroshot-terms.md are not touched. --notes rewrites the generated section at the end of this file.
- check_ch2-02-03.py: own per-line check (adapted from check_ch2-01.py, see its docstring). It imports the generator's
  tables (writes nothing). Mutation-tested: a dropped negation, a dropped opening phrase, a changed number, swapped
  synonyms, a dropped item of a list head, a wrong kasiṇa, and an unknown Pāli word in an opening are all reported.

## Checks (all pass)
- check_chapter_ids.py: 2-02 OK (143 segments); 2-03 OK (96 segments).
- pi-6-mr/check_text_pe.py: 2-02 OK (174 lines), 2-03 OK (109 lines), dashes match; chk-pe copies deleted.
- pi-4-mr/check_marks.py: OK, OK.
- check_ch2-02-03.py: OK, 0 mismatches (174 + 109 lines).

## How the new openings work
- A rule in CU_EXTRA_RULES takes «Yasmiṃ samaye … » up to «, / – / ␣ tasmiṃ samaye». Three heads:
  «rūpūpapattiyā / arūpūpapattiyā maggaṃ bhāveti» = «သိမ်မွေ့သော ရုပ်ဘုံ / ရုပ်မရှိသော ဘုံ၌ ဖြစ်ပေါ်ရန် လမ်းကို ပွားများ၍»;
  «[lokuttaraṃ X bhāveti…pe… ]* lokuttaraṃ X bhāveti niyyānikaṃ apacayagāmiṃ PURPOSE» = «… PURPOSE၊ လွတ်မြောက်ရာသို့
  ပို့ဆောင်သော၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သော၊ လောကကို ကျော်လွန်သော X-ကို ပွားများ၍» (purpose and adjectives move
  before the noun); «kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti Q» = «Q ကာမဘုံနှင့် ဆိုင်သော ကုသိုလ်စိတ်သည် ဖြစ်ပေါ်လာသော
  အချိန်၌» (as 2-01, the qualifiers before the citta).
- Jhāna: «[PRE] FORMULA … LASTJH upasampajja viharati Q» = «[PRE]၊ FORMULA… Q LASTJH-ကို ဝင်စား၍ နေသော အချိန်၌».
  The qualifiers Q (paṭipadā, object, kasiṇa, «-sahagataṃ», hīna / majjhima / paṇīta, adhipateyya, suññata,
  appaṇihita) are attributives in Burmese, so they stand before the last jhāna noun; the arūpa «…saññāsahagataṃ»
  (an adjective of the jhāna placed earlier in the Pāli) joins Q. Every «…pe…» stays one «…» in place; the dash of
  the third-jhāna quotation stays. upasampajja viharati = «ဝင်စား၍ နေ» (the sample's «ဈာန် ဝင်စား…»).
- Separators: Pāli space between two phrases = «၊ » (none before the jhāna noun); «, » = «၊ »; « – » kept; a Pāli
  comma that is missing stays missing.
- A synonym list closed by «, idaṃ tasmiṃ samaye» instead of a dash (^1-364) has its own rule (r_rel_comma).

## Main choices (one-line reasons)
- Mātikā strings reused unchanged: parittā / appamāṇā (+ -ārammaṇā), hīnā / majjhimā / paṇītā, niyyānikā,
  apacayagāmino, lokuttarā, rūpāvacarā / arūpāvacarā, savitakkā / savicārā / avitakkā / avicārā / avitakkavicāramattā,
  upekkhāsahagatā; QUAL / QUAL_ADV of 2-01 unchanged.
- maggaṃ in «rūpūpapattiyā maggaṃ» = «လမ်း» (the way to rebirth); lokuttara maggo / maggaṃ = MAGGA «မဂ်».
- paṭipadā = «ကျင့်စဉ်»; dukkha- / sukha-paṭipadā = «ခက်ခဲသော / လွယ်ကူသော» (difficult / easy: a different sense from
  the feeling words နာကျင် / သာယာ); abhiññā (dandha- / khippa-) = «ထူးကဲစွာ သိခြင်း နှေးကွေးသော / လျင်မြန်သော».
- kasiṇa = «ကသိုဏ်း» (everyday Burmese); X-kasiṇaṃ = «X ကသိုဏ်းကို အာရုံပြုသော» (TAKES of the sample); colours
  nīla / pīta / lohita / odāta = «အပြာ / အဝါ / အနီ / အဖြူ» (modern plain words).
- abhibhāyatana = «လွှမ်းမိုးရာ နယ်ပယ်» (abhibhuyya = «လွှမ်းမိုး၍»); bahiddhā here = «ပြင်ပ၌» (outside oneself; the
  Mātikā's «သူတစ်ပါး၌» is the sense «in others»); ajjhattaṃ = «မိမိ၌» as in the Mātikā; arūpasaññī = «ရုပ်ဟု
  မမှတ်သိဘဲ» (saññā = မှတ်သိ).
- vimokkha = «လွတ်မြောက်ခြင်း» (kept apart from the sample's vimutti «လွတ်မြောက်မှု»); brahmavihāra = «ဗြဟ္မစိုရ်»;
  mettā / karuṇā / muditā = everyday «မေတ္တာ / ကရုဏာ / မုဒိတာ»; asubha = «မတင့်တယ်ခြင်း» (subha = «တင့်တယ်»; the loan
  အသုဘ reads as «funeral»); the ten corpses described plainly («ဖူးရောင်နေသော အလောင်း» …), X-saññāsahagataṃ = «X-ဟု
  မှတ်သိမှုနှင့်အတူ ဖြစ်သော».
- Jhāna formula: vivicceva kāmehi = «ကာမတို့မှ ကင်းဆိတ်၍သာ»; vivekaja / samādhija = «ကင်းဆိတ်ခြင်းမှ / သမာဓိမှ
  ဖြစ်ပေါ်သော»; pītisukha = «ပီတိနှင့် သာယာမှု»; vūpasamā = «ငြိမ်းသွားခြင်းကြောင့်»; sampasādana = «ကြည်လင်မှု»;
  cetaso ekodibhāva = «စိတ်ကို စုစည်း တည်ငြိမ်စေသော» (no «တစ်ခု», which would read as the number one); virāga =
  «ပြယ်ပျောက်သွားခြင်း»; ariyā = «အရိယာတို့»; pahāna = «ပယ်ခြင်း»; atthaṅgama = «ချုပ်ငြိမ်းသွားခြင်း»; domanassa =
  «စိတ်ဆင်းရဲမှု» (not နှလုံးမသာမှု, which carries a negation syllable); upekkhāsatipārisuddhi = «ဥပေက္ခာကြောင့် သတိ
  စင်ကြယ်သော».
- Immaterial bases (āyatana = «နယ်ပယ်»): «အဆုံး မရှိသော ကောင်းကင် / သိစိတ် နယ်ပယ်», «ဘာမျှ မရှိသော နယ်ပယ်», «မှတ်သိမှု
  ရှိသည်လည်း မဟုတ်၊ မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်» (three negations, as neva-saññā-n-āsaññā).
- Lokuttara purposes: diṭṭhigata = «မှားယွင်းသော အယူ»; bhūmi = «အဆင့်»; kāmarāga = «ကာမကို တပ်မက်မှု» (as bhavataṇhā
  «ဘဝကို တပ်မက်မှု»); byāpāda = «ဖျက်ဆီးလိုစိတ်» (abyāpāda without မရှိခြင်း); tanubhāva = «ပါးလျစေရန်»; anavasesa =
  «အကြွင်းအကျန် မရှိအောင်»; māna = «မာန်»; uddhacca = «စိတ် ပျံ့လွင့်မှု» (one root with avikkhepa «စိတ် မပျံ့လွင့်ခြင်း»).
- 20 great methods: satipaṭṭhāna «သတိပဋ္ဌာန်», iddhipāda «ဣဒ္ဓိပါဒ်», bojjhaṅga «ဗောဇ္ဈင်», sacca «သစ္စာ» (everyday
  Burmese words); sammappadhāna = «မှန်ကန်သော ကြိုးပမ်းအားထုတ်ခြင်း» (SAMMA + the sample's PADHANA).
- New factors: anaññātaññassāmītindriya = «မသိရသေးသည်ကို သိရတော့မည်ဟူသော စွမ်းရည်»; aññindriya = «အပြည့်အဝ သိခြင်း၏
  စွမ်းရည်»; sammāvācā / -kammanta / -ājīva = «မှန်ကန်သော စကား / အလုပ် / အသက်မွေးမှု»; X-sambojjhaṅgo = «X ဗောဇ္ဈင်»;
  maggaṅga = «မဂ်၏ အင်္ဂါ»; maggapariyāpanna = «မဂ်၌ အကျုံးဝင်သောအရာ» (root of pariyāpannā «အကျုံးဝင်»).
- Abstinence list (sammāvācā …): nine distinct plain words; the privatives akiriyā / akaraṇaṃ / anajjhāpatti /
  velāanatikkamo each one «မ». setughāta = «တံတားကို ဖြိုဖျက်ခြင်း» (literal).
- Headings: Catukkanayo / Pañcakanayo = «ဈာန် လေးပါး / ငါးပါး နည်း»; soḷasakkhattuka = «တစ်ဆယ့်ခြောက်ကြိမ် နည်း»,
  aṭṭhakkhattuka = «ရှစ်ကြိမ် နည်း»; Tebhūmaka = «ဘုံ သုံးပါးနှင့် ဆိုင်သော»; Suññataṃ / Appaṇihitaṃ (heading and
  colophon) = «ဆိတ်သုဉ်းသော / တောင့်တမှု မရှိသော ဈာန်» (the jhāna added as a minor clarification; in the openings the
  bare attributive); Appamāṇāni (heading) = «အတိုင်းအဆ မရှိသော လွှမ်းမိုးရာ နယ်ပယ်များ» (noun added, parallel to
  «Abhibhāyatanāni parittāni»); Adhipati = «အကြီးအမှူး».
- Sigla «(bahūsu)» («in many editions») kept in Roman script as «Bahūsu», like the other sigla.
- Checker additions: NOT_NEG «ဗြဟ္မ»; the arūpa base names ākāsānañca- / viññāṇañca- (an-anta) and ākiñcañña- count as
  one negation each, nevasaññānāsañña- as three; compound numbers «တစ်ဆယ့်ခြောက်» (16) and «နှစ်ဆယ်» (20); verbs ending in
  «သည်» followed by a letter («ရှိသည်ကို», «ရှိသည်လည်း») are not finite verbs.

## Unsure Pāli / for the reviewer
- kāyena paṭisaṃvedeti (third jhāna) = «ကိုယ်ဖြင့် ခံစား၍» (body, plain), not the 2-01 KAYA «စိတ်၏ အဖော်တို့».
- «jānāmi passāmīti» = «သိ၏၊ မြင်၏ဟု မှတ်သိလျက်» and «subhanti» = «တင့်တယ်၏ဟု သဘောထား၍»: «perceiving / regarding» added
  so that the Burmese clause has a verb.
- abhiññā = «ထူးကဲစွာ သိခြင်း» (the loan အဘိညာဉ် reads as «supernormal powers»).
- Word order: the jhāna qualifiers stand before the LAST jhāna noun of an abbreviated series («ဒုတိယ ဈာန်… ပထမ ဈာန်…
  Q ပဉ္စမ ဈာန်ကို …»); the Pāli has them after «upasampajja viharati».
- sasaṅkhārena in the kāmāvacara series (^1-270) stays in place as the 2-01 adverb «တိုက်တွန်းမှုဖြင့်», before «…».
- nīla = «အပြာ» (blue); the traditional «ညို» was not used.

## Source slips (translated as written)
- ^1-165: «manindriyaṃ hoti upekkhindriyaṃ hoti» without comma: no «၊» there either.
- ^1-189: «pathavīkasiṇaṃ tasmiṃ samaye» without comma; ^1-204: «parittāni tāni» without comma: none in Burmese.
- ^1-167, ^1-180, ^1-182, ^1-202: a dash before «tasmiṃ samaye» instead of a comma: kept (dash rule).
- ^1-300 / ^1-301: «Katamo … sammākammanto / sammāājīvo hoti? Yā …» and ^1-304 «Katamo … sammāsamādhi»: gender
  mismatches of the relative / interrogative; no effect in Burmese.
- ^1-364: the aññindriya list ends «…, idaṃ tasmiṃ samaye …» without a dash, then «…pe… ye vā pana …»: kept.
- ^1-259 / ^1-261: jhāna series «dutiyaṃ … tatiyaṃ … paṭhamaṃ … catutthaṃ» (karuṇā / muditā): translated as written.

## New terms (generated by make_ch2-02-03.py --notes)

One «Pāli = Burmese» per line; all additive (no existing value changed).

### SIGLA

bahūsu = Bahūsu

### VAR_KIND

paṭhamajjhānaṃ = စာလုံးပေါင်းကွဲ
dutiyajjhānaṃ = စာလုံးပေါင်းကွဲ
tatiyajjhānaṃ = စာလုံးပေါင်းကွဲ
catutthajjhānaṃ = စာလုံးပေါင်းကွဲ
pañcamajjhānaṃ = စာလုံးပေါင်းကွဲ
dukkhāpaṭipadaṃ = စာလုံးပေါင်းကွဲ
sukhāpaṭipadaṃ = စာလုံးပေါင်းကွဲ
puḷuvakasaññāsahagataṃ = စာလုံးပေါင်းကွဲ
brahmavihārajjhānāni = စာလုံးပေါင်းကွဲ
asubhajjhānaṃ = စာလုံးပေါင်းကွဲ
arūpajjhānāni = စာလုံးပေါင်းကွဲ

### SYN

pītisambojjhaṅgo = ပီတိ ဗောဇ္ဈင်
samādhisambojjhaṅgo = သမာဓိ ဗောဇ္ဈင်
vīriyasambojjhaṅgo = ဝီရိယ ဗောဇ္ဈင်
satisambojjhaṅgo = သတိ ဗောဇ္ဈင်
dhammavicayasambojjhaṅgo = သဘောတရားများကို စိစစ်ခြင်း ဗောဇ္ဈင်
passaddhisambojjhaṅgo = ငြိမ်းအေးခြင်း ဗောဇ္ဈင်
maggaṅgaṃ = မဂ်၏ အင်္ဂါ
maggapariyāpannaṃ = မဂ်၌ အကျုံးဝင်သောအရာ
ārati = ရှောင်ခြင်း
virati = ရှောင်ကြဉ်ခြင်း
paṭivirati = ပြန်လှည့် ရှောင်ကြဉ်ခြင်း
veramaṇī = ကင်းဝေးခြင်း
akiriyā = မပြုခြင်း
akaraṇaṃ = မပြုလုပ်ခြင်း
anajjhāpatti = မကျူးလွန်ခြင်း
velāanatikkamo = နယ်နိမိတ်ကို မကျော်လွန်ခြင်း
setughāto = တံတားကို ဖြိုဖျက်ခြင်း

### NAMES

anaññātaññassāmītindriyaṃ = မသိရသေးသည်ကို သိရတော့မည်ဟူသော စွမ်းရည်
aññindriyaṃ = အပြည့်အဝ သိခြင်း၏ စွမ်းရည်
sammāvācā = မှန်ကန်သော စကား
sammākammanto = မှန်ကန်သော အလုပ်
sammāājīvo = မှန်ကန်သော အသက်မွေးမှု
navindriyāni = စွမ်းရည် ကိုးပါး
tivaṅgikaṃ jhānaṃ = အင်္ဂါ သုံးပါး ရှိသော ဈာန်
duvaṅgikaṃ jhānaṃ = အင်္ဂါ နှစ်ပါး ရှိသော ဈာန်
aṭṭhaṅgiko maggo = အင်္ဂါ ရှစ်ပါး ရှိသော မဂ်

### GEN

catūhi vacīduccaritehi = နှုတ်ဖြင့် ပြုသော ဒုစရိုက် လေးပါးမှ
tīhi kāyaduccaritehi = ကိုယ်ဖြင့် ပြုသော ဒုစရိုက် သုံးပါးမှ
micchāājīvā = မှားယွင်းသော အသက်မွေးမှုမှ
tesaṃ dhammānaṃ anaññātānaṃ adiṭṭhānaṃ appattānaṃ aviditānaṃ asacchikatānaṃ sacchikiriyāya = မသိရသေး၊ မမြင်ရသေး၊ မရောက်ရသေး၊ မတွေ့ရှိရသေး၊ မျက်မှောက် မပြုရသေးသော ထို သဘောတရားတို့ကို မျက်မှောက်ပြုရန် ဖြစ်သော
tesaṃ dhammānaṃ ñātānaṃ diṭṭhānaṃ pattānaṃ viditānaṃ sacchikatānaṃ sacchikiriyāya = သိပြီး၊ မြင်ပြီး၊ ရောက်ပြီး၊ တွေ့ရှိပြီး၊ မျက်မှောက်ပြုပြီးသော ထို သဘောတရားတို့ကို မျက်မှောက်ပြုရန် ဖြစ်သော

### HEAD

Rūpāvacarakusalaṃ = သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော ကုသိုလ်
Arūpāvacarakusalaṃ = ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော ကုသိုလ်
Tebhūmakakusalaṃ = ဘုံ သုံးပါးနှင့် ဆိုင်သော ကုသိုလ်
Lokuttarakusalaṃ = လောကကို ကျော်လွန်သော ကုသိုလ်
Catukkanayo = ဈာန် လေးပါး နည်း
Pañcakanayo = ဈာန် ငါးပါး နည်း
Catasso paṭipadā = ကျင့်စဉ် လေးပါး
Cattāri ārammaṇāni = အာရုံ လေးပါး
Dve ārammaṇāni = အာရုံ နှစ်ပါး
Soḷasakkhattukaṃ = တစ်ဆယ့်ခြောက်ကြိမ် နည်း
soḷasakkhattukaṃ = တစ်ဆယ့်ခြောက်ကြိမ် နည်း
soḷasakkhattukāni = တစ်ဆယ့်ခြောက်ကြိမ် နည်း
Aṭṭhakasiṇaṃ soḷasakkhattukaṃ = ကသိုဏ်း ရှစ်ပါး တစ်ဆယ့်ခြောက်ကြိမ် နည်း
Abhibhāyatanāni parittāni = အကန့်အသတ် ရှိသော လွှမ်းမိုးရာ နယ်ပယ်များ
Aṭṭhakkhattukaṃ = ရှစ်ကြိမ် နည်း
Idampi aṭṭhakkhattukaṃ = ဤသည်လည်း ရှစ်ကြိမ် နည်း
Appamāṇāni = အတိုင်းအဆ မရှိသော လွှမ်းမိုးရာ နယ်ပယ်များ
Aparampi aṭṭhakkhattukaṃ = နောက်ထပ် ရှစ်ကြိမ် နည်း
Imānipi abhibhāyatanāni soḷasakkhattukāni = ဤ လွှမ်းမိုးရာ နယ်ပယ်တို့လည်း တစ်ဆယ့်ခြောက်ကြိမ် နည်း
Tīṇi vimokkhāni soḷasakkhattukāni = လွတ်မြောက်ခြင်း သုံးပါး တစ်ဆယ့်ခြောက်ကြိမ် နည်း
Imānipi tīṇi vimokkhāni soḷasakkhattukāni = ဤ လွတ်မြောက်ခြင်း သုံးပါးလည်း တစ်ဆယ့်ခြောက်ကြိမ် နည်း
Cattāri brahmavihārajhānāni = ဗြဟ္မစိုရ် ဈာန် လေးပါး
Asubhajhānaṃ = မတင့်တယ်ခြင်း ဈာန်
Cattāri arūpajhānāni = ရုပ်မရှိသော ဈာန် လေးပါး
Suddhikapaṭipadā = ကျင့်စဉ် သက်သက်
Suññataṃ = ဆိတ်သုဉ်းသော ဈာန်
Suññatamūlakapaṭipadā = ဆိတ်သုဉ်းခြင်းကို အခြေခံသော ကျင့်စဉ်
Appaṇihitaṃ = တောင့်တမှု မရှိသော ဈာန်
Appaṇihitamūlakapaṭipadā = တောင့်တမှု မရှိခြင်းကို အခြေခံသော ကျင့်စဉ်
Vīsati mahānayā = နည်းကြီး နှစ်ဆယ်
Adhipati = အကြီးအမှူး
Lokuttaraṃ cittaṃ = လောကကို ကျော်လွန်သော စိတ်
Paṭhamo maggo = ပထမ မဂ်
Dutiyo maggo = ဒုတိယ မဂ်
Tatiyo maggo = တတိယ မဂ်
Catuttho maggo = စတုတ္ထ မဂ်
Cattāri brahmavihārajhānāni soḷasakkhattukāni = ဗြဟ္မစိုရ် ဈာန် လေးပါး တစ်ဆယ့်ခြောက်ကြိမ် နည်း
Asubhajhānaṃ soḷasakkhattukaṃ = မတင့်တယ်ခြင်း ဈာန် တစ်ဆယ့်ခြောက်ကြိမ် နည်း
Cattāri arūpajhānāni soḷasakkhattukāni = ရုပ်မရှိသော ဈာန် လေးပါး တစ်ဆယ့်ခြောက်ကြိမ် နည်း
Cattāri arūpajhānāni [arūpajjhānāni (sī. syā.)] soḷasakkhattukāni = ရုပ်မရှိသော ဈာန် လေးပါး [စာလုံးပေါင်းကွဲ (Sī., Syā.): arūpajjhānāni] တစ်ဆယ့်ခြောက်ကြိမ် နည်း

### COLO

Rūpāvacarakusalaṃ = သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော ကုသိုလ်
Arūpāvacarakusalaṃ = ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော ကုသိုလ်
Tebhūmakakusalaṃ = ဘုံ သုံးပါးနှင့် ဆိုင်သော ကုသိုလ်
Lokuttarakusalaṃ = လောကကို ကျော်လွန်သော ကုသိုလ်
Catukkanayo = ဈာန် လေးပါး နည်း
Pañcakanayo = ဈာန် ငါးပါး နည်း
Catasso paṭipadā = ကျင့်စဉ် လေးပါး
Cattāri ārammaṇāni = အာရုံ လေးပါး
Dve ārammaṇāni = အာရုံ နှစ်ပါး
Soḷasakkhattukaṃ = တစ်ဆယ့်ခြောက်ကြိမ် နည်း
soḷasakkhattukaṃ = တစ်ဆယ့်ခြောက်ကြိမ် နည်း
soḷasakkhattukāni = တစ်ဆယ့်ခြောက်ကြိမ် နည်း
Aṭṭhakasiṇaṃ soḷasakkhattukaṃ = ကသိုဏ်း ရှစ်ပါး တစ်ဆယ့်ခြောက်ကြိမ် နည်း
Abhibhāyatanāni parittāni = အကန့်အသတ် ရှိသော လွှမ်းမိုးရာ နယ်ပယ်များ
Aṭṭhakkhattukaṃ = ရှစ်ကြိမ် နည်း
Idampi aṭṭhakkhattukaṃ = ဤသည်လည်း ရှစ်ကြိမ် နည်း
Appamāṇāni = အတိုင်းအဆ မရှိသော လွှမ်းမိုးရာ နယ်ပယ်များ
Aparampi aṭṭhakkhattukaṃ = နောက်ထပ် ရှစ်ကြိမ် နည်း
Imānipi abhibhāyatanāni soḷasakkhattukāni = ဤ လွှမ်းမိုးရာ နယ်ပယ်တို့လည်း တစ်ဆယ့်ခြောက်ကြိမ် နည်း
Tīṇi vimokkhāni soḷasakkhattukāni = လွတ်မြောက်ခြင်း သုံးပါး တစ်ဆယ့်ခြောက်ကြိမ် နည်း
Imānipi tīṇi vimokkhāni soḷasakkhattukāni = ဤ လွတ်မြောက်ခြင်း သုံးပါးလည်း တစ်ဆယ့်ခြောက်ကြိမ် နည်း
Cattāri brahmavihārajhānāni = ဗြဟ္မစိုရ် ဈာန် လေးပါး
Asubhajhānaṃ = မတင့်တယ်ခြင်း ဈာန်
Cattāri arūpajhānāni = ရုပ်မရှိသော ဈာန် လေးပါး
Suddhikapaṭipadā = ကျင့်စဉ် သက်သက်
Suññataṃ = ဆိတ်သုဉ်းသော ဈာန်
Suññatamūlakapaṭipadā = ဆိတ်သုဉ်းခြင်းကို အခြေခံသော ကျင့်စဉ်
Appaṇihitaṃ = တောင့်တမှု မရှိသော ဈာန်
Appaṇihitamūlakapaṭipadā = တောင့်တမှု မရှိခြင်းကို အခြေခံသော ကျင့်စဉ်
Vīsati mahānayā = နည်းကြီး နှစ်ဆယ်
Adhipati = အကြီးအမှူး
Lokuttaraṃ cittaṃ = လောကကို ကျော်လွန်သော စိတ်
Paṭhamo maggo = ပထမ မဂ်
Dutiyo maggo = ဒုတိယ မဂ်
Tatiyo maggo = တတိယ မဂ်
Catuttho maggo = စတုတ္ထ မဂ်
Cattāri brahmavihārajhānāni soḷasakkhattukāni = ဗြဟ္မစိုရ် ဈာန် လေးပါး တစ်ဆယ့်ခြောက်ကြိမ် နည်း
Asubhajhānaṃ soḷasakkhattukaṃ = မတင့်တယ်ခြင်း ဈာန် တစ်ဆယ့်ခြောက်ကြိမ် နည်း
Cattāri arūpajhānāni soḷasakkhattukāni = ရုပ်မရှိသော ဈာန် လေးပါး တစ်ဆယ့်ခြောက်ကြိမ် နည်း

### Opening phrases: FORM

vivicceva kāmehi = ကာမတို့မှ ကင်းဆိတ်၍သာ
vivicca akusalehi dhammehi = အကုသိုလ် သဘောတရားတို့မှ ကင်းဆိတ်၍
savitakkaṃ = စတင်ကြံစည်မှု ရှိသော
savicāraṃ = ဆက်လက်သုံးသပ်မှု ရှိသော
vivekajaṃ pītisukhaṃ = ကင်းဆိတ်ခြင်းမှ ဖြစ်ပေါ်သော ပီတိနှင့် သာယာမှု ရှိသော
vitakkavicārānaṃ vūpasamā = စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှုတို့ ငြိမ်းသွားခြင်းကြောင့်
ajjhattaṃ sampasādanaṃ = မိမိ၌ ကြည်လင်မှု ရှိသော
cetaso ekodibhāvaṃ = စိတ်ကို စုစည်း တည်ငြိမ်စေသော
avitakkaṃ = စတင်ကြံစည်မှု မရှိသော
avicāraṃ = ဆက်လက်သုံးသပ်မှု မရှိသော
avitakkaṃ vicāramattaṃ = စတင်ကြံစည်မှု မရှိဘဲ ဆက်လက်သုံးသပ်မှုသာ ရှိသော
samādhijaṃ pītisukhaṃ = သမာဓိမှ ဖြစ်ပေါ်သော ပီတိနှင့် သာယာမှု ရှိသော
pītiyā ca virāgā = ပီတိလည်း ပြယ်ပျောက်သွားခြင်းကြောင့်
upekkhako ca viharati = ဥပေက္ခာ ရှိလျက်လည်း နေ၍
sato ca sampajāno = သတိ ရှိလျက် ကောင်းစွာ ဆင်ခြင်သိမြင်လျက်လည်း
sukhañca kāyena paṭisaṃvedeti = သာယာမှုကိုလည်း ကိုယ်ဖြင့် ခံစား၍
yaṃ taṃ ariyā ācikkhanti – "upekkhako satimā sukhavihārī"ti = အရိယာတို့က – “ဥပေက္ခာ ရှိသူ၊ သတိ ရှိသူ၊ သာယာစွာ နေသူ” ဟု ပြောကြားကြသော
sukhassa ca pahānā = သာယာမှုကိုလည်း ပယ်ခြင်းကြောင့်
dukkhassa ca pahānā = နာကျင်မှုကိုလည်း ပယ်ခြင်းကြောင့်
pubbeva somanassadomanassānaṃ atthaṅgamā = ရှေးဦးကပင် ဝမ်းမြောက်မှုနှင့် စိတ်ဆင်းရဲမှုတို့ ချုပ်ငြိမ်းသွားခြင်းကြောင့်
adukkhamasukhaṃ = မနာကျင် မသာယာသော
upekkhāsatipārisuddhiṃ = ဥပေက္ခာကြောင့် သတိ စင်ကြယ်သော
sabbaso rūpasaññānaṃ samatikkamā = ရုပ်ဟု မှတ်သိမှုတို့ကို အလုံးစုံ ကျော်လွန်ခြင်းကြောင့်
paṭighasaññānaṃ atthaṅgamā = ထိခိုက်မှုဟု မှတ်သိမှုတို့ ချုပ်ငြိမ်းသွားခြင်းကြောင့်
nānattasaññānaṃ amanasikārā = အမျိုးမျိုး ကွဲပြားမှုဟု မှတ်သိမှုတို့ကို နှလုံး မသွင်းခြင်းကြောင့်
sabbaso ākāsānañcāyatanaṃ samatikkamma = အဆုံး မရှိသော ကောင်းကင် နယ်ပယ်ကို အလုံးစုံ ကျော်လွန်၍
sabbaso viññāṇañcāyatanaṃ samatikkamma = အဆုံး မရှိသော သိစိတ် နယ်ပယ်ကို အလုံးစုံ ကျော်လွန်၍
sabbaso ākiñcaññāyatanaṃ samatikkamma = ဘာမျှ မရှိသော နယ်ပယ်ကို အလုံးစုံ ကျော်လွန်၍

### Opening phrases: QADJ

ākāsānañcāyatanasaññāsahagataṃ = အဆုံး မရှိသော ကောင်းကင် နယ်ပယ်ဟု မှတ်သိမှုနှင့်အတူ ဖြစ်သော
viññāṇañcāyatanasaññāsahagataṃ = အဆုံး မရှိသော သိစိတ် နယ်ပယ်ဟု မှတ်သိမှုနှင့်အတူ ဖြစ်သော
ākiñcaññāyatanasaññāsahagataṃ = ဘာမျှ မရှိသော နယ်ပယ်ဟု မှတ်သိမှုနှင့်အတူ ဖြစ်သော
nevasaññānāsaññāyatanasaññāsahagataṃ = မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်ဟု မှတ်သိမှုနှင့်အတူ ဖြစ်သော

### Opening phrases: QTAB

dukkhapaṭipadaṃ = ကျင့်စဉ် ခက်ခဲသော
sukhapaṭipadaṃ = ကျင့်စဉ် လွယ်ကူသော
dandhābhiññaṃ = ထူးကဲစွာ သိခြင်း နှေးကွေးသော
khippābhiññaṃ = ထူးကဲစွာ သိခြင်း လျင်မြန်သော
parittaṃ = အကန့်အသတ် ရှိသော
appamāṇaṃ = အတိုင်းအဆ မရှိသော
parittārammaṇaṃ = အကန့်အသတ် ရှိသည်ကို အာရုံပြုသော
appamāṇārammaṇaṃ = အတိုင်းအဆ မရှိသည်ကို အာရုံပြုသော
hīnaṃ = ယုတ်ညံ့သော
majjhimaṃ = အလယ်အလတ်
paṇītaṃ = မွန်မြတ်သော
suññataṃ = ဆိတ်သုဉ်းသော
appaṇihitaṃ = တောင့်တမှု မရှိသော
mettāsahagataṃ = မေတ္တာနှင့်အတူ ဖြစ်သော
karuṇāsahagataṃ = ကရုဏာနှင့်အတူ ဖြစ်သော
muditāsahagataṃ = မုဒိတာနှင့်အတူ ဖြစ်သော
somanassasahagataṃ = ဝမ်းမြောက်မှုနှင့်အတူ ဖြစ်သော
upekkhāsahagataṃ = ဥပေက္ခာနှင့်အတူ ဖြစ်သော
ñāṇasampayuttaṃ = ဉာဏ်နှင့် ယှဉ်တွဲသော
ñāṇavippayuttaṃ = ဉာဏ်နှင့် ကင်းကွာသော
sasaṅkhārena = တိုက်တွန်းမှုဖြင့်
pathavīkasiṇaṃ = မြေ ကသိုဏ်းကို အာရုံပြုသော
āpokasiṇaṃ = ရေ ကသိုဏ်းကို အာရုံပြုသော
tejokasiṇaṃ = မီး ကသိုဏ်းကို အာရုံပြုသော
vāyokasiṇaṃ = လေ ကသိုဏ်းကို အာရုံပြုသော
nīlakasiṇaṃ = အပြာ ကသိုဏ်းကို အာရုံပြုသော
pītakasiṇaṃ = အဝါ ကသိုဏ်းကို အာရုံပြုသော
lohitakasiṇaṃ = အနီ ကသိုဏ်းကို အာရုံပြုသော
odātakasiṇaṃ = အဖြူ ကသိုဏ်းကို အာရုံပြုသော
chandādhipateyyaṃ = ဆန္ဒကို အကြီးအမှူးပြုသော
vīriyādhipateyyaṃ = ဝီရိယကို အကြီးအမှူးပြုသော
cittādhipateyyaṃ = စိတ်ကို အကြီးအမှူးပြုသော
vīmaṃsādhipateyyaṃ = စုံစမ်းဆင်ခြင်မှုကို အကြီးအမှူးပြုသော
uddhumātakasaññāsahagataṃ = ဖူးရောင်နေသော အလောင်းဟု မှတ်သိမှုနှင့်အတူ ဖြစ်သော
vinīlakasaññāsahagataṃ = ညိုမည်းနေသော အလောင်းဟု မှတ်သိမှုနှင့်အတူ ဖြစ်သော
vipubbakasaññāsahagataṃ = ပြည်ယိုနေသော အလောင်းဟု မှတ်သိမှုနှင့်အတူ ဖြစ်သော
vicchiddakasaññāsahagataṃ = ပြတ်ထွက်နေသော အလောင်းဟု မှတ်သိမှုနှင့်အတူ ဖြစ်သော
vikkhāyitakasaññāsahagataṃ = ကိုက်စားခံရသော အလောင်းဟု မှတ်သိမှုနှင့်အတူ ဖြစ်သော
vikkhittakasaññāsahagataṃ = ပြန့်ကျဲနေသော အလောင်းဟု မှတ်သိမှုနှင့်အတူ ဖြစ်သော
hatavikkhittakasaññāsahagataṃ = ခုတ်ထစ်၍ ပြန့်ကျဲနေသော အလောင်းဟု မှတ်သိမှုနှင့်အတူ ဖြစ်သော
lohitakasaññāsahagataṃ = သွေးစွန်းနေသော အလောင်းဟု မှတ်သိမှုနှင့်အတူ ဖြစ်သော
puḷavakasaññāsahagataṃ = ပိုးလောက်တက်နေသော အလောင်းဟု မှတ်သိမှုနှင့်အတူ ဖြစ်သော
aṭṭhikasaññāsahagataṃ = အရိုးစုဟု မှတ်သိမှုနှင့်အတူ ဖြစ်သော

### Opening phrases: ADJ

parittāni = အကန့်အသတ် ရှိသော
appamāṇāni = အတိုင်းအဆ မရှိသော
suvaṇṇadubbaṇṇāni = အဆင်း လှသည်လည်း ရှိ၊ ဆိုးသည်လည်း ရှိသော
nīlāni = ပြာသော
nīlavaṇṇāni = အဆင်း ပြာသော
nīlanidassanāni = ပြာ၍ မြင်ရသော
nīlanibhāsāni = ပြာ၍ တောက်ပသော
pītāni = ဝါသော
pītavaṇṇāni = အဆင်း ဝါသော
pītanidassanāni = ဝါ၍ မြင်ရသော
pītanibhāsāni = ဝါ၍ တောက်ပသော
lohitakāni = နီသော
lohitakavaṇṇāni = အဆင်း နီသော
lohitakanidassanāni = နီ၍ မြင်ရသော
lohitakanibhāsāni = နီ၍ တောက်ပသော
odātāni = ဖြူသော
odātavaṇṇāni = အဆင်း ဖြူသော
odātanidassanāni = ဖြူ၍ မြင်ရသော
odātanibhāsāni = ဖြူ၍ တောက်ပသော

### Opening phrases: PRE_FIXED

ajjhattaṃ arūpasaññī bahiddhā rūpāni passati = မိမိ၌ ရုပ်ဟု မမှတ်သိဘဲ ပြင်ပ၌ ရုပ်တို့ကို မြင်၍
rūpī rūpāni passati = ရုပ် ရှိသူ ဖြစ်၍ ရုပ်တို့ကို မြင်၍
subhanti = တင့်တယ်၏ဟု သဘောထား၍

### Opening phrases: HEADS

rūpūpapattiyā maggaṃ bhāveti = သိမ်မွေ့သော ရုပ်ဘုံ၌ ဖြစ်ပေါ်ရန် လမ်းကို ပွားများ၍
arūpūpapattiyā maggaṃ bhāveti = ရုပ်မရှိသော ဘုံ၌ ဖြစ်ပေါ်ရန် လမ်းကို ပွားများ၍

### Opening phrases: PURPOSE

diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā = မှားယွင်းသော အယူတို့ကို ပယ်ရန်၊ ပထမ အဆင့်သို့ ရောက်ရန်
kāmarāgabyāpādānaṃ tanubhāvāya dutiyāya bhūmiyā pattiyā = ကာမကို တပ်မက်မှုနှင့် ဖျက်ဆီးလိုစိတ်တို့ ပါးလျစေရန်၊ ဒုတိယ အဆင့်သို့ ရောက်ရန်
kāmarāgabyāpādānaṃ anavasesappahānāya tatiyāya bhūmiyā pattiyā = ကာမကို တပ်မက်မှုနှင့် ဖျက်ဆီးလိုစိတ်တို့ကို အကြွင်းအကျန် မရှိအောင် ပယ်ရန်၊ တတိယ အဆင့်သို့ ရောက်ရန်
rūparāgaarūparāgamānauddhaccaavijjāya anavasesappahānāya catutthāya bhūmiyā pattiyā = သိမ်မွေ့သော ရုပ်ဘုံကို တပ်မက်မှု၊ ရုပ်မရှိသော ဘုံကို တပ်မက်မှု၊ မာန်၊ စိတ် ပျံ့လွင့်မှု၊ အမှန်ကို မသိမှုတို့ကို အကြွင်းအကျန် မရှိအောင် ပယ်ရန်၊ စတုတ္ထ အဆင့်သို့ ရောက်ရန်

### Opening phrases: LOKX

lokuttaraṃ jhānaṃ bhāveti = လောကကို ကျော်လွန်သော ဈာန်ကို ပွားများ၍
lokuttaraṃ maggaṃ bhāveti = လောကကို ကျော်လွန်သော မဂ်ကို ပွားများ၍
lokuttaraṃ satipaṭṭhānaṃ bhāveti = လောကကို ကျော်လွန်သော သတိပဋ္ဌာန်ကို ပွားများ၍
lokuttaraṃ sammappadhānaṃ bhāveti = လောကကို ကျော်လွန်သော မှန်ကန်သော ကြိုးပမ်းအားထုတ်ခြင်းကို ပွားများ၍
lokuttaraṃ iddhipādaṃ bhāveti = လောကကို ကျော်လွန်သော ဣဒ္ဓိပါဒ်ကို ပွားများ၍
lokuttaraṃ indriyaṃ bhāveti = လောကကို ကျော်လွန်သော စွမ်းရည်ကို ပွားများ၍
lokuttaraṃ balaṃ bhāveti = လောကကို ကျော်လွန်သော စွမ်းအားကို ပွားများ၍
lokuttaraṃ bojjhaṅgaṃ bhāveti = လောကကို ကျော်လွန်သော ဗောဇ္ဈင်ကို ပွားများ၍
lokuttaraṃ saccaṃ bhāveti = လောကကို ကျော်လွန်သော သစ္စာကို ပွားများ၍
lokuttaraṃ samathaṃ bhāveti = လောကကို ကျော်လွန်သော စိတ်ငြိမ်သက်ခြင်းကို ပွားများ၍
lokuttaraṃ dhammaṃ bhāveti = လောကကို ကျော်လွန်သော သဘောတရားကို ပွားများ၍
lokuttaraṃ khandhaṃ bhāveti = လောကကို ကျော်လွန်သော အစုအဝေးကို ပွားများ၍
lokuttaraṃ āyatanaṃ bhāveti = လောကကို ကျော်လွန်သော အာရုံခံ နယ်ပယ်ကို ပွားများ၍
lokuttaraṃ dhātuṃ bhāveti = လောကကို ကျော်လွန်သော ဓာတ်ကို ပွားများ၍
lokuttaraṃ āhāraṃ bhāveti = လောကကို ကျော်လွန်သော အာဟာရကို ပွားများ၍
lokuttaraṃ phassaṃ bhāveti = လောကကို ကျော်လွန်သော တွေ့ထိမှုကို ပွားများ၍
lokuttaraṃ vedanaṃ bhāveti = လောကကို ကျော်လွန်သော ခံစားမှုကို ပွားများ၍
lokuttaraṃ saññaṃ bhāveti = လောကကို ကျော်လွန်သော မှတ်သိမှုကို ပွားများ၍
lokuttaraṃ cetanaṃ bhāveti = လောကကို ကျော်လွန်သော စေ့ဆော်မှုကို ပွားများ၍
lokuttaraṃ cittaṃ bhāveti = လောကကို ကျော်လွန်သော စိတ်ကို ပွားများ၍

### Opening phrases: MISC

niyyānikaṃ apacayagāmiṃ = လွတ်မြောက်ရာသို့ ပို့ဆောင်သော၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သော
tāni abhibhuyya jānāmi passāmīti = ထိုရုပ်တို့ကို လွှမ်းမိုး၍ သိ၏၊ မြင်၏ဟု မှတ်သိလျက်
ajjhattaṃ arūpasaññī bahiddhā = မိမိ၌ ရုပ်ဟု မမှတ်သိဘဲ ပြင်ပ၌
rūpāni passati = ရုပ်တို့ကို မြင်၍
upasampajja viharati = ဝင်စား၍ နေသော
kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti = ကာမဘုံနှင့် ဆိုင်သော ကုသိုလ်စိတ်သည် ဖြစ်ပေါ်လာသော

### Opening phrases: JH

paṭhamaṃ jhānaṃ = ပထမ ဈာန်
dutiyaṃ jhānaṃ = ဒုတိယ ဈာန်
tatiyaṃ jhānaṃ = တတိယ ဈာန်
catutthaṃ jhānaṃ = စတုတ္ထ ဈာန်
pañcamaṃ jhānaṃ = ပဉ္စမ ဈာန်
