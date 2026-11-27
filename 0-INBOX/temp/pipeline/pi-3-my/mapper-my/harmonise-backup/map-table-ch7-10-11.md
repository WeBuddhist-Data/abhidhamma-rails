# pi-3 Burmese keyword mapping: rules and review table (Dhātukathā «ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း», chapters 7-chatthanayo, 10-navamanayo, 11-dasamanayo)

Written by map_ch7-10-11.py (a copy of the approved sample map_all.py, parallel agent). Burmese from the FINAL pi-3 text of this track only (AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters); pi-1 / pi-2 values from AI_translation/burmese/pi-1- and pi-2-keywords-by-reference-pali-burmese-plain.md. No other Burmese source.

## Verification

| chapter | lines | keyword preservation | presence failures | comma / ၊ / « / » | rule-matched chunks | (no direct equivalent) |
|---|---|---|---|---|---|---|
| 7-chatthanayo | 84 | bad [] | 0 | [] | 187 | 1 |
| 10-navamanayo | 36 | bad [] | 0 | [] | 5 | 1 |
| 11-dasamanayo | 58 | bad [] | 0 | [] | 15 | 1 |

## Reuse of pi-1 / pi-2

- Keyword uses: 2479; distinct keywords: 413.
- Keywords that pi-1 or pi-2 also has: 233 distinct; their values taken **unchanged from pi-1 / pi-2**: 227 distinct keyword-value pairs, 967 uses (a pi-2 value: 186 pairs, 903 uses; a pi-1 value only: 41 pairs, 64 uses).
- Keywords new in pi-3 (in neither mapping): 180 distinct.

### Values that differ from pi-1 / pi-2 for the same keyword

| keyword | pi-3 value (uses) | pi-2 value(s) | pi-1 value(s) | reason |
|---|---|---|---|---|
| antare | ကြားညှပ် (2) | အကြား (1) | - | the verse's cūḷantare / mahantare «ကြားညှပ်» (pi-1 antara heading word); pi-2 «အကြား» (between) is not in the segment |
| arūpa | ရုပ် မဟုတ်သော (1) | ရုပ်မရှိသော (15) | ရုပ်မရှိသော (109) | ^3-352 verse «Arūpakkhandhā» «ရုပ် မဟုတ်သော အစုအဝေး» (the non-material aggregates, pi-1 arūpino «ရုပ် မဟုတ်သော»); the plane keeps «ရုပ်မရှိသော» |
| aññāta | သိရသော (3) | - | သိသော (3) | pi-1 «သိသော» is not in the segment: the text renders anaññāta «မသိရသေးသည်ကို», positive part «သိရ» + «သော» (rule 8, M7) |
| bodhi | ဗောဇ္ဈင် (3) | ဗောဓိ (2) | - | pi-2 «ဗောဓိ» is not in the segment: the text renders bojjhaṅgā by the one word «ဗောဇ္ဈင်» (aṅgā = no direct equivalent) |
| dukkha | နာကျင် (2) | ဒုက္ခ (136) · ဆင်းရဲ (7) · ခက်ခဲသော (7) · နာကျင်သော (3) | ခက်ခဲသော (77) · နာကျင်သော (6) · နာကျင်မှု (5) · ဒုက္ခ (4) | fragment of adukkhamasukhāya: the positive part of the text's «မနာကျင်» (rule 8); one sense per segment |
| dukkhaṃ | ကိုယ်ဆင်းရဲခြင်း (1) | နာကျင်မှု (17) · ဒုက္ခ (15) · နာကျင်သော (1) | နာကျင်မှု (7) | the jāti list (soko … dukkhaṃ … upāyāso): the pi-3 text's word «ကိုယ်ဆင်းရဲခြင်း» (my3 terms, pi-2 ^2-206 rails); pi-2 «နာကျင်မှု / ဒုက္ခ» are not in the segment |
| nayo | ခွဲနည်း (3) | - | နည်း (4) | the pi-3 text's one word «ခွဲနည်း» (M8); pi-1 «နည်း» stands alone in its text |
| pare | နောက် (2) | သူတစ်ပါး (1) | - | «tato pare» «ထို့နောက်တွင်» = «နောက်» (after; 7-10-11 M4); pi-2 «သူတစ်ပါး» (others) is another sense, not in the segment |
| paññāsa | ငါးဆယ်ပါး (2) | ငါးဆယ် (1) | - | the verse count with the text's classifier «ငါးဆယ်ပါး» (pi-1 harmonise decision 5); pi-2 «ငါးဆယ်» is the bare number, not in this form in the segment |
| āyatanena | အာရုံခံ နယ်ပယ် (142) | (no direct equivalent) (9) | - | the counted noun «အာရုံခံ နယ်ပယ် N-ပါး» (ekenāyatanena); pi-2 (no direct equivalent) is a compound member inside one Burmese word |

## Rules

The value is the word or phrase of THAT segment's Burmese (the FINAL pi-3 text) that carries the keyword, in the
dictionary form of the approved mappings. **Binding and unchanged:** pi-1 rules 1–11 and the agreed later pi-1 rules,
pi-2 N1–N11 and its harmonise decisions, and the approved pi-3 sample (`map-table.md`, M1–M9, its 11 differences and
its values): this script is a copy of `map_all.py` with the same tables, compose rules, context functions and
presence check; the sample's values are taken for the same keyword in the same kind of segment (sampayutto /
vippayutto «ယှဉ်တွဲသော / ကင်းကွာသော» in every number and gender, the counts with «ပါး», the count biterms
«āyatanehi N» M1, «A / B» M2, «X dhammā» with a gap M4, ñassāmi «သိရတော့သည်», aññāta «သိရသော», bodhi «ဗောဇ္ဈင်» with
aṅgā (no direct equivalent), vokāra, rūpa / dukkha / sukha by the first compound). pi-2 and pi-1 values are reused
where they occur in the segment (pi-2 first).

Rules this run uses that pi-1 / pi-2 / the sample already had, applied to the shapes of the sixth, ninth and tenth
methods:

- **The association frame** «S katihi khandhehi … sampayutto? … X-hi … sampayutto; … kehici sampayutto»:
  sampayutto / -ā / -aṃ = ယှဉ်တွဲသော, vippayutto / -ā / -aṃ = ကင်းကွာသော (pi-1 / pi-2; text «…သည်», «…ကြသည်»,
  «…သနည်း»: rule 3, sample M7); Natthi = မရှိသည် (pi-1 / pi-2; text «မရှိ။», rule 4); the counts and counted nouns
  as in the sample (dasahāyatanehi = အာရုံခံ နယ်ပယ် ဆယ်ပါး, soḷasahi dhātūhi = ဓာတ် ဆယ့်ခြောက်ပါး, āyatanehi dasahi =
  အာရုံခံ နယ်ပယ် … ဆယ်ပါး).
- **Headings and colophons** (rule 7, decision 4): nayo = ခွဲနည်း (sample M8), the ordinals chaṭṭha / chaṭṭho = ဆဋ္ဌမ
  (pi-2), navama / Navamassa = နဝမ, dasama / dasamo = ဒသမ (the text's words); vippayoga = ကင်းကွာခြင်း (= the sample's
  vippayogo); sampayutta / vippayutta in «Sampayuttena sampayutta-» «ယှဉ်တွဲသည့်အရာဖြင့် ယှဉ်တွဲသည့်အရာ» = ယှဉ်တွဲသော /
  ကင်းကွာသော (pi-1 / pi-2, sample N11 «…သည့်အရာ»); niddeso / niddese = အကျယ် ဖော်ပြချက်; ādi = စသည်.
