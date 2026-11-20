# Brief: consistency (harmonise) pass, pi-2 Vietnamese plain zero-shot

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at full paths; never write files from PowerShell), PowerShell for commands, `python -I -X utf8`. Write only in AI_translation\vietnamese\pi-2-vietnamese-plain-zeroshot_split_chapters\ (the 19 part files) and 0-INBOX\temp\pipeline\pi-2-vi-ai\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit the builders, never run git (not even git status), never write "seed". You cannot write report files for me: return your report as text.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\.

## Situation
Ten agents translated the 18 chapters one after another, each importing the earlier builders (0-INBOX\temp\pipeline\pi-2-vi-ai\build_*_vi.py, notes-*.md, vi-zeroshot-terms.md). preamble.md and the first 77 non-empty lines of 1-khandhavibhango.md (= pi-2-vi-ai\ch1-sample.md) are user-approved and stay unchanged. Where the same Pāli occurs in different chapters, or in pi-1 (whose Vietnamese is final and reviewed: AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters\), the Vietnamese must now be identical, and one Pāli term in one sense gets one Vietnamese term. Rules: 0-INBOX\temp\pipeline\vietnamese-style.md. The run log with every agent's choices and source slips: pi-2-vi-ai\agents-run.md (read the lines marked "FOR THE HARMONISE PASS" and "FOR THE REVIEW").

## Method (as the pi-1 pass)
Models: 0-INBOX\temp\pipeline\pi-1-vi-ai\harmonise_vi.py and find_divergences_vi.py (read them).
Write pi-2-vi-ai\harmonise_vi.py: fixed old → new strings applied to the Vietnamese chapter files, each rule touching only a Vietnamese line whose aligned Pāli line (non-empty line i ↔ i) matches the rule's Pāli pattern (or a listed block ID). Back up the pre-pass files to pi-2-vi-ai\backup-pre-harmonise\ once and always start from the backup (rerunnable); log every replacement to pi-2-vi-ai\harmonise-log.tsv (rule, part, line, old, new). Line counts, IDs, heading levels and dashes must not change. Support --dry. Do NOT rebuild with the builders; note in pi-2-vi-ai\harmonise-notes.md which builder constants would need the same change.

## Step 1: find divergences
Write pi-2-vi-ai\find_divergences_vi.py:
- (a) whole segments across all 18 chapters grouped by normalised Pāli (strip ^id and variant brackets, collapse spaces, drop the space before punctuation): identical Pāli, different Vietnamese → list;
- (b) the same for pi-2 segments whose Pāli is identical to a pi-1 segment (pi-1 Vietnamese wins);
- (c) recurring Pāli terms and phrases across chapters (collect from the notes files and builders, confirm in the outputs): at least the realm and god names, kāmesumicchācāra, veramaṇī, the vīriya / paññā / sati / samādhi strings, the jhāna formula pieces, the lokuttara openings, the question-section predicates, «đó được gọi là …», «không nên nói …», the counted names, sajjha / rajata, dhamme ñāṇaṃ, vatthu, kāmadhātu, Catukkaṃ / Pañcakaṃ, abhiññeyya.
Write the result to pi-2-vi-ai\divergences.md (keep a copy of the first run as divergences-pre.md).

## Step 2: decisions (coordinator)
1. **Source as written (user rule).** Only plain spelling slips and missing punctuation are rendered as meant; a wrong mark, a doubled or missing negation, or a one-letter slip that changes the meaning stays as written.
   - ^2-171 (3-dhatuvibhango) «kilesasampayuttā ceva no ca na kilesā» was rendered as meant: render the doubled negation as written (literally, keeping both negations), and say how.
   - ^2-1014 and the ^2-1023 verse (18): questions that the Pāli closes with «.» were given «?»: restore «.» (as pi-1 ^1-473 / ^1-1478).
   - ^2-809 (16) «atthato» read as attato: leave it as it is for now; the user decides at the review. List it.
