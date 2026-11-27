# pi-7 Burmese keyword mapping, phase 2, group g2 (2-01 vitakkattika … 2-17 sanidassanasappaṭighattika)

Script: `map_g2.py`. It imports `map7_rules.py` unchanged (md5 909bed2528b27eb55051c73f3ce28f81) and holds one table
for the 17 chapters (`G2`), two per-segment overrides (`CTX`) and one context function (`f_natthi_g2`). Burmese comes
from the FINAL pi-7 text and the pi-1 … pi-6 mappings only. Helper scripts (read-only checks) are in
`work/*_g2.py`.

## Numbers

| chapter | lines | bad | presence failures | «, » / «၊» / « / » | (no direct equivalent) |
|---|---|---|---|---|---|
| 2-01-vitakkattika | 236 | [] | 0 | 0 | 4 |
| 2-02-pitittika | 96 | [] | 0 | 0 | 5 |
| 2-03-dassanenapahatabbattika | 201 | [] | 0 | 0 | 2 |
| 2-04-dassanenapahatabbahetukattika | 208 | [] | 0 | 0 | 0 |
| 2-05-acayagamittika | 169 | [] | 0 | 0 | 1 |
| 2-06-sekkhattika | 162 | [] | 0 | 0 | 1 |
| 2-07-parittattika | 178 | [] | 0 | 0 | 3 |
| 2-08-parittarammanattika | 80 | [] | 0 | 0 | 3 |
| 2-09-hinattika | 9 | [] | 0 | 0 | 0 |
| 2-10-micchattaniyatattika | 140 | [] | 0 | 0 | 3 |
| 2-11-maggarammanattika | 98 | [] | 0 | 0 | 0 |
| 2-12-uppannattika | 49 | [] | 0 | 0 | 1 |
| 2-13-atitattika | 45 | [] | 0 | 0 | 1 |
| 2-14-atitarammanattika | 88 | [] | 0 | 0 | 0 |
| 2-15-ajjhattattika | 119 | [] | 0 | 0 | 2 |
| 2-16-ajjhattarammanattika | 63 | [] | 0 | 0 | 1 |
| 2-17-sanidassanasappatighattika | 125 | [] | 0 | 0 | 1 |
| **g2** | **2066** | **[]** | **0** | **0** | **28** |

- The 28 (no direct equivalent) are all karoti (14) and katvā (14) after an act compound (T11, U2). The act
  compounds are uposathakammaṃ, gāmaghātaṃ, nigamaghātaṃ and ekāgārikaṃ.
- Keyword uses: 33821. Of these, 15743 are taken unchanged from pi-1 … pi-6 and 16682 are keywords pi-1 … pi-6 never
  mapped. 1396 uses in 73 keyword / value pairs differ from pi-1 … pi-6 (see below).
- Presence: every chunk of every value stands in its segment's Burmese. Where it is not literal, it matches one of
  the approved ending rules (verb, attr, attr-fut, neg-verb, …), and there are no other exceptions.
- Extra checks (not required, `work/sentchk_g2.py -g`, `work/wordchk_g2.py`): every value is present in the aligned
  sentence of its keyword wherever the Pāli and Burmese sentence counts agree (33595 of 33821 uses). The one
  exception is the text's own omission of «ဖြစ်ပေါ်သည်» (§E 6). The 14 unaligned segments (226 uses) were checked by
  eye.
- Reproducibility: two runs give byte-identical `.mapped.md` files.

## A. Rules used (unchanged)

- pi-1 rules 1-11 and the agreed later pi-1 rules:
  - nouns without their final particles (rule 1);
  - adjectives and participles «…သော», gerundives «…ရမည့်» (rule 3);
  - verbs «…သည်» (rule 4);
  - «၊» dropped inside a term (rule 6);
  - « … » for discontinuous parts (rule 10);
  - one sense per segment (rule 11);
  - absolutives «…၍».
