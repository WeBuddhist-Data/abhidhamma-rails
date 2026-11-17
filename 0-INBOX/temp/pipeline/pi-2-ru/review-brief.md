# Brief: independent review of the Russian Vibhaṅga (pi-2), plain rails translation

You are an independent reviewer and a careful Pāli–Russian bilingual checker. You are READ-ONLY: do not edit any translation file.
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: use the Read tool; run python as `python -I -X utf8`; write helper scripts with the Write tool (never via a shell redirect).
- Put any helper scripts in 0-INBOX\temp\pipeline\pi-2-ru\review\, named after your part (r1_*.py …). Never create files at the repo root or in a system temp folder. Do not run git; never write "seed".
- Do not open the termbase, the keyword maps, the Russian zero-shot (pi-2-russian-plain-zeroshot*), or any builder or notes in 0-INBOX\temp\pipeline\pi-2-ru\ (rails\, termbase\, senses\, mapper-ru\, the build_*/notes-* files): the point is a reading that is not anchored on them. Never grep AI_translation\russian\ as a folder or with a wildcard; open the named files only.
- You cannot write report files: return your report as text.

## Inputs
- **Pāli:** AI_translation\pali\pi-2_split_chapters\<ch>.md
- **Russian:** the same filenames in AI_translation\russian\pi-2-russian-plain-rails_split_chapters\
- **Alignment:** segments align by the block ID at the end of each segment (e.g. ^2-112); non-empty lines align one to one.
- **Optional references** for hard readings: the English translation 3-TRANSFORMATIONS\Translations\en-Contemporary-English-Abhidhamma\en-vibhanga-ai.md and the Hindi rails translation AI_translation\hindi\pi-2-hindi-plain.md (find segments by block ID); the commentaries 1-SOURCES\Commentaries\pi-vibhanga-atthakatha.md, pi-vibhanga-mulatiika.md, pi-vibhanga-anutiika.md. For passages the Vibhaṅga shares with the Dhammasaṅgaṇī, the approved Russian pi-1 (AI_translation\russian\pi-1-russian-plain.md) shows the house wording. The Pāli is the authority.
- **Style:** 0-INBOX\temp\pipeline\russian-style.md (typography, the dash rule, «…»/„…“, no «ли»).
- **Audience:** AI_translation\audience_profile\plain.md. The reader has no Buddhist background: the Russian must be clear, natural and modern, with nothing added.

## About the text
The Vibhaṅga analyses 18 topics (aggregates, bases, elements, truths, faculties, dependent origination, foundations of mindfulness, right efforts, bases of power, factors of awakening, path, jhāna, measureless states, precepts, analytical knowledges, knowledge, minor topics, the heart of the teaching). Most chapters have three methods: by the discourses («Разбор по наставлениям»), by the Abhidhamma («Разбор по Абхидхамме») and a question section («Раздел вопросов») that runs the topic through the Dhammasaṅgaṇī matrix of triads and pairs. The text is formulaic and abbreviates heavily with …pe… (rendered «…»). Everything turns on:
- which item is meant: kusala / akusala / abyākata (благой / неблагой / этически неопределённый), sahetuka vs ahetuka vs hetu, sampayutta vs vippayutta, sāsava vs anāsava, sekkha vs asekkha, the sphere (kāma-, rūpa-, arūpa-avacara, lokuttara);
- negations (na, no, a-, an-, neva … na) and "X ceva … no ca Y" polarity; siyā = «иногда»; «na vattabbo» = «нельзя определить»; in Russian, «ни … ни» with a participle or verb needs «не»;
- numbers: counts of aggregates, bases, elements, faculties, the N-fold divisions («по одному», «на два вида» …), the jhāna ordinals, the lifespans of chapter 18;
- complete synonym strings: nothing dropped, nothing added, order kept;
- the paṭipadā (dukkha / sukha; dandha / khippa) and ārammaṇa (paritta / appamāṇa) permutations; the links of dependent origination.

Translation policy (user rules, not errors): the source is translated as written, so source slips are kept; only plain spelling slips are rendered as meant. The N-fold lines carry no «классификация» (user). «X – это …» has no comma after a plain noun or list; the comma stays where it closes a clause or a participial / «кроме» phrase. Where the Pāli has «na vattabbo – "A"ti, "B"» without a second ti, B is rendered as a plain statement («…, подвержена оковам, но не является оковами») on purpose. Where the Pāli has no dash, the Russian has none.

## Check every segment for
**1. CRITICAL: meaning errors**
- a wrong number or ordinal;
- wholesome and unwholesome swapped, conjoined and dissociated swapped, or a wrong triad or pair item;
- a negation lost or added; siyā lost or added;
- a wrong permutation of the paṭipadā or ārammaṇa formulas; a wrong link in dependent origination;
- a synonym dropped or added in a string, or omitted or added content (beyond «…» for …pe…);
- content on the wrong ID.

**2. MAJOR**
- Russian that is ungrammatical or misleading, so a reader would likely misread it (case government, agreement of gender and number with явление, совокупность, сфера, элемент, способность, истина, ум; participle agreement in long chains);
- the same Pāli formula, item or term rendered inconsistently within your part.

**3. MINOR**
- awkward wording or register; a word repeated next to itself where the Pāli does not need it;
- Pāli left in Latin script outside variant brackets.

**Typography:** "–" only where the Pāli has "–" or "—", same spot, same count per line; statements end with "."; questions with "?" and never «ли»; quotes «…» / „…“; no double blank lines.

## How to check
The text is extremely repetitive. Verify the first instance of each formula carefully, then scan later segments for deviations by script: compare numerals and ordinals, count comma-separated items in the synonym strings (Pāli vs Russian), compare polarity words (na/no/siyā vs не/ни/иногда) line by line. Read chapter openings, headings and the non-formulaic passages closely. Do not flag a source slip as a Russian error, but mention source slips briefly.

## Report (concise, plain text, as your final message)
- A table: ID | file | severity | Pāli (short) | Russian (short) | problem | suggested Russian fix.
- Then the counts per severity, the number of segments checked, and a one-paragraph overall judgement.
