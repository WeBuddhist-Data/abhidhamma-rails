# Brief: consistency (harmonise) pass, pi-1 Russian plain zero-shot

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Write only in AI_translation\russian\pi-1-russian-plain-zeroshot_split_chapters\ (the 14 part files) and 0-INBOX\temp\pipeline\pi-1-ru\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not run git, never write "seed". You cannot write report files for me: return your report as text.

## Situation
Nine agents translated the 12 parts in parallel from one term list (pi-1-ru\ru-zeroshot-terms.md), each with a builder script (pi-1-ru\build_*_ru.py) and a notes file (pi-1-ru\notes-*.md). preamble.md, 1-matika.md and the first 122 non-empty lines of 2-01 (= pi-1-ru\ch2-01-sample.md) are user-approved and must stay unchanged.
Where the same Pāli occurs in different parts, the Russian must now be identical, and one Pāli term gets one Russian term. Rules: russian-style.md (dash rule, «…»/„…“, no «ли»).

## Method (as the English and Hindi pi-1 passes)
Models (read them): pi-1-ru\ref\en_harmonise.py, ref\hi_harmonise_hi.py, ref\hi_find_divergences_hi.py.
Write pi-1-ru\harmonise_ru.py: fixed old → new strings applied to the Russian part files, each rule touching only a Russian line whose aligned Pāli line (non-empty line i ↔ non-empty line i) matches the rule's Pāli pattern. Back up the pre-pass files to pi-1-ru\backup-pre-harmonise\ once (always start from the backup, so the script can be rerun), log every replacement to pi-1-ru\harmonise-log.tsv (rule, part, line, old, new). Line counts, IDs, heading levels and dashes must not change. Support --dry.
Do NOT rebuild with the builders (that would drop the pass); edit the outputs with the script. Note in pi-1-ru\harmonise-notes.md which builder constants would need the same change.

## Step 1: find divergences systematically
Write pi-1-ru\find_divergences_ru.py:
- (a) Whole segments: group segments across all parts by their Pāli (normalised: strip the ^id, variant brackets, collapse spaces); where the Pāli is identical but the Russian differs, list them.
- (b) Recurring Pāli terms and phrases: collect the Russian each part uses for each (from the notes files and builders, confirmed in the outputs). At least: the jhāna formula (vivicceva kāmehi, vivicca akusalehi dhammehi, savitakkaṃ savicāraṃ vivekajaṃ, vitakkavicārānaṃ vūpasamā, ajjhattaṃ sampasādanaṃ, pītiyā ca virāgā, upekkhako ca viharati sato ca sampajāno, sukhassa ca pahānā, upasampajja viharati, the subject «человек»), paṭipadā / abhiññā, adhipateyya, kasiṇa, āruppa spheres, sasaṅkhāra, bhūmi, cittuppāda, the counting lines («И в это время есть …»), ṭhapetvā frames, tadekaṭṭhā, kammassa katattā, sāta / asāta, viññatti, upacaya, santati, kakkhaḷa, diṭṭhigata, micchādiṭṭhi, sakkāyadiṭṭhi, sīlabbataparāmāsa, the lobha / dosa / moha / diṭṭhi / vicikicchā / uddhacca / thina / middha / kukkucca / māna / issā / macchariya strings, the āsava / saṃyojana / gantha / ogha / yoga / nīvaraṇa / upādāna / kilesa group names, sārāga, the bahūsu siglum, patiṭṭhāho.
Write the result to pi-1-ru\divergences.md.

