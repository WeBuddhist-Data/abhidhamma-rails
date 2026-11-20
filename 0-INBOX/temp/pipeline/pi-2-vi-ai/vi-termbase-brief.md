# Brief: termbase-builder, Pāli→Vietnamese plain, pi-2 (Vibhaṅga)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at full paths; never write any file from PowerShell), PowerShell for commands, `python -I -X utf8`. Write ONLY in 0-INBOX\temp\pipeline\pi-2-vi-ai\termbase\. Do not touch 1-SOURCES\, 4-SYSTEM\ or AI_translation\ (the assembler writes there, not you), do not edit any pi-1 file, never create files at the repo root or in a system temp folder, never run git (not even git status). Never use the words "seed" or "unseeded" anywhere. You cannot write report files for me: return your report as text.

The user approves the termbase explicitly afterwards; your job is a clean, consistent proposal plus the list of points the user must decide.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\. No web lookups of Vietnamese Abhidhamma translations. Our terms must be our own.

## Read first
- AI_translation\skills\termbase-builder.md. Follow it.
- 0-INBOX\temp\pipeline\pi-1-vi-ai\vi-termbase-brief.md (the pi-1 Vietnamese brief: its rules 1–7 apply here with "pi-2" for "pi-1", in particular the CITATION FORM rule 2 and the distinct pairs of rule 4); this brief adds what is specific to pi-2. Also 0-INBOX\temp\pipeline\hindi-termbase-brief.md, section "How to choose".
- 0-INBOX\temp\pipeline\pi-1-vi-ai\termbase\APPROVED.md: the user's pi-1 termbase decisions (binding wherever pi-2 has the same Pāli word in the same meaning), and 0-INBOX\temp\pipeline\pi-1-vi-ai\termbase\termbase-decisions.md (how pi-1 chose).
- AI_translation\audience_profile\plain.md (no Buddhist background; understanding first).
- 0-INBOX\temp\pipeline\vietnamese-style.md (core terms and the pairs that must stay distinct; binding; sati = «sự tỉnh thức», never «chánh niệm»).
- The pi-2 decisions the user approved: 0-INBOX\temp\pipeline\pi-2-vi-ai\vi-zeroshot-terms.md, harmonise-notes.md, mapper-vi\vi-map-conventions-pi2.md, senses\senses-conventions.md; and pi-2-vi-ai\agents-run.md (search it for "FOR THE REVIEW", "FOR THE HARMONISE PASS", "User").
- How the Russian run settled the same pi-2 senses (meaning only, not wording): AI_translation\russian\pi-2-pali-russian-termbase-plain.md and 0-INBOX\temp\pipeline\pi-2-ru\termbase\termbase-decisions.md, APPROVED.md (grep, don't read whole).

## Input, output, tools
- Input: AI_translation\vietnamese\pi-2-pali-word-vietnamese-senses-plain.md (4,971 headwords, 5,121 senses; 177 senses have 2+ candidates). Line N = headword N.
- Your decisions: 0-INBOX\temp\pipeline\pi-2-vi-ai\termbase\decisions.tsv, one line each: `hw|sense_index<TAB>term<TAB>short reason` (sense_index 0-based within the senses line). Start the file with a `#` comment line stating the citation-form rule.
- Helper: `python -I -X utf8 0-INBOX\temp\pipeline\pi-2-vi-ai\termbase\tb_tool_vi.py` (READ-ONLY; call it, don't edit it; read its docstring):
  - `list <from> <to> [--multi]`: senses with candidate counts from the pi-2 map, decisions so far, and the same headword's terms in the approved pi-1 Vietnamese termbase ("prior").
  - `fam <regex>`: a whole lemma family across pi-2.
  - `prior <regex>`: a family in the pi-1 Vietnamese termbase.
  - `hcount <vietnamese> …`: occurrences in the merged pi-2 Vietnamese zero-shot.
  - `crossbook`: senses whose pi-2 term differs from every pi-1 term of the same headword (163 before your decisions; most are different senses or different forms, see rule 3).
  - `check <from> <to>`: every multi-candidate sense decided, no forbidden characters, outside choices listed. Must print "no errors" for 1 4971.
- Then run the assembler yourself to confirm: `python -I -X utf8 0-INBOX\temp\pipeline\termbase_assemble.py 2 vietnamese vi-ai plain` must print "no errors" (it writes AI_translation\vietnamese\pi-2-pali-vietnamese-termbase-plain.md and termbase\termbase-decisions.md; that is expected).

## Vietnamese pi-2 specifics
1. **Order of preference for multi-candidate senses:** (a) a core term in vietnamese-style.md, a user decision (pi-1 APPROVED.md, the pi-2 decisions above) or the pi-2 term list; (b) the approved pi-1 Vietnamese termbase term for the same Pāli word in the same meaning, when it is among the candidates (pi-2 repeats many pi-1 passages word for word); (c) the form the pi-2 translation uses most (map counts / hcount); (d) the clearest plain-Vietnamese candidate. Citation form as pi-1 rule 2 (noun headwords with their nominaliser as used alone; stems, compound members and adjectives bare; tense words only where the tense is the point; classifiers «loại» / «bậc» / «vị» and «có» dropped unless part of the meaning; the unbroken form over a gapped « … » form).
2. **Family alignment** (decisions on single-candidate senses) only where the same Pāli lemma in the same meaning drifted to a different Vietnamese word. Variants inside one sense are not drift: choose the citation form. The approved sense splits stay split.
3. **Cross-book differences: report, do not force.** Run `crossbook`. Where pi-2's term differs from the approved pi-1 term for the same Pāli word AND the same meaning (not a different sense, not only a citation-form difference), keep the pi-2 term unless the pi-1 term is among the candidates (then 1b applies), and list the case under "Cross-book differences" (pali | sense | pi-2 term | pi-1 term). Known ones from the map and senses: cuti «sự lìa khỏi» (pi-1 «sự chết»); santuṭṭhitā «sự biết đủ»; paṭigha «sự va chạm»; dussanā «sự khởi sân»; the jātā string of ch12; the god names pi-1 lacks. The user decides those.
4. **User decisions on pi-2 so far (binding):** book title «Phân tích các hiện tượng»; section headings «Phân tích theo kinh / theo Vi Diệu Pháp / Phần hỏi đáp»; rajataṃ «đồng tiền» (coin) vs sajjha «bạc»; vatthu «chỗ dựa» (āghātavatthu included); Catukkaṃ / Pañcakaṃ two forms (jhāna method «phương pháp chia bốn / năm» vs classification «phân loại theo nhóm bốn / năm»); counted questions «… là những gì?»; N-vidhena «theo nhóm N»; the nāma/rūpa pair «phần tinh thần / phần vật chất»; the senses sample splits (Jāti «sự sinh» / «xuất thân»; Duka / Tika «bộ đôi / bộ ba» vs «phân loại theo nhóm hai / ba»; āhāro «dưỡng chất» / «thức ăn»; Dhātu «yếu tố» / «cõi»).
5. **Keep distinct Pāli terms distinct** where the text puts them side by side (check with `fam`, `hcount` and the segments). The pi-1 pairs (vīriya «tinh tấn» vs padhāna / vāyāma «nỗ lực»; vicikicchā vs kaṅkhā; kukkucca vs uddhacca; cetanā vs sañcetanā; parāmāsa vs abhinivesa vs diṭṭhigata; sammappadhāna = sammāvāyāma), plus pi-2's: kāmadhātu «yếu tố dục lạc» (element) vs «cõi dục lạc» (plane); vossagga «sự buông xả» (ch10) vs «sự buông lơi» (pamāda list, ch17); viharati «sống» vs «an trú»; hetu «gốc rễ» vs «nguyên nhân»; pasāda «chất nhạy cảm» vs «lòng tin trong sáng»; mada «sự say sưa» vs māna «sự kiêu mạn» / atimāna «sự ngạo mạn» / omāna «sự tự ti»; veramaṇī vs virati in the abstention lists (check what the text has); sukha «hạnh phúc» / «dễ chịu» / «dễ dàng» / «thú vui».
6. **Points for the user (report the termbase term; don't change the translation):** ^2-511 mokkhaṃ «sự giải thoát» (likely 'chief', as the Russian reads it); ^2-220 ṭhiti (the life string reads «sự tồn tại», the map gives «sự ổn định»); ^2-1023 koṭi «triệu» (crores converted to millions); cetasikaṃ sukhaṃ «sự dễ chịu trong tâm» under a "mental happiness" tag; arahato / arahanto «bậc A-la-hán» one sense; paṭibhāna «tài ứng đáp»; ^2-724 dhammaṃ «Giáo Pháp»; the awakening-factor names in quotes; any other sense where the attested form would mislead a plain reader.
7. **Term form:** no ", ", " / ", "; " inside a term; no em or en dash. Gapped values with " … " only as attested.
8. **Outside terms:** only when every candidate is wrong for a plain reader; give the reason. These need the user's approval.

## Report (under 450 words, as text)
- The `check` and assembler output lines.
- Number of multi-candidate decisions and of family re-alignments.
- Outside-candidate choices with reasons.
- The 15 most consequential choices (high-frequency terms, contested pairs, the points above).
- Cross-book differences (the table in rule 3), the main ones first.
- Points for the user, each with your proposal.
- Anything you are unsure of.