- **The summary verses** (identical in ch7 and ch11): the noun without its locative (rule 1): Gocchakesu / gocchake =
  အစု (pi-1 «N-တို့၏ အစု»), antare / antara = ကြားညှပ် (pi-1), duke = နှစ်မျိုးတွဲ (pi-2), niddese = အကျယ် ဖော်ပြချက်;
  the counts with the text's classifier «ပါး» (pi-1 harmonise decision 5): ekūnavīsati = ဆယ့်ကိုးပါး, paññāsa =
  ငါးဆယ်ပါး, pannarasa, aṭṭhārasa, cuddasa = ဆယ့်လေးပါး, tecattālīsaṃ = လေးဆယ့်သုံးပါး, Tevīsa (Tevīsa padasataṃ «ပုဒ်
  တစ်ရာ့နှစ်ဆယ့်သုံးပါး») = နှစ်ဆယ့်သုံးပါး with sataṃ = တစ်ရာ (pi-2); mahābhavā: bhavā = ဘဝ (the noun without «ကြီး»
  = mahā, as pi-1 harmonise decision 5 bhūtā «မူလဓာတ်» of mahābhūtā); «na labbhati» «မတွေ့ရ»: labbhati = တွေ့ရသည်
  (rule 8 positive part, rule 4 verb + သည်); «saṅgahaṃ gatā» «အကျုံးဝင်ကြသည်» = အကျုံးဝင်သော (rule 3, as the sample's
  saṅgahitā); jīvitaṃ = အသက်, nāmarūpaṃ, dukkhasaccaṃ (pi-2).
- **Sense by context, one sense per segment**: arūpa in Arūpabhavo / arūpāvacarā = ရုပ်မရှိသော (the plane, pi-1 /
  pi-2) but in the ch10 verse «Arūpakkhandhā cattāro» «ရုပ် မဟုတ်သော အစုအဝေး» = ရုပ် မဟုတ်သော (the non-material
  aggregates; pi-1 arūpino «ရုပ် မဟုတ်သော»; ^3-352, CTX); rūpa in Rūpabhavo / rūpāvacarā = သိမ်မွေ့သော ရုပ် (sample);
  dukkha in dukkhasaccaṃ (verse) = ဒုက္ခ, dukkhaṃ / dukkhena in the jāti list = ကိုယ်ဆင်းရဲခြင်း (sample).
- **Fragments** (rule 8): kāmāvacarehi in «Na kāmāvacarehi», pariyāpannehi in apariyāpannehi, uppannehi in
  anuppannehi, saṃsaṭṭhehi in cittavisaṃsaṭṭhehi, ārammaṇehi in anārammaṇehi = the positive part (pi-1 / pi-2 values
  of the nominative, M1 below).
- **Compound members inside one Burmese word** (pi-2 harmonise decision 4): aṅgā (ch7, bojjhaṅgā) and aṅgehi (ch10,
  ch11, bojjhaṅgehi «ဗောဇ္ဈင်») = (no direct equivalent), as the sample's aṅgā: the only (no direct equivalent), one
  per chapter. This is the same split as ch12-15 Q1 (inflected keywords) and ch3-6-8-9 M11.

## NEW rules (for the user's review)

7-10-11 M1. **Inflected keywords take the value of their nominative.** The ninth and tenth methods name every item
    in the instrumental («Vedanākkhandhena ye dhammā…», «Sukhasahagatehi dhammehi ye dhammā…», «Appamaññāya …»,
    «pañcahi indriyehi …»), and the text renders the item with its nominative's Burmese + «နှင့်». The dictionary
    form is the same in every case (rule 1: no case particle, no plural; rule 3 for adjectives), so the script tries
    the nominative of a keyword it has not found (-ena → -o / -aṃ, -ehi → -ā / -āni, -īhi → -ino, -ūhi → -ū / -uno,
    -āya → -ā, -uyā → -u) in the tables and then in the pi-2 / pi-1 mapping, keeping the value only if it occurs
    in the segment; «X dhammehi» first takes the pi-1 / pi-2 phrase of «X dhammā» where the text has it as a phrase
    (hetukehi dhammehi = အမြစ် ရှိသော သဘောတရား), otherwise it is composed as «X dhammā» (rule 5, sample M4:
    avitakka dhammehi = စတင်ကြံစည်မှု မရှိသော … သဘောတရား). Examples: Vedanākkhandhena = ခံစားမှု အစုအဝေး, indriyena =
    စွမ်းရည်, sahagatehi = အတူ ဖြစ်သော, sahagatehi dhammehi = အတူ ဖြစ်သော သဘောတရား, Hetūhi = အမြစ် (rule 2),
    anuparivattīhi = နောက်သို့ လိုက်ပါသော, sahabhūhi = အတူ တည်ရှိသော, rūpīhi = ရုပ် ဖြစ်သော. 231 keyword uses
    (labelled «-nom» in the --pairs listing); no new Burmese value comes from it.
7-10-11 M2. **The relative frame of the tenth method** «X-ena ye dhammā vippayuttā, tehi dhammehi ye dhammā
    vippayuttā» (text «Xနှင့် ကင်းကွာသော သဘောတရားများ၊ ထိုသဘောတရားတို့နှင့် ကင်းကွာသော သဘောတရားများ»):
    dhammā vippayuttā = «ကင်းကွာသော သဘောတရား» (the relative clause «ye dhammā vippayuttā», its first occurrence in
    every segment: the qualifier before the noun, as pi-1 dhammā saṅkhatā «ပြုပြင်ဖန်တီးထားသော သဘောတရား» and pi-2 N3;
    ch8's «dhammā vippayuttā» = «သဘောတရား … ကင်းကွာသော» (ch3-6-8-9 M12) is the subject + predicate frame, another kind
    of segment); dhammehi vippayuttā = «သဘောတရား … ကင်းကွာသော» (the gap holds «တို့နှင့်»; = ch12-15 Q2 for the same
    frame). One value in every segment (rule 10). ch10 has no such biterm keyword.
7-10-11 M3. **Item + verb biterms** «X-ena vippayuttā» (bhavena, viññāṇena, Adhimokkhena, Kusalehi vippayuttā),
    = ch12-15 Q2: «Xနှင့် ကင်းကွာသော» where the text has it contiguous (^3-364 «ဘဝနှင့် ကင်းကွာသော», ^3-368
    «ဆုံးဖြတ်မှုနှင့် ကင်းကွာသော»; the object keeps its «နှင့်», pi-1 rule 3), else «X … ကင်းကွာသော» (^3-362
    viññāṇena, ^3-365 bhavena: other items stand between; ^3-369 Kusalehi «ကုသိုလ် သဘောတရားများနှင့်…»; rule 10).
    Adhimokkhena = «ဆုံးဖြတ်မှု» (the noun of pi-2 adhimokkhapaccayā «ဆုံးဖြတ်မှုကြောင့်»; = ch12-15 Q6).
7-10-11 M4. **«tato pare» / «tato upari»** (verses, text «ထို့နောက်တွင်» / «ထို့အထက်တွင်»): pare = «နောက်», upari =
    «အထက်» («ထို့» is tato, not a keyword; the locative «တွင်» goes, rule 1; = ch4 upari «အထက်»). pi-2 pare
    «သူတစ်ပါး» (others) is another sense and not in the segment. For map-harmonise: ch13 has upari «အထက်တွင်».
7-10-11 M5. **kehici** (in «… ekāya dhātuyā kehici sampayutto», text «… တို့၏ အချို့နှင့်») = «အချို့» (some of):
    the noun, «၏ … နှင့်» are particles (rule 1). «na kehici» segments have no kehici keyword. **upādādhammehi** (one
    Pāli word, upādādhammehi ye dhammā) = «မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော သဘောတရား» (= pi-1 upādā dhammā, rule 5).

