# Brief: apply the bilingual-review fixes to the pi-2 Burmese rails

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8` (scripts in files). Scratch only in `0-INBOX/temp/pipeline/pi-2-my/rails/` and `pi-2-my/review/`. Never use the system temp directory. Never commit. Never use the words for a planted starting value or its negative. No existing Burmese translation, nissaya or web source (never open `0-INBOX/temp/language-priority/`). Read `pi-1-my/` only; never edit it.

## Where to fix
The rails text `AI_translation/burmese/pi-2-burmese-plain-rails_split_chapters/` is built by `pi-2-my/rails/regen_rails.sh` (rails layer `my_formulas_rails.py` + `build_rails.py`, residual rules `apply_termbase.py`). Model: the pi-1 Burmese fix run, `pi-1-my/review/fix-brief.md`, `pi-1-my/review/fix-notes.md` and `pi-1-my/rails/apply_fixes.py`.
- A fix that changes a repeated formula or term goes into the rails layer (new labelled patches with exact counts), so identical Pāli keeps identical Burmese.
- Single-segment fixes go into a new `pi-2-my/rails/apply_fixes.py`, run by regen_rails.sh right after apply_termbase.py: each fix an explicit rule (exact old → new or a regex), restricted to the segment IDs or to lines whose Pāli has the triggering words, with an expected count (the run fails on a mismatch); log to `rails/fixes-log.tsv`.
- Do NOT edit the zero-shot chapters, the generators, `my2_formulas.py`, or the termbase / decisions / APPROVED.md (the termbase change below is already made).

## Inputs
`pi-2-my/review/report-A.md` (A1–A9) and `report-B.md` (B1–B6). Pāli: `AI_translation/pali/pi-2_split_chapters/`. Style: `0-INBOX/temp/pipeline/burmese-style.md`. Locked termbase and its note: `pi-2-my/termbase/APPROVED.md`.

## Termbase change already made (user-approved 2026-11-18)
`decisions-A.tsv` section «Review fix A8 / B2»: maccu|0 «သေဆုံးခြင်း», siṅgāratā|0 «ဟန်လုပ်ခြင်း»; reassembled, new sha256 6ffa74840ba6c9e018ae4abe089aa6116d0148da7cee4a94c04436fe4d53e658, already recorded in regen_rails.sh (TB_SHA) and protected-md5-before.txt. Update the adherence / classification inputs that depend on the termbase (adherence-zeroshot.txt and the classified rows will change for maccu and siṅgāratā: the zero-shot's «သေမင်း» / «ကြွားလုံး ထုတ်ခြင်း» become GENUINE misses fixed by your patches).

## Decisions (user and coordinator, 2026-11-18)
- **APPLY A1** (^2-188, 3-dhatu line 102): render the intended reading as ^1/^2 parallels do (1-khandha:695, 2-ayatana:77, 5-indriya:70): «… “…ဖြစ်နိုင်သော သဘောတရားများ”ဟု ခေါ်ဆို၍ မရ၊ မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်သော်လည်း မှားယွင်းသော ယူဆမှု မဟုတ်သော သဘောတရားများ ဖြစ်ကြသည်။»; the copied quote slip reverses the meaning. Keep the line's dash count equal to the Pāli. Log as a source slip rendered for its intended reading.
- **APPLY A2** (Dasāyatanā rūpā. / Dasa dhātuyo rūpā. / Sattindriyā rūpā.): «… သည် ရုပ် ဖြစ်သော သဘောတရားများ ဖြစ်ကြသည်။» (as 1-khandha:690 «ရုပ် ဖြစ်သော သဘောတရား ဖြစ်သည်»); find every «X rūpā.» predicate by script and fix all.
- **APPLY A3** (ch6, 10 compressed citta openings): put the qualifiers on the citta, as pi-1 does, so they cannot be read as describing the prompting or the object (e.g. «… ဖြစ်၍ … ယှဉ်တွဲလျက် / ကင်းကွာလျက် …»). Use pi-1's own Burmese for the same qualifier sequence where it exists; identical Pāli = identical Burmese; keep pi-1 identity.
- **APPLY A4** (^2-223 two sentences): add «သို့သော်» before «–» as in 2-ayatana:67 and 4-sacca:158; check by script for any other «၊ – “» of that formula without «သို့သော်».
- **APPLY A5** (^2-184): «… ဖြစ်ပေါ်သည်၊ မနောကိုလည်းကောင်း …» (add the «၊» that separates the two clauses; check the parallel tajjā… sentences for the same).
- **APPLY A8** maccu «သေဆုံးခြင်း» (^2-193, ^2-236) per the termbase change.
- **KEEP A6, A7** as written (user: source slips are translated as written; known, logged). **KEEP A9** («ဆဋ္ဌမ အာရုံခံ နယ်ပယ်» stays; consistent).
- **APPLY B1** (^2-U30): «ဤလမ်းမှားကို မှီဝဲခြင်း၊ နီးကပ်စွာ မှီဝဲခြင်း၊ ကောင်းစွာ မှီဝဲခြင်း၊ ဆည်းကပ်ခြင်း၊ ကောင်းစွာ ဆည်းကပ်ခြင်း၊ ကိုးကွယ်ခြင်း၊ ကောင်းစွာ ကိုးကွယ်ခြင်း၊ ထိုလမ်းမှားဘက်သို့ ညွတ်ကိုင်းခြင်း ရှိသမျှ»; check the other «X sevanā» definitions (e.g. pāpamittatā, the other *-sevanā) so each object is right and the sevanā words match the heading.
- **APPLY B2** siṅgaṃ «ဟန်လုပ်မှု», siṅgāratā «ဟန်လုပ်ခြင်း» in all places (mātikā item 35 ^2-832, heading ^2-17-2-10-0, ^2-852 definition and its closing quote).
- **APPLY B3** «ဤသာသနာ၌» at ^2-724 and ^2-796 (as the 125 others).
- **APPLY B4** drop the «၊» after «သတ္တဝါတို့အပေါ်၌» (8 lines, mettā / karuṇā / muditā / upekkhā).
- **APPLY B5** (^2-392): the list «၊» after the variant bracket; check the parallel lines with the same bracket.
- **APPLY B6** (^2-1023, 6 lines): «ထိုရက်ဖြင့် ရက် သုံးဆယ်သည် တစ်လ ဖြစ်သည်» (keep the rest; check every place of the formula).
- For every pattern, find ALL instances by script, apply only where the Pāli matches, and keep synonym lists distinct.

## Verify (all must pass, in regen_rails.sh)
For all 19 files: check_chapter_ids.py, check_text_pe_rails.py, pi-4-mr/check_marks.py OK; adherence on the rails: GENUINE 0 (classification updated only for the user-approved termbase change); pi-1 identity unchanged (321/321); align differences only the accepted zero-shot set (align_kept.py); line_scan 0; zero-shot files unchanged; termbase hash = the new lock. A second run must give byte-identical output.

## Report (short, numbers first)
Per fix ID: instances changed; lines changed per chapter; check results; align numbers; anything not applied and why. Same into `review/fix-notes.md`.
