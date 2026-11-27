# pi-7 Burmese zero-shot (Paṭṭhāna «အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»): consistency pass — notes

Brief: harmonise-brief.md; items: harmonise-todo.md (H1–H24). Started 2026-11-24. Not committed.
Backups (before any edit): harmonise-backup/code/ (every make_*.py, check_*.py, my7_formulas.py, chk_mutate.py,
write_terms.py) and harmonise-backup/chapters/ (the 75 chapter files incl. the preamble).
align-before.txt / align-hidden-before.txt saved from the published state before any change
(1074 repeated sentences, 24 differing; hidden 1361 uneven lines, 0 unmatched).

Import chain (regen_zeroshot.sh header): sample <- my7_formulas; 1-01, 1-03-05 <- sample; 2-01-02 <- 1-03-05;
2-03-06 <- 1-01 + 1-03-05; 2-07-11 <- 2-01-02; 2-12-17, 3-01-02 <- 2-03-06; 3-03-06, 3-07-08-10 <- 3-01-02;
3-09 <- 3-03-06; 4-01 <- 3-07-08-10; 4-02-09 <- 2-07-11 + 2-12-17 + 3-03-06 + 3-07-08-10; 4-10-14 <- 3-09 + 4-01 +
4-02-09; 4-15-21 <- 4-10-14; 5-01-04 <- 2-07-11 + 2-12-17 + 3-09 + 4-01; 5-05-12, 5-13-20 <- 5-01-04.

## Progress log
- [x] backups, align before
- [x] baseline rebuild byte-identical (regen-run0.txt)
- [x] H1 … H24 (decisions below)
- [x] repeated sentences (align 24 → 0, hidden 0 → 0) / identity (harmonise_pi123456.py: all identical)
- [x] checks updated where a form changed on purpose (4 checks, listed below)
- [x] regen twice (regen-run1.txt, regen-run2.txt: ALL CHECKS PASSED both; md5-run1.txt = md5-run2.txt: the second run
  changed no byte of the 75 chapters, the merged file or my7-zeroshot-terms.md), merged file written

## Items
(Work log, 2026-11-24: baseline rebuild with the unchanged generators = the 75 backed-up files, byte-identical
(regen-run0.txt; the baseline check run was stopped after the rebuild and --regress, all OK so far). Edits below were
made in this order; every edit carries a «harmonise H…» comment in its file.)

### Edits made (generator: item)
- my7_formulas.py: H2 (_lex_item: a kind-«n» noun before a postposition takes no «သည်»), H6 (np_parse: two term
  slots side by side «A၊ B N»).
- make_ch1-01.py: H4 (tassa paṭighātatthāya «ထိုအမှုကို ချေဖျက်ရန်»), H5 (KAMMA5 = pi-5 deeds), H9 (sekkhā vā
  puthujjanā vā «…တို့ဖြစ်စေ၊ …တို့ဖြစ်စေ»), H17 (kamma-line «Sahajātā –» label without a Kammapaccayo heading).
- make_ch1-03-05.py: H1 (HLINES «Anulomaṃ.»), H3 (asaññasattānaṃ «…တို့၏»), formless minds as 1-01 (align),
  H11 / H16 / H9 (bits(): NP-nom NP-dat before «…» tried before the one-list reading).
- make_ch2-01-02.py: H10 (anumajjantena «ပြန်လည် စိစစ်လျက်»), H14 (bare evaṃ «ဤသို့»: 2 notes).
- make_ch2-03-06.py: H18 (chandarāga «လိုလားမှု ရာဂ»), H16 (ajjhattika attributive «အတွင်းပိုင်း»).
- make_ch2-07-11.py: H14 («(evaṃ gaṇetabbaṃ)» «(ဤသို့ ရေတွက်ရမည်)»), H6 (compound term stacks «A၊ B»).
- make_ch3-01-02.py, make_ch3-03-06.py, make_ch3-09.py: H19 (bare «X-sadisa» = bare name).
- make_ch3-07-08-10.py: H22 (heṭṭhā «ရှေ့၌»), align («yathā … evaṃ kātabbaṃ ninnānākaraṇaṃ» = 3-03 order, 4 notes).
- make_ch4-01.py: H20 (labbhati «တွေ့ရသည်»).
- make_ch4-02-09.py: H20 (vāra list before «vitthāretabba…» «Xကိုလည်း»), H24 («…paṭiccavārasadisaṃ» «…နှင့် တူသည်»).
- make_ch4-10-14.py: H22 (HETTHA «ရှေ့»).
- make_ch4-15-21.py: H20 (object list), H14 («evaṃ vitthāretabbaṃ» «ဤသို့»).
- make_ch5-01-04.py: H24 («yathā kusalattike pañhāvāraṃ, evaṃ …» «…ကဲ့သို့ ထိုနည်းတူ»).
- make_ch5-05-12.py: H23 («{hetuyā aṭṭha?}» «{ပါဌ်ကွဲ ((မသေချာ)): hetuyā aṭṭha}»).

