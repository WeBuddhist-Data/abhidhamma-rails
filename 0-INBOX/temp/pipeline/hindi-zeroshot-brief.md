# Brief: Hindi zero-shot, remaining chapters (pi-3, pi-4, pi-5)

Work in D:\Work\OpenPecha\abhidhamma-rails. The machine is Windows: use the Read/Write tools for files and PowerShell for commands, and run python as `python -I -X utf8`. Many agents translate other chapters in parallel (the user approved this). Write ONLY your own chapter files, plus helper scripts and notes named after your chapters inside your book's scratch folder.

The user approved the chapter-1 samples. Your job is to continue in exactly the same style.

## Read first
- **0-INBOX\temp\pipeline\hindi-style.md**: the shared rules, the strict dash rule, the cross-book core terms, the lessons from the Russian review and the verify commands. These are binding.
- **AI_translation\skills\zeroshot-translator.md** and **AI_translation\audience_profile\plain.md**.
- **Your book's approved term list** (READ-ONLY): 0-INBOX\temp\pipeline\pi-N-hi\hi-zeroshot-terms.md. Copy its formulas verbatim.
- **Your book's approved sample(s)**, which model structure, formulas and typography:
  - pi-3: AI_translation\hindi\pi-3-hindi-plain-zeroshot_split_chapters\1-uddeso.md, plus 0-INBOX\temp\pipeline\pi-3-hi\ch2-sample.md and make_ch2_sample.py.
  - pi-4: AI_translation\hindi\pi-4-hindi-plain-zeroshot_split_chapters\1-matika.md.
  - pi-5: 0-INBOX\temp\pipeline\pi-5-hi\ch1-sample.md and build_ch1_sample.py.
- **Cross-check of meaning only** (translate FROM THE PĀLI):
  - the English zero-shot, AI_translation\english\pi-N-english-plain-zeroshot_split_chapters\<same file>;
  - the user-approved Russian term notes in 0-INBOX\temp\pipeline\pi-3\, pi-4\ or pi-5-ru\ (ru-zeroshot-terms.md and notes-*.md). These show which decisions each chapter needs.

## Source and output
- Source: AI_translation\pali\pi-N_split_chapters\<ch>.md
- Output: AI_translation\hindi\pi-N-hindi-plain-zeroshot_split_chapters\<ch>.md, with the same filename. The folder exists.
- Long chapters may be written in parts and joined, but the final file must be complete.
- If your chapter's opening was already done as an approved sample (pi-3 ch2 lines 1–42, pi-5 ch1 lines 1–59), reuse that text unchanged and continue from there.

## Rules
- Identical Pāli formulas get identical Hindi, within your chapters and with the approved samples. A helper script with fixed formula strings is the safest way to guarantee this. Highly repetitive chapters (the Dhātukathā tables, the Kathāvatthu debate cycles) should be generated that way.
- If you settle a NEW recurring term, record it in 0-INBOX\temp\pipeline\pi-N-hi\notes-<your chapters>.md, one "Pāli = Hindi" per line. Do NOT edit hi-zeroshot-terms.md.
- No notes or commentary of your own inside the translation. Translate headings, editorial notes and variant brackets as in the samples.

## Verify every chapter (all must pass before you report)
Use the two commands in hindi-style.md:
- `check_chapter_ids.py` must print OK;
- the dash/line check must show equal line counts and 0 dash mismatches.

Also confirm there are no "—", no ":-" and no double blank lines.

## Final report (short)
- Per chapter: the checks passed and the segment count.
- Key new terms.
- Pāli you were unsure about.
