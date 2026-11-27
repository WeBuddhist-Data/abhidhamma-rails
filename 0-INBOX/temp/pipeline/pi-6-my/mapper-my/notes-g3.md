# pi-6 Burmese keyword mapping, PHASE 2, group G3 (9-01 … 10-13): notes

Chapters 9-01 … 9-03 dhammayamaka and 10-01 … 10-13 indriyayamaka, mapped in chapter order by `map_g3.py` (imports
`map6_rules.py`, NOT edited, md5 74f11cc5c6e57834b6ef88d07aa13a54; holds only the group table `T_ALL`, three per-segment
overrides `CTX` and five context functions `FUNCS_G3`). Burmese from the FINAL pi-6 text only; vocabulary from
`my6-zeroshot-terms.md`, the zero-shot notes `notes-ch9-10a.md` / `notes-ch10b.md` / `notes-ch10c.md`, `harmonise-notes.md`
and the final pi-1 … pi-5 mappings. Not committed. Run:
`/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 map_g3.py [chapter-prefix …] [--report]`.
Read-only helpers: `work/dry_g3.py` (module-only dry run), `work/g3_seg.py` (segment / KWIC viewer).
Two runs give byte-identical `.mapped.md` files and identical output (`work/g3_run1.txt`, `work/g3_run2.txt`,
`work/g3_md5_run1.txt` = `work/g3_md5_run2.txt`).

## Numbers (verifier of the module + the brief's preservation command)

| chapter | lines | bad | presence failures | «, » / «၊» / « / » | (no direct equivalent) | chunks by an ending rule |
|---|---|---|---|---|---|---|
| 9-01-dhammayamaka | 165 | [] | 0 | 0 | 0 | verb 116, plural 60, attr 8 |
| 9-02-dhammayamaka | 136 | [] | 0 | 0 | 4 | verb 212, plural 56, attr 12 |
| 9-03-dhammayamaka | 69 | [] | 0 | 0 | 1 | plural 84, verb 71, attr 4 |
| 10-01-indriyayamaka | 166 | [] | 0 | 0 | 0 | - |
| 10-02-indriyayamaka | 69 | [] | 0 | 0 | 1 | attr 35, verb 10 |
| 10-03-indriyayamaka | 20 | [] | 0 | 0 | 0 | attr 53 |
| 10-04-indriyayamaka | 20 | [] | 0 | 0 | 0 | attr 34, verb 14 |
| 10-05-indriyayamaka | 57 | [] | 0 | 0 | 0 | verb 53, attr 48, abs 4 |
| 10-06-indriyayamaka | 40 | [] | 0 | 0 | 0 | attr 34, abs 8, verb 4 |
| 10-07-indriyayamaka | 10 | [] | 0 | 0 | 0 | attr 9, abs 4 |
| 10-08-indriyayamaka | 37 | [] | 0 | 0 | 0 | attr 29, verb 18 |
| 10-09-indriyayamaka | 22 | [] | 0 | 0 | 0 | attr 18, abs 8, verb 1 |
| 10-10-indriyayamaka | 12 | [] | 0 | 0 | 0 | attr 9, abs 4, verb 1 |
| 10-11-indriyayamaka | 10 | [] | 0 | 0 | 0 | attr 9, abs 4 |
| 10-12-indriyayamaka | 39 | [] | 0 | 0 | 0 | attr 30, abs 12, verb 4 |
| 10-13-indriyayamaka | 61 | [] | 0 | 0 | 7 | verb 77, attr 48, neg-infix 44 |
| **total** | **933** | **[]** | **0** | **0** | **13** | 1249 (verb 581, attr 380, plural 200, abs 44, neg-infix 44) |

- Every (no direct equivalent) is a keyword «(no direct equivalent)» of the keyword files (frame value); no other keyword
  got it. No presence exception outside the module's approved ending rules.
- The module alone left 465 uses (96 keywords) without a value and gave 33 uses a value that is changed here (listed
  under «Module overrides»); every one is now mapped.
