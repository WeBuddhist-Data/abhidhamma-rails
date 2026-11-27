# pi-1 Burmese keyword mapping: consistency pass (harmonise) notes

Brief: `map-harmonise-brief.md`. All changes made through the mapping scripts (backed up first in `harmonise-backup/`:
`map_*.py`, `map-table*.md`, and every `*.mapped.md` in `harmonise-backup/mapped/`), then the scripts were re-run.
No mapped file was edited by hand. The sample (`map_all.py`, `map-table.md`, `preamble.mapped.md`,
`1-matika.mapped.md`) is unchanged (byte-identical after re-run). Burmese only from this track's final text; no
other Burmese source was opened. Translation files, 1-SOURCES/, 4-SYSTEM/ and other tracks untouched.

## Numbers

- Values changed: **181** in 11 chapter files (preamble, 1-matika, 2-02: 0).
  2-01: 7 · 2-03: 4 · 2-04: 4 · 2-05: 1 · 3-01: 5 · 3-02: 9 · 3-03: 1 · 4-01: 62 · 4-02: 39 · 4-03: 19 · 5: 30.
- Book-wide scan (`harmonise_map_scan.py`, first letter case-insensitive, all 14 `*.mapped.md`): keywords with more
  than one value **104 before → 95 after** (`scan-before.tsv`, `scan-after.tsv`; contexts per value in
  `scan-after-detail.txt`). Every one of the 95 is a logged, justified difference (table below).
- Values with « / » alternatives: 31 before → 0 after.
- Verification: all 14 chapters `bad []`, presence failures 0 in every script, no «, » / «၊» in any value;
  assembler wrote `AI_translation/burmese/pi-1-keywords-by-reference-pali-burmese-plain.md`, **1916 lines**, every ID
  once, keyword counts unchanged.

## Scripts changed

- `map_4.py` (4-01, 4-02, 4-03): absolutives, rūpa, na, ñāṇaṃ, vipākato, vattabbaṃ; rule 12 and rule 22 rewritten.
- `map_3.py` (3-01..3-03): rūpa / rūpaṃ one sense per segment (f_rupa, f_rupam, rule 13).
- `map_5.py` (5): numerals with «ပါး» (rule 12), asaññā, bhūtā, vipāka, kammassa katattā.
- `map_2-01.py`, `map_2-02-03.py`, `map_2-04-05.py`: nikkhitta one value (rules text updated).
- `map_all.py`: not edited (re-run only, output identical).
- New helpers (read-only on the mapping): `harmonise_map_scan.py`, `harmonise_kw.py`, `harmonise_ctx.py`,
  `harmonise_abs.py`, `harmonise_rupa.py`, `harmonise_map_reasons.py`.

## Decisions applied

1. **Absolutives keep «…၍»** (rule 4 «verb + သည်» = finite verbs only). Only `map_4.py` was an outlier (its old rule
   12 put every non-finite verb in «သည်»). Changed: ṭhapetvā / Ṭhapetvā = ချန်ထား၍ (52), ārabbha = အာရုံပြု၍ (12),
   «X dhamme ārabbha» = «… သဘောတရားတို့ကို အာရုံပြု၍» (8), paṭicca in paṭiccasamuppanna = အကြောင်းတို့ကို မှီ၍ (11),
   upādāya = မှီ၍ (2, was «မှီ၍ ဖြစ်သော»; upādāya rūpaṃ keeps «မှီ၍ ဖြစ်သော ရုပ်» as in 3 and 5), disvā = မြင်၍, sutvā =
   ကြား၍, ghāyitvā = နမ်း၍, sāyitvā = လျက်၍, phusitvā = ထိ၍, viññāya = သိ၍, karitvā = ပြု၍, abhiññā (sayaṃ abhiññā
   sacchikatvā) = ထူးကဲစွာ သိ၍. Where the text's conjunctive is «ပြီး» it stays (the value must be in the text):
   sacchikatvā = မျက်မှောက်ပြုပြီး (3), uppajjitvā («ဖြစ်ပေါ်ပြီးမှ», မှ dropped by rule 1) = ဖြစ်ပေါ်ပြီး (1).
   paṭicca in paṭiccasamuppāda keeps the Mātikā «အကြောင်းအကျိုး ဆက်စပ်» (1-M2-122, 4-03 1-1343). No other script
   had an absolutive in «သည်» (scan `harmonise_abs.py`). Finite verbs inside keywords («ārabbha ye uppajjanti» =
   အာရုံပြု၍ ဖြစ်ပေါ်သည်) unchanged.
2. **«samaye X» = «အချိန်၌ ရှိသော X»**: already true everywhere (2-01, 2-03, 2-04, 2-05; 2-02 has no such keyword).
   Bare «samaye» (2-03) = the noun အချိန် (not a «samaye X» keyword). No change.
