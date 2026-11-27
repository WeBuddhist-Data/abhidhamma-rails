# pi-5 Burmese keyword mapping: text inconsistencies, consistency scan, S1 review (phases 1–3)

Phase 1 (preamble, 1-puggalakatha) wrote §E–§G; phase 3 (2026-11-21, whole book) wrote §A–§D. The translation was not
changed. Burmese only from this track's FINAL pi-5 text, my5-zeroshot-terms.md and the final pi-1 … pi-4 mappings;
pi-1-my … pi-4-my were only read. Files of phase 3: `phase3-changes.tsv` (every changed value with its reason),
`scan-after-kept.tsv` (every keyword that keeps more than one value, with its category), `work/scan-before.tsv` /
`work/scan-after.tsv` (+ `-detail.txt`), `work/stem-uniq.txt` / `work/stem-uses-after.tsv` (S1 list), helpers
`work/map_scan.py`, `work/scan_classify.py`, `work/scan_minor.py`, `work/scan_kept.py`, `work/stemlist.py`,
`work/stemcheck.py`, `work/diff3.py`, `work/reasons.py`, `work/verify_all.py`, `work/runall.sh`.

## A. Text inconsistencies for the rails step (merged: phase 1 §A, notes-ch2-15, notes-ch16-31, phase-3 scan)

1. **uddāna and saṃkhitta share one word.** «(Saṃkhittaṃ)» = «(အကျဉ်းချုပ်)» (ch1 ^5-53 … ^5-238) and «Tassuddānaṃ» =
   «ထို၏ အကျဉ်းချုပ်» (all 23 vagga uddānas); peyyāla «အကျဉ်းချုံ့ချက်» (^5-238) a third close form. Mapped as the text has
   them.
2. **nicca / dhuva in one list** (^5-238): niccabhattaṃ «အမြဲ ထမင်း», dhuvayāgū «အမြဲ ယာဂု» against «niccā dhuvā
   sassatā» = «မြဲသော၊ ခိုင်ခံ့သော၊ ထာဝရ တည်မြဲသော» in the same segment.
3. **taṇhā / rāga.** ^5-75 «taṇhāsaṃyojanānaṃ» = «တဏှာ နှောင်ကြိုး», elsewhere taṇhā «တပ်မက်မှု» (18 uses); rāga is
   «ရာဂ» (56) but «တပ်မက်မှု» in ch21 (asātarāga ^5-21-8-1-0, ^5-675, ^5-685), «တပ်မက်မှု» being taṇhā's word.
4. **hita / attha in one sutta** (^5-230 «… atthāya hitāya sukhāya …» «အကျိုး … စီးပွား», hitāya «အကျိုးစီးပွား» and
   «အကျိုး»; attahitāya «မိမိ၏ အကျိုး»).
5. **añña**: «Aနှင့် Bသည် တခြားစီ» (the frame) / «… တခြား» without «စီ» (^5-78, ^5-80) / «အခြား» (^5-89, ^5-116).
6. **suddha / kevala share «သက်သက်»** (^5-233, ^5-235) while Suddhasaccikaṭṭho = «ရိုးရိုး …».
7. **sandhāvataṃ saṃsarataṃ** (^5-75) «ကူးသွား ကျင်လည်နေကြသော»: two participles, one ending.
8. **gati**: the heading «Gatianuyogo» «လားရာကို စစ်ဆေးမေးမြန်းခြင်း» against pi-2 «လားရာ ဘဝ» (termbase).
9. **The «said» verbs** «ဟောတော်မူသည် / ပြောခဲ့သည် / လျှောက်ခဲ့သည်» by speaker (by design, harmonise B5; no change).
10. **Spacing of the same word**: sacchikaroti «မျက်မှောက်ပြုသူ» (^5-194) vs «မျက်မှောက် မပြုသူ»; paṇidahantassa «ဆု
    တောင်းသော» (ch17, 22, 26) vs «ဆုတောင်း…» (ch15); ābhoga «စိတ်ညွတ်» (ch15) vs «စိတ် ညွတ်» (ch17); iṭṭhā / kantā
    «…ဖွယ်ကောင်းသော» (ch10) vs «…ဖွယ် ကောင်းသော» (ch16); dvipadānaṃ «ခြေနှစ်ချောင်း» (^5-799) vs «ခြေ နှစ်ချောင်း»
    (^5-872). Values follow each segment's spelling.
