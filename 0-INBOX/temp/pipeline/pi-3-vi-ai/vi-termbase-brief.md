# Brief: termbase-builder, Pāli→Vietnamese plain, pi-3 (Dhātukathā)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at full paths; never write any file from PowerShell), PowerShell for commands, `python -I -X utf8`. Write ONLY in 0-INBOX\temp\pipeline\pi-3-vi-ai\termbase\. Do not touch 1-SOURCES\, 4-SYSTEM\ or AI_translation\ (the assembler writes there, not you), do not edit any pi-1 / pi-2 file, never create files at the repo root or in a system temp folder, never run git (not even git status). Never use the words "seed" or "unseeded" anywhere. No web. You cannot write report files for me: return your report as text.

The user approves the termbase explicitly afterwards; your job is a clean, consistent proposal plus the list of points the user must decide.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\: Grep only the specific files named here. Our terms must be our own.

## Read first
- AI_translation\skills\termbase-builder.md. Follow it.
- 0-INBOX\temp\pipeline\pi-2-vi-ai\vi-termbase-brief.md and 0-INBOX\temp\pipeline\pi-1-vi-ai\vi-termbase-brief.md (their rules apply here with "pi-3" for "pi-2"; in particular the CITATION FORM rule and the distinct pairs). Also 0-INBOX\temp\pipeline\hindi-termbase-brief.md, section "How to choose".
- The user's termbase decisions (binding wherever pi-3 has the same Pāli word in the same meaning): 0-INBOX\temp\pipeline\pi-1-vi-ai\termbase\APPROVED.md and 0-INBOX\temp\pipeline\pi-2-vi-ai\termbase\APPROVED.md (pi-2's says cross-book terms follow pi-1), plus pi-2-vi-ai\termbase\decisions-user.tsv and decisions-review.tsv (the pi-2 review changes the user approved).
- AI_translation\audience_profile\plain.md; 0-INBOX\temp\pipeline\vietnamese-style.md (core terms, distinct pairs; sati = «sự tỉnh thức», never «chánh niệm»).
- The pi-3 decisions the user approved: 0-INBOX\temp\pipeline\pi-3-vi-ai\vi-zeroshot-terms.md, harmonise-notes.md, mapper-vi\vi-map-conventions-pi3.md, senses\senses-conventions.md; and pi-3-vi-ai\agents-run.md (search it for "FOR THE REVIEW", "HARMONISE", "User").
- How the Russian run settled pi-3 (meaning only): AI_translation\russian\pi-3-pali-russian-termbase-plain.md (grep, don't read whole).

## Input, output, tools
- Input: AI_translation\vietnamese\pi-3-pali-word-vietnamese-senses-plain.md (661 headwords, 669 senses; about 17 senses have 2+ candidates). Line N = headword N.
- Your decisions: 0-INBOX\temp\pipeline\pi-3-vi-ai\termbase\decisions.tsv, one line each: `hw|sense_index<TAB>term<TAB>short reason` (sense_index 0-based). Start the file with a `#` comment line stating the citation-form rule.
- Helper: `python -I -X utf8 0-INBOX\temp\pipeline\pi-3-vi-ai\termbase\tb_tool_vi.py` (READ-ONLY; call it; read its docstring): `list <from> <to> [--multi]`, `fam <regex>`, `prior <regex>` (pi-1 AND pi-2 termbases), `hcount <vietnamese> …` (in the merged pi-3 zero-shot), `crossbook` (30 senses differ from every pi-1 / pi-2 term before your decisions), `check <from> <to>` (must print "no errors" for 1 661).
- Then run the assembler yourself: `python -I -X utf8 0-INBOX\temp\pipeline\termbase_assemble.py 3 vietnamese vi-ai plain` must print "no errors" (it writes AI_translation\vietnamese\pi-3-pali-vietnamese-termbase-plain.md and termbase\termbase-decisions.md; that is expected).

## Vietnamese pi-3 specifics
1. **Order of preference for multi-candidate senses:** (a) a core term in vietnamese-style.md, a user decision (pi-1 / pi-2 APPROVED.md, the pi-3 decisions above) or the pi-3 term list; (b) the approved pi-2, then pi-1 Vietnamese termbase term for the same Pāli word in the same meaning, when it is among the candidates; (c) the form the pi-3 translation uses most (hcount); (d) the clearest plain-Vietnamese candidate. Citation form as the pi-1 / pi-2 rule (nouns with their nominaliser as used alone; stems, compound members, adjectives and predicates bare; tense words only where the tense is the point; «có» / «điều» dropped unless part of the meaning; the unbroken form over a gapped « … » form).
2. **Family alignment** on single-candidate senses only where the same Pāli lemma in the same meaning drifted to a different Vietnamese word. Approved sense splits stay split.
3. **Cross-book differences: report, do not force.** Run `crossbook`. Where pi-3's term differs from the approved pi-1 / pi-2 term for the same Pāli word AND the same meaning, keep pi-3's unless the prior term is among the candidates (then 1b applies), and list it under "Cross-book differences" (pali | sense | pi-3 term | prior term). Many of the 30 are different senses (verse words such as pare, antare, vidhā; reference words in another case): say so briefly. The user decides real ones.
4. **User decisions on pi-3 so far (binding):** book title «Thảo luận về các yếu tố»; chapter headings «Phương pháp thứ nhất … thứ mười bốn», Uddeso «Phần nêu đề mục»; padaniddeso «Giải thích đề mục về …»; saṅgahita «được gộp vào», sampayutta «gắn liền với», sabhāga / visabhāga «cùng loại / khác loại»; the shared frames (vi-zeroshot-brief.md SHARED FRAMES); the senses sample (upekkhā, saññā, hetukā one sense each; ādi «mục khác» / «bắt đầu bằng»; arūpa «không hình sắc» / «phi vật chất»).
5. **Keep distinct Pāli terms distinct** where the text puts them side by side (check with `fam`, `hcount`): the pi-1 / pi-2 pairs, and in pi-3 sukha «hạnh phúc» (jhāna) vs «dễ chịu» (feeling); dukkha «khổ đau» vs «khó chịu»; rūpa «vật chất» vs «hình sắc».
6. **Points for the user (report; don't change the translation):** anything in agents-run.md marked FOR THE REVIEW that touches a term (e.g. samucchede «sự phân tách», the verse words, kāma / āyatana keyword at 3-227 / 3-455), and any sense where the attested form would mislead a plain reader.
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