- Phrase scan (`--report`, the G1 / G2 «scattered words» check): every value stands in its segment as a phrase except
  ending-rule cases of approved rules: the plural future «Sကြလိမ့်မည်» of the Dhammayamaka (uppajjissanti /
  nirujjhissanti, rule «plural»), upapajjitvā «ပြန်လည် ဖြစ်ပေါ်၍» against the text's «…ပြီး» (44, pi-5 Q1), and the bare
  positive of a negated clause in 10-13 (parijānāti / sacchikaroti in every tense where the text has only «ပိုင်းခြား မသိ /
  မျက်မှောက် မပြု», rule 8 / Q5; rules «neg-verb» / «neg-infix»). The literal tier with scattered words occurred once:
  the slip upapajjissati of ^6-10-309 (module «ပြန်လည် ဖြစ်ပေါ်လိမ့်မည်» from «ပြန်လည် ဖြစ်ပေါ်…» and «…လိမ့်မည်» of other
  clauses; overridden, O4); a value glued to a phrase of ANOTHER keyword occurred in compose (O1) and in the feminine
  participles (O3).
- Values vs pi-1 … pi-5 (same keyword or its base form): 6483 uses the same, 3426 uses of keywords pi-1 … pi-5 never
  mapped, 343 uses (29 pairs) different (table below; 122 of them are the base-form artefact of «-anti»).
- Values vs the sample and the G1 / G2 files (same keyword): Pacchimabhavikānaṃ «နောက်ဆုံး ဘဝ ရှိသော» (4) and Itaresaṃ
  «အခြား» (2), both the module's tuple value where the text has the attributive before a noun («… ရှိသော မိန်းမတို့»,
  «အခြား ယောက်ျားတို့»); otherwise none.

## S1 review (stem fallback): module alone 125 uses (19 keyword / value pairs); kept 119 (13 pairs), corrected 6 (6 pairs)

