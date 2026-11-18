# Brief: consistency (harmonise) pass, pi-1 Vietnamese plain zero-shot

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Write only in AI_translation\vietnamese\pi-1-vietnamese-plain-zeroshot_split_chapters\ (the 14 part files) and 0-INBOX\temp\pipeline\pi-1-vi-ai\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, never run git (not even git status), never write "seed". You cannot write report files for me: return your report as text.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\vi-*.md, 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\.

## Situation
Nine agents translated the 12 parts ONE AT A TIME, each importing the earlier builders (pi-1-vi-ai\build_*_vi.py) and keeping notes (pi-1-vi-ai\notes-*.md), so most shared strings are already identical. preamble.md, 1-matika.md and the first 122 non-empty lines of 2-01 (= pi-1-vi-ai\ch2-01-sample.md) are user-approved and must stay unchanged. Rules: 0-INBOX\temp\pipeline\vietnamese-style.md (dash rule, quotes, core terms, sati = «sự tỉnh thức»). The run log with every agent's choices and source slips: pi-1-vi-ai\agents-run.md.

## Method (as the Russian pi-1 pass)
Models (read them): 0-INBOX\temp\pipeline\pi-1-ru\harmonise-brief.md, pi-1-ru\harmonise_ru.py, pi-1-ru\find_divergences_ru.py.
- Write pi-1-vi-ai\find_divergences_vi.py: (a) group segments across all parts by their normalised Pāli (strip the ^id and variant brackets, collapse spaces) and list those where identical Pāli has different Vietnamese; (b) recurring Pāli terms and phrases with the Vietnamese each part uses (from the notes files, confirmed in the outputs): at least the jhāna formula, paṭipadā / abhiññā, adhipateyya, kasiṇa, the formless spheres, sasaṅkhāra, bhūmi (stage vs plane, see below), cittuppāda, ṭhapetvā frames, tadekaṭṭhā, kammassa katattā, sāta / asāta, viññatti, upacaya, santati, diṭṭhigata, the lobha / dosa / moha / diṭṭhi / vicikicchā / uddhacca / thina / middha / kukkucca / māna / issā / macchariya strings, the āsava / saṃyojana / gantha / ogha / yoga / nīvaraṇa / upādāna / kilesa group names, patiṭṭhāho, the bahūsu siglum. Write the result to pi-1-vi-ai\divergences.md (and keep a copy of the first run as divergences-pre.md).
- Write pi-1-vi-ai\harmonise_vi.py: fixed old → new strings applied to the Vietnamese part files, each rule touching only a Vietnamese line whose aligned Pāli line (non-empty line i ↔ non-empty line i) matches the rule's Pāli pattern (book-wide typography rules may skip the Pāli test). Back up the pre-pass files to pi-1-vi-ai\backup-pre-harmonise\ once (always start from the backup, so the script can be rerun), log every replacement to pi-1-vi-ai\harmonise-log.tsv (rule, part, line, old, new). Line counts, IDs, heading levels and dashes must not change. Support --dry.
- Do NOT rebuild with the builders (that would drop the pass); edit the outputs with the script. Note in pi-1-vi-ai\harmonise-notes.md which builder constants would need the same change.

## Decisions (coordinator)
1. **Doubled «là» in the 3-02/3-03 answer frame** (about 121 lines): «– đây là loại vật chất là lĩnh vực mắt.» reads clumsily. "idaṃ taṃ rūpaṃ P" = "this is that matter which is P". Replace the frame with ONE grammatical form with no doubled «là», e.g. «– vật chất này là lĩnh vực mắt.» / «– vật chất này thuộc về …» (i.e. «– vật chất này» + the 3-01 predicate unchanged). If you find a clearly better single form, use it and say why. Same frame everywhere it occurs; the 3-01 predicates themselves stay byte-identical.
2. **Four dots:** where the Pāli has "…pe…." (or "…pe… ." etc.) the Vietnamese must not end with «….»; write «…» (the Russian review decision for the same case). Apply book-wide outside the approved sample/matrix, and report the count. Check ^1-337 and ^1-363 in 2-03 first.
3. **«Tikaṃ.»** is «Phân loại theo nhóm ba.» in 3-01 and «Các bộ ba.» in 4-01. Look at what each closes in the Pāli. If both close the same kind of unit, use one form; if they genuinely differ, keep both and give the reason. Apply the same check to the other count words (Dukaṃ, Ekakaṃ …).
4. **bhūmi:** «giai đoạn» for the path stages (2-03 paṭhamāya bhūmiyā pattiyā) and «cõi» for the planes (ch5 catūsu bhūmīsu) are two senses; keep both. «Ở cấp độ có X» (4-01/4-02 X-bhūmiyaṃ) is a third sense; keep it consistent between 4-01, 4-02/4-03 and ch5.
5. **sukhabhūmiyaṃ** split («có cảm giác dễ chịu» for triad 2, «có hạnh phúc» for triad 7) is deliberate: keep.
6. **akakkhaḷatā «sự không thô cứng»** is in the approved sample: keep; kakkhaḷa «cứng» stays in ch3.
7. **sammappadhāna = sammāvāyāma = «nỗ lực đúng đắn»** (user-approved pairing): keep.
8. For every other divergence of identical Pāli: the terms file and the approved sample win, then the earlier part in book order (it was built first and later parts imported it), then the part with more occurrences.
9. Do not change: renderings that differ because the Pāli differs; source slips translated as written (agents-run.md lists them); deliberate departures recorded in the notes.

## Apply and verify
Run harmonise_vi.py. Then run find_divergences_vi.py again: segment-level divergences (a) must be 0 except where the Pāli differs only inside variant brackets or the text was rightly kept as written (list those). For every part:
- `python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-1_split_chapters AI_translation\vietnamese\pi-1-vietnamese-plain-zeroshot_split_chapters <part>.md` (OK)
- `python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py <pali> <vietnamese>` (0 mismatches, 0 extra)
- the per-part verify_vi_*.py scripts (OK; if a script encodes the old frame or «….», note it rather than editing the old checker, and write verify_vi_all.py that checks all 14 files).
- 1-matika.md, preamble.md and the first 122 non-empty lines of 2-01 unchanged vs the backup.
Also grep the whole set for: «—», «:-», «chánh niệm», «seed», «….», «loại vật chất là», Latin letters outside [..] brackets, CR, double blank lines, non-NFC text.

## Final report (under 450 words, as text)
Rules applied (count per rule and part), the frame chosen under 1, the outcome of 3, other divergences found and how they were settled, divergences left on purpose, check results, and anything that needs the user's eye.
