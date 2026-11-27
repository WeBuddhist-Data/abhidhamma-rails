# pi-6 Burmese keyword mapping, PHASE 2, group G1 (2-02 … 5-03): notes

Script `map_g1.py` (imports `map6_rules.py`, which is NOT edited; holds only the G1 group table `T_ALL`, one per-segment
override `CTX` and five context functions `FUNCS_G1`). Burmese from the FINAL pi-6 text only; pi-1 … pi-5 mappings and
the pi-6 zero-shot notes (notes-ch3, notes-ch2-02-4-5, harmonise-notes) for the vocabulary. Read-only helpers in
`work/*_g1.py`. Run: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 map_g1.py [--s1] [--diff] [--pairs]`.

## Numbers (verified per chapter, in chapter order)

| chapter | lines | bad | presence failures | «, » / «၊» / « / » | (no direct equivalent) | chunks by an ending rule |
|---|---|---|---|---|---|---|
| 2-02-khandhayamaka | 156 | [] | 0 | 0 | 5 | 73 (verb 68, abs 4, neg-verb 1) |
| 3-01-ayatanayamaka | 93 | [] | 0 | 0 | 2 | 50 (attr 40, verb 10) |
| 3-02-ayatanayamaka | 46 | [] | 0 | 0 | 0 | 40 (attr 30, abs 6, verb 4) |
| 3-03-ayatanayamaka | 48 | [] | 0 | 0 | 0 | 33 (attr 23, abs 6, verb 4) |
| 3-04-ayatanayamaka | 65 | [] | 0 | 0 | 3 | 50 (attr 29, verb 15, abs 6) |
| 3-05-ayatanayamaka | 66 | [] | 0 | 0 | 1 | 51 (verb 26, attr 19, abs 6) |
| 3-06-ayatanayamaka | 61 | [] | 0 | 0 | 6 | 33 (attr 18, abs 9, verb 6) |
| 4-dhatuyamaka | 50 | [] | 0 | 0 | 2 | 7 (attr 4, verb 3) |
| 5-01-saccayamaka | 155 | [] | 0 | 0 | 3 | 28 (verb 14, attr 14) |
| 5-02-saccayamaka | 113 | [] | 0 | 0 | 3 | 42 (verb 32, attr 10) |
| 5-03-saccayamaka | 27 | [] | 0 | 0 | 5 | 12 (verb 8, attr 4) |
| **total** | **880** | **[]** | **0** | **0** | **30** | 419 |

- `bad []` also by the brief's own one-line command for each chapter. No presence exception outside the approved
  ending rules (attr / verb / abs / neg-verb: pi-1 rules 3 / 4 / 8, pi-2 N11, pi-3 M7, pi-4 P3, pi-5 Q1). All 30
  (no direct equivalent) are keywords «(no direct equivalent)» of the keyword files (frame value).
- Phrase scan (`work/phrase_g1.py`): every value stands in its segment as a phrase except the approved ending-rule
  cases upapajjitvā «ပြန်လည် ဖြစ်ပေါ်၍» against the text's «…ပြီး» (37 uses, pi-5 Q1) and one bare positive of a
  negated clause (nirujjhati, 2-02 ^6-2-130 «မချုပ်ငြိမ်း», rule 8 / Q5).
- Keyword uses 7665: the same value as a pi-1 … pi-5 mapping of the keyword (or its base form) 3572; a keyword pi-1 …
  pi-5 never mapped 3828; a different value 265 (31 pairs, below). No value differs from the phase-1 sample
  (1-mulayamaka, 2-01) for the same keyword.
- The module alone left 293 uses without a value (2-02 2, 3-01 40, 3-02 7, 3-03 9, 3-04 22, 3-05 18, 3-06 16, 4 20,
  5-01 67, 5-02 76, 5-03 16); all are mapped by the group table below.

## S1 (stem fallback) review: 141 uses of 40 keywords, kept 66 (24 keywords), corrected 75 (16 keywords)

Every use whose module-only value comes from S1 was checked against its segment (the script compares the module-only
run with the final one).

- **Kept** (the text's word for the keyword): Apāye «အပါယ်» 3; Avasese «ကြွင်းကျန်သော» 2 («ကြွင်းကျန်သော အစုအဝေး လေးပါး …»);
  Jivhāpi / jivha «လျှာ» 1 / 1; Kāyadhātuṃ, kāyadhātuñca «ကိုယ် ဓာတ်» 2 / 1; Manodhātuṃ, manodhātuñca «မနော ဓာတ်» 2 / 1;
  Rūpadhātuṃ, rūpadhātuñca «အဆင်းအရောင် ဓာတ်» 2 / 1; gandhadhātuñca «အနံ့ ဓာတ်» 1; rasadhātuñca «အရသာ ဓာတ်» 1;
  sotadhātuṃ, sotadhātuñca «နား ဓာတ်» 1 / 1; dhātū «ဓာတ်» 12; anulomampi «အဟုတ်ပြ ပုံစံ» 8; paccanīkampi «အငြင်းပြ ပုံစံ» 8;
  uppādepi «ဖြစ်ပေါ်ခြင်း» 3; nirodhepi «ချုပ်ငြိမ်းခြင်း» 5; atītepi «အတိတ်» 1; paccuppannepi «ပစ္စုပ္ပန်» 1;
  atītānāgatepi «အတိတ်နှင့် အနာဂတ်» 1; paññācakkhu «ပညာမျက်စိ» 6; manāyatana (slip) «မနော အာရုံခံ နယ်ပယ်» 1.
- **Corrected**: Cakkaṃ / cakkaṃ «မျက်စိ» -> «လှည့်ပတ်ခြင်း» 14 / 2 (G7); Attharaso «အနက်» -> «အနက်၏ အရသာ» 4, dhammaraso
  «သဘောတရား» -> «တရား၏ အရသာ» 4, vimuttiraso «လွတ်မြောက်မှု» -> «လွတ်မြောက်မှု၏ အရသာ» 4 (G6); Uppādavāro / uppādavāre,
  Nirodhavāro / nirodhavāre, Pariññāvāro «X» -> «Xအလိုက် ဖော်ပြချက်» 2 / 5, 3 / 2, 3 (G1); yatthakaṃ / Yatthakaṃ / yatthakā
  «အကြင်» -> «အကြင်နေရာ၌ အပိုင်း» 4 / 2 / 1 (G2); āpāyikānaṃ / Āpāyikānaṃ «အပါယ်» -> «အပါယ်၌ ရှိသူ» 18 / 6 (G10, R5);
  asaññattā «အသညသတ်» -> «အသညသတ် ဘုံ» 1 (slip, R5 plane).

## Rules used (binding, unchanged)

pi-1 rules 1-11 and the agreed later pi-1 rules; pi-2 N1-N11; pi-3 M1-M9 (M2: a word only inside a Roman-script
variant = (no direct equivalent)); pi-4 P1-P8 / A2 (P6 agent nouns «…သူ»); pi-5 Q1-Q8, S1, S3 / G3, G1 / G2; the
phase-1 pi-6 rules R1-R9 (map-table.md) as approved by the coordinator 2026-11-22 (two root-predicate shapes, the
segment's own form, Āmantā / No / Natthi, nāma «စိတ်ပိုင်း», arūpa plane «ရုပ်မရှိသော ဘုံ»). The module maps the
frame of every G1 chapter unchanged (verbs R2, participles R3, khandha R4, planes R5, headings R6, families R8 incl. the
four sacca «X သစ္စာ», answers R9).

## NEW rules of the group (G1-G11), for review

G1. **A vāra named in running text or in an editorial note** (R6 reads only heading lines) = the text's whole name
    «Xအလိုက် ဖော်ပြချက်» (rule 7; the «၌ / ၌လည်း» of the locative and the «လည်း» of -pi go, rules 1 / Q4): Uppādavāro /
    uppādavāre / -vārepi «ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်», Nirodhavāro / nirodhavāre / -vārepi «ချုပ်ငြိမ်းခြင်းအလိုက်
    ဖော်ပြချက်», Uppādanirodhavāro / -vārepi «ဖြစ်ပေါ်ခြင်းနှင့် ချုပ်ငြိမ်းခြင်းအလိုက် ဖော်ပြချက်», Pariññāvāro
    «ပိုင်းခြား သိခြင်းအလိုက် ဖော်ပြချက်»; without vāra the noun (uppādepi «ဖြစ်ပေါ်ခြင်း», uppādanirodhepi «ဖြစ်ပေါ်ခြင်းနှင့်
    ချုပ်ငြိမ်းခြင်း»); vāresu «ဖော်ပြချက်» («ဖော်ပြချက် သုံးပါးလုံး၌»); vārasaṅkhepo «ဖော်ပြချက်တို့၌ အကျဉ်း ဖော်ပြထားသည်»
    (notes-ch3 «upari vārasaṅkhepo»; the inner «တို့၌» stays, rule 1).
G2. **The editorial sections** yassaka / yatthaka / yassayatthaka (f_aka) = «Q အပိုင်း» with the cited question word
    of the text's quotation «“အကြင်သူအား” / “အကြင်နေရာ၌” / “အကြင်သူအား အကြင်နေရာ၌” အပိုင်း» (harmonise-notes; the cited
    word keeps its «အား / ၌», rule 1 inner particles; the final «၌ / တွင် / ကို / များ» and the «လည်း» of -pi go): yassakampi
    «အကြင်သူအား အပိုင်း», yatthakaṃ / -kā / -kānaṃ / -kampi «အကြင်နေရာ၌ အပိုင်း», yassayatthakampi / yassayatthakepi /
    «yassa yatthake» «အကြင်သူအား အကြင်နေရာ၌ အပိုင်း»; X-sadisaṃ «Q အပိုင်းနှင့် တူညီသည်» (rule 4: yassakasadisaṃ,
    yatthakasadisaṃ), the text's adverbial «…နှင့် တူညီအောင်» where the note has «sadisaṃ kātabbaṃ» (yassayatthakasadisaṃ,
    5-01 ^6-5-70). A section name that stands only inside a Roman-script variant (5-02 ^6-5-95 «[yassakampi yatthakampi
    (sī. syā.)]») = (no direct equivalent) by M2 (no such keyword in the files; the function checks it).
G3. **sa-X-ka / a-X-ka persons** (f_saka; frame-coverage «Whole-book dry run») = the adjective «X ရှိသော / X မရှိသော»
    (pi-1 rule 3 as Sahetukaṃ «အမြစ် ရှိသော»; the text's «X ရှိလျက် / X မရှိဘဲ» before the participle by the ending rule
    «လျက် / ဘဲ», pi-2 N11): sacakkhukānaṃ «မျက်စိ ရှိသော», acakkhukānaṃ «မျက်စိ မရှိသော», sasotakānaṃ «နား ရှိသော»,
    asotakānaṃ «နား မရှိသော», arūpakānaṃ «ရုပ် မရှိသော» (the person without matter, not the plane R5).
G4. **The fused negative nāyatana** (f_nayatana; na + āyatana in one word, as pi-1 / pi-2 nariya «အရိယာ မဟုတ်သော»,
    nattā «အတ္တ မဟုတ်သော»): the subject nāyatanā «အာရုံခံ နယ်ပယ်တို့ မဟုတ်သော အရာ» = «အာရုံခံ နယ်ပယ် … မဟုတ်သော» (the inner
    plural «တို့» outside, rule 10); the predicate nāyatanaṃ / nāyatananti «… အာရုံခံ နယ်ပယ် မဟုတ်သလော» = «အာရုံခံ နယ်ပယ်
    မဟုတ်» (pi-1 rule 5, Q5).
G5. **X-vippayutta citta and its moments** (f_citta; notes-ch2-02-4-5): taṇhāvippayuttacitte (vattamāne) «တပ်မက်မှုနှင့်
    ကင်းကွာသော စိတ်» (pi-1 rule 3 «…နှင့် ကင်းကွာသော», pi-1 / pi-2 taṇhā «တပ်မက်မှု»; vattamāne is its own keyword); two
    members «Aနှင့် ကင်းကွာ၍ Bနှင့် ကင်းကွာသော စိတ်» (the text's absolutive «၍»); upapatticitta «ပြန်လည် ဖြစ်ပေါ်ခြင်း စိတ်»;
    with a moment «… စိတ်၏ ဖြစ်ခြင်း ခဏ / ပြိုပျက်ခြင်း ခဏ» (R8 / harmonise B1: the final «၌» goes, the inner «၏» stays).
G6. **The non-āyatana kinds of sota / gandha / rasa** in the 3-01 / 4 niddesa = «X၏ Y» (notes-ch3; rule 1 the inner «၏»):
    Sīlagandho «သီလ၏ အနံ့», samādhigandho «သမာဓိ၏ အနံ့», paññāgandho «ပညာ၏ အနံ့», Attharaso «အနက်၏ အရသာ», dhammaraso
    «တရား၏ အရသာ», vimuttiraso «လွတ်မြောက်မှု၏ အရသာ»; taṇhāsotaṃ «တပ်မက်မှု ရေစီး»; Dibbasotaṃ «နတ်နား» (pi-5).
G7. **cakka = the round «လှည့်ပတ်ခြင်း»** (Cakkaṃ / cakkaṃ bandhitabbaṃ «လှည့်ပတ်ခြင်းကို … ဖွဲ့ရမည်»; the same word as the
    phase-1 headings «…cakkavāro = … လှည့်ပတ်ခြင်း ဖော်ပြချက်»).
G8. **yattha «where» = «အကြင်နေရာ»** (the text «အကြင်နေရာ၌», rule 1; the place noun is yattha's own word, as pi-2 yassa
    «အကြင်သူ»): Yattha / yattha, and composed «Yassa yattha» = «အကြင်သူအား အကြင်နေရာ» (Q3, the inner «အား» stays).
G9. **A chapter title cited in a note, any case** = the approved title whole (rule 7; the text quotes it): āyatanayamake /
    āyatanayamakassa «အာရုံခံ နယ်ပယ်များကို အတွဲလိုက် မေးဖြေခြင်း», dhātuyamakampi / -assa / -epi «ဓာတ်များကို အတွဲလိုက်
    မေးဖြေခြင်း»; X-sadiso «Xနှင့် တူညီသည်» (ghānasadiso «နှာခေါင်းနှင့် တူညီသည်», ghānadhātusadisā «နှာခေါင်း ဓာတ်နှင့်
    တူညီသည်»; pi-1 / pi-2 «တူညီသူ» is the person, not in the segment).
G10. **The persons of ch. 5** (tuples: the agent noun, its attributive before another person noun, rule 3 / P6):
    Abhisametāvīnaṃ «ထင်ထင်ရှားရှား သိမြင်ပြီးသူ / …သိမြင်ပြီးသော» (harmonise A1; pi-5 abhisameti), Anabhisametāvīnaṃ
    «ထင်ထင်ရှားရှား မသိမြင်ရသေးသူ / …မသိမြင်ရသေးသော»; caññe «အခြားသူ» («မဂ်ကို ရရှိမည့် အခြားသူတို့»; the «ca» has no word,
    R1); āpāyikānaṃ «အပါယ်၌ ရှိသူ» (R5 beings of a plane; Apāye «အပါယ်»); aggaphalassa «အမြတ်ဆုံး ဖိုလ်» (agga- pi-2).
G11. **Pāli slips** = the value of the intended word where the text renders that word: vadanākkhandho «ခံစားမှု အစုအဝေး»
    (2-02 ^6-2-185), sotāyananti «နား အာရုံခံ နယ်ပယ်» (3-01 ^6-3-13), parinibbāntānaṃ «ပရိနိဗ္ဗာန် ပြုဆဲသူ» (3-05 ^6-3-172),
    asaññattā «အသညသတ် ဘုံ» (5-02 ^6-5-76, «… ဘုံမှ စုတေဆဲသူ»), upapajjissati for uppajjissati «ဖြစ်ပေါ်လိမ့်မည်» (3-06
    ^6-3-212, CTX; the module had assembled «ပြန်လည် ဖြစ်ပေါ်လိမ့်မည်» from chunks scattered over the segment);
    uppajjittharūpāyatanañca (3-01 ^6-3-43, two words run together) «အဆင်းအရောင် အာရုံခံ နယ်ပယ် … ဖြစ်ပေါ်ခဲ့သည်» (both
    members, verb last Q3, « … » for the «လည်း» of ca Q4). The module's stem values for the slips manāyatana, nirujjhatī,
    nirujjhiti, jivha, aggamaggaṃ paṭilabhissānti are the intended word's and are kept.

## Module overrides (for phase 3; `map6_rules.py` not edited)

1. **f_rupam (STOCK rūpaṃ / rūpa)**: in the āyatana / dhātu padasodhana and niddesa («rūpaṃ rūpāyatanaṃ?», «rūpaṃ
   rūpadhātūti?») the module gives «အဆင်းအရောင်» because the Pāli has rūpāyatan- / rūpadhātu, but that word belongs to
   the keyword rūpāyatanaṃ / rūpadhātu; the text renders the bare rūpaṃ «ရုပ်» («ရုပ်သည် အဆင်းအရောင် အာရုံခံ နယ်ပယ်
   ဖြစ်သလော»). G1 override `f_rupam_g1`: «ရုပ်» where the text has a free «ရုပ်» (not inside «ရုပ်မရှိ / ရုပ်ဘုံ / ရုပ် မရှိ /
   ရုပ် ရှိလျက် / ရုပ် အစုအဝေး»), else the module value; for rūpaṃ, Rūpaṃ, rūpanti, Rūpañca, rūpañceva (3-01 8 uses, 4 6
   uses changed from «အဆင်းအရောင်» to «ရုပ်»). Suggest moving it into the module (other groups: check 9 / 10 rūpa).
2. **S1 values that are wrong** (corrected above): the module should not reach S1 for the vāra names in running text
   (G1), the section names (G2), cakka (G7), the «X-raso» kinds (G6), āpāyika (G10); suggest the G1 table entries.
3. **Keywords the module does not map** (293 uses): the G1 table `T_ALL` and `FUNCS_G1` (f_aka, f_saka, f_citta,
   f_nayatana) are general (regex families) and can move into the module as they are.
4. The R1 base form of «parijānanti» is «parijānaṃ» (base_forms reads «-anti» as «-aṃ + ti»), so the diff counter
   compares it with pi-2's participle «ပိုင်းခြား သိ၍»; the value itself comes from R2 (correct). Harmless here; phase 3
   may want base_forms to skip finite «-anti».

## Values different from pi-1 … pi-5 (same keyword; 265 uses, 31 pairs)

| keyword = G1 value | pi-1 … pi-5 value (uses) | reason |
|---|---|---|
| arūpaṃ / Arūpaṃ / arūpā = ရုပ်မရှိသော ဘုံ | ရုပ် မဟုတ်သော (37 / 2 / 3) | module R5, as phase 1 (approved) |
| anulomaṃ = အဟုတ်ပြ ပုံစံ; paccanīkaṃ = အငြင်းပြ ပုံစံ | အစဉ်အတိုင်း; ပြောင်းပြန် (24 / 24) | module FRAME, as phase 1 (approved) |
| kāmāvacaraṃ / Kāmāvacaraṃ / Kāmāvacarā / kāmāvacarā = ကာမဘုံ | ကာမဘုံနှင့် ဆိုင်သော (20 / 7 / 12 / 8) | module R5: the plane as goal / source («ကာမဘုံ၌ ပြန်လည် ဖြစ်ပေါ်ဆဲ», «ကာမဘုံမှ စုတေဆဲ»); the adjective not in the segment |
| rūpāvacara- (aṃ, e, ā; 15 / 6 / 3 / 4 / 3 / 4) = သိမ်မွေ့သော ရုပ်ဘုံ; arūpāvacaraṃ / -e = ရုပ်မရှိသော ဘုံ (13 / 10) | …ဘုံနှင့် ဆိုင်သော | module R5, as above |
| kāmāvacarānaṃ / Kāmāvacarānaṃ = ကာမဘုံ၌ ရှိသူ (4 / 5), ကာမဘုံ၌ ရှိသော (3) | ကာမဘုံနှင့် ဆိုင်သော | module R5 beings of a plane (agent noun / attributive before a person noun) |
| Cakkaṃ / cakkaṃ = လှည့်ပတ်ခြင်း | တရားစက် (14 / 2) | G7: the round of the Yamaka; pi-2 / pi-5 «တရားစက် / စကြာ» (the wheel of Dhamma) not in the segment |
| dhātū / dhātūti = ဓာတ် | ဘုံ (12 / 4) | rule 11: the elements of ch. 4 «ဓာတ်တို့» (pi-1 / pi-2 / pi-3 dhātu «ဓာတ်»); pi-5 «ဘုံ» is the plane sense, not in the segment |
| Rūpadhātuṃ / rūpadhātuñca / rūpadhātūti = အဆင်းအရောင် ဓာတ် | သိမ်မွေ့သော ရုပ် ဓာတ် / …ရုပ်ဘုံ (2 / 1 / 2) | rule 11: the visible-object element of the eighteen (pi-2 rūpadhātu «အဆင်းအရောင် ဓာတ်» in ch. 4's own segments); the plane sense not in the segment |
| Yattha / yattha = အကြင်နေရာ | (no direct equivalent) / အကြင် (8 / 1) | G8: the text's «အကြင်နေရာ၌» carries yattha (correlative, as pi-2 yassa «အကြင်သူ»); pi-5's relative-pronoun (no direct equivalent) applies where the Burmese builds the clause with «ရှိသော» |
| Avasese = ကြွင်းကျန်သော | အကြွင်း (2) | S1 kept: the text's attributive «ကြွင်းကျန်သော အစုအဝေး လေးပါး …»; pi-1 noun «အကြွင်း» not in the segment |
| parijānanti = ပိုင်းခြား သိသည် | ပိုင်းခြား သိ၍ (6) | not a real difference: R2 present plural; the pi value is that of the false base form «parijānaṃ» (override 4) |

## Text inconsistencies (for the rails step; the translation was not changed)

T1. Pāli slips in G1 (G11): vadanākkhandho (^6-2-185), sotāyananti (^6-3-13), uppajjittharūpāyatanañca (^6-3-43, no
    space), parinibbāntānaṃ (^6-3-172), manāyatana…pe… (^6-3-186), upapajjissati for uppajjissati (^6-3-212),
    nirujjhatī ti (3-04 ^6-3-131), asaññattā (^6-5-76), nirujjhiti (5-02), aggamaggaṃ paṭilabhissānti (5-01). The
    Burmese renders the intended word in each.
T2. 5-03 ^6-5-159 / ^6-5-162: the Pāli has both «arūpe aggamaggassa ca phalassa ca uppādakkhaṇe» and «arūpe aggaphalassa
    uppādakkhaṇe»; the text keeps them apart («အမြတ်ဆုံး မဂ်နှင့် ဖိုလ်» / «အမြတ်ဆုံး ဖိုလ်»), correct; noted because the
    keyword list has «aggaphalassa» and «Aggamaggassa / phalassa» in the same segment.
T3. The editorial notes render «sadisaṃ» as «တူညီသည်» but «sadisaṃ kātabbaṃ» as «တူညီအောင် ပြုရမည်» (5-01 ^6-5-70,
    4 ^6-4-18, 3-05 ^6-3-201): one Pāli word, two Burmese constructions; the mapping takes each segment's own form (G2).
T4. In the āyatana niddesa «Dibbasotaṃ taṇhāsotaṃ sotaṃ» the predicate sotaṃ is «“သောတ” (နား သို့မဟုတ် ရေစီး)» while the
    keyword sotaṃ elsewhere in the segment is «နား»; one sense per segment: «နား» (the «ရေစီး» belongs to taṇhāsotaṃ).

## Unclear mappings (for the coordinator)

U1. nāyatanā as subject (G4): «အာရုံခံ နယ်ပယ် … မဟုတ်သော» (gap over the plural «တို့») or the contiguous «အာရုံခံ
    နယ်ပယ်တို့ မဟုတ်သော» (the plural inside, rule 1 inner particles). Chose the gap (rule 1: no plural markers in a value).
U2. sa-X-ka persons (G3): «X ရှိသော» by the ending rule (as the frame-coverage note) or the text's literal «X ရှိလျက် /
    X မရှိဘဲ» (as absolutives keep «၍»). Chose «…ရှိသော / …မရှိသော».
U3. Yattha «အကြင်နေရာ» (G8) departs from pi-5's two values; if the coordinator prefers the relative-pronoun reading,
    the value is «အကြင်» (present in every segment).
U4. The slip «uppajjittharūpāyatanañca» (G11): the joined value «အဆင်းအရောင် အာရုံခံ နယ်ပယ် … ဖြစ်ပေါ်ခဲ့သည်»; the Pāli
    verb belongs to the preceding dhammāyatanañca (in the text before rūpāyatana), Q3 puts it last.
