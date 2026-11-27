# pi-7 Burmese rails: bilingual-review fixes (2026-11-26)

Brief: `review/fix-brief.md`. Inputs: `report-A.md` (A1–A9), `report-B.md` (B1–B19), `report-C.md` (C1–C6). Model:
pi-6's fix round (`pi-6-my/rails/apply_fixes.py`, `pi-6-my/review/fix-notes.md`; read only). Built by
`rails/regen_rails.sh`, which now runs `rails/apply_fixes.py` right after `apply_termbase.py` and then the case check.

- **Backup:** the pre-fix rails text and the rails/ files are in `review/fix-backup/`. The pre-fix rails text md5
  (`cat *.md | md5`) 7e113b03… matches `review/rails-before-fixes-md5.txt`; a baseline regen before any fix
  reproduced it byte for byte (`review/fix-run0-baseline.txt`).
- **Not touched:** the zero-shot chapters, the 18 generators, my7_formulas.py, the termbase (sha256 ceb0842a…, the new
  lock), APPROVED.md / decisions files, the keyword maps, pi-1-my … pi-6-my, the rails layer (no new layer patch).
- **New in rails/:** `apply_fixes.py` (the rules), `case_fixes.py` (the frozen case rows), `case_check.py` (the case
  check), `fixes-log.tsv` (every replacement). Helpers, not part of the checks: `case_propose.py`, `case_freeze.py`,
  `b11_scan.py`, `b12_scan.py`, `fixdiff.py`, `cx.py`, `kw_bk.py`, `pl.py`, `cc_distinct.py`.
- **Changed in rails/:** `regen_rails.sh` (apply_fixes + case check), `classify_misses.py` (also reads
  `fixes-log.tsv` to attribute fixed rows), `adherence-zeroshot.txt` (re-recorded with the new termbase).

## Numbers
- **Case check:** 13,838 clauses. Before the fixes 175 units were left; after them **0 are left**, with 1 explained.
- **apply_fixes:** 124 rules made 1,326 replacements on 948 lines.
  - 87 frozen CASE rows (K1 … K5, 92 replacements);
  - 18 hand case rules M01 … M18 (31);
  - B11 (151), B12 (737), and the single items.
- **Lines changed against the pre-fix rails:** 948 of 27,749 non-empty lines. Against the zero-shot the rails now
  differ in 1,094 lines (was 170; `rails/lines-changed.txt`).
- **Per chapter against the pre-fix rails:**
  - 1-00 1, 1-01 17, 1-02 5, 1-03 20, 1-04 56, 1-05 5
  - 2-01 44, 2-02 19, 2-03 3, 2-04 8, 2-05 8, 2-06 1, 2-07 10, 2-08 9, 2-10 9, 2-11 11, 2-12 1, 2-13 1, 2-14 14,
    2-15 12, 2-16 13, 2-17 29
  - 3-01 48, 3-02 78, 3-03 23, 3-04 10, 3-05 18, 3-07 11, 3-08 11, 3-09 186, 3-10 16
  - 4-01 100, 4-02 58, 4-03 13, 4-04 5, 4-05 1, 4-06 2, 4-07 2, 4-11 1, 4-13 3, 4-14 2, 4-15 27, 4-20 2, 4-21 2
  - 5-01 2, 5-02 2, 5-03 1, 5-04 4, 5-09 1, 5-10 3, 5-11 5, 5-12 6, 5-13 1, 5-15 2, 5-17 1, 5-18 1, 5-19 3, 5-20 1
  - All other chapters: 0.

## Why rules on the built text, not layer patches
The brief asks for the repeated formulas in the rails layer where one generator string builds them. The three
families named there are not built by one string in this book:
- the pañhāvāra example clauses are parsed and rendered by my7_formulas' engine (`panha`, `np_my`, `lex`) and, for
  most chapters, by each generator's own clause code (make_ch1-01, make_ch2-01-02, make_ch3-01-02, make_ch3-07-08-10,
  make_ch3-09, make_ch4-01 …): the wrong cases come from several different parsers (a neuter «-aṃ» read as an
  accusative, a nominative subject taken as the first recipient of «X-assa ca Y-ānañca», a co-subject moved into the
  recipient list), each in a handful of frames;
- the stacking «၊» (B12) is written by np_parse (my7_formulas), by the COMBO / SEP code of make_ch2-07-11,
  make_ch5-01-04, make_ch4-02-09, make_ch4-15-21, make_ch5-13-20 and by literal strings;