2. **The vīriya strings:** check every vīriya (and sati / samādhi / paññā) string in the book against its own Pāli line: an item in the Vietnamese that the Pāli line lacks, or the reverse, is an error (the Russian pass found «sammāvāyāmo» added at ^2-220). Fix what you find.
3. **Catukkaṃ / Pañcakaṃ:** «Phân loại theo nhóm bốn / năm» (ch16, pi-1) vs «Phương pháp chia bốn / chia năm» (ch12). Look at what each closes in the Pāli. If they close the same kind of unit, use one form; if they genuinely differ (a count of items vs the fourfold / fivefold jhāna method), keep both and give the reason.
4. **kāmadhātu:** «yếu tố dục lạc» (ch3, the element of sensual desire beside byāpāda- / vihiṃsādhātu) vs «cõi dục lạc» (ch18, the plane): two senses, keep both; list it.
5. **vatthu:** «chỗ dựa» (ch16 ñāṇavatthu, pi-1) vs «căn cứ» (ch3 āghātavatthu): check pi-1's rendering of āghātavatthu (pi-1 4-02 and the kilesavatthu lists) and follow pi-1 for each compound.
6. **dhamme ñāṇaṃ:** «sự hiểu biết về Giáo Pháp» (path-knowledge catukka, ch16) vs «về các hiện tượng» (paṭisambhidā formula, ch15/16) differ in meaning: keep both; list it. ^2-724 «dhammaṃ jānāti» «biết Giáo Pháp» inside the paṭisambhidā passage: check against the commentary (1-SOURCES\Commentaries\, the Vibhaṅga aṭṭhakathā) and choose; report.
7. **sajjha / rajata** (both «bạc» in ch3): keep them apart where they stand in the same list; check the commentary and pi-1's rendering of the same list, and choose; report the choice.
8. **kāmesumicchācāra**: one wording everywhere (ch4, 11, 14, 17). **The gods / realm names**: one wording within pi-2, pi-1's where pi-1 has the name (4-02/4-03: «Sắc Cứu Cánh», «cõi Phạm Thiên», «Tha Hóa Tự Tại» …); list any pi-2 name pi-1 lacks.
9. **Quotes around awakening-factor names** used as question topics («Ở đây, “chi phần giác ngộ là sự tỉnh thức” là gì?», ch4/ch10): keep, but make it uniform wherever such a name is a question topic or subject; list the count.
10. For every other divergence of identical Pāli: pi-1 Vietnamese wins; then the approved sample and vi-zeroshot-terms.md; then the chapter with more occurrences.
11. Do not change: the approved sample; renderings that differ because the Pāli differs; source slips translated as written (each chapter's notes file lists them); deliberate context splits recorded in the notes (e.g. vossagga «sự buông xả» (ch10) vs «sự buông lơi» (pamāda list, ch17); viharati «sống» vs «an trú»; Kāyaviññāṇadhātu sukhasahagata «có sự dễ chịu đi kèm» by the user's body rule).

## Step 3: apply and verify
Run harmonise_vi.py, then find_divergences_vi.py again: (a) and (b) must be 0 except where the Pāli differs only inside variant brackets or the text was rightly kept as written (list those). For every chapter:
- `python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-2_split_chapters AI_translation\vietnamese\pi-2-vietnamese-plain-zeroshot_split_chapters <ch>.md` (OK)
- `python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py <pali> <vietnamese>` (0 mismatches, 0 extra)
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py <pali> <vietnamese> …` (OK)
- preamble.md and the first 77 non-empty lines of 1-khandhavibhango.md unchanged vs the backup.
Also grep the whole set for: «—», «:-», «chánh niệm», «seed», «….», Latin outside [..], CR, double blank lines, non-NFC text.

## Final report (under 450 words, as text)
Rules applied (count per rule and chapter), the choices you made under 3, 5, 6, 7 and 10 with reasons, divergences left on purpose, cross-book differences for the user, check results.
