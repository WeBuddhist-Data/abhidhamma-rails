# Brief: Vietnamese zero-shot of pi-2 (Vibhaṅga), remaining chapters

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool at their full paths, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Write ONLY your own chapter files in the output folder, plus builder/helper scripts and notes named after your chapters inside 0-INBOX\temp\pipeline\pi-2-vi-ai\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any other agent's files, never run git (not even git status), never write "seed" or "unseeded". You cannot write report files for me: return your report as text.

The user approved the sample (preamble and chapter 1 through the line before ^2-1-2-2-0) on 2026-11-18, with the book title «Phân tích các hiện tượng». **The chapter groups run ONE AT A TIME, in book order (user).** Continue in exactly the same style.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No web lookups of Vietnamese Abhidhamma translations. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\ (search only the specific files named here).

## Read first (binding)
- 0-INBOX\temp\pipeline\vietnamese-style.md: style, DASH RULE, “…” / ‘…’, core terms (sati = «sự tỉnh thức», never «chánh niệm»), verify commands.
- 0-INBOX\temp\pipeline\pi-2-vi-ai\vi-zeroshot-terms.md (READ-ONLY): book title «Phân tích các hiện tượng», all 18 chapter headings, the section headings («Phân tích theo kinh», «Phân tích theo Vi Diệu Pháp», «Phần hỏi đáp»), the aggregate formulas, classification frames and terms. Copy them verbatim.
- The approved sample and its builder (READ-ONLY; import, do not edit): 0-INBOX\temp\pipeline\pi-2-vi-ai\ch1-sample.md, built by build_ch1_sample_vi.py (`sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-vi-ai"); import build_ch1_sample_vi as S`). Importing writes nothing.
- **The finished earlier groups' builders, notes and output chapters** (pi-2-vi-ai\build_<chapters>_vi.py, notes-<chapters>.md, AI_translation\vietnamese\pi-2-vietnamese-plain-zeroshot_split_chapters\): the same Pāli must get the same Vietnamese, so import or copy their strings (importing must not rewrite their outputs).
- **Cross-book Vietnamese (user-approved, reviewed): pi-1 Dhammasaṅgaṇī.** The Vibhaṅga reuses its matrix items, the mind-state definitions, the synonym strings, the jhāna formulas, the matter lists and the question/answer frames. Where the Pāli is identical or nearly identical to pi-1, reuse the pi-1 Vietnamese:
  1. AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters\ (final text; find matches by grepping the Pāli in AI_translation\pali\pi-1_split_chapters\ and reading the same non-empty line in the Vietnamese file; pi-2-vi-ai\pi1_lookup_vi.py prints the pi-1 Vietnamese line for a Pāli match);
  2. AI_translation\vietnamese\pi-1-pali-vietnamese-termbase-plain.md and 0-INBOX\temp\pipeline\pi-1-vi-ai\termbase\APPROVED.md (the user's decisions: bodily pain «khó chịu»; sukha «hạnh phúc» (jhāna factor) vs «dễ chịu» (pleasant feeling); vāra «mục» vs bhāṇavāra «phần»; ajjhatta «ở nơi bản thân»; vaṇṇanibhā «ánh màu»; asuropo «sự nói năng cộc cằn»; cittahetuka «có tâm làm nguyên nhân»).
- AI_translation\skills\zeroshot-translator.md and AI_translation\audience_profile\plain.md.
- **Cross-check of meaning and structure only (translate FROM THE PĀLI):** the English rails translation AI_translation\english\pi-2-english-plain-rails_split_chapters\<ch>.md and the Russian one AI_translation\russian\pi-2-russian-plain-rails_split_chapters\<ch>.md (same filenames; find segments by block ID); the Russian zero-shot builders and notes for the same chapters (0-INBOX\temp\pipeline\pi-2-ru\build_<chapters>_ru.py, notes-<chapters>.md) show how each chapter is structured.

## Source and output
- Source: AI_translation\pali\pi-2_split_chapters\<ch>.md
- Output: AI_translation\vietnamese\pi-2-vietnamese-plain-zeroshot_split_chapters\<ch>.md (same filename; the folder exists).
- 1-khandhavibhango.md only: its first 77 non-empty lines are the approved sample. Reuse 0-INBOX\temp\pipeline\pi-2-vi-ai\ch1-sample.md byte-for-byte as the start of the file and continue from ##### Vedanākkhandho ^2-1-2-2-0.
- These chapters are very repetitive (the same lists, synonym strings and question/answer frames many times). Generate them with a builder script with fixed formula strings (pi-2-vi-ai\build_<chapters>_vi.py), so every repeat is byte-identical.

## Rules
- Identical Pāli = identical Vietnamese, within your chapters, with the approved sample, with the earlier groups and with pi-1 Vietnamese.
- Core: dhamma = hiện tượng (the Teaching = Giáo Pháp); abyākata = không xác định về mặt đạo đức; kusala/akusala = thiện/bất thiện; khandha = khối; rūpa = vật chất (visible form = hình sắc); saṅkhāra (aggregate) = tạo tác; vitakka / vicāra = sự hướng tâm / sự duy trì tâm; vīriya «tinh tấn» vs vāyāma / padhāna «nỗ lực»; paṭiccasamuppāda = sự sinh khởi tùy thuộc vào điều kiện; mātikā = ma trận.
- A NEW recurring term or formula you settle goes into 0-INBOX\temp\pipeline\pi-2-vi-ai\notes-<your chapters>.md, one "Pāli = tiếng Việt" per line. Do NOT edit vi-zeroshot-terms.md or the sample builder.
- No notes or commentary of your own inside the translation. Variant brackets "[khác chính tả (Sī., Syā.): <Pāli>]" for spelling-only variants, "[dị bản (…): <Pāli>]" otherwise. "…pe…" → "…" (never «….»). (Ka)/(Kha)/(Ga) → (a)/(b)/(c). Digits stay.
- No "—" or "–" unless the Pāli has one at that spot (same count per line); no ":-". Questions end with "?" and use a Vietnamese question word. Avoid a doubled «là».
- Translate the Pāli as written (user rule): no emendations; only plain spelling slips and missing punctuation may be rendered as meant. Report suspected slips.

## Verify every chapter (all must pass before you report)
- `python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-2_split_chapters AI_translation\vietnamese\pi-2-vietnamese-plain-zeroshot_split_chapters <ch>.md` prints OK.
- `python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py <pali ch> <vietnamese ch>`: equal line counts, 0 dash mismatches, 0 extra em-dashes.
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py <pali ch> <vietnamese ch>` prints OK (IDs, line counts, CR, blanks, NFC, dashes, foreign letters, «chánh niệm»).
- 1-khandhavibhango only: the file starts with ch1-sample.md exactly.

## Final report (short, as text, under 350 words)
- Per chapter: checks passed, segment count.
- Key new terms/formulas (also in your notes file) and what you reused from pi-1 / earlier groups.
- Pāli you were unsure about or that looks like a source slip (translated as written).
