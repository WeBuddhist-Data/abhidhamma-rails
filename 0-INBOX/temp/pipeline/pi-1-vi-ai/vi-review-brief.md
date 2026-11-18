# Brief: independent review of the Vietnamese Dhammasaṅgaṇī (pi-1), plain rails translation

You are an independent reviewer and a careful Pāli–Vietnamese bilingual checker. You are READ-ONLY: do not edit any translation file.
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: use the Read tool; run python as `python -I -X utf8`; write helper scripts with the Write tool (never via a shell redirect).
- Put any helper scripts in 0-INBOX\temp\pipeline\pi-1-vi-ai\review\, named after your part (r1_*.py …). Never create files at the repo root or in a system temp folder. Never run git (not even git status); never write "seed".
- Do not open the termbase, the keyword maps, the word senses, the Vietnamese zero-shot, or any builder or notes in 0-INBOX\temp\pipeline\pi-1-vi-ai\ (rails\, termbase\, senses\, mapper-vi\, build_*, notes-*): the point is a reading that is not anchored on them.
- You cannot write report files: return your report as text.

## Inputs
- **Pāli:** AI_translation\pali\pi-1_split_chapters\<ch>.md
- **Our Vietnamese (under review):** the same filenames in AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters\
- **Alignment:** segments align by the block ID at the end of each segment (e.g. ^1-112); non-empty lines align one to one.
- **Reference human translation (Tịnh Sự):** 1-SOURCES\Translations\Vietnamese\vi-1-tinh_su.md, block-aligned to the same IDs (each block carries the root block ID; find segments by ID). It is COPYRIGHTED: use it only to check meaning. Never copy its wording into a suggested fix; quote at most a few words of it to identify a point. Your suggested fixes must be in our own words and our own terms.
- **Optional references** for hard readings: the English translation 3-TRANSFORMATIONS\Translations\en-Contemporary-English-Abhidhamma\en-dhammasangani-ai.md and the Russian rails translation AI_translation\russian\pi-1-russian-plain-rails_split_chapters\ (find segments by block ID); the commentaries in 1-SOURCES\Commentaries\. The Pāli is the authority.
- **Style:** 0-INBOX\temp\pipeline\vietnamese-style.md (typography, the dash rule, “…” / ‘…’, core terms; sati = «sự tỉnh thức», never «chánh niệm»).
- **Audience:** AI_translation\audience_profile\plain.md. The reader has no Buddhist background: the Vietnamese must be clear, natural and modern, with nothing added.

## About the text
The Dhammasaṅgaṇī opens with a matrix (mātikā = «ma trận») of triads and pairs and then classifies phenomena (dhamma = «hiện tượng»). Chapter 2 defines the states of mind and their factors by long synonym strings; chapter 3 classifies matter (rūpa = «vật chất»; visible form = «hình sắc»); chapters 4 and 5 go through the matrix item by item. The text is formulaic and abbreviates heavily with …pe… (rendered «…»). Everything turns on:
- which item is meant: kusala / akusala / abyākata («thiện» / «bất thiện» / «không xác định về mặt đạo đức»), sahetuka vs ahetuka vs hetu, sampayutta vs vippayutta, sāsava vs anāsava, sekkha vs asekkha, the sphere (kāma-, rūpa-, arūpa-avacara, lokuttara);
- negations (na, no, a-, an-, neva … na) and "X ceva … no ca Y" polarity;
- numbers: the jhāna ordinals, the counts, the N-fold groupings;
- complete synonym strings: nothing dropped, nothing added, order kept;
- the paṭipadā (dukkha / sukha; dandha / khippa) and ārammaṇa (paritta / appamāṇa) permutations.

Translation policy (user rules, not errors): the source is translated as written, so source slips are kept (e.g. an answer ending «?» at ^1-33, ^1-135, ^1-377; a question ending «.» at ^1-473); only plain spelling slips and missing punctuation are rendered as meant. User terminology decisions (not errors): bodily pain dukkha = «khó chịu» (never «đau khổ»); sukha = «hạnh phúc» as the jhāna factor, «dễ chịu» for pleasant feeling; vāra «mục», bhāṇavāra «phần»; ajjhatta «ở nơi bản thân»; mātikā «ma trận»; vīriya «tinh tấn» vs vāyāma / padhāna «nỗ lực».

## Part A: bilingual check of every segment
**1. CRITICAL: meaning errors**
- a wrong number or ordinal;
- wholesome and unwholesome swapped, conjoined and dissociated swapped, or a wrong triad or pair item;
- a negation lost or added;
- a wrong permutation of the paṭipadā or ārammaṇa formulas;
- a synonym dropped or added in a string, or omitted or added content (beyond «…» for …pe…);
- content on the wrong ID.

**2. MAJOR**
- Vietnamese that is ungrammatical or misleading, so a reader would likely misread it (word order, a doubled «là», a dangling classifier, a modifier attached to the wrong noun in long chains);
- the same Pāli formula, item or term rendered inconsistently within your part.

**3. MINOR**
- awkward wording or register; a word repeated next to itself where the Pāli does not need it;
- Pāli left in Latin script outside variant brackets.

**Typography:** "–" only where the Pāli has "–" or "—", same spot, same count per line; statements end with "."; questions with "?" and a Vietnamese question word; quotes “…” / ‘…’; no «….»; no double blank lines.

## Part B: comparison with the Tịnh Sự translation
For every segment of your part, compare our Vietnamese with Tịnh Sự's on MEANING (not wording or terminology choices). Report only where the comparison reveals something to check:
- Tịnh Sự reads the Pāli differently in a way that changes the meaning (scope of a negation, which item is meant, a number, who/what a phrase refers to, a different sense of a word). Check the Pāli (and the commentary if needed) and say which reading is right. Do NOT treat Tịnh Sự as the authority.
- Tịnh Sự has content we lack, or we have content it lacks (beyond …pe… expansions it may make): check the Pāli and say which is right.
- A passage where Tịnh Sự is clearly easier for a lay reader to follow in structure: describe the structural point (e.g. "splits the long list into two sentences"), and propose a fix in our own words.
Do not report differences of terminology where ours follows the user decisions above or is simply another valid word. Do not report Tịnh Sự's own slips except where they help explain a reading.

## How to check
The text is extremely repetitive. Verify the first instance of each formula carefully, then scan later segments for deviations by script: compare numerals and ordinals, count comma-separated items in the synonym strings (Pāli vs Vietnamese), compare polarity words line by line. Read chapter openings, headings and the non-formulaic passages closely. Do not flag a source slip as a Vietnamese error, but mention source slips briefly.

## Report (concise, plain text, as your final message)
- Part A table: ID | file | severity | Pāli (short) | Vietnamese (short) | problem | suggested Vietnamese fix (our wording).
- Part B table: ID | file | kind (reading / content / clarity) | what differs (brief) | which is right and why | suggested fix to ours (our wording), or "none".
- Then the counts per severity and per kind, the number of segments checked, and a one-paragraph overall judgement.