### H8 supplied words (rule: supply only where the Pāli has an obvious omission)
Checked every supplied word the groups logged (notes-*.md «suppl…»). KEPT (each fills an evident ellipsis of the
formula, or the head noun of a substantivised adjective that Burmese cannot leave without a head):
1. 1-04 «khandhe paṭicca vatthu, vatthuṃ khandhā»: the second pair's link «မှီ၍» (the paṭicca of the pair carried over).
2. 1-03 … 1-05, 2-01 … 2-02, 2-07 … 2-11: «X-assa ca Y-assa ca Zpaccayena» / a bare term before «…dhammaṃ» with the
   noun left out: «သဘောတရား» (the frame's noun; the Burmese term is an attributive «…သော» and needs its head).
3. 2-04 two missing link words («paccayā» in the paccayavāra, «saṃsaṭṭho» in the saṃsaṭṭhavāra): the formula word of
   that vāra, evident from every other sentence of the vāra.
4. 2-03 «(ajjhattikā mahābhūtā ca āhārasamuṭṭhānañca)», 3-09 «(yāva utusamuṭṭhānaṃ)», 4-01 «mahābhūte paccayā
   cittasamuṭṭhānaṃ», 5-05-12 «(cittasamuṭṭhānameva …)»: «ရုပ်» (the substantivised «-samuṭṭhāna» = rūpa).
5. 3-05 «(dve āvajjanā kātabbā, paṭhamo natthi)», 3-09 «paṭhamasseva …»: «ပြဿနာ» (masculine ordinal = pañho).
6. 3-01 «(vitthāretabbaṃ yāva. Nahetū khandhā)»: «အောက်ပါ» before «အထိ» (yāva has its object after the source's
   full stop; Burmese «…အထိ» cannot stand without an object; the stop is kept as written).
7. 5-13-20 «သဘောတရား» after a term used as a noun in a note («Kusale pañca» …) (head of an attributive term).
8. 5-01-04, 4-02 …: «သဘောတရား» after «-dhammadhamma» terms: the noun is inside the compound (not supplied).
REMOVED: none (no logged supplied word lacks an evident omission). Kept 8 kinds, removed 0.

### Decisions per item (chosen form — reason — generators — lines before → now)
Counts are from harmonise_scan.py (lines that carry the Pāli item; «other forms» uses before → after).
- H1 «Anulomaṃ.» (order) = «အဟုတ်ပြ ပုံစံ။» — coordinator decision (1-01, 2-07 … 2-11). make_ch1-03-05.py HLINES
  (2-01-02 inherits). 12 lines (1-03 2, 1-04 4, 1-05 1, 2-01 3, 2-02 2). The mind moment keeps «လျော်ညီခြင်း စိတ်»;
  in 2-01 two lines had it as an object «…စိတ်ကို» before «X-assa vitakkassa ca»: now the subject «…စိတ်သည်»
  (make_ch2-01-02.py prep token + LEX). 2 lines.
- H2 «…မှုသည်ကို» = «…မှုကို» — a stray «သည်» (rule: a kind-n noun before a postposition has no case of its own).
  my7_formulas.py _lex_item. Also fixes the same slip «ပထမ ဈာန်သည်ကို / … ဉာဏ်သည်ကို လေးစားဖွယ်ရာ» (2-07, 4-01) and
  «စိတ်ဆင်းရဲမှုသည်ကို» (1-05, 2-03, 2-04 …). 2-03-06's KNOWN_DIFF line now identical.
- H3 asaññasattānaṃ = «အသညသတ်တို့၏» — every use is «asaññasattānaṃ (ekaṃ) mahābhūtaṃ …» (possessive genitive);
  majority (171 / 60); pi-5 «…၌» answers an existence question (another case use). make_ch1-03-05.py ASANNA.
- H4 tassa paṭighātatthāya = «ထိုအမှုကို ချေဖျက်ရန်» — no locked term; «ရန်» already gives atthāya; paṭighāta is
  counteraction (plainest correct; = 1-03 … 1-05, 2-07 … 2-11). make_ch1-01.py GERUND.
- H5 heinous deeds = pi-5 «အမိကို သတ်ခြင်း ကံ», «အဖကို …», «ရဟန္တာကို …», «ဘုရား၏ ကိုယ်တော်မှ သွေးကို ထွက်စေခြင်း ကံ»,
  «သံဃာကို သင်းခွဲခြင်း ကံ» — binding (pi-5). make_ch1-01.py KAMMA5 (W() witnesses). 4-01's in-memory override is now
  the same value.
- H6 two terms on one noun = «A၊ B N» (the coordinator's stacking pattern) — also for two terms side by side
  without «ca» (2-07 / 2-08 «appamāṇārammaṇe paritte khandhe», «kusalaṃ appamāṇaṃ», 2-01 «vipākaṃ
  avitakkavicāramattaṃ», the compounds «…ārammaṇa…cittasamaṅgissa», «maggahetukamaggādhipati-»). A descriptive
  qualifier before a term («ahetukaṃ parittaṃ», «ahetukaṃ vipākābyākataṃ») keeps the space (approved sample).
  my7_formulas.py (np_parse, lex join), make_ch2-07-11.py COMBO. The sample regenerates byte-identical.
- H7 / H17 kamma-kind label in a kamma line = «အတူ ပေါ်ပေါက်သည့် ကံ –» (decided). make_ch1-01.py (kamma line
  detection). 11 lines (3-07 1, 3-08 2, 3-09 6, 3-10 2). Outside the kamma lines the bare name stays (201 labels).
- H8 see the H8 section above: 8 kinds kept, 0 removed.
- H9 the 3 shared sentences: «rūpāyatanaṃ cakkhuviññāṇassa…pe…» and «kabaḷīkāro āhāro imassa kāyassa…pe…» =
  conditioning «…သည်» + conditioned «…အား» (with H11); «sekkhā vā puthujjanā vā» = «…တို့ဖြစ်စေ၊ …တို့ဖြစ်စေ» (pi-1's
  «vā … vā» «…ဖြစ်စေ၊ …ဖြစ်စေ», precedence 1). make_ch1-03-05.py bits(), make_ch1-01.py.
- H10 anumajjantena = «ပြန်လည် စိစစ်လျက်» — no locked term; most chapters (2-03, 2-15, 3-01 vs 2-01, 2-02).
  make_ch2-01-02.py ANUMAJJ. 8 uses.
- H11 «X Y-assa…pe…» before «…» = conditioning / conditioned — make_ch1-03-05.py bits(): the NP-nom NP-dat frame is
  tried before the one-list reading (1-03 … 2-02, 2-07 … lines; 3-02 ^565 / ^848 too: H16).
- H12 «dve mahābhūtā» = «မူလဓာတ်ကြီး နှစ်ပါး» — verified: no «နှစ်ခု မူလဓာတ်ကြီး» anywhere (no change).
- H13 shared-count runs: verified one pattern book-wide (731 lines, never «၊» before the shared count; no change).
- H14 «evaṃ» without «yathā» = «ဤသို့»; «yathā … evaṃ» = «…ကဲ့သို့ / …အတိုင်း ထိုနည်းတူ» — the 2-03 … 2-06 lineage
  and 140 / 45 uses before. make_ch2-07-11.py «(evaṃ gaṇetabbaṃ)» (45 + 1 lines 2-07, 2-08, 2-10, 2-11),
  make_ch2-01-02.py (2 notes), make_ch4-15-21.py «evaṃ vitthāretabbaṃ» (4-18, 4-20: 4 lines). 1-05 lines 81 / 116 are
  H11 (done).
- H15 the sixth-dyad terms: 3-03-06 and 3-07-08-10 agree («X-နှင့် ကင်းကွာသော်လည်း X၏ အာရုံ ဖြစ်နိုင်သော» /
  «X-နှင့် ကင်းကွာ၊ X၏ အာရုံ မဖြစ်နိုင်သော»; every later group reads them from there). heṭṭhā: see H22.
- H16 3-02 ^565 / ^848 (and 3-09 ^249 / ^2625 already): subject + recipient «A လည်းကောင်း၊ B လည်းကောင်း C အား» (bits(),
  H11). ajjhattika attributive = the locked «အတွင်းပိုင်း» («အတွင်းပိုင်း မူလဓာတ်ကြီး», «အတွင်းပိုင်း စွမ်းရည်»; = the
  3-09 dyad term): make_ch2-03-06.py AJJHATTIKA (3-01-02, 4-01 read it). 21 uses.
- H17 see H7.
- H18 chandarāga = «လိုလားမှု ရာဂ» — locked pi-2 termbase (same sense, own / others' property; pi-5 the same).
  make_ch2-03-06.py CHANDARAGA (4-01 inherits). 14 uses (2-03, 2-04, 4-01).
- H19 a bare «X-sadisa» (no «paccaya» in the Pāli) = the bare name «Xနှင့် တူ…»; with «paccaya» «Xဟူသော
  အကြောင်းနှင့် တူ…» — the book-wide majority (112 bare / 19). make_ch3-01-02.py (3), make_ch3-03-06.py (6),
  make_ch3-09.py (7 entries). The «(sahajātaṃ sahajātasadisaṃ, …)» notes of 3-10 / 4-01 were already bare.
- H20 a vāra list before «vitthāretabba…» = object «Xကိုလည်း» (pi-5 «… အားလုံးကို အကျယ် ချဲ့ရမည်»; 2-15, 3-01,
  5-01 …); before «-sadisaṃ / -sadisā» alone the nominative «Xလည်း». make_ch4-02-09.py vara_list(obj),
  make_ch4-15-21.py, make_ch5-05-12.py. labbhati = «တွေ့ရသည်» (module «na labbhati» «မတွေ့ရ», 3-09, 4-02 …):
  make_ch4-01.py (1 line).
- H21 the na-X rule: kept (exact, «A … မဟုတ်သည် မဟုတ်သော»; a neither-nor term negated «Aလည်း မဟုတ်၊ Bလည်း မဟုတ်သည်
  မဟုတ်သော»). A lighter form would either drop the scope of the outer negation or need a new noun; every 5-xx group
  uses this one rule (5-05-12 / 5-13-20 read the atoms of 5-01-04). No change.
- H22 heṭṭhā (earlier in the text) = «ရှေ့» / «ရှေ့၌» — pi-6 final «heṭṭhā» «ရှေ့၌ ရှိသော» (precedence 1).
  make_ch3-07-08-10.py (3-10), make_ch4-10-14.py (4-13); 4-01 reads 3-07-08-10's value. 3 lines.
- H23 5-05-12 / 5-13-20 shared headings and notes: aligned (align_check 0). piṭṭhi «နောက်ဆုံး နှစ်မျိုးတွဲများ»
  everywhere; Antimadukaṃ (5-20) «အဆုံးသတ် နှစ်မျိုးတွဲ» kept apart (antima = the last dyad, piṭṭhi = the back dyads;
  one Burmese for both would merge two names). «{hetuyā aṭṭha?}» = «{ပါဌ်ကွဲ ((မသေချာ)): hetuyā aṭṭha}» (as 2-07 and
  5-15; the variant keeps its Pāli): make_ch5-05-12.py (2 lines of 5-12).
- H24 4-15-21 vs 5-01 / 5-02: «…paṭiccavārasadisaṃ» = «…နှင့် တူသည်» (singular sadisaṃ; pi-6 «…လည်း … တူညီသည်»;
  -sadisā keeps «တူကြသည်»): make_ch4-02-09.py; «Sahajātavārampi … evaṃ vitthāretabbaṃ» = «…ကိုလည်း ဤသို့ …» (H14,
  H20); «Yathā kusalattike pañhāvāraṃ, evaṃ …» = «…ကဲ့သို့ ထိုနည်းတူ» (1-01 rule: «yathā X» «Xကဲ့သို့», «yathā
  X-gaṇanā» «… ရေတွက်ချက်အတိုင်း»): make_ch5-01-04.py. The 4-17 ^7-51-34 / 5-12 ^7-66-30 cluster lines agree
  (term + «ဖြစ်သော…»; no change).
- align (not in the list): the formless-base minds «<base> ကုသိုလ် / ပြုရုံမျှသာ ဖြစ်သော စိတ် / ကံ၏ အကျိုး» = 1-01
  (make_ch1-03-05.py; 1-03, 1-04: the 4 differing sentences of align-before); «(Yathā cūḷantaraduke lokiyadukaṃ evaṃ
  kātabbaṃ ninnānākaraṇaṃ.)» and the same frame in 3-07 / 3-08 = the 3-03 order «… ထိုနည်းတူ ကွဲပြားချက် မရှိ
  ပြုရမည်» (no «၊» the Pāli lacks): make_ch3-07-08-10.py (4 notes).

### Checks updated on purpose (each where a form was changed on purpose)
- check_ch1-03-05.py: the term-order test (O) also reads «<base> ကံ၏ အကျိုး» as the vipāka term (align change).
- check_ch2-07-11.py: the combined-term table expects «A၊ B» (H6).
- check_ch3-01-02.py: the note «(anulomasahajātasadisā)» expects «(အဟုတ်ပြ ပုံစံ၌ အတူ ပေါ်ပေါက်ခြင်းနှင့် တူကြသည်)» (H19).
- check_ch5-05-12.py: the Latin-left test ignores the Pāli inside variant braces (as check_ch5-13-20) (H23).

## Results (regen_zeroshot.sh, run 1 = regen-run1.txt; run 2 = regen-run2.txt)
- Lines changed vs harmonise-backup/chapters/: 674 (1-01 10, 1-03 34, 1-04 42, 1-05 11, 2-01 63, 2-02 12, 2-03 6,
  2-04 4, 2-05 5, 2-06 6, 2-07 60, 2-08 24, 2-10 26, 2-11 9, 2-12 1, 2-15 1, 3-01 5, 3-02 4, 3-03 2, 3-05 2, 3-07 6,
  3-08 9, 3-09 14, 3-10 6, 4-01 22, 4-02 56, 4-03 13, 4-04 5, 4-05 5, 4-06 5, 4-07 7, 4-08 3, 4-09 7, 4-10 24, 4-11 4,
  4-12 1, 4-13 12, 4-14 10, 4-15 46, 4-16 7, 4-17 7, 4-18 10, 4-19 7, 4-20 16, 4-21 16, 5-01 16, 5-02 4, 5-04 2,
  5-09 1, 5-10 1, 5-11 1, 5-12 2, 5-20 2; the sample 1-00 / 1-02 and the preamble unchanged; all others 0).
- align_check: 24 differing before → 0 after (1074 repeated sentences); align_hidden: 0 → 0 (1361 uneven lines);
  harmonise_align_explained.py: nothing to explain.
- pi-1 … pi-6 identity (harmonise_pi123456.py): pi-1 12/12, pi-2 74/74, pi-3 2/2, pi-4 7230/7230, pi-5 6/6, pi-6 3/3,
  all identical, 0 explained.
- harmonise_scan.py: 30 / 30 items OK (harmonise-table.tsv written); headings / colophons: identical Pāli = identical
  Burmese (0 differing).
- check_chapter_ids / check_text_pe7 / check_marks: OK for all 75 files. Agents' checks: 0 mismatches each; reuse
  n / n; mutation 9/9, 8/8, 8/8, 9/9, 9/9, 10/10, 10/10, 10/10, 10/10, 11/11, 12/12, 11/11, 11/11, 14/14, 12/12, 13/13,
  14/14; every --regress identical (make_ch2-03-06 --regress: 1-01 now identical, its KNOWN_DIFF line no longer
  differs since H2); check_ch4-10-14 / check_ch4-15-21 --regress identical.
- Merged file AI_translation/burmese/pi-7-burmese-plain-zeroshot.md: 75 files in the Pāli folder's order (preamble,
  then the chapters), joined as pi-6; 16249 segments = the sum over the chapters.
- Left as is (explained): H21 (rule kept, see above); 3-07 ^556 note order «… ကဲ့သို့ ထိုနည်းတူ အကျယ် ချဲ့ရမည်၊ ဤသို့
  ပြန်လည် ဆင်ခြင်၍ ပြုရမည်» (two clauses, both rules applied); «-sadisaṃ ninnānākaraṇaṃ» notes with a «၊» the Pāli
  lacks in 3-07 … 4-01 (each Pāli note occurs once; not a repeated sentence, not in the to-do list).
