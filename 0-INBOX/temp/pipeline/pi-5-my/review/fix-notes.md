# pi-5 Burmese rails: bilingual-review fixes (2026-11-22)

Brief: `review/fix-brief.md`. Inputs: `report-A.md` (A1–A22), `report-B.md` (B1–B20), termbase change 2026-11-22
(APPROVED.md «Change 2026-11-22 (bilingual review A / B)», sha256 dbc04869…). Built by `rails/regen_rails.sh`:
rails layer `rails/my_formulas_rails.py` (new families L40–L51, 28 source patches; layer 152 → 180 patches), two
residual rules following the decisions (R501 retargeted, R203 withdrawn; 198 → 197 rules), and the new
`rails/apply_fixes.py` (F01–F44, 43 explicit rules with segment IDs, Pāli triggers, expected counts and book-wide
checks of every pattern; log `rails/fixes-log.tsv`), run right after `apply_termbase.py`. Not touched: zero-shot
chapters, generators, my5_formulas.py, termbase, APPROVED.md, decisions-A.tsv, termbase-decisions.md, keyword maps,
pi-1-my … pi-4-my. Pre-fix rails text and rails/ files kept in `review/fix-backup/`.

## Numbers
- 124 lines changed against the pre-fix rails (zero-shot → rails now 675 of 3460, was 597).
- Per chapter: 1: 12, 2: 2, 3: 3, 5: 5, 9: 5, 10: 14, 11: 2, 12: 6, 13: 2, 14: 1, 15: 9, 16: 16, 17: 2, 19: 2, 20: 8,
  22: 4, 25: 2, 26: 3, 28: 15, 30: 7, 31: 4; all other chapters 0.
- apply_fixes: 43 rules, 84 replacements, 53 lines; layer L40–L51 and R501 / R203 make the rest.