3. **rūpa, one sense per segment**: all «ရုပ် / အဆင်းအရောင်» and «သိမ်မွေ့သော ရုပ် / ရုပ်» removed (map_3.py). Sense of
   the FIRST occurrence in the Pāli segment (logged by the script, `rupa one-sense` lines):
   - 3-01 1-584, 1-594: rūpa = သိမ်မွေ့သော ရုပ် (first: rūpāvacara; matter rūpasaṅgaha later).
   - 3-01 1-585, 1-593, U1: rūpa = ရုပ် (first: rūpasaṅgaho; rūpāyatana / rūpadhātu later).
   - 3-02 1-596, 597, 599, 616, 617, 618, 619, 698; 3-03 1-814: rūpaṃ = ရုပ် (first: «Katamaṃ taṃ rūpaṃ …», matter;
     the object seen «rūpaṃ sanidassanaṃ … passati» / «Yaṃ rūpaṃ … vaṇṇanibhā» later).
   - 3-02 1-656 «Katamaṃ taṃ rūpaṃ sanidassanaṃ?» = ရုပ် (the question head «မြင်နိုင်သော ရုပ်» is matter, not the
     object seen; the old value was «ရုပ် / အဆင်းအရောင်»).
   - 4-01 1-1065, 1-1141, 4-02 1-1236 (lobha list): rūpa = အဆင်းအရောင် (was ရုပ်): its first rūpa compound is rūpāsā
     «အဆင်းအရောင်ကို မျှော်လင့်ခြင်း»; rūpataṇhā «ရုပ်ကို တပ်မက်မှု» comes later (map_4.py f_rupa4 now reads the
     first compound; a-rūpa compounds are skipped because they carry the keyword arūpa, so 4-02 1-1292 and 5 1-1606
     keep သိမ်မွေ့သော ရုပ် from rūpāvacarā).
   A book-wide check (`harmonise_rupa.py`) finds every other rūpa / Rūpa value already matching its first compound.
   Same principle applied to **nikkhitta** (anikkhittachandatā «ဆန္ဒကို လက်မလွှတ်ခြင်း» before anikkhittadhuratā
   «ဝန်ကို မချထားခြင်း»): «လက်လွှတ်သော / ချထားသော» → «လက်လွှတ်သော» in 2-01 (7), 2-03 (4), 2-04 (4), 2-05 (1), as
   4-03 already had.
4. **Headings** take the Burmese of that heading: all heading keywords already did (checked over every `-0`
   segment). **Report, text headings that differ for the same Pāli element** (translation not edited):
   - suññata: Suññatavāro (2-01 ^1-1-1-3-0) «ဆိတ်သုဉ်းကြောင်း ဖော်ပြချက်» vs Suññatamūlakapaṭipadā (2-03 ^1-1-5-3-0)
     «ဆိတ်သုဉ်းခြင်းကို အခြေခံသော ကျင့်စဉ်» and Suññatapaṭipadā (2-05 ^1-1-8-3-0) «ဆိတ်သုဉ်းခြင်းနှင့် ကျင့်စဉ်».
   - suññataṃ: Suññataṃ (2-03 ^1-1-5-2-0) «ဆိတ်သုဉ်းသော ဈာန်» vs Suddhikasuññataṃ (2-05 ^1-1-8-2-0)
     «ဆိတ်သုဉ်းခြင်း သက်သက်» (adjective vs noun).
   - appaṇihitaṃ: Appaṇihitaṃ (2-03 ^1-1-5-4-0) «တောင့်တမှု မရှိသော ဈာန်» vs Suddhikaappaṇihitaṃ (2-05 ^1-1-8-4-0)
     «တောင့်တမှု မရှိခြင်း သက်သက်».
   - The cittuppāda headings with an inserted feeling (Kiriyāmanoviññāṇadhātusomanassasahagatā …) give the
     discontinuous «ပြုရုံမျှသာ ဖြစ်သော … မနော»; Kiriyāmanodhātu is continuous. Consistent with the text.
5. **Same keyword, same kind of segment, same value** (scan): aligned
   - na (4-01 1-1101) «မဟုတ်» → «မ» (the sample's prefix; first occurrence = the question «kenaci na viññeyyā»
     «မသိနိုင်သော»).
   - numerals keep the text's count with its classifier: 5 Dvādasa «ဆယ့်နှစ်» → «ဆယ့်နှစ်ပါး» (7), dasa / Dasa «ဆယ်» →
     «ဆယ်ပါး» (7), ekādasa «ဆယ့်တစ်» → «ဆယ့်တစ်ပါး» (5), as 2-04, 4-01..4-03; the bare number stays only where the
     text counts with «မျိုး» (dasavidhena, ekādasavidhena in 3-01 / 3-03).
   - asaññā (5, nevasaññānāsañña) «မှတ်သိမှု မရှိသည်» → «မှတ်သိမှု မရှိသော» (3), as 2-04, 2-05, 4-02 (rule 3).
   - bhūtā (5, fragment of mahābhūtā) «မူလဓာတ်ကြီး» → «မူလဓာတ်» (2), as 3-01, 4-01..4-03 (mahābhūtā keeps ကြီး).
   - vipāka (5 1-1441, vipākahetu) «ကံ၏ အကျိုး ဖြစ်သော» → «ကံ၏ အကျိုး» (rule 2: the noun without the copula, as the
     2-04 / 2-05 headings).
   - vipākato (4-01 1-1068, 1-1077, «as resultant») «အကျိုး အဖြစ်» → «အကျိုး» (as 5 rule 15, «အဖြစ်» is the
     «as» marker).
   - vattabbaṃ (4-02 1-1198, 1-1200, «na vattabbaṃ» = «ခေါ်ဆို၍ မရ») «ခေါ်ဆိုသည်» → «ခေါ်ဆို၍ ရ» (as 5 rule 14: the
     gerundive «can be called», positive part by rule 8).
   - kammassa katattā (5) «ကံကို ပြုခဲ့ခြင်း» → «ကံကို ပြုခဲ့ခြင်းကြောင့်» (5), as 4-01 / 4-02: ကြောင့် is the causal
     meaning of katattā and not a rule-1 particle (3-02 / 3-03 keep their own text «ပြုခဲ့သော ကံကြောင့်»).
   - ñāṇaṃ (4-01 1-1067, 1-1106, 1-1128, 4-02 1-1168, 1-1238: moha / avijjā definitions) «ဉာဏ်» → «သိခြင်း»: the
     keyword's first occurrence is aññāṇaṃ «မသိခြင်း» (rule 8, positive part), as 2-04 1-390 and 4-03; the old ALT
     picked «ဉာဏ်» from the later «ဉာဏ်နုံခြင်း».
   Mātikā items keep the sample values throughout.
6. **«(no direct equivalent)»** for Yo / Yā / Yaṃ (and ye, cāti) and caya left as they are. Where the text itself
   writes a word, the existing values stay (yaṃ / yo / yañca = «ရှိသမျှ» in «… vā panaññampi atthi» and «yañca rūpaṃ
   …»; Yo = «အကြင်» in 4-01 1-1092).