- pi-2 N1-N11: Xpaccayā «…ကြောင့်», and one Burmese word for two members.
- pi-4 P6 (agent nouns «…သူ»).
- pi-5 Q1 / Q5, and S1 with the M1 guard.
- pi-6 R1 / R7 / R8.
- Phase 1 T1-T13, M1, M2, and the coordinator's decisions U1-U5.
- The pi-1 … pi-6 values where the segment has them as the keyword's own word (U3):
  - atthappaṭisambhidāya: pi-2 atthapaṭisambhidā;
  - paṭibhānappaṭisambhidāya: pi-2;
  - X-sampadaṃ «X ပြည့်စုံခြင်း»: pi-4 sīlasampadā;
  - pañcāyatanāni: āyatanāni «အာရုံခံ နယ်ပယ်»;
  - mātikāpadāni: mātikā + padāni;
  - aniccānupassanā: pi-2 anupassanā «အဖန်ဖန် ရှုခြင်း»;
  - niyatamicchādiṭṭhiyā: niyatā + micchādiṭṭhi.

## B. New rules (g2), with reasons

- **G2-1, natthi in a note** (`f_natthi_g2`). The module's f_natthi gives «မရှိသည်» wherever the segment has that
  phrase anywhere. Where every Pāli sentence holding natthi has only the bare «မရှိ» in its aligned Burmese sentence,
  the value is «မရှိ». Example: «(… paṭisandhikkhaṇe natthi)» «(… ခဏ၌ မရှိ)».
  - Reason: pi-5 Q5, and phase 1 already decided «မရှိ» for the notes.
  - Effect: 5 uses. Everything else stays with the module.
- **G2-2, neva-X of the pahātabba triads.** nevadassanena = «သစ္စာကို မြင်ခြင်း … မဟုတ်», the counterpart of the module's
  nabhāvanāya «ဘာဝနာ ပွားများခြင်း … မဟုတ်သော».
  - Reason: rule 10. The keyword's parts are «သစ္စာကို မြင်ခြင်း» and the «မဟုတ်» of its own clause; the «ဖြင့်လည်း
    ပယ်ရမည်» in between belongs to pahātabba. The first clause ends «မဟုတ်၊», so there is no «သော» (19 uses).
- **G2-3, a term-mūlaka note.** X-mūlake = «X … အခြေခံခြင်း» and X-mūlakā = «X … အခြေခံသော». X is the module's term value
  (the condition mūlakas: «Nဟူသော အကြောင်းကို အခြေခံခြင်း»).
  - Reason: the text supplies the head noun «သဘောတရားကို», which the Pāli does not have. Phase 1 §A 5 maps the head
    nouns the text adds without the noun (Abyākatamūlaṃ). Rule 10 gives the gap.
  - Keywords: Avitakkavicāramattamūlakā, Anidassana(s)appaṭighamūlake / -ā (14 uses).
- **G2-4, participles in -antena take the text's adverbial form**, as the frame's anumajjantena «ပြန်လည် စိစစ်လျက်» does:
  - gacchantena «တွဲ၍ သွားစေလျက်»;
  - asammohantena «မရောထွေးစေဘဲ».

  The nominative -amāno keeps pi-5's «…သော» (patthayamāno «တောင့်တသော», S1, matched by the approved attr ending
  «လျက်»).
- **G2-5, the bare verb keyword of a «na …» clause** takes the positive dictionary form, because na is not a keyword in
  these files:
  - likhitā «ရေးထားသော» (the text has «မရေးထားသော»);
  - samenti «ညီသည်» (the text has «မညီကြ», neg-verb ending).

## C. Module overrides (for phase 3; 125 uses)

