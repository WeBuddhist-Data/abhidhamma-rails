# pi-4 Burmese rails: bilingual-review fixes (2026-11-20)

Brief: `review/fix-brief.md`. Inputs: `report-A.md` (A1–A6), `report-B.md` (B1–B6), rails doubt 5 of `rails/notes-rails.md`.
Built by `rails/regen_rails.sh`: rails layer `rails/my_formulas_rails.py` (new patches L26, L27; layer 36 → 40 source
patches) and the new `rails/apply_fixes.py` (F01–F05, explicit rules with segment IDs, Pāli triggers and expected counts,
plus book-wide checks of every pattern; log `rails/fixes-log.tsv`), run right after `apply_termbase.py`. Not touched by
me: zero-shot chapters, generators, my4_formulas.py, termbase, decisions-A.tsv, termbase-decisions.md, APPROVED.md,
keyword maps, pi-1-my/, pi-2-my/, pi-3-my/. Pre-fix rails and rails/ outputs kept in `review/fix-backup/`.

## Applied: 13 lines changed against the pre-fix rails (zero-shot → rails now 60 of 561 lines, was 49)

| ID | where | instances | lines per chapter |
|---|---|---|---|
| A1 | F01 (^4-M-16) | 1: «“ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း” ခေါင်းစဉ်စာရင်း ပြီးဆုံးပြီ။» (the book title, = colophon ^4-209); script: the only mātikā colophon, no old form left | 1-matika 1 (l.211) |
| A6 | F02 (^4-94) | 1: «ထို့အတူပင် … လူနာနှင့် တူသော ပုဂ္ဂိုလ် သုံးယောက်တို့သည် …»; script over all 12 «Evamevaṃ … puggalā» similes: the other 11 have ime (tayome / cattārome / pañcime) and keep «ဤ» | 4-tika 1 (l.13) |
| B1 | F03 (^4-176) | 1: «မြို့၏ အရှေ့ဘက်၌» (termbase narassa «မြို့»); narassa occurs once | 5-catukka 1 (l.152) |
| B2 | L26 (make_ch5, 2 patches) | 4 lines, 12 changes: «ဤလောက၌ အချို့သော ပုဂ္ဂိုလ်အဖို့ ချီးမွမ်းဖွယ်လည်း ရှိ၏၊ ကဲ့ရဲ့ဖွယ်လည်း ရှိ၏။» ×4 and yo (pi) tattha (a)vaṇṇo «ထိုတို့အနက် … ရှိသမျှကို» ×8; every other word kept; script: Pāli «vaṇṇopi … saṃvijjati» 4 = Burmese 4, «yo tattha (a)vaṇṇo» 8 = 8, no «ထိုသူ၌ …ဖွယ်» left | 5-catukka 4 (l.111–114) |
| B3 | not changed | 0: the text already has each termbase term at its Pāli slot: paravaṇṇanāya «ချီးမွမ်းစကား», parathomanāya «ချီးကျူးစကား» (termbase thomanāya), parapasaṃsanāya «ထောမနာစကား» (termbase pasaṃsanāya), paravaṇṇahārikāya «ဂုဏ်သတင်း ဆောင်ယူချက်». The reviewer's order would put pasaṃsanā's term in thomanā's slot. The list occurs once (^4-171); checked by script (apply_fixes, line_scan KR) | 0 |
| B4 | L27 (make_ch5, 2 patches) | 4 lines: the pasāda / appasāda lines end «… ဟူ၍လည်း ကြည်ညိုမှုကို ဖြစ်စေ၏။» (^4-164 l.103, ^4-165 l.109) / «… ဟူ၍လည်း မကြည်ညိုမှုကို ဖြစ်စေ၏။» (l.104, l.108), the line's own janeti phrase (termbase pasādaṃ janeti, appasādaṃ); script: each of the 4 «janeti –» lines ends with the same phrase as before its dash; the 4 bhāsati lines keep «ပြောဆို၏» | 5-catukka 4 |
| B5 | not changed | 0: pi-1 ^1-1350 has the identical Pāli frame («yā sā vācā neḷā … bahujanamanāpā tathārūpiṃ vācaṃ bhāsitā hoti», only neḷā / nelā) and renders it «… လူအများ စိတ်တွေ့သော စကား ရှိ၏ ထိုသို့သော စကားကို ပြောဆိုသူ ဖြစ်၏» (finite «ရှိ၏», no «၊»), which is ^4-178 word for word. pi-1 has no relative clause «ရှိသမျှ» there, so «use its form if the Pāli matches» keeps the text; a relative clause would make ^4-178 differ from pi-1 ^1-1350 (and from ^4-100 «… ရှိ၏၊ ထိုသို့သော …», pi-2 ^2-904 asākhalyaṃ «… ရှိ၏၊ ထိုသို့သော …»). Checked by script (apply_fixes reads pi-1 ^1-1350; line_scan KR). If the relative clause is still wanted, it is one F rule on ^4-178 l.162 («စကား ရှိ၏ ထိုသို့သော» → «စကား ရှိသမျှ ထိုသို့သော») | 0 |
| B6 | F04 (^4-175) | 1: «… ထောင်စောင့် ဖြစ်၏၊ သို့မဟုတ် ကြမ်းကြုတ်သော အလုပ် ရှိသော အခြား တစ်စုံတစ်ယောက် ဖြစ်၏။» The decision's «အလုပ်ကို လုပ်ကိုင်သော» is replaced by the termbase term it asks to keep: kurūra «ကြမ်းကြုတ်သော» + kammantā «အလုပ် ရှိသော» (the text had «အလုပ် ရှိကြသော»); the subject switch is gone | 5-catukka 1 (l.150) |
| doubt 5 | F05 (^4-179) | 1: «… လှည့်ဖြားခြင်း၊ ကောက်ကျစ်ခြင်း၊ ကွေ့ဝိုက်သော နည်းလမ်း …» (termbase sāci «ကွေ့ဝိုက်သော»); nikati keeps «ကောက်ကျစ်ခြင်း» (3 Pāli nikati = 3); no «ကောက်ကျစ်သော» left in the book | 5-catukka 1 (l.166) |

