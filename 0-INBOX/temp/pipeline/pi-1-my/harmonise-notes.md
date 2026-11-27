# Consistency pass: pi-1 Burmese zero-shot (Dhammasaṅgaṇī «သဘောတရားများကို စုစည်းရေတွက်ခြင်း»), 14 chapter files

One Pāli item = one Burmese form across the book. Every change was made in the generators or in the shared module
`my_formulas.py`, then every chapter was rebuilt from its generator. Nothing was edited by hand in the chapter files.
Pāli only (no Burmese translation or nissaya, no web search). Nothing committed.

- Rebuild + all checks: `regen_zeroshot.sh` (order: `make_sample.py --terms`, `make_ch2-01.py`, then 2-02-03,
  2-04-05, 3, 4, 5). A second run changes no chapter byte (and no byte of `my-zeroshot-terms.md`).
- Item table: `harmonise-table.tsv` (written by `harmonise_scan.py --table`): 93 items (91 with other forms found before
  the pass, 1009 uses changed; 2 already one form) + 12 checked / kept items.
- Scans: `harmonise_scan.py` (every item, before vs now; fails if an other form is left; also runs
  `harmonise_lines.py`: identical Pāli units of any length, headings and colophons included, and `harmonise_tables.py`:
  the same Pāli key in all seven generators' tables, 19 kept keys listed in its KEEP with the reason),
  `harmonise_diff.py` (changed lines vs the backup), `harmonise_align_diff.py` (word-level view of align_check),
  `harmonise_count.py` (uses per form = the «majority» of the precedence rule), `harmonise_typo.py` (no «?», «।», «:-»,
  NFC, no Zawgyi-range code points, no double blank line), `grep_pm.py` (Pāli regex -> Burmese line).
- `align_check_my.py`, `align_hidden_my.py`: Burmese copies of pi-4-mr/align_check.py and pi-4-mr/rails/align_hidden.py.
  The Marathi scripts split sentences on «.» / «?», which Burmese does not have, so every Burmese line was compared whole
  (1648 lines); the copies split the Burmese on «။» and name the chapter file in the locations («2-03:12»).
- Backups (before the pass): `harmonise-backup/` (every generator, every check, `my_formulas.py`,
  `my-zeroshot-terms.md`) and `harmonise-backup/chapters-before/` (the 14 chapter files). The backup terms file was
  older than the 2-01 module section (its Headings list lacked the 2-01 titles); the rebuild adds them.
- Result: 475 lines changed in 12 files: 2-01: 1, 2-02: 1, 2-03: 27, 2-04: 15, 2-05: 67, 3-01: 2, 3-02: 3, 3-03: 2,
  4-01: 143, 4-02: 129, 4-03: 23, 5: 62; preamble and 1-matika (the user-approved sample): 0.
- align_check: 51 differing sentences before, 0 now (`align-before.txt`, `align-after.txt`). align_hidden: 0 unmatched
  before and now (18 uneven lines; `align-hidden-before.txt`, `align-hidden-after.txt`).
- All checks pass: check_chapter_ids, pi-6-mr/check_text_pe.py, pi-4-mr/check_marks.py OK on all 14 files (chk-pe
  copies deleted by the script); check_sample, check_ch2-01, check_ch2-02-03, check_ch2-04-05, check_ch3, check_ch4,
  check_ch5: 0 mismatches.

## Decision rules
The todo's precedence: (1) the user-approved sample (preamble, Mātikā strings of my_formulas.py); (2) the 2-01 model
(factor names, synonym table, frames); (3) matter terms: the Rūpakaṇḍa 3-xx; (4) the majority of uses in the book
(`harmonise_count.py`); (5) the plainest for an ordinary reader. Two working rules on top:
- The jhāna / path / immaterial openings follow the kusala chapters 2-02 / 2-03: 2-04 / 2-05 repeat their sentences
  word for word («Katame dhammā abyākatā? Yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti … ime dhammā kusalā.»), which is
  what align_check reported, and 2-02 / 2-03 hold the majority of the openings (134 of 240 «upasampajja viharati»).
- Grammar wins over a count: in Burmese the purpose clause stands before the verb it belongs to.
Genuine sense differences are kept and listed below and in the table (CHECKED).

## Shared module `my_formulas.py` (edited)
- Above the old end: only the 2-01 heading «Aṭṭha kāmāvacaramahākusalacittāni» (mahākusala = «မဟာကုသိုလ်», todo).
- New block at the end «Consistency pass»: UDDHACCA, KUKKUCCA, VICIKICCHA, KANKHA, DITTHIGATA, RAGA, KAMARAGA,
  BHAVARAGA, MANA, PATIGHA_AV, KIRIYA, KIRIYA_ATTR, VIMAMSA, PATIPADA, ABHINNA, VINNATTI, KAYAVINNATTI, VACIVINNATTI,
  AKASADHATU, APODHATU, KABALIKARA, RUPA_SANTATI, CITTAJA, CITTAHETUKA, SAMANNAPHALA; the jhāna block JH_* (the 2-02 / 2-03
  tables moved here: JH_FORM, JH_QADJ, JH_Q, JH_KASINAS, JH_PURPOSE, JH_HEADS, JH_LOKX, JH_ARUPA_BASE, JH_BHAVETI,
  JH_UPAS, JH_NIYY_APAC …); HSYN (one synonym table for the akusala factors: the moha, diṭṭhi, vicikicchā, dosa and
  uddhacca lists) and HMEMBERS (the cluster members), with `harm(d)` that puts the shared values into a generator's
  table. make_ch2-02-03, make_ch2-04-05, make_ch3, make_ch4 and make_ch5 read these instead of their own strings.

## Items (Pāli: chosen form; reason; generators changed; uses of the other forms before)
Todo items:
1. **uddhacca** = «ယောက်ယက်ခတ်မှု» (majority; kept apart from kukkucca «နောင်တ ပူပန်မှု» and vikkhepa «ပျံ့လွင့်ခြင်း»).
   2-02-03 (the 4th-path purpose). 1.
2. **vicikicchā** = «ယုံမှားမှု», **kaṅkhā** = «သံသယ» (kaṅkhāyanā «သံသယ ဖြစ်ခြင်း», kaṅkhāyitattaṃ «သံသယ ဖြစ်ထားသော
   အဖြစ်»), saṃsayo = «ဒွိဟ ဖြစ်ခြင်း» (one pair, kept distinct; majority = 4-0x, 75 of 105 vicikicchā uses). 2-04-05,
   5. 32 + 3.
3. **abhiññā** = «ထူးကဲစွာ သိခြင်း» (dandha- / khippa- = «… နှေးကွေးသော / လျင်မြန်သော»; «sayaṃ abhiññā» = «ကိုယ်တိုင်
   ထူးကဲစွာ သိ၍»): the 2-02 / 2-03 jhāna model. 2-04-05, 4. 135 + 127.
4. **kiriyā / kiriya** = «ပြုရုံမျှသာ ဖြစ်သော» (majority: 5 has 152 uses); «kiriyā neva kusalā nākusalā na ca
   kammavipākā» = «ပြုရုံမျှသာ ဖြစ်သော၊ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်၊ ကံ၏ အကျိုးလည်း မဟုတ်သော» everywhere.
   3, 4. 7.
5. **kāmarāga** = «ကာမရာဂ», bhavarāga «ဘဝရာဂ», rāga = «ရာဂ» (4 / 5 majority; one word, as 5); rūparāga /
   arūparāga = «သိမ်မွေ့သော ရုပ်ဘုံ၌ ရာဂ / ရုပ်မရှိသော ဘုံ၌ ရာဂ»; taṇhā stays «… ကို တပ်မက်မှု» (sample bhavataṇhā),
   so kāmataṇhā = «ကာမကို တပ်မက်မှု» is not kāmarāga. 2-02-03, 4. 15 + 7 + 2. māna = «မာန» (4-0x majority). 1.
6. **cluster members** (fetters, knots, hindrances, clingings, āsavas): the Nikkhepa names (majority), built on the
   approved cluster nouns: e.g. «ကာမရာဂ နှောင်ကြိုး», «မုန်းတီးမှု နှောင်ကြိုး», «ယုံမှားမှု နှောင်ကြိုး», «သီလ
   အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှု နှောင်ကြိုး», «… ဟူသော ကိုယ် အထုံး», «ကာမကို လိုလားမှု အတားအဆီး», «ကာမ
   စွဲလမ်းမှု», «အတ္တဟူသော ဝါဒ စွဲလမ်းမှု», diṭṭhiparāmāso «အယူဆိုင်ရာ မှားယွင်းသော ယူဆမှု». HMEMBERS; 5. 37.
7. **wrong-view and moha (and doubt, dosa, uddhacca) synonym lists**: one table (HSYN) = the 4-0x forms (majority,
   e.g. abhiniveso 12 : 2), except dhammavicayasambojjhaṅgo «… ဗောဇ္ဈင်» and maggapariyāpannaṃ «မဂ်၌ အကျုံးဝင်သောအရာ»
   (2-0x majority, 10 : 1 and 29 : 1). diṭṭhigata = «အယူမှား» everywhere (compounds, purposes and the list item:
   96 : 25 : 23). 2-04-05, 4. 39 keys, 49 + 48 uses.
8. **kāya- / vacīviññatti** = «ကိုယ်ဖြင့် / နှုတ်ဖြင့် ထုတ်ဖော်ပြသမှု»; **ākāsadhātu** «ဟင်းလင်းပြင် ဓာတ်»;
   **āpodhātu** «ရေဓာတ်»; **kabaḷīkāro āhāro** «လုတ်ပြု၍ စားရသော အာဟာရ»; also rūpassa santati «ရုပ်၏
   ဆက်လက်ဖြစ်ပေါ်ခြင်း», cittaja «စိတ်မှ မွေးဖွားသော», cittahetuka «စိတ်ကို အမြစ်ပြုသော» (the 3-xx forms). 4, 5.
   12 + 2 + 2 + 4 + 2 + 2.
9. **bahiddhā**: kept, a genuine sense difference. Mātikā / 3-03 / 4 / 5 «သူတစ်ပါး၌» (in others); 2-02 abhibhāyatana
   «ajjhattaṃ arūpasaññī bahiddhā rūpāni passati» = «… ပြင်ပ၌ ရုပ်တို့ကို မြင်၍»: the forms seen outside oneself (the
   kasiṇa objects of the bases of mastery), not «in other beings».
10. **kāyena** (third jhāna) = «စိတ်၏ အဖော်တို့ဖြင့်» (the 2-01 KAYA): decided by sense from the text itself, which
    defines the jhāna's sukha as cetasika sukha («cetasikaṃ sātaṃ cetasikaṃ sukhaṃ»), so the «body» that feels it is the
    mental body; the plain «ကိုယ်ဖြင့်» would say «physically». JH_FORM. 1. For the user's review.
11. **paṭigha**: kept, a genuine sense difference: aversion = «မုန်းတီးမှု» (2-04, 4-0x, 5; 4-0x «စိတ်ထိခိုက်ခြင်း» -> it,
    10 uses), impact = the Mātikā «ထိခိုက်မှု» (sappaṭigha, paṭighasaññā).
12. **mahākusala** = «မဟာကုသိုလ်» (2-01 heading «ကာမဘုံနှင့် ဆိုင်သော မဟာကုသိုလ်စိတ် ရှစ်ပါး»); check_ch2-01 now has
    «မဟာ» in NOT_NEG. 1. mahāvipāka («ကြီးကျယ်သော ကံ၏ အကျိုး») kept: vipāka has no loan in this track.
13. **Jhāna / path / immaterial openings** (2-04-05 rebuilt on the shared JH_* tables, joined as 2-02 / 2-03):
    qualifiers are attributives joined with «၊ » («ကျင့်စဉ် ခက်ခဲသော၊ ထူးကဲစွာ သိခြင်း နှေးကွေးသော ပထမ ဈာန်ကို»; 132
    paṭipadā, 76 suññata / animitta / appaṇihita, 2 adhipateyya); paṭipadā = «ကျင့်စဉ်» (also dukkhanirodhagāminī
    paṭipadā, 4-0x «အကျင့်», 7); suññataṃ «ဆိတ်သုဉ်းသော», animittaṃ «အမှတ်အသား မရှိသော», appaṇihitaṃ «တောင့်တမှု
    မရှိသော»; -ādhipateyyaṃ «X-ကို အကြီးအမှူးပြုသော», vīmaṃsā «စုံစမ်းဆင်ခြင်မှု» (4-0x «စူးစမ်း…», 2); X-kasiṇaṃ «X
    ကသိုဏ်းကို အာရုံပြုသော»; upasampajja viharati «ဝင်စား၍ နေသော» (already one form); the purpose before the
    lokuttara head («အယူမှားတို့ကို ပယ်ရန်၊ ပထမ အဆင့်သို့ ရောက်ရန်၊ လွတ်မြောက်ရာသို့ ပို့ဆောင်သော၊ … ဈာန်ကို
    ပွားများ၍၊ …»; 49 lines of 2-05; ^1-553: three purposes, then the head); rūpūpapattiyā maggaṃ «… ဖြစ်ပေါ်ရန် လမ်းကို»
    (6); samatikkamma «ကျော်လွန်၍» (9); the immaterial bases «အဆုံး မရှိသော ကောင်းကင် / သိစိတ် နယ်ပယ်», «ဘာမျှ မရှိသော
    နယ်ပယ်», «မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်» (also 5 and the 4-02 realm names,
    which were «အာကာသာနဉ္စာယတန / နေဝသညာနာသညာယတန»), X-saññāsahagataṃ «X-ဟု မှတ်သိမှုနှင့်အတူ ဖြစ်သော» moved before
    the jhāna noun (12); iddhipāda «ဣဒ္ဓိပါဒ်» (2); aññindriya «အပြည့်အဝ သိမြင်ခြင်း၏ စွမ်းရည်» (as aññā / aññātāvī
    and the sample's «သိမြင်»; 2-02-03, 5); diṭṭhadhammasukhavihāra «မျက်မှောက်ဘဝ၌ပင် သာယာစွာ နေထိုင်-» (4-0x
    «ချမ်းသာစွာ», sukha = သာယာ); tanubhāvāya «ပါးလျစေရန်», anavasesappahānāya «အကြွင်းအကျန် မရှိအောင် ပယ်ရန်».
    «…nti kusalaṃ / vipāko» (only 2-05): «Q…သော ကုသိုလ် / Q…သော ကံ၏ အကျိုး» with the shared Q. The check_ch2-04-05
    verb count now skips «ရှိသည်လည်း» (as check_ch2-02-03).
14. **Headings and colophons**: harmonise_lines.py finds 0 differing units (headings included). Aligned: Suddhika- =
    «X သက်သက်» (2-05 «သီးသန့် X», 6), «Vīsati mahānayā» = «နည်းကြီး နှစ်ဆယ်» (2), «Rūpakaṇḍe paṭhamabhāṇavāro» =
    «ရုပ် အခန်း၌ …» (as «Nikkhepakaṇḍe …», 1), Tattha = «ထိုတို့အနက်» (3-01 «ထိုတွင်», 1), vuccati = «ဤသည်ကို Xဟု
    ခေါ်သည်» (3-0x «X ဟု», 4).
15. **Source slips**: ^1-850 «dhoso» = ghoso (3-03, same Burmese); patiṭṭhāho = paṭiggāho («ခိုင်မြဲစွာ စွဲကိုင်ခြင်း»,
    2-04, 4-0x); «ः» = «၊» (4-0x); ^1-553 «kāmarā gabyāpādānaṃ» = kāmarāga…; missing commas stay missing (2-02 ^1-165 /
    189 / 204, 2-04 ^1-574 / 579, 4-0x ^1-1059 / 1101), the 4-0x noun series keep the «၊» the agent gave them
    consistently.

Frames of the Nikkhepa / Aṭṭhakathā chapters (align_check: 4-0x vs 5; precedence 1 = the approved Mātikā strings):
16. «ime dhammā X» = «ဤသဘောတရားများသည် {Mātikā X} သဘောတရားများ ဖြစ်ကြသည်» (5 and 2-04 / 2-05 abyākata; kusalā /
    akusalā: noun predicate «… ကုသိုလ် ဖြစ်ကြသည်»; 4-0x had the predicate «… ကြသည်», 80 closers); the same in «Sabbepi
    kusalā dhammā X» and a comma series of bare Mātikā terms before «– ime dhammā» («X သဘောတရားများ၊ …»).
    check_ch4's closer expectation changed on purpose (this form).
17. «Katame dhammā X-vippayuttā Y / na hetū Y» = «X သဘောတရားများအနက် Y …» (the sample's «kho pana» pair; 4-0x
    «X-၍ / X-ဘဲ Y», 34). 18. «Teva / Tāneva / Sveva X …» = «ထို Xများသည်ပင် … သဘောတရားများ ဖြစ်ကြသည်» (sg «… သဘောတရား
    ဖြစ်သည်»; 7). 19. «Cittaṃ na vattabbaṃ – A-ntipi, B-ntipi» = «စိတ်သည် – A သဘောတရားဟုလည်းကောင်း၊ B …ဟုလည်းကောင်း
    ခေါ်ဆို၍ မရ» (5's frame; 2). 20. sāmaññaphala «ရဟန်းအဖြစ်၏ ဖိုလ်» (phala = ဖိုလ်; 1). 21. «yañca rūpaṃ …» = «… ရုပ်
    ရှိသမျှလည်း» (7); «anidassanaṃ appaṭighaṃ» = the Mātikā term «မမြင်နိုင်၊ ထိခိုက်မှုလည်း မရှိသော» (its variant
    reading is the compound; 3-03, 4: 5); avasesa «ကြွင်းကျန်သော» (26); «Sabbeva kāmāvacarā kusalākusalābyākatā dhammā» =
    «… ကုသိုလ်၊ အကုသိုလ်၊ … သဘောတရားများ အားလုံးပင်» (1); «ye ca dhammā kiriyā … , sabbañca rūpaṃ, asaṅkhatā ca dhātu»
    = «… သဘောတရားများလည်း၊ ရုပ် အားလုံးလည်း၊ … ဓာတ်လည်း» (3-01 as 4-01).

## Checks changed (only where a form was changed on purpose)
- check_ch2-01.py: NOT_NEG + «မဟာ» (mahākusala).
- check_ch2-04-05.py: the verb count ignores «ရှိသည်» / «ဖြစ်သည်» followed by a letter (the shared nevasañña phrase).
- check_ch4.py: the «ime dhammā X» closer expectation (item 16); negation weights of the immaterial realm names
  (ākāsānañca- / viññāṇañca- / ākiñcañña- = 1, nevasaññānāsañña- = 3, as check_ch2-02-03).
- check_ch5.py: the «ti / tipi» count ignores «အမှန်ဟု» inside the shared kāyagantha name (idaṃsaccābhiniveso).

## Kept (CHECKED in the table; sense or grammar)
bahiddhā, paṭigha (items 9, 11); sineho (cohesion / affection); niyatā (Mātikā «ကျိန်းသေသော» / ajjhatta list «သီးသန့်
ဖြစ်သော»); nāmaṃ («အမည်» / «စိတ်ပိုင်း»); mahāvipāka; the grammatical variants harmonise_tables.py lists in KEEP
(attributive / noun / accusative forms of one key). For the user's review: kāyena = mental body (item 10), and
micchādiṭṭhi «မှားယွင်းသော အယူ» beside diṭṭhigataṃ «အယူမှား» in one list (distinct strings, both «wrong»).
