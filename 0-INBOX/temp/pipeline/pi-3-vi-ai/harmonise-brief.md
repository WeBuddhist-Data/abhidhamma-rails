# Brief: harmonise pass over the pi-3 Vietnamese zero-shot (Dhātukathā)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool at their full paths, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. You are the only agent running. Edit ONLY the chapter files in AI_translation\vietnamese\pi-3-vietnamese-plain-zeroshot_split_chapters\ (never 1-uddeso.md and 2-pathamanayo.md text that the user approved as the sample, except an item below names them), plus new files in 0-INBOX\temp\pipeline\pi-3-vi-ai\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, never run git, never write "seed" or "unseeded". No web. Return your report as text.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. Grep only the specific files named here, never whole folders.

## Context
Chapters 3-15 were translated in parallel (up to three agents at once, one chapter each), from the approved sample (preamble, 1-uddeso, 2-pathamanayo; builder build_sample_vi.py; terms vi-zeroshot-terms.md) and the coordinator's SHARED FRAMES in vi-zeroshot-brief.md. Each chapter has build_<N>_vi.py and notes-<N>.md in 0-INBOX\temp\pipeline\pi-3-vi-ai\. agents-run.md lists the open points (lines marked HARMONISE). Read vietnamese-style.md (0-INBOX\temp\pipeline\) and the pi-2 harmonise pattern (0-INBOX\temp\pipeline\pi-2-vi-ai\harmonise-brief.md, harmonise_vi.py) first.

## Method
1. Back up all 16 chapter files to 0-INBOX\temp\pipeline\pi-3-vi-ai\backup-pre-harmonise\.
2. Write harmonise_vi.py: exact string replacements, each with an asserted count, logged to harmonise-log.tsv (file, block id, old, new, reason). Do not rebuild chapters from their builders.
3. Find divergences in code: for every Pāli sentence or clause that occurs in more than one place (split each Pāli line and its Vietnamese line on sentence ends, compare), list Vietnamese variants (find_divergences_vi.py → divergences.md). Identical Pāli must give identical Vietnamese across all chapters; pick the sample's or the majority form and justify it.
4. Settle the named points:
   - Uddāna / closing verses (ch3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15): same Pāli words get the same Vietnamese across verses (gocchaka, pada, antara, tato upari «tiếp theo đó» ch10 vs «từ đó trở đi» ch13, viññāṇadhātu, padassa niddese, -ti dropping, capitalisation, whether a word may move to the next verse line).
   - TRANSLATE AS WRITTEN (user rule): remove added words. ch4 verse «ba sự thật cũng vậy»: «ba» is not in the Pāli (tathā saccā). ch13 verse «Bốn khối ngoài khối vật chất» for "Rūpakkhandhā cattāro" adds «ngoài khối vật chất»: render the Pāli words as written and list it for the user.
   - "Xehi dhammehi ye dhammā" (plural instrumental heads): ch3/ch6 «đối với các hiện tượng <pred>, những hiện tượng nào» vs ch4/ch12 «các hiện tượng <pred>» inside a chain. One form.
   - Pronoun after an association verb: «nó» / «chúng» follows the last chain member (ch10, 11, 13, 15); check ch8 and ch9 follow the same rule.
   - ch7 inserts «thì» before the predicate when the subject ends in «gắn liền với X» (8 lines): apply the same everywhere the same shape occurs, or remove it everywhere; one rule.
   - na kehici … vippayuttā «… mà chúng không gắn liền với, nhưng …» (ch7, ch8): consistent across chapters; check whether the final «với» reads correctly.
   - ^3-487 «ye vippayuttā» without dhammā rendered «những gì»: keep or make «những hiện tượng nào» (as written: no dhammā; decide and report).
   - Kehici clause wording, «Không có.», «Không gắn liền với bao nhiêu?», khandha-only answers: one form each.
   - Variant brackets: same labels for the same kind of variant ([khác chính tả …] vs [dị bản …]); (bahūsu) «(nhiều bản)».
   - Dependent-origination links in the instrumental (avijjāpaccayā saṅkhārena / saṅkhārehi): same quoted pi-2 string everywhere.
5. Do not change counts or Pāli slips that were translated as written. Do not change what pi-1 / pi-2 strings say.

## Verify (all must pass)
For every chapter: check_chapter_ids.py OK, dashcheck.py 0 mismatches, pi-1-vi-ai\verify_rails_vi.py OK (commands in vi-zeroshot-brief.md). Re-run find_divergences_vi.py after the changes: remaining divergences listed with reasons in harmonise-notes.md. No «—», «–», «:-», «….», «là là», «được được», «chánh niệm».

## Report (under 400 words, as text)
- Lines changed per chapter; checks.
- Each named point: the form chosen and why.
- Points for the user (as-written removals, ^3-487, anything you could not settle).
