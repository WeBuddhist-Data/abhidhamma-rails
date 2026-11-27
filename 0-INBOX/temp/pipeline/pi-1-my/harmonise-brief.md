# Brief: consistency pass over the pi-1 Burmese zero-shot (Dhammasaṅgaṇī «သဘောတရားများကို စုစည်းရေတွက်ခြင်း»)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Call Python as `python3 -I -X utf8` (scripts in files). Scratch only in 0-INBOX/temp/pipeline/pi-1-my/. Never commit. Never use the words for a planted starting value or its negative. Back up every generator, check or module you edit into pi-1-my/harmonise-backup/ first, and snapshot all 14 chapter files there before you start.

Six agents translated the book with their own generators on one shared module; they drifted on secondary formulas and terms. Your job: one form per item across the whole book, applied IN THE GENERATORS / the shared module (never by hand in the chapter files), then rebuild every chapter and re-run every check. Source rule: Pāli only; never look up or use any existing Burmese translation or nissaya; no web searches.

## Inputs
- Generators (pi-1-my/): make_sample.py (preamble, 1-matika), make_ch2-01.py, make_ch2-02-03.py, make_ch2-04-05.py, make_ch3.py, make_ch4.py, make_ch5.py; shared module my_formulas.py (you MAY edit it for shared strings, but the user-approved sample strings — the Mātikā items, book frame, cluster names, headings — stay unchanged unless the todo says otherwise; keep every generator working).
- my-zeroshot-terms.md is written by `make_sample.py --terms` (which drops the 2-01 section) and then re-completed by make_ch2-01.py: rebuild in that order.
- Checks: check_sample.py, check_ch2-01.py, check_ch2-02-03.py, check_ch2-04-05.py, check_ch3.py, check_ch4.py, check_ch5.py.
- Agents' notes pi-1-my/notes-*.md; the drift already reported: pi-1-my/harmonise-todo.md. Handle every item there and its precedence rule.
- Pāli: AI_translation/pali/pi-1_split_chapters/; Burmese: AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters/.
- Style: 0-INBOX/temp/pipeline/burmese-style.md (binding).
- Cross-chapter sentence check: `python3 -I -X utf8 0-INBOX/temp/pipeline/pi-4-mr/align_check.py <pali_dir> <my_dir> --all` (identical Pāli sentences must have identical Burmese) and `python3 -I -X utf8 0-INBOX/temp/pipeline/pi-4-mr/rails/align_hidden.py <pali_dir> <my_dir>`. Read both scripts first (they were written for Marathi; adapt a copy into pi-1-my/ if anything is language-specific, e.g. sentence end «။»). Save the before outputs as pi-1-my/align-before.txt / align-hidden-before.txt.

## What to align
- Every item in harmonise-todo.md.
- Every sentence align_check and align_hidden report: 0 left at the end, unless the Pāli context genuinely differs (explain each).
- The synonym tables: the same Pāli synonym = the same Burmese everywhere; within one list no two synonyms share a word.
- Headings and colophons consistent.
- Make pi-1-my/harmonise-table.tsv: Pāli<TAB>chosen Burmese<TAB>other forms<TAB>chapters; apply each item only where the Pāli line has it.

## Verify (all must pass)
For every chapter: check_chapter_ids.py, pi-6-mr/check_text_pe.py, pi-4-mr/check_marks.py print OK (delete chk-pe copies afterwards); every agent's own check reports 0 mismatches (update a check's expected Burmese only where you changed that form on purpose, and say so); align_check 0 differing (or explained); align_hidden 0 (or explained). Write the rebuild + all checks into one script pi-1-my/regen_zeroshot.sh, and confirm a second run changes no chapter byte.

## Log and report
Log every change in pi-1-my/harmonise-notes.md (item, chosen form, reason, generators changed, count). Final report short, numbers first: items aligned, lines changed per chapter, align_check before/after, align_hidden before/after, check results, anything left and why, and the list of chosen forms for the todo items (for the user's review).
