# Brief: consistency pass over the pi-5 Burmese zero-shot (Kathāvatthu «အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း»)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8` (scripts in files). Scratch only in `0-INBOX/temp/pipeline/pi-5-my/`. Never commit. Never use the words for a planted starting value or its negative. Back up every generator, check or module you edit into `pi-5-my/harmonise-backup/` first, and snapshot all 32 chapter files there before you start. Source rule: Pāli only; never open any existing Burmese translation or nissaya (never `0-INBOX/temp/language-priority/`); no web searches. Read `pi-1-my/` … `pi-4-my/` only; never edit them. Never use /private/tmp.

Four agents (the sample and three groups) translated the book with their own generators on one shared module; they drifted on some terms and some "corrected" source slips. Your job: one form per item across the whole book, applied IN THE GENERATORS / the shared module (never by hand in the chapter files), then rebuild every chapter and re-run every check.

## Inputs
- Generators (pi-5-my/): make_sample.py (preamble, 1), make_ch2-5.py, make_ch6-10.py, make_ch11-12.py, make_ch13-16.py, make_ch17-20.py, make_ch21-25.py, make_ch26-31.py (note the import chain: later generators import make_ch11-12 → make_ch6-10 → make_sample; make_ch2-5 is separate); shared module my5_formulas.py (+ terms_my5.py) (you MAY edit it for shared strings; the user-approved sample strings stay unchanged; keep every generator working). make_sample.py also writes my5-zeroshot-terms.md.
- Checks: check_sample.py, check_ch*.py (each with a pi-1 … pi-4 reuse test).
- Agents' notes pi-5-my/notes-*.md; the drift and rule issues: **pi-5-my/harmonise-todo.md** (handle every item, with its precedence).
- Pāli: AI_translation/pali/pi-5_split_chapters/; Burmese: AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters/.
- Style: 0-INBOX/temp/pipeline/burmese-style.md. pi-1 … pi-4 final: AI_translation/burmese/pi-{1,2,3,4}-burmese-plain-rails_split_chapters/ and the locked termbases pi-{1,2,3,4}-pali-burmese-termbase-plain.md.
- Cross-chapter sentence checks: `0-INBOX/temp/pipeline/pi-1-my/align_check_my.py <pali_dir> <my_dir> --all` and `pi-1-my/align_hidden_my.py <pali_dir> <my_dir>` (split on «။»). Save the before outputs as pi-5-my/align-before.txt / align-hidden-before.txt.
- **pi-1 … pi-4 identity check:** write `pi-5-my/harmonise_pi1234.py`: every Pāli sentence (and heading) of pi-5 that also occurs in pi-1, pi-2, pi-3 or pi-4 must have exactly their final (rails) Burmese (report n / n per book and every difference). Model: `0-INBOX/temp/pipeline/pi-4-my/harmonise_pi123.py` (read only). Where pi-5 adapts a pi-1 / pi-2 sentence on purpose (e.g. the arahant sentence without «တော်မူ»), list it as an explained difference.

## What to align
- Every item in harmonise-todo.md (part A: source slips as written; part B: term drift).
- Every sentence align_check and align_hidden report: 0 left at the end unless the Pāli context genuinely differs (explain each).
- pi-1 … pi-4 identity: n / n identical (or explained).
- The dialectic frames, propositions, sutta quotations and term tables: the same Pāli = the same Burmese everywhere.
- Headings and colophons consistent.
- pi-5-my/harmonise-table.tsv: Pāli<TAB>chosen Burmese<TAB>other forms<TAB>chapters; apply each item only where the Pāli line has it.

## Verify (all must pass)
For every chapter: check_chapter_ids.py, pi-6-mr/check_text_pe.py, pi-4-mr/check_marks.py print OK (delete chk-pe copies afterwards); every agent's own check reports 0 mismatches and its reuse n / n (update a check's expected Burmese only where you changed that form on purpose, and say so); align_check 0 differing (or explained); align_hidden 0 (or explained); harmonise_pi1234 n / n. Write the rebuild + all checks into one script pi-5-my/regen_zeroshot.sh, and confirm a second run changes no chapter byte.

## Log and report
Log every change in pi-5-my/harmonise-notes.md (item, chosen form, reason, generators changed, count). Final report short, numbers first: items aligned, lines changed per chapter, align before/after, align_hidden before/after, pi-1 … pi-4 identity, source slips reverted / kept (with reasons), check results, anything left and why, and the chosen forms for the todo items (for the user's review).

Usage: you may be paused for usage limits; save progress (notes, backups) as you go so you can resume.