| keyword | module value | g2 value | uses | reason |
|---|---|---|---|---|
| kāraṇena | အကြောင်း (pi-5) | နည်းလမ်း | 44 | «iminā kāraṇena» = «ဤနည်းလမ်းဖြင့်» in every g2 use (rule 1). The pi-5 «အကြောင်း» stands in these segments only in the condition names. Tuple (နည်းလမ်း, အကြောင်း). |
| uposathakammaṃ | ဥပုသ် | ဥပုသ် စောင့်ထိန်းခြင်း | 12 | Where the compound is cut off by …pe…, the text has the noun «ဥပုသ် စောင့်ထိန်းခြင်း…». With «ဥပုသ်» alone, the kamma part has no word (U2: the compound takes its whole act). Tuple (ဥပုသ်ကို စောင့်ထိန်းသည်, ဥပုသ် စောင့်ထိန်းခြင်း, ဥပုသ်). |
| Sekkhañca, sekkhañca, sekkhassa, sekkhe | ကျင့်ကြံဆဲသူ | ကျင့်ကြံဆဲသူ၏ | 23 | T7: a triad term takes one value in every case form, and the binding pi-1 / pi-2 value of Sekkhaṃ / Sekkho / sekkhā (as a qualifier) is «ကျင့်ကြံဆဲသူ၏». Sekkhaṃ and Sekkhañca of the same segments got different values. The person nouns sekkhā / Sekkhā / Sekkhānaṃ («ကျင့်ကြံဆဲသူတို့») keep «ကျင့်ကြံဆဲသူ». |
| asekkhassa, asekkhe | ကျင့်ကြံမှု ပြီးဆုံးသူ | ကျင့်ကြံမှု ပြီးဆုံးသူ၏ | 12 | as sekkha (pi-2 asekkho). |
| vipassanti | ထိုးထွင်း၍ ရှုကြသည် | ထိုးထွင်း၍ ရှုသည် | 9 | rule 4 / T10: the plural «ကြ» comes by the ending rule (as samāpajjanti «ဝင်စားသည်» and vipassati «ထိုးထွင်း၍ ရှုသည်»). |
| uppādenti | ဖြစ်စေကြသည် | ဖြစ်စေသည် | 4 | as vipassanti (uppādeti «ဖြစ်စေသည်»). |
| paripuṇṇā, paripuṇṇaṃ | ပြည့်စုံ (terms) | ပြည့်စုံသော / ပြည့်စုံစွာ | 7 | rule 3: the adjective «ပြည့်စုံသော», the frame's paripuṇṇaṃ value. The text's «ပြည့်စုံသည် / ပြည့်စုံကြသည်» matches by the attr ending. ^7-9-19 has only the adverb, so it gets «ပြည့်စုံစွာ». The bare stem «ပြည့်စုံ» is not a dictionary form. |
| gaṇetabbā, gaṇetabbāni, gaṇetabbo, vitthāretabbāni | …ရမည် | …ရမည့် | 7 | rule 3: gerundives «…ရမည့်» in every case, as the frame's gaṇetabbaṃ / vitthāretabbā. The term family gave the text's finite form. |
| natthi | မရှိသည် | မရှိ | 5 | G2-1. |
| atthi (^7-10-112) | ရှိခြင်း (cond) | ရှိသည် | 1 | «(idhāpi ārammaṇaupanissayā atthi)» «(… အမှီ ရှိသည်)» is the verb. «ရှိခြင်း» stands in the segment only in the condition name of atthipaccaye (CTX). |
| dukkhaṃ (^7-11-54) | နာကျင်မှု (pi-2) | ဆင်းရဲ | 1 | «pariyiṭṭhimūlakaṃ dukkhaṃ paccanubhoti» «… ဆင်းရဲကို ခံစားသည်». «နာကျင်မှု» stands only in kāyikassa dukkhassa (CTX). In ^7-11-56 the one dukkhaṃ keyword stays «နာကျင်မှု», because kāyikaṃ dukkhaṃ is the majority sense there. |

Suggested module changes:
- the term family should prefer a pi-1 … pi-6 value of a case sibling over the generator's term (sekkha);
- -tabbā / -tabbāni / -tabbo should get «…ရမည့်»;
- the plural verbs should lose «ကြ»;
- kāraṇena should be «နည်းလမ်း» in «iminā kāraṇena».

## D. Values that differ from pi-1 … pi-6 or from the sample (same keyword)

The 27 keyword / value pairs that phase 1 already lists (map-table.md, «Values different from pi-1 … pi-6») recur
here with the same reasons. Examples: assādeti «သာယာ», the counting locatives ārammaṇe / magge / vigate …, uppādeti,
paccavekkhati, datvā, deti, katvā, vuṭṭhahantassa, nirodhā, kusalākusalaṃ, sahajāto. The other pairs are below.

