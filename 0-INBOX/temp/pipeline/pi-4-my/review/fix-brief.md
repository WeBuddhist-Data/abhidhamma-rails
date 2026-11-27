# Brief: apply the bilingual-review fixes to the pi-4 Burmese rails

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8` (scripts in files). Scratch only in `0-INBOX/temp/pipeline/pi-4-my/rails/` and `pi-4-my/review/` (never the system temp directory: not /private/tmp, not /tmp, no `cd /tmp`). Never commit. Never use the words for a planted starting value or its negative. No existing Burmese translation, nissaya or web source (never open `0-INBOX/temp/language-priority/`). Read `pi-1-my/`, `pi-2-my/`, `pi-3-my/` only; never edit them.

## Where to fix
The rails text `AI_translation/burmese/pi-4-burmese-plain-rails_split_chapters/` is built by `pi-4-my/rails/regen_rails.sh` (layer `my_formulas_rails.py` + `build_rails.py`, rules `apply_termbase.py`). Model: `pi-3-my/rails/apply_fixes.py` and `pi-2-my/review/fix-notes.md`.
- A fix that changes a repeated formula goes into the rails layer (labelled patches with exact counts).
- Single-segment fixes go into a new `pi-4-my/rails/apply_fixes.py`, run by regen_rails.sh right after apply_termbase.py: explicit rules restricted to segment IDs or Pāli triggers, with expected counts (the run fails on a mismatch); log to `rails/fixes-log.tsv`.
- Do NOT edit the zero-shot chapters, the generators, `my4_formulas.py`, or the termbase / decisions / APPROVED.md.

## Inputs
`pi-4-my/review/report-A.md` (A1–A6), `report-B.md` (B1–B6), the rails doubts in `pi-4-my/rails/notes-rails.md`. Pāli: `AI_translation/pali/pi-4_split_chapters/`. Style: `0-INBOX/temp/pipeline/burmese-style.md`. Locked termbase: `pi-4-my/termbase/APPROVED.md`.

## Termbase change already made (2026-11-20, coordinator under the user's standing go-ahead)
narassa|0 «မြို့» (was «လူ»), sāci|0 «ကွေ့ဝိုက်သော» (was «ကောက်ကျစ်သော»); new sha256 6ba052ff7edfcfa36d808b8aaf8b69600ce303d13381aaee4b8a81d3d92c2723, already in regen_rails.sh TB_SHA and protected-md5-before.txt line 1. Re-run the zero-shot adherence input with the new termbase and update the classification.

## Decisions
- **APPLY A1** (^4-M-16): «“ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း” ခေါင်းစဉ်စာရင်း ပြီးဆုံးပြီ။» (the book title, as ^4-209).
- **APPLY A6** (^4-94): drop the added «ဤ» (the Pāli has no ime): «ထို့အတူပင် လူနာနှင့် တူသော ပုဂ္ဂိုလ် သုံးယောက်တို့သည် …».
- **KEEP A2** («စေတနာ» is part of the approved person-type name; everyday Burmese), **A3, A4** (the Pāli has no full stop / comma; user rule: no added punctuation), **A5** (paññapeti «ပညတ်» = the locked pi-2 usage, 15× in pi-2 ch17).
- **APPLY B1** (^4-176): «မြို့၏ အရှေ့ဘက်၌ …» (termbase narassa «မြို့»).
- **APPLY B2** (^4-166, all 4 lines, the same form): the praise / blame are what can be said, not the speaker's own: «ဤလောက၌ အချို့သော ပုဂ္ဂိုလ်အဖို့ ချီးမွမ်းဖွယ်လည်း ရှိ၏၊ ကဲ့ရဲ့ဖွယ်လည်း ရှိ၏။ ထိုတို့အနက် ကဲ့ရဲ့ဖွယ် ရှိသမျှကို …» (and the matching vaṇṇa line); «tattha» = «ထိုတို့အနက်» as elsewhere in the book. Keep every other word of the 4 lines.
- **APPLY B3** (^4-171): the Pāli order: «ချီးမွမ်းစကား၊ ထောမနာစကား၊ ချီးကျူးစကား၊ ဂုဏ်သတင်း ဆောင်ယူချက်» (check which Burmese word is the termbase term of parathomanā / parapasaṃsanā and put each at its Pāli slot; same in every place of this list).
- **APPLY B4** (^4-164, ^4-165, the 4 pasāda / appasāda lines only): no added «ပြောဆို၏»; the line ends with the pasādaṃ / appasādaṃ janeti verb phrase of the text (its termbase term), e.g. «… ဟူ၍လည်း ကြည်ညိုမှုကို ဖြစ်စေ၏» / «… မကြည်ညိုမှုကို ဖြစ်စေ၏» — use the text's own janeti phrase. The bhāsati lines keep «ပြောဆို၏».
- **APPLY B5** (^4-178, and every «Yā sā vācā … tathārūpiṃ vācaṃ bhāsitā hoti» line): a relative clause, as pi-1 renders the same frame (check pi-1 ^1-1350 and use its form if the Pāli matches): «… စကား ရှိသမျှ၊ ထိုသို့သော စကားကို ပြောဆိုသူ ဖြစ်၏» only if pi-1 has «၊» there; otherwise without it.
- **APPLY B6** (^4-175): «… သို့မဟုတ် ကြမ်းကြုတ်သော အလုပ်ကို လုပ်ကိုင်သော အခြား တစ်စုံတစ်ယောက် ဖြစ်၏» (keep the termbase term for kurūrakammanta).
- **APPLY rails doubt 5** (^4-179): sāci «ကွေ့ဝိုက်…» per the termbase change, nikati keeps «ကောက်ကျစ်ခြင်း».
- For every pattern, find ALL instances by script and apply only where the Pāli matches.

## Verify (all must pass, in regen_rails.sh)
All 12 files: check_chapter_ids.py, check_text_pe (wrapper), check_marks.py OK; adherence: GENUINE 0; pi-1 / pi-2 / pi-3 identity unchanged (45/45, 35/36 + 1 explained, 2/2); align 0 differing; align_hidden 0; line_scan 0; zero-shot files unchanged; termbase hash = the new lock. A second run must give byte-identical output.

## Report (short, numbers first)
Per fix ID: instances changed; lines changed per chapter; check results; anything not applied and why. Same into `review/fix-notes.md`, with the KEEP decisions and their reasons.
