# Brief: apply the bilingual-review fixes to the pi-3 Burmese rails

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8` (scripts in files). Scratch only in `0-INBOX/temp/pipeline/pi-3-my/rails/` and `pi-3-my/review/` (never the system temp directory, not even /private/tmp). Never commit. Never use the words for a planted starting value or its negative. No existing Burmese translation, nissaya or web source (never open `0-INBOX/temp/language-priority/`). Read `pi-1-my/` and `pi-2-my/` only; never edit them.

## Where to fix
The rails text `AI_translation/burmese/pi-3-burmese-plain-rails_split_chapters/` is built by `pi-3-my/rails/regen_rails.sh` (layer `my_formulas_rails.py` + `build_rails.py`, rules `apply_termbase.py`, both empty so far). Model: the pi-2 fix run, `pi-2-my/review/fix-brief.md`, `fix-notes.md` and `pi-2-my/rails/apply_fixes.py`.
- A fix that changes a repeated formula goes into the rails layer (labelled patches with exact counts).
- Single-segment fixes go into a new `pi-3-my/rails/apply_fixes.py`, run by regen_rails.sh right after apply_termbase.py: explicit rules restricted to segment IDs or to lines whose Pāli has the triggering words, with expected counts (the run fails on a mismatch); log to `rails/fixes-log.tsv`.
- Do NOT edit the zero-shot chapters, the generators, `my3_formulas.py`, or the termbase / decisions / APPROVED.md.

## Inputs
`pi-3-my/review/report-A.md` (A1–A5) and `report-B.md` (B1–B4). Pāli: `AI_translation/pali/pi-3_split_chapters/`. Style: `0-INBOX/temp/pipeline/burmese-style.md`. Locked termbase: `pi-3-my/termbase/APPROVED.md`.

## Termbase change already made (2026-11-19, coordinator under the user's standing go-ahead)
buddho|0 = «နားလည်ပြီးသော» (was «နားလည်အပ်သော»); new sha256 857bfa8eff945d72eb1a52ec55c452798b34f9d11860322bfe7cc15096f243f3, already in regen_rails.sh TB_SHA and protected-md5-before.txt line 1. Re-run the zero-shot adherence input with the new termbase (buddho at ^3-227 / ^3-455 becomes a GENUINE miss fixed by your rule) and update the classification accordingly.

## Decisions
- **APPLY A3 + B3 (one form, both verse lines, ^3-227 and ^3-455):** «… နှစ်ပါး၊ အပိုင်းအခြားနှင့်တကွ ဤခွဲနည်းကို ကောင်းစွာ နားလည်ပြီး ဖြစ်သည်။». At ^3-227 the variant bracket stays right after its word: «အပိုင်းအခြား [ပါဌ်ကွဲ (Syā.): dvevīsati]နှင့်တကွ …» (keep the bracket text and the «[» count exactly as now). Keep the line's dash / «…» counts.
- **APPLY A4:** «nāmarūpena» items rendered «စိတ်ပိုင်းနှင့် ရုပ်ပိုင်းနှင့်» → «စိတ်ပိုင်းနှင့် ရုပ်ပိုင်းတို့နှင့်» (find every instance by script; only where the Pāli has nāmarūpena; same in all frames).
- **KEEP A1** «ကြားညှပ် အစုကြီး» (mahantarā has no duka in the Pāli; harmonise B5 rule: «နှစ်မျိုးတွဲ» only where the Pāli has duka).
- **KEEP A2** «အကြောင်းတို့၏ အခြင်းအရာ» (literal and accurate for paccayākāra, single place; termbase doubt logged: the ākāre entry's sense is svākāra).
- **KEEP A5, B1, B2** (source as written: the Pāli elides / has no separator / has «..»; user rule: no added punctuation, slips as written; harmonise A2 / A4).
- **KEEP B4** (^3-447 slip rendered for its intended reading with the text's own words; aligning would drop the keyword's term).

## Verify (all must pass, in regen_rails.sh)
All 16 files: check_chapter_ids.py, check_text_pe (wrapper), check_marks.py OK; adherence: GENUINE 0; pi-1 / pi-2 identity unchanged (13/13, 12/12); align differences only the accepted 5; align_hidden 0; line_scan 0; zero-shot files unchanged; termbase hash = the new lock. A second run must give byte-identical output.

## Report (short, numbers first)
Per fix ID: instances changed; lines changed per chapter; check results; anything not applied and why. Same into `review/fix-notes.md`, with the KEEP decisions and their reasons.
