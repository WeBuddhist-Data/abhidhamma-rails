# Brief: Vietnamese zero-shot of pi-5 (Kathāvatthu), ONE chapter

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool at their full paths under D:\Work\OpenPecha\abhidhamma-rails, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Write ONLY your own chapter file in the output folder, plus `build_<N>_vi.py` and `notes-<N>.md` (N = your chapter number) inside 0-INBOX\temp\pipeline\pi-5-vi-ai\. Never create files at the repo root, outside the repo or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any other file (other agents' chapters, builders and notes, the sample, the terms file), never run git (not even git status), never write "seed" or "unseeded" in any file. No web access. You cannot write report files for me: return your report as text.

The user approved the sample (preamble, 1-puggalakatha) on 2026-11-21, with the book title «Các vấn đề tranh luận». **Three agents work at the same time, one chapter each.** Finished chapters of other agents (build_<M>_vi.py, notes-<M>.md, their output files) may be read and must be followed for identical Pāli.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No web lookups. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\: Grep only the specific files named here, never a whole folder.

## Read first (binding)
- 0-INBOX\temp\pipeline\vietnamese-style.md: style, DASH RULE, “…” / ‘…’, core terms, verify commands.
- 0-INBOX\temp\pipeline\pi-5-vi-ai\vi-zeroshot-terms.md (READ-ONLY): book title, all chapter and kathā headings, every debate formula, the labels and terms. Copy them verbatim.
- The approved sample and its builder (READ-ONLY; import, do not edit): AI_translation\vietnamese\pi-5-vietnamese-plain-zeroshot_split_chapters\1-puggalakatha.md, built by 0-INBOX\temp\pipeline\pi-5-vi-ai\build_sample_vi.py (`sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai"); import build_sample_vi as B`; importing writes nothing). Its constants hold the debate frames (question «Có phải X không?», «Đúng vậy.», «Không nên nói như vậy.», the rebuttal pentad sentences, «Hãy thừa nhận sự bác bỏ / sự phản bác.», the micchā verdict «Điều bạn nói ở đây là sai – “…”», the section labels, the speaker notes, the sutta-quote frames, «này bạn» for re), and the quote-order repair rule.
- Cross-book Vietnamese (user-approved, reviewed): pi-1, pi-2, pi-3, pi-4 rails (AI_translation\vietnamese\pi-N-vietnamese-plain-rails_split_chapters\), termbases (AI_translation\vietnamese\pi-N-pali-vietnamese-termbase-plain.md) and the user's decisions (0-INBOX\temp\pipeline\pi-N-vi-ai\termbase\APPROVED.md). Lists, jhāna / path / fruit phrases, person types (pi-4) and sutta passages already translated there: reuse their Vietnamese; pi-5-vi-ai\find_pi1234_rails_vi.py prints the line for a Pāli pattern.
- AI_translation\skills\zeroshot-translator.md and AI_translation\audience_profile\plain.md.
- Cross-check of meaning and structure only (translate FROM THE PĀLI): AI_translation\russian\pi-5-russian-plain-rails_split_chapters\<ch>.md (by block ID); 0-INBOX\temp\pipeline\pi-5-ru\ru-zeroshot-terms.md, ru-rails-formulas.md; the commentary 1-SOURCES\Commentaries\pi-kathavatthu-atthakatha.md (Pāli; allowed) for hard readings.

## Source and output
- Source: AI_translation\pali\pi-5_split_chapters\<ch>.md
- Output: AI_translation\vietnamese\pi-5-vietnamese-plain-zeroshot_split_chapters\<ch>.md (same filename; the folder exists).
- Generate it with a builder (pi-5-vi-ai\build_<N>_vi.py, importing build_sample_vi) using fixed strings for every repeated frame, so every repeat is byte-identical. The builder asserts every string it takes from pi-1-4 still occurs in those rails files and runs the sample's per-line dash / quote / NFC checks if B offers them.
- A NEW recurring term or formula you settle goes into notes-<N>.md, "Pāli = tiếng Việt" per line.

## Rules
- Identical Pāli = identical Vietnamese, within your chapter, with the sample, with other finished pi-5 chapters and with pi-1-4 Vietnamese.
- Core: dhamma = hiện tượng (the Teaching = Giáo Pháp); puggala = người; saccikaṭṭha «thực tại chân thật»; paramattha «thực tại tối hậu»; upalabbhati «được tìm thấy»; sakavādī «người theo học thuyết của chúng ta»; paravādī «người theo học thuyết khác»; sati = sự tỉnh thức (never «chánh niệm»).
- Speaker notes in square brackets are translated inside the same brackets. Variant brackets "[khác chính tả (…): <Pāli>]" / "[dị bản (…): <Pāli>]" as the sample. "…pe…" → "…" (never «….»). Digits stay.
- **DASH RULE:** "–" exactly where the Pāli has "–", same count per line; never add one; no ":-". Questions end with "?" and use a Vietnamese question word. Avoid a doubled «là».
- **Quotes:** nesting as the Pāli shows, outer “…” inner ‘…’; repair a garbled close order ("’ → ’”) as the sample does; report other quote irregularities and keep them as written.
- Translate the Pāli as written (user rule): no emendations, add nothing that is not in the Pāli; only plain spelling slips and missing punctuation may be rendered as meant. Report suspected slips.
- Verses: each Pāli line one Vietnamese line.

## Verify your chapter (all must pass before you report)
- `python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-5_split_chapters AI_translation\vietnamese\pi-5-vietnamese-plain-zeroshot_split_chapters <ch>.md` prints OK.
- `python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py <pali ch> <vietnamese ch>`: equal line counts, 0 dash mismatches, 0 extra em-dashes.
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py <pali ch> <vietnamese ch>` prints OK.
- The builder's asserts pass.

## Final report (short, as text, under 300 words)
- Checks passed, segment count.
- Key new terms / formulas (also in your notes file) and what you reused from the sample / pi-1-4 / other chapters.
- Pāli you were unsure about or that looks like a source slip (translated as written).
