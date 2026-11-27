# Brief: apply the bilingual-review fixes to the pi-5 Burmese rails

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8` (scripts in files). Scratch only in `0-INBOX/temp/pipeline/pi-5-my/rails/` and `pi-5-my/review/` (never the system temp directory: not /private/tmp, not /tmp, no `cd /tmp`). Never commit. Never use the words for a planted starting value or its negative. No existing Burmese translation, nissaya or web source (never open `0-INBOX/temp/language-priority/`). Read `pi-1-my/` … `pi-4-my/` only; never edit them.

## Where to fix
The rails text `AI_translation/burmese/pi-5-burmese-plain-rails_split_chapters/` is built by `pi-5-my/rails/regen_rails.sh` (layer `my_formulas_rails.py` + `build_rails.py`, rules `apply_termbase.py` / `residual_rules.py`). Model: `pi-4-my/rails/apply_fixes.py` and `pi-4-my/review/fix-notes.md`.
- A fix that changes a repeated formula or proposition goes into the rails layer (labelled patches with exact counts), so every repetition changes together.
- Single-segment fixes go into a new `pi-5-my/rails/apply_fixes.py`, run by regen_rails.sh after the existing rules: explicit rules restricted to segment IDs or Pāli triggers, with expected counts (the run fails on a mismatch); log to `rails/fixes-log.tsv`.
- Do NOT edit the zero-shot chapters, the generators, `my5_formulas.py`, or any termbase / decisions / APPROVED.md file.

## Inputs
`pi-5-my/review/report-A.md` (A1–A22), `report-B.md` (B1–B20). Pāli: `AI_translation/pali/pi-5_split_chapters/`. Style: `0-INBOX/temp/pipeline/burmese-style.md`. Locked termbase: `pi-5-my/termbase/APPROVED.md`.

## Termbase change already made (2026-11-22, coordinator under the user's standing go-ahead)
See APPROVED.md «Change 2026-11-22 (bilingual review A / B)»: appiyaṃ «မခွဲခြား»; abhisambuddhāni / Abhisambujjhitvā / abhisambujjhati «ကိုယ်တိုင် အပြည့်အဝ သိမြင်…»; Bhaṭo «ကျွေးမွေးခဲ့သူ»; voropeti «သတ်သည်», voropetvā «သတ်၍», mātaraṃ voropetvā / Asañcicca voropetvā «…အသက်မှ သတ်၍» (the passive jīvitā voropitā keeps «ချခံရသော»); ānantariko / ānantariyassa / Dhammasaññī ānantariko «ချက်ချင်း အကျိုးပေးသော ကံ…»; samphaṃ «အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား». New sha256 dbc048698d57557f5a6900a770d799f0deecdc6ec29cfe9ff1bb4d378d38e0d6, already in regen_rails.sh TB_SHA, and the four termbase-folder md5s are re-recorded in protected-md5-before.txt. Re-run the zero-shot adherence input with the new termbase and update the classification (the rows the change makes GENUINE are fixed by your rules / patches).

## Decisions
- **APPLY (meaning):** B1 (every verb of ^5-651 negated, both persons), B2 (^5-491 prose and verse: «ငါတို့ ကျွေးမွေးခဲ့သူသည် ငါတို့ကို ပြန်လည် ကျွေးမွေးလိမ့်မည်»: no added «သား», the Pāli has no word for it), B3, A1, A2 + A3 (the identity formula in all its lines: «…ဟူသော စကားကို မခွဲခြားဘဲ … ဤစကားတို့သည် တစ်ခုတည်း ဖြစ်သော၊ အနက် တူသော၊ …»; find every instance by script), A4, A5, A6, A7 (restore the line order; each bracket on the line of its word).
- **APPLY (consistency):** B4 (paṇidahantassa / appaṇidahantassa «ဆုတောင်းသူ / မဆုတောင်းသူ» everywhere, or the termbase's «ဆုတောင်းသော» form in attributive use), B5 (active voropeti «အသက်မှ သတ်…» book-wide per the termbase; passive stays), B6, B7 (pi-2 / pi-3 «အင်္ဂါ ရှစ်ပါး ရှိသော အရိယာ မဂ်»), B8 (pettivisaya «ပြိတ္တာ ဘုံ», pi-2), B9 (one wording for the SN quotation and the ch31 thesis, without the doubled «ဆင်းရဲ ဒုက္ခ»: use the termbase term of dukkhaṃ in this sense; the reference bracket after «ဟု»), B10 (one wording, 20:29's), B11, B12 (samphappalāpa everywhere per the termbase), B13 (align ch15 / ch16 with ch24), A15, A16 («ကဲ၊» where the Pāli is Handa in the same use), A17, A18.
- **APPLY (minor):** A8, A9, A10, A11, A12, A13, A14, A20, B14, B15 (saḷāyataniko attabhāvo without «ရရှိခြင်း» where the Pāli has no paṭilābha, book-wide), B17, B18, B19, A22 (every bracket right after its word).
- **APPLY (quote rule):** A21 + B20: no quote mark where the Pāli has none, in every vagga colophon and kathā heading of the book (the approved «“X” ပြီးဆုံးပြီ» section-end form keeps its quotes; it is the pi-1 … pi-4 pattern). Drop the stray ’ at 10:258.
- **KEEP A19** (harmonise decision: the divine eye sees «အဆင်းအရောင်» (pi-2 ^2-517), the thesis «Rūpaṃ puggalo» keeps «ရုပ်» as everywhere in the book; identical propositions keep one wording).
- **KEEP B16** (kapiñjara «ငှက်ကြီး»: no attested Burmese bird name in the sources; the termbase term stands).
- For every pattern, find ALL instances by script and apply only where the Pāli matches; keep identical Pāli = identical Burmese.

## Verify (all must pass, in regen_rails.sh)
All 32 files: check_chapter_ids.py, check_text_pe (wrapper), check_marks.py OK; adherence: GENUINE 0; pi-1 … pi-4 identity unchanged (2/2, 4/4, 2/21 + 19 explained, 5/7 + 2 explained); align only the accepted 1:426; align_hidden 0; line_scan 0; zero-shot files unchanged; termbase hash = the new lock. A second run must give byte-identical output.

## Report (short, numbers first)
Per fix ID: instances changed; lines changed per chapter; check results; anything not applied and why. Same into `review/fix-notes.md`, with the KEEP decisions and their reasons.
