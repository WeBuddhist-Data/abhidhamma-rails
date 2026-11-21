# Brief: RAILS Vietnamese translation, plain audience, pi-5 (Kathāvatthu): ONE chapter

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at full paths under D:\Work\OpenPecha\abhidhamma-rails; never write any file from PowerShell), PowerShell for commands, `python -I -X utf8 -B` (-B: no __pycache__). LF line endings: open(..., "w", encoding="utf-8", newline="\n").
- Write ONLY your chapter file AI_translation\vietnamese\pi-5-vietnamese-plain-rails_split_chapters\<ch>.md, plus `build_rails_<N>_vi.py` and `notes-rails-<N>.md` (N = chapter number) in 0-INBOX\temp\pipeline\pi-5-vi-ai\rails\ (and the adherence copy in rails\adh-<N>\). Never create files at the repo root, outside the repo or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any other file (the sample, its builder, vi-rails-formulas.md, rails-coordinator-rules.md, other agents' chapters), never run git (not even git status), never write "seed" or "unseeded". No web. You cannot write report files for me: return your report as text.
- The user approved the rails sample (preamble, 1-puggalakatha) on 2026-11-21. **Three agents work at the same time, one chapter each.** Copy the approved strings exactly; finished chapters of other agents (build_rails_<M>_vi.py, notes-rails-<M>.md, their chapter files) must be followed for identical Pāli.

## FORBIDDEN
- The copyrighted reference translation: never open, grep or search 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\.
- The Vietnamese zero-shot of THIS book: AI_translation\vietnamese\pi-5-vietnamese-plain-zeroshot_split_chapters\, pi-5-vietnamese-plain-zeroshot.md, and everything zero-shot in pi-5-vi-ai\ (build_*_vi.py and notes-*.md outside rails\, vi-zeroshot-*.md, coordinator-rules.md, harmonise*, backup-pre-harmonise\, divergences*.md, find_divergences_vi.py, vi_common.py, probe_*.py, builder_hits_vi.py, find_pi1234_rails_vi.py, fix_crlf_vi.py, merge_zeroshot_vi.py); the Vietnamese side of the keyword maps (pi-5-vi-ai\mapper-vi\ except *.keywords.md; AI_translation\vietnamese\pi-5-keywords-by-reference-pali-vietnamese-plain.md).
- No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\: Grep only the specific files named here.

## Read first (binding)
- AI_translation\skills\rails-verse-translator.md; 0-INBOX\temp\pipeline\vietnamese-style.md.
- 0-INBOX\temp\pipeline\pi-5-vi-ai\rails\vi-rails-formulas.md (approved: the book frame, headings, debate frames, the rebuttal pentad, section labels, speaker notes, quote repair) and 0-INBOX\temp\pipeline\pi-5-vi-ai\rails\rails-coordinator-rules.md; the sample builder rails\build_rails_sample_vi.py (import READ-ONLY: `sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails"); import build_rails_sample_vi as S`; importing writes nothing); the approved sample chapter AI_translation\vietnamese\pi-5-vietnamese-plain-rails_split_chapters\1-puggalakatha.md.
- Locked termbase: AI_translation\vietnamese\pi-5-pali-vietnamese-termbase-plain.md and 0-INBOX\temp\pipeline\pi-5-vi-ai\termbase\APPROVED.md (saṃvara «sự thu thúc»; adhipati «yếu tố chủ đạo»; hetupaccaya «điều kiện gốc rễ»; aggo «bậc hàng đầu»; (a)kusala kāya- / vacī- / manokamma «nghiệp (bất) thiện bằng thân / lời nói / ý»; feelings sukha / dukkha «dễ chịu» / «khó chịu», kāyika / cetasika dukkha «nơi thân» / «trong tâm», «khổ đau» / «hạnh phúc» for suffering in general and happiness; niyata «cố định»; tiṭṭheyya / tiṭṭhanti «kéo dài», tiṭṭhati «duy trì», atthi «tồn tại»; no «một» before «bậc A-la-hán» where the Pāli has no numeral; names Sê-ni-gia, Sô-ma, Diêm-ma, Tu-bạt-đà-la; pariyāpanna «nằm trong»; kāraṇika «người thi hành hình phạt» / «người huấn luyện»), plus the pi-1 … pi-4 APPROVED.md. Terms in citation form; add or drop «các» / «những», «có», «là», tense words as grammar needs; never swap in a synonym. If no sense fits, use the closest sibling entry and REPORT it. Kathā names: from the termbase (the headword of the kathā), «Bàn về …».
- pi-1 … pi-4 Vietnamese rails for identical Pāli (AI_translation\vietnamese\pi-N-vietnamese-plain-rails_split_chapters\; rails\find_pi1234r_vi.py prints the line for a Pāli pattern).
- Meaning and layout only: AI_translation\russian\pi-5-russian-plain-rails_split_chapters\<ch>.md, AI_translation\english\pi-5-english-plain.md (grep by block ID); 0-INBOX\temp\pipeline\pi-5-ru\ru-rails-formulas.md; the commentary 1-SOURCES\Commentaries\pi-kathavatthu-atthakatha.md (Pāli; allowed).

## Source and output
- Source: AI_translation\pali\pi-5_split_chapters\<ch>.md. Output: AI_translation\vietnamese\pi-5-vietnamese-plain-rails_split_chapters\<ch>.md.
- Build it with rails\build_rails_<N>_vi.py from fixed strings (importing S), so every repeat is byte-identical; the builder asserts every (pi-N) string it uses still occurs in those rails, and runs S's per-line dash / quote / NFC checks.
- New recurring strings (similes, verses, frames not in the formulas file, kathā names): notes-rails-<N>.md, "Pāli = tiếng Việt" per line.

## Rules
- Block IDs exact; headings keep their #-level; each segment has the source's number of non-empty lines; one blank line between segments.
- DASH RULE: "–" only where the Pāli has one, same count per line; no ":-". "…pe…" → "…" (never «….»). Questions end with "?" with a Vietnamese question word; keep the Pāli's own punctuation where it differs and report it. Quotes “…” / ‘…’ as the Pāli nests them; repair the garbled close "’ → ’” as the sample does. Variant brackets as the sample.
- Translate the Pāli as written: no emendations; add nothing that is not in the Pāli and drop nothing that is (a repeated word stays); never merge sentences; only plain spelling slips and missing punctuation may be rendered as meant. Report suspected slips.
- Identical Pāli = identical Vietnamese, within your chapter, with the sample, with other finished chapters and with pi-1 … pi-4 rails (unless the termbase decides otherwise).
- One Pāli word that the argument turns on keeps one Vietnamese word throughout (do not split it by context).
- Similes and verses: each Pāli line one Vietnamese line.
- Readability for a plain reader; avoid «là là», «được được».

## Verify (all must pass)
```
python -I -X utf8 -B 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-5_split_chapters AI_translation\vietnamese\pi-5-vietnamese-plain-rails_split_chapters <ch>.md
python -I -X utf8 -B 0-INBOX\temp\pipeline\dashcheck.py <pali ch> <vietnamese ch>
python -I -X utf8 -B 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py <pali ch> <vietnamese ch>
```
Termbase adherence: copy your chapter (Write tool) into rails\adh-<N>\ and run `python -I -X utf8 -B 0-INBOX\temp\pipeline\termbase_adherence_vi.py AI_translation\pali\pi-5-keywords-by-reference-pali-plain.md AI_translation\vietnamese\pi-5-pali-vietnamese-termbase-plain.md 0-INBOX\temp\pipeline\pi-5-vi-ai\rails\adh-<N>`; read misses with judgement and fix genuine ones.

## Report (under 300 words, as text)
Checks, segment count, adherence; new strings (notes file); reuse from the sample / pi-1 … pi-4 / other chapters; termbase misfits and gaps; unsure Pāli or slips.