- **Kept**: itthiyo / itthīnaṃ / Itthiṃ / Itthiñca «မိန်းမ» 36 / 19 / 2 / 4 and purisā / Purisaṃ / Purisañca «ယောက်ျား»
  36 / 2 / 4 (pi-4 itthī, pi-5 puriso; the text's head noun «မိန်းမတို့ / ယောက်ျားတို့», rule 1); Aññātāviṃ /
  Aññātāviñca (10-02) «အပြည့်အဝ သိမြင်ပြီးသူ» 2 / 1 (pi-5 aññātāvī; now also in the group table, same value); Acittakānaṃ
  «စိတ် မရှိသော» 4 (= f_saka); Aṭṭhamako / Aṭṭhamakañca «အဋ္ဌမ» 5 / 1 (pi-5 aṭṭhamakassa, binding, as G2; U5);
  paññācakkhu «ပညာမျက်စိ» 3.
- **Corrected**: Aññātāviñca (10-01 ^6-10-141) «အပြည့်အဝ သိမြင်ပြီးသူ၏ စွမ်းရည်» -> «အပြည့်အဝ သိမြင်ပြီးသူ» and
  Anaññātaññassāmītiñca «… ဟူသော စွမ်းရည်» -> «မသိရသေးသည်ကို သိရတော့မည်ဟူသော» (the stem took the faculty NAME of the same
  segment; the keyword is the bare word «Xñca indriye ca ṭhapetvā» «Xနှင့် စွမ်းရည်တို့ကို ချန်ထား၍»); the vāra colophons in
  body lines Uppādavāro «ဖြစ်ပေါ်ခြင်း», Nirodhavāro «ချုပ်ငြိမ်းခြင်း», Pariññāvāro «ပိုင်းခြား သိခြင်း», Bhāvanāvāro «ဘာဝနာ
  ပွားများခြင်း» -> «Xအလိုက် ဖော်ပြချက်» (G1 rule G1 / G2 V1; the text's «ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်။»).
- In the final files 112 uses still come from the stem fallback, all in the «kept» list.

## Rules used

pi-1 rules 1-11 and the agreed later pi-1 rules, pi-2 N1-N11, pi-3 M1-M9, pi-4 P1-P8 / A2, pi-5 Q1-Q8 / S1 / S3 / G1-G3,
the phase-1 rules R1-R9 (`map-table.md`) as settled by the coordinator 2026-11-22, and the G1 / G2 group rules where
the same keyword stands in the same sense (yattha «အကြင်နေရာ» G1 G8 / G2 O6; vāra names in body lines G1 G1 / G2 V1;
sa-X-ka persons G1 G3; X-vippayutta citta + moment G1 G5; upapatticitta, taṇhāsota, agga- G1 G5 / G6 / G10; Pāli slips
G1 G11). Most used here: R2 (uppajjati / nirujjhati with the plural «ကြ», pajahati, parijānāti, bhāveti, sacchikaroti,
paṭilabhati in every tense and polarity), R3 (upapajjantānaṃ / cavantānaṃ «…ဆဲသူ», upapajjitvā «…၍»), R4 «(X-indriya-
mūlakaṃ)» = «X၏ စွမ်းရည်ကို အခြေခံသော», R5 (planes and beings), R6 (headings), R8 (-samaṅgī), the pi-2 faculty names
(«X၏ စွမ်းရည်») and their bare words, rule 3 / 10.

## NEW group rules (W1-W7, for review; the coordinator may move them into the module in phase 3)

W1. **X-sampayutta / X-vippayutta citta compounds** (f_citta; extends G1 G5 to X = kusala, akusala, saddhā, somanassa,
    upekkhā, ñāṇa; zero-shot notes ch9-10a / ch10b / ch10c): «Xနှင့် ယှဉ်တွဲသော / ကင်းကွာသော စိတ်» (pi-1 rule 3, pi-1 ^1-1,
    pi-2 ^2-767); two members «Aနှင့် ယှဉ်တွဲ၍ / ကင်းကွာ၍ Bနှင့် … သော စိတ်» (the text's absolutive); -pacchimacitta «…
    နောက်ဆုံး စိတ်»; -pacchimacittasamaṅgīnaṃ «… နောက်ဆုံး စိတ်နှင့် ပြည့်စုံသူ» (R8 agent noun); with a moment «… စိတ်၏
    ဖြစ်ခြင်း ခဏ / ပြိုပျက်ခြင်း ခဏ» (harmonise B1, the final «၌» goes). 305 uses the module left without a value, all
    literal phrases of the text; upapatticitta (+ moments) as G1.
W2. **Persons qualified by a citta factor**: ñāṇasampayuttānaṃ / Ñāṇasampayuttānaṃ = «ဉာဏ်နှင့် ယှဉ်တွဲသော» (as the pi-2
    ñāṇavippayuttānaṃ «ဉာဏ်နှင့် ကင်းကွာသော» in the same segments; the text's «… ယှဉ်တွဲလျက်» by the ending rule «လျက်»,
    harmonise B9); sa-X-ka / a-X-ka with X = cakkhu, sota, citta, any case incl. the nominative sacakkhukā (f_saka, G1 G3)
    «X ရှိသော / X မရှိသော».
W3. **Feminine participles -antīnaṃ** (f_fem): «itthīnaṃ upapajjantīnaṃ» «ပြန်လည် ဖြစ်ပေါ်ဆဲ မိန်းမတို့» = the attributive
    «ပြန်လည် ဖြစ်ပေါ်ဆဲ» (R3: the participle before another person noun without a marker); after a relative «… tāsaṃ
    upapajjantīnaṃ / cavantīnaṃ» «…မိန်းမတို့အနက် ပြန်လည် ဖြစ်ပေါ်ဆဲသူတို့ / စုတေဆဲသူတို့» = the agent noun (the module
    value). One sense per segment: the keyword's first occurrence in the Pāli decides (its preceding word tāsaṃ or not).
W4. **The bare words of the faculties** (padasodhana / paṇṇatti, 10-01 / 10-02): aññaṃ / Aññaṃ / aññanti / Aññañca =
    «အပြည့်အဝ သိမြင်ခြင်း», anaññātaññassāmīti / -tiṃ / -tiñca (and the slip anaññātaññāssāmīti) = «မသိရသေးသည်ကို
    သိရတော့မည်ဟူသော», Aññātāviṃ / Aññātāviñca = «အပြည့်အဝ သိမြင်ပြီးသူ»: the pi-2 faculty name without «(၏) စွမ်းရည်»
    (ch9-10a notes; harmonise A2); the head noun «အရာ» that the text adds after «…ဟူသော» is not part of the value (rule 3,
    as the module's bare abyākatā «… မဟုတ်သော» against the text's «… မဟုတ်သော အရာများ»; U1).
W5. **«Xñca dhamme ca ṭhapetvā»** (9-01 ^6-9-26): «Xနှင့် သဘောတရားများကို ချန်ထား၍» = «Xနှင့် သဘောတရား» (Q3; the «နှင့်» of
    ca … ca stays inside, rule 1; the plural goes): Kusalañca dhamme «ကုသိုလ်နှင့် သဘောတရား», Akusalañca dhamme «အကုသိုလ်နှင့်
    သဘောတရား», Abyākatañca dhamme «ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော … သဘောတရား» (rule 10 over the text's «အရာများနှင့်»;
    U3).
W6. **sacchikaroti, bare positive of a negated clause** (f_sacchi; rule 8 / Q5): the module's «မျက်မှောက်ပြု…» wherever the
    verifier finds it (literal, by an ending rule, or the «neg-infix» rule against «မျက်မှောက် မပြု…»); in the 4 segments of
    10-13 (^6-10-447 … ^6-10-450) where the text has only «မျက်မှောက် မပြုခဲ့၊ / …သလော» the past has no verifiable joined
    form, so sacchikarittha / -itthāti = «မျက်မှောက် ပြုခဲ့သည်», the positive part with the text's spacing (pi-5 sacchikaroti
    «မျက်မှောက် ပြုသည်»; U4).
W7. **Other group values**: the vāra colophons in body lines (Uppāda-, Nirodha-, Uppādanirodha-, Pariññā-, Bhāvanā-,
    Pavattivāro) «Xအလိုက် ဖော်ပြချက်» (f_vara; Bhāvanāvāro «ဘာဝနာ ပွားများခြင်းအလိုက် ဖော်ပြချက်», ch9-10a); the headings with
    a source digit and no dot «#### 3 Suddhadhammavāro» (R6 cannot split them) = the text's whole part «ရိုးရိုး သဘောတရား
    ဖော်ပြချက်», «ရိုးရိုး သဘောတရားကို အခြေခံ၍ လှည့်ပတ်ခြင်း ဖော်ပြချက်»; the book colophon Yamakapakaraṇaṃ «အတွဲလိုက်
    မေးဖြေခြင်း ကျမ်း» (pi-2 Vibhaṅgapakaraṇaṃ «ခွဲခြမ်းစိတ်ဖြာခြင်း ကျမ်း»; U8); aggaphalaṃ «အမြတ်ဆုံး ဖိုလ်», taṇhāsotaṃ
    «တပ်မက်မှု ရေစီး», upapatticittassa «ပြန်လည် ဖြစ်ပေါ်ခြင်း စိတ်» (G1 values); the Pāli slips with the intended word's value
    (Ghānandriyamūlakaṃ «နှာခေါင်း၏ စွမ်းရည်ကို အခြေခံသော», cavantāna «စုတေဆဲသူ»; CTX: ^6-10-309 upapajjissati
    «ဖြစ်ပေါ်လိမ့်မည်», ^6-10-398 uppajjantānaṃ and ^6-10-206 uppajjantīnaṃ «ပြန်လည် ဖြစ်ပေါ်ဆဲ», harmonise A3).

## Module overrides (map6_rules.py not edited; for phase 3)

O1. **compose glued to another keyword's phrase** (Kusalañca / Akusalañca / Abyākatañca dhamme, 4 uses): join_text_order
    found «X သဘောတရား» (the phrase of the keyword «X dhammā» in the (Kha) question of the same segment) and dropped the
    «နှင့်» of «Xနှင့် သဘောတရားများကို»; override W5. Phase 3 might prefer a «နှင့်» join where both Pāli members carry ca.
O2. **stem fallback took a faculty name for a bare word** (Aññātāviñca, Anaññātaññassāmītiñca; 2 uses) and the module had
    no value for aññaṃ / anaññātaññassāmīti and their forms (46 uses): W4.
O3. **feminine participles** (upapajjantīnaṃ, 18 uses): the module's agent noun «ပြန်လည် ဖြစ်ပေါ်ဆဲသူ» stands in those
    segments only as the word of the masculine upapajjantānaṃ; W3.
O4. **Pāli slips** (3 uses): upapajjissati (^6-10-309) «ပြန်လည် ဖြစ်ပေါ်လိမ့်မည်» assembled from chunks scattered over the
    segment (the literal-tier case of G1 / G2); uppajjantānaṃ / uppajjantīnaṃ (^6-10-398 / ^6-10-206) «ဖြစ်ပေါ်ဆဲသူ», found
    only inside the «ပြန်လည် ဖြစ်ပေါ်ဆဲသူ» of another keyword; override the text's «ပြန်လည် ဖြစ်ပေါ်ဆဲ» (intended upapajj-).
O5. **vāra names in body lines** (4 uses): stem values of the bare action noun; W7 (as G1 / G2).
O6. **Yattha / yattha** (2): pi-5 «အကြင်» -> «အကြင်နေရာ» (as G1 / G2).
O7. **Gaps the module leaves** (no value; 419 further uses): the citta compounds W1 incl. upapatticitta (305),
    ñāṇasampayuttānaṃ (34), the sa-X-ka persons (55; with the S1-kept Acittakānaṃ 59), sacchikarittha / -itthāti in
    negated-only segments (8), Uppādanirodhavāro in a body line (1), the Suddhadhamma headings (2), aggaphalaṃ (8),
    taṇhāsotaṃ (3), Yamakapakaraṇaṃ (1), the slips Ghānandriyamūlakaṃ / cavantāna (2).
O8. (noted, harmless, as G1 override 4) base_forms reads finite «-anti» as «-aṃ + ti», so the diff counter compares
    nirujjhissanti / -antīti (116) and parijānanti (6) with a false base form; the values come from R2 and are correct.

## Values different from pi-1 … pi-5 (same keyword; 343 uses, 29 pairs)

| keyword = G3 value | pi-1 … pi-5 value (uses here) | reason |
|---|---|---|
| nirujjhissanti / -antīti / Nirujjhissanti = ချုပ်ငြိမ်းလိမ့်မည် | ချုပ်ငြိမ်းသည် (51 / 62 / 3) | not a difference: R2 future; the pi value is that of the false base form (O8) |
| parijānanti = ပိုင်းခြား သိသည် | ပိုင်းခြား သိ၍ (6) | not a difference: R2 present (O8; G1 override 4) |
| anulomaṃ / paccanīkaṃ = အဟုတ်ပြ / အငြင်းပြ ပုံစံ | အစဉ်အတိုင်း / ပြောင်းပြန် (22 / 22) | module FRAME (approved sample departure 2) |
| Rūpāvacare / rūpāvacare / rūpāvacaraṃ / Rūpāvacaraṃ / -ā = သိမ်မွေ့သော ရုပ်ဘုံ; arūpāvacare / -aṃ = ရုပ်မရှိသော ဘုံ; kāmāvacaraṃ / Kāmāvacarā = ကာမဘုံ | …နှင့် ဆိုင်သော (21+3+10+2+2 / 21+15 / 18+16) | module R5: the plane as a place («…၌ / …မှ»; harmonise B8), as G1 |
| Kāmāvacarānaṃ / kāmāvacarānaṃ = ကာမဘုံ၌ ရှိသူ (8), ကာမဘုံ၌ ရှိသော (3) | ကာမဘုံနှင့် ဆိုင်သော | module R5 beings (before «အခြားသူ» the attributive), as G1 / G2 |
| arūpaṃ = ရုပ်မရှိသော ဘုံ | ရုပ် မဟုတ်သော (8) | module R5 (approved) |
| aññaṃ / Aññaṃ / aññanti / Aññañca = အပြည့်အဝ သိမြင်ခြင်း | တခြားစီ (17 / 3 / 2 / 2) | rule 11 (sense) / W4: añña = final knowledge (the faculty aññindriya); pi-5 «တခြားစီ» is añña "other", not in the segment |
| sacchikaroti / -otīti / -onti = မျက်မှောက်ပြုသည် | မျက်မှောက် ပြုသည် (12 / 8 / 4) | R2: the pi-6 text writes the positive joined «မျက်မှောက်ပြု၏ / …သလော»; pi-5's spaced form is the text's only in the negative (T2) |
| Yattha / yattha = အကြင်နေရာ | (no direct equivalent) (1 / 1) | G1 G8 / G2 O6 |

## Text inconsistencies (for the rails step; the translation was not changed)

T1. Pāli slips in G3 (the Burmese renders the intended word): upapajjissati for uppajjissati (10-06 ^6-10-309),
    uppajjantānaṃ for upapajjantānaṃ (10-11 ^6-10-398), uppajjantīnaṃ for upapajjantīnaṃ (10-03 ^6-10-206),
    anaññātaññāssāmīti (10-01 ^6-10-3), Ghānandriyamūlakaṃ (10-08 ^6-10-336), cavantāna (10-08 ^6-10-361),
    Pacchimacittasamaṅgīna (10-06 ^6-10-314; the module's R8 reads it).
T2. sacchikaroti has two spellings in the text: positive joined «မျက်မှောက်ပြု…», negative spaced «မျက်မှောက် မပြု…» (pi-4
    ^4-17); the pi-5 FINAL mapping has «မျက်မှောက် ပြုသည်». The mapping follows each segment (W6); the rails step may want one
    spacing.
T3. kusalānaṃ / akusalānaṃ / kusalākusalānaṃ (+ uppāda- / bhaṅgakkhaṇe): the text adds the understood dhammānaṃ
    («ကုသိုလ် သဘောတရားတို့၏ ဖြစ်ခြင်း ခဏ၌»; ch9-10a notes); no keyword carries «သဘောတရား» there (the module value «ကုသိုလ် …
    ဖြစ်ခြင်း ခဏ» leaves it out; U2).
T4. The text adds the head noun «အရာ(များ)» after the bare anaññātaññassāmīti and abyākatā («… ဟူသော အရာ», «… မဟုတ်သော
    အရာများ»; harmonise A2); no keyword carries it.
T5. Headings «#### 3 Suddhadhammavāro» / «#### 4 Suddhadhammamūlacakkavāro» (^6-9-4-0, ^6-9-5-0) carry a source digit
    without a dot, so the heading parts do not split as the other headings do (mapped by the table).
T6. The two forms of «yassa cittassa anantarā» (harmonise A1 / B10) both occur in G3: «အကြင်စိတ်၏» (9-01 …, 10-09 …) and
    «မိမိ စိတ်၏» (10-05 … 10-07, 10-12); no G3 keyword is affected (cittassa = «စိတ်», anantarā = «ချက်ချင်း နောက်»).

## Unclear mappings (for review)

U1. anaññātaññassāmīti «မသိရသေးသည်ကို သိရတော့မည်ဟူသော» without the text's head noun «အရာ» (W4); with it the value would be
    the contiguous «… ဟူသော အရာ».
U2. kusalānaṃ uppādakkhaṇe «ကုသိုလ် … ဖြစ်ခြင်း ခဏ» (module compose, kept) against «ကုသိုလ် သဘောတရား … ဖြစ်ခြင်း ခဏ» (the
    understood dhammānaṃ as part of kusalānaṃ; T3).
U3. Abyākatañca dhamme «… မဟုတ်သော … သဘောတရား» (gap over «အရာများနှင့်») against «… မဟုတ်သော အရာ … သဘောတရား».
U4. sacchikarittha «မျက်မှောက် ပြုခဲ့သည်» (4 segments) against «မျက်မှောက်ပြုခဲ့သည်» (12): one keyword, two spellings, because
    the verifier cannot place the joined past against «မျက်မှောက် မပြုခဲ့၊»; phase 3 could add that ending (neg-infix with the
    «သည်» of «…ခဲ့သည်» standing for «၊ / သလော») and use the joined form throughout.
U5. Aṭṭhamako / Aṭṭhamakañca «အဋ္ဌမ» follows pi-5 (binding, as G2 U5) although the text says «အဋ္ဌမ ပုဂ္ဂိုလ်».
U6. vattamāne «ဖြစ်နေသော» (pi-5) against the text's «ဖြစ်နေစဉ်» (ending rule «စဉ်»), as G2 U7.
U7. sa-X-ka «X ရှိသော» and ñāṇasampayuttānaṃ «ဉာဏ်နှင့် ယှဉ်တွဲသော» by the ending rule against the text's «… ရှိလျက် /
    … ယှဉ်တွဲလျက်» (as G1 U2).
U8. Yamakapakaraṇaṃ includes «ကျမ်း» (pakaraṇa, as pi-2); without it the title «အတွဲလိုက် မေးဖြေခြင်း» (the FRAME
    Yamakapāḷi value).
