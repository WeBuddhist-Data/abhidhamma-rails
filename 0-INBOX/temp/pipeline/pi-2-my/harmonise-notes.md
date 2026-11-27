# Consistency pass: pi-2 Burmese zero-shot (Vibhaṅga «ခွဲခြမ်းစိတ်ဖြာခြင်း»), 19 chapter files (2026-11-18)

One Pāli item = one Burmese form across the book. Every change was made in the generators or in the shared module
`my2_formulas.py`; every chapter was rebuilt from its generator; nothing was edited by hand in a chapter file. Pāli only
(no Burmese translation or nissaya, `0-INBOX/temp/language-priority/` not opened, no web search); `pi-1-my/` read only.
Nothing committed.

## How it was done
- Backups before the pass: `harmonise-backup/` (the 8 generators, the 8 checks, `my2_formulas.py`,
  `my2-zeroshot-terms.md`, the agents' notes) and `harmonise-backup/chapters-before/` (the 19 chapter files). The
  generators reproduced the chapter files byte for byte before any change (baseline run).
- Shared values: a new block «consistency pass» at the END of `my2_formulas.py` (nothing above it changed; the
  approved sample strings are untouched: preamble and ch1 0 lines changed, `my2-zeroshot-terms.md` byte-identical).
  It holds VIEW10 (the ten views read from the final pi-1 text), TI_VA, SIG_UNKNOWN, UPAPATTI, ADHIMOKKHA, UPK, TRUTH,
  PAJANATI, CITTA16, SPEECH, VIHIMSA, SANKAPPA, VITIKKAMA, SUTTANTA + BYASANA_HEAD, SANGATI, CETOVIMUTTI, ADINNADANA,
  FEEL_SYN, VIEW_NAMES. The generators read them (each changed spot is marked «consistency pass» in the code).
- Rebuild + every check: `regen_zeroshot.sh` (a generator that stops on a missed line now fails the run). A second run
  changes no chapter byte (md5 of the 19 files equal).
- Scans written for the pass: `harmonise_pi1.py` (pi-1 identity: every pi-2 sentence and heading that occurs in pi-1 =
  pi-1's final Burmese, from `pi-1-burmese-plain-rails_split_chapters`), `harmonise_scan.py --table` (every item,
  before vs now, writes `harmonise-table.tsv`), `harmonise_lists.py` (synonym lists in the output: the same Pāli item =
  the same Burmese item; no two synonyms of one list sharing one Burmese item), `harmonise_align_kept.py` (every
  difference align_check still reports must be explained), `harmonise_align_diff.py` (word-level view of align_check),
  `harmonise_tables.py [--p1]` (the generators' tables compared key by key, also against the pristine pi-1 tables),
  `harmonise_diff.py [-v ch]` (lines changed vs the backup), `grep_pm.py` (Pāli regex -> Burmese line / sentence).

## Result
- Lines changed: 98 in 13 files: 2: 3, 3: 5, 4: 13, 5: 1, 6: 5, 7: 1, 11: 2, 12: 4, 14: 10, 15: 2, 16: 1, 17: 35,
  18: 16; preamble, 1 (the approved sample), 8, 9, 10, 13: 0.
- align_check: 83 differing sentences before (`align-before.txt`), 73 now (`align-after.txt`): 71 are ch1 (the approved
  sample) «Atthi X, atthi Y …» sentences whose Pāli has no subject (the subject is the aggregate of the section:
  ခံစားမှု / မှတ်သိမှု / ပြုပြင်ဖန်တီးမှု / သိစိတ်; nothing else differs), 2 are kept for context (below); 0 unexplained.
- align_hidden: 0 unmatched before and now (83 uneven lines; `align-hidden-before.txt`, `align-hidden-after.txt`).
- pi-1 identity (`harmonise_pi1.py`): 321 / 321 before and now (`harmonise-pi1-before.txt`).
- Items: 44 changed / aligned (12 source slips, 31 term / list items, 1 frame), 19 checked and kept;
  `harmonise_scan.py`: other forms left 0. `harmonise_lists.py`: 1624 list items, 0 with more than one Burmese
  (1 kept: rūpataṇhā), 0 shared inside a list.
- All checks pass: check_chapter_ids, pi-6-mr/check_text_pe.py, pi-4-mr/check_marks.py OK on 19 files (chk-pe copies
  deleted by the script); check_sample, check_ch2-4, check_ch5-7-11, check_ch6, check_ch12-14, check_ch15-16,
  check_ch17, check_ch18: 0 mismatches, pi-1 reuse 2/2 + 14/14, 4/4 + 2/2 + 2/2, 16/16, 121/121, 52/52 + 18/18 + 2/2,
  23/23 + 17/17, 56/56, 20/20.
- Checks changed on purpose (only where a form was changed on purpose): `check_ch2-4.py` SLIPS no longer re-reads the
  three content slips («no ca na kilesā», «atthi ahetu», «ajjhattaṃ») and counts «ahetu» as a negation;
  `check_ch18.py` SLIPS empty (^2-1039 as written) and «dukkhamasukh-» counted as one negation.

## Decision rules
harmonise-todo.md precedence: (1) pi-1 final Burmese for identical Pāli (rails text, locked termbase); (2) the approved
pi-2 sample; (3) the majority of the chapters (uses counted in the output); (4) the plainest. The user's slip rule:
content slips are translated as written; a pure spelling slip may keep the intended word; no punctuation the Pāli
lacks is added. Grammar (number of the subject, case) is not counted as drift.

## A. Source slips (translated as written: reverted)
1. ^2-171 «"saṃyojanañceva saṃyojaniya"ntipi» (ca missing): «“နှောင်ကြိုးလည်း ဖြစ်၊ နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်သော
   သဘောတရား”» (no «လည်း» for the missing ca). make_ch2-4 (T entry). 1 line.
2. ^2-171 «"upādāniyañceva upādānasampayuttañcā"ti» (was read upādānañceva): «“စွဲလမ်းမှု၏ အာရုံလည်း ဖြစ်နိုင်၊
   စွဲလမ်းမှုနှင့်လည်း ယှဉ်တွဲသော သဘောတရား”» (pi-1 CEVA pattern). make_ch2-4. 1.
3. ^2-171 «siyā upādānasampayuttaupādāniyā» (was read -vippayutta-): «စွဲလမ်းမှုနှင့် ယှဉ်တွဲသော သဘောတရားများအနက်
   စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော» (pi-1 ^1-1087 two-term form). make_ch2-4. 1.
4. ^2-171 «kilesasampayuttā ceva no ca na kilesā» (was read «no ca kilesā»): «… ကိလေသာ မဟုတ်သည် မဟုတ်သော» (the double
   negative). make_ch2-4, check_ch2-4. 1.
5. ^2-184 «atthi hetu, atthi ahetu» (was read «na hetu»): a-hetu = not a root, Burmese «အမြစ် မဟုတ်သော» (the same words
   as na hetu; the reading is removed, the word is mapped as written). make_ch2-4, check_ch2-4. 0 lines.
6. ^2-188 «na vattabbā – "parāmāsā ceva parāmaṭṭhā cāti parāmaṭṭhā ceva no ca parāmāsā".» (was split into two items,
   the second rendered as a statement «… ” ဖြစ်ကြသည်»): ONE quotation, the inner «ti» = «ဟု», no «ဟု» after the closing
   quote: «– “A ဟု B” ခေါ်ဆို၍ မရ။». make_ch2-4 (sentence rule). 1.
7. ^2-206 Dukaṃ «Dve saccā nīvaraṇiyā dve saccā anīvaraṇiyā.» (stop / comma missing): no «၊» added. make_ch2-4. 1.
8. ^2-206 Dukaṃ «Dukkhasaccaṃ siyā ajjhattaṃ, siyā bāhiraṃ» (was read ajjhattikaṃ): ajjhatta «မိမိ၌ ရှိသော» (pi-1),
   not ajjhattika «အတွင်းပိုင်း». make_ch2-4, check_ch2-4. 1.
9. ch5 ^2-223 «siyā parittārammaṇaṃ siyā mahaggatārammaṇaṃ» and ch7 «Siyā vipākā siyā vipākadhammadhammā» (comma
   missing): the «၊» the agent supplied removed. make_ch5-7-11 (r_siya_ns). 2.
10. ^2-711 «kāmāvacare kusalaṃ cittaṃ» (was read kāmāvacaraṃ): the locative as written «ကာမဘုံ၌ ကုသိုလ်စိတ်». make_ch12-14. 1.
11. ^2-974 / ^2-976 taṇhāvicarita «… vā yathā so …» (comma missing): the supplied «၊» removed. make_ch17. 2.
12. ^2-1039 «siyā dukkhamasukhāya» (was read adukkhamasukhāya): as written «နာကျင် မသာယာသော ခံစားမှုနှင့် ယှဉ်တွဲသော».
    make_ch18, check_ch18. 1.

Kept (spelling slips, as the rule allows; or already as written), logged: jīvhindriyampetaṃ, Sattadhātuyo, «micchā
ājīvā», the stray spaces («" tipi», «nti pi», «…pe…»), ^2-933 bhavantattaṃ (= pi-1 bhantattaṃ), ^2-273 abhinibbati,
^2-277 akusamūlaṃ, ^2-688 muditāyatanā, ^2-508 ākiñcāyatanaṃ, ^2-749 apaṭighā, ^2-753 anuppādinn- / ajjhatā,
ch5 arūpajīvatindriyaṃ, ch9 viññāṇakhandho / Tathābhūtasa / maggariyāpannaṃ, ^2-717 sahetūkā / bhāvanāyapahātabbā:
one letter, joined / split word or stray space, the word unchanged. ^2-517 «Ñatvādhikaraṇamenaṃ»: the sentence differs
from pi-1's «Yatvādhikaraṇamenaṃ manindriyaṃ …» in this one letter only (checked), pi-1's Burmese kept. ^2-245
upādānasampayuttaṃ: already as written («စွဲလမ်းမှုနှင့် ယှဉ်တွဲသော စွဲလမ်းမှု»). ^2-576 «santā hoti»: singular kept
(as written). ^2-974 (7) «– evaṃ bhavissanti hoti»: one «evaṃ» rendered once (as written; the agent's note describes
another form than its output, the output is as written). ^2-777 upariṭṭhimā (variant -e): the adjective's ending is
not visible in the Burmese attributive. ch10 ^2-478 stray «yo»: a relative without its clause, not rendered (logged).
The other slip lists of ch5–7–11, ch6, ch15–16, ch17, ch18 were checked: as written.

## B. Term drift (chosen form; reason; generators; other-form uses before -> now)
1. Suttanta definitions of birth … despair, one table for ch4 and ch6 (`F.SUTTANTA`, `F.BYASANA_HEAD`):
   sattanikāya «ထိုထို သတ္တဝါ အမျိုးအစား၌ / မှ» (plainer for nikāya; ch4 had «အပေါင်း»; 3 -> 0);
   abhinibbatti «ထင်ရှားစွာ ပေါ်ထွက်ခြင်း» (pi-1 abhinibbattā; 1 -> 0); khandhānaṃ pātubhāvo «အစုအဝေးတို့၏ ထင်ရှား လာခြင်း»
   (ch18 pātubhavanti; «ပေါ်ထွက်» is abhinibbatti's word; 1 -> 0); «X-byasanena vā phuṭṭhassa» «X ပျက်စီးခြင်းဖြင့်
   ထိခိုက်ခံရသူ၏ဖြစ်စေ», samannāgatassa «ကြုံတွေ့နေရသူ၏», dukkhadhammena phuṭṭhassa «ဆင်းရဲဖွယ်ရာဖြင့် ထိခိုက်ခံရသူ၏»
   (ch6, plainer than «တွေ့ကြုံရသူ / ပြည့်စုံသူ»; 21 -> 0); antoparisoko «အတွင်း ပြင်းစွာ စိုးရိမ်ခြင်း» (pari- as
   upāyāso «ပြင်းစွာ»; 1 -> 0); parideva «… စကား၊ ပေါက်ကရ ပြောခြင်း၊ ကမောက်ကမ ပြောခြင်း၊ မြည်တမ်းခြင်း …» (ch4: one
   Burmese item per Pāli word; ch6 joined «vācā palāpo»; 4 -> 0); no «ရှိသမျှ» where the list has no relative (ch4;
   3 -> 0); cuti «စုတေခြင်း» (one form already). make_ch2-4, make_ch6.
2. upapatti (noun) «ပြန်လည် ဖြစ်ပေါ်ခြင်း», upapattibhavo «ပြန်လည် ဖြစ်ပေါ်ခြင်း ဘဝ» (ch18 majority, 55 lines; pi-1 upapattiyā
   «ဖြစ်ပေါ်ရန်»); ch6 had «ပဋိသန္ဓေ ဘဝ». make_ch6. 4 -> 0.
3. adhimokkha «ဆုံးဖြတ်မှု» (ch6, 150 uses); ch18 «ဆုံးဖြတ်ချက်». make_ch18. 1 -> 0.
4. The four truths as written: «ဒုက္ခ သစ္စာ», «ဖြစ်ပေါ်ခြင်း သစ္စာ», «ချုပ်ငြိမ်းခြင်း သစ္စာ», «မဂ် သစ္စာ» (ch4, 41 / 40 uses;
   the Pāli samudayasaccaṃ has no dukkha-); ch18 added «ဒုက္ခ». make_ch18. 19 -> 0.
5. upādānakkhandha «စွဲလမ်းမှု၏ အာရုံ ဖြစ်သော အစုအဝေး» (ch4, ch7); ch12 «… ဖြစ်နိုင်သော». make_ch12-14. 1 -> 0.
6. The ten views (identical Pāli): the final pi-1 items read from pi-1 4-01 (`F.VIEW10`): tathāgata «မြတ်စွာဘုရား»,
   «လောကသည် ထာဝရ တည်မြဲသည်», «အသက်သည် ကိုယ်ခန္ဓာပင် ဖြစ်သည်» …; and the pi-1 frame «X"ti vā» = «Xဟူ၍ဖြစ်စေ»
   (`F.TI_VA`) for every «ti vā» of ch17 (ch17 had «တထာဂတ», «လောကသည် မြဲ၏», «ဟုဖြစ်စေ»). The «ဟုဖြစ်စေ» left in ch17
   (187) are «X vā» without «ti» in the sakkāyadiṭṭhi frame, exactly pi-1's own form. make_ch17. 21 -> 0.
7. pi-1 suttantika view names (identical Pāli, pi-1 SUT): bhavadiṭṭhi «ဘဝ ဆက်လက် တည်ရှိသည်ဟူသော အယူ», vibhavadiṭṭhi, sassata-,
   uccheda-, antavā-, anantavā-, pubbantānu-, aparantānu-diṭṭhi (`F.VIEW_NAMES`); ch17 had its own. make_ch17. 12 -> 0.
8. The editors' «(?)» «(အမည်မသိ မူ)» (ch17, ch18: 4 uses); ch3 «(ရင်းမြစ် မသေချာ)». make_ch2-4, make_ch17, make_ch18. 1 -> 0.
9. nekkhamma- / abyāpāda- / avihiṃsāsaṅkappo «X-ဆိုင်ရာ ကြံစည်မှု», avihiṃsā «ညှဉ်းပန်းမှု မရှိခြင်း» (pi-1 vihiṃsā; ch3,
   ch4, ch12, ch17; ch11 had «ညှဉ်းဆဲလိုစိတ်», which is abyāpajja's word in ch6 / ch13); ch4 had «X-ကို ကြံစည်မှု».
   make_ch2-4, make_ch5-7-11. 4 -> 0.
10. The wrong speeches (ch17, 4 lists): musāvāda «မုသား ပြောခြင်း», pisuṇā vācā «ကုန်းတိုက်သော စကား», samphappalāpa
    «အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား» (pharusā vācā one form already); adinnādāna «မပေးသည်ကို ယူခြင်း» (ch4, ch11, ch17).
    make_ch2-4, make_ch5-7-11, make_ch12-14. 16 -> 0.
11. sammāājīvena jīvikaṃ kappeti «… အသက်မွေး၏» (ch11; ch4 split the word). make_ch2-4. 1 -> 0.
12. kāyiko / vācasiko / kāyikavācasiko (a)vītikkamo «ကိုယ်ပိုင်းဆိုင်ရာ / နှုတ်ပိုင်းဆိုင်ရာ / ကိုယ်ပိုင်းဆိုင်ရာနှင့်
    နှုတ်ပိုင်းဆိုင်ရာ (မ)ကျူးလွန်ခြင်း» (pi-1 kāyika «ကိုယ်ပိုင်းဆိုင်ရာ»; ch17); ch12 «ကိုယ်ဖြင့် …». make_ch12-14. 9 -> 0.
13. The sixteen states of mind (ch7 cittānupassanā = ch16 cetopariyañāṇa, `F.CITTA16`) and (bhikkhu) pajānāti
    «ကွဲပြားစွာ သိ၏» (pi-1 pajānanā «ကွဲပြားစွာ သိခြင်း»; ch7); ch16 had «သိသည်», «တွန့်ဆုတ်သော», «ပျံ့လွင့်သော».
    The Tathāgata's «သိတော်မူသည်» (honorific) is kept. make_ch5-7-11, make_ch15-16. 21 -> 0.
14. -cetovimutti «… စိတ်လွတ်မြောက်မှု» (ch13, 40 uses); ch3 «စိတ် လွတ်မြောက်ခြင်း». make_ch2-4, make_ch12-14. 2 -> 0.
15. saṅgati «စုဝေးခြင်း», samāgamo «ဆုံဆည်းခြင်း», samodhānaṃ «ပေါင်းစည်းခြင်း» (+ the a- forms; ch6, 5 uses each); ch4 used
    the same Burmese words for other Pāli words. make_ch2-4. 4 -> 0.
16. khīraṃ «နွားနို့», sappi «ထောပတ်ကြည်» (pi-1 names); ch3 «နို့», «ထောပတ်ဆီ». make_ch2-4. 2 -> 0.
17. gehasitaṃ cetasikaṃ sātaṃ … (ch17): the pi-1 feeling synonyms (`F.FEEL_SYN`: «စိတ်ပိုင်းဆိုင်ရာ နှစ်သက်ဖွယ်ကောင်းမှု»,
    «… နှစ်သက်ဖွယ်ကောင်း၍ သာယာသော ခံစားရခြင်း» …); ch17 had «စိတ်၌ ဖြစ်သော ချမ်းသာမှု» etc. make_ch17. 16 -> 0.
18. Frame: the multi-citta opening «Yasmiṃ samaye KIND uppannaṃ hoti Q…pe… Q sasaṅkhārena…pe… OBJS» (ch14, ch15): the
    pi-1 single-opening order (objects first, «Q KIND-သည် [ADV] ဖြစ်ပေါ်ပြီးသော အချိန်၌»: ch14) and no «၊» before the
    adverb «တိုက်တွန်းမှုဖြင့်» (ch15); ch15 put KIND first, ch14 a «၊» before the adverb. make_ch12-14, make_ch15-16.
    17 -> 0 (this also clears the align_check difference 14:24 / 15:23).

## Checked and kept (genuine sense / context differences; also in harmonise-table.tsv as CHECKED)
- dukkhaṃ, label of «Yaṃ kāyikaṃ asātaṃ … – idaṃ vuccati "dukkhaṃ"» (align_check): ch4 / ch6 «ကိုယ်ဆင်းရဲခြင်း» (the
  dukkha of «soka-parideva-dukkha-domanass-upāyāsā», pi-1 final) vs ch12 «နာကျင်မှု» (the dukkha of «dukkhassa ca
  pahānā», pi-1 final): the label names the word being defined.
- «Tattha katamaṃ saṅkhārapaccayā viññāṇaṃ?» (align_check): 6:10 suttanta «ပြုပြင်ဖန်တီးမှုများကြောင့်» (saṅkhārā plural,
  pi-1 final 4-03) vs the abhidhamma exposition (saṅkhāro singular).
- rūpasaññā: jhāna formula «ရုပ်ဟု မှတ်သိမှု» (ch12, ch16, ch17) vs the six-object list «အဆင်းအရောင်ဟု မှတ်သိမှု».
- rūpataṇhā: six-object list «အဆင်းအရောင်ကို တပ်မက်မှု» vs kāma / rūpa / arūpa-taṇhā «သိမ်မွေ့သော ရုပ်ဘဝကို တပ်မက်မှု».
- kāyopi passambhati (ch10) «ကိုယ်လည်း ငြိမ်းအေး၏»: no identical pi-1 sentence; pi-1 termbase kāyo «ကိုယ်»; pi-1's
  «စိတ်၏ အဖော်တို့» for kāyapassaddhi is that compound's own definition (^1-320), not stated in this sentence.
- idha: «ဤသာသနာ၌» (a monk / disciple, pi-1 ^1-1377) vs «ဤလောက၌» (anyone, pi-1 Idhekacco).
- hadayaṃ: the organ «နှလုံး» (body list) vs «နှလုံးသား» (pi-1 citta synonym).
- attha (ch15): «အကျိုးအနက်» kept for both (one compound covering result and meaning; the Pāli does not split them);
  «atthaṃ carati» (benefit) «အကျိုး» in ch17.
- cuti: «စုတေခြင်း» in the maraṇa lists (one form already); pi-1 cuti «သေခြင်း» kept in ch16 cutūpapāta: in the maraṇa
  list «သေခြင်း» is maraṇaṃ, two synonyms of one list may not share it.
- «na vattabbā A-tipi, B-tipi»: one frame «… ဟု(လည်းကောင်း) … ခေါ်ဆို၍ မရ» everywhere; quotes and dash follow the Pāli
  per line (check_marks OK, 19 files).
- Chapter titles «X ကို ခွဲခြမ်းစိတ်ဖြာခြင်း»: one pattern; the ch15 variant note names ch3 as ch3's title
  «“ဓာတ်များကို ခွဲခြမ်းစိတ်ဖြာခြင်း”». Headings and colophons (Suttanta- / Abhidhammabhājanīyaṃ, Pañhāpucchakaṃ, -niddeso,
  -mātikā, Catukkaṃ / Pañcakaṃ, X niṭṭhito): each Pāli heading has one Burmese (372 headings scanned).
- Grammar, not counted as drift: the predicate noun / number of the pañhāpucchaka items follows the subject (ch16
  «ပညာ», where the Pāli predicate agrees with paññā); «kāmasineho» «ကာမကို ချစ်ခင်မှု» is pi-1's own (^1-1159).

## Left
Nothing unexplained: align_check 73 = 71 topic noun (ch1, approved sample, no subject in the Pāli) + 2 context;
harmonise_scan 0 other forms; harmonise_lists 0. The ch17 «ဟုဖြစ်စေ» of «X vā» without «ti» (sakkāyadiṭṭhi frame) is
pi-1's own form and stays.
