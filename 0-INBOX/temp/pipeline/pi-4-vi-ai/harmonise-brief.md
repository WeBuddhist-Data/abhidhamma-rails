# Brief: harmonise pass over the pi-4 Vietnamese zero-shot (Puggalapaññatti)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool at their full paths under D:\Work\OpenPecha\abhidhamma-rails, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. You are the only agent running. Edit ONLY the chapter files in AI_translation\vietnamese\pi-4-vietnamese-plain-zeroshot_split_chapters\ (the approved sample 1-matika.md / 2-ekakapuggalapannatti.md only where an item below names it), plus new files in 0-INBOX\temp\pipeline\pi-4-vi-ai\. Never create files at the repo root, outside the repo, or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, never run git, never write "seed". No web. Return your report as text.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. Grep only the specific files named here, never whole folders.

## Context
Chapters 3-11 were translated in parallel (three agents at a time, one chapter each) from the approved sample (preamble, 1-matika, 2-ekakapuggalapannatti; builder build_sample_vi.py with B.NAME for every person; terms vi-zeroshot-terms.md). Each chapter has build_<N>_vi.py and notes-<N>.md in 0-INBOX\temp\pipeline\pi-4-vi-ai\. agents-run.md lists the open points (lines with HARMONISE / FOR THE REVIEW). Read vietnamese-style.md (0-INBOX\temp\pipeline\) and the pi-3 harmonise tools as a model: 0-INBOX\temp\pipeline\pi-3-vi-ai\harmonise_vi.py, find_divergences_vi.py, vi_common.py, harmonise-notes.md (copy and adapt them to pi-4 paths; do not edit the pi-3 files).

## Method
1. Back up all chapter files to 0-INBOX\temp\pipeline\pi-4-vi-ai\backup-pre-harmonise\.
2. Write pi-4-vi-ai\harmonise_vi.py: exact string replacements, each with an asserted count, logged to harmonise-log.tsv (file, block id, old, new, reason). Do not rebuild chapters from their builders.
3. Find divergences in code (pi-4-vi-ai\find_divergences_vi.py → divergences.md): identical Pāli segments, lines, sentences and members must give identical Vietnamese across all chapters; pick the sample's or the majority form and justify it.
4. Settle the named points:
   - «Kathañca puggalo X hoti?» ch5 «Người như thế nào là X?» vs ch8 «Và như thế nào là X?»; and «Evaṃ puggalo X hoti.» «Như vậy là X.» everywhere. One form.
   - Person-plural questions: ch4 «… là những ai?» vs the sample's «là gì?»: persons take «là những ai?», non-persons «là gì?»; apply consistently (check the sample's own person questions too and report if the sample would change).
   - samannāgata: «được trang bị» vs ch6 «sở hữu» (beauty): one rule (same meaning = same word; state it).
   - «So» «Người ấy» / «Vị ấy» by referent (lay person / monk): check it is consistent.
   - The unquoted «Người này được gọi là X.» (where the Pāli has no quotes or dash) vs the quoted form: keep as written per the Pāli; check consistency.
   - **^4-176 «puratthimena narassa»** was rendered as nagarassa («ở phía đông thành phố»): a one-letter emendation that changes the word. User rule: translate as written. Render the Pāli as written (narassa = 'of the man / of a person'; check the commentary 1-SOURCES\Commentaries\pi-puggalapannatti-atthakatha.md and the English / Russian pi-4 rails for how the phrase reads) and list it for the user with both readings.
   - Variant-bracket labels: the same kind of variant gets the same label; (aṭṭhakathā) «(Chú giải)» everywhere.
   - Anything else the divergence finder shows.
5. Do not change counts or Pāli slips that were translated as written. Do not change what pi-1 / pi-2 / pi-3 strings say. Do not change B.NAME person names (if two chapters disagree on a name, the sample's name wins).

## Verify (all must pass)
For every chapter: check_chapter_ids.py OK, dashcheck.py 0 mismatches, pi-1-vi-ai\verify_rails_vi.py OK (commands in vi-zeroshot-brief.md). Re-run find_divergences_vi.py after the changes: remaining divergences listed with reasons in harmonise-notes.md. No «—», «:-», «….», «là là», «được được», «chánh niệm».

## Report (under 400 words, as text)
Lines changed per chapter; checks; each named point with the form chosen and why; points for the user (^4-176, anything you could not settle).
