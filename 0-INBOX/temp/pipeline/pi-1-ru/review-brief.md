# Brief: independent review of the Russian Dhammasaṅgaṇī (pi-1), plain rails translation

You are an independent reviewer and a careful Pāli–Russian bilingual checker. You are READ-ONLY: do not edit any translation file.
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: use the Read tool; run python as `python -I -X utf8`; write helper scripts with the Write tool (never via a shell redirect).
- Put any helper scripts in 0-INBOX\temp\pipeline\pi-1-ru\review\, named after your part (r1_*.py …). Never create files at the repo root or in a system temp folder. Do not run git; never write "seed".
- Do not open the termbase, the keyword maps, the Russian zero-shot, or any builder or notes in 0-INBOX\temp\pipeline\pi-1-ru\ (rails\, termbase\, senses\, mapper-ru\): the point is a reading that is not anchored on them.
- You cannot write report files: return your report as text.

## Inputs
- **Pāli:** AI_translation\pali\pi-1_split_chapters\<ch>.md
- **Russian:** the same filenames in AI_translation\russian\pi-1-russian-plain-rails_split_chapters\
- **Alignment:** segments align by the block ID at the end of each segment (e.g. ^1-112); non-empty lines align one to one.
- **Optional references** for hard readings: the English translation 3-TRANSFORMATIONS\Translations\en-Contemporary-English-Abhidhamma\en-dhammasangani-ai.md and the Hindi rails translation AI_translation\hindi\pi-1-hindi-plain.md (find segments by block ID); the commentaries in 1-SOURCES\Commentaries\. The Pāli is the authority.
- **Style:** 0-INBOX\temp\pipeline\russian-style.md (typography, the dash rule, «…»/„…“, no «ли»).
- **Audience:** AI_translation\audience_profile\plain.md. The reader has no Buddhist background: the Russian must be clear, natural and modern, with nothing added.

## About the text
The Dhammasaṅgaṇī opens with a matrix (mātikā = «матрица») of triads and pairs and then classifies phenomena (dhamma = «явление»). Chapter 2 defines the states of mind and their factors by long synonym strings; chapter 3 classifies material form; chapters 4 and 5 go through the matrix item by item. The text is formulaic and abbreviates heavily with …pe… (rendered «…»). Everything turns on:
- which item is meant: kusala / akusala / abyākata (благой / неблагой / этически неопределённый), sahetuka vs ahetuka vs hetu, sampayutta vs vippayutta, sāsava vs anāsava, sekkha vs asekkha, the sphere (kāma-, rūpa-, arūpa-avacara, lokuttara);
- negations (na, no, a-, an-, neva … na) and "X ceva … no ca Y" polarity; in Russian, «ни … ни» with a participle or verb needs «не»;
- numbers: the jhāna ordinals, the counts, the N-fold groupings;
- complete synonym strings: nothing dropped, nothing added, order kept;
- the paṭipadā (dukkha / sukha; dandha / khippa) and ārammaṇa (paritta / appamāṇa) permutations.

Translation policy (user rules, not errors): the source is translated as written, so source slips are kept (e.g. an answer ending «?» at ^1-33, ^1-135, ^1-377); only plain spelling slips are rendered as meant. «X – это …» has no comma after a plain noun or list; the comma stays where it closes a clause or a participial / «кроме» phrase («То, что …, – это …»).

## Check every segment for
**1. CRITICAL: meaning errors**
- a wrong number or ordinal;
- wholesome and unwholesome swapped, conjoined and dissociated swapped, or a wrong triad or pair item;
- a negation lost or added;
- a wrong permutation of the paṭipadā or ārammaṇa formulas;
- a synonym dropped or added in a string, or omitted or added content (beyond «…» for …pe…);
- content on the wrong ID.

**2. MAJOR**
- Russian that is ungrammatical or misleading, so a reader would likely misread it (case government, agreement of gender and number with явление, совокупность, элемент, способность, ум; participle agreement in long chains);
- the same Pāli formula, item or term rendered inconsistently within your part.

**3. MINOR**
- awkward wording or register; a word repeated next to itself where the Pāli does not need it;
- Pāli left in Latin script outside variant brackets.

**Typography:** "–" only where the Pāli has "–" or "—", same spot, same count per line; statements end with "."; questions with "?" and never «ли»; quotes «…» / „…“; no double blank lines.

## How to check
The text is extremely repetitive. Verify the first instance of each formula carefully, then scan later segments for deviations by script: compare numerals and ordinals, count comma-separated items in the synonym strings (Pāli vs Russian), compare polarity words line by line. Read chapter openings, headings and the non-formulaic passages closely. Do not flag a source slip as a Russian error, but mention source slips briefly.

## Report (concise, plain text, as your final message)
- A table: ID | file | severity | Pāli (short) | Russian (short) | problem | suggested Russian fix.
- Then the counts per severity, the number of segments checked, and a one-paragraph overall judgement.