## Applied (per fix ID: instances changed, where)
| ID | how | instances |
|---|---|---|
| B1 | L50 | ^5-651 (20:109): «na ca arahā …» list, every verb negative: 4 verbs made negative (+1 already), «… မမှီဝဲရာ၊ … မခံယူရာ၊ … မခံယူရာ၊ … မခံယူရာ… … မခံယူရာသလော» |
| B2 | F01 | 2 (^5-491 prose 15:121, verse 15:123): «ငါတို့ ကျွေးမွေးခဲ့သူသည် ငါတို့ကို ပြန်လည် ကျွေးမွေးလိမ့်မည်» (no «သား») |
| B3 | F02 | 1 (^5-867, 28:47): «သောမ၊ ယမ၊ ဝေဿဝဏ် မင်းလည်း မဟုတ်၊» |
| A1 | F03 | 2 (^5-60, 1:263): «… အားလုံးသည် ပုဂ္ဂိုလ် ဖြစ်သည်ကား မဟုတ်သလော» ×2 |
| A2 + A3 | L40 | identity formula found by script: appiyaṃ karitvā 19 «…ဟူသော စကားကို မခွဲခြားဘဲ», esese 24 «ဤစကားတို့သည် တစ်ခုတည်း ဖြစ်သော၊ အနက် တူသော၊ …» (^5-67, ^5-68, ^5-285, ^5-304–306, ^5-501); 15 lines (ch1 6, ch5 4, ch9 4, ch15 1) |
| A4 | F04 | 3 (^5-273): «မပျက်ယွင်းတတ်သော အရာကို ထိုးဖောက်၍ မသိရသေး…» |
| A5 | F05, F06 | 5: ^5-403 abhisambuddhāni ×3 «ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူခဲ့…» (the Pāli has 3, not 4), ^5-450 abhisambujjhati / Abhisambujjhitvā ×2 (termbase change) |
| A6 | F07 | 1 (^5-405, 12:178): «“ဓမ္မစကြာကို လည်စေရန် …» |
| A7 | F08, F09 | 2 lines (^5-325, 10:190–191): 190 «“ငါသည် လွတ်မြောက်စေရန် မတတ်နိုင် [ပါဌ်ကွဲ …]၊», 191 «ဓောတက၊ လောက၌ ယုံမှားသံသယ ရှိသူ တစ်စုံတစ်ယောက်ကိုမျှ [စာလုံးပေါင်းကွဲ …]၊» |
| B4 | L41 | 24 old forms replaced (12 «စိတ်ကို (မ)ထားရှိသူ» ch22, 9 «စိတ် ဦး(မ)တည်ထားသူ» ch26, 3 «ဆု မတောင်းသူ» ch15 / ch17); now paṇidahantassa 20 «ဆုတောင်းသူ», appaṇidahantassa 10 «မဆုတောင်းသူ» book-wide |
| B5 | L51, R501, F10 | 16: ^5-780 (25:20) active voropeti ×6 «အသက်မှ သတ်…» (L51; the pi-2 ^2-U55 witness of the passive is kept); ^5-857–859 R501 now «အမိကို အသက်မှ သတ်၍» ×9 (termbase mātaraṃ / Asañcicca voropetvā); B18 below. Passive «… အသက်မှ ချခံရ…» kept (13 instances). Script: no active voropeti line keeps «အသက်မှ ချ» |
| B6 | L42 | 37 «အနန္တရိယ…» → «ချက်ချင်း အကျိုးပေးသော ကံ ရှိသူ» (ānantariko ×30, ch28) / «ချက်ချင်း အကျိုးပေးသော ကံကို ပြုသော ပုဂ္ဂိုလ်» (ānantariyassa, ^5-508); none left |
| B7 | L43 | 4 (^5-874, ^5-875): «အင်္ဂါ ရှစ်ပါး ရှိသော အရိယာ မဂ်» (pi-2 ^2-486) |
| B8 | L44 | 6 («ပြိတ္တာ နယ်ပယ်» ×2 ^5-503, «ပြိတ္တာ နယ်» ×4 ^5-903, ^5-904); pettivisaya now «ပြိတ္တာ ဘုံ» 8 of 8 |
| B9 | L45, F11, F43 | ch31: thesis «ဒုက္ခသည်သာ …» ×4, quotation «“မမြဲသော အရာသည် ဒုက္ခ”ဟု» ×4, bracket after «ဟု» (31:48); script found the same SN 3.15 quotation at ^5-338 (10:305, «“အကြင်အရာသည် မမြဲ၊ ထိုအရာသည် ဒုက္ခ”») → same wording ×2 + bracket after «ဟု» (F43). Now 8 of 8 one wording |
| B10 | F12 | ^5-782 (25:25) = 20:29's wording (3 replacements, 1 line); script: 2 quotations, 1 wording |
| B11 | F13 | 1 (^5-546, 16:220) «မပေးသည်ကို ယူခြင်း ကံကြောင့်»; adinnādāna «ယူ…» 6 of 6 |
| B12 | L46 | 4 (^5-314, ^5-901, ^5-908, ^5-909); samphaṃ palap- / samphappalāpa «အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား» 9 of 9 |
| B13 | L47, F14 | ch15 «na sukhavedaniyaṃ na dukkhavedaniyaṃ…pe…» ×7 = ch24 «… ဖြစ်စေတတ်သော အရာ မဟုတ်၊ …» (the full negative list of ^5-492 keeps its attributive form); ch16 «X kusalo sārammaṇo» 32 «ကုသိုလ် ဖြစ်သော၊ အာရုံ» → «ကုသိုလ် ဖြစ်၍ အာရုံ» (= ch24); the frame «X vipāko, X sukhavedaniyo …» «ဖြစ်သည်၊» → «ဖြစ်၍» ×20 (ch15 8, and ch20 12: identical Pāli frame, = ch24) |
| A15 | F15 | 2 (^5-338): «ခဏကို ရရှိပြီ» both; the 10:303 variant after «ရရှိပြီ» (A22) |
| A16 | L49 | 3 (^5-307, ^5-308 «အမှန်အားဖြင့်», ^5-546 «ကောင်းပြီ၊») → «ကဲ၊»; Handa hi 4 of 4 «ကဲ၊» |
| A17 | R203 withdrawn | 2 (^5-89, ^5-90): «အခြား မဖြစ်ဘဲ မကွယ်ပျောက်ဘဲ …» = ^5-78; anañño 4 of 4 «အခြား မဖြစ်ဘဲ» |
| A18 | F17 | 2 (^5-378): «မရသေးသော၊ မပိုင်ဆိုင်ရသေးသော၊ မျက်မှောက် မပြုရသေးသော» |
| A8 | F20 | 1 (^5-94, 1:354) «… မပျက် ဆိုလျှင်» |
| A9 | F21 | 1 bracket (^5-401, 12:138) «[… ဟောတော်မူချက်ကို မြင်၍ မေးသည်]» moved after «… ခံယူကြသကဲ့သို့» |
| A10 | F22 | 2 (^5-401, 12:141) «အရပ် အားလုံးကိုလည်း ကြည့်ရှု၏» |
| A11 | F23 | 1 (^5-269) «… သက်ဆင်းရန် မထိုက်တန်ကြ» |
| A12 | F24 | 1 (^5-269) «ဘုရားရှင်၌ မကြည်ညိုကြ» |
| A13 | F25 | 5 (^5-268, 2:177) «… ရောက်သည်၊» (no «ဟူ၍») |
| A14 | F26 | 1 (^5-342) «… မရောက်သူ ဖြစ်သလော» |
| A20 | F27 | 1 (^5-296) «ပြုခြင်း၏ အကျိုး မရှိဟု …၊ ကံ၏ အကျိုး မရှိဟု …» |
| B14 | F18 | 1 (^5-653, 20:118) «…”ဟု ဤသို့ မဆိုသင့်သလော» |
| B15 | L48 | 4 (^5-519, ^5-523, ^5-546) «… ခြောက်ပါး ရှိသော ကိုယ်ခန္ဓာ»; script: saḷāyataniko attabhāvo occurs 4× (all ch16; ch1–12 has only attabhāvapaṭilābha, 61 «… ရရှိခြင်း» kept) |
| B17 | F28 | 1 bracket (^5-546) after «အမိကို သတ်ခြင်း ကံကြောင့်» |
| B18 | F10 | 1 (^5-653) «… အသက်မှ သတ်ခြင်း» |
| B19 | F19 | 2 (^5-906) «… နယ်ပယ်သို့ မရောက်လာကြ» (no «မျက်စိ၏» / «ကိုယ်၏»); 6 of 6 one form |
| A21 + B20 | F37–F42 | 6: vagga lines ^5-192, ^5-238 (uddāna), ^5-306 without quotes; 10:258 stray «’» dropped; heading ^5-19-4-1-0 «ဤကား ဒုက္ခဟူသော ဆွေးနွေးချက်»; its section end ^5-620 «“ဤကား ဒုက္ခဟူသော ဆွေးနွေးချက်” ပြီးဆုံးပြီ» (outer quotes kept, inner ‘’ dropped). Script: 506 vagga / heading lines without Pāli quotes, 0 with Burmese quotes; the 220 «“X” ပြီးဆုံးပြီ» section ends and the book-title lines 31:62 / 31:64 keep their quotes |
| A22 | F29–F36, F44 (+ F11, F15, F21, F28) | brackets after their word: the reviewer's 10:90, 10:255 (duplicated reference split to its two places), 11:289, 12:179; by script every bracket glued to a following word (10:281, 13:30, 13:116, 2:78, 31:48, 10:303) and the one duplicated pair: 0 left; 10:254 (same segment) also |