## Scan before (104 keywords with more than one value)

Full list with chapters: `scan-before.tsv`. Resolved (10 keywords now single-valued): ṭhapetvā, ārabbha,
upādāya, asaññā, bhūtā, Dvādasa, na, nikkhitta, vattabbaṃ, vipāka. New in the list (1): ekādasa (5 now
«ဆယ့်တစ်ပါး» vs 3-01 / 3-03 «ဆယ့်တစ်» from «ဆယ့်တစ်မျိုး»: the numeral rule, not an inconsistency). Reduced (the
outlier or the « / » alternative removed, a genuine difference remains): rūpa, rūpaṃ, paṭicca, dasa, kammassa
katattā, vipākato, ñāṇaṃ. 104 − 10 + 1 = 95.

## Scan after: every kept difference (95)

Generated by `harmonise_map_reasons.py` from `scan-after.tsv` (values: uses; chapters). «REPORT (text)» = the same Pāli is worded differently in the translation itself (not edited).

| keyword | values (uses; chapters) | why kept |
|---|---|---|
| abhinibbattā | ထင်ရှားစွာ ပေါ်ထွက်ပြီးသော (2; 4-01) · ထင်ရှားစွာ ပေါ်ထွက်သော (2; 4-01) | 4-01 arisen list (1-1041/1046) «…ပြီးသော» vs the not-yet list (1-1042/1045, «မ…သေးသော»): positive stem of the fragment that lost a-, no «ပြီး» in the text (4-01 rule 16). Grammar. |
| abyākatahetū | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော အမြစ် (7; 4-01) · ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော သဘောတရားတို့၏ အမြစ် (1; 5) | 4-01 1-1059 «… အမြစ်» vs 5 1-1441 «… သဘောတရားတို့၏ အမြစ်» for the same Pāli answer: the text's own wording differs (presence: the other value is not in that segment). REPORT (text). |
| akusalahetū | အကုသိုလ် အမြစ် (4; 4-01) · အကုသိုလ်၏ အမြစ် (1; 5) | 4-01 «အကုသိုလ် အမြစ်» vs 5 1-1441 «အကုသိုလ်၏ အမြစ်», same Pāli: the text's own wording differs (presence: the other value is not in that segment). REPORT (text). |
| akusalaṃ | အကုသိုလ်စိတ် (59; 5) · အကုသိုလ် (6; 2-05) | «neva kusalaṃ nākusalaṃ» (2-05) = the adjective «အကုသိုလ်» vs the Aṭṭhakathā list noun «အကုသိုလ်စိတ်» (the text supplies စိတ်; 5 rule 18). Grammar / text form. |
| akusalābyākatā | အကုသိုလ်နှင့် ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော (39; 4-01 4-02) · အကုသိုလ် ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော (2; 4-01 5) | 4-01 ALT: the text has «အကုသိုလ်နှင့် …» (17+22) or «အကုသိုလ် …» without နှင့် (1-1026, 5 1-1437). the text's own wording differs (presence: the other value is not in that segment). |
| anussati | အဖန်ဖန် အောက်မေ့ခြင်း (13; 2-01 2-03 4-03) · အောက်မေ့နိုင်သော (1; 4-03) | sati synonym «အဖန်ဖန် အောက်မေ့ခြင်း» vs pubbenivāsānussati ñāṇa «ရှေးဘဝများကို အောက်မေ့နိုင်သော ဉာဏ်» (4-03 1-1380). genuine sense difference / construction. |
| appaṇihitaṃ | တောင့်တမှု မရှိသော (37; 2-03 2-05) · တောင့်တမှု မရှိခြင်း (1; 2-05) | heading Appaṇihitaṃ «တောင့်တမှု မရှိသော ဈာန်» (2-03) vs heading Suddhikaappaṇihitaṃ «တောင့်တမှု မရှိခြင်း သက်သက်» (2-05): decision 4 (heading Burmese). REPORT: the text's headings differ. |
| arūpino dhammā | ရုပ် မဟုတ်သော … သဘောတရား (78; 2-01 2-02 2-03 2-04 2-05) · ရုပ် မဟုတ်သော သဘောတရား (1; 1-matika) | the cittuppāda formula inserts «အခြား» («ရုပ် မဟုတ်သော အခြား သဘောတရား») → « … » (sample rule 10) vs Mātikā continuous. Text shape. |
| asātaṃ | နှစ်သက်ဖွယ် မကောင်းသော (15; 2-01 2-04) · နှစ်သက်ဖွယ် မကောင်းမှု (6; 2-04 2-05) | noun «နှစ်သက်ဖွယ် မကောင်းမှု» (asātaṃ dukkhaṃ: the feeling) vs attributive «နှစ်သက်ဖွယ် မကောင်းသော» in «neva sātaṃ nāsātaṃ». Grammar. |
| bahiddhā | ပြင်ပ၌ (45; 2-02) · သူတစ်ပါး၌ (12; 1-matika 3-03 4-01 5) · အပြင်ဘက် (6; 4-01 4-02) | «in others» «သူတစ်ပါး၌» (Mātikā) / «outside» «အပြင်ဘက်» (ito bahiddhā, outside the dispensation) / «externally» «ပြင်ပ၌» (abhibhāyatana: bahiddhā rūpāni passati). genuine sense difference (harmonise-notes). |
| bhedo | ကွဲထွက်ခြင်း (3; 3-02 3-03) · ကွဲခြင်း (3; 3-02 3-03) | vacībhedo «ကွဲထွက်ခြင်း» (utterance) vs aniccatā list «ကွဲခြင်း» (breaking up). genuine sense difference. |
| brahma | ဗြဟ္မစိုရ် (2; 2-02) · ဗြဟ္မာ့ (1; 4-02) | brahmavihāra «ဗြဟ္မစိုရ်» vs brahmaloka «ဗြဟ္မာ့ပြည်». genuine sense difference. |
| cetasikaṃ | စိတ်ပိုင်းဆိုင်ရာ (35; 2-01 2-03 2-04) · စိတ်၏ အဖော် (1; 3-01) | feeling definitions «စိတ်ပိုင်းဆိုင်ရာ» (mental) vs the Mātikā cetasika dyad in the 3-01 Ekaka (acetasikaṃ) «စိတ်၏ အဖော်» (sample value). genuine sense difference. |
| chanda | ဆန္ဒ (37; 2-02 2-03 2-05) · လိုလားမှု (4; 4-02 5) | chandādhipateyya «ဆန္ဒ» vs kāmacchanda «ကာမကို လိုလားမှု». the text's own wording differs (presence: the other value is not in that segment). |
| dasa | ဆယ်ပါး (9; 4-01 4-02 5) · ဆယ် (2; 3-01 3-03) | numerals keep the count the text uses: «ဆယ်ပါး» where the text counts with ပါး (4-01, 4-02, 5: aligned) vs dasavidhena «ဆယ်မျိုးဖြင့်» (3-01, 3-03: vidha has its own word). Rule. |
| dhamma | သဘောတရား (78; preamble 2-01 2-02 2-03 2-04 2-05 3-01 3-03 4-01 4-02 4-03 5) · တရား (2; 4-01 4-03) | «သဘောတရား» (state) vs «တရား» (the Teaching) in dhammamacchariya / dhammapaṭisanthāra (4-01, 4-03). genuine sense difference. |
| dhamme | တရားတော် (4; 4-01 4-02) · သဘောတရား (1; 4-01) | «တရားတော်» (the Teaching) in the doubt list «dhamme kaṅkhati» vs states. genuine sense difference. |
| domanassa | စိတ်ဆင်းရဲမှု (29; 2-04 5) · စိတ်ဆင်းရဲခြင်း (1; 4-03) | «စိတ်ဆင်းရဲမှု» vs the paṭiccasamuppāda list (4-03 1-1343) «စိတ်ဆင်းရဲခြင်း»: the text's own wording differs (presence: the other value is not in that segment) (list ending, 4 rule 20). |
| dukkha | ခက်ခဲသော (77; 2-02 2-03 2-05) · နာကျင်သော (6; 3-01 3-02 3-03) · နာကျင်မှု (5; 2-02 2-05 5) · ဒုက္ခ (4; 4-01 4-02 4-03) | dukkhapaṭipadā «ခက်ခဲသော» (difficult) / pain «နာကျင်မှု» / dukkhasamphassa «နာကျင်သော» / dukkhamūla, dukkhakkhandha «ဒုက္ခ». genuine sense difference. |
| ekādasa | ဆယ့်တစ်ပါး (5; 5) · ဆယ့်တစ် (2; 3-01 3-03) | as dasa: 5 «ဆယ့်တစ်ပါး» vs ekādasavidhena «ဆယ့်တစ်မျိုး» (3-01, 3-03). Rule. |
| eva | သာ (61; 2-03 2-04 2-05) · ပင် (1; 3-01) | vivicceva «ကင်းဆိတ်၍သာ» «သာ» vs -meva in 3-01 1-594 «…သည်ပင်» «ပင်». the text's own wording differs (presence: the other value is not in that segment). |
| gāho | စွဲကိုင်ခြင်း (27; 2-04 4-01 4-02 4-03) · ယူနိုင်ခြင်း (4; 4-01 4-02) | view list «စွဲကိုင်ခြင်း» vs anekaṃsaggāho «တစ်ထစ်ချ မယူနိုင်ခြင်း» → «ယူနိုင်ခြင်း». the text's own wording differs (presence: the other value is not in that segment). |
| hetū | အမြစ် (50; 1-matika 2-01 2-02 2-03 2-04 4-01 5) · အကြောင်း (2; 4-03) | root «အမြစ်» vs ṭhānāṭhāna «hetū paccayā» «အကြောင်း» (cause). genuine sense difference. |
| indriyānaṃ | စွမ်းရည် (3; 3-02 3-03) · အာရုံခံ အင်္ဂါ (2; 4-03) | jaratā «indriyānaṃ paripāko» «စွမ်းရည်» (faculties) vs the sense doors «အာရုံခံ အင်္ဂါ» (4-03, as the sample's indriyesu). the text's own wording differs (presence: the other value is not in that segment). |
| jātā | မွေးဖွားပြီးသော (2; 4-01) · မွေးဖွားသော (2; 4-01) | = abhinibbattā (arisen / not-yet lists, 4-01 rule 16). Grammar. |
| kammassa katattā | ပြုခဲ့သော ကံကြောင့် (56; 3-02 3-03) · ကံကို ပြုခဲ့ခြင်းကြောင့် (10; 4-01 4-02 5) | 3-02/3-03 text «ပြုခဲ့သော ကံကြောင့်» vs 4/5 «ကံကို ပြုခဲ့ခြင်းကြောင့်» (5 aligned to 4: ကြောင့် kept). the text's own wording differs (presence: the other value is not in that segment). |
| kamyatā | လိုချင်ခြင်း (3; 4-01 4-02) · ထူလိုခြင်း (2; 4-01 4-02) · လိုလားခြင်း (1; 4-03) | ketukamyatā «အလံ ထူလိုခြင်း» / sādhukamyatā «… လိုချင်ခြင်း» / bhiyyokamyatā «ပိုမို လိုလားခြင်း»: the fragment takes the verb of its compound. the text's own wording differs (presence: the other value is not in that segment). |
| khandha | ပင်စည် (4; 3-02) · အစုအဝေး (1; 4-02) | khandharasa «ပင်စည်» (trunk) vs aggregate «အစုအဝေး». genuine sense difference. |
| khandhā | အစုအဝေး (35; 2-01 2-02 2-03 2-04 2-05 4-01) · အစု (1; 4-03) | aggregates «အစုအဝေး» vs āpattikkhandhā «အပြစ် အစု» (classes of offence, 4-03). genuine sense difference / text. |
| kiriyato | ပြုရုံမျှသာ ဖြစ်သော စိတ် (25; 5) · ပြုရုံမျှသာ (7; 5) | as kusalato (5 rule 15). Grammar. |
| kiriyā | ပြုရုံမျှသာ ဖြစ်သော (93; 2-05 3-01 4-01 4-02 5) · ပြုခြင်း (3; 2-03) | functional «ပြုရုံမျှသာ ဖြစ်သော» vs akiriyā «မပြုခြင်း» (non-doing, abstinence list 2-03) → «ပြုခြင်း». genuine sense difference. |
| kiriyā mano | ပြုရုံမျှသာ ဖြစ်သော … မနော (2; 2-05) · ပြုရုံမျှသာ ဖြစ်သော မနော (1; 2-05) | heading shapes: «ပြုရုံမျှသာ ဖြစ်သော မနော» continuous vs «ပြုရုံမျှသာ ဖြစ်သော၊ … မနော» where the heading inserts the feeling. Text shape (decision 4). |
| kiriyāmano | ပြုရုံမျှသာ ဖြစ်သော မနော (2; 2-05 5) · ပြုရုံမျှသာ ဖြစ်သော … မနော (2; 2-05) | as kiriyā mano (decision 4). Text shape. |
| kusalahetū | ကုသိုလ် အမြစ် (9; 4-01) · ကုသိုလ်၏ အမြစ် (1; 5) | 4-01 «ကုသိုလ် အမြစ်» vs 5 1-1441 «ကုသိုလ်၏ အမြစ်», same Pāli: the text's own wording differs (presence: the other value is not in that segment). REPORT (text). |
| kusalato | ကုသိုလ်စိတ် (16; 5) · ကုသိုလ် (7; 5) | 5 rule 15: «-ato ca … -ato ca» = «as» (ကုသိုလ်အဖြစ်) vs «-ato N» = «among» (ကုသိုလ်စိတ်အနက်), decided by the keyword's first occurrence. Grammar. |
| kusalaṃ | ကုသိုလ်စိတ် (77; 5) · ကုသိုလ် (34; 2-01 2-02 2-03 2-05) | headings and «neva kusalaṃ nākusalaṃ» «ကုသိုလ်» vs the Aṭṭhakathā kinds of mind «ကုသိုလ်စိတ်» (5 rule 18). Grammar / text form. |
| kusalesu | ကုသိုလ် (2; 1-matika 4-03) · ကုသိုလ်စိတ် (1; 5) | Mātikā «kusalesu dhammesu» (sample) vs 5 1-1441 «kusalesu uppajjanti» = «ကုသိုလ်စိတ်တို့၌» (in wholesome minds). genuine sense difference. |
| kāya | ကိုယ် (167; 2-03 3-01 3-02 3-03 4-01 4-02 4-03 5) · စိတ်၏ အဖော်တို့ (23; 2-01 2-03) | body «ကိုယ်» vs the mental body «စိတ်၏ အဖော်တို့» in kāyapassaddhi etc. (harmonise item 10). genuine sense difference. |
| kāyassa | ကိုယ် (3; 3-02 3-03) · စိတ်၏ အဖော် (1; 4-02) · ကိုယ်ခန္ဓာ (1; 4-03) | kāyaviññatti «ကိုယ်» / «imassa kāyassa» «ကိုယ်ခန္ဓာ» / middha «စိတ်၏ အဖော်» (mental body). genuine sense difference / text. |
| kāyena | ကိုယ် (3; 3-02 4-03) · စိတ်၏ အဖော်တို့ (1; 2-02) | body door «ကိုယ်» vs third jhāna «sukhañca kāyena paṭisaṃvedeti» «စိတ်၏ အဖော်တို့ဖြင့်» (mental body). genuine sense difference. |
| maggaṃ | လမ်း (114; 2-02 2-04) · မဂ် (4; 2-03 2-05) | «rūpūpapattiyā maggaṃ» «လမ်း» (way to rebirth) vs lokuttara «မဂ်». genuine sense difference. |
| maggo | မဂ် (17; 2-01 2-03 2-04) · လမ်း (12; 4-01 4-02) | path «မဂ်» vs kummaggo «လမ်းမှား» (road). genuine sense difference. |
| mucchā | မိန်းမောမှု (6; 4-01 4-02) · မိန်းမောခြင်း (3; 4-01 4-02) | lobha list «…ခြင်း» vs kāma lists «…မှု» (4 rule 20 ALT). the text's own wording differs (presence: the other value is not in that segment). |
| nandī | နှစ်သက်မှု (6; 4-01 4-02) · နှစ်သက်ခြင်း (3; 4-01 4-02) | as mucchā. the text's own wording differs (presence: the other value is not in that segment). |
| nibbattā | ပေါ်ထွက်ပြီးသော (2; 4-01) · ပေါ်ထွက်သော (2; 4-01) | = abhinibbattā. Grammar. |
| niyatā | ကျိန်းသေသော (12; 1-matika 4-01 4-02 5) · သီးသန့် ဖြစ်သော (2; 4-01) | «ကျိန်းသေသော» (fixed) vs «ajjhattaṃ paccattaṃ niyatā» «သီးသန့် ဖြစ်သော» (individual). genuine sense difference. |
| para | သူတစ်ပါး (2; 4-01 4-03) · ပရ (1; 4-02) | «သူတစ်ပါး» (others) vs the loan paranimmitavasavattī «ပရ» (4 rule 19). genuine sense difference. |
| patho | လမ်းကြောင်း (14; 2-04 4-01 4-02) · လမ်း (5; 2-04 4-01 4-02) | dvedhāpatho «လမ်း နှစ်ခွ» vs micchāpatho «မှားယွင်းသော လမ်းကြောင်း». the text's own wording differs (presence: the other value is not in that segment). |
| paṭicca | အကြောင်းတို့ကို မှီ၍ (94; 2-01 2-02 2-03 2-04 2-05 4-01 4-02) · အကြောင်းအကျိုး ဆက်စပ် (2; 1-matika 4-03) | absolutive «အကြောင်းတို့ကို မှီ၍» (aligned, decision 1) vs paṭiccasamuppāda «အကြောင်းအကျိုး ဆက်စပ်» (Mātikā value kept, decision 1). |
| phala | အသီး (8; 3-02) · ဖိုလ် (2; 4-03) | fruition «ဖိုလ်» vs fruit «အသီး» (phalagandha). genuine sense difference. |
| phalaṃ | အသီးအပွင့် (3; 4-02 4-03) · ဖိုလ် (2; 4-01 5) | fruition «ဖိုလ်» vs kamma's fruit «အသီးအပွင့်». genuine sense difference. |
| pātubhūtā | ထင်ရှားလာပြီးသော (2; 4-01) · ထင်ရှား လာသော (2; 4-01) | = abhinibbattā. Grammar. |
| rūpa | သိမ်မွေ့သော ရုပ် (226; 1-matika 2-02 2-03 2-04 2-05 3-01 4-01 4-02 5) · အဆင်းအရောင် (153; 2-01 2-04 2-05 3-02 3-03 4-01 4-02 4-03 5) · ရုပ် (18; 2-02 2-04 2-05 3-01 4-01) | decision 3: rūpāvacara «သိမ်မွေ့သော ရုပ်» / rūpāyatana, rūpadhātu, rūpārammaṇa, rūpāsā «အဆင်းအရောင်» / matter «ရုပ်»; one value per segment by the first compound; no alternatives left. genuine sense difference. |
| rūpañca | ရုပ် (54; 5) · ရုပ်ပိုင်း (1; 1-matika) | matter «ရုပ်» (rūpañca nibbānañca) vs the Mātikā nāma/rūpa pair «ရုပ်ပိုင်း» (sample). genuine sense difference. |
| rūpañca nibbānañca | ရုပ်လည်း နိဗ္ဗာန်လည်း (48; 5) · ရုပ်နှင့် နိဗ္ဗာန် (6; 5) | 5: «ရုပ်လည်း နိဗ္ဗာန်လည်း» vs «ရုပ်နှင့် နိဗ္ဗာန်» (1-1401 …). the text's own wording differs (presence: the other value is not in that segment). |
| rūpaṃ | ရုပ် (511; 3-01 3-02 3-03 4-01 4-02 4-03 5) · အဆင်းအရောင် (2; 4-03) · ရုပ်ပိုင်း (1; 4-03) | matter «ရုပ်» / object seen «အဆင်းအရောင်» (cakkhunā rūpaṃ disvā) / nāma-rūpa «ရုပ်ပိုင်း» (4-03 1-1317); one value per segment (decision 3). genuine sense difference. |
| rūpaṃ appaṭighaṃ | ထိခိုက်မှု မရှိသော … ရုပ် (4; 3-03) · ထိခိုက်မှု မရှိသော ရုပ် (1; 3-02) | 3-03 headings insert «စွမ်းရည် ဖြစ်သော» (rūpaṃ appaṭighaṃ indriyaṃ) → « … ». Text shape. |
| rūpaṃ sappaṭighaṃ | ထိခိုက်မှု ရှိသော … ရုပ် (4; 3-03) · ထိခိုက်မှု ရှိသော ရုပ် (3; 3-01 3-02) | as rūpaṃ appaṭighaṃ. Text shape. |
| sacca | အမှန် (4; 4-01 5) · သစ္စာ (1; 4-03) | idaṃsaccābhinivesa «အမှန်» (true) vs saccānulomika «သစ္စာ» (the truths). genuine sense difference. |
| saddhā | ယုံကြည်မှု (36; 2-01 2-02 2-03 4-03) · ယုံကြည်မှု ရှိသော (1; 4-03) | noun «ယုံကြည်မှု» vs «saddhā sīlavanto» (faithful persons) «ယုံကြည်မှု ရှိသော». Grammar. |
| sammā | မှန်ကန်သော (123; 2-01 2-02 2-03 2-05 4-01 4-03) · မှန်ကန်စွာ (3; 4-02 4-03) · အပြည့်အဝ (1; preamble) | path factors «မှန်ကန်သော» / sammaggatā, sammāpaṭipannā «မှန်ကန်စွာ» (adverb) / sammāsambuddha «အပြည့်အဝ» (sample). Grammar / sense. |
| sampaggāho | ခိုင်မြဲစွာ ထမ်းဆောင်ခြင်း (16; 2-01 2-03 2-04 2-05) · အလွန် မြှင့်တင်ခြင်း (2; 4-01 4-02) | dhurasampaggāho «ခိုင်မြဲစွာ ထမ်းဆောင်ခြင်း» vs the māna list «အလွန် မြှင့်တင်ခြင်း». genuine sense difference / text. |
| samuppannā | ဖြစ်ပေါ်လာသော (73; 2-01 2-02 2-03 2-04 2-05) · ကောင်းစွာ ဖြစ်ပေါ်ပြီးသော (2; 4-01) · ကောင်းစွာ ဖြစ်ပေါ်သော (2; 4-01) | «ဖြစ်ပေါ်လာသော» in paṭiccasamuppannā (2-xx cittuppāda formula) vs «ကောင်းစွာ ဖြစ်ပေါ်ပြီးသော / …သော» in the 4-01 arisen / not-yet synonym lists (sam- = ကောင်းစွာ there). Text form per formula + grammar. |
| samuṭṭhitā | ကောင်းစွာ ထပေါ်ပြီးသော (2; 4-01) · ကောင်းစွာ ထပေါ်သော (2; 4-01) | = abhinibbattā. Grammar. |
| samāpatti | ဈာန် ဝင်စားရာ (2; 1-matika 4-03) · ဈာန် ဝင်စားမှု (1; 4-03) | Mātikā «ဈာန် ဝင်စားရာ» (sample) vs 4-03 1-1339 «tāhi samāpattīhi» «ဈာန် ဝင်စားမှု»: the Mātikā value is not in 1-1339's text. the text's own wording differs (presence: the other value is not in that segment). REPORT (text). |
| santuṭṭhitā | ရောင့်ရဲမှု (3; 1-matika 4-03) · ရောင့်ရဲခြင်း (1; 4-03) | «ရောင့်ရဲမှု» (Mātikā, 4-03 asantuṭṭhitā) vs 4-03 1-1355 «ရောင့်ရဲခြင်း»: the text's own wording differs (presence: the other value is not in that segment). |
| sañjātā | ကောင်းစွာ မွေးဖွားပြီးသော (2; 4-01) · ကောင်းစွာ မွေးဖွားသော (2; 4-01) | = abhinibbattā. Grammar. |
| saṃvego | သံဝေဂ ရခြင်း (1; 1-matika) · သံဝေဂ (1; 4-03) | Mātikā «သံဝေဂ ရခြင်း» (sample) vs 4-03 1-1376 «Saṃvegoti» «သံဝေဂ ဟူသည်»: «ရခြင်း» not in that segment. the text's own wording differs (presence: the other value is not in that segment). REPORT (text). |
| sekkhā | ကျင့်ကြံဆဲသူ၏ (4; 1-matika 4-01 5) · ကျင့်ကြံမှု (2; 4-01 5) | «ကျင့်ကြံဆဲသူ၏» (sekkhā) vs the fragment of asekkhā «ကျင့်ကြံမှု» (positive part of «ကျင့်ကြံမှု ပြီးဆုံးသူ၏», rule 8). Fragment. |
| sineho | ချစ်ခင်မှု (6; 4-01 4-02) · စေးကပ်မှု (4; 3-02 3-03) · ချစ်ခင်ခြင်း (3; 4-01 4-02) | as mucchā; plus āpodhātu «စေးကပ်မှု» (cohesion): genuine sense difference. |
| sukha | လွယ်ကူသော (43; 2-02 2-03 2-05) · သာယာမှု (13; 1-matika 2-04 3-01 4-01 4-02 5) · သာယာစွာ (8; 2-05 4-02) · သာယာသော (6; 3-01 3-02 3-03) | sukhapaṭipadā «လွယ်ကူသော» (easy) / feeling «သာယာမှု» / sukhavihāra «သာယာစွာ» / sukhasamphassa «သာယာသော». genuine sense difference. |
| sukhā | သာယာသော (20; 2-01 2-03 2-04) · ချိုသော (1; 4-03) | «သာယာသော» (pleasant feeling) vs kaṇṇasukhā «နားကို ချိုသော» (sweet to the ear). genuine sense difference. |
| suññata | ဆိတ်သုဉ်းခြင်း (4; 2-03 2-05) · ဆိတ်သုဉ်းကြောင်း (2; 2-01) | decision 4: Suññatavāro «ဆိတ်သုဉ်းကြောင်း ဖော်ပြချက်» (2-01) vs Suññatamūlakapaṭipadā / Suññatapaṭipadā «ဆိတ်သုဉ်းခြင်း…» (2-03, 2-05). REPORT: the text's headings differ for suññata. |
| suññataṃ | ဆိတ်သုဉ်းသော (40; 2-03 2-05) · ဆိတ်သုဉ်းခြင်း (1; 2-05) | decision 4: heading Suññataṃ «ဆိတ်သုဉ်းသော ဈာန်» (2-03) vs Suddhikasuññataṃ «ဆိတ်သုဉ်းခြင်း သက်သက်» (2-05); in the formula the adjective «ဆိတ်သုဉ်းသော». REPORT: the text's headings differ. |
| sātaṃ | နှစ်သက်ဖွယ်ကောင်းမှု (20; 2-01 2-03 2-04) · နှစ်သက်ဖွယ်ကောင်းသော (15; 2-01 2-04) | as asātaṃ (noun vs «neva sātaṃ nāsātaṃ»). Grammar. |
| thambhitattaṃ | တောင့်တင်းနေသော အဖြစ် (7; 2-04 4-01 4-02) · တောင့်တင်းထားသော အဖြစ် (1; 3-03) | «cittassa» «တောင့်တင်းနေသော အဖြစ်» vs vāyodhātu «rūpassa» «တောင့်တင်းထားသော အဖြစ်». the text's own wording differs (presence: the other value is not in that segment). |
| uppannaṃ | ဖြစ်ပေါ်လာသော (25; 2-01 2-02 2-04 2-05) · ဖြစ်ပေါ်သော (21; 5) · ဖြစ်ပေါ်ပြီးသော (2; 3-01) | cittuppāda formula «ဖြစ်ပေါ်လာသော» (2-xx) vs «etthuppannaṃ» «ဖြစ်ပေါ်သော» (5) vs the 3-01 Ekaka list «ဖြစ်ပေါ်ပြီး၊» → «ဖြစ်ပေါ်ပြီးသော». the text's own wording differs (presence: the other value is not in that segment). |
| uppannā | ဖြစ်ပေါ်လာသော (10; 2-04 2-05) · ဖြစ်ပေါ်ပြီးသော (4; 1-matika 4-01 5) · ဖြစ်ပေါ်သော (2; 4-01) | Mātikā / arisen-question «ဖြစ်ပေါ်ပြီးသော» (sample) vs the cittuppāda formula «dhātu uppannā hoti» «ဖြစ်ပေါ်လာသော» vs the 4-01 not-yet list «ဖြစ်ပေါ်သော». the text's own wording differs (presence: the other value is not in that segment). |
| uppādāya | ဖြစ်ပေါ်ရန် (2; 4-03) · ဖြစ်ပေါ်စေရန် (1; 4-03) | «ဖြစ်ပေါ်ရန်» vs anuppādāya «မဖြစ်ပေါ်စေရန်» (causative in the text). the text's own wording differs (presence: the other value is not in that segment). |
| uṭṭhitā | ထပေါ်ပြီးသော (2; 4-01) · ထပေါ်သော (2; 4-01) | = abhinibbattā. Grammar. |
| vatthūni | ဖြစ်ရာ အခြေခံ (1; 4-02) · အခြေခံ (1; 5) | 4-02 1-1235 «ကိလေသာ ဖြစ်ရာ အခြေခံ» vs 5 1-1565 «ကိလေသာ အခြေခံ», same Pāli: the text's own wording differs (presence: the other value is not in that segment). REPORT (text). |
| vaṇṇa | အရောင် (6; 3-02 3-03) · ဂုဏ်သတင်း (1; 4-01) | vaṇṇamacchariya «ဂုဏ်သတင်း» (praise) vs vaṇṇanibhā «အရောင်» (colour). genuine sense difference. |
| vibhava | ဘဝ ပြတ်စဲခြင်း (3; 4-01 4-02) · ဘဝ ပျောက်ကွယ်သည် (2; 1-matika 4-03) | vibhavadiṭṭhi «ဘဝ ပျောက်ကွယ်သည်» (sample) vs vibhavataṇhā «ဘဝ ပြတ်စဲခြင်းကို တပ်မက်မှု». the text's own wording differs (presence: the other value is not in that segment). |
| vipākamanoviññāṇadhātu | ကံ၏ အကျိုး ဖြစ်သော … မနော သိစိတ် ဓာတ် (2; 2-04) · ကံ၏ အကျိုး ဖြစ်သော မနော သိစိတ် ဓာတ် (1; 2-05) | as kiriyā mano. Text shape (decision 4). |
| vipākato | အကျိုး ဖြစ်သော စိတ် (17; 5) · ကံ၏ အကျိုး (9; 5) · အကျိုး (2; 4-01) | as kusalato (5 rule 15); 4-01 1-1068/1077 «as» = «အကျိုး» (aligned to 5's «as» form without «အဖြစ်»; the 4-01 text has no «ကံ၏»). Grammar / text. |
| vipākato ca kiriyato | ကံ၏ အကျိုးအဖြစ်လည်းကောင်း ပြုရုံမျှသာအဖြစ်လည်းကောင်း (25; 5) · အကျိုး ဖြစ်သော စိတ်အနက်လည်းကောင်း ပြုရုံမျှသာ ဖြစ်သော စိတ်အနက်လည်းကောင်း (1; 5) | as kusalato (5 rule 15). Grammar. |
| vipākā manoviññāṇadhātu | ကံ၏ အကျိုး ဖြစ်သော … မနော သိစိတ် ဓာတ် (1; 2-04) · ကံ၏ အကျိုး ဖြစ်သော မနော သိစိတ် ဓာတ် (1; 2-05) | as kiriyā mano: heading inserts the feeling. Text shape (decision 4). |
| vāro | အပိုင်း (6; 2-01 3-02 3-03 4-01 4-02) · ဖော်ပြချက် (4; 2-01) | koṭṭhāsa- / suññatavāra «ဖော်ပြချက်» vs bhāṇavāra «ရွတ်ဖတ်ရန် အပိုင်း». genuine sense difference. |
| yañca | ရှိသမျှ (15; 4-01 4-02 5) · (no direct equivalent) (1; 4-01) | decision 6 (relative pronouns): «ရှိသမျှ» where the text renders «yañca rūpaṃ …» as «… ရုပ် ရှိသမျှလည်း», none in 4-01 1-1043 («… ဖြစ်ပေါ်လာမည့် ရုပ်လည်း»). Text. |
| yaṃ | (no direct equivalent) (97; 2-01 2-03 2-04 2-05 3-02 3-03 4-01 4-02 4-03) · ရှိသမျှ (56; 3-02 3-03 5) | decision 6: (no direct equivalent), except «yaṃ vā panaññampi atthi» = «အခြား … ရှိသမျှ» (3 rule 15). Text. |
| yo | (no direct equivalent) (120; 2-01 2-03 2-04 2-05 3-02 3-03 4-01 4-02 4-03) · ရှိသမျှ (12; 3-02) · အကြင် (1; 4-01) | decision 6: as yaṃ; Yo in 4-01 1-1092 = «အကြင်» (the text writes it). Text. |
| ñāṇaṃ | သိခြင်း (8; 2-04 4-01 4-02 4-03) · ဉာဏ် (5; 1-matika 4-01 4-03) | knowledge «ဉာဏ်» vs the fragment of aññāṇaṃ «မသိခြင်း» → «သိခြင်း» (rule 8); one value per segment by first occurrence (4-01 1-1067/1106/1128, 4-02 1-1168/1238 aligned). genuine sense difference. |
| āhāraṃ | အာဟာရ (4; 2-03 2-05) · အစာ (2; 4-03) | lokuttara āhāra «အာဟာရ» (nutriment) vs bhojana «အစာ» (food, 4-03). genuine sense difference. |
| ākāsa | ဟင်းလင်းပြင် (47; 3-01 3-02 3-03 4-02 5) · ကောင်းကင် (12; 2-02 2-04 2-05 4-02 5) | ākāsadhātu «ဟင်းလင်းပြင်» (space element) vs ākāsānañcāyatana «ကောင်းကင်». the text's own wording differs (presence: the other value is not in that segment). |
| āyatanāni | အာရုံခံ နယ်ပယ် (34; 2-01 2-02 2-03 2-04 2-05) · နယ်ပယ် (2; 2-02) | sense bases «အာရုံခံ နယ်ပယ်» vs abhibhāyatanāni «လွှမ်းမိုးရာ နယ်ပယ်» (2-02). genuine sense difference. |
