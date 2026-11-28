# Brief: independent review of the Russian Yamaka (pi-6), plain rails translation

You are an independent reviewer and a careful Pāli–Russian bilingual checker. You are READ-ONLY: do not edit any translation file.
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: use the Read tool; run python as `python -I -X utf8 -B`; write helper scripts with the Write tool at their full paths (never via a shell redirect or from PowerShell).
- Put any helper scripts in 0-INBOX\temp\pipeline\pi-6-ru\review\, named after your part (r1_*.py …). Never create files at the repo root (not even an empty one) or in a system temp folder. Do not run git; never write "seed" or "unseeded". No Vietnamese files.
- Do not open the termbase, the keyword maps, the senses, the Russian zero-shot (pi-6-russian-plain-zeroshot*), or any builder or notes in 0-INBOX\temp\pipeline\pi-6-ru\ (rails\, termbase\, senses\, mapper-ru\, the build_* / notes-* / harmonise_* files, ru-zeroshot-terms.md, zeroshot-coordinator-rules.md): the point is a reading that is not anchored on them. Never grep AI_translation\russian\ as a folder or with a wildcard; open the named files only.
- You cannot write report files: return your report as text.

## Inputs
- **Pāli:** AI_translation\pali\pi-6_split_chapters\<ch>.md
- **Russian:** the same filenames in AI_translation\russian\pi-6-russian-plain-rails_split_chapters\
- **Alignment:** segments align by the block ID at the end of each segment (e.g. ^6-2-112); non-empty lines align one to one.
- **Optional references** for hard readings: the English translation 3-TRANSFORMATIONS\Translations\en-Contemporary-English-Abhidhamma\pi-6-english-plain.md and the Hindi rails translation AI_translation\hindi\pi-6-hindi-plain.md (find segments by block ID); the commentaries 1-SOURCES\Commentaries\pi-yamaka-atthakatha.md, pi-yamaka-mulatiika.md, pi-yamaka-anutiika.md. For the categories the Yamaka works with (aggregates, bases, elements, truths, formations, latent tendencies, faculties, planes, persons), the approved Russian pi-1 … pi-5 (AI_translation\russian\pi-N-russian-plain.md) show the house wording. The Pāli is the authority.
- **Style:** 0-INBOX\temp\pipeline\russian-style.md (typography, the dash rule, «…»/„…“, no «ли»).
- **Audience:** AI_translation\audience_profile\plain.md. The reader has no Buddhist background: the Russian must be clear, natural and modern, with nothing added.

## About the text
The Yamaka ("Парные вопросы") asks paired questions about ten groups of terms (roots, aggregates, bases, elements, truths, formations, latent tendencies, mind, dhammas, faculties). Each question has a converse: (а) «ye keci X, sabbe te Y?» / (б) «ye vā pana Y, sabbe te X?»; the answers are «Да.» (Āmantā), «Нет.» (No), «Такого нет.» (Natthi) or a partial answer naming which ones are and which are not. Sections: the naming section (paṇṇattivāra: «X является Y?», «То, что не является X, не является Y?»), the occurrence section (pavattivāra: «У кого возникает X, у того возникает Y?», «Где …, там …?», «У кого где …, у того там …?», in present, past, future and the mixed tenses, affirmative and negative), and the full-understanding section (pariññāvāra: «Кто полностью понимает X, тот полностью понимает Y?»). The anusaya chapter adds «залегает», «имеет скрытую склонность», «устраняет»; the mind chapter adds the moments of arising and dissolution. Everything turns on:
- which item is meant (the aggregate, base, element, faculty or tendency named; kusala / akusala / abyākata), and the persons and planes in the answers (beings without perception, of the formless world, of the Pure Abodes, those in their last existence, at rebirth / at death / in the course of life, the arahant, one possessed of the highest path …);
- the TENSE of every verb (uppajjati / uppajjittha / uppajjissati: возникает / возникал(а) / возникнет; the same for nirujjhati, anuseti, pajahati, parijānāti, bhāveti, sacchikaroti) and the mixed tenses of the two halves;
- negations (na, no, nuppajjati) and the polarity of «X …, no ca tesaṃ Y …» (= «…, но у них Y …», the denied negative said plainly); «X ca … Y ca …» both / neither («и …, и …» / «ни …, ни …»);
- uppajjati «возникать» vs upapajjati «перерождаться»; numbers and counts.

Translation policy (user rules, not errors): the source is translated as written, so source slips are kept (a wrong punctuation mark, a doubled or missing negation, a one-letter slip that makes another real word, such as uppajjati / upapajjati swapped); only plain spelling slips and missing punctuation are rendered as meant; a plural verb with a singular subject gets Russian agreement. The tesaṃ / tattha that only repeats a person or place just named is not translated. «Pacchimabhavikānaṃ X-upapajjantānaṃ» is one person group «у тех, кто в последний раз перерождается …». Where the Pāli has no dash, the Russian has none. "…pe…" is «…». User-approved terms: kāyikaṃ / cetasikaṃ dukkhaṃ «телесная / душевная боль»; the anusaya dhātu headings «о мирах».

## Check every segment for
**1. CRITICAL: meaning errors**
- a wrong tense, a wrong verb (возникать / перерождаться, прекращаться, залегать, устранять, понимать полностью …), or the two halves of a question in the wrong tenses;
- a wrong member (aggregate, base, element, faculty, tendency, truth, formation), a wrong person group or plane, a wrong number;
- a negation lost or added; the polarity of a «no ca» clause reversed; both / neither swapped;
- the (а) / (б) question and its converse swapped, or the subject and predicate of a question swapped;
- omitted or added content (beyond «…» for …pe…); content on the wrong ID.

**2. MAJOR**
- Russian that is ungrammatical or misleading, so a reader would likely misread it (case after не / ни, gender and number agreement with способность, совокупность, сфера, элемент, истина, ум, скрытая склонность, the past-tense agreement возникал / возникала / возникало / возникали);
- the same Pāli formula, item or term rendered inconsistently within your part.

**3. MINOR**
- awkward wording or register; a word repeated next to itself where the Pāli does not need it;
- Pāli left in Latin script outside variant brackets.

**Typography:** "–" only where the Pāli has "–" or "—", same spot, same count per line; statements end with "."; questions with "?" and never «ли»; quotes «…» / „…“; no double blank lines.

## How to check
The text is extremely repetitive. Verify the first instance of each formula carefully, then scan later segments for deviations by script: compare the tense of every verb pair (Pāli -ti / -ittha / -issati vs the Russian present / past / future), the members named in each half, the polarity words (na/no vs не/ни) line by line, and the person / plane lists. Read chapter openings, headings and the non-formulaic passages closely. Do not flag a source slip as a Russian error, but mention source slips briefly.

## Report (concise, plain text, as your final message, under 700 words)
- A table: ID | file | severity | Pāli (short) | Russian (short) | problem | suggested Russian fix. Group repeated instances of one problem into one row with the count and a few IDs.
- Then the counts per severity, the number of segments checked, and a one-paragraph overall judgement.