Lines changed against the pre-fix rails: 1-matika 1, 4-tika 1, 5-catukka 11 (l.103, 104, 108, 109, 111–114, 150, 152,
166), all other chapters 0. Against the zero-shot: preamble 0/3, 1 2/185, 2 2/47, 3 0/48, 4 19/57, 5 32/147, 6 1/34,
7 0/8, 8 1/12, 9 1/3, 10 2/11, 11 0/6 — total 60 of 561.

## Kept as decided

- **A2** «စေတနာ» in cetanābhabbo / anusañceteti: part of the approved person-type NAME; everyday Burmese.
- **A3** (^4-66) and **A4** (^4-52): the Pāli has no full stop / comma there; user rule: no added punctuation.
- **A5** paññapeti «ပညတ်» (^4-130, ^4-131): the locked pi-2 usage (15× in pi-2 ch17).
- **B3**, **B5**: no change needed (see the table).

## Termbase change (coordinator, 2026-11-20) and the termbase-dependent inputs

- `rails/adherence-zeroshot.txt` re-run with the new termbase (sha256 6ba052ff…): 122 → 124 misses (+ ^4-176 narassa
  «လူ», + ^4-179 sāci «ကောက်ကျစ်သော»).
- `rails/protected-md5-before.txt`: besides line 1 (termbase, set upstream), lines 29–31 (termbase/APPROVED.md,
  decisions-A.tsv, termbase-decisions.md) still held their pre-change md5s although the coordinator changed them in the
  same step (all four files 2026-11-20 09:30:11; each holds the «2026-11-20» narassa / sāci record), so step 0 failed.
  I set those three lines to the current md5s (old file in `review/fix-backup/`); the files themselves were not touched.
- `classify_misses.py`: GENUINE families narassa → F03, sāci → F05; `applied_ids` also reads `fixes-log.tsv` (F nn);
  a new ARTEFACT row for the two rails-introduced misses at ^4-M-16 (paññatti «သတ်မှတ်ချက်», puggalapaññatti
  «ပုဂ္ဂိုလ် သတ်မှတ်ချက်»: the colophon now names the book by its approved title, as ^4-0 / ^4-209).
- `map_vs_termbase.py`: FIXED narassa «လူ» (F03), sāci «ကောက်ကျစ်သော» (F05), with their GONE forms.
- `line_scan.py`: 19 new families (F01–F05, L26, L27 req / forbid; KR: B3 order, B4's bhāsati lines, B5 = pi-1 form,
  ^4-100 with the Pāli comma); 74 of 74 families have Pāli hits.

## Checks (regen_rails.sh, all pass; a second run is byte-identical: 12 chapters + 14 rails/ outputs, 26 files)

protected md5 unchanged (84 files); termbase sha256 = the new lock 6ba052ff7edf…; plain build = zero-shot 12 / 12;
layer 40 source patches, 0 residual rules, fixes 5 rules / 5 replacements; check_chapter_ids + check_text_pe + check_marks
OK in all 12 files; typography OK; adherence: zero-shot 124 misses (input reproduced), rails 5790 checked, 80 misses =
ARTEFACT 70 + INFLECTION 10 (all known rows), GENUINE fixed 45, GENUINE or unknown left 0; sense-level 0 unexplained of
5828 (FIXED 75); align: 70 repeated Pāli sentences, 0 differing; hidden: 0 unmatched; pi-1 / pi-2 / pi-3 identity 45 / 45,
35 / 36 + 1 explained, 2 / 2; line scan 0 lines left (zero-shot 157 flags); zero-shot files unchanged (protected md5);
ALL CHECKS PASSED.