## Presence: chunks matched by an ending rule (not literally in the segment)

Every other chunk of every value occurs literally in its segment's Burmese.

| segment | keyword | chunk | rule |
|---|---|---|---|
| 3-228 | sampayutto | ယှဉ်တွဲသော | attr |
| 3-228 | vippayutto | ကင်းကွာသော | attr |
| 3-228 | Natthi | မရှိသည် | verb |
| 3-229 | sampayutto | ယှဉ်တွဲသော | attr |
| 3-229 | vippayutto | ကင်းကွာသော | attr |
| 3-230 | sampayutto | ယှဉ်တွဲသော | attr |
| 3-230 | vippayutto | ကင်းကွာသော | attr |
| 3-231 | sampayuttaṃ | ယှဉ်တွဲသော | attr |
| 3-231 | vippayuttaṃ | ကင်းကွာသော | attr |
| 3-231 | Natthi | မရှိသည် | verb |
| 3-232 | sampayuttaṃ | ယှဉ်တွဲသော | attr |
| 3-232 | vippayuttaṃ | ကင်းကွာသော | attr |
| 3-233 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-233 | vippayuttā | ကင်းကွာသော | attr |
| 3-233 | Natthi | မရှိသည် | verb |
| 3-234 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-234 | vippayuttā | ကင်းကွာသော | attr |
| 3-235 | sampayuttaṃ | ယှဉ်တွဲသော | attr |
| 3-235 | vippayuttaṃ | ကင်းကွာသော | attr |
| 3-236 | sampayuttaṃ | ယှဉ်တွဲသော | attr |
| 3-236 | vippayuttaṃ | ကင်းကွာသော | attr |
| 3-236 | Natthi | မရှိသည် | verb |
| 3-237 | sampayuttaṃ | ယှဉ်တွဲသော | attr |
| 3-237 | vippayuttaṃ | ကင်းကွာသော | attr |
| 3-238 | sampayuttaṃ | ယှဉ်တွဲသော | attr |
| 3-238 | vippayuttaṃ | ကင်းကွာသော | attr |
| 3-239 | sampayuttaṃ | ယှဉ်တွဲသော | attr |
| 3-239 | vippayuttaṃ | ကင်းကွာသော | attr |
| 3-240 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-240 | vippayuttā | ကင်းကွာသော | attr |
| 3-240 | ñassāmi | သိရတော့သည် | verb |
| 3-240 | aññāta | သိရသော | attr |
| 3-241 | sampayuttaṃ | ယှဉ်တွဲသော | attr |
| 3-241 | vippayuttaṃ | ကင်းကွာသော | attr |
| 3-242 | sampayutto | ယှဉ်တွဲသော | attr |
| 3-242 | vippayutto | ကင်းကွာသော | attr |
| 3-243 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-243 | vippayuttā | ကင်းကွာသော | attr |
| 3-244 | sampayutto | ယှဉ်တွဲသော | attr |
| 3-244 | vippayutto | ကင်းကွာသော | attr |
| 3-245 | sampayutto | ယှဉ်တွဲသော | attr |
| 3-245 | vippayutto | ကင်းကွာသော | attr |
| 3-245 | Natthi | မရှိသည် | verb |
| 3-246 | sampayutto | ယှဉ်တွဲသော | attr |
| 3-246 | vippayutto | ကင်းကွာသော | attr |
| 3-247 | sampayutto | ယှဉ်တွဲသော | attr |
| 3-247 | vippayutto | ကင်းကွာသော | attr |
| 3-247 | Natthi | မရှိသည် | verb |
| 3-248 | sampayuttaṃ | ယှဉ်တွဲသော | attr |
| 3-248 | vippayuttaṃ | ကင်းကွာသော | attr |
| 3-249 | sampayuttaṃ | ယှဉ်တွဲသော | attr |
| 3-249 | vippayuttaṃ | ကင်းကွာသော | attr |
| 3-250 | sampayutto | ယှဉ်တွဲသော | attr |
| 3-250 | vippayutto | ကင်းကွာသော | attr |
| 3-251 | sampayuttaṃ | ယှဉ်တွဲသော | attr |
| 3-251 | vippayuttaṃ | ကင်းကွာသော | attr |
| 3-252 | sampayutto | ယှဉ်တွဲသော | attr |
| 3-252 | vippayutto | ကင်းကွာသော | attr |
| 3-253 | sampayutto | ယှဉ်တွဲသော | attr |
| 3-253 | vippayutto | ကင်းကွာသော | attr |
| 3-254 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-254 | vippayuttā | ကင်းကွာသော | attr |
| 3-255 | sampayuttaṃ | ယှဉ်တွဲသော | attr |
| 3-255 | vippayuttaṃ | ကင်းကွာသော | attr |
| 3-256 | sampayutto | ယှဉ်တွဲသော | attr |
| 3-256 | vippayutto | ကင်းကွာသော | attr |
| 3-257 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-257 | vippayuttā | ကင်းကွာသော | attr |
| 3-257 | Natthi | မရှိသည် | verb |
| 3-258 | vippayuttā | ကင်းကွာသော | attr |
| 3-259 | vippayuttā | ကင်းကွာသော | attr |
| 3-260 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-260 | vippayuttā | ကင်းကွာသော | attr |
| 3-260 | Natthi | မရှိသည် | verb |
| 3-261 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-261 | saṃkiliṭṭha | ညစ်နွမ်းသော | attr |
| 3-261 | vippayuttā | ကင်းကွာသော | attr |
| 3-261 | Natthi | မရှိသည် | verb |
| 3-262 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-262 | vippayuttā | ကင်းကွာသော | attr |
| 3-262 | Natthi | မရှိသည် | verb |
| 3-263 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-263 | vippayuttā | ကင်းကွာသော | attr |
| 3-263 | Natthi | မရှိသည် | verb |
| 3-263 | upādinna | ဖြစ်သော | attr |
| 3-263 | asaṃkiliṭṭha | မညစ်နွမ်းသော | attr |
| 3-264 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-264 | vippayuttā | ကင်းကွာသော | attr |
| 3-265 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-265 | vippayuttā | ကင်းကွာသော | attr |
| 3-265 | avitakka dhammā | မရှိသော | attr |
| 3-266 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-266 | vippayuttā | ကင်းကွာသော | attr |
| 3-266 | Natthi | မရှိသည် | verb |
| 3-267 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-267 | vippayuttā | ကင်းကွာသော | attr |
| 3-268 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-268 | vippayuttā | ကင်းကွာသော | attr |
| 3-269 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-269 | vippayuttā | ကင်းကွာသော | attr |
| 3-269 | Natthi | မရှိသည် | verb |
| 3-270 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-270 | vippayuttā | ကင်းကွာသော | attr |
| 3-270 | Natthi | မရှိသည် | verb |
| 3-271 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-271 | vippayuttā | ကင်းကွာသော | attr |
| 3-271 | paritta | ရှိသော | attr |
| 3-271 | Natthi | မရှိသည် | verb |
| 3-272 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-272 | vippayuttā | ကင်းကွာသော | attr |
| 3-272 | mahaggata | ကြီးမြတ်သော | attr |
| 3-272 | appamāṇa | မရှိသော | attr |
| 3-273 | uppannā | ဖြစ်ပေါ်သော | attr |
| 3-273 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-273 | vippayuttā | ကင်းကွာသော | attr |
| 3-273 | Natthi | မရှိသည် | verb |
| 3-274 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-274 | vippayuttā | ကင်းကွာသော | attr |
| 3-274 | Natthi | မရှိသည် | verb |
| 3-275 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-275 | vippayuttā | ကင်းကွာသော | attr |
| 3-275 | Natthi | မရှိသည် | verb |
| 3-276 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-276 | vippayuttā | ကင်းကွာသော | attr |
| 3-276 | Natthi | မရှိသည် | verb |
| 3-277 | vippayuttā | ကင်းကွာသော | attr |
| 3-278 | vippayuttā | ကင်းကွာသော | attr |
| 3-278 | Natthi | မရှိသည် | verb |
| 3-279 | vippayuttā | ကင်းကွာသော | attr |
| 3-280 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-280 | vippayuttā | ကင်းကွာသော | attr |
| 3-280 | Natthi | မရှိသည် | verb |
| 3-281 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-281 | vippayuttā | ကင်းကွာသော | attr |
| 3-281 | Natthi | မရှိသည် | verb |
| 3-282 | vippayuttā | ကင်းကွာသော | attr |
| 3-283 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-283 | Natthi | မရှိသည် | verb |
| 3-284 | vippayuttā | ကင်းကွာသော | attr |
| 3-284 | Natthi | မရှိသည် | verb |
| 3-285 | vippayuttā | ကင်းကွာသော | attr |
| 3-286 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-286 | vippayuttā | ကင်းကွာသော | attr |
| 3-287 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-287 | Natthi | မရှိသည် | verb |
| 3-288 | vippayuttā | ကင်းကွာသော | attr |
| 3-289 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-289 | vippayuttā | ကင်းကွာသော | attr |
| 3-289 | Natthi | မရှိသည် | verb |
| 3-290 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-290 | Natthi | မရှိသည် | verb |
| 3-291 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-291 | vippayuttā | ကင်းကွာသော | attr |
| 3-292 | vippayuttā | ကင်းကွာသော | attr |
| 3-293 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-293 | vippayuttā | ကင်းကွာသော | attr |
| 3-293 | Natthi | မရှိသည် | verb |
| 3-294 | vippayuttā | ကင်းကွာသော | attr |
| 3-295 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-295 | Natthi | မရှိသည် | verb |
| 3-296 | vippayuttā | ကင်းကွာသော | attr |
| 3-296 | Natthi | မရှိသည် | verb |
| 3-297 | vippayuttā | ကင်းကွာသော | attr |
| 3-298 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-298 | vippayuttā | ကင်းကွာသော | attr |
| 3-298 | Natthi | မရှိသည် | verb |
| 3-299 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-299 | vippayuttā | ကင်းကွာသော | attr |
| 3-300 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-300 | vippayuttā | ကင်းကွာသော | attr |
| 3-300 | Natthi | မရှိသည် | verb |
| 3-301 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-301 | vippayuttā | ကင်းကွာသော | attr |
| 3-302 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-302 | vippayuttā | ကင်းကွာသော | attr |
| 3-303 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-303 | vippayuttā | ကင်းကွာသော | attr |
| 3-304 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-304 | pariyāpannā | အကျုံးဝင်သော | neg-infix |
| 3-304 | vippayuttā | ကင်းကွာသော | attr |
| 3-304 | Natthi | မရှိသည် | verb |
| 3-304 | kāmāvacarā | ဆိုင်သော | attr |
| 3-304 | avacarā | ဆိုင်သော | attr |
| 3-305 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-305 | vippayuttā | ကင်းကွာသော | attr |
| 3-305 | labbhati | တွေ့ရသည် | verb |
| 3-305 | Natthi | မရှိသည် | verb |
| 3-10-1-0 | sampayutta | ယှဉ်တွဲသော | attr |
| 3-325 | ñassāmi | သိရတော့သည် | verb |
| 3-325 | aññāta | သိရသော | attr |
| 3-340 | avitakka dhammehi | မရှိသော | attr |
| 3-352 | saṅgahaṃ gatā | အကျုံးဝင်သော | attr |
| 3-11-1-0 | vippayutta | ကင်းကွာသော | attr |
| 3-361 | ñassāmi | သိရတော့သည် | verb |
| 3-361 | aññāta | သိရသော | attr |
| 3-373 | saṃkiliṭṭha | ညစ်နွမ်းသော | attr |
| 3-375 | upādinna | ဖြစ်သော | attr |
| 3-375 | asaṃkiliṭṭha | မညစ်နွမ်းသော | attr |
| 3-377 | avitakka dhammehi | မရှိသော | attr |
| 3-383 | paritta | ရှိသော | attr |
| 3-384 | mahaggata | ကြီးမြတ်သော | attr |
| 3-384 | appamāṇa | မရှိသော | attr |
| 3-385 | uppannehi | ဖြစ်ပေါ်သော | attr |
| 3-407 | pariyāpannehi | အကျုံးဝင်သော | neg-infix |
| 3-407 | kāmāvacarehi | ဆိုင်သော | attr |
| 3-407 | avacarehi | ဆိုင်သော | attr |
| 3-408 | labbhati | တွေ့ရသည် | verb |

