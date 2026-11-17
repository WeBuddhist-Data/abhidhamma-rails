# Brief: apply the approved review fixes, pi-2 Russian rails (Vibhaṅga)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any pi-1 file or any builder (build_rails_*_ru.py), do not run git, never write "seed", never create files at the repo root. You cannot write report files for me: return your report as text.

## What to apply
The user approved ("Apply all", 2026-11-17) every row marked **APPLY** in 0-INBOX\temp\pipeline\pi-2-ru\review\findings-r1.md … findings-r6.md, plus the two **ASK** rows decided as recommended:
- r3: kusalo dhammacchando = «благое желание как явление» (all 7 places in ch. 8 and 9; keep the rest of each string).
- r4: brahmacakkaṃ = «высшее колесо» (all 12 places in ch. 16, inflected: «приводит в движение высшее колесо»).
The r3 padhāna / vāyāma row stays as it is. Rows marked REJECT stay as they are. The termbase was already updated (termbase\APPROVED.md, decisions-review.tsv); do not touch it.

## How
1. Copy the 19 files of AI_translation\russian\pi-2-russian-plain-rails_split_chapters\ to 0-INBOX\temp\pipeline\pi-2-ru\review\backup-pre-fixes\ first.
2. Write 0-INBOX\temp\pipeline\pi-2-ru\review\apply_review_fixes_ru.py: exact string replacements per file (old → new, each with its expected count, asserting the count), applied to the chapter files, idempotent when re-run on the backup copy, logging every changed line to review\fixes-log.tsv (file, line, finding, before, after).
3. Read each finding's segment in Pāli and Russian before writing its replacement. Book-wide rows («….» → «…» at a sentence end; «неповреждённа» → «неповреждена») apply wherever they occur; for the others, check the whole book for the same string (identical Pāli must keep identical Russian) and apply it everywhere it belongs.
4. Specific notes:
   - r4 ch. 15 (2-725 … 2-745, 21 segments): replace the broken «Каким выражением обозначаются эти явления, при этом знание высказывания выражений …» with one grammatical sentence that keeps every term (выражение, обозначаться, знание, высказывание, выражения, относящиеся к явлениям, аналитическое знание выражений), the same string in all 21 places; mind 2-725 where it runs on after a comma. No new dash.
   - r3 2-465: make the quoted feminine items agree the way the book does elsewhere for feminine singular subjects (look at ch. 2–3 and ch. 7–9 for the pattern) and say which form you used.
   - r5 2-854 giddhikatā: check AI_translation\russian\pi-2-pali-russian-termbase-plain.md; if giddhikatā/giddhikattaṃ has a termbase term, keep it and report; otherwise apply «жадное стремление, состояние жадного стремления».
   - r5 2-948: no dash (the Pāli has none).
   - r6 2-1029 line 1: end with «.», line 2 becomes its own sentence; keep the line count and dashes.
5. The DASH RULE holds: "–" only where the Pāli has it, same count per line. Never change a block ID, a line count or a variant bracket.
6. Write review\builders-stale.md: the builders no longer reproduce the chapter files; the run order to rebuild is builder → apply_review_fixes_ru.py (on a refreshed backup).

## Verify (all must pass, for all 19 files)
```
python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-2_split_chapters AI_translation\russian\pi-2-russian-plain-rails_split_chapters <ch>.md
python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py AI_translation\pali\pi-2_split_chapters\<ch>.md AI_translation\russian\pi-2-russian-plain-rails_split_chapters\<ch>.md
python -I -X utf8 0-INBOX\temp\pipeline\pi-2-ru\rails\extra_checks.py <pali> <russian> …
python -I -X utf8 0-INBOX\temp\pipeline\pi-2-ru\rails\find_divergences_rails_ru.py
```
find_divergences must still print "diverging: 0". Also confirm: no «колесо Брахмы», no «стремление к Учению», no «Каким выражением … при этом», no «кристалл», no «сопли», no «неповреждённа», no «….».

## Report (short, as text)
Number of lines changed per finding (from fixes-log.tsv), the exact new strings for the ch. 15 sentence, 2-465, 2-948 and 2-1029, the giddhikatā outcome, and the verification output.
