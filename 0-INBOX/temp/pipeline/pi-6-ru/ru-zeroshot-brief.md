# Brief: Russian zero-shot of pi-6 (Yamaka), ONE chapter

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool at their full paths under D:\Work\OpenPecha\abhidhamma-rails, never via a shell redirect or from PowerShell), PowerShell for commands, `python -I -X utf8 -B` (-B: no __pycache__). LF line endings: open(..., "w", encoding="utf-8", newline="\n"). Write ONLY your own chapter file in the output folder, plus `build_<N>_ru.py` and `notes-<N>.md` inside 0-INBOX\temp\pipeline\pi-6-ru\ (N = your file's number prefix, e.g. 2-01, 7-03, 8). Never create files at the repo root (not even an empty one), outside the repo or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any other file (other agents' chapters, builders and notes, the sample, the terms file, the coordinator rules), never run git (not even git status), never write "seed" or "unseeded" in any file. No web access. Grep only the specific files named here, never a whole folder. If you run long, write the builder in several Write/Edit steps. You cannot write report files for me: return your report as text.

The user approved the sample (preamble, 1-mulayamaka). **Up to three agents work at the same time, one chapter each.** The coordinator may send you messages with frames other agents settled: follow them.

## Read first (binding)
- 0-INBOX\temp\pipeline\russian-style.md: style, DASH RULE, «…» / „…“, no «ли», core terms, verify commands.
- 0-INBOX\temp\pipeline\pi-6-ru\zeroshot-coordinator-rules.md: the user's decisions, which wave-1 agent sets which frame family, and shared frames. Re-read it before you build and before you report.
- 0-INBOX\temp\pipeline\pi-6-ru\ru-zeroshot-terms.md (READ-ONLY): book title, the ten yamaka headings, all recurring section headings, the pair-question frames, answers, partial-answer frames, labels and terms. Copy them verbatim.
- The approved sample and its builder (READ-ONLY; import, do not edit): AI_translation\russian\pi-6-russian-plain-zeroshot_split_chapters\1-mulayamaka.md, built by 0-INBOX\temp\pipeline\pi-6-ru\build_sample_ru.py (`sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru"); import build_sample_ru as B`; importing writes nothing). Use its constants and checks; take labels from it, never type them.
- **Frame-setter outputs** named in the coordinator rules (build_2-01_ru.py / notes-2-01.md, build_7-01_ru.py / notes-7-01.md, build_8_ru.py / notes-8.md) once they exist: import / copy their frames for identical Pāli (load a hyphenated module with importlib.import_module("build_2-01_ru")). If you are yourself the frame-setter of a family, settle that family's frames carefully and list every one in your notes file.
- Cross-book Russian (user-approved, reviewed): pi-1 … pi-5 rails (AI_translation\russian\pi-N-russian-plain-rails_split_chapters\), termbases (AI_translation\russian\pi-N-pali-russian-termbase-plain.md; grep, don't read whole) and the user's decisions (0-INBOX\temp\pipeline\pi-1-ru\termbase\APPROVED.md, pi-2-ru\termbase\APPROVED.md). The aggregates, bases, elements, truths, formations, latent tendencies, faculties, planes and beings (asaññasatta, arūpa, the path and fruit persons …) are all translated there: reuse their Russian; `python -I -X utf8 -B 0-INBOX\temp\pipeline\pi-6-ru\find_pi12345r_ru.py "<Pāli regex>" [books] [max_hits]` prints the line. Person types follow pi-4.
- AI_translation\skills\zeroshot-translator.md and AI_translation\audience_profile\plain.md.
- Cross-check of meaning and structure only (translate FROM THE PĀLI): the English pi-6 rails AI_translation\english\pi-6-english-plain-rails_split_chapters\<ch>.md and the Hindi pi-6 rails AI_translation\hindi\pi-6-hindi-plain-rails_split_chapters\<ch>.md (by block ID), the English termbase AI_translation\english\pi-6-pali-english-termbase-plain.md; the commentary 1-SOURCES\Commentaries\pi-yamaka-atthakatha.md (Pāli; allowed) for hard readings. Do not open any Vietnamese file.

## Source and output
- Source: AI_translation\pali\pi-6_split_chapters\<ch>.md
- Output: AI_translation\russian\pi-6-russian-plain-zeroshot_split_chapters\<ch>.md (same filename; the folder exists).
- Generate it with a builder (pi-6-ru\build_<N>_ru.py, importing build_sample_ru and, where they exist, the frame-setter builders) using fixed strings for every repeated frame, so every repeat is byte-identical. Importing your builder must not write anything (`if __name__ == "__main__":`). The builder asserts every string it takes from pi-1-5 still occurs in those rails files and runs the sample's per-line dash / quote / NFC / id checks.
- A NEW recurring term or formula you settle goes into notes-<N>.md, "Pāli = Russian" per line.

## Rules
- Identical Pāli = identical Russian, within your chapter, with the sample, with other finished pi-6 chapters and with pi-1-5 Russian.
- Core terms as in ru-zeroshot-terms.md and russian-style.md; exact member names (rūpakkhandha, cakkhāyatana, cakkhundriya …) from pi-1 / pi-2 Russian.
- Variant brackets «[вариант написания (…): <Pāli>]» for spelling-only variants, «[вариант чтения (…): <Pāli>]» otherwise. "…pe…" → "…" (never «….»). Digits and numbering stay.
- **DASH RULE:** "–" exactly where the Pāli has "–", same count per line; never add one; no ":-". Questions end with "?"; no «ли».
- Translate the Pāli as written (user rule): no emendations, add nothing that is not in the Pāli, drop nothing (a repeated word stays); only plain spelling slips and missing punctuation may be rendered as meant. A WRONG punctuation mark (a comma where a full stop belongs, «.» ending a question …), a doubled or missing negation, or a one-letter slip that changes the meaning stays as written. Report suspected slips.
- Readability for a plain reader: each pair question must be a clear Russian question (who / where / which ones), and a partial answer must say plainly which ones are and which are not.

## Verify your chapter (all must pass before you report)
- `python -I -X utf8 -B 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-6_split_chapters AI_translation\russian\pi-6-russian-plain-zeroshot_split_chapters <ch>.md` prints OK.
- `python -I -X utf8 -B 0-INBOX\temp\pipeline\dashcheck.py <pali ch> <russian ch>`: equal line counts, 0 dash mismatches, 0 extra em-dashes.
- `python -I -X utf8 -B 0-INBOX\temp\pipeline\pi-1-ru\verify_ru.py <pali ch> <russian ch>` passes.
- No «ли», no Latin outside variant brackets, no double blank lines, no CR. The builder's asserts pass.

## Final report (short, as text, under 350 words)
- Checks passed, segment count.
- Key new frames / terms (also in your notes file) as "Pāli = Russian", and what you reused from the sample / frame-setters / pi-1-5.
- Pāli you were unsure about or that looks like a source slip (translated as written).