| keyword = g2 value | pi-1 … pi-6 value (uses) | reason |
|---|---|---|
| vatthu / Vatthu = မှီရာ ဝတ္ထု | အခြေခံ (190) | the module's STOCK value (the base of the Paṭṭhāna, «မှီရာ ဝတ္ထု» in the text); pi-3's «အခြေခံ» is another sense |
| pañhā = ပြဿနာ | မေးခွန်း (75) | the pi-7 text's word (T7 / terms) |
| sahajātaṃ = အတူ ပေါ်ပေါက်ခြင်း | အတူ ဖြစ်ပေါ်သော (57) | T1: the kind of a condition in a list «sahajātaṃ, purejātaṃ, …» |
| kāraṇena = နည်းလမ်း | အကြောင်း (44) | §C |
| ekādasa … tevīsa, tiṃsa = …ခု | …ပါး (119) | T6: the answer count takes the text's classifier «ခု» |
| sattapi = ခုနစ်ခု | သတ္တဝါ (9) | T6 count; pi-5 «သတ္တဝါ» is satta "being" |
| parikammaṃ = ကြိုတင် ပြင်ဆင်မှု | ပွတ်တိုက်ပေးခြင်း (16) | the jhāna preliminary (module STOCK); the pi-4 value is the bodily rubbing |
| vodānaṃ / vodānañca = စင်ကြယ်ခြင်း စိတ် | စင်ကြယ်ခြင်း (17) | the mind-moment name keeps «စိတ်» (phase 1 §A 5) |
| sammattaniyato = မှန်ကန်မှု၌ ကျိန်းသေသော | မှန်ကန်မှု၌ လမ်းကြောင်း သေချာပြီးသော (15) | the pi-7 text's term (the pi-1 value is not in the segment) |
| bhojanaṃ = အစားအစာ | ဘောဇဉ် (10) | the pi-7 text's word |
| anulomaṃ / Anulomañca / Anulomaṃ = လျော်ညီခြင်း စိတ် | အဟုတ်ပြ ပုံစံ (13) | the mind moment, not the order (harmonise H1, one sense per segment) |
| paro = သူတစ်ပါး | တစ်ဦး (9) | the text's «သူတစ်ပါးသည်»; pi-5 «တစ်ဦး» is not in the segment |
| kusale = ကုသိုလ် | ကုသိုလ် သဘောတရား (4) | rule 5: «သဘောတရား» only for a «dhammā» keyword |
| uppādenti = ဖြစ်စေသည် | ဖြစ်ပေါ်စေသည် (4) | the text's «ဖြစ်စေကြသည်» (§C); pi-5 «ဖြစ်ပေါ်စေသည်» is not in the segment |
| patthanā = တောင့်တခြင်း | ဆုတောင်းခြင်း (3) | the pi-7 text's word |
| aññamaññapaccaya, vippayutta, vigata, Atthi = the condition name | the plain word | T1 / T4 (hyphen-compound parts, headings) |
| cakkaṃ = စက် | လှည့်ပတ်ခြင်း (3) | the text's word |
| passitvā = ကြည့်၍ | မြင်၍ (2) | «passitvā kātabbaṃ» «ကြည့်၍ ပြုရမည်»; pi-4 «မြင်၍» is not in the segment |
| voropeti = သတ်သည် | ချသည် (2) | T11 «jīvitā voropeti» «အသက်မှ သတ်သည်» |
| gamanāni = သွားပုံ | လိုက်ခြင်း (1) | the text's «ထို သွားပုံများ» |
| Gaṇanāya = ရေတွက်ချက် | ရေတွက်ပုံ (1) | S1 kept, the text's «ရေတွက်ချက်၌» |
| byañjanena = စကားလုံး | အသွင် (1) | the text's «စကားလုံးနှင့်» |
| ante = အဆုံးတိုင်း | အစွန်း (1) | «ante ante» «အဆုံးတိုင်း၌» (rule 1) |
| asaññasattā = အသညသတ် | အသညသတ် ဘုံ (1) | the text has no «ဘုံ» here |
| vipākaṃ = ကံ၏ အကျိုး | ကံ၏ အကျိုး ဖြစ်သော (1) | the noun sense (phase 1 §B) |
| paripuṇṇaṃ = ပြည့်စုံစွာ | ပြည့်စုံသော (1) | §C (^7-9-19, the adverb) |

Against the sample (same keyword, another value by context):
- natthi «မရှိသည်» / «မရှိ» (sample «မရှိခြင်း» in a list);
- uposathakammaṃ «ဥပုသ် စောင့်ထိန်းခြင်း» / «ဥပုသ်» (§C);
- anulomaṃ «လျော်ညီခြင်း စိတ်»;
- assādeti «သာယာသည်», where the text has it (8; U1);
- rūpaṃ «အဆင်းအရောင်» (f_rupam);
- Anantara as a hyphen-compound part of a heading «… ဟူသော အကြောင်း» (T4);
- atthi «ရှိသည်» (the verb in a note);
- vipāke «ကံ၏ အကျိုး» (not the condition);
- naindriya / namagga «… မဟုတ်ခြင်း» (T4, a heading compound).