## Step 2: decisions
Fixed by the coordinator (apply everywhere the Pāli has the item):
1. **Jhāna formula and its frame: the 2-01/2-02 wording wins** (it comes first in the book and 2-04 already follows it): vivicceva kāmehi = «полностью уединившись от чувственных удовольствий»; vitakkavicārānaṃ vūpasamā = «с затиханием направленной мысли и удержания мысли» («успокоение» is reserved for samatha); upasampajja viharati and the clause order as in 2-01/2-02; sukhassa ca pahānā = «с устранением приятного»; the human subject «человек» (not the impersonal plural). Align 2-03 and 2-05 (and any other part) to it, including the lokuttara opening clauses that 2-05 copied from 2-03, keeping their own lokuttara-only wording where 2-01/2-02 has no equivalent.
2. **paṭipadā / abhiññā:** «с трудным / лёгким способом практики», «медленным / быстрым высшим знанием» (2-01/2-02).
3. **vīmaṃsā = «пытливость»** everywhere (adhipati «при преобладании пытливости»), distinct from vicaya = исследование.
4. **sasaṅkhārena = «с побуждением»** (all parts already; confirm).
5. **asāta:** ONE word in every string. Check the approved sample strings first (they win); if the sample has neither, use «безотрадный» and the matching «ни отрадно, ни безотрадно» form.
6. **viññatti = «внешнее выражение»**: kāyaviññatti / vacīviññatti = «телесное / речевое внешнее выражение» (3-01/3-02/3-03, pi-5). Align ch5 («сообщение») and 4-02/4-03 («выражение»).
7. **upacaya = «рост»** (ch3); align ch5 («нарастание»). santati = «непрерывность».
8. **diṭṭhigata(sampayutta) = «(связанный с) приверженностью воззрениям»** (2-04); align ch5 where it has «ложное воззрение» for diṭṭhigata. micchādiṭṭhi stays «ложное воззрение».
9. **patiṭṭhāho = «закрепление»** everywhere (as written, like 2-04 ^1-381 and the English "fixation"; user rule: translate the source as written). Align 4-01 (^1-1124, ^1-1143, ^1-1144, «цепкость»), keeping the variant brackets where the Pāli has them.
10. **kammassa katattā:** one form; prefer the one with more occurrences, inflected only where the grammar of the line forces it.
11. **cittuppāda = «вид ума»** in ch5 (keep; matches the approved heading). Report every other place cittuppāda occurs and what it has.
12. **Typo:** 2-02 «сферыбесконечного» and any other missing space between «сферы» and the next word.
13. **sārāga** next to rāga: one rendering in 4-01 and 4-02 (choose «сильная страсть» or «пристрастие»).
14. **bahūsu siglum** = «(во многих изданиях)» everywhere.
15. For every other divergence of identical Pāli: the terms file and the approved sample win, then an earlier Russian book (AI_translation\russian\pi-3/4/5 termbases), then the part with more occurrences. Between 4-01 and 4-02/4-03, prefer 4-01 unless 4-02/4-03 matches the terms file or an earlier book and 4-01 does not.
16. Do not change: the approved sample and matrix; renderings that differ because the Pāli differs (e.g. rūpataṇhā's two senses in 4-02, hetū paccayā «причины и условия»); source slips translated as written; deliberate departures recorded in the notes. Do not change sammappadhāna («правильное усилие», user-approved pairing of padhāna / vāyāma = усилие).

## Step 3: apply and verify
Run harmonise_ru.py. Then run find_divergences_ru.py again: segment-level divergences (a) must be 0 except where the Pāli differs only inside variant brackets or the text was rightly kept as written (list those). For every part:
- `python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-1_split_chapters AI_translation\russian\pi-1-russian-plain-zeroshot_split_chapters <part>.md` (OK)
- `python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py <pali> <russian>` (0 mismatches, 0 extra)
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-ru\verify_ru.py <pali> <russian> …` (OK)
- 1-matika.md, preamble.md and the first 122 non-empty lines of 2-01 unchanged vs the backup.
Also grep the whole set for: «—», «:-», «ли» as a word, «seed», Latin letters outside [..] brackets, «сферыбесконечн», «сообщение», «нарастание», «цепкость», «отстранившись от чувственных», «с успокоением направленной».

## Final report (under 450 words, as text)
Rules applied (count per rule and part), the choices you made under 5/10/13/15 with reasons, divergences left on purpose, check results, and anything that needs the user's eye.
