# pi-3 Burmese rails: bilingual-review fixes (2026-11-19)

Brief: `review/fix-brief.md`. Inputs: `report-A.md` (A1–A5), `report-B.md` (B1–B4). Built by `rails/regen_rails.sh`:
rails layer `rails/my_formulas_rails.py` unchanged (0 patches: neither fix is a repeated formula), `apply_termbase.py`
unchanged (0 rules), new `rails/apply_fixes.py` (F1, F2: explicit rules with segment IDs, Pāli triggers and expected
counts, per-line count = Pāli hits, «[» / «…» / «–» counts kept, book-wide «nāmarūpena» count; log `rails/fixes-log.tsv`),
run right after `apply_termbase.py`. Pre-fix rails and scripts kept in `review/fix-backup/`.

## Applied: 4 lines changed (zero-shot → rails now 4 of 673 lines, was 0)

| ID | rule | instances | lines per chapter |
|---|---|---|---|
| A3 + B3 | F1 (^3-227, ^3-455; trigger «visayo … esanayo subuddho») | 2: «… နှစ်ပါး၊ အပိုင်းအခြားနှင့်တကွ ဤခွဲနည်းကို ကောင်းစွာ နားလည်ပြီး ဖြစ်သည်။»; at ^3-227 «အပိုင်းအခြား [ပါဌ်ကွဲ (Syā.): dvevīsati]နှင့်တကွ …» (bracket text and «[» count as before; «…» / «–» counts unchanged) | 6-pancamanayo 1 (l.81), 14-terasamanayo 1 (l.23) |
| A4 | F2 (^3-202, ^3-449; trigger «nāmarūpena») | 2: «စိတ်ပိုင်းနှင့် ရုပ်ပိုင်းနှင့်» → «စိတ်ပိုင်းနှင့် ရုပ်ပိုင်းတို့နှင့်»; found by script: the Pāli has exactly 2 «nāmarūpena» (ch6 frame «X နှင့် အစုအဝေး …», ch14 list «X နှင့်…»), no «ရုပ်ပိုင်းနှင့်» left anywhere; nominative nāmarūpaṃ lines untouched | 6-pancamanayo 1 (l.23), 14-terasamanayo 1 (l.7) |

Nothing decided as APPLY was left unapplied.

## Kept, as decided

- **A1** «ကြားညှပ် အစုကြီး» (^3-190): mahantarā has no duka in the Pāli; harmonise B5 rule: «နှစ်မျိုးတွဲ» only where the Pāli has duka.
- **A2** «အကြောင်းတို့၏ အခြင်းအရာ» (^3-190): literal and accurate for paccayākāra, single place. Termbase doubt logged: the ākāre entry's sense is svākāra.
- **A5** (^3-187, ^3-192), **B1** (^3-269), **B2** (^3-357): source as written (the Pāli elides / has no separator / has «..»). User rule: no added punctuation, slips as written (harmonise A2 / A4).
- **B4** (^3-447): the slip is rendered for its intended reading with the text's own words; aligning it with ^3-352 would drop the keyword's term.

## Termbase change (made upstream; inputs updated for it)

buddho|0 = «နားလည်ပြီးသော» (was «နားလည်အပ်သော»), termbase sha256 857bfa8eff94… (regen_rails.sh TB_SHA).
- `rails/adherence-zeroshot.txt` re-run with the new termbase: 6 → 8 misses (buddho at ^3-227 / ^3-455, the zero-shot's
  «နားလည်အပ်သော»).
- `rails/classify_misses.py`: GENUINE family `FAM = {"buddho": "F1"}`; `applied_ids` also reads `fixes-log.tsv` (rule IDs
  F n). Result: 8 zero-shot misses = GENUINE 2 (fixed by F1) + ARTEFACT 5 + INFLECTION 1; rails introduce 0.
- `rails/line_scan.py`: families F1 (subuddho req «ကောင်းစွာ နားလည်ပြီး ဖြစ်သည်», «နားလည်အပ်» forbidden anywhere) and F2
  (nāmarūpena req «စိတ်ပိုင်းနှင့် ရုပ်ပိုင်းတို့နှင့်», «ရုပ်ပိုင်းနှင့်» forbidden anywhere). Zero-shot 8 flags, rails 0.
- `rails/protected-md5-before.txt`: besides line 1 (termbase, set upstream), the md5s of `termbase/APPROVED.md`,
  `decisions-A.tsv` and `termbase-decisions.md` were still the pre-change values; the three files were changed upstream at
  12:18 with exactly this buddho change (APPROVED.md «Change 2026-11-19», decisions-A.tsv buddho|0). Their md5 lines were
  re-recorded (files themselves not touched; old list in `review/fix-backup/rails-scripts/`).

## Checks (regen_rails.sh; second run byte-identical, 31 files)

protected md5 unchanged (75 files); termbase sha256 = new lock; plain build = zero-shot 16 / 16; ids + text_pe + marks
OK in all 16 files; typography OK; adherence: zero-shot 8430 checked, 8 misses (input reproduced), rails 6 misses =
ARTEFACT 5 + INFLECTION 1, GENUINE fixed 2, GENUINE or unknown left 0; sense-level 0 unexplained of 8442; align: 75
repeated Pāli sentences, 5 differing = the accepted 5, 0 new; hidden 0 unmatched; pi-1 identity 13 / 13, pi-2 12 / 12;
line scan 0 (zero-shot 8 flags; 26 / 26 families with Pāli hits); zero-shot files unchanged; ALL CHECKS PASSED.
