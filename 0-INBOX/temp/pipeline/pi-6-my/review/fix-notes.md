# pi-6 Burmese rails: bilingual-review fixes (2026-11-23)

Brief: `review/fix-brief.md`. Inputs: `report-A.md` (A1–A6), `report-B.md` (B1–B7), `report-C.md` (C1–C9). Model:
pi-5's fix round (`pi-5-my/rails/apply_fixes.py`, `pi-5-my/review/fix-notes.md`; read only). Built by
`rails/regen_rails.sh`:
- **Rails layer** `rails/my_formulas_rails.py`: new families L02–L09, 22 source patches (layer 3 → 25 patches).
- **New `rails/apply_fixes.py`**: run right after `apply_termbase.py`. It has 10 explicit rules (F01–F10; F08–F10 are B4-ext,
  the coordinator follow-up) and the quote rule Q01. Each rule has a segment-ID or Pāli-frame scope, a Pāli trigger, an expected count and book-wide checks.
  The log is `rails/fixes-log.tsv`.
- **Residual rules**: none, unchanged.
- **Not touched**: the zero-shot chapters, the generators, my6_formulas.py, the termbase (sha256 847e49cd…),
  APPROVED.md / decisions files, the keyword maps, and pi-1-my … pi-5-my.
- **Backup**: the pre-fix rails text and the rails/ files are in `review/fix-backup/`. The rails text md5
  81d5c592… matches `review/rails-before-fixes-md5.txt`.

## Numbers
- **Lines changed against the pre-fix rails:** 820 (679 before B4-ext). Against the zero-shot the rails now differ in
  873 of 14213 lines (was 86).
- **Per chapter against the pre-fix rails:**
  - 2-01: 11, 2-02: 3
  - 3-01: 15, 3-03: 12, 3-04: 14, 3-05: 14, 3-06: 17
  - 4: 19
  - 5-01: 51, 5-02: 42, 5-03: 14
  - 6-01: 59, 6-02: 65
  - 7-02: 28, 7-04: 29, 7-05: 1, 7-06: 38, 7-07: 8, 7-08: 29
  - 8: 10
  - 9-01: 55, 9-02: 55, 9-03: 35
  - 10-01: 6, 10-03: 15, 10-04: 15, 10-05: 6, 10-06: 1, 10-08: 27, 10-09: 43, 10-10: 41, 10-11: 36, 10-12: 4,
    10-13: 2
  - All other chapters: 0.
- **Per chapter against the zero-shot:** see `rails/lines-changed.txt`. It differs from the pre-fix column only by the
  L01 lines (6-01, 6-02, 10-05, 10-06, 10-07, 10-12).
- **apply_fixes:** 11 rules, 622 replacements on 425 lines. The layer makes the rest.

