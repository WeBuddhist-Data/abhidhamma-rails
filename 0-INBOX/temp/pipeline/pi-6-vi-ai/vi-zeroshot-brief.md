# Brief: Vietnamese zero-shot of pi-6 (Yamaka), ONE chapter

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool at their full paths under D:\Work\OpenPecha\abhidhamma-rails, never via a shell redirect or from PowerShell), PowerShell for commands, `python -I -X utf8 -B` (-B: no __pycache__). LF line endings: open(..., "w", encoding="utf-8", newline="\n"). Write ONLY your own chapter file in the output folder, plus `build_<N>_vi.py` and `notes-<N>.md` inside 0-INBOX\temp\pipeline\pi-6-vi-ai\ (N = your file's number prefix, e.g. 2-01, 7-03, 8). Never create files at the repo root (not even an empty one), outside the repo or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any other file (other agents' chapters, builders and notes, the sample, the terms file, the coordinator rules), never run git (not even git status), never write "seed" or "unseeded" in any file. No web access. You cannot write report files for me: return your report as text.

The user approved the sample (preamble, 1-mulayamaka) on 2026-11-22 as proposed: book title «Các cặp câu hỏi». **Up to five agents work at the same time, one chapter each.** The coordinator may send you messages with frames other agents settled: follow them.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No web lookups. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\: Grep only the specific files named here, never a whole folder.

## Read first (binding)
- 0-INBOX\temp\pipeline\vietnamese-style.md: style, DASH RULE, “…” / ‘…’, core terms, verify commands.
- 0-INBOX\temp\pipeline\pi-6-vi-ai\zeroshot-coordinator-rules.md: the user's decisions, which wave-1 agent sets which frame family, and shared frames. Re-read it before you build and before you report.
- 0-INBOX\temp\pipeline\pi-6-vi-ai\vi-zeroshot-terms.md (READ-ONLY): book title, the ten yamaka headings, all recurring section headings (approved), the pair-question frames, answers, partial-answer frames, labels and terms. Copy them verbatim.
- The approved sample and its builder (READ-ONLY; import, do not edit): AI_translation\vietnamese\pi-6-vietnamese-plain-zeroshot_split_chapters\1-mulayamaka.md, built by 0-INBOX\temp\pipeline\pi-6-vi-ai\build_sample_vi.py (`sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai"); import build_sample_vi as B`; importing writes nothing). Use its constants and checks.
- **Frame-setter outputs** named in the coordinator rules (build_2-01_vi.py / notes-2-01.md, build_7-01_vi.py / notes-7-01.md, build_8_vi.py / notes-8.md) once they exist: import / copy their frames for identical Pāli. If you are yourself the frame-setter of a family, settle that family's frames carefully and list every one in your notes file.
- Cross-book Vietnamese (user-approved, reviewed): pi-1 … pi-5 rails (AI_translation\vietnamese\pi-N-vietnamese-plain-rails_split_chapters\), termbases (AI_translation\vietnamese\pi-N-pali-vietnamese-termbase-plain.md) and the user's decisions (0-INBOX\temp\pipeline\pi-N-vi-ai\termbase\APPROVED.md; pi-1-vi-ai\vi-core-terms.md). The aggregates, bases, elements, truths, formations, latent tendencies, faculties, planes and beings (asaññasatta, arūpa, the path and fruit persons …) are all translated there: reuse their Vietnamese; pi-6-vi-ai\find_pi12345r_vi.py prints the line for a Pāli pattern. Person types follow pi-4.
- AI_translation\skills\zeroshot-translator.md and AI_translation\audience_profile\plain.md.
- Cross-check of meaning and structure only (translate FROM THE PĀLI): the English pi-6 rails AI_translation\english\pi-6-english-plain-rails_split_chapters\<ch>.md (by block ID) and its termbase AI_translation\english\pi-6-pali-english-termbase-plain.md; the commentary 1-SOURCES\Commentaries\pi-yamaka-atthakatha.md (Pāli; allowed) for hard readings. There is no Russian pi-6.

## Source and output
- Source: AI_translation\pali\pi-6_split_chapters\<ch>.md
- Output: AI_translation\vietnamese\pi-6-vietnamese-plain-zeroshot_split_chapters\<ch>.md (same filename; the folder exists).
- Generate it with a builder (pi-6-vi-ai\build_<N>_vi.py, importing build_sample_vi and, where they exist, the frame-setter builders) using fixed strings for every repeated frame, so every repeat is byte-identical. Importing your builder must not write anything (`if __name__ == "__main__":`). The builder asserts every string it takes from pi-1-5 still occurs in those rails files and runs the sample's per-line dash / quote / NFC / id checks.
- A NEW recurring term or formula you settle goes into notes-<N>.md, "Pāli = tiếng Việt" per line.

## Rules
- Identical Pāli = identical Vietnamese, within your chapter, with the sample, with other finished pi-6 chapters and with pi-1-5 Vietnamese.
- Core: dhamma = hiện tượng (the Teaching = Giáo Pháp); khandha «khối»; āyatana «lĩnh vực nhận biết»; dhātu «yếu tố»; sacca «sự thật»; saṅkhāra «tạo tác»; anusaya «khuynh hướng tiềm ẩn» (anuseti «nằm sẵn»); indriya «năng lực»; mūla «gốc rễ»; sati = sự tỉnh thức (never «chánh niệm»). Take the exact member names (rūpakkhandha, cakkhāyatana, cakkhundriya …) from pi-1 / pi-2.
- (Ka) (Kha) (Ga) (Gha) (Ṅa) (Ca) (Cha) (Ja) → (a) (b) (c) (d) (e) (f) (g) (h). Variant brackets "[khác chính tả (…): <Pāli>]" for spelling-only variants, "[dị bản (…): <Pāli>]" otherwise. "…pe…" → "…" (never «….»). Digits and numbering stay.
- **DASH RULE:** "–" exactly where the Pāli has "–", same count per line; never add one; no ":-". Questions end with "?" and use a Vietnamese question word. Avoid a doubled «là».
- **Quotes:** nesting as the Pāli shows, outer “…” inner ‘…’; report any repair.
- Translate the Pāli as written (user rule): no emendations, add nothing that is not in the Pāli, drop nothing (a repeated word stays); only plain spelling slips and missing punctuation may be rendered as meant. Report suspected slips.
- Readability for a plain reader: each pair question must be a clear Vietnamese question (who / where / which ones), and a partial answer must say plainly which ones are and which are not.

## Verify your chapter (all must pass before you report)
- `python -I -X utf8 -B 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-6_split_chapters AI_translation\vietnamese\pi-6-vietnamese-plain-zeroshot_split_chapters <ch>.md` prints OK.
- `python -I -X utf8 -B 0-INBOX\temp\pipeline\dashcheck.py <pali ch> <vietnamese ch>`: equal line counts, 0 dash mismatches, 0 extra em-dashes.
- `python -I -X utf8 -B 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py <pali ch> <vietnamese ch>` prints OK.
- The builder's asserts pass.

## Final report (short, as text, under 350 words)
- Checks passed, segment count.
- Key new frames / terms (also in your notes file) as "Pāli = tiếng Việt", and what you reused from the sample / frame-setters / pi-1-5.
- Pāli you were unsure about or that looks like a source slip (translated as written).
