# Brief: termbase-builder, Pāli→Vietnamese plain, pi-4 (Puggalapaññatti)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at full paths under D:\Work\OpenPecha\abhidhamma-rails; never write any file from PowerShell), PowerShell for commands, `python -I -X utf8`. Write ONLY in 0-INBOX\temp\pipeline\pi-4-vi-ai\termbase\. Do not touch 1-SOURCES\, 4-SYSTEM\ or AI_translation\ (the assembler writes there, not you), do not edit any pi-1 / pi-2 / pi-3 file, never create files at the repo root, outside the repo or in a system temp folder, never run git (not even git status). Never use the words "seed" or "unseeded" anywhere. No web. You cannot write report files for me: return your report as text.

The user approves the termbase explicitly afterwards; your job is a clean, consistent proposal plus the list of points the user must decide.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\: Grep only the specific files named here. Our terms must be our own.

## Read first
- AI_translation\skills\termbase-builder.md. Follow it.
- 0-INBOX\temp\pipeline\pi-3-vi-ai\vi-termbase-brief.md, pi-2-vi-ai\vi-termbase-brief.md and pi-1-vi-ai\vi-termbase-brief.md (their rules apply here with "pi-4" for the book; in particular the CITATION FORM rule and the distinct pairs). Also 0-INBOX\temp\pipeline\hindi-termbase-brief.md, section "How to choose".
- The user's termbase decisions (binding wherever pi-4 has the same Pāli word in the same meaning): 0-INBOX\temp\pipeline\pi-1-vi-ai\termbase\APPROVED.md, pi-2-vi-ai\termbase\APPROVED.md (cross-book terms follow pi-1), pi-3-vi-ai\termbase\APPROVED.md, plus pi-2-vi-ai\termbase\decisions-user.tsv / decisions-review.tsv and pi-3-vi-ai\termbase\decisions-user.tsv.
- AI_translation\audience_profile\plain.md; 0-INBOX\temp\pipeline\vietnamese-style.md (core terms, distinct pairs; sati = «sự tỉnh thức», never «chánh niệm»).
- The pi-4 decisions the user approved: 0-INBOX\temp\pipeline\pi-4-vi-ai\vi-zeroshot-terms.md, harmonise-notes.md, mapper-vi\vi-map-conventions-pi4.md, senses\senses-conventions.md; and pi-4-vi-ai\agents-run.md (search it for "FOR THE REVIEW", "HARMONISE", "User").
- How the Russian run settled pi-4 (meaning only): AI_translation\russian\pi-4-pali-russian-termbase-plain.md (grep, don't read whole).

## Input, output, tools
- Input: AI_translation\vietnamese\pi-4-pali-word-vietnamese-senses-plain.md (2,147 headwords, 2,221 senses; about 100 senses have 2+ candidates). Line N = headword N.
- Your decisions: 0-INBOX\temp\pipeline\pi-4-vi-ai\termbase\decisions.tsv, one line each: `hw|sense_index<TAB>term<TAB>short reason` (sense_index 0-based). Start the file with a `#` comment line stating the citation-form rule.
- Helper: `python -I -X utf8 0-INBOX\temp\pipeline\pi-4-vi-ai\termbase\tb_tool_vi.py` (READ-ONLY; call it; read its docstring): `list <from> <to> [--multi]`, `fam <regex>`, `prior <regex>` (pi-1, pi-2 AND pi-3 termbases), `hcount <vietnamese> …` (in the merged pi-4 zero-shot), `crossbook` (202 senses differ from every pi-1 / pi-2 / pi-3 term before your decisions; many are different senses or citation-form variants), `check <from> <to>` (must print "no errors" for 1 2147).
- Then run the assembler yourself: `python -I -X utf8 0-INBOX\temp\pipeline\termbase_assemble.py 4 vietnamese vi-ai plain` must print "no errors" (it writes AI_translation\vietnamese\pi-4-pali-vietnamese-termbase-plain.md and termbase\termbase-decisions.md; that is expected).

## Vietnamese pi-4 specifics
1. **Order of preference for multi-candidate senses:** (a) a core term in vietnamese-style.md, a user decision (pi-1 / pi-2 / pi-3 APPROVED.md, the pi-4 decisions above) or the pi-4 term list; (b) the approved pi-3, pi-2, then pi-1 Vietnamese termbase term for the same Pāli word in the same meaning, when it is among the candidates; (c) the form the pi-4 translation uses most (hcount); (d) the clearest plain-Vietnamese candidate. Citation form as the pi-1 / pi-2 / pi-3 rule (nouns with their nominaliser as used alone; stems, compound members, adjectives and predicates bare; tense words only where the tense is the point; «có» / «điều» dropped unless part of the meaning; person names with their head noun «người» / «bậc» as approved; the unbroken form over a gapped « … » form).
2. **Family alignment** on single-candidate senses only where the same Pāli lemma in the same meaning drifted to a different Vietnamese word. Approved sense splits stay split.
3. **Cross-book differences: report, do not force.** Run `crossbook`. Where pi-4's term differs from the approved pi-1 / pi-2 / pi-3 term for the same Pāli word AND the same meaning, keep pi-4's unless the prior term is among the candidates (then 1b applies), and list it under "Cross-book differences" (pali | sense | pi-4 term | prior term), real ones first. Group the rest (different senses, citation-form variants) briefly. The user decides real ones (pi-2 rule: cross-book terms follow pi-1).
4. **User decisions on pi-4 so far (binding):** book title «Định danh các hạng người»; paññatti «sự định danh»; puggala «người» / «hạng người» (counted); the person-type names of the matrix (pi-4-vi-ai\build_sample_vi.py NAME) and the definition frame «Thế nào là X? Ở đời này, có người … – người này được gọi là “X”.»; chapter headings «Định danh các hạng người theo nhóm N»; harmonise decisions (Kathañca «Người như thế nào là X?»; samannāgata «được trang bị» for qualities / «mang» for bad states; «vị ấy» for monks / «người ấy» for others; abhininnāmeti «dẫn tâm»); the map and senses samples (incl. the puggalā / viharati / hoti / dhamma / rūpa / ṭhita / ekaka… splits).
5. **Keep distinct Pāli terms distinct** where the text puts them side by side: the pi-1 / pi-2 / pi-3 pairs; in pi-4 vitakka «sự hướng tâm» vs abhininnāmeti «dẫn tâm»; hāyati «suy giảm» vs parihāyati «sa sút»; sukha «hạnh phúc» / «dễ chịu»; dukkha «khổ đau» / «khó chịu»; viharati «sống» / «an trú».
6. **Points for the user (report; don't change the translation):** ^4-176 narassa (as written «của một người»; the aṭṭhakathā reads nagarassa «thành phố»); anything in agents-run.md marked FOR THE REVIEW that touches a term; any sense where the attested form would mislead a plain reader.
7. **Term form:** no ", ", " / ", "; " inside a term; no em or en dash. Gapped values with " … " only as attested.
8. **Outside terms:** only when every candidate is wrong for a plain reader; give the reason. These need the user's approval.

## Report (under 450 words, as text)
- The `check` and assembler output lines.
- Number of multi-candidate decisions and of family re-alignments.
- Outside-candidate choices with reasons.
- The 15 most consequential choices.
- Cross-book differences (rule 3), real ones first.
- Points for the user, each with your proposal.
- Anything you are unsure of.
