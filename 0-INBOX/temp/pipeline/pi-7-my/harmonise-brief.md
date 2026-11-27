# Brief: consistency pass over the pi-7 Burmese zero-shot (Paṭṭhāna «အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»)

## Setup and rules
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh).
- Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8`. Call it by its full path, never through a quoted shell variable. Put scripts in files.
- Scratch goes only in `0-INBOX/temp/pipeline/pi-7-my/`.
- Never commit.
- Never use the words for a planted starting value or its negative.
- **Backups first:**
  - Back up every generator, check or module you edit into `pi-7-my/harmonise-backup/` before editing it.
  - Snapshot all 75 chapter files there before you start.
- **Sources:** Pāli only. Never open any existing Burmese translation or nissaya, never open `0-INBOX/temp/language-priority/`, and do no web searches.
- Read `pi-1-my/` … `pi-6-my/` only; never edit them.
- Never use /private/tmp or /tmp, and no `cd /tmp`.
- You are the only agent running, so you may use `pi-7-my/check_text_pe7.py` (it uses and deletes `pi-7-my/chk-pe/`).

## The job
Nineteen agents translated the book: the sample, eighteen groups and the coordinator's preamble. Each used its own generator, and most generators import earlier ones in memory. They drifted on some terms and frames.

Your job is to bring every item to one form across the whole book:
- Apply each change IN THE GENERATORS or in the shared module. Never edit the chapter files by hand.
- Then rebuild every chapter and re-run every check.

## Inputs
**Generators** (in `pi-7-my/`):
- make_sample.py (1-00, 1-02)
- make_ch1-01.py, make_ch1-03-05.py
- make_ch2-01-02.py, make_ch2-03-06.py, make_ch2-07-11.py, make_ch2-12-17.py
- make_ch3-01-02.py, make_ch3-03-06.py, make_ch3-07-08-10.py, make_ch3-09.py
- make_ch4-01.py, make_ch4-02-09.py, make_ch4-10-14.py, make_ch4-15-21.py
- make_ch5-01-04.py, make_ch5-05-12.py, make_ch5-13-20.py
- The preamble was written by the coordinator; reproduce it in the regen script as a fixed table.

How the generators fit together:
- **Map the import chain first.** Many generators import others and extend them in memory, so a change upstream reaches every chapter downstream. Rebuild in dependency order.
- **The «--regress» options** prove the upstream outputs are unchanged. After your edits they must agree with the NEW upstream outputs.
- **The shared module is my7_formulas.py.** You MAY edit it for shared strings. The coordinator-approved sample choices (agents.txt) stay unchanged unless an item below says otherwise. Keep every generator working.

**Checks:** check_sample.py and check_ch*.py. Each has a pi-1 … pi-6 reuse test, an identity test against the finished groups, and `--mutate`.

**Notes and drift:**
- The agents' notes are in `pi-7-my/notes-*.md`.
- The drift and rule issues are in **`pi-7-my/harmonise-todo.md` (H1–H24)**. Handle every item, with the decision it states. Where an item says "one form" without a decision, choose by this precedence:
  1. the locked pi-1 … pi-6 term or final rails Burmese;
  2. the approved sample;
  3. the form most chapters use;
  4. the plainest correct Burmese.

**Text and references:**
- Pāli: `AI_translation/pali/pi-7_split_chapters/`.
- Burmese: `AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/`.
- Style: `0-INBOX/temp/pipeline/burmese-style.md`.
- pi-1 … pi-6 final: `AI_translation/burmese/pi-{1,…,6}-burmese-plain-rails_split_chapters/` and the locked termbases.

**Cross-chapter sentence checks:**
- `0-INBOX/temp/pipeline/pi-1-my/align_check_my.py <pali_dir> <my_dir> --all`
- `pi-1-my/align_hidden_my.py <pali_dir> <my_dir>` (splits on «။»)

Save the before outputs as `pi-7-my/align-before.txt` / `align-hidden-before.txt`.

**pi-1 … pi-6 identity check:** write `pi-7-my/harmonise_pi123456.py`.
- Every Pāli sentence and heading of pi-7 that also occurs in pi-1 … pi-6 must have exactly their final (rails) Burmese.
- Report n / n per book, and every difference.
- Model: `pi-6-my/harmonise_pi12345.py` (read only).
- List each explained difference, for example an approved sample departure.

## What to align
- **The to-do list:** every item in harmonise-todo.md.
- **Repeated sentences:** every sentence that align_check and align_hidden report. Leave 0 at the end, unless the Pāli context really differs; explain each one you keep.
- **Identity:** pi-1 … pi-6 identity n / n, identical or explained.
- **Frames and terms:** the same Pāli must give the same Burmese everywhere. That covers:
  - the condition frames in every case and polarity, and the counting frames;
  - the term stacking «A၊ B N» and the na-X rule;
  - the section, order and part headings, and the notes («Yathā …», «-sadisaṃ», «vitthāretabbaṃ» …);
  - the colophons.
- **Supplied words (H8):** keep a supplied word only where the Pāli has an obvious omission. List every one you keep.
- **Change table:** write `pi-7-my/harmonise-table.tsv` with the columns Pāli<TAB>chosen Burmese<TAB>other forms<TAB>chapters. Apply each item only where the Pāli line has it.

## Verify (all must pass)
- **Every chapter:** check_chapter_ids.py, check_text_pe7.py and pi-4-mr/check_marks.py print OK.
- **Every agent's own check:** 0 mismatches, its reuse n / n, and its mutation test. Update a check's expected Burmese only where you changed that form on purpose, and say so.
- **Cross-chapter:** align_check 0 differing (or explained); align_hidden 0 (or explained); harmonise_pi123456 n / n.
- **One script:** write the full rebuild and all checks into `pi-7-my/regen_zeroshot.sh`. The generators are slow, so run it in the background if it takes over 2 minutes. Confirm that a second run changes no chapter byte.
- **Merged file:** finally, merge the chapters in book order (the pi-7 Pāli folder's order, as pi-6 did) into `AI_translation/burmese/pi-7-burmese-plain-zeroshot.md`. Check that the segment count equals the sum over the chapters.

## Log and report
- Log every change in `pi-7-my/harmonise-notes.md`: item, chosen form, reason, generators changed, count.
- Keep the final report short, numbers first:
  - items aligned;
  - lines changed per chapter;
  - align before / after, and align_hidden before / after;
  - pi-1 … pi-6 identity;
  - supplied words kept / removed;
  - check results;
  - anything left, and why;
  - the chosen forms for the to-do items, for review.

## Usage
You may be paused for usage limits. Save progress (notes, backups) as you go so you can resume.
