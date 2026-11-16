# Brief: independent review of the Marathi Vibhaṅga (pi-2, «विश्लेषण»)

You are an independent reviewer and a careful Pāli–Marathi bilingual checker. You are READ-ONLY: do not create, edit or delete any file.
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Use the Read tool, Grep/Glob and Bash.
- Run any check scripts inline only, as `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 - <<'EOF' … EOF` heredocs, without writing files (plain python3 is too old).
- Do NOT open the Marathi termbase, the senses or keyword files, the zero-shot Marathi, or any notes or scripts in 0-INBOX: review the translation against the Pāli on its own.

## Inputs
- **Pāli:** AI_translation/pali/pi-2_split_chapters/<ch>.md
- **Marathi:** the same filenames in AI_translation/marathi/pi-2-marathi-plain-rails_split_chapters/
- **Alignment:** segments align by the block ID at the end of each segment (e.g. ^2-112), and lines align one to one within a segment.
- **Optional reference** for hard readings: the English zero-shot AI_translation/english/pi-2-english-plain-rails_split_chapters/<same file>. The Pāli is the authority.
- **Audience:** AI_translation/audience_profile/plain.md. The reader has no Buddhist background, so the Marathi must be clear, natural, modern standard Marathi, with nothing added.

## About the text
The Vibhaṅga analyses one topic per chapter (khandha, āyatana, dhātu, sacca, indriya, paṭiccasamuppāda, satipaṭṭhāna, sammappadhāna, iddhipāda, bojjhaṅga, maggaṅga, jhāna, appamaññā, sikkhāpada, paṭisambhidā, ñāṇa, khuddakavatthu, dhammahadaya), mostly in three parts: the suttanta analysis, the abhidhamma analysis (often quoting the Dhammasaṅgaṇī definitions and synonym lists word for word) and the questions (pañhāpucchaka: the mātikā triads / dyads applied to the topic). Everything turns on:
- the synonym lists and definitions: each Pāli item its own Marathi, order and count kept; the same Pāli synonym the same Marathi everywhere;
- the eleven qualifiers (past / future / present, internal / external, gross / subtle, inferior / superior, far / near), the twelve links of dependent origination, the four truths, the faculties, the jhāna formulas;
- polarity (a-/an-/na-/no- terms, «na vattabbā», «siyā»), numbers (ch16's knowledge by one … ten, ch18's life spans and planes), the mātikā terms.
- Read closely also ch12-14's lines where Pāli and Marathi negation or number counts differ (the consistency pass left 65 such lines unverified).

## Known conventions you should NOT report as errors
- «…pe…» / «…Pe…» become one «…». Statements end with «.», never «।». Quotes “…” / ‘…’.
- Suttanta frame «त्यांपैकी X म्हणजे काय? … – याला X म्हणतात»; the Dhammasaṅgaṇī definition frame as in pi-1 «त्या वेळी कोणता X असतो? … – हा त्या वेळी असणारा X आहे.»; pañhāpucchaka siyā = «कधी …», na vattabbā = «… म्हणता येत नाही».
- Factor names: phassa संपर्क, vedanā अनुभूती, saññā ओळख, cetanā इरादा, citta मन (bare mano in the citta list = अंतःकरण), vitakka आरंभिक विचार, vicāra सततचा विचार, pīti उल्हास, sukha सुख, ekaggatā मनाची एकाग्रता; kāya- in kāyapassaddhi … = «मनाच्या सहचरांची» (the mental body); thina / middha आळस / सुस्ती; rāga आसक्ती; bhāveti «साधना करतो»; paṭipadā वाटचाल; bhūmi टप्पा (stage) / स्तर (plane); jarā वार्धक्य; dhātu as element तत्त्व, as sphere लोक; paccaya in the dependent-origination chain «…मुळे»; the fourth truth «दुःखाच्या अंताकडे नेणारा मार्ग».
- kusala / akusala / abyākata = हितकारक / हानिकारक / नैतिकदृष्ट्या अनिर्धारित; dyad terms «स्वतः X असलेला / नसलेला», «Xचा विषय होणारा»; joins inside one term with «व».
- Variant brackets «[पाठभेद (Syā.): …]», «[लेखनभेद (…): …]». Source slips are translated as written and are known; report one only if the Marathi is wrong for the intended reading.

## Check every segment for
**1. CRITICAL: meaning errors** — polarity (a negation lost or added), a wrong factor / term, a synonym list item lost, added, swapped or merged, a wrong number, omitted or added content, content on the wrong ID.
**2. MAJOR** — Marathi that is ungrammatical or misleading so a reader would likely misread it; the same Pāli formula or synonym rendered inconsistently within your part.
**3. MINOR** — awkward wording, a heavy word where a plain one exists, Pāli left in Latin script outside variant brackets.
**Also typography:** dashes «–»/«—» only where the Pāli has them, same count per line; no «।»; no double blank lines.

## How to check
Check BY SCRIPT, per line: numbers, dash counts, the synonym count per definition line (Pāli items vs Marathi items), polarity (Pāli negations vs Marathi न / नसलेला / नाही), and that each recurring Pāli synonym always gets the same Marathi. Use the results to find lines to read closely; then read closely every chapter opening, every definition list, and every flagged line, spread over all your chapters.

## Report (concise, as your final message: you cannot write files)
- A table: ID | file | severity | Pāli (short) | Marathi (short) | problem | suggested Marathi fix (the full corrected Marathi phrase).
- One row per recurring pattern, with the IDs or the count.
- Then the counts per severity, segments checked, script results, and a one-paragraph overall judgement.
