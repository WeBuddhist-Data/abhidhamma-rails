# Brief: apply the bilingual-review fixes to the pi-1 Burmese rails

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8` (scripts in files). Scratch only in `0-INBOX/temp/pipeline/pi-1-my/rails/` and `review/`. Never commit. Never use the words for a planted starting value or its negative. No existing Burmese translation, nissaya or web source (never open `0-INBOX/temp/language-priority/`).

## Where to fix
The rails text `AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters/` is built by `pi-1-my/rails/regen_rails.sh` (rails layer `my_formulas_rails.py` + `build_rails.py`, residual rules `apply_termbase.py`). Add the review fixes the same way as the Marathi run (model: `0-INBOX/temp/pipeline/pi-1-mr/rails/apply_fixes.py` and `pi-1-mr/review/fix-brief.md`):
- a fix that changes a repeated formula or term goes into the rails layer (new labelled patches with exact counts);
- single-segment fixes go into a new `pi-1-my/rails/apply_fixes.py`, run by regen_rails.sh right after apply_termbase.py: each fix an explicit rule (exact old → new or a regex), restricted to the segment IDs or to lines whose Pāli has the triggering words, with an expected count (the run fails on a mismatch); log to `rails/fixes-log.tsv`.
- Do NOT edit the zero-shot chapters or generators.

## Inputs
`pi-1-my/review/report-A.md` (A1–A5) and `report-B.md` (B1–B11). Pāli: `AI_translation/pali/pi-1_split_chapters/`. Style: `0-INBOX/temp/pipeline/burmese-style.md`. Locked termbase and its note: `pi-1-my/termbase/APPROVED.md`.

## Decisions (user and coordinator, 2026-11-17)
- **APPLY** A1, A2 (vipāka headings: the result, not the kamma, is abyākata; pattern of ^1-565), A3 («ကံ၏ ကြီးကျယ်သော အကျိုး»), A4 (suññata sub-headings with «ဈာန်», as the appaṇihita ones), A5 (no «၊» inside the «neva sātaṃ nāsātaṃ» item, all 15 places).
- **APPLY** B1 (lobha list: first rūpataṇhā «သိမ်မွေ့သော ရုပ်ဘဝကို တပ်မက်မှု», second «အဆင်းအရောင်ကို တပ်မက်မှု», all 3 segments), B2 (drop «စီ» only; no «၊» added: the Pāli is translated as written), B4 (Dasa kilesavatthūni = «ကိလေသာ အခြေခံ ဆယ်ပါး», the termbase's vatthūni, in both places), B6 (cittahetuka = «စိတ်ကို အကြောင်းပြုသော», negative «… မဟုတ်သော»: the termbase's hetū "causes" sense; all places), B7 (one stem for byāpatti / byāpajjanā / byāpajjitattaṃ in that list; check the termbase for byāpatti and keep the three items distinct), B8 (the bhūmi locative frame with a noun: «… ကာမဘုံနှင့် ဆိုင်သော စိတ်၊ … စိတ်တို့၌», all 18 segments, same pattern), B9 (kusalābyākatā / kusalākusalābyākatā runs: «ကုသိုလ် သဘောတရားနှင့် …», all 48), B10 (drop the added «သေပြီးနောက်» in ^1-1322 … ^1-1325; labels otherwise unchanged), B11 (link the list to «အခြား ရုပ်» with «ဖြစ်သည့်», all 36).
- **APPLY, user decision: bahiddhā = «မိမိ၏ ပြင်ပ၌» (outside oneself) book-wide** for the "external / belonging to others" sense: the Mātikā triad items (bahiddhā dhammā «မိမိ၏ ပြင်ပ၌ ရှိသော သဘောတရား», ajjhattabahiddhā, bahiddhārammaṇā, ajjhattabahiddhārammaṇā), «ajjhattaṃ vā bahiddhā vā» (incl. the four elements, B5), ^1-1435 (B3) and every other use of that sense. This changes the locked termbase: do it ONLY through `pi-1-my/termbase/decisions-A.tsv` (a new commented section «Review fix, user-approved 2026-11-17») + `termbase_assemble.py 1 burmese my plain` ("no errors"), then add a dated note and the new sha256 to `termbase/APPROVED.md` and update regen_rails.sh's recorded termbase hash. The other two bahiddhā senses stay («ပြင်ပ၌» in the bases of mastery, «အပြင်ဘက်» for ito bahiddhā).
- For every pattern, find ALL instances by script, apply only where the Pāli matches, and keep synonym lists distinct and identical Pāli = identical Burmese.

## Verify (all must pass, in regen_rails.sh)
For all 14 chapters: check_chapter_ids.py, pi-6-mr/check_text_pe.py, pi-4-mr/check_marks.py OK (delete chk-pe copies); adherence on the rails: GENUINE 0 (classification updated only for the user-approved termbase change); align_check_my --all 0 differing, align_hidden_my 0 unmatched; line_scan 0; zero-shot files unchanged. A second run must give identical output.

## Report (short, numbers first)
Per fix ID: instances changed; lines changed per chapter; check results; align numbers; the termbase change (entries, new hash); anything not applied and why. Same into `review/fix-notes.md`.