## Applied (per fix ID: instances changed)
| ID | how | instances |
|---|---|---|
| C1 | L02 (6 patches) | 27 lines. The reviewer's 6 lines in 10-01 (avaseso kāyo, avasesā upekkhā). By script, the same frame «S ṭhapetvā avasesa N, na S» had the same head-noun loss in 21 more lines: 2-01 avasesā saṅkhārā ×5; 3-01 kāyo, rūpaṃ, dhammo ×3; 4 kāyo, rūpaṃ, mano, dhammo; 5-01 dukkhasaccaṃ, samudayo ×2, nirodho ×2, maggo ×2. All of them now read «ကြွင်းကျန်သော Nသည် N ဖြစ်သည်၊ S မဟုတ်»; none is left. |
| B2 | L03 | 24 lines (6-01: 8, 6-02: 16). The text is now «… နောက်ဆုံး စိတ် ဖြစ်ပေါ်မည့် ကာမဘုံ၌ ရှိသူတို့». The frame has no rūpāvacarānaṃ / arūpāvacarānaṃ (script: 0). |
| B4 | L04 | 12 lines: every tesaṃ cavantānaṃ of the B2 frame. The text is now «… ပရိနိဗ္ဗာန် ပြုမည့်သူတို့၊ စုတေဆဲ ထိုသူတို့အား». |
| B4-ext | F08–F10 (frame rules; coordinator follow-up 2026-11-23) | 222 instances on 160 lines: every other «… -issanti tesaṃ / tāsaṃ cavant… / upapajjant…» apposition (the persons named by a relative clause, then picked up by tesaṃ / tāsaṃ + participle), found by the Pāli. tesaṃ: 196 «…တို့၊ စုတေဆဲ / ပြန်လည် ဖြစ်ပေါ်ဆဲ ထိုသူတို့»; tāsaṃ cavantīnaṃ 10 and upapajjantīnaṃ 16 «… မိန်းမတို့၊ … ထိုမိန်းမတို့» (tāsaṃ = «ထိုမိန်းမတို့», as the text renders it 61 times). Per chapter: 2-02 2, 3-03 16, 3-04 12, 3-05 12, 3-06 21, 5-01 16, 5-02 16, 5-03 16, 10-09 27, 10-10 45, 10-11 39. Book check: 234 Pāli appositions (with the 12 of L04) = 234 Burmese forms; no «…တို့အနက်» is left anywhere. No line has a partitive (yesaṃ …), so no «အနက်» was kept. One rule per participle, so 10-10 ^6-10-387 (tāsaṃ upapajjantīnaṃ and tesaṃ cavantānaṃ after «မိန်းမတို့») gets each by its own Pāli. |
| B3 | F01 | 1 (^6-6-147) «ဖြစ်ပေါ်ခြင်းနှင့် ချုပ်ငြိမ်းခြင်းအလိုက် ဖော်ပြချက်၌လည်း» |
| A1 | L05 (2 patches) | 6 lines (^6-2-26, 27, 28) «… အရာသည် “ရူပ” (ရုပ် သို့မဟုတ် သဘော) ဖြစ်သည်၊ ရုပ် အစုအဝေး မဟုတ်။», and the paccanīka the same |
| C2 / C3 / B5 | F02 (frame rule) | 255. By script, these are the only person genitives that stand right before a moment phrase: Suddhāvāsānaṃ dutiye (akusale) citte vattamāne 60 and upapatticittassa 32; arahantānaṃ cittassa 48; (Kāmāvacarānaṃ) pacchimacittassa 16; samāpannānaṃ (kāmāvacarānaṃ) assāsapassāsānaṃ 44; (an)abhisametāvīnaṃ taṇhāya 32; itaresaṃ cittassa / kusalānaṃ / vitakkavicārānaṃ … 15. |
| C6 | L08 (3 patches) | 24 lines (10-09 6, 10-10 9, 10-11 9) «… နောက်ဆုံး စိတ် ဖြစ်ပေါ်မည့် ထိုစိတ်၏ …». No finite form is left. |
| C4 | F03 (frame rule) | 30 «Uppajjittha.» / «Nirujjhittha.» → «ဖြစ်ပေါ်ခဲ့ကြသည်။» / «ချုပ်ငြိမ်းခဲ့ကြသည်။» (9-01 10, 9-02 12, 9-03 8). The script then checks all 172 restated answers: «ကြ» in the answer exactly when it is in the question's verb. |
| B1 | L06 (2 patches) | 145 instances on 131 lines (7-02 28, 7-04 28, 7-06 38, 7-07 8, 7-08 29). All 146 apariyāpanna list items now have «၊»; no «နှင့် ဘဝဘုံတို့၌ အကျုံးမဝင်» is left. |
| C7 | F04 | 8 (^6-9-1, 2, 5, 8). Bare abyākatā «… မဟုတ်သော အရာများ» → «… မဟုတ်သော အရာ». This is the majority treatment: bare kusalā / akusalā take no head noun and no «များ», and na kusalā takes «… မဟုတ်သော အရာ». The plural verb «ကြ» stays as the Pāli has it. |
| C9 | F05 | 8: the reviewer's 6, plus ^6-7-122 (7-04) and ^6-7-148 (7-05) found by script. No «သို့သော်» without «၊» is left. |
| A2 / B6 / C5 | L07 (5 patches) | 202 «သူ အားလုံးတို့၏» → «သူအားလုံးတို့၏»; none left. The participle form «…ဆဲသူ အားလုံးတို့» is not this rendering and stays. |
| A3 | F06 | 3 (^6-4-10) «(အသံ အပိုင်းသည် နှာခေါင်း အပိုင်းနှင့် တူညီသည်)», «(လျှာ အပိုင်းလည်း နှာခေါင်း ဓာတ် အပိုင်းနှင့် တူညီသည်)», «(အထိအတွေ့ အပိုင်းသည် နှာခေါင်း အပိုင်းနှင့် တူညီသည်)». The other sadisa notes already name their sections. |
| A4 | L09 (3 patches) | 15 lines without «အပြည့်အစုံ» (including ^6-3-12, ^6-4-4 and ^6-4-12); none left. |
| A5 | F07 | 1 (^6-4-12) «(X၏ သတ်မှတ်ချက်ကဲ့သို့ Y၏ သတ်မှတ်ချက်ကိုလည်း အကျယ် ချဲ့ရမည်။ …)». This is ^6-4-17's wording; the elliptical verb is supplied from ^6-4-17. |
| A6 / B7 / C8 | Q01 | 94 quote spans removed on 45 lines. They were section labels (66), chapter names in notes (13), quoted answers / words (6), «ချုပ်ငြိမ်းခြင်း သမာပတ်ကို ဝင်စားနေသူတို့အား» (5), and yāva saraṇaaraṇā (4 spans on 2 lines). For the saraṇaaraṇā pair, «“A” “B” အတွဲ» became «A၊ B အတွဲ». Kept: the chapter / book-end «“X” (ကျမ်း) ပြီးဆုံးပြီ» lines, «“သောတ”» ×8 and «“ရူပ”» ×6. Script: the quote count of every line now equals the Pāli, apart from these kept kinds. |

