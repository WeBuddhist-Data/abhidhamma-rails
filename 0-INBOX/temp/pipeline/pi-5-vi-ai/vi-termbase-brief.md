# Brief: termbase-builder, Pāli→Vietnamese plain, pi-5 (Kathāvatthu)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at full paths under D:\Work\OpenPecha\abhidhamma-rails; never write any file from PowerShell), PowerShell for commands, `python -I -X utf8 -B`. Write ONLY in 0-INBOX\temp\pipeline\pi-5-vi-ai\termbase\, with LF line endings. Do not touch 1-SOURCES\, 4-SYSTEM\ or AI_translation\ (the assembler writes there, not you), do not edit any pi-1 … pi-4 file, never create files at the repo root, outside the repo or in a system temp folder, never run git (not even git status). Never use the words "seed" or "unseeded" anywhere. No web. You cannot write report files for me: return your report as text.

The user approves the termbase explicitly afterwards; your job is a clean, consistent proposal plus the list of points the user must decide.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\: Grep only the specific files named here. Our terms must be our own.

## Read first
- AI_translation\skills\termbase-builder.md. Follow it.
- 0-INBOX\temp\pipeline\pi-4-vi-ai\vi-termbase-brief.md, pi-3-vi-ai\vi-termbase-brief.md, pi-2-vi-ai\vi-termbase-brief.md and pi-1-vi-ai\vi-termbase-brief.md (their rules apply here with "pi-5" for the book; in particular the CITATION FORM rule and the distinct pairs). Also 0-INBOX\temp\pipeline\hindi-termbase-brief.md, section "How to choose".
- The user's termbase decisions (binding wherever pi-5 has the same Pāli word in the same meaning): 0-INBOX\temp\pipeline\pi-1-vi-ai\termbase\APPROVED.md … pi-4-vi-ai\termbase\APPROVED.md (cross-book terms follow pi-1), plus the decisions-user.tsv / decisions-review.tsv files in pi-2-vi-ai\termbase\, pi-3-vi-ai\termbase\ and pi-4-vi-ai\termbase\.
- AI_translation\audience_profile\plain.md; 0-INBOX\temp\pipeline\vietnamese-style.md (core terms, distinct pairs; sati = «sự tỉnh thức», never «chánh niệm»).
- The pi-5 decisions the user approved: 0-INBOX\temp\pipeline\pi-5-vi-ai\vi-zeroshot-terms.md, coordinator-rules.md, harmonise-notes.md, mapper-vi\vi-map-conventions-pi5.md, mapper-vi\map-coordinator-rules.md, senses\senses-conventions.md; and pi-5-vi-ai\agents-run.md (search it for "For the user", "termbase", "Clash", "For review", "User").
- How the Russian run settled pi-5 (meaning only): AI_translation\russian\pi-5-pali-russian-termbase-plain.md (grep, don't read whole).

## Input, output, tools
- Input: AI_translation\vietnamese\pi-5-pali-word-vietnamese-senses-plain.md (5,443 headwords, 5,615 senses; 354 senses have 2+ candidates). Line N = headword N.
- Your decisions: 0-INBOX\temp\pipeline\pi-5-vi-ai\termbase\decisions.tsv, one line each: `hw|sense_index<TAB>term<TAB>short reason` (sense_index 0-based). Start the file with a `#` comment line stating the citation-form rule.
- Helper: `python -I -X utf8 -B 0-INBOX\temp\pipeline\pi-5-vi-ai\termbase\tb_tool_vi.py` (READ-ONLY; call it; read its docstring): `list <from> <to> [--multi]`, `fam <regex>`, `prior <regex>` (pi-1 … pi-4 termbases), `hcount <vietnamese> …` (in the merged pi-5 zero-shot), `crossbook` (475 senses differ from every pi-1 … pi-4 term before your decisions; many are different senses or citation-form variants), `check <from> <to>` (must print "no errors" for 1 5443).
- Then run the assembler yourself: `python -I -X utf8 -B 0-INBOX\temp\pipeline\termbase_assemble.py 5 vietnamese vi-ai plain` must print "no errors" (it writes AI_translation\vietnamese\pi-5-pali-vietnamese-termbase-plain.md and termbase\termbase-decisions.md; that is expected).

## Vietnamese pi-5 specifics
1. **Order of preference for multi-candidate senses:** (a) a core term in vietnamese-style.md, a user decision (pi-1 … pi-4 APPROVED.md, the pi-5 decisions above) or the pi-5 term list; (b) the approved pi-4, pi-3, pi-2, then pi-1 Vietnamese termbase term for the same Pāli word in the same meaning, when it is among the candidates; (c) the form the pi-5 translation uses most (hcount); (d) the clearest plain-Vietnamese candidate. Citation form as the pi-1 … pi-4 rule (nouns with their nominaliser as used alone; stems, compound members, adjectives and predicates bare; tense words only where the tense is the point; «có» / «điều» / «khi» dropped unless part of the meaning; person names with their head noun «người» / «bậc» as approved; the unbroken form over a gapped « … » form).
2. **Family alignment** on single-candidate senses only where the same Pāli lemma in the same meaning drifted to a different Vietnamese word. Approved sense splits stay split.
3. **Cross-book differences: report, do not force.** Run `crossbook`. Where pi-5's term differs from the approved pi-1 … pi-4 term for the same Pāli word AND the same meaning, keep pi-5's unless the prior term is among the candidates (then 1b applies), and list it under "Cross-book differences" (pali | sense | pi-5 term | prior term), real ones first. Group the rest (different senses, citation-form variants) briefly. The user decides real ones (pi-2 rule: cross-book terms follow pi-1).
4. **User decisions on pi-5 so far (binding):** book title «Các vấn đề tranh luận»; saccikaṭṭha «thực tại chân thật», paramattha «thực tại tối hậu», upalabbhati «được tìm thấy», sakavādī «người theo học thuyết của chúng ta», paravādī «người theo học thuyết khác»; atthi «tồn tại» in the theses; the debate formulas (vi-zeroshot-terms.md); kathā «Bàn về …»; the harmonise decisions (harmonise-notes.md); the map and senses samples (incl. the micchā / vata / niggaha / atthi / rūpa / kathā / buddho / pathavī splits).
5. **Keep distinct Pāli terms distinct** where the text puts them side by side: the pi-1 … pi-4 pairs; in pi-5 niggaha «sự bác bỏ» vs paṭikamma «sự phản bác»; niggaha «sự bác bỏ» (debate) vs «sự chế ngự» (mind); micchā «sai» (verdict) vs «sai lầm» (path factor); atthi «tồn tại» vs upalabbhati «được tìm thấy»; viparīta «điều sai lệch» vs vipariyesa «sự đảo ngược»; samāpajjanta vs samāpanna; sukha «hạnh phúc» / «dễ chịu»; dukkha «khổ đau» / «khó chịu».
6. **Points for the user (report; don't change the translation; give your proposal for each):** the list "For the user" in harmonise-notes.md and agents-run.md, in particular: kāyika / cetasika dukkha and sukha / dukkha as feelings (ch10, ch14 ^5-452, ch17, ch25 uddāna: «khổ đau» / «hạnh phúc» vs pi-1 «khó chịu» / «dễ chịu»); the paccaya names (hetu «nguyên nhân» vs pi-1 «gốc rễ», adhipati «chi phối» vs pi-1 «yếu tố chủ đạo», samanantara, āsevanā); saṃvara «sự phòng hộ» vs pi-1 indriyasaṃvara «sự thu thúc»; niyata vs pi-4 «có hướng đi cố định»; «một bậc A-la-hán»; dhammataṇhā; upaṭṭhāka vs pi-4 «người chăm sóc»; tiṭṭhati «tồn tại» vs atthi; «Tóm tắt của chương này –»; atta «cá nhân»; the names Seniya, Soma, Yama, Subhadda (proposed Vietnamese forms in harmonise-notes.md); pariyāpanna «nằm trong» and «yếu tố âm thanh» (harmonise beyond the list); any sense where the attested form would mislead a plain reader.
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