## Kept as decided
- **A19** (^5-122): the divine eye sees «အဆင်းအရောင်» (= pi-2 ^2-517); the thesis «Rūpaṃ puggalo» keeps «ရုပ်» as
  everywhere in the book (harmonise decision: identical propositions keep one wording).
- **B16** kapiñjara «ငှက်ကြီး»: no attested Burmese bird name in the sources; the termbase term stands.

## Termbase-dependent inputs
- `rails/adherence-zeroshot.txt` re-run with the new termbase (dbc04869…): 928 → 943 misses (+15: appiyaṃ ×3,
  samphaṃ ×4, abhisambuddhāni, Abhisambujjhitvā, abhisambujjhati, Bhaṭo, ānantariyassa, ānantariko ×8; − the five
  voropetvā «ချ၍» rows, now hits). Reproduced each run.
- Classification (`classify_misses.py` also reads `fixes-log.tsv`; 5 new ARTEFACT rules in `classify_rules.py`):
  GENUINE fixed 662 (655 before the termbase change), GENUINE / unknown left 0; ARTEFACT 256, INFLECTION 36. The new
  ARTEFACT rows: the decided wordings A17 (añño ^5-89 / ^5-90), A10 (viloketi ^5-401), B11 (ādāna stem entry ^5-546),
  A20 (natthika ^5-296), B9 (Dukkhaṃ parinipphannaṃ ^5-917 / ^5-918), and STALE phrase entries.
