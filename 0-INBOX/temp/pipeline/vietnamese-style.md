# Vietnamese plain translations: shared style rules (pi-1 onward)

Written 2026-11-17 for pi-1, modelled on russian-style.md and hindi-style.md. Every Vietnamese brief points here. The "Core terms" section is filled in from the approved pi-1 sample and grows book by book.

Audience: AI_translation\audience_profile\plain.md. Readers have little or no Buddhist background. Write clear, modern, natural Vietnamese. Minor clarification through wording is OK, but add nothing that is absent from the source. Priority: understanding > accuracy > readability > consistency.

## Reference translation: OFF LIMITS for translators
A copyrighted human Vietnamese translation (Tịnh Sự) is in the vault for REVIEW ONLY. Translation, mapping, senses, termbase and rails agents must NEVER open, grep or search:
- 1-SOURCES\Translations\Vietnamese\vi-*.md
- 0-INBOX\raw-data\vi-*
- 0-INBOX\temp\pipeline\pi-*-vi\ (the alignment folders, e.g. pi-1-vi, pi-2-vi, pi-3-4-vi), pi-1-th-vi\, vi-tools\
Our scratch lives in 0-INBOX\temp\pipeline\pi-N-vi-ai\ instead. Do not look up Vietnamese translations of the Abhidhamma on the web either. Our wording must be our own.

## Language and vocabulary
- Modern standard Vietnamese in a plain register, full diacritics, Unicode NFC.
- **Technical terms:** translate the concept into words a lay Vietnamese reader understands. Prefer common words, including everyday Sino-Vietnamese words (tâm, trí tuệ, chánh niệm, thiền định …), over specialist Hán-Việt jargon that only trained Buddhists know. No bare transliterations of opaque Pāli terms (khandha, āyatana, dhātu …). Established Vietnamese Buddhist words stay: Đức Phật, Đức Thế Tôn, A-la-hán, Niết-bàn, tỳ-khưu.
- **Book titles:** the Vietnamese name only, no Pāli name and no bracketed gloss. Mid-sentence, put the title in “…”. Citation brackets such as [Puggalapaññatti 131] stay as references. Frontmatter `title:` uses a normal hyphen: `<Vietnamese title> - tiếng Việt phổ thông`.
- Keep the chosen word for a term consistent. Natural Vietnamese word order and classifiers (các, những, sự, niềm, trạng thái …) where Vietnamese needs them, applied the same way every time a formula repeats.

## Typography
- Statements end with ".". Questions end with "?" and are phrased with a Vietnamese question word (gì, nào, bao nhiêu, có … không …).
- Quotes: “…” outer, ‘…’ nested. No space before . , ; : ? !
- **DASH RULE (user, strict):** "–" or "—" appears ONLY where the Pāli has "–" or "—", at the same spot and with the same count on every line. Never add a dash anywhere else. Use "là", ":", a comma or a reordered sentence instead. No ":-".
- "…pe…" becomes "…" at the same spot.
- **Digits:** where the Pāli has digits, e.g. "(1)", keep them. Numbers written as Pāli words become Vietnamese words.
- **Variant brackets:** keep the sigla and the variant's Pāli, translate the label:
  - "[dị bản (Sī., Syā.): …]" when a word differs;
  - "[khác chính tả (Syā.): …]" for spelling-only differences.
- Translate editorial notes in square brackets.

## Structure (hard rules)
- Every block ID stays exactly as in the source, at the end of the last line of its segment, in the same order.
- Headings keep their #-level.
- Each segment has exactly the source's number of non-empty lines, one blank line between segments, no double blank lines, no CR characters.
- Identical Pāli formulas get identical Vietnamese. Use a builder script with fixed formula strings.
- Translate FROM THE PĀLI. The English, Hindi and Russian outputs and their builders are a cross-check of meaning and structure only.
- Translate the Pāli as written: no emendations of apparent slips; only plain spelling slips may be rendered as meant. Report suspected slips.
- Never write "seed" or "unseeded".

## Lessons from the earlier reviews (binding, all languages)
- abyākata = "ethically indeterminate" (never a word meaning just "neutral"). vipākābyākata / kiriyābyākata keep that word plus "result of action" / "functional".
- Keep these pairs distinct, one word each, never swapped: vicikicchā vs kaṅkhā; mettā vs abyāpāda; kukkucca vs uddhacca; vīriya vs padhāna / vāyāma.
- samudaya = arising. yoni (mode of birth) is distinct from saṃsāra (the round of rebirths).
- āsavānaṃ khaya = destruction (not "exhaustion") of the āsavas.
- arahatta = the state of an arahant.
- mātikā = "matrix" in English (never "outline"); choose a Vietnamese word with that meaning (a framework list of headings), not "summary" or "outline".

## Core terms (cross-book)
APPROVED 2026-11-17 with the pi-1 sample: the list is 0-INBOX\temp\pipeline\pi-1-vi-ai\vi-core-terms.md (62 entries; binding for all seven books). Highlights: dhamma = hiện tượng (the Teaching = Giáo Pháp); mātikā = ma trận; khandha = khối; āyatana = lĩnh vực nhận biết; dhātu = yếu tố; citta = tâm; viññāṇa = thức; vedanā = cảm giác; saññā = tri giác; cetanā = chủ ý; kusala / akusala / abyākata = thiện / bất thiện / không xác định về mặt đạo đức; vitakka / vicāra = sự hướng tâm / sự duy trì tâm; samādhi = định tâm; jhāna = tầng thiền; vīriya = tinh tấn vs vāyāma / padhāna = nỗ lực; **sati = sự tỉnh thức** (satindriya = năng lực tỉnh thức, sammāsati = tỉnh thức đúng đắn, micchāsati = tỉnh thức sai lầm; user decision 2026-11-17, never «chánh niệm»). Book title pi-1: «Liệt kê các hiện tượng».
Items covered by the list: dhamma (phenomenon / the Teaching), khandha, āyatana, dhātu, sacca, indriya, rūpa (matter / visible object), citta, cetasika, viññāṇa, vedanā, saññā, cetanā, phassa, manasikāra, saddhā, vīriya, sati, samādhi, paññā, jhāna, vitakka, vicāra, pīti, sukha, upekkhā, kusala / akusala / abyākata, hetu, āsava, saṃyojana, gantha, ogha, yoga, nīvaraṇa, parāmāsa, upādāna, kilesa, lobha, dosa, moha, avijjā, taṇhā, diṭṭhi, māna, hiri / ottappa, lokiya / lokuttara, ariya, magga / phala, sotāpanna, arahant, nibbāna, bhagavā, bhikkhu, puggala, saṅkhāra, asaṅkhata, paṭiccasamuppāda, kappa.

## Verify (must pass)
```
python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py <pali_split_dir> <vietnamese_split_dir> <ch>.md
python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py <pali_file> <vietnamese_file>
```
check_chapter_ids prints OK; dashcheck shows equal line counts and 0 dash mismatches. For a partial sample, compare against the same Pāli lines. Also check: no "—", no Latin words outside variant brackets and citations, no double blank lines, no CR, text is NFC.