11. **^5-371 omission**: «Aṭṭhamako puggalo duppañño elamūgoti? Na hevaṃ vattabbe…pe…» has no Burmese (duppañño,
    elamūgo = (no direct equivalent)).
12. **dhammacakka**: ch3 ^5-270 / ch26 «ဓမ္မစကြာ» vs ch12 ^5-405 «တရားစက်».
13. **ruhiruppādaka**: ch3 ^5-269 «… သွေးကို ထွက်စေသူ» vs ch10 ^5-333 «… သွေးကို စိမ်းစေသူ».
14. **The jāta / niruddha series** of the same Pāli lists: ch5 ^5-283 / ^5-284 and ch17 «မဖြစ်သေး / ကင်းကွာပြီး / ကွယ်ပြီး /
    လုံးဝ ကွယ်ပြီး» vs ch7 ^5-299 / ^5-300 and ch27 «မမွေးဖွားသေး / ကင်းပျောက်ပြီး / ကွယ်ပျောက်ပြီး / လုံးဝ
    ကွယ်ပျောက်ပြီး» (vigataṃ, atthaṅgataṃ, abbhatthaṅgataṃ; sañjātaṃ «ကောင်းစွာ မွေးဖွားပြီး» ^5-300).
15. **parinibbuta**: «ပရိနိဗ္ဗာန် ပြုပြီး» (ch1), «… ပြုတော်မူပြီ» (^5-281), «… စံဝင်တော်မူပြီး» (^5-296), «… ပြုတော်မူခဲ့»
    (^5-802, ^5-896).
16. **thera**: «မထေရ်» (^5-264, ^5-389, ^5-423) vs «ထေရ်» (^5-346 «ဂဝမ္ပတိ ထေရ်»).
17. **Spelling «ယောက်ျား» / «ယောကျ်ား»**: «ယောကျ်ား» in ch12 ^5-402, ch15 ^5-491, ch16 ^5-514, ^5-539; «ယောက်ျား» in ch1,
    ch22 ^5-708 and elsewhere.
18. **paṭikuṭṭha**: ch5 ^5-296 «မကန့်ကွက်အပ်ကြ» vs ch15 ^5-480 «မကဲ့ရဲ့အပ်ကုန်» (the same formula).
19. **sukhadukkha**: «ချမ်းသာနှင့် ဆင်းရဲ» (ch1) vs «ချမ်းသာ ဆင်းရဲ» (^5-488, ^5-539) vs «သုခ ဒုက္ခ» (^5-801); «သာယာမှု
    နာကျင်မှု» (^5-742, the feelings: correct there).
20. **nirodhadhamma**: «ချုပ်ငြိမ်းတတ်သော သဘော ရှိ» (ch1, 3, 25, 31) vs «ချုပ်ငြိမ်းခြင်း သဘော ရှိ» (ch10) in the same stock
    phrase «yaṃ kiñci samudayadhammaṃ …».
21. **Vagga headings and ordinals**: «Catutthavaggo / Chaṭṭhavaggo / Sattamavaggo» repeated on every kathā heading line (11
    each); the ordinal spellings follow the text (ဒသမ, ဧကာဒသမ … တေဝီသတိမ). No change.
22. **The siglum «(Sabbattha)»** stays Roman in the Burmese bracket ^5-525.
23. **iṭṭha / aniṭṭha**: «လိုလားဖွယ်» (ch1, 10, 15), «လိုလားဖွယ် ကောင်းသော» (^5-512), «လိုလားအပ်သော» (ch18 ^5-591).
24. **parinipphanna**: «ပြည့်စုံစွာ ဖြစ်ပေါ်ပြီး» (ch19), «အမှန်တကယ် ဖြစ်ပေါ်ပြီး» (ch23), «ပြည့်စုံစွာ ပြီးမြောက်» (ch31).
25. **upacaya**: kammūpacaya «ကံ၏ စုဆောင်းမှု» (ch23) vs puññūpacaya «ကောင်းမှု စုဆောင်းခြင်း» (ch25, puññasañcaya ch28).
26. **The same sutta passage in two wordings**: «sañcetanikānaṃ kammānaṃ … apare vā pariyāye» (^5-635 vs ^5-782); the
    arahant list ^5-778 (ch25) «စုပုံ / ဖြန့်ကြဲ / ဖြိုဖျက်» vs ^5-894 (ch30) «စုစည်း / ဖြန့်ကျက် / ဖျက်ဆီး»; saṃvattaniya
    «ရောက်စေတတ်သော» (^5-777) vs «ပို့ဆောင်တတ်သော» (^5-894, ^5-903); āneñja «မတုန်လှုပ်သော» vs «မတုန်မလှုပ်သော»;
    sobhagya «ကောင်းသော ကံကြမ္မာ» vs «ကောင်းကျိုး ချမ်းသာ».