## Where the brief's literal wording was not followed (with the reason)
- **C1 «avasesā upekkhā»: singular «ကြွင်းကျန်သော ဥပေက္ခာသည် … ဖြစ်သည်၊ … မဟုတ်» rather than «ဥပေက္ခာတို့သည် … ကြ».**
  The number comes from the noun's own term. Feminine avasesā upekkhā parallels avaseso kāyo and avasesaṃ sotaṃ,
  and the identical Pāli phrase «Avasesā upekkhā na indriyaṃ» (^6-10-140, ^6-10-155) already reads «ကြွင်းကျန်သော
  ဥပေက္ခာသည်» three times. A plural here would give one Pāli phrase two renderings. A one-line change in L02 makes it
  plural if wanted.
- **B5, stacked samāpannānaṃ kāmāvacarānaṃ: the text's join «ပထမ ဈာန်ကို ဝင်စားနေသူတို့နှင့် ကာမဘုံ၌ ရှိသူတို့၏ ဝင်လေ …»
  is kept.** The brief's example drops «တို့နှင့်» («… ဝင်စားနေသူ ကာမဘုံ၌ ရှိသူတို့၏ …»). The rule says «join them as
  the text already does elsewhere». The text joins this pair with «နှင့်» in all 20 other places, and the form
  «ဝင်စားနေသူ ကာမဘုံ၌ ရှိသူတို့» occurs nowhere.
- **«Catutthajjhānaṃ samāpannānaṃ suddhāvāsānaṃ dutiye citte vattamāne» (8 places): «… ဝင်စားနေသူတို့၊ သုဒ္ဓါဝါသ ဘုံ၌
  ရှိသူတို့၏ ဒုတိယ စိတ် …».** «နှင့်» became «၊» so that the new «၏» does not reach the jhāna group. These are separate
  groups, and the brief says to «keep «၊» where the Pāli lists separate groups».
