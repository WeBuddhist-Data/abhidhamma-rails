# Brief: align the pi-4 Vietnamese termbase to the approved review fixes

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools (scripts with the Write tool at full paths under D:\Work\OpenPecha\abhidhamma-rails), PowerShell for commands, `python -I -X utf8`. Write ONLY 0-INBOX\temp\pipeline\pi-4-vi-ai\termbase\decisions-review.tsv (and helper scripts in termbase\). The assembler writes AI_translation\vietnamese\pi-4-pali-vietnamese-termbase-plain.md and termbase\termbase-decisions.md; that is expected. Do not edit decisions.tsv, decisions-user.tsv, any translation file, 1-SOURCES\ or 4-SYSTEM\; never run git; never write "seed". No web. Never open 1-SOURCES\Translations\Vietnamese\, 0-INBOX\raw-data\vi-*, the alignment folders (pi-*-vi\, pi-1-th-vi\, vi-tools\) or the pi-4 Vietnamese zero-shot. Grep only named files. Return the report as text.

## Context
The user approved the pi-4 review fixes on 2026-11-21 ("Approve, then merge") and the alignment of the termbase to them, as was done for pi-2 (model: 0-INBOX\temp\pipeline\pi-2-vi-ai\termbase\decisions-review.tsv and agents-run.md "Termbase aligned to the review"). The fixes are logged in 0-INBOX\temp\pipeline\pi-4-vi-ai\rails\review-fixes-log.tsv and described in rails\review-fixes-notes.md and 0-INBOX\temp\pipeline\pi-4-vi-ai\vi-review-fixes-brief.md (decisions 1-11).

## Task
1. Run termbase adherence on the fixed rails to list the misses:
   `python -I -X utf8 0-INBOX\temp\pipeline\termbase_adherence_vi.py AI_translation\pali\pi-4-keywords-by-reference-pali-plain.md AI_translation\vietnamese\pi-4-pali-vietnamese-termbase-plain.md AI_translation\vietnamese\pi-4-vietnamese-plain-rails_split_chapters` (140 misses now; 98 before the fixes).
2. For each miss that comes from a review decision (the agent named: arūpa, dhammā «Giáo Pháp», anuseti, uddhaṃsoto, vihāya, avakkanti, buddhānaṃ, purisapuggalo, pāpa- / kalyāṇamitto, the ^4-170 pheggu / sāra entries, dhamma ^4-172, gāmino; check them all), write a line in termbase\decisions-review.tsv: `hw|sense_index<TAB>new term<TAB>reason (review decision N, ^ids)`, in citation form. Use `python -I -X utf8 0-INBOX\temp\pipeline\pi-4-vi-ai\termbase\tb_tool_vi.py fam <regex>` to find the sense index. Only change a sense whose ALL uses in the text now take the new wording; if a headword's sense is used both in the old and the new way (shared senses), do NOT change it and list it under "Not set".
3. If a headword|sense already has a line in decisions.tsv or decisions-user.tsv, the assembler reports a duplicate: then list it under "Needs a decision.tsv edit" in your report instead of writing it (the coordinator handles it).
4. Re-assemble: `python -I -X utf8 0-INBOX\temp\pipeline\termbase_assemble.py 4 vietnamese vi-ai plain` must print "no errors"; then re-run the adherence check and report the new miss count.

## Report (under 300 words, as text)
Lines written, aligned / outside counts, adherence before / after, the "Not set" list with reasons, any "Needs a decision.tsv edit" items.
