# pi-6 Burmese zero-shot, group ch9-10a: notes (9-01 / 9-02 / 9-03 Dhammayamaka, 10-01 … 10-04 Indriyayamaka)

Status: all seven chapters generated and checked 2026-11-22. Not committed. Brief: burmese-zeroshot-brief.md.
Source rule kept: translated from the Pāli only; no Burmese translation / nissaya / web source opened
(0-INBOX/temp/language-priority/ not opened), no web search. pi-1 … pi-5 read only through their FINAL rails texts
(witnesses in the generator; kwic6.py lookups) and the locked termbases. Finished pi-6 groups (make_sample.py,
make_ch2-02-4-5.py, make_ch3.py, make_ch6-8.py and their notes) read only, never run; their functions copied.

## Files
- Output (AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters/): 9-01-dhammayamaka.md (170 segments, 509
  lines), 9-02 (143 / 406), 9-03 (72 / 203), 10-01-indriyayamaka.md (166 / 1083), 10-02 (70 / 505), 10-03 (20 / 328),
  10-04 (20 / 222).
- `make_ch9-10a.py` (generator; imports my6_formulas.py unchanged, extends its tables in memory; `--misses`,
  `--frames` prints the frame examples), `check_ch9-10a.py` (per-line check + reuse test; `--mutate`).
- Run: `python3 -I -X utf8 make_ch9-10a.py`, `python3 -I -X utf8 check_ch9-10a.py --mutate`.

## Checks (final run)
- check_chapter_ids / check_text_pe / check_marks: OK for all seven files (my chk-pe copies deleted afterwards).
- check_ch9-10a.py: A 7/7 regenerated identical; B1 3256 lines; B2 4563 negations, each one Burmese negative; B3 4231
  uppajj / nirujjh verbs (root, tense, polarity, double negative, plural «ကြ») + 8 bhāveti / pajahati, 812 answers;
  B4 2181 labelled lines, every «vā pana» = «တစ်ဖန်»; B5 digits + 164 number words; B6 2461 distinct Pāli sentences, one
  Burmese each, checked together with the finished pi-6 chapters (6 shared, identical); B7 208 headings / colophons /
  table lines; B8 36 quoted lines nested right; B9 1044 women / men / attribute occurrences; 0 mismatches.
  Reuse test 13286 / 13286 (C1 22 faculty names 2496/2496, C2 715/715, C3 80 terms 10075/10075). Per chapter:
  9-01 1554/1554, 9-02 1858/1858, 9-03 1046/1046, 10-01 2626/2626, 10-02 2227/2227, 10-03 2367/2367, 10-04 1608/1608.
  6 documented exceptions (anuloma / paccanīka, cavati, Natthi, “သောတ”, uppādakkhaṇe, anaññātaññassāmīti bare word).
- Mutation test: 10/10 caught (dropped «မ», «ခဲ့», «ကြ», «ကား မဟုတ်», «တစ်ဖန်»; tāsaṃ «ထိုမိန်းမတို့» -> «ထိုသူတို့»; changed
  faculty name; changed attribute; «ဟုတ်ပါသည်» -> «မဟုတ်ပါ»; future -> present).

## Method (for the 10-05 … 10-13 agents: tables 1-4 at the top of make_ch9-10a.py)
- TABLE 1: the 22 faculties read from pi-2 ^2-221 (order asserted), bare words = the name without «၏ စွမ်းရည်».
- TABLE 2: indriya person groups. A group = [attributes …] [itthīnaṃ / purisānaṃ] participle; Burmese = the attributes
  in Pāli order joined with a space, then the participle (upapajjantānaṃ / upapajjantīnaṃ «ပြန်လည် ဖြစ်ပေါ်ဆဲ», cavantānaṃ
  «စုတေဆဲ»), then the head «မိန်းမတို့» / «ယောက်ျားတို့» / «…သူတို့». tāsaṃ: «…မိန်းမတို့အား»; «no ca tāsaṃ» and tāsaṃ after a
  final moment «ထိုမိန်းမတို့အား» (tesaṃ «ထိုသူတို့အား»).
- TABLE 3: moment compounds «A(sampa|vippa)yutta…cittassa» = «Aနှင့် ယှဉ်တွဲ၍ / ကင်းကွာ၍ … Zနှင့် ယှဉ်တွဲသော / ကင်းကွာသော စိတ်»
  (+ «၏ ဖြစ်ခြင်း / ပြိုပျက်ခြင်း ခဏ၌»).
