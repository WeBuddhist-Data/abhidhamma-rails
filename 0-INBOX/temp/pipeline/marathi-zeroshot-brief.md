# Brief: Marathi zero-shot, remaining chapters (pi-3)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails. The machine is macOS (zsh). Use the Read/Write tools for files, and run Python as `python3 -I -X utf8`. Write helper scripts to files rather than inline `python3 -c` with regexes. Several agents translate other chapters in parallel (the user approved this). Write ONLY your own chapter files, plus helper scripts and notes named after your chapters inside `0-INBOX/temp/pipeline/pi-3-mr/`. Never use the system temp directory. Do not commit anything.

The user approved the chapter-1 and chapter-2-opening samples. Your job is to continue in exactly the same style.

## Read first
- **0-INBOX/temp/pipeline/marathi-style.md**: the shared rules, the strict dash rule, the core terms, the lessons from the Russian review and the verify commands. Binding.
- **AI_translation/skills/zeroshot-translator.md** and **AI_translation/audience_profile/plain.md**.
- **The approved term list** (READ-ONLY): 0-INBOX/temp/pipeline/pi-3-mr/mr-zeroshot-terms.md. Copy its formulas verbatim.
- **The formula module** (READ-ONLY): 0-INBOX/temp/pipeline/pi-3-mr/mr_formulas.py. Import it in your generator (`sys.path.insert(0, <that folder>)`). Do not edit it; if you need a new helper, define it in your own script and log the new string in your notes.
- **The approved samples**, which model structure, formulas and typography:
  - AI_translation/marathi/pi-3-marathi-plain-zeroshot_split_chapters/1-uddeso.md
  - 0-INBOX/temp/pipeline/pi-3-mr/ch2-sample.md, built by make_ch2_sample.py.
- **Cross-check of meaning only** (translate FROM THE PĀLI):
  - the Hindi zero-shot, AI_translation/hindi/pi-3-hindi-plain-zeroshot_split_chapters/<same file> (it went through a user-approved review; use it to see what each Pāli term means and how the structure was handled, then write natural Marathi, not a word-for-word copy of the Hindi);
  - the English zero-shot, AI_translation/english/pi-3-english-plain-zeroshot_split_chapters/<same file>.

## Source and output
- Source: AI_translation/pali/pi-3_split_chapters/<ch>.md
- Output: AI_translation/marathi/pi-3-marathi-plain-zeroshot_split_chapters/<ch>.md, same filename. The folder exists.
- Chapter 2 only: its opening (^3-2-0 to ^3-36) is the approved sample. Copy make_ch2_sample.py to make_ch2.py, keep those blocks byte-for-byte, and continue from ^3-37. Self-check in the script that the first 36 blocks equal ch2-sample.md.

## Rules
- Identical Pāli formulas get identical Marathi, within your chapters and with the approved samples. These chapters are tables of near-identical sentences: GENERATE them with a script that uses the mr_formulas helpers, with a per-segment spec (subject, numbers, singular/plural/gender). Don't type repeated formulas by hand.
- Get every number right. After generating, check by script that the sequence of numbers in each Marathi line matches the Pāli line (e.g. map Pāli ekena/dvīhi/tīhi/catūhi/pañcahi/… and the Marathi number words to integers and compare; ignore numbers inside the group closers).
- Get polarity right: saṅgahita/asaṅgahita (समाविष्ट / बाहेर), sampayutta/vippayutta (जोडलेले / वेगळे), "Natthi" (कशाशीही नाही), "kehici" (अंशतः).
- Gender/number agreement: see the "Association / dissociation" section of the terms list.
- Dhammasaṅgaṇī mātikā items (kusalā dhammā, hetū dhammā, saraṇā dhammā, …) and the summary verses (uddāna) at chapter ends: translate their meaning in plain Marathi, in the same form wherever they recur in your chapters. Log every such item in your notes; a consistency pass will align them across agents afterwards.
- If you settle a NEW recurring term or phrase, record it in 0-INBOX/temp/pipeline/pi-3-mr/notes-<your chapters>.md, one "Pāli = Marathi" per line. Do NOT edit mr-zeroshot-terms.md.
- No notes or commentary of your own inside the translation. Translate headings, editorial notes and variant brackets as in the samples and the style file.
- Never write "—" or "–" unless the Pāli line has one at that spot (same count per line). No "।", no ":-".

## Verify every chapter (all must pass before you report)
```
python3 -I -X utf8 0-INBOX/temp/pipeline/check_chapter_ids.py AI_translation/pali/pi-3_split_chapters AI_translation/marathi/pi-3-marathi-plain-zeroshot_split_chapters <ch>.md
python3 -I -X utf8 0-INBOX/temp/pipeline/pi-3-mr/check_text.py AI_translation/pali/pi-3_split_chapters/<ch>.md AI_translation/marathi/pi-3-marathi-plain-zeroshot_split_chapters/<ch>.md
```
The first must print OK. The second must print OK (equal line counts, dashes match, ellipses match, no "।", no ":-", no double blank lines). Plus your own number check: 0 mismatches.

## Final report (short)
- Per chapter: the checks passed, segment count, number-check result.
- Key new terms (or point to your notes file).
- Pāli you were unsure about, and any source slips (translate as written and flag; don't fix the Pāli).
