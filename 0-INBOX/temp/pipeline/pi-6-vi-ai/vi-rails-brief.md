# Brief: RAILS Vietnamese translation, plain audience, pi-6 (Yamaka): ONE chapter

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at full paths under D:\Work\OpenPecha\abhidhamma-rails; never write any file from PowerShell), PowerShell for commands, `python -I -X utf8 -B` (-B: no __pycache__). LF line endings: open(..., "w", encoding="utf-8", newline="\n").
- Write ONLY your chapter file AI_translation\vietnamese\pi-6-vietnamese-plain-rails_split_chapters\<ch>.md, plus `build_rails_<N>_vi.py` and `notes-rails-<N>.md` (N = the chapter's number prefix, e.g. 2-01, 4, 10-13) in 0-INBOX\temp\pipeline\pi-6-vi-ai\rails\ (and the adherence copy in rails\adh-<N>\). Never create files at the repo root (not even an empty one), outside the repo or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any other file (the sample, its builder, vi-rails-formulas.md, rails-coordinator-rules.md, other agents' chapters and builders), never run git (not even git status), never write "seed" or "unseeded". No web. You cannot write report files for me: return your report as text.
- The user approved the rails sample (preamble, 1-mulayamaka) on 2026-11-22. **Five agents work at the same time, one chapter each.** Copy the approved strings exactly; finished chapters of other agents (build_rails_<M>_vi.py, notes-rails-<M>.md, their chapter files) must be followed for identical Pāli.

## FORBIDDEN
- The copyrighted reference translation: never open, grep or search 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\.
- The Vietnamese zero-shot of THIS book: AI_translation\vietnamese\pi-6-vietnamese-plain-zeroshot_split_chapters\, pi-6-vietnamese-plain-zeroshot.md, and everything in 0-INBOX\temp\pipeline\pi-6-vi-ai\ outside termbase\ and rails\ (build_*_vi.py, notes-*.md, vi-zeroshot-*.md, zeroshot-coordinator-rules.md, harmonise*, backup-pre-harmonise\, divergences*.md, find_divergences_vi.py, vi_common.py, probe_*.py, list_headings_vi.py, merge_zeroshot_vi.py, split_keywords_vi.py, senses_prepare_vi.py, senses\, the other briefs); the Vietnamese side of the keyword map (pi-6-vi-ai\mapper-vi\ except *.keywords.md; AI_translation\vietnamese\pi-6-keywords-by-reference-pali-vietnamese-plain.md).
- No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\: Grep only the specific files named here.