## E. S1 review (stem fallback): 25 uses, all kept, 0 corrected

Each use was checked by eye against the segment and the keyword's sense:

| keyword = value | uses | context |
|---|---|---|
| passati = မြင်သည် | 14 | «rūpaṃ passati» «… အဆင်းအရောင်ကို မြင်သည်» |
| vibhajitabbaṃ = ခွဲခြမ်းစိတ်ဖြာရမည့် | 4 | «… ခွဲခြမ်းစိတ်ဖြာရမည်» |
| Gaṇanāya = ရေတွက်ချက် | 1 | «ရေတွက်ချက်၌» |
| gaṇanāni = ရေတွက်ချက် | 1 | «ရေတွက်ချက် လေးခုလုံး» |
| bhinditvā = ဖြိုခွဲ၍ | 1 | «သံဃာကို ဖြိုခွဲ၍» |
| uppādetvā = ထွက်စေ၍ | 1 | «lohitaṃ uppādetvā» «သွေးကို ထွက်စေ၍» |
| ninnānākaraṇā = ကွဲပြားချက် မရှိ | 1 | Q5 |
| patthayamāno = တောင့်တသော | 1 | pi-5 -amāno «…သော»; the text's «တောင့်တလျက်» (attr) |
| samenti = ညီသည် | 1 | G2-5 |

## F. Keywords newly mapped (68 keywords, 181 uses; all in `G2`)

- Gerundives «…ရမည့်»: dassetabbo, uddharitabbā, dīpetabbā / -o, niyāmetabbaṃ / -āni, kātabbāni, niddisitabbaṃ.
- Verbs, participles and absolutives: āgacchati «ပါဝင်လာသည်», passitvā «ကြည့်၍», vibhajitvā «ခွဲခြမ်းစိတ်ဖြာ၍», gahite
  «ယူသော» (locative absolute «ယူသောအခါ», rule 3), gacchantena, asammohantena, likhitā.