27. **The ten-crimes list** ^5-784 (ch25) vs ^5-901 (ch30) / ^5-908 (ch31) and ch10 ^5-314: pisuṇaṃ «ကုန်းတိုက်သော စကား» vs
    «ကုန်းချောစကား»; samphaṃ «အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား» vs «အကျိုးမဲ့ စကား»; nillopaṃ «ဓားပြ / ဥစ္စာ / လုယက်»;
    paripanthe tiṭṭheyya «စောင့်ဆိုင်းလုယက် / ဓားပြ တိုက်»; ekāgārikaṃ «အိမ်တစ်အိမ်တည်းကို ဝိုင်းဝန်း၍» vs «အိမ်တစ်လုံးကို
    ဝိုင်းဝန်း»; bhojanīyaṃ «ဘောဇဉ်» vs «စားဖွယ်»; asuci «မစင်ကြယ်သော သုက်ထွက်ခြင်း» (^5-535) vs «မစင်ကြယ်သော သုက်».
28. **purisayuga** «လူ အတွဲ» (ch1) vs «လူ အစုံ» (^5-791); **āpāyiko / nerayiko** «… ရောက်သူ / … ကျသူ» (^5-657) vs «…
    ရောက်မည့် / … ကျမည့်» (^5-861); (kāraṇikā «ညှဉ်းပန်း နှိပ်စက်သူ» / «လေ့ကျင့်ပေးသူ»: two senses, correct).
29. **«mātaraṃ jīvitā voropetvā»** (^5-857 … ^5-859) = «အမိကို သတ်၍» (jīvitā not rendered) vs ch20 ^5-641 «jīvitā
    voropito» «အသက်မှ ချခံရ».
30. **^5-918 uddāna «Mahāniyāmo»** = «ကြီးမားသော အစု၊ သေချာသော လမ်းကြောင်း» (the compound split into two items).
31. **brahma(cariya)** «မြင့်မြတ်သော (အကျင့်)» (ch3, 9, 12, 25; 23 uses) vs «မြတ်သော (အကျင့်)» (ch10, 3 uses) (phase-3 scan).
32. **arahattasacchikiriyāya** «ရဟန္တာ ဖိုလ်ကို မျက်မှောက်ပြုရန်» (ch11–13, 9) vs «ရဟန္တာ အဖြစ်ကို …» (ch3, 10, 13, 4) for the
    same formula; arahatta / arahattaṃ / arahatte likewise «ရဟန္တာ အဖြစ်» / «ရဟန္တာ ဖိုလ်» (phase-3 scan).

32 items: the 32 entries of phase 1 (10), notes-ch2-15 (11) and notes-ch16-31 (11), less 4 joined duplicates (the
«ယောက်ျား» spelling, dhammacakka, the vagga headings / ordinals, the spacing of dvipadānaṃ into item 10), plus 4 from the
phase-3 scan (items 10 and 14 widened; items 31, 32 new; item 3 widened with rāga).

## B. Book-wide consistency scan (32 *.mapped.md; model pi-4-my/mapper-my/map_scan.py)

`work/map_scan.py` (first letter case-insensitive) — **before** (phase-2 files, `work/phase2-mapped/`): 5,470 keywords,
**501 with more than one value**; **after** phase 3: 5,470 keywords, **483 with more than one value**.

Method: for every keyword with more than one value, `work/scan_minor.py` lists each use whose value is not the
keyword's most frequent value although the segment also has the most frequent value as a phrase (outside the use's own
words): 255 such uses (120 keywords) before the alignment, 173 (90 keywords) after. Every one of the 120 was reviewed
by hand (Pāli and Burmese of the segment); `work/scan_classify.py` / `work/scan_kept.py` classify the rest.