## Keyword → Burmese (uses)

«pi-2» / «pi-1» = the value is a pi-2 / pi-1 value of the same keyword. Several values = the keyword reads differently by context.

| Pāli keyword | Burmese (uses) |
|---|---|
| Adhimokkhena vippayuttā | ဆုံးဖြတ်မှုနှင့် ကင်းကွာသော (1) |
| adhipatino | အကြီးအမှူး (1, pi-1) |
| adhipatīhi | အကြီးအမှူး (1) |
| akusalehi | အကုသိုလ် (1, pi-2) |
| akusalehi dhammehi | အကုသိုလ် သဘောတရား (1, pi-2) |
| akusalā | အကုသိုလ် (1, pi-2) |
| akusalā dhammā | အကုသိုလ် သဘောတရား (1, pi-2) |
| anidassana | မမြင်နိုင်သော (2, pi-2) |
| antara | ကြားညှပ် (1, pi-1) |
| antare | ကြားညှပ် (2) |
| anuparivattino | နောက်သို့ လိုက်ပါသော (1, pi-1) |
| anuparivattīhi | နောက်သို့ လိုက်ပါသော (2) |
| anuttarehi | ထိုထက် သာလွန်သည် မရှိသော (1) |
| anuttarehi dhammehi | ထိုထက် သာလွန်သည် မရှိသော သဘောတရား (1) |
| anuttarā | ထိုထက် သာလွန်သည် မရှိသော (1, pi-2) |
| anuttarā dhammā | ထိုထက် သာလွန်သည် မရှိသော သဘောတရား (1, pi-1) |
| Anāsavehi | စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော (1) |
| Anāsavehi dhammehi | စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော သဘောတရား (1) |
| Anāsavā | စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော (1, pi-2) |
| Anāsavā dhammā | စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော သဘောတရား (1, pi-1) |
| apacaya | လျော့ပါးခြင်း (2, pi-2) |
| Appamaññā | အပ္ပမညာ (1, pi-2) |
| Appamaññāya | အပ္ပမညာ (1) |
| appamaññāya | အပ္ပမညာ (1) |
| appamāṇa | အတိုင်းအဆ မရှိသော (2, pi-1) |
| Appamāṇehi | အတိုင်းအဆ မရှိသော (1) |
| Appamāṇehi dhammehi | အတိုင်းအဆ မရှိသော သဘောတရား (1) |
| Appamāṇā | အတိုင်းအဆ မရှိသော (1, pi-2) |
| Appamāṇā dhammā | အတိုင်းအဆ မရှိသော သဘောတရား (1, pi-1) |
| ariyena | အရိယာ (2) |
| ariyo | အရိယာ (1, pi-2) |
| arūpa | ရုပ်မရှိသော (4, pi-2) · ရုပ် မဟုတ်သော (1) |
| asaṃkiliṭṭha | ကိလေသာဖြင့် မညစ်နွမ်းသော (2, pi-2) |
| asaṅkhatehi | ပြုပြင်ဖန်တီးထားခြင်း မရှိသော (1) |
| asaṅkhatehi dhammehi | ပြုပြင်ဖန်တီးထားခြင်း မရှိသော သဘောတရား (1) |
| asaṅkhatā | ပြုပြင်ဖန်တီးထားခြင်း မရှိသော (1, pi-2) |
| asaṅkhatā dhammā | ပြုပြင်ဖန်တီးထားခြင်း မရှိသော သဘောတရား (1, pi-1) |
| asekkhehi | ကျင့်ကြံမှု ပြီးဆုံးသူ၏ (1) |
| asekkhā | ကျင့်ကြံမှု ပြီးဆုံးသူ၏ (1, pi-2) |
| avacarehi | ဘုံနှင့် ဆိုင်သော (2) |
| avacarā | ဘုံနှင့် ဆိုင်သော (2, pi-1) |
| avijjā | အမှန်ကို မသိမှု (1, pi-2) |
| avijjāya | အမှန်ကို မသိမှု (2, pi-1) |
| avitakka dhammehi | စတင်ကြံစည်မှု မရှိသော … သဘောတရား (3) |
| avitakka dhammā | စတင်ကြံစည်မှု မရှိသော … သဘောတရား (2) |
| Avitakkehi dhammehi | စတင်ကြံစည်မှု မရှိသော သဘောတရား (1) |
| Avitakkā dhammā | စတင်ကြံစည်မှု မရှိသော သဘောတရား (1, pi-1) |
| aññā / aññātāvī | အပြည့်အဝ သိမြင်ခြင်း … အပြည့်အဝ သိမြင်ပြီးသူ (3) |
| aññāta | သိရသော (3) |
| aṅgehi | (no direct equivalent) (2) |
| aṅgā | (no direct equivalent) (1, pi-2) |
| aṭṭhaṅgikena | အင်္ဂါ ရှစ်ပါး ရှိသော (2) |
| aṭṭhaṅgiko | အင်္ဂါ ရှစ်ပါး ရှိသော (1, pi-2) |
| aṭṭhārasa | ဆယ့်ရှစ်ပါး (2, pi-2) |
| bahiddhā | မိမိ၏ ပြင်ပ၌ (2, pi-2) |
| balehi | စွမ်းအား (2) |
| balāni | စွမ်းအား (1, pi-2) |
| bhavena | ဘဝ (5) |
| bhavena vippayuttā | ဘဝ … ကင်းကွာသော (2) · ဘဝနှင့် ကင်းကွာသော (1) |
| bhavo | ဘဝ (4, pi-2) |
| bhavā | ဘဝ (2) |
| bhāvanāya pahātabbehi | ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် (2) |
| bhāvanāya pahātabbā | ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် (2, pi-1) |
| bodhi | ဗောဇ္ဈင် (3) |
| cakkhu | မျက်စိ (5, pi-2) |
| Cakkhudhātu | မျက်စိ ဓာတ် (1, pi-2) |
| cakkhudhātuyā | မျက်စိ ဓာတ် (1) |
| cakkhundriyaṃ | မျက်စိ၏ စွမ်းရည် (1, pi-2) |
| cakkhundriyena | မျက်စိ၏ စွမ်းရည် (1) |
| cakkhuviññāṇa | မျက်စိ သိစိတ် (3, pi-2) |
| Cakkhuviññāṇadhātu | မျက်စိ သိစိတ် ဓာတ် (1, pi-2) |
| Cakkhuviññāṇadhātuyā | မျက်စိ သိစိတ် ဓာတ် (1) |
| cakkhuviññāṇadhātuyā | မျက်စိ သိစိတ် ဓာတ် (1) |
| Cakkhāyatanaṃ | မျက်စိ အာရုံခံ နယ်ပယ် (1, pi-2) |
| Cakkhāyatanena | မျက်စိ အာရုံခံ နယ်ပယ် (1) |
| cetanā | စေ့ဆော်မှု (1, pi-2) |
| cetanāya | စေ့ဆော်မှု (2, pi-2) |
| Cetasikehi | စိတ်၏ အဖော် (1) |
| cetasikehi | စိတ်၏ အဖော် (1) |
| Cetasikā | စိတ်၏ အဖော် (1, pi-2) |
| chaṭṭha | ဆဋ္ဌမ (1) |
| chaṭṭho | ဆဋ္ဌမ (1, pi-2) |
| citta | စိတ် (4, pi-2) |
| cittasaṃsaṭṭhasamuṭṭhānānuparivattino | စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နောက်သို့ လိုက်ပါသော (1, pi-1) |
| cittasaṃsaṭṭhasamuṭṭhānānuparivattīhi | စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နောက်သို့ လိုက်ပါသော (2) |
| Cittaṃ | စိတ် (1, pi-2) |
| Cittehi | စိတ် (1) |
| cittehi | စိတ် (1) |
| Cittena | စိတ် (1, pi-2) |
| cittena | စိတ် (1, pi-2) |
| Cittā | စိတ် (1, pi-2) |
| cuddasa | ဆယ့်လေးပါး (1) |
| dasa | ဆယ်ပါး (93, pi-2) |
| dasahi dhātūhi | ဓာတ် ဆယ်ပါး (24) |
| dasahāyatanehi | အာရုံခံ နယ်ပယ် ဆယ်ပါး (93) |
| dasama | ဒသမ (1) |
| dasamo | ဒသမ (1) |
| Dassanena | သစ္စာကို မြင်ခြင်း (4, pi-2) |
| dhamma | သဘောတရား (2, pi-2) |
| dhammehi vippayuttā | သဘောတရား … ကင်းကွာသော (38) |
| dhammā vippayuttā | ကင်းကွာသော သဘောတရား (56) |
| Dhātu | ဓာတ် (1, pi-2) |
| dhātu | ဓာတ် (2, pi-2) |
| dhātuyā | ဓာတ် (143, pi-2) |
| dhātūhi | ဓာတ် (139) |
| domanassa | စိတ်ဆင်းရဲမှု (3, pi-2) |
| domanassaṃ | စိတ်ဆင်းရဲမှု (1, pi-2) |
| domanassena | စိတ်ဆင်းရဲမှု (2) |
| duke | နှစ်မျိုးတွဲ (1) |
| dukkha | နာကျင်မှု (3, pi-2) · နာကျင် (2) · ဒုက္ခ (2, pi-2) |
| dukkhasaccaṃ | ဒုက္ခ သစ္စာ (2, pi-2) |
| dukkhaṃ | ကိုယ်ဆင်းရဲခြင်း (1) |
| dukkhena | ကိုယ်ဆင်းရဲခြင်း (2) |
| dukkhāya | နာကျင်သော (3, pi-2) |
| dvādasa | ဆယ့်နှစ်ပါး (1, pi-2) |
| ekādasahi | ဆယ့်တစ်ပါး (8) |
| ekādasahi dhātūhi | ဓာတ် ဆယ့်တစ်ပါး (8) |
| ekūnavīsati | ဆယ့်ကိုးပါး (2) |
| ganthehi | အထုံး (2) |
| ganthā | အထုံး (1, pi-2) |
| gocchake | အစု (1) |
| Gocchakesu | အစု (2) |
| gāmino dhammā | ဦးတည်သော သဘောတရား (1, pi-1) |
| gāmīhi dhammehi | ဦးတည်သော သဘောတရား (1) |
| hetukehi | အမြစ် (4) |
| hetukehi dhammehi | အမြစ် ရှိသော သဘောတရား (2) |
| hetukā | အမြစ် (5, pi-2) |
| hetukā dhammā | အမြစ် ရှိသော သဘောတရား (2, pi-1) |
| Hetū | အမြစ် (1, pi-2) |
| Hetūhi | အမြစ် (2) |
| hīnehi | ယုတ်ညံ့သော (1) |
| hīnehi dhammehi | ယုတ်ညံ့သော သဘောတရား (1) |
| hīnā | ယုတ်ညံ့သော (1, pi-2) |
| hīnā dhammā | ယုတ်ညံ့သော သဘောတရား (1, pi-1) |
| iddhi | ဣဒ္ဓိ (3, pi-2) |
| indriyaṃ | စွမ်းရည် (5, pi-2) |
| indriyehi | စွမ်းရည် (2) |
| indriyena | စွမ်းရည် (9) |
| indriyā | စွမ်းရည် (1, pi-2) |
| indriyāni | စွမ်းရည် (1, pi-2) |
| itthi | မိန်းမ (2, pi-2) |
| jarā | အိုခြင်း (2, pi-2) |
| Jhānaṃ | ဈာန် (1, pi-2) |
| Jhānena | ဈာန် (1) |
| jhānena | ဈာန် (1) |
| Jāti | မွေးဖွားခြင်း (2, pi-2) |
| jīvitaṃ | အသက် (2, pi-2) |
| kehici | အချို့ (141) |
| khandhehi | အစုအဝေး (97) |
| khandhena | အစုအဝေး (116) |
| Khandho | အစုအဝေး (1, pi-2) |
| khandho | အစုအဝေး (3, pi-2) |
| kilesa | ကိလေသာ (3, pi-2) |
| kilesehi | ကိလေသာ (3) |
| kilesā | ကိလေသာ (2, pi-2) |
| Kusalehi | ကုသိုလ် (1) |
| Kusalehi dhammehi | ကုသိုလ် သဘောတရား (1) |
| Kusalehi vippayuttā | ကုသိုလ် … ကင်းကွာသော (1) |
| Kusalā | ကုသိုလ် (1, pi-2) |
| Kusalā dhammā | ကုသိုလ် သဘောတရား (1, pi-2) |
| kāma / āyatanehi | ကာမ … အာရုံခံ နယ်ပယ် (2) |
| kāmāvacarehi | ကာမဘုံနှင့် ဆိုင်သော (1) |
| kāmāvacarā | ကာမဘုံနှင့် ဆိုင်သော (1, pi-2) |
| kāya | ကိုယ် (2, pi-2) |
| labbhati | တွေ့ရသည် (2) |
| Lokuttarehi | လောကကို ကျော်လွန်သော (1) |
| Lokuttarā | လောကကို ကျော်လွန်သော (1, pi-2) |
| magga | မဂ် (5, pi-2) |
| maggena | မဂ် (2) |
| maggo | မဂ် (1, pi-2) |
| mahaggata | ကြီးမြတ်သော (2, pi-1) |
| mahaggatehi | ကြီးမြတ်သော (1) |
| mahaggatehi dhammehi | ကြီးမြတ်သော သဘောတရား (1) |
| mahaggatā | ကြီးမြတ်သော (1, pi-2) |
| mahaggatā dhammā | ကြီးမြတ်သော သဘောတရား (1, pi-1) |
| mana | မနော (7, pi-1) |
| manasikārena | နှလုံးသွင်းခြင်း (2) |
| manasikāro | နှလုံးသွင်းခြင်း (1, pi-2) |
| mano | မနော (1, pi-2) |
| manodhātu | မနော ဓာတ် (1, pi-2) |
| manodhātuyā | မနော ဓာတ် (1, pi-2) |
| manoviññāṇa | မနော သိစိတ် (3, pi-2) |
| manoviññāṇadhātu | မနော သိစိတ် ဓာတ် (1, pi-2) |
| manoviññāṇadhātuyā | မနော သိစိတ် ဓာတ် (2) |
| Manāyatanaṃ | မနော အာရုံခံ နယ်ပယ် (1, pi-2) |
| manāyatanaṃ | မနော အာရုံခံ နယ်ပယ် (1, pi-2) |
| manāyatanena | မနော အာရုံခံ နယ်ပယ် (2) |
| maraṇaṃ | သေခြင်း (2, pi-2) |
| micchatta | မှားယွင်းမှု (2, pi-2) |
| Natthi | မရှိသည် (36, pi-2) |
| navama | နဝမ (1) |
| Navamassa | နဝမ (1) |
| nayo | ခွဲနည်း (3) |
| niddese | အကျယ် ဖော်ပြချက် (1) |
| niddeso | အကျယ် ဖော်ပြချက် (5, pi-2) |
| nirodha | ချုပ်ငြိမ်းခြင်း (2, pi-2) |
| niyatehi | ကျိန်းသေသော (2) |
| niyatehi dhammehi | ကျိန်းသေသော သဘောတရား (2) |
| niyatā | ကျိန်းသေသော (2, pi-2) |
| niyatā dhammā | ကျိန်းသေသော သဘောတရား (2, pi-1) |
| niyyānikehi dhammehi | လွတ်မြောက်ရာသို့ ပို့ဆောင်သော သဘောတရား (1) |
| niyyānikā dhammā | လွတ်မြောက်ရာသို့ ပို့ဆောင်သော သဘောတရား (1, pi-1) |
| nāmarūpaṃ | စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း (2, pi-2) |
| nāsaññā | မှတ်သိမှု မရှိသည် မဟုတ်သော (2, pi-1) |
| nīvaraṇehi | အတားအဆီး (2, pi-2) |
| nīvaraṇā | အတားအဆီး (1, pi-2) |
| oghehi | ရေအလျဉ် (2) |
| oghā | ရေအလျဉ် (1, pi-2) |
| paccayā | ကြောင့် (13, pi-2) |
| padhānaṃ | ကြိုးပမ်းအားထုတ်ခြင်း (1, pi-2) |
| padhānena | ကြိုးပမ်းအားထုတ်ခြင်း (2) |
| pahātabbehi | ပယ်ရမည့် (2) |
| pahātabbā | ပယ်ရမည့် (2, pi-2) |
| pannarasa | ဆယ့်ငါးပါး (2, pi-2) |
| pannarasahi | ဆယ့်ငါးပါး (12) |
| pannarasahi dhātūhi | ဓာတ် ဆယ့်ငါးပါး (12) |
| pare | နောက် (2) |
| paridevena | ငိုကြွေးခြင်း (1) |
| paridevo | ငိုကြွေးခြင်း (1, pi-2) |
| paritta | အကန့်အသတ် ရှိသော (2, pi-2) |
| pariyāpannehi | ဘဝဘုံတို့၌ အကျုံးဝင်သော (1) |
| pariyāpannā | ဘဝဘုံတို့၌ အကျုံးဝင်သော (1) |
| parāmaṭṭhehi | မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်သော (3) |
| parāmaṭṭhā | မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်သော (2, pi-2) |
| parāmāsa | မှားယွင်းသော ယူဆမှု (5, pi-2) |
| parāmāsehi | မှားယွင်းသော ယူဆမှု (2) |
| parāmāsā | မှားယွင်းသော ယူဆမှု (1, pi-2) |
| paññā | ပညာ (3, pi-2) |
| paññāsa | ငါးဆယ်ပါး (2) |
| paṇītehi | မွန်မြတ်သော (1) |
| paṇītehi dhammehi | မွန်မြတ်သော သဘောတရား (1) |
| paṇītā | မွန်မြတ်သော (1, pi-2) |
| paṇītā dhammā | မွန်မြတ်သော သဘောတရား (1, pi-1) |
| phassa | တွေ့ထိမှု (2, pi-2) |
| Phassena | တွေ့ထိမှု (2) |
| phassena | တွေ့ထိမှု (2) |
| Phasso | တွေ့ထိမှု (1, pi-2) |
| phasso | တွေ့ထိမှု (1, pi-2) |
| phoṭṭhabba | အထိအတွေ့ (3, pi-2) |
| phoṭṭhabbadhātu | အထိအတွေ့ ဓာတ် (1, pi-2) |
| phoṭṭhabbadhātuyā | အထိအတွေ့ ဓာတ် (1) |
| phoṭṭhabbāyatanaṃ | အထိအတွေ့ အာရုံခံ နယ်ပယ် (1, pi-2) |
| phoṭṭhabbāyatanena | အထိအတွေ့ အာရုံခံ နယ်ပယ် (1) |
| purisa | ယောက်ျား (2, pi-2) |
| pīti | ပီတိ (3, pi-2) |
| pītikehi | ပီတိ (2) |
| pītikā | ပီတိ (1, pi-1) |
| raṇehi | ပဋိပက္ခ (1) |
| raṇā | ပဋိပက္ခ (1, pi-1) |
| rūpa | သိမ်မွေ့သော ရုပ် (4, pi-2) · ရုပ် (2, pi-2) |
| Rūpakkhandhena | ရုပ် အစုအဝေး (1) |
| Rūpakkhandho | ရုပ် အစုအဝေး (1, pi-2) |
| rūpino | ရုပ် ဖြစ်သော (1, pi-1) |
| rūpino dhammā | ရုပ် ဖြစ်သော သဘောတရား (1, pi-1) |
| rūpīhi | ရုပ် ဖြစ်သော (1) |
| rūpīhi dhammehi | ရုပ် ဖြစ်သော သဘောတရား (1) |
| sacca | သစ္စာ (1, pi-2) |
| saccaṃ | သစ္စာ (4, pi-2) |
| saccena | သစ္စာ (3) |
| saccā | သစ္စာ (1, pi-2) |
| saddhā | ယုံကြည်မှု (3, pi-2) |
| sahabhuno | အတူ တည်ရှိသော (1, pi-2) |
| sahabhūhi | အတူ တည်ရှိသော (2) |
| sahagatehi | အတူ ဖြစ်သော (10) |
| sahagatehi dhammehi | အတူ ဖြစ်သော သဘောတရား (10) |
| sahagatā | အတူ ဖြစ်သော (6, pi-2) |
| sahagatā dhammā | အတူ ဖြစ်သော သဘောတရား (6, pi-1) |
| sahetukehi | အမြစ် ရှိသော (1) |
| sammatta | မှန်ကန်မှု (2, pi-2) |
| sammā | မှန်ကန်သော (3, pi-2) |
| sampayutta | ယှဉ်တွဲသော (1, pi-1) |
| sampayuttaṃ | ယှဉ်တွဲသော (12, pi-2) |
| sampayuttehi | ယှဉ်တွဲသော (7) |
| sampayutto | ယှဉ်တွဲသော (12, pi-2) |
| sampayuttā | ယှဉ်တွဲသော (88, pi-2) |
| samudaya | ဖြစ်ပေါ်ခြင်း (3, pi-2) |
| samuṭṭhānehi | ဖြစ်ပေါ်လာသော (2) |
| samuṭṭhānā | ဖြစ်ပေါ်လာသော (1, pi-2) |
| samādhi | သမာဓိ (3, pi-2) |
| sanidassana | မြင်နိုင်သော (2, pi-2) |
| sanidassanehi | မြင်နိုင်သော (1) |
| sanidassanehi dhammehi | မြင်နိုင်သော သဘောတရား (1) |
| sanidassanā | မြင်နိုင်သော (1, pi-2) |
| sanidassanā dhammā | မြင်နိုင်သော သဘောတရား (1, pi-1) |
| Sappītikehi dhammehi | ပီတိ ရှိသော သဘောတရား (1) |
| sappītikehi dhammehi | ပီတိ ရှိသော သဘောတရား (1) |
| Sappītikā dhammā | ပီတိ ရှိသော သဘောတရား (1, pi-1) |
| saraṇehi dhammehi | ပဋိပက္ခ ရှိသော သဘောတရား (1) |
| saraṇā dhammā | ပဋိပက္ခ ရှိသော သဘောတရား (1, pi-1) |
| sataṃ | တစ်ရာ (2, pi-2) |
| sati | သတိ (6, pi-2) |
| savicārehi dhammehi | ဆက်လက်သုံးသပ်မှု ရှိသော သဘောတရား (2) |
| savicārā dhammā | ဆက်လက်သုံးသပ်မှု ရှိသော သဘောတရား (1, pi-1) |
| savitakka dhammehi | စတင်ကြံစည်မှု ရှိသော … သဘောတရား (2) |
| savitakka dhammā | စတင်ကြံစည်မှု ရှိသော … သဘောတရား (1) |
| Savitakkehi dhammehi | စတင်ကြံစည်မှု ရှိသော သဘောတရား (1) |
| savitakkehi dhammehi | စတင်ကြံစည်မှု ရှိသော သဘောတရား (1) |
| Savitakkā dhammā | စတင်ကြံစည်မှု ရှိသော သဘောတရား (1, pi-1) |
| saññā | မှတ်သိမှု (8, pi-2) |
| saññākkhandhena | မှတ်သိမှု အစုအဝေး (2) |
| saññākkhandho | မှတ်သိမှု အစုအဝေး (1, pi-2) |
| saññāya | မှတ်သိမှု (2, pi-1) |
| saṃkilesikehi | ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော (5) |
| saṃkilesikā | ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော (4, pi-2) |
| saṃkiliṭṭha | ကိလေသာဖြင့် ညစ်နွမ်းသော (2, pi-2) |
| Saṃkiliṭṭhehi | ကိလေသာဖြင့် ညစ်နွမ်းသော (1) |
| saṃkiliṭṭhehi | ကိလေသာဖြင့် ညစ်နွမ်းသော (2) |
| saṃkiliṭṭhehi dhammehi | ကိလေသာဖြင့် ညစ်နွမ်းသော သဘောတရား (1) |
| Saṃkiliṭṭhā | ကိလေသာဖြင့် ညစ်နွမ်းသော (2, pi-2) |
| saṃkiliṭṭhā | ကိလေသာဖြင့် ညစ်နွမ်းသော (1, pi-2) |
| Saṃkiliṭṭhā dhammā | ကိလေသာဖြင့် ညစ်နွမ်းသော သဘောတရား (1, pi-1) |
| saṃsaṭṭhehi | ရောနှောသော (3) |
| saṃsaṭṭhehi dhammehi | ရောနှောသော သဘောတရား (2) |
| saṃsaṭṭhā | ရောနှောသော (2, pi-2) |
| saṃsaṭṭhā dhammā | ရောနှောသော သဘောတရား (1, pi-1) |
| Saṃyojanehi | နှောင်ကြိုး (2) |
| Saṃyojanā | နှောင်ကြိုး (1, pi-2) |
| saṅgahaṃ gatā | အကျုံးဝင်သော (1) |
| saṅkhāra | ပြုပြင်ဖန်တီးမှု (6, pi-2) |
| saṅkhārakkhandhena | ပြုပြင်ဖန်တီးမှု အစုအဝေး (2) |
| saṅkhārakkhandho | ပြုပြင်ဖန်တီးမှု အစုအဝေး (1, pi-2) |
| saṅkhārehi | ပြုပြင်ဖန်တီးမှု (2) |
| saṅkhārā | ပြုပြင်ဖန်တီးမှု (1, pi-2) |
| sekkhehi | ကျင့်ကြံဆဲသူ၏ (1) |
| sekkhā | ကျင့်ကြံဆဲသူ၏ (1, pi-2) |
| Sokena | စိုးရိမ်ခြင်း (1) |
| sokena | စိုးရိမ်ခြင်း (1) |
| Soko | စိုးရိမ်ခြင်း (1, pi-2) |
| somanassa | ဝမ်းမြောက်မှု (3, pi-2) |
| soḷasa | ဆယ့်ခြောက်ပါး (1, pi-2) |
| soḷasahi | ဆယ့်ခြောက်ပါး (49) |
| soḷasahi dhātūhi | ဓာတ် ဆယ့်ခြောက်ပါး (49) |
| sukha | သာယာမှု (9, pi-2) |
| Sukhāya | သာယာသော (3, pi-2) |
| sukhāya | သာယာသော (2, pi-2) |
| taṇhā | တပ်မက်မှု (1, pi-2) |
| taṇhāya | တပ်မက်မှု (2, pi-2) |
| tecattālīsaṃ | လေးဆယ့်သုံးပါး (1) |
| Tevīsa | နှစ်ဆယ့်သုံးပါး (2) |
| upari | အထက် (1) |
| upaṭṭhānaṃ | ပဋ္ဌာန် (1) |
| upaṭṭhānena | ပဋ္ဌာန် (2) |
| upekkhā | ဥပေက္ခာ (9, pi-2) |
| uppannehi | ဖြစ်ပေါ်သော (1) |
| uppannā | ဖြစ်ပေါ်သော (1, pi-1) |
| upādinna | ကံကြောင့် ဖြစ်သော (4, pi-2) |
| upādinnehi | ကံကြောင့် ဖြစ်သော (1) |
| upādinnā | ကံကြောင့် ဖြစ်သော (1, pi-2) |
| upādā | မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော (2, pi-2) |
| upādā dhammā | မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော သဘောတရား (1, pi-1) |
| upādādhammehi | မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော သဘောတရား (1) |
| upādānaṃ | စွဲလမ်းမှု (1, pi-2) |
| Upādānehi | စွဲလမ်းမှု (2) |
| upādānena | စွဲလမ်းမှု (2) |
| upādāniyehi | စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော (2) |
| upādāniyā | စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော (2, pi-2) |
| Upādānā | စွဲလမ်းမှု (1, pi-2) |
| Upāyāsena | ပြင်းစွာ ပူပန်ခြင်း (1) |
| upāyāsena | ပြင်းစွာ ပူပန်ခြင်း (1) |
| Upāyāso | ပြင်းစွာ ပူပန်ခြင်း (1, pi-2) |
| Vedanā | ခံစားမှု (1, pi-2) |
| vedanā | ခံစားမှု (7, pi-2) |
| Vedanākkhandhena | ခံစားမှု အစုအဝေး (2) |
| Vedanākkhandho | ခံစားမှု အစုအဝေး (1, pi-2) |
| Vedanāya | ခံစားမှု (1, pi-2) |
| vedanāya | ခံစားမှု (8, pi-2) |
| vicāra | ဆက်လက်သုံးသပ်မှု (2, pi-2) |
| vicārehi | ဆက်လက်သုံးသပ်မှု (6) |
| vicārā | ဆက်လက်သုံးသပ်မှု (4, pi-2) |
| vippayoga | ကင်းကွာခြင်း (2) |
| vippayutta | ကင်းကွာသော (1, pi-2) |
| vippayuttaṃ | ကင်းကွာသော (12, pi-2) |
| vippayutto | ကင်းကွာသော (12, pi-2) |
| vippayuttā | ကင်းကွာသော (110, pi-2) |
| vippayuttā dhammā | ကင်းကွာသော သဘောတရား (4, pi-1) |
| visaṃsaṭṭhehi dhammehi | မရောနှောသော သဘောတရား (1) |
| visaṃsaṭṭhā dhammā | မရောနှောသော သဘောတရား (1, pi-1) |
| vitakka | စတင်ကြံစည်မှု (7, pi-2) |
| vitakka / vicāra | စတင်ကြံစည်မှု … ဆက်လက်သုံးသပ်မှု (2) |
| vitakka / vicārehi | စတင်ကြံစည်မှု … ဆက်လက်သုံးသပ်မှု (3) |
| vitakka / vicārā | စတင်ကြံစည်မှု … ဆက်လက်သုံးသပ်မှု (2) |
| vitakkehi | စတင်ကြံစည်မှု (3) |
| vitakkehi / vicārehi | စတင်ကြံစည်မှု … ဆက်လက်သုံးသပ်မှု (3) |
| vitakkā | စတင်ကြံစည်မှု (2, pi-2) |
| vitakkā / vicārā | စတင်ကြံစည်မှု … ဆက်လက်သုံးသပ်မှု (2) |
| viññāṇa | သိစိတ် (4, pi-2) |
| Viññāṇakkhandhena | သိစိတ် အစုအဝေး (1) |
| viññāṇakkhandhena | သိစိတ် အစုအဝေး (1) |
| Viññāṇakkhandho | သိစိတ် အစုအဝေး (1, pi-2) |
| viññāṇaṃ | သိစိတ် (1, pi-2) |
| viññāṇena | သိစိတ် (2) |
| viññāṇena vippayuttā | သိစိတ် … ကင်းကွာသော (1) |
| vokāra | အစုအဝေး (4) |
| yogehi | ထမ်းပိုး (2) |
| yogā | ထမ်းပိုး (1, pi-2) |
| ñassāmi | သိရတော့သည် (3) |
| ācaya | စုပုံခြင်း (2, pi-2) |
| ādi | စသည် (1, pi-2) |
| ārammaṇehi | အာရုံ (6) |
| ārammaṇā | အာရုံ (6, pi-2) |
| āsava | စိတ်အစွန်းအထင်း (3, pi-2) |
| Āsavehi | စိတ်အစွန်းအထင်း (2) |
| āsavehi | စိတ်အစွန်းအထင်း (1) |
| Āsavā | စိတ်အစွန်းအထင်း (1, pi-2) |
| āsavā | စိတ်အစွန်းအထင်း (1, pi-2) |
| āyatana | အာရုံခံ နယ်ပယ် (3, pi-2) |
| Āyatanaṃ | အာရုံခံ နယ်ပယ် (1, pi-2) |
| āyatanehi | အာရုံခံ နယ်ပယ် (121) |
| āyatanehi dasahi | အာရုံခံ နယ်ပယ် … ဆယ်ပါး (24) |
| āyatanehi ekādasahi | အာရုံခံ နယ်ပယ် … ဆယ့်တစ်ပါး (8) |
| āyatanehi pannarasahi | အာရုံခံ နယ်ပယ် … ဆယ့်ငါးပါး (12) |
| āyatanehi soḷasahi | အာရုံခံ နယ်ပယ် … ဆယ့်ခြောက်ပါး (49) |
| āyatanena | အာရုံခံ နယ်ပယ် (142) |
