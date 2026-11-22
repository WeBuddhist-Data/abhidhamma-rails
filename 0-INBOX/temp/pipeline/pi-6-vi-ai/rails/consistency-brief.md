# Brief: pi-6 Vietnamese rails CONSISTENCY PASS (coordinator-delegated, 2026-11-22)

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at full paths; never write a file from PowerShell, not even a scratch file), PowerShell for commands, `python -I -X utf8 -B`. LF line endings: open(..., "w", encoding="utf-8", newline="\n").
- All 43 rails chapters + preamble are finished in AI_translation\vietnamese\pi-6-vietnamese-plain-rails_split_chapters\ and pass the checks. They were built by importable builders (rails\build_rails_<N>_vi.py) from shared frames, so most identical Pāli already reads identically. Your job: find what still differs, make identical Pāli read identically across the chapters by the precedence below, and settle the known clashes, WITHOUT changing anything else.
- Write ONLY: 0-INBOX\temp\pipeline\pi-6-vi-ai\rails\consistency_find_vi.py, consistency_fix_vi.py, rails\consistency\ (pre-fix copies of every chapter you change, made once, never overwritten), rails\consistency-log.tsv (file, block id, old → new, reason), rails\consistency-notes.md, rails\divergences-rails.md, and the changed chapter files. Do NOT edit any build_rails_*.py, notes-rails-*.md, vi-rails-formulas.md, rails-coordinator-rules.md, the termbase, or anything outside these. Never run git. Never write "seed". No web. No files at the repo root. Return your report as text.

## FORBIDDEN (strict)
- Never open, grep or search 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\.
- Never open this book's Vietnamese zero-shot or its tools: AI_translation\vietnamese\pi-6-vietnamese-plain-zeroshot_split_chapters\, pi-6-vietnamese-plain-zeroshot.md, and everything in 0-INBOX\temp\pipeline\pi-6-vi-ai\ outside termbase\ and rails\ (build_*_vi.py, notes-*.md, vi-zeroshot-*.md, zeroshot-coordinator-rules.md, harmonise*, backup-pre-harmonise\, divergences*.md, find_divergences_vi.py, vi_common.py, probe_*.py, senses\, mapper-vi\ except *.keywords.md); AI_translation\vietnamese\pi-6-keywords-by-reference-pali-vietnamese-plain.md.
- No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\: Grep only single named files (a Python script may read the files of the rails chapter folder and the Pāli split folder, which you need).

## Inputs (allowed)
- The rails chapters and the Pāli chapters (AI_translation\pali\pi-6_split_chapters\), rails\build_rails_<N>_vi.py and notes-rails-<N>.md (to see why a chapter chose a wording), vi-rails-formulas.md, rails-coordinator-rules.md (the decisions, chapter by chapter), 0-INBOX\temp\pipeline\pi-6-vi-ai\vi-rails-brief.md, the termbase AI_translation\vietnamese\pi-6-pali-vietnamese-termbase-plain.md and pi-6-vi-ai\termbase\APPROVED.md, pi-1 … pi-5 rails (rails\find_pi12345r_vi.py), the commentary 1-SOURCES\Commentaries\pi-yamaka-atthakatha.md (Pāli).
- A model for the finder: 0-INBOX\temp\pipeline\pi-5-vi-ai\rails\consistency_find_vi.py (copy and adapt; pi-5 files untouched). The Yamaka needs masking: member names (khandha, āyatana, dhātu, sacca, saṅkhāra, dhamma, indriya, anusaya), kusala / akusala / abyākata, verb tenses, labels; compare line, sentence and head skeletons (person / place heads before «thì»), editorial notes in brackets, headings and closing lines.

## Precedence (where identical Pāli differs)
1. The termbase / APPROVED.md (user-approved) and the user decisions in rails-coordinator-rules.md.
2. pi-1 … pi-5 rails wording for that Pāli.
3. The approved sample (preamble, 1-mulayamaka) and vi-rails-formulas.md.
4. The family setter (rails-coordinator-rules.md, "Family setters" and the "From rails …" sections), then the earlier chapter.
Only where the Pāli is truly identical AND the meaning in context is the same. Where the context differs (a different sense, e.g. bare dukkhaṃ «khổ đau» in Sacca vs «sự khó chịu» in Indriya; sabbattha «ở mọi nơi» vs «ở mọi chỗ»), keep both and list it as "kept: context". Sentence-initial capitals and the Pāli's own punctuation / spacing differences (e.g. "Āmantā …pe…." vs "Āmantā…pe….") are not divergences.