## Read first (binding)
- AI_translation\skills\rails-verse-translator.md; 0-INBOX\temp\pipeline\vietnamese-style.md.
- 0-INBOX\temp\pipeline\pi-6-vi-ai\rails\vi-rails-formulas.md (approved: book frame, yamaka titles, labels, headings, pair questions, answers, the four methods, the hetuvāra series) and 0-INBOX\temp\pipeline\pi-6-vi-ai\rails\rails-coordinator-rules.md (the user's termbase decisions, rules, the shared person / place question shell, the family setters; re-read it before you report); the sample builder rails\build_rails_sample_vi.py (import READ-ONLY: `sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails"); import build_rails_sample_vi as S`; importing writes nothing; labels always from S.LABEL); the approved sample chapter AI_translation\vietnamese\pi-6-vietnamese-plain-rails_split_chapters\1-mulayamaka.md.
- Your family setter's builder and notes (rails-coordinator-rules.md, "Family setters"), once it is finished: import it with importlib (file names contain "-").
- Locked termbase: AI_translation\vietnamese\pi-6-pali-vietnamese-termbase-plain.md and 0-INBOX\temp\pipeline\pi-6-vi-ai\termbase\APPROVED.md, plus the pi-1 … pi-5 termbase\APPROVED.md. Terms in citation form; add or drop «các» / «những», «có», «là», tense words as grammar needs; never swap in a synonym. If no sense fits, use the closest sibling entry and REPORT it. Member names (khandha, āyatana, dhātu, sacca, saṅkhāra, dhamma, indriya, anusaya, persons, planes) from the termbase.
- pi-1 … pi-5 Vietnamese rails for identical Pāli (AI_translation\vietnamese\pi-N-vietnamese-plain-rails_split_chapters\; rails\find_pi12345r_vi.py <regex> prints the line for a Pāli pattern).
- Meaning and layout only (never wording): AI_translation\english\pi-6-english-plain-rails_split_chapters\<ch>.md (there is no Russian pi-6); the commentary 1-SOURCES\Commentaries\pi-yamaka-atthakatha.md (Pāli; allowed; grep it).

## Source and output
- Source: AI_translation\pali\pi-6_split_chapters\<ch>.md. Output: AI_translation\vietnamese\pi-6-vietnamese-plain-rails_split_chapters\<ch>.md.
- Build it with rails\build_rails_<N>_vi.py from fixed strings and slot functions (importing S and your family setter), so every repeat is byte-identical; the builder asserts every (pi-N) string it uses still occurs in those rails, and runs S's per-line dash / quote / NFC checks. The Yamaka repeats one frame thousands of times: parse the Pāli line into its frame and slots, never translate line by line by hand; a line your parser cannot place must fail the build (no silent fallback).
- Expose your frames as named constants and functions (later chapters import them). New recurring strings: notes-rails-<N>.md, "Pāli = tiếng Việt" per line.

## Rules
- Block IDs exact; headings keep their #-level; each segment has the source's number of non-empty lines; one blank line between segments.
- DASH RULE: "–" only where the Pāli has one, same count per line; no ":-". "…pe…" → "…" (never «….»). Questions end with "?" with a Vietnamese question word; keep the Pāli's own punctuation where it differs and report it. Variant brackets as the sample.
- Translate the Pāli as written: no emendations; add nothing that is not in the Pāli and drop nothing that is (a repeated word stays); never merge sentences; only plain spelling slips and missing punctuation may be rendered as meant. Report suspected slips.
- Identical Pāli = identical Vietnamese, within your chapter, with the sample, with other finished chapters and with pi-1 … pi-5 rails (unless the termbase decides otherwise). Where two finished rails chapters disagree, follow rails-coordinator-rules.md, then pi-1 … pi-5, then the family setter, then the earlier chapter, and list the clash in your notes.
- Distinct pairs stay distinct: mūla «gốc rễ» / mūlamūla «cội rễ»; paṭiloma «chiều ngược» / paccanīka «chiều nghịch»; uppajjati «sinh khởi» / upapajjati «tái sinh»; uppanna «ở trạng thái đã sinh khởi» / uppajjittha «đã sinh khởi»; parijānāti «hiểu biết trọn vẹn» / pajahati «dứt bỏ» / bhāveti «tu tập» / sacchikaroti «tự mình chứng nghiệm»; pahīna «đã được dứt bỏ» / appahīna «chưa được dứt bỏ».
- Readability for a plain reader; avoid «là là», «được được».

## Verify (all must pass)
```
python -I -X utf8 -B 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-6_split_chapters AI_translation\vietnamese\pi-6-vietnamese-plain-rails_split_chapters <ch>.md
python -I -X utf8 -B 0-INBOX\temp\pipeline\dashcheck.py <pali ch> <vietnamese ch>
python -I -X utf8 -B 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py <pali ch> <vietnamese ch>
```
Termbase adherence: copy your chapter (Write tool) into rails\adh-<N>\ and run `python -I -X utf8 -B 0-INBOX\temp\pipeline\termbase_adherence_vi.py AI_translation\pali\pi-6-keywords-by-reference-pali-plain.md AI_translation\vietnamese\pi-6-pali-vietnamese-termbase-plain.md 0-INBOX\temp\pipeline\pi-6-vi-ai\rails\adh-<N>`; read misses with judgement and fix genuine ones.

## Report (under 300 words, as text)
Checks, segment count, adherence; the frames you set or imported (notes file); reuse from the sample / pi-1 … pi-5 / other chapters; termbase misfits and gaps; unsure Pāli or slips.