- Nouns:
  - paṭhamaudāharaṇe «ပထမ ဥပမာ», sattasu «ခုနစ်ခု», gamanāni «သွားပုံ», Sakabhaṇḍe «မိမိ ပစ္စည်း»;
  - missagataṃ «ရောစပ်ချက်», missakapañhā «ရောစပ် ပြဿနာ», pāḷiyaṃ «ပါဠိတော်»;
  - Paṭhamassa «ပထမ», paṭisandhicittaṃ «ပဋိသန္ဓေ စိတ်», paro «သူတစ်ပါး»;
  - pariyosānapadā «အဆုံးသတ် ပုဒ်», tividharūpasaṅgaho / -ena «ရုပ် သုံးမျိုးကို စုစည်းခြင်း»;
  - sādhukaṃ «ကောင်းစွာ», ante «အဆုံးတိုင်း», paṭighātatthāya «ချေဖျက်ရန်»;
  - dassitanayena «ပြထားသော နည်းအတိုင်း» (the text's adverbial phrase: no case particle to strip).
- Compounds:
  - pavattipaṭisandhi «ဘဝ ဖြစ်စဉ် … ပဋိသန္ဓေ» (or «ဘဝ ဖြစ်ဆဲ ကာလ …»; a dvandva, rule 10);
  - ārammaṇaupanissayā «အာရုံဖြင့် အားကြီးသော အမှီ» (= ārammaṇūpanissayo);
  - kusalasamāpattiṃ, kiriyasamāpattiṃ «ပြုရုံမျှသာ ဖြစ်သော သမာပတ်»;
  - viññāṇañcāyatanakiriyassa, nevasaññānāsaññāyatanakiriyaṃ (the kiriya adjective without the text's «စိတ်», §A 5 of
    phase 1);
  - ṭhānāṭhānakosallassa (two text forms, §G 2);
  - paṭhamajjhānapaccavekkhaṇaṃ «ပထမ ဈာန်ကို ပြန်လည် ဆင်ခြင်ခြင်း», maggapaccavekkhaṇaṃ;
  - appamāṇārammaṇaappamāṇacittasamaṅgissa, ajjhattārammaṇabahiddhācittasamaṅgissa («… စိတ်နှင့် ပြည့်စုံသူ», T12);
  - the X-sampadaṃ terms;
  - Natthivigatapaccayaṃ «မရှိခြင်းဟူသော အကြောင်း ပျောက်ကွယ်ခြင်းဟူသော အကြောင်း» (T1 names, rule 6).
- The neva-X and X-mūlaka terms of G2-2 and G2-3.
- vicākānaṃ (§G 1).

## G. Text inconsistencies (for the rails step; the translation is not changed)

1. **vicākānaṃ** (^7-7-114) is a Pāli slip for vipākānaṃ. The Burmese has vipāka's «ကံ၏ အကျိုး ဖြစ်သော», and the
   mapping follows it.
2. **ṭhānāṭhānakosallassa** has two renderings:
   - «ဖြစ်နိုင်ခြင်းနှင့် မဖြစ်နိုင်ခြင်း၌ ကျွမ်းကျင်ခြင်း» (2-05, 2-06);
   - «ဖြစ်နိုင်သော အကြောင်းနှင့် မဖြစ်နိုင်သော အကြောင်း၌ ကျွမ်းကျင်မှု» (2-07 ^7-13-74, 2-10 ^7-16-46).
3. **suciṇṇāni** has two renderings:
   - «ကောင်းစွာ ကျင့်ခဲ့ဖူးသော အမှုတို့» (2-03, 2-05, 2-06, 2-13, 2-15, 2-16, 2-17);
   - «ကောင်းစွာ ပြုခဲ့ဖူးသည်တို့» (2-01, 2-07, 2-08, 2-10).
4. **pavatti in pavattipaṭisandhi** is «ဘဝ ဖြစ်စဉ်» in 2-04, 2-14 and 2-15, and «ဘဝ ဖြစ်ဆဲ ကာလ» in 2-07 (also 2-01's
   «pavattipi» «ဘဝ ဖြစ်ဆဲ ကာလကိုလည်း»).
5. **uposathakammaṃ cut off by …pe…** is «ဥပုသ်…» in some segments and «ဥပုသ် စောင့်ထိန်းခြင်း…» in others.
6. **The text drops the verb**: «ဖြစ်ပေါ်သည်» (uppajjati) is missing in the aligned abbreviated sentence of ^7-9-19,
   ^7-9-42, ^7-10-20 and ^7-22-5. The value stands elsewhere in the segment.
7. **Head nouns the text adds** (as phase 1 §A 5): «သဘောတရားကို» inside the term-mūlaka notes (G2-3), and «စိတ်» after
   the kiriya compounds.
8. **The sekkha triad**:
   - the body has «ကျင့်ကြံဆဲသူ၏» (genitive), but the heading Sekkhattikaṃ has «ကျင့်ကြံဆဲသူ သုံးမျိုးတွဲ»;
   - the person nouns have «ကျင့်ကြံဆဲသူတို့».
9. **Pāli spelling variants** mapped as written:
   - paṭibhānapaṭisambhidāya (2-05) against paṭibhānappaṭisambhidāya (2-06 …);
   - ārammaṇaupanissayā (no sandhi) against ārammaṇūpanissayo.
10. **dassitanayena / passitvā**: the text renders passitvā as «ကြည့်၍» ("looking at"), where pi-4 has «မြင်၍».

## H. Unclear mappings (for the coordinator)

- **G2-3 gap or head noun**: X-mūlake could instead take the whole text phrase «X သဘောတရားကို အခြေခံခြင်း». The gap
  follows phase 1 §A 5. Phase 3 should settle this together with Abyākatamūlaṃ (g6).
- **gahite = «ယူသော»**: the locative absolute is «… ယူသောအခါ» in the text. «အခါ» ("when") is dropped as case
  material (rule 3). The alternative is «ယူသောအခါ».
- **dassitanayena = «ပြထားသော နည်းအတိုင်း»**: «အတိုင်း» is kept as the meaning of the instrumental. The alternative is
  «ပြထားသော နည်း» (rule 1, as Xpaccayena loses «ဖြင့်»).
- **ante = «အဆုံးတိုင်း»**: the keyword file lists the repeated «ante ante» once, and the text renders the repetition
  with «တိုင်း».
- **sekkha as a qualifier «…၏» against the person noun**: decided by the Pāli word that follows (dhamma / khandha /
  phala = qualifier). The module's T7 order should be reviewed book-wide in phase 3.
- **likhitā / samenti in «na …»** (G2-5): the positive dictionary form, because na is not a keyword. The alternative
  is the negative of Q5 («မရေးထားသော», «မညီ»).