- TABLE 4: frame examples (`--frames`).
- Leads: the module's who_my first (sample identity); else the lead parser copied from make_ch2-02-4-5.py (units:
  persons, moments, places; persons joined «A၊ Bနှင့် C», other units «၊ »; final person «အား», final moment «ထိုသူတို့အား»).
- Dhammayamaka: «kusalā dhammā» is read as one subject term (dh_join), except in the suddhadhammavāra questions
  «(Ka) kusalā dhammā?» (two terms: kusalā / dhammā). Plural subjects take «ကြ» on every verb; a bare short answer
  takes the number of its verb form («Uppajjittha.» = the sample's «ဖြစ်ပေါ်ခဲ့သည်။», «Uppajjanti.» = «ဖြစ်ပေါ်ကြသည်။»).
- Paṇṇatti frames copied from make_ch2-02-4-5.py (pannatti2), ch6-8 «X na Y, X.»; «…pe…» lines as make_ch2-02-4-5.py.

## New recurring terms and frames («Pāli = Burmese»)
Reused from FINAL (witnessed at import): the 22 faculties pi-2 ^2-221 («မျက်စိ၏ စွမ်းရည်» … «အပြည့်အဝ သိမြင်ပြီးသူ၏ စွမ်းရည်»),
head «စွမ်းရည် နှစ်ဆယ့်နှစ်ပါး»; indriya «စွမ်းရည်» (pi-1 ^1-1); kusalā / akusalā / abyākatā dhammā (pi-1 ^1-M1-1);
kusalākusalānaṃ dhammānaṃ «ကုသိုလ်နှင့် အကုသိုလ် သဘောတရားတို့» (pi-1 ^1-583), akusalānaṃ dhammānaṃ «အကုသိုလ် သဘောတရားတို့»
(pi-1 ^1-30); ñāṇasampayutta / -vippayutta «ဉာဏ်နှင့် ယှဉ်တွဲ / ကင်းကွာ» (pi-1 ^1-1, ^1-147); -sahagata «နှင့်အတူ» (pi-1
^1-M1-7); vinā «မပါဘဲ» (pi-5 ^5-227); bhāveti «ပွားများ» (pi-5 ^5-390); pajahati «ပယ်» (pi-5 ^5-317); bhāvanā «ဘာဝနာ
ပွားများခြင်း» (pi-1 ^1-M1-8); kāmāvacara / rūpāvacara (place) «ကာမဘုံ / သိမ်မွေ့သော ရုပ်ဘုံ» (pi-1 ^1-M2-93/94); itthī
«မိန်းမ», puriso «ယောက်ျား», somanassa «ဝမ်းမြောက်မှု», upekkhā «ဥပေက္ခာ», saddhā «ယုံကြည်မှု» (pi-2 ^2-219); moments,
pavatte, aggamagga, arahant, nirodhasamāpanna, dutiye (akusale) citte vattamāne, «yassa cittassa anantarā aggamaggaṃ
paṭilabhissanti» exactly as ch2-02-4-5.

NEW (proposed here):
- indriyā (plural) = စွမ်းရည်တို့ (as khandhā «အစုအဝေးတို့»); indriyaṃ = စွမ်းရည်
- bare words: cakkhu မျက်စိ, sotaṃ နား, ghānaṃ နှာခေါင်း, jivhā လျှာ, kāyo ကိုယ်, mano မနော, itthī မိန်းမ, puriso ယောက်ျား,
  jīvitaṃ အသက်, sukhaṃ သာယာမှု, dukkhaṃ နာကျင်မှု, somanassaṃ ဝမ်းမြောက်မှု, domanassaṃ စိတ်ဆင်းရဲမှု, upekkhā ဥပေက္ခာ,
  saddhā ယုံကြည်မှု, vīriyaṃ ဝီရိယ, sati သတိ, samādhi သမာဓိ, paññā ပညာ, aññaṃ အပြည့်အဝ သိမြင်ခြင်း, aññātāvī အပြည့်အဝ
  သိမြင်ပြီးသူ (all = the pi-2 name without «၏ စွမ်းရည်»; cakkhu … mano identical with the dhātu / āyatana chapters)
- anaññātaññassāmīti (bare word) = “မသိရသေးသည်ကို သိရတော့မည်”
- sa-X-ka / a-X-ka attributes: sacakkhuka မျက်စိ ရှိလျက် / acakkhuka မျက်စိ မရှိဘဲ; sasotaka / asotaka နား …; saghānaka /
  aghānaka နှာခေါင်း …; sacittaka / acittaka စိတ် …; sahetuka / ahetuka အမြစ် ရှိလျက် / အမြစ် မရှိဘဲ (as ch. 3 / ch2-02-4-5)
- na itthīnaṃ = မိန်းမ မဟုတ်ဘဲ; na purisānaṃ = ယောက်ျား မဟုတ်ဘဲ (attributes); itthīnaṃ … upapajjantīnaṃ = … ပြန်လည် ဖြစ်ပေါ်ဆဲ
  မိန်းမတို့; purisānaṃ … upapajjantānaṃ = … ပြန်လည် ဖြစ်ပေါ်ဆဲ ယောက်ျားတို့
- tāsaṃ = (…မိန်းမတို့)အား; no ca tāsaṃ = သို့သော် ထိုမိန်းမတို့အား
- somanassena = ဝမ်းမြောက်မှုနှင့်အတူ; vinā somanassena = ဝမ်းမြောက်မှု မပါဘဲ; upekkhāya = ဥပေက္ခာနှင့်အတူ; vinā upekkhāya =
  ဥပေက္ခာ မပါဘဲ
- ñāṇasampayuttānaṃ = ဉာဏ်နှင့် ယှဉ်တွဲလျက်; ñāṇavippayuttānaṃ = ဉာဏ်နှင့် ကင်းကွာလျက် (attributes before the participle)
- X-sampayutta- / X-vippayuttacittassa = Xနှင့် ယှဉ်တွဲသော / ကင်းကွာသော စိတ်၏ (X: kusala, akusala, saddhā, somanassa, upekkhā,
  ñāṇa); two members «Aနှင့် ယှဉ်တွဲ၍ Bနှင့် ကင်းကွာသော စိတ်» (e.g. kusalavippayuttaakusalavippayuttacittassa = ကုသိုလ်နှင့်
  ကင်းကွာ၍ အကုသိုလ်နှင့် ကင်းကွာသော စိတ်၏)
- kusalānaṃ (uppādakkhaṇe) = ကုသိုလ် သဘောတရားတို့၏; akusalānaṃ = အကုသိုလ် သဘောတရားတို့၏; kusalākusalānaṃ = ကုသိုလ်နှင့်
  အကုသိုလ် သဘောတရားတို့၏ («dhammānaṃ» understood, as pi-1)
- Dhammayamaka pavatti: yassa kusalā dhammā uppajjanti tassa akusalā dhammā uppajjantīti? = အကြင်သူအား ကုသိုလ် သဘောတရားများ
  ဖြစ်ပေါ်ကြ၏၊ ထိုသူအား အကုသိုလ် သဘောတရားများ ဖြစ်ပေါ်ကြသလော။ (every verb with a plural subject «…ကြ…»: ဖြစ်ပေါ်ကြသည် /
  ဖြစ်ပေါ်ခဲ့ကြသည် / ဖြစ်ပေါ်ကြလိမ့်မည်; မဖြစ်ပေါ်ကြ / မဖြစ်ပေါ်ခဲ့ကြ / မဖြစ်ပေါ်ကြလိမ့်မည်; double negative «မဖြစ်ပေါ်ကြသည်ကား မဟုတ်»)
- Dhammayamaka paṇṇatti: bare kusalā = ကုသိုလ်; akusalā = အကုသိုလ်; abyākatā = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော အရာများ
  (the adjective needs a noun); dhammā = သဘောတရားများ; Kusalaṃ ṭhapetvā = ကုသိုလ်ကို ချန်ထား၍; (Ka) kusalā kusalā dhammā? =
  ကုသိုလ်သည် ကုသိုလ် သဘောတရားများ ဖြစ်ကြသလော။; (Ka) kusalā dhammā? (suddha) = ကုသိုလ်သည် သဘောတရားများ ဖြစ်ကြသလော။
- bhāvanāvāra: yo kusalaṃ dhammaṃ bhāveti so akusalaṃ dhammaṃ pajahatīti? = အကြင်သူသည် ကုသိုလ် သဘောတရားကို ပွားများ၏၊
  ထိုသူသည် အကုသိုလ် သဘောတရားကို ပယ်သလော။; na bhāveti = မပွားများ; nappajahati = မပယ်
- Yaṃ X indriyaṃ taṃ Xñceva indriyañca. = အကြင်Xသည် စွမ်းရည် ဖြစ်၏၊ ထိုXသည် Xလည်း ဖြစ်၊ စွမ်းရည်လည်း ဖြစ်သည်။ (yaṃ / yo / yā
  «အကြင်», taṃ / so / sā «ထို», as ch6-8 «အကြင်စိတ်»); Avasesaṃ / Avaseso X na Y. = ကြွင်းကျန်သော Xသည် Y မဟုတ်။
- Headings: Suddhadhammavāro = ရိုးရိုး သဘောတရား ဖော်ပြချက်; Suddhadhammamūlacakkavāro = ရိုးရိုး သဘောတရားကို အခြေခံ၍
  လှည့်ပတ်ခြင်း ဖော်ပြချက် («3 …» / «4 …» with the source digit); Suddhindriyavāro = ရိုးရိုး စွမ်းရည် ဖော်ပြချက်;
  Suddhindriyamūlacakkavāro = ရိုးရိုး စွမ်းရည်ကို အခြေခံ၍ လှည့်ပတ်ခြင်း ဖော်ပြချက်; Bhāvanāvāro = ဘာဝနာ ပွားများခြင်းအလိုက်
  ဖော်ပြချက် (colophon «Bhāvanāvāro.» + «။»); Pavattivāro = ဖြစ်ပျက်ခြင်းအလိုက် ဖော်ပြချက်; Uppāda- / Nirodha- /
  Uppādanirodhavāro as ch6-8 / ch2-02-4-5
- (Xindriyamūlakaṃ) = (X၏ စွမ်းရည်ကို အခြေခံ၍) (as ch. 3 «(… နယ်ပယ်ကို အခြေခံ၍)»)

## Choices for the reviewer / the consistency pass
1. Plural «ကြ» with the Dhammayamaka subjects (kusalā dhammā …): natural Burmese and the ch. 1 practice (plural
   predicates «…ကြသလော»); the bare short answers keep the number of their Pāli verb form for identity with the sample.
2. tāsaṃ «ထိုမိန်းမတို့အား» (feminine, as the Pāli) instead of the neutral «ထိုသူတို့အား».
3. bare abyākatā «… မဟုတ်သော အရာများ» (an adjective cannot stand alone); kusalā / akusalā stay bare (nouns in Burmese).
4. Lead rule as ch2-02-4-5 (units with «၊ », a final moment + «ထိုသူတို့အား»); ch6-8 attaches a moment to the person
   before it; to be aligned in the consistency pass.
5. Instrumental somanassena / upekkhāya «…နှင့်အတူ» (from -sahagata «နှင့်အတူ ဖြစ်သော»), not «…ဖြင့်».

## Unsure Pāli / meaning
- «Kāyindriyaṃ ṭhapetvā avaseso kāyo, na kāyindriyaṃ» read as «… ကြွင်းကျန်သော အရာသည် ကိုယ် ဖြစ်သည်» (as the dhātu
  chapter in ch2-02-4-5); «avaseso kāyo» could also be read as one subject «the remaining body».
- «Yaṃ sotaṃ indriyaṃ taṃ sotañceva indriyañca» (which ear is a faculty …): literal correlative.
- kusalānaṃ uppādakkhaṇe: «dhammānaṃ» understood («ကုသိုလ် သဘောတရားတို့၏»).
- ñāṇasampayuttānaṃ upapajjantānaṃ: "reborn with (a rebirth consciousness) joined with knowledge"; rendered literally
  «ဉာဏ်နှင့် ယှဉ်တွဲလျက် ပြန်လည် ဖြစ်ပေါ်ဆဲသူတို့».

## Source slips (translated as written, logged)
- 9-01 ^6-9-16: «(Kha) niddeso» as a text line (no «#»): «(ခ) အကျယ် ဖော်ပြချက်» as a text line.
- 9-03 ^6-9-229: «Abhidhammapiṭake» as the last text line (as the preamble frame).
- 10-01 ^6-10-1: variant «[viriyindiyaṃ (sī. syā.)]» (pi-2 «viriyindriyaṃ»): spelling-only label «စာလုံးပေါင်းကွဲ», reading kept.
- 10-01 ^6-10-3: «na anaññātaññāssāmīti» for anaññātaññassāmīti (same Burmese).
- 10-01 ^6-10-100: «Kāyindriyaṃ ṭhapetvā avaseso kāyo na kāyindriyaṃ.» (comma missing): no «၊» before the negative.
- 10-01 ^6-10-140: «Avaseso kāyo na indriyā» (plural; the parallels have «na indriyaṃ»): «… စွမ်းရည်တို့ မဟုတ်။».
- 10-01 ^6-10-105 … : «Āmantā …pe….» with a space before «…»: kept («ဟုတ်ပါသည် …။»).
- 10-03 ^6-10-206: «uppajjantīnaṃ» for upapajjantīnaṃ: read as upapajjantīnaṃ («ပြန်လည် ဖြစ်ပေါ်ဆဲ»).