## Do NOT change (list them in the notes as "left for the user")
- Any termbase-vs-chapter wording (that goes to the termbase alignment later), including the Itaresaṃ / second-plane position forms («chúng sinh khác trong cõi …», «… và cõi X»).
- Lines translated as written where the Pāli looks inconsistent (^6-7-243, ^6-9-192, ^6-6-121, ^6-10-357, ^6-10-361 and the others in the notes): they go to the review.
- If a fix would change the approved sample (1-mulayamaka.md or preamble.md), do not change it: list it as "sample differs" with both wordings.

## Known clashes logged by the coordinator (check each; fix by the precedence or report why not)
1. Double «và» in nested runs of groups: «… cõi hình sắc và cõi không hình sắc và chúng sinh Vô Tưởng» (3-03), «… tầng thiền thứ hai và tầng thiền thứ ba và chúng sinh trong cõi dục lạc» (6-01), 3-06 ^6-3-221 … 226, 10-05, 10-06 ^6-10-301 / 302, 10-07, 10-11 ^6-10-396, and any others the finder shows. Rule (coordinator, from 3-02 / 3-03 / 10-07): a run of groups is joined flat, with commas and one «và» before the last item of the whole run («A, B, C và D»). Apply it wherever it does not create a misreading (e.g. a later group read as the object of «nhập»); where it would, keep the inner «và», join the outer item with «, và …» and list it. Count every change.
2. Editorial-note wording differs across chapters: «như đã được phân tích trong …, … cũng nên phân tích như vậy» (pi-2; 2-02, 5-02, 3-06) vs 4's «cũng nên được phân tích như vậy»; «Các câu hỏi về quá khứ … cả chiều thuận lẫn chiều nghịch» (5-02, 6-02) vs 3-05 «Câu hỏi về … theo chiều thuận và chiều nghịch»; sadisaṃ «giống nhau» / «giống như vậy»; vitthāretabbaṃ «nên được trình bày chi tiết». Unify identical Pāli by the precedence (pi-2 / pi-5 wording first).
3. Head parser disagreements the agents reported (10-03 vs 10-02 / 3-02 on plane-only heads; 9-01 vs 3-02 on nested runs): check that every identical Pāli head prints the same in every chapter.
4. Closing lines and headings: "<X>vāro." / "<X>vāro niṭṭhito." / "<X>vāre anulomaṃ / paṭilomaṃ." must read the same in every yamaka for the same Pāli (2-02 «Mục về sự chấm dứt.», 3-03 «Mục về sự sinh khởi.», 7-xx closers); yamaka closers from the sample.
5. Cut questions: «… không?» for a cut ending in "?", «…» for a cut without "?" (rules); check every chapter.
6. Plus every group in divergences-rails.md.

## Method
- consistency_find_vi.py writes rails\divergences-rails.md (before and after). consistency_fix_vi.py: explicit (file, old, new) replacements with asserted counts (as 0-INBOX\temp\pipeline\pi-5-vi-ai\rails\consistency_fix_vi.py does), working from the pre-fix copies in rails\consistency\, so it can be re-run safely; it rewrites consistency-log.tsv each run.
- After the fixes, run for EVERY chapter file (44 files incl. preamble):
  - `python -I -X utf8 -B 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-6_split_chapters AI_translation\vietnamese\pi-6-vietnamese-plain-rails_split_chapters <ch>.md`
  - `python -I -X utf8 -B 0-INBOX\temp\pipeline\dashcheck.py <pali ch> <vietnamese ch>`
  - `python -I -X utf8 -B 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py <pali ch> <vietnamese ch>`
  - termbase adherence over the whole folder: `python -I -X utf8 -B 0-INBOX\temp\pipeline\termbase_adherence_vi.py AI_translation\pali\pi-6-keywords-by-reference-pali-plain.md AI_translation\vietnamese\pi-6-pali-vietnamese-termbase-plain.md AI_translation\vietnamese\pi-6-vietnamese-plain-rails_split_chapters` (report the totals; misses should not rise).
  - and re-run consistency_find_vi.py; every remaining group must be explained in consistency-notes.md ("kept: context", "left for the user", "sample differs", "not identical Pāli", "false hit").
- Rules stay in force: no "—" / "–" beyond the Pāli's dashes; no «….», «:-», «là là», «được được», «chánh niệm», «vẫn đã», «Vào tâm mà ngay sau đó»; NFC; LF.

## Report (under 400 words, as text)
Number of changes per chapter; each known clash 1-6 and how it was settled; the finder's group counts before / after; what is left for the user; checks and adherence totals.
