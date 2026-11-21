# Brief: RAILS Vietnamese translation, plain audience, pi-3 (Dhātukathā): ONE chapter

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at full paths; never write any file from PowerShell), PowerShell for commands, `python -I -X utf8`.
- Write ONLY your chapter file AI_translation\vietnamese\pi-3-vietnamese-plain-rails_split_chapters\<ch>.md, plus `build_rails_<N>_vi.py` and `notes-rails-<N>.md` (N = chapter number) in 0-INBOX\temp\pipeline\pi-3-vi-ai\rails\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any other file (the sample, its builder, vi-rails-formulas.md, other agents' chapters), never run git (not even git status), never write "seed" or "unseeded". No web. You cannot write report files for me: return your report as text.
- The user approved the rails sample (preamble, 1-uddeso, 2-pathamanayo) and its proposed frames for ch3-15 on 2026-11-20. **Three agents work at the same time, one chapter each.** Copy the approved strings exactly; finished chapters of other agents (build_rails_<M>_vi.py, notes-rails-<M>.md, their chapter files) must be followed for identical Pāli.

## FORBIDDEN
- The copyrighted reference translation: never open, grep or search 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\.
- The Vietnamese zero-shot of THIS book: AI_translation\vietnamese\pi-3-vietnamese-plain-zeroshot_split_chapters\, pi-3-vietnamese-plain-zeroshot.md, and everything zero-shot in pi-3-vi-ai\ (build_*_vi.py outside rails\, notes-*.md outside rails\, vi-zeroshot-*.md, harmonise*, backup-pre-harmonise\, divergences*.md, find_divergences_vi.py, vi_common.py, probe_*.py, lookup_vi.py, merge_zeroshot_vi.py); the Vietnamese side of the keyword maps (pi-3-vi-ai\mapper-vi\ except *.keywords.md; AI_translation\vietnamese\pi-3-keywords-by-reference-pali-vietnamese-plain.md).
- No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\: Grep only the specific files named here.

## Read first (binding)
- AI_translation\skills\rails-verse-translator.md; 0-INBOX\temp\pipeline\vietnamese-style.md.
- 0-INBOX\temp\pipeline\pi-3-vi-ai\rails\vi-rails-formulas.md (approved; its "(proposed for ch3-15)" frames are now approved) and the sample builder rails\build_rails_sample_vi.py (import READ-ONLY: `sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\rails"); import build_rails_sample_vi as S`; importing writes nothing). The approved sample chapters AI_translation\vietnamese\pi-3-vietnamese-plain-rails_split_chapters\1-uddeso.md, 2-pathamanayo.md.
- Locked termbase: AI_translation\vietnamese\pi-3-pali-vietnamese-termbase-plain.md and 0-INBOX\temp\pipeline\pi-3-vi-ai\termbase\APPROVED.md (nāsaññā «không phải không tri giác»; labbhati «tìm thấy»; Samucchede written «sự phân tích»; the kāma / āyatana artefact uses the separate terms «dục lạc», «lĩnh vực nhận biết»; ^3-447 «Rūpakkhandhā cattāro» as written), plus pi-1 / pi-2 APPROVED.md. Terms in citation form; add or drop «các» / «những», «có», «là», «điều», «với», tense words as grammar needs; never swap in a synonym. If no sense fits, use the closest sibling entry and REPORT it.
- pi-1 / pi-2 Vietnamese rails for identical Pāli (AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters\, pi-2-vietnamese-plain-rails_split_chapters\; rails\find_pi12_vi.py looks up the line for a Pāli pattern).
- Meaning and layout only: AI_translation\russian\pi-3-russian-plain-rails_split_chapters\<ch>.md, AI_translation\english\pi-3-english-plain.md (grep by block ID).

## Source and output
- Source: AI_translation\pali\pi-3_split_chapters\<ch>.md. Output: AI_translation\vietnamese\pi-3-vietnamese-plain-rails_split_chapters\<ch>.md.
- Build it with rails\build_rails_<N>_vi.py from fixed formula strings (importing S), so every repeat is byte-identical; the builder asserts every (pi-1) / (pi-2) string it uses still occurs in those rails.
- New recurring strings (verse words, labels, frames not in the formulas file): notes-rails-<N>.md, "Pāli = tiếng Việt" per line.

## Rules
- Block IDs exact; headings keep their #-level; each segment has the source's number of non-empty lines; one blank line between segments.
- DASH RULE: "–" only where the Pāli has one, same count per line; no ":-". "…pe…" → "…" (never «….»). Questions end with "?" with a Vietnamese question word. Quotes “…” / ‘…’. Variant brackets as the sample.
- Translate the Pāli as written: no emendations, add nothing that is not in the Pāli (Vietnamese grammar words such as «nhưng», «thì», pronouns as in the sample are fine); only plain spelling slips and missing punctuation may be rendered as meant. Report suspected slips (wrong counts kept as written).
- Summary verses (uddāna): each Pāli line one Vietnamese line, no word moved to another line, same Pāli words = same Vietnamese across chapters.
- Readability for a plain reader; avoid «là là», «được được».

## Verify (all must pass)
```
python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-3_split_chapters AI_translation\vietnamese\pi-3-vietnamese-plain-rails_split_chapters <ch>.md
python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py <pali ch> <vietnamese ch>
python -I -X utf8 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py <pali ch> <vietnamese ch>
```
Termbase adherence: copy your chapter (Write tool) into a scratch folder rails\adh-<N>\ and run `python -I -X utf8 0-INBOX\temp\pipeline\termbase_adherence_vi.py AI_translation\pali\pi-3-keywords-by-reference-pali-plain.md AI_translation\vietnamese\pi-3-pali-vietnamese-termbase-plain.md 0-INBOX\temp\pipeline\pi-3-vi-ai\rails\adh-<N>`; read misses with judgement and fix genuine ones.

## Report (under 300 words, as text)
Checks, segment count, adherence; new strings (notes file); reuse from the sample / pi-1 / pi-2 / other chapters; termbase misfits and gaps; unsure Pāli or slips.
