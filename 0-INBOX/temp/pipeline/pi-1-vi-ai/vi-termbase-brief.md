# Brief: termbase-builder, Pāli→Vietnamese plain, pi-1 (Dhammasaṅgaṇī)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Write ONLY in 0-INBOX\temp\pipeline\pi-1-vi-ai\termbase\. Do not touch 1-SOURCES\, 4-SYSTEM\ or AI_translation\ (the assembler writes there, not you), never create files at the repo root or in a system temp folder, never run git (not even git status). Never use the words "seed" or "unseeded" anywhere. You cannot write report files for me: return your report as text.

The user approves the termbase explicitly afterwards; your job is a clean, consistent proposal plus the list of points the user must decide.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\. No web lookups of Vietnamese Abhidhamma translations. Our terms must be our own.

## Read first
- AI_translation\skills\termbase-builder.md. Follow it.
- 0-INBOX\temp\pipeline\hindi-termbase-brief.md, section "How to choose" (rules 1–5). They apply here with Vietnamese in place of Hindi; this brief adds what is specific to Vietnamese pi-1.
- AI_translation\audience_profile\plain.md (no Buddhist background; understanding first).
- 0-INBOX\temp\pipeline\vietnamese-style.md and pi-1-vi-ai\vi-core-terms.md (core terms and the review lessons on pairs that must stay distinct; binding; sati = «sự tỉnh thức», never «chánh niệm»).
- pi-1-vi-ai\vi-zeroshot-terms.md (the pi-1 term list: headings and all matrix items), pi-1-vi-ai\harmonise-notes.md, pi-1-vi-ai\senses\senses-conventions.md. The user approved the pi-1 translation, the keyword map and the senses built from these.
- pi-1-vi-ai\agents-run.md: the user decisions and the open points logged so far (search it for "FOR THE RAILS REVIEW", "dukkha", "āhāra").
- For how a finished termbase of this book looks and how the Russian run settled the same Pāli senses (meaning only, not wording): AI_translation\russian\pi-1-pali-russian-termbase-plain.md and 0-INBOX\temp\pipeline\pi-1-ru\termbase\termbase-decisions.md (grep, don't read whole).

## Input, output, tools
- Input: AI_translation\vietnamese\pi-1-pali-word-vietnamese-senses-plain.md (2,485 headwords, 2,526 senses; 101 senses have 2+ candidates). Line N = headword N.
- Your decisions: 0-INBOX\temp\pipeline\pi-1-vi-ai\termbase\decisions.tsv, one line each: `hw|sense_index<TAB>term<TAB>short reason` (sense_index 0-based within the senses line). Start the file with a `#` comment line.
- Helper: `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-vi-ai\termbase\tb_tool_vi.py` (read its docstring):
  - `list <from> <to> [--multi]`: senses with candidate counts from the pi-1 map and the decisions so far ("prior" is empty: there is no approved Vietnamese termbase of another book yet).
  - `fam <regex>`: a whole lemma family across pi-1.
  - `hcount <vietnamese> …`: occurrences in the merged pi-1 Vietnamese zero-shot.
  - `check <from> <to>`: every multi-candidate sense decided, no forbidden characters, outside choices listed. Must print "no errors" for 1 2485.
- Then run the assembler yourself to confirm: `python -I -X utf8 0-INBOX\temp\pipeline\termbase_assemble.py 1 vietnamese vi-ai plain` must print "no errors" (it writes AI_translation\vietnamese\pi-1-pali-vietnamese-termbase-plain.md and termbase\termbase-decisions.md; that is expected).

## Vietnamese pi-1 specifics
1. **Order of preference for multi-candidate senses:** (a) a core term in vietnamese-style.md / vi-core-terms.md, the pi-1 term list (vi-zeroshot-terms.md; matrix items as named there) or a user decision; (b) the form the pi-1 translation uses most (map counts / hcount); (c) the clearest plain-Vietnamese candidate.
2. **Citation form (Vietnamese has no inflection; most multi-candidate senses are variants of one expression):**
   - A noun headword (an abstract noun, a factor, a list item) takes the standalone noun form with its nominaliser as the text uses it on its own: «sự tỉnh thức», «sự hoài nghi», «niềm tin», «sự xao động». A compound member, stem or adjective takes the bare form: «tỉnh thức», «hoài nghi».
   - Participles and verbs: the bare verb, unless the Pāli tense is the point of the term (matrix items such as uppannā «đã sinh khởi» vs uppādino «sẽ sinh khởi» keep their tense word; a future verb keeps «sẽ»).
   - Drop «có» (having) and classifiers such as «loại» unless they are part of the meaning (sahagata «có X đi kèm», -ika «có X» keep «có»).
   - Prefer the unbroken form over the gapped « … » form when both are attested for one sense; keep a gapped form only when it is the only candidate.
   - Record the rule you apply once in the decisions file header and apply it the same way across a family (`fam`).
3. **Family alignment** (decisions on single-candidate senses) only where the same Pāli lemma in the same meaning drifted to a different Vietnamese word. The approved sense splits stay split (rūpa, dhamma, kāya, dukkha, sukha, vuṭṭhāna, saṅkha, phala, para, santuṭṭhitā …).
4. **Keep distinct Pāli terms distinct** where the text puts them side by side (check with `fam`, `hcount` and the segments). Decide and give the reason:
   - vīriya «tinh tấn» vs padhāna / vāyāma «nỗ lực»; vicikicchā vs kaṅkhā; kukkucca «hối tiếc» vs uddhacca «xao động»; mettā vs abyāpāda; sammappadhāna = sammāvāyāma «nỗ lực đúng đắn» (user-accepted pairing; list it, do not change).
   - parāmāsa «hiểu sai lệch» vs abhinivesa and the diṭṭhigata family («mắc kẹt trong các quan điểm»).
   - cetanā «chủ ý» vs sañcetanā «sự cố ý» (they stand side by side in the cetanā string).
5. **Open points to put to the user (decide a proposal, mark it, explain):**
   - **dukkha, bodily pain:** the translation renders dukkhaṃ / dukkhasahagataṃ as «sự đau khổ» but dukkhindriyaṃ as «năng lực khó chịu» in the same segments (^1-556, ^1-1388, ^1-1404). Propose one term for pain (the rails step will then make the text consistent).
   - **āhāra, edible food:** kabaḷīkāro āhāro is «dưỡng chất» (same as nutriment in general). Say whether a plain reader needs «thức ăn» there.
   - **sukha / sukhaṃ:** «hạnh phúc» (factor) vs «dễ chịu» (feeling) sit in one combined sense; propose the term and say whether the split should be restored.
   - Any other sense where the attested form would mislead a plain reader.
6. **Term form:** no ", ", " / ", "; " inside a term; no em or en dash. Gapped values with " … " only as attested.
7. **Outside terms:** only when every candidate is wrong for a plain reader; give the reason. These need the user's approval.

## Report (under 450 words, as text)
- The `check` and assembler output lines.
- Number of multi-candidate decisions and of family re-alignments.
- The citation-form rule you applied (one paragraph).
- Outside-candidate choices with reasons.
- The 15 most consequential choices (high-frequency terms, contested pairs, the open points above).
- The open points for the user, each with your proposal.
- Anything you are unsure of.