- Termbase doubts for the coordinator (termbase not changed): phrase entries not updated by the 2026-11-22 change
  still hold the old wording: mātughātako / Mātughātako / pitughātako / saṅghabhedako / Saṅghabhedako /
  ruhiruppādako ānantariko «… အနန္တရိယကံ ရှိသော», Bhagavatā abhisambuddhāni «… ထိုးထွင်း သိတော်မူခဲ့သော», Dukkhaṃ
  parinipphannaṃ «ဆင်းရဲ ဒုက္ခ …»; natthika «ဘာမျှ မရှိ» vs A20; viloketi «ဘေးသို့ ကြည့်သည်» vs A10.
- `line_scan.py`: 19 new families (req / forbid for the fixes); 50 of 50 families with Pāli hits, rails 0 lines left
  (zero-shot 369 flags).

## Not changed (observed, not in the decisions)
- 28:11 / 28:12 (^5-860, ^5-861): the passive «pitā / arahā jīvitā voropito» reads «အဖကို / ရဟန္တာကို သတ်ခဲ့ပြီး»,
  while 28:10 reads «အမိသည် အသက်မှ ချခံရပြီး» (R618). «Passive stays» was applied literally; one rule would align them.
- 30:81 (^5-906) ajjhattiko kāyo «မိမိ၏ ကိုယ်» vs 30:80 «အတွင်းပိုင်း မျက်စိ» (R623).
- Bracket placement beyond the reviewer's lines and the script-detectable classes (glued, duplicated) was not
  audited book-wide: many sentence-final variant brackets follow the book's clause-end convention.

## Checks (regen_rails.sh, all pass; a second run is byte-identical: 48 files)
protected md5 unchanged (137 files, zero-shot chapters and generators among them); termbase sha256 = the new lock
dbc048698d57…; plain build = zero-shot 32 / 32; layer 180 patches, 197 residual rules (361 replacements), fixes 43
rules / 84 replacements; check_chapter_ids + check_text_pe + check_marks OK in all 32 files; typography OK;
adherence: zero-shot 943 (input reproduced), rails 292 = ARTEFACT 256 + INFLECTION 36, GENUINE 0; align: 690 repeated
Pāli sentences, 1 differing = the accepted 1:426; align_hidden 0; pi-1 … pi-4 identity 2/2, 4/4, 2/21 + 19 explained,
5/7 + 2 explained (unchanged); line scan 0; ALL CHECKS PASSED. Run logs: `review/fix-run1.txt`, `review/fix-run2.txt`.

Inspection helpers added in rails/ (not part of the checks): show_seg.py, pcount.py, quotescan.py
(`review/quotescan-before.txt`).

## Coordinator follow-up (2026-11-22): open points 1–3
1. **F45** (^5-859, 28:11–12): the passive «pitā / arahā jīvitā voropito» = «အဖသည် / ရဟန္တာသည် အသက်မှ ချခံရပြီး…» as
   28:10 (R618): 4 replacements, 2 lines. The «Not changed» point above on this is now done.
2. **F46** (^5-906, 30:81): ajjhattiko (ceva) kāyo = «အတွင်းပိုင်း ကိုယ်» (termbase ajjhattika / ajjhattikaṃ
   «အတွင်းပိုင်း», = «အတွင်းပိုင်း မျက်စိ» 30:80): 3 replacements, 1 line. The «Not changed» point above on this is now done.
   Both lines had already changed in this round, so the counts stay at 124 lines against the pre-fix rails and
   675 against the zero-shot. apply_fixes is now 45 rules, 91 replacements, 55 lines. There are 2 new line_scan
   families (52 of 52 with Pāli hits).