- **Kept «၊» (separate items, not a genitive before a moment):**
  - «cavantānaṃ / upapajjantānaṃ pavatte cittassa …» (pavatte between);
  - «asaññasattā cavantānaṃ arūpe …» (a place between);
  - the relative «yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tassa cittassa …» (no genitive of persons);
  - «Ye puthujjanā … tesaṃ taṇhāya …» (already «ထိုသူတို့၏»).
- **F02 and F03 are frame rules on the built text rather than layer patches.** The lead and answer strings of these
  frames are assembled by five different generators (make_ch2-02-4-5, make_ch6-8, make_ch9-10a, make_ch10b,
  make_ch10c). One rule keyed on the Pāli frame reaches every repetition in all chapters. It has per-line hit counts,
  a book total, a book-wide check that no old form is left, and align_check stays at 0 differing.

## Not changed (observed, for the coordinator)
- **B4 outside 6-01 / 6-02:** first left as scoped (108 lines with «သူတို့အနက်»). The coordinator then asked for it
  book-wide; it is done as B4-ext above.
- **B2 adherence:** no kāmāvacarānaṃ row appeared, because the segments hold the beings-sense term «ကာမဘုံ၌ ရှိသူ»
  and so are hits. No CONTEXT row was needed, and the termbase is unchanged.

## Classification and checks
- **Adherence:** the zero-shot input has 333 misses, reproduced each run. The rails have 360 misses, all INFLECTION;
  GENUINE / unverified 0.
  - The 27 new rows (cavantānaṃ 21, upapajjantānaṃ 6) are the B4 / B4-ext apposition «စုတေဆဲ / ပြန်လည် ဖြစ်ပေါ်ဆဲ
    ထိုသူတို့»: the attributive before a person noun, the agent-noun rule of APPROVED.md. classify_rules.py has two
    INFLECTION rules for them, each with a Pāli check «-issanti tesaṃ / tāsaṃ cavant… / upapajjant…».
  - The uppajjissati rule's text form now also accepts the B2 form.
- **line_adh.py:** 1145 line misses, 0 unexplained. The INF patterns were extended for B2 and B4 (cavantīnaṃ «ထိုမိန်းမ»).
- **line_scan.py:** the §A2 family for kāmāvacarānaṃ pacchimacittaṃ now requires the B2 form and forbids the old
  adjective. The Kāmāvacarānaṃ pacchimacittassa family requires «…တို့၏». Result: 27 of 27 families have Pāli hits,
  and 0 rails lines are left (the zero-shot has 236 flags).
- **regen_rails.sh** (it now runs apply_fixes.py after apply_termbase.py). All checks pass:
  - protected md5s unchanged (188 files);
  - termbase sha256 = the lock 847e49cdef8b…;
  - plain build = zero-shot, 44 / 44;
  - check_chapter_ids + check_text_pe + check_marks OK in all 44 files; typography OK;
  - align_check 0 differing (659 repeated sentences); align_hidden 0 unmatched;
  - identity: pi-1 10/10, pi-2 14/14, pi-3 10/332 + 322 explained, pi-4 10/10, pi-5 2791/2791 (unchanged; no fix
    touched a sentence shared with pi-1 … pi-5);
  - line scan 0.
- **Stability:** a second run changed no byte (58 files). The run logs are `review/fix-run1.txt` and
  `review/fix-run2.txt`; after B4-ext `review/fix-run3.txt` and `review/fix-run4.txt` (all checks pass, the second
  run byte-identical).

Inspection helpers added in rails/ (not part of the checks): pl.py (aligned Pāli / Burmese grep) and fixdiff.py (lines
changed against the pre-fix rails or the zero-shot).