### Aligned (rule; 54 values, phase3-changes.tsv «SC» 29 / «SC-katha» 25; also G5 2 and bhedako 2, counted as G5 / S1)

- **A1 kathā headings** (25 uses, ch2–15): «X … ဆွေးနွေးချက်» → the text's «Xအကြောင်း ဆွေးနွေးချက်» as in ch16–31 (53 uses)
  — rule 1 (the inner «အကြောင်း» stays), rule 10 (« … » only for discontinuous parts); module `kathā_heading()`.
- **yoni** (5, ch11 / ch14) «ဘဝ» → «မွေးဖွားရာ အမျိုးအစား»: in the list «bhavo gati … yoni» «ဘဝ» is bhavo's word (the
  pi value was present only as bhavo's); module STOCK.
- **atta** of attabhāva (5, ch11 / ch14) (no direct equivalent) → «ကိုယ်» (pi-2 decision 4, as ch16–31; module @atta).
- **Q1** pajahitvā / visinitvā / apacinitvā (^5-268) «Xပြီး၍» → «X၍».
- **rule 1** dhammapade «“ဓမ္မပဒ”၌» → «“ဓမ္မပဒ”» (^5-231, ^5-872; module STOCK); abbokiṇṇaṃ «ကြားမလပ်ဘဲ» → «ကြားမလပ်» (^5-548).
- **Q8 / rule 3** sabbaññū «… သိသူ» → «… သိသော» (^5-804); sampajāno «… ဆင်ခြင်သိမြင်ခြင်း ရှိသူ» → «… ဆင်ခြင်သိမြင်သော»
  (^5-371).