3. `rails/termbase-proposals-2.tsv` (written and checked by `rails/make_proposals2.py`): 10 proposals.
   - **Replaced sense 0 (7):** mātughātako / pitughātako / saṅghabhedako / ruhiruppādako ānantariko «… ချက်ချင်း
     အကျိုးပေးသော ကံ ရှိသော», Bhagavatā abhisambuddhāni «မြတ်စွာဘုရား … ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူခဲ့သော», Dukkhaṃ
     parinipphannaṃ «ဒုက္ခ … ပြည့်စုံစွာ ဖြစ်ပေါ်ပြီးသော», natthika «ကံ၏ အကျိုး မရှိ».
   - **Mātughātako and Saṅghabhedako:** these are the same termbase entries as mātughātako and saṅghabhedako (the
     headword lookup ignores case), so 8 listed entries become 6 rows here.
   - **Added sense 1 (3):** viloketi «ကြည့်ရှုသည်» (^5-401; sense 0 «ဘေးသို့ ကြည့်သည်» is still right in ^5-336 and
     ^5-852, so replacing it would contradict them); ādāna «ယူခြင်း» (adinnādāna ^5-546; sense 0 «ကိုင်ခြင်း» is still
     right for ādānanikkhepanaṃ ^5-293); añño «အခြား» (anañño ^5-89 / ^5-90, A17; sense 0 «တခြားစီ» is still right in
     the other segments). These are the only other headwords the review fixes contradict (adherence: every other
     touched keyword is still a hit).
   - **Check:** each replaced term occurs in every rails segment whose keyword list has the headword. With an added
     sense, every such segment holds one of the entry's terms, and the new term is in its own segments. No ", ",
     " / ", "; ", «၊» or dash inside a term.
Checks: regen_rails.sh ALL CHECKS PASSED, second run byte-identical (49 files); GENUINE left 0; align 1 (= 1:426);
identity unchanged; line scan 0. Run logs `review/fix-run3.txt`, `review/fix-run4.txt`. Waiting for the new termbase
sha256 to re-run.

## Termbase round 2 (2026-11-22, APPROVED.md «Change 2026-11-22 (review fix round 2)», sha256 e45d99f4…)
- The coordinator applied the 7 sense-0 proposals (6 stale phrase rows and natthika). The three added senses were not
  taken (viloketi, ādāna, añño). The coordinator set TB_SHA and the four termbase md5s; I edited no termbase file.
- `rails/adherence-zeroshot.txt` re-run: 943 → 951 misses. The 11 new rows are the new phrase terms, which the
  zero-shot lacks; 3 changed rows replace their old terms (ruhiruppādako ×2, Dukkhaṃ parinipphannaṃ ×2). The round-1
  file is kept as `review/fix-backup/adherence-zeroshot.round1.txt`.
- New class **CONTEXT** (`classify_rules.CONTEXT`, used by `classify_misses.py` only in the listed segment IDs):
  viloketi ^5-401, ādāna ^5-546, añño ^5-89 / ^5-90 = 4 rows. `rails_misses_check.py` accepts CONTEXT. The round-1
  ARTEFACT rules for these, for natthika and for Dukkhaṃ parinipphannaṃ are removed, together with the abhisambuddhāni
  stale substitution; those rows are now termbase hits or CONTEXT.
- Result: rails 279 misses = ARTEFACT 239 + CONTEXT 4 + INFLECTION 36; GENUINE fixed 674, left 0.
- Checks: regen_rails.sh ALL CHECKS PASSED twice, the second run byte-identical (49 files). Termbase sha256 e45d99f4d08f.
  Rails text unchanged by this round: 675 of 3460 lines changed against the zero-shot, 124 against the pre-fix rails.
  align 1 (= 1:426); identity 2/2, 4/4, 2/21 + 19, 5/7 + 2; line scan 0. Logs: `review/fix-run5.txt`, `review/fix-run6.txt`.
