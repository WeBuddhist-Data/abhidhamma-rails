# Brief: Vietnamese zero-shot of pi-4 (Puggalapaññatti), ONE chapter

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool at their full paths, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Write ONLY your own chapter file in the output folder, plus `build_<N>_vi.py` and `notes-<N>.md` (N = your chapter number) inside 0-INBOX\temp\pipeline\pi-4-vi-ai\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any other file (other agents' chapters, builders and notes, the sample, the terms file), never run git (not even git status), never write "seed" or "unseeded" in any file. No web access. You cannot write report files for me: return your report as text.

The user approved the sample (preamble, 1-matika, 2-ekakapuggalapannatti) on 2026-11-20, with the book title «Định danh các hạng người». **Three agents work at the same time, one chapter each.** Finished chapters of other agents (build_<M>_vi.py, notes-<M>.md, their output files) may be read and must be followed for identical Pāli.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No web lookups. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\: Grep only the specific files named here.

## Read first (binding)
- 0-INBOX\temp\pipeline\vietnamese-style.md: style, DASH RULE, “…” / ‘…’, core terms, verify commands.
- 0-INBOX\temp\pipeline\pi-4-vi-ai\vi-zeroshot-terms.md (READ-ONLY): book title, all headings and closers, the frames, every person-type name. Copy them verbatim.
- The approved sample and its builder (READ-ONLY; import, do not edit): AI_translation\vietnamese\pi-4-vietnamese-plain-zeroshot_split_chapters\1-matika.md, 2-ekakapuggalapannatti.md, built by 0-INBOX\temp\pipeline\pi-4-vi-ai\build_sample_vi.py (`sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-4-vi-ai"); import build_sample_vi as B`; importing writes nothing). **B.NAME[pali] holds every person-type name of the matrix: your chapter's definition headings, questions and quoted names MUST use exactly these strings.** The definition frame «Thế nào là X? Ở đời này, có người … – người này được gọi là “X”.» (plural «– những người này được gọi là “…”»), the chapter heading «Định danh các hạng người theo nhóm N» and the closers are constants there.
- Cross-book Vietnamese (user-approved, reviewed): pi-1, pi-2, pi-3 rails (AI_translation\vietnamese\pi-1-…, pi-2-…, pi-3-vietnamese-plain-rails_split_chapters\), termbases (AI_translation\vietnamese\pi-1/2/3-pali-vietnamese-termbase-plain.md) and the user's decisions (0-INBOX\temp\pipeline\pi-1-vi-ai\termbase\APPROVED.md, pi-2-vi-ai\…, pi-3-vi-ai\…). Where the Pāli repeats a passage of those books (jhāna, vimokkha, path / fruit phrases, sīla strings, the similes), reuse their Vietnamese; pi-4-vi-ai\find_pi123_vi.py prints the line for a Pāli pattern.
- AI_translation\skills\zeroshot-translator.md and AI_translation\audience_profile\plain.md.
- Cross-check of meaning and structure only (translate FROM THE PĀLI): AI_translation\english\pi-4-english-plain.md and AI_translation\russian\pi-4-russian-plain-rails_split_chapters\<ch>.md (find segments by block ID); 0-INBOX\temp\pipeline\pi-4\ru-zeroshot-terms.md, ru-rails-formulas.md, notes-<N>.md.

## Source and output
- Source: AI_translation\pali\pi-4_split_chapters\<ch>.md
- Output: AI_translation\vietnamese\pi-4-vietnamese-plain-zeroshot_split_chapters\<ch>.md (same filename; the folder exists).
- Generate it with a builder (pi-4-vi-ai\build_<N>_vi.py, importing build_sample_vi) using fixed strings for every repeated frame, list and simile, so every repeat is byte-identical. The builder asserts that every string it takes from pi-1 / pi-2 / pi-3 still occurs in those rails files and that every person name it uses equals B.NAME.
- A NEW recurring term, simile or formula you settle goes into notes-<N>.md, "Pāli = tiếng Việt" per line.

## Rules
- Identical Pāli = identical Vietnamese, within your chapter, with the sample, with other finished pi-4 chapters and with pi-1 / pi-2 / pi-3 Vietnamese.
- Core: dhamma = hiện tượng (the Teaching = Giáo Pháp); puggala = người (counting word «hạng người»); paññatti = sự định danh; sati = sự tỉnh thức (never «chánh niệm»); sīla = giới; samādhi = định; paññā = trí tuệ (check pi-1 / pi-2 for each).
- No notes or commentary of your own inside the translation. Variant brackets "[khác chính tả (Sī., Syā.): <Pāli>]" for spelling-only variants, "[dị bản (…): <Pāli>]" otherwise. "…pe…" → "…" (never «….»). (Ka)/(Kha)/(Ga) → (a)/(b)/(c). Digits and numbering stay.
- **DASH RULE:** "–" exactly where the Pāli has "–", same count per line; never add one; no ":-". Questions end with "?" and use a Vietnamese question word. Avoid a doubled «là».
- Translate the Pāli as written (user rule): no emendations, add nothing that is not in the Pāli; only plain spelling slips and missing punctuation may be rendered as meant. Report suspected slips.
- Similes and verses (gāthā): each Pāli line one Vietnamese line; nothing moved across lines.

## Verify your chapter (all must pass before you report)
- `python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-4_split_chapters AI_translation\vietnamese\pi-4-vietnamese-plain-zeroshot_split_chapters <ch>.md` prints OK.
- `python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py <pali ch> <vietnamese ch>`: equal line counts, 0 dash mismatches, 0 extra em-dashes.
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py <pali ch> <vietnamese ch>` prints OK.
- The builder's asserts pass.

## Final report (short, as text, under 300 words)
- Checks passed, segment count.
- Key new terms / similes / formulas (also in your notes file) and what you reused from the sample / pi-1 / pi-2 / pi-3 / other chapters.
- Pāli you were unsure about or that looks like a source slip (translated as written).