- **pi-1 … pi-4 binding** Abhabbo «မထိုက်တန်သော» → «မထိုက်တန်» (^5-641).
- **S6** anupalitto «လိမ်းကျံသော» → «မလိမ်းကျံသော» (^5-405, as ^5-803).
- **one sense per segment, the first**: sacchikato and its three compounds at ^5-366 «မျက်မှောက် ပြုရသေးသော» →
  «… မျက်မှောက်ပြုပြီးသော» (the text «… မျက်မှောက်ပြုပြီး၍» first); buddha ^5-333 (buddhasāsane) «မြတ်စွာဘုရား» →
  «ဘုရား»; methunaṃ dhammaṃ ^5-310 / ^5-387 «မေထုန် … သဘော» → «မေထုန် အကျင့်» (the text's phrase, as ch30 / ch31).
- **Q3 / G2** anāgatāya / paccuppannāya buddho (^5-399) «ဘုရား … X» → «X … ဘုရား».
- (with S1, §C) bhedako «ခွဲသူ» → «သင်းခွဲသူ» (^5-334, ^5-350, as ch16–31); G5 no paccuppannaṃ paccuppannaṃ (^5-295)
  «ပစ္စုပ္ပန်သည် ပစ္စုပ္ပန် မဟုတ်», Rūpena rūpaṃ (^5-826) «ရုပ်ဖြင့် ရုပ်».

### Kept (483 keywords; category per keyword in `scan-after-kept.tsv`)

| category | keywords | of which reviewed by hand (top value also in the segment) | why kept |
|---|---|---|---|
| sense | 253 | 35 | different words: another sense or construction of the keyword, one sense per segment by the first in the Pāli (dhamma «သဘောတရား / တရား / အရာ / ဓမ္မ», rūpa(ṃ) «ရုပ် / သိမ်မွေ့သော ရုပ် / အဆင်းအရောင်», dukkha / sukha senses, eva «ပင် / သာ», saha «အတူ / တစ်ပြိုင်နက်», phala «ဖိုလ် / အကျိုး / အသီးအပွင့်», micchā, jāti, magga, dhātu, para, eka …), or the text's own different word for the same sense (§A) |
| form | 150 | 22 | the same word with another ending / spacing / an added word, as the text has it in that segment (participle vs perfect «ရောက်သော / ရောက်ပြီးသော», noun vs attributive, the text's spacing §A 10, «ရဟန္တာ / ရဟန္တာ အဖြစ်» person vs state) |
| construction | 53 | 27 | the same members glued with the segment's particle (rule 1) or separated « … » / in another order (rule 10, Q3 / G2, mechanic 2): each segment's own construction |
| none | 27 | 6 | (no direct equivalent) in some segments: pi-2 decision 4 (one word, one member: jano, aṅga, sañña, bhāvo …), M2 (only in a Roman variant: karonti ^5-868 …), Q7 (relative pronouns), one Burmese verb for two keywords (jīvitā ^5-857 …) |

The 90 reviewed keywords and their decision (all kept): construction (27: the glued value is the segment's own
phrase, or the text has the members only across «…»: arahato bhāvito ^5-319 / ^5-323; kilese jahati, puggalo
upalabbhati / sandhāvati, dakkhiṇaṃ …, niyāmaṃ okkam…, kusala(mūla)ṃ …, saṅgho dakkhiṇaṃ …, soḷasa sahassāni …);
sense (35: as the table above; akāsi / gacchati ^5-918 the uddāna's own verbs; okkamituṃ one Burmese verb with
abhabbo; nillopaṃ §A 27; paññāpeti ^5-236 ch1's «ပညတ်သည်»; seṭṭho / uttamo ^5-799 the verse's words; upapattiyā
«saha upapattiyā» rendered as a clause; vata «အကျင့်ဝတ်» of sīlabbata); form (22: Appaṇihito ^5-832 a noun like
suññatā / animitta in that list; samannāgata a heading noun; niyato ^5-644 the pi-4 value; pahīyanti / saṃyojanā
pahīyanti the text's passive; vimuttaṃ / pattā / upagaṃ the text's participle; samphaṃ the member of samphappalāpa);
none (6: sañña, vaccha, patto ^5-387, karonti, jīvitā, vata ^5-377 as phase 2).

## C. S1 review (stem fallback, group rule S1 of ch2–15; now the module's `make_stem()`)

The stem fallback is used only in ch2–15 (ch1 and ch16–31 map every keyword before it). Phase 2 had 726 uses; after
the module consolidation 721 uses = **411 distinct keyword=value pairs** (`work/stem-uniq.txt`), every pair checked
against its segments' Pāli and Burmese (`work/stemcheck.py`):

- **corrected 19 pairs (30 uses + 1 composed value that follows)**, by rule: carita «အကျင့်» → «ကျင့်ပြီးသော» (rule 3, 4);
  okkanta «သက်ဆင်းသည် / သက်ဆင်းခြင်း» → «သက်ဆင်းပြီးသော / သက်ဆင်းသော» (rule 3, 4); pariyāye «စိတ်ကို ပိုင်းခြား၍» →
  «ပိုင်းခြား၍ သိသော» (5); paṭilābhā «ရသော» → «ရခြင်း» (2); bhedako «ခွဲသူ» → «သင်းခွဲသူ» (2); bodhiyā ^5-417
  «ဘုရားလောင်း» → «ဗောဓိ» (+ bodhiyā buddho «ဗောဓိဖြင့် ဘုရား»); passanto «မြင်သည်» → «မြင်နေသော» (S5); samāpajjeyya
  «ဝင်စားနေသော» → «ဝင်စားနေသည်» (rule 4); uppajja «ဖြစ်ပေါ်သည်» → «ဖြစ်ပေါ်၍»; ṭhitā «တည်ရှိခြင်း» → «တည်သော»; ṭhiti
  ^5-455 «တည်သော» → «တည်ရာ»; sakavādi «မိမိ» → «မိမိဘက်»; sahajātā ^5-476 «အတူ» → «အတူ ပေါ်ပေါက်သော»; vedaniyā /
  vedaniyaṃ «ခံစားမှု» → «ခံစားမှုကို ဖြစ်စေတတ်သော»; haraṇo «ဆောင်သည်» → «ယူဆောင်နိုင်သော» (rule 8); upapattiyā ^5-378
  «ပြန်လည် ဖြစ်ပေါ်သော» → «ပြန်လည် ဖြစ်ပေါ်ခြင်း»; uppādā ^5-383 «ဖြစ်ပေါ်သော» → «ဖြစ်ပေါ်ခြင်း». The corrections are
  table / CTX entries in map_ch2-15.py («phase 3 S1 review»).
- **kept 392 pairs (691 uses)**: the value is the keyword's sense and the segment's word in the rule form (inflected forms
  of a mapped stem: anāgāmiphalena «အနာဂါမိဖိုလ်», cetanāhi «စေ့ဆော်မှု», sotāpattimaggo «သောတာပတ္တိမဂ်» …; compound
  members carrying their part of the text's phrase: kaṭṭhavanappatīnaṃ «ထင်း … သစ်ပင်», kāriyaṃ «အကျင့်» of
  dukkarakāriyaṃ; fragments of a negative compound = the positive part, rule 8: aniccato «မမြဲ», attato «အတ္တ», niccaṃ
  «မြဲသော», subhaṃ «တင့်တယ်သော»). The least certain kept ones: upapattiyā «saha upapattiyā» «ပြန်လည် ဖြစ်ပေါ်သော» (the
  text's clause «… ဖြစ်ပေါ်သည်နှင့်»), vārivahā «ရေ», sayambhū «ကိုယ်တိုင်».

S1 is approved after this review (coordinator decision of 2026-11-21) and stays the last fallback of the module's
lookup (`Mapper(stem=make_stem(tables))`, used by map_ch2-15.py).

## D. Module consolidation (task 1)

- Moved into `map5_rules.py` (STOCK / FUNCS «phase 3» blocks; the group tables no longer carry them): parinibbāyī
  «ပရိနိဗ္ဗာန် ပြုသော» (Q8); parinibbuto, parinibbute, thero, sukhadukkhaṃ, nirodhadhammaṃ, rāga / rāgo, samāpatti,
  nirodho / nirodhaṃ (tuples: the text's form per segment, `alt()`); aññā (sammadaññā «သိ၍», aññāpaṭivedha «ရဟန္တာ
  ဖိုလ်»); aṅga / aṅgo / aṅgaṃ / aṅgā / aṅgānaṃ (bojjhaṅga member, by the first aṅga compound); antarikā «အကြား ကာလ»;
  bhāvito / bhāvitā «ပွားများထားသော»; dhammo (@dhammo); magga / maggo / maggaṃ (@magga); dhātū (@dhatu_plane); dukkhā
  (@dukkha); jano / janassa (@jana); sukha_loan («သုခ», named by the ch24 / ch25 tables); and from the scan atta, yoni,
  dhammapade. Single-segment forms stay CTX rules in the chapter scripts. These moves changed no value by themselves
  (one CTX was needed: ^5-485 dhammo «တရား»).
- The three mechanics: `negate()` checks a gapped negative «S … မV» part by part (was one literal phrase); `glue()` does
  not glue a verb through the verbal noun «…ခြင်း» (M2, 11 values; the CTX ^5-239 «Parihāyati arahā» is no longer
  needed); `phrase_present()` accepts the perfect predicate «Xပြီး ဖြစ်» (M3, 27 values).
- Book-wide rules now in the Mapper: S1 (`stem=`), S3 / G3 (`internal_neg` + `negate`), G1 / G2 (`pali_order`), G5 by
  table. **G2 made exact** (phase 3): «the text has the members in that order» = within one clause (no «။ … – “ ”»;
  for a bare adjacency also no «၊»), the X not inside Y's own words, and an attributive «…သော X» adjacency stays.
  Applied to ch1–15 this gave 44 values in the Pāli order (G2); in ch16–31 it undid 7 phase-2 reorderings that went
  across a clause or through «ရုပ်» inside «ရုပ်မရှိသော» (G2r). The frame «aññaṃ X añño puggalo» of ch1 keeps Q3 by table
  entries (aññaṃ rūpaṃ / aññaṃ viññāṇaṃ).
- Values changed in all (phase3-changes.tsv, 177): task 1 — G2 44, M3 27, M2 11, G2r 7, OV 1 (= 90); task 2 — S1 31; task
  3 — SC 29, SC-katha 25, G5 2 (= 56). Every change has its reason; `work/reasons.py` refuses an unexplained one.

## E. Keyword ambiguities (phase 1, how they were settled)

- **aṭṭha**: «thing» (saccikaṭṭha = «အမှန်တကယ် အရာ») vs «eight»; FRAME @attha_thing.
- **aññā**: «other» (fem.) vs «final knowledge» (aññindriya, aññātāvī «အပြည့်အဝ သိမြင်…»); f_anna_f by the first in the
  Pāli (phase 3: also sammadaññā «သိ၍», aññāpaṭivedha «ရဟန္တာ ဖိုလ်»).
- **upādā**: «မှီ၍» vs the fragment of anupādā(parinibbāna) = the positive part «စွဲလမ်းမှု» (rule 8).
- **vādī**: the speakers of the note «[… sakavādī/paravādīpucchā …]» = «မိမိဘက် / တစ်ဖက်သား» vs the epithets «…
  ဆိုတော်မူသော» (Q8).
- **micchā**: verdict «မှားသည်» / «idaṃ te micchā» «အမှား» / compound «မှားယွင်းသော»; one sense per segment (first).
- **vata**: «vata re» «အမှန်ပင်» vs the vow «အကျင့်ဝတ်»; the exclamation «Ime vata bhonto sattā» (^5-377) (no direct
  equivalent).
- **Tena hi**: «သို့ဖြစ်လျှင်» vs «သို့ဖြစ်၍» (first in the text).
- **dhātuyā / rūpa / rūpaṃ / sukha / dukkha / para / purisa / yo yaṃ yena / hevameva / suniggahitova** and the extractor
  fragments: as phase 1 (FRAME / STOCK functions; ^5-122 CTX).

## F. Unclear mappings left (for review; merged from phase 1 §C, notes-ch2-15, notes-ch16-31, phase 3)

1. satasahassa «သိန်း» (^5-239): sahassehi = «သိန်း», sata = (no direct equivalent).
2. sukkavissaṭṭhiṃ (^5-308) «သုက်», vissaṭṭhiṃ = (no direct equivalent).
3. Taññeva «ထို … ပင်»; sabbena sabbaṃ «လုံးဝ» (both members one word).
4. bhabba / abhabba «ထိုက်တန်သော / မထိုက်တန်» (pi) vs the text's «…နိုင်» (ch3 ^5-269, ch13); abhabbo … okkamituṃ
   (^5-661) = (no direct equivalent) + «မသက်ဆင်းနိုင်».
5. samāpanna with a separate jhāna / samāpatti keyword: «သမာပတ်ကို ဝင်စားနေသော» includes the object.
6. Verse words akkhāsi / bhonto / vediyā; mā (^5-622) «မ».
7. nillopaṃ hareyya / hātabbaṃ / haranti (ch30, ch31) = nillopaṃ «လုယက်», the verb (no direct equivalent).
8. manasikārā «နှလုံး သွင်း» (^5-576), katānaṃ «ပြုခဲ့», niruddhaṃ «ချုပ်ငြိမ်းပြီး» (^5-820): bare stems where the text has
   no ending; apahattā / upahattā (^5-748) rendered as verbs; viharituṃ / iddhiyā paggahetuṃ / vādeti bare stems.
9. satta rattindivāni (^5-626) «ခုနစ်» + «ရက် … ညဉ့်».
10. sañña / satta / sattānaṃ of asaññasatta = «အသညသတ်» for one member; pana ^5-884, bhāvo / bhāva of attabhāva =
    (no direct equivalent).
11. Kappaṭṭho «ကမ္ဘာ ပတ်လုံး တည်ရမည့်သူ» and the person types as names (P1).
12. dha = the reference sigla (ch1 «“ဓမ္မပဒ”», ^5-887 «သဘောတရားများကို စုစည်းရေတွက်ခြင်း»).
13. sassato: adjective «ထာဝရ တည်မြဲသော» vs the view clause «ထာဝရ တည်မြဲသည်» (f_sassato).
14. Phase 3: upapattiyā in «saha upapattiyā» (^5-388 … ^5-390, ^5-417) «ပြန်လည် ဖြစ်ပေါ်သော» (the text a clause
    «… ဖြစ်ပေါ်သည်နှင့်»); Appaṇihito ^5-832 «တောင့်တမှု မရှိခြင်း» (a noun in that list); arahato bhāvito ^5-319 /
    ^5-323 in text order (the members only across the «…pe…» gaps).

## G. For later runs

`work/runall.sh` runs map_ch1.py, map_ch2-15.py, map_ch16-31.py in that order; `work/verify_all.py` prints the three
checks for all 32 files; `work/diff3.py` + `work/reasons.py` list and explain every change against `work/phase2-mapped/`.