- the coordination (B11) by the clause code of 1-04, 2-17, 3-02, 3-03, 3-05, 3-09, 3-10.
So, as pi-6 F02 … F10, every family is one rule keyed on the Pāli on the built text: it fires on every line whose
aligned Pāli has the frame, the same Pāli gets the same change, and align_check stays at 0 differing.

## The case check (`rails/case_check.py`)
Every Pāli clause «… Xpaccayena paccayo» (13,838 in 75 chapters) is paired with its Burmese clause (the n-th
condition phrase of the line); clauses are split into «…»-cut units. In the Pāli, by script (no lexicon): the trailing
run of genitive / dative words is the recipient list, the words before it the conditioning subject; items are counted
by «ca» / «-ñca» and head nouns («A ca B ca N» with two exclusive qualifiers is two items, with two qualifiers that
both hold one). A unit is LEFT when the Burmese
- S0: has no subject marker «…သည်» / «…လည်းကောင်း» before the recipients (subject dropped, marked «ကို», merged into
  the recipients, or left as a bare qualifier);
- S1: has fewer co-subjects «…လည်းကောင်း» than the Pāli (or the stack «A၊ B N» for an exclusive pair);
- S2: has «၊» after the last co-subject, joining the subject and recipient lists;
- D0: has more recipients «…အား» than the Pāli (a conditioning item or a genitive among them);
- D1: has no recipient «…အား», or fewer than the Pāli where nothing joins them.
Result on the pre-fix rails: 175 units left (B's 45 clauses, A1, C1, and the rest of the book). After the fixes:
**0 left**, 1 explained (2-06 ^7-12-53 «Sekkhā phalasamāpattiyā kāyikassa sukhassa»: the only nominative is the
persons «sekkhā», which cannot be the condition; the text reads «ကျင့်ကြံဆဲသူ၏ ဖိုလ်သမာပတ်အား …», the persons'
genitive, as «ariyānaṃ»; a source oddity, kept).

## Applied (per fix ID: instances changed / lines)
| ID | how | instances |
|---|---|---|
| B1 | M01 | 1 (3-01 ^7-24-30) «အမြစ်လည်းကောင်း၊ ယှဉ်တွဲသော အစုအဝေးလည်းကောင်း အမြစ်တို့အားလည်းကောင်း၊ …» |
| B2 | M02 | 1 (3-07 ^7-30-32) |
| B3 | M03 | 1 (3-05 ^7-28-36): vatthu is a co-subject |
| B4 | M04, plus M18 for the 3-10 twin (diṭṭhupādānañca) | 2 |
| B5 | K3, plus M17 for the 3-10 twin (diṭṭhupādānaṃ kāmupādānassa) | 2 |
| B6 | M05 | 1 (3-09 ^7-32-84) |
| B7 | K2 «Xအားလည်းကောင်း၊ → Xသည်» | 16: vatthu ×5, adhipati ×5, cetanā ×3 (one noparāmāsā cetanā), khandhā ×2, hetū ×1 |
| B8 | K1 / K3 «အိပ်ရာ နေရာကို / နေရာ၊ → နေရာသည်» | 12 |
| B9 | M06 | 1 (3-01 ^7-24-107) |
| B10 | K2 | 4: the 3 listed (3-01, 3-05, 3-10), plus 5-11 «Hetu ceva sahetuko ca akusalo …» (spelling-only slip, logged) |
| A1 | M16 | 1 (1-01 ^7-2-423) «မပေးသည်ကို ယူခြင်းသည် …» |
| C1 | M07 | 3 (4-15 ^7-49-205) |
| case, book-wide by pattern (not in the reports) | K1, K2, K4, K5, M08 … M15 | 2-01 neuter subjects «…ကို → …သည်» (cuticittaṃ, anulomaṃ, vodānaṃ, phalaṃ, parikammaṃ, nevasaññānāsaññāyatanaṃ, nibbānaṃ) 25; 2-08 ñāṇaṃ «ကို» 3; 3-01 Ākāsānañcāyatanaṃ 1; 2-01 «၊» after the last co-subject (K4) 22; 2-01 recipients written without «အား» (K5) 9; 2-05 / 2-08 / 2-16 comma-list subjects 3; 2-17, 3-09 co-subjects 2; M14 «Xassa parikammaṃ» «Xအား → X၏ ကြိုတင် ပြင်ဆင်မှု» 11 (4-01); M15 «maggo sekkhānaṃ …» «ကျင့်ကြံဆဲသူတို့၏» 2 (1-01, 2-05) |
| B11 | frame rule (12 exclusive pairs) | 151 on 106 lines (1-04 25, 2-17 7, 3-02 32, 3-03 1, 3-05 3, 3-09 80, 3-10 3). No exclusive stack is left. |
| B12 | frame rule | 737 on 535 lines (29 chapters). None is left. |
| B13 | single rule | 1 (3-09 line 2471) |
| B14 | single rule | 1 (4-01 ^7-35-101) |
| B15 | frame rule | 41 (19 chapters). No «ပယ်ရမည့် အမြစ် နှစ်/သုံးမျိုးတွဲ» is left. |
| B16 / A7 | frame rule | 130 on 108 lines. No «သံဃာကို ဖြိုခွဲသည်» is left. |
| B17 | single rule | 1 (4-01 ^7-35-184) |
| B18, B19 | single rules | 1 each |
| A2 | frame rule | 3 (1-03 ^7-4-62, 2-02 ^7-8-4 ×2) |
| A3 | frame rule | 4 (2-07 ×2, 2-10 ×2) |
| A4 | frame rule | 8 (1-01 3, 3-01 1, 3-09 2, 4-01 1, 4-11 1) |
| A5, A6, A8 | single rules | 1 each |
| C2 | frame rule | 3 (4-01 ^7-35-367, 4-14 ^7-48-73, 4-21) |
| C3 | single rule | 2 quote pairs (5-20 ^7-74-92) |
| C4 / A9 | frame rule | 5 (2-07 2, 5-12 2, 5-15 1) |
| C6 | frame rule | 111 (13 chapters). The brief's «214» counts both «ကိုလည်း» of each frame; the garden path is only at the last one, before «မှီ၍». |

## Decisions applied as the brief words them, and where the wording was read
- **B17 tīṇiyeva moho:** the majority form «မောဟနှင့် သုံးခုသာ» (7 of 8). «… သုံးခု၌သာ မောဟ» would say that delusion
  is found only in three; the notes say that only three questions are obtained, and delusion is the one item that
  the nahetu answers include. The one different form (4-01 ^7-35-184 «မောဟ သုံးခုသာ») now reads «မောဟနှင့် သုံးခုသာ».
  (3-09 «Tīṇi moho yathā cittasamuṭṭhānaduke …» is another sentence and is not touched.)
- **B11 also for asyndetic exclusive pairs:** 3-02 «(ime ajjhattikabāhirā mahābhūtā kātabbā)» and «Ajjhattikā
  bāhirā mahābhūtā …» (no «ca») had the same contradictory stack «အတွင်းပိုင်း၊ ပြင်ပ မူလဓာတ်ကြီး» and are split
  the same way. Pairs that can both hold («pītisahagatā ca sukhasahagatā ca», «maggārammaṇā ca maggādhipatī ca»,
  «kenaci viññeyyā ca kenaci naviññeyyā ca») keep the stack (B12 form). The «A ca B ca dhammā» titles keep their
  form «A သဘောတရားနှင့် B သဘောတရား» (no stack there).
- **B11 inside a list:** a stack that was one member of a «…အား၊ …အား» list or of a «၊» list keeps that list's form
  («… ဤကိုယ်အား၊ … ဤကိုယ်အား»; «…ရုပ်၊ …ရုပ်၊»); «ဤ» (imassa) goes with each member.
- **B12 scope:** a «၊» between two «…သော» qualifiers only where the line's Pāli has two adjacent qualifier words of one
  noun (checked line by line: the stacks never outnumber the Pāli pairs, plus the copies B11 makes). The qualifier
  phrases are the book's own renderings: the Burmese of every single-term title «X dhammo Y dhammassa» and 20
  descriptive qualifiers of the clause frames (sahagata, vipāka, ahetuka, cittasamuṭṭhāna, pacchājāta, purejāta,
  sampayuttaka …). Internal «…သော» of one phrase («မှားယွင်းသော ယူဆမှုနှင့် ယှဉ်တွဲသော») is never split.
- **A3:** «(cakkaṃ kātabbaṃ kusalattikasadisaṃ)» (2-07) = «(စက်ဝိုင်း ပြုရမည်၊ ကုသိုလ် သုံးမျိုးတွဲနှင့် တူသည်)».
- **A4:** also «imaṃ / idaṃ nānaṃ» (3-01, 3-09 ×2, 4-11) and «Savicāraduke imaṃ nānākaraṇaṃ» (4-01): the same word
  (layer L02: nānaṃ of the notes is nānākaraṇa).
- **B15:** also the short headings «Dassanahetuttika-…» / «…dassanahetukattikaṃ» of 4-21 and 5-xx (the same triad):
  41 headings, colophons and notes.
- **B14 / B13 / B10** are logged as spelling-only slips (fixes-log rule B13, B14; B10 = the CASE K2 rows of 3-01
  ^7-24-146, 3-05 ^7-28-106, 3-10 ^7-33-100, read as 3-10 line 590 «X သဘောတရားသည် X သဘောတရားအား»; the 5-11
  «Hetu ceva sahetuko ca akusalo dhammo nahetussa ceva …» clause had the same doubled object and is fixed the same way).

## KEEP
- **C5:** two condition locatives sharing one count keep the Pāli's list with no connector (harmonise H13).

## Not applied, with the reason
- **bhinditvā «ဖြိုခွဲ၍» (4 segments: ^7-2-423, ^7-6-14, ^7-16-45, ^7-35-335; 4 forms) is kept.** The 2026-11-26
  termbase change covers bhindati only. The locked term for the absolutive is still «ဖြိုခွဲ၍», and applying B16 to
  it made 4 adherence rows UNVERIFIED (run 1). For the coordinator: if bhinditvā should follow, the termbase needs
  «သင်းခွဲ၍», and then one line of the B16 rule.
- **2-06 ^7-12-53 «Sekkhā phalasamāpattiyā kāyikassa sukhassa»:** kept. This is the case check's one explained unit
  (see above).

## Checks (regen_rails.sh; run logs `review/fix-run1.txt`, `fix-run2.txt`, `fix-run3.txt`)
- **Protected inputs:** the md5s are unchanged (292 files), and the termbase sha256 equals the lock ceb0842a….
- **Plain build:** it equals the zero-shot in 75 / 75 files.
- **Per chapter:** check_chapter_ids, the text check and check_marks pass in all 75 files; typography is OK.
- **Case check:** 13,838 clauses, 0 left (1 explained).
- **Adherence:**
  - zero-shot input 1,844 misses (re-recorded with the new termbase; was 1,751);
  - rails 1,695 misses: INFLECTION 1,691 and ARTEFACT 4; GENUINE / unverified left 0;
  - the zero-shot's GENUINE rows: 149 (56 before the change), all fixed in the rails. The 93 rows the termbase change adds (B15, B16) are
    fixed by the B15 / B16 rules (classify_misses reads fixes-log.tsv).
- **Alignment:** align_check 0 differing (1,074 repeated sentences); align_hidden 0 unmatched.
- **Identity with pi-1 … pi-6:** unchanged at 12/12, 74/74, 2/2, 7230/7230, 6/6 and 3/3. No fix touched a sentence
  shared with an earlier book.
- **Line scan:** 0 lines left.
- **Reproducibility:** run 2 (`fix-run2.txt`) and run 3 (`fix-run3.txt`) both pass all checks, and run 3 changed no
  byte (100 output files). The rails text md5 (`cat *.md | md5`) is f937c41c…; run 1 failed only on the 4 bhinditvā
  rows (see «Not applied»).

## Coordinator verification and addition (2026-11-27)
- Independent rebuild of the agent's state: rails md5 (`cat *.md | md5`) f937c41cbebc23c219590c0f339eb6bc, identical to the agent's; ALL CHECKS PASSED.
- **Missed by the case check, 4 clauses (B8 remainder):** «… senāsanaṃ cittaṃ / moho X-assa …» with no «ca» still had «အိပ်ရာ နေရာကို စိတ်သည် / မောဟသည်». These are B8's listed ^7-32-128 and ^7-32-216 ×2, plus a matching instance in 3-04 ^7-27-78 (line 488). The case check did not see them because they sit inside «…» lists.
- **Added rule M19** in `rails/apply_fixes.py`: «အိပ်ရာ နေရာ၊ စိတ်သည် / မောဟသည်», the form already at 3-09 line 1387. «senāsanaṃ moho ca …» keeps «…လည်းကောင်း၊ …လည်းကောင်း» (6 places), and the 3-01 line 667 comma list «bhojanaṃ, senāsanaṃ, moho ca» is kept as it is. 4 replacements, expected 4.
- **Wider scan** (`review/coord_scan4.py`) for an item marked «ကို» before «…» or directly before a recipient or subject: no other misses. The remaining hits are accusatives of paṭicca / upanissāya, deeds lists, and the compound «ဒုစရိုက်ကို မရှက်မှု».
- **Final:** two regen runs, ALL CHECKS PASSED, no byte changed on the rerun. Rails md5 9e0e4beee3ce6156708979b73089a555; fixes-log 1052 rows. The termbase sha is ceb0842a…, the protected md5s are unchanged (292), and identity is unchanged.
