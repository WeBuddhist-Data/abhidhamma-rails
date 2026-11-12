# Brief: independent review of the Hindi Vibhaṅga (pi-2)

You are an independent reviewer and a careful Pāli–Hindi bilingual checker. You are READ-ONLY: do not edit any translation file.
- Work in D:\Work\OpenPecha\abhidhamma-rails. It is a Windows machine: use the Read tool, and run python as `python -I -X utf8`.
- Put any helper scripts in 0-INBOX\temp\pipeline\pi-2-hi\review\, named after your part (review_<part>_*.py). Never create files at the repo root. Do not run git. Do not open the termbase, the keyword maps, the zero-shot Hindi or any notes or builders in 0-INBOX\temp\pipeline\pi-2-hi\rails\: the point is a reading that is not anchored on them.

## Inputs
- **Pāli:** AI_translation\pali\pi-2_split_chapters\<ch>.md
- **Hindi:** the same filenames in AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters\
- **Alignment:** segments align by the block ID at the end of each segment (e.g. ^2-112). Non-empty lines align one to one.
- **Optional reference** for hard readings: an independent English translation, AI_translation\english\pi-2-english-plain-zeroshot_split_chapters\<ch>.md (same segments; some lines may start with an old paragraph number, ignore it). The commentary in 1-SOURCES\Commentaries\ may also help for a hard reading. The Pāli is the authority.
- **Audience:** AI_translation\audience_profile\plain.md. The reader has no Buddhist background, so the Hindi must be clear, natural and modern, with nothing added.

## About the text
The Vibhaṅga analyses 18 topics (aggregates, sense bases, elements, truths, faculties, dependent origination, mindfulness, right efforts, bases of success, enlightenment factors, path factors, jhāna, the immeasurables, the precepts, analytical knowledges, knowledge, minor items, the heart of phenomena). Most chapters have three sections: by the discourses (उपदेशों के अनुसार विश्लेषण), by the Abhidhamma (अभिधम्म के अनुसार विश्लेषण) and question-and-answer (प्रश्नोत्तर), the last going through the Dhammasaṅgaṇī matrix (mātikā = «मूल सूची»; dhamma = «परिघटना» in this translation). The text is formulaic and abbreviates heavily with …pe…. Everything turns on:
- which item is meant: kusala / akusala / abyākata, sahetuka vs ahetuka vs hetu, sampayutta vs vippayutta, sāsava vs anāsava, sekkha vs asekkha, the sphere (kāma-, rūpa-, arūpa-avacara, lokuttara), past/future/present, internal/external;
- negations (na, no, a-, an-, neva … na) and "X ceva … no ca Y" polarity; siyā (कभी …) vs plain statements; na vattabbā (cannot be said) frames;
- numbers: the jhāna ordinals, the counts (eko, dve, pañca …), the N-fold groupings, the numbered lists of chapter 17 and 18;
- complete synonym strings: nothing dropped, nothing added, order kept;
- the dependent-origination links and their order (chapter 6), the paṭipadā (dukkha / sukha; dandha / khippa) and ārammaṇa permutations.

## Check every segment for

**1. CRITICAL: meaning errors**
- a wrong number or ordinal;
- wholesome and unwholesome swapped, conjoined and dissociated swapped, or a wrong triad or pair item;
- a negation lost or added; siyā lost or added;
- a wrong permutation or a wrong link;
- a synonym dropped or added in a string, or omitted or added content (beyond "…" for …pe…);
- content placed on the wrong ID.

**2. MAJOR**
- Hindi that is ungrammatical or misleading, so that a reader would likely misread it. This includes number and gender agreement with समूह, परिघटना, तत्व, क्षमता, इंद्रिय-क्षेत्र, अनुभूति, पहचान, मानसिक रचना, चेतना etc.
- The same Pāli formula, item or term rendered inconsistently within your part.

**3. MINOR**
- awkward wording or register, a word sitting next to its own repetition where the Pāli does not need it;
- Pāli left in Latin script outside variant brackets.

**Also check typography:**
- "–" only where the Pāli has "–" or "—", at the same spot, with the same count per line;
- statements end with «।»; quotes are “…”;
- no double blank lines.

## How to check
The text is extremely repetitive. Verify the first instance of each formula carefully, then scan later segments for deviations by script: compare numerals and ordinals, count comma-separated items in the synonym strings (Pāli space- or comma-separated against Hindi comma-separated), and compare polarity words line by line (na/no/a- against न/नहीं/रहित; siyā against कभी). Read chapter openings, headings and the non-formulaic passages closely. Do not flag a source slip as a Hindi error, but do mention source slips briefly.

## Report (concise; plain text, as your final message; you cannot write files)
- A table: ID | file | line (non-empty line number in the chapter) | severity | Pāli (short) | Hindi (short) | problem | suggested Hindi fix (the exact old → new string where possible).
- Then the counts per severity, the number of segments checked, and a one-paragraph overall judgement.
