# Brief: independent review of the Hindi Yamaka (pi-6)

You are an independent reviewer and a careful Pāli–Hindi bilingual checker. You are READ-ONLY: do not edit any translation file.
- Work in D:\Work\OpenPecha\abhidhamma-rails. It is a Windows machine: use the Read tool, and run python as `python -I -B -X utf8`.
- Put any helper scripts in 0-INBOX\temp\pipeline\pi-6-hi\review\, named after your part (review_<part>_*.py). Never create files at the repo root or in a system temp folder. Do not run git. Never write "seed" or "unseeded".
- Do not open the termbase, the keyword maps, the zero-shot Hindi, or any notes, builders or reports in 0-INBOX\temp\pipeline\pi-6-hi\ (rails\ included): the point is a reading that is not anchored on them.

## Inputs
- **Pāli:** AI_translation\pali\pi-6_split_chapters\<f>.md
- **Hindi:** the same filenames in AI_translation\hindi\pi-6-hindi-plain-rails_split_chapters\
- **Alignment:** segments align by the block ID at the end of each segment (e.g. ^6-2-50). Non-empty lines align one to one.
- **Optional reference** for hard readings: the reviewed English translation AI_translation\english\pi-6-english-plain-rails_split_chapters\<f>.md (same segments), and the commentary in 1-SOURCES\Commentaries\. The Pāli is the authority.
- **Audience:** AI_translation\audience_profile\plain.md. The reader has no Buddhist background, so the Hindi must be clear, natural and modern, with nothing added.

## About the text
The Yamaka ("Pairs") asks paired questions about ten topics (roots, aggregates, sense bases, elements, truths, formations, latent tendencies, mind, phenomena, faculties) and answers them. It is almost entirely formulaic and abbreviates heavily with …pe…. Everything turns on:
- **polarity**: na / no / a- / an-, "nuppajjati", the positive (anuloma) vs negative (paccanīka) sections;
- **tense**: uppajjati / uppajjittha / uppajjissati and nirujjhati / nirujjhittha / nirujjhissati, often mixed inside one sentence (e.g. "uppajjati … uppajjissati"): each clause keeps its own tense;
- **which item**: the aggregate, sense base, element, truth, formation, tendency or faculty named in each slot, and their order in the question pair (Ka) X→Y, (Kha) Y→X;
- **who and where**: person (yassa … tassa), place (yattha … tattha), both (yassa yattha … tassa tattha); the being/place chains (Asaññasatta, pañcavokāra, catuvokāra, arūpa, Suddhāvāsa, those reborn / dying / attaining final nibbāna, the sense-organ beings sacakkhuka / acakkhuka, women / men, moments of arising / dissolution): nothing dropped, nothing added, nothing swapped;
- **numbers**: Tīṇeva, Naveva, dve / tayo / cattāro puggalā, the jhāna ordinals.

## Approved conventions (do NOT flag these)
- dhamma = «परिघटना»; kusala / akusala / abyākata = «हितकर / हानिकर / नैतिक रूप से अनिर्धारित»; khandha = «समूह»; āyatana = «इंद्रिय-क्षेत्र»; dhātu = «तत्व»; sacca = «सत्य»; saṅkhāra = «रचना»; anusaya = «सुप्त प्रवृत्ति» (feminine); citta = «मन»; indriya = «क्षमता» (feminine); puggala = «व्यक्ति»; okāsa = «स्थान».
- In the term-checking pairs, bare words stay bare (rūpaṃ = «रूप», saṅkhārā = «रचनाएँ», cakkhu = «आँख») while the full names take the full term («भौतिक रूप का समूह», «आँख की क्षमता»).
- Āmantā = «हाँ।»; Natthi (as an answer) = «ऐसा कोई नहीं है।»; short answers like "Uppajjati." = «उत्पन्न होता है।».
- **"no ca tesaṃ Y V" is always rendered by flipping the polarity**: "no ca tesaṃ Y uppajjati" = «पर उनमें Y उत्पन्न नहीं होता»; "no ca tesaṃ Y nuppajjati" = «पर उनमें Y उत्पन्न होता है». This is correct, not a lost or added negation.
- The quotative -ti is dropped. "…pe…" = "…". (Ka)/(Kha)/… = (क)/(ख)/…
- Being chunks keep «में» and are joined «A में और B में»; two places sharing one participle are joined with «या» («सूक्ष्म भौतिक लोक या अभौतिक लोक में अंतिम जन्म वालों में»); catuvokārānaṃ pañcavokārānaṃ = «चार या पाँच समूहों वाले अस्तित्व के प्राणियों में»; sense-organ beings «आँख वाले / आँख से रहित»; na itthīnaṃ = «स्त्रियों से भिन्न».
- Source slips (wrong labels, missing ca, misspellings) were translated as meant; mention them only briefly.

## Check every segment for

**1. CRITICAL: meaning errors**
- polarity wrong (after applying the "no ca" flip rule above);
- a wrong tense in any clause;
- a wrong item in a slot, or the (Ka)/(Kha) order swapped;
- a being, place or moment dropped, added or swapped in a chain; a wrong number;
- omitted or added content (beyond "…" for …pe…); content placed on the wrong ID.

**2. MAJOR**
- Hindi that is ungrammatical or misleading, so that a reader would likely misread it, including verb agreement with feminine क्षमता / सुप्त प्रवृत्ति / रचना / परिघटना and masculine समूह / इंद्रिय-क्षेत्र / तत्व / सत्य / मन.
- The same Pāli formula rendered inconsistently within your part.

**3. MINOR**
- awkward wording or register; Pāli left in Latin script outside variant brackets.

**Also check typography:** "–" only where the Pāli has "–" or "—", at the same spot; statements end with «।», questions with «?»; quotes are “…”; no double blank lines.

## How to check
The text is extremely repetitive. Verify the first instance of each formula carefully by reading, then check every segment by script: for each line, compare the polarity (count na/no/nuppajj/na uppajj… in the Pāli against न/नहीं in the Hindi, applying the flip rule per clause), the tense markers (-ittha → «था/थी/थे/थीं», -issati/-issanti → «गा/गी/गे/गीं», present → «ता/ती/ते … है/हैं» or bare «होता/होती»), the item names in each slot (build a Pāli→Hindi table from the first instances and check every slot against it), and the number of being/place chunks. Read chapter openings, headings, notes in brackets and the non-formulaic passages closely.

## Report (concise; plain text, as your final message; you cannot write files)
- A table: ID | file | line (non-empty line number in the file) | severity | Pāli (short) | Hindi (short) | problem | suggested Hindi fix (the exact old → new string where possible).
- If one error repeats in many segments, give one row with the pattern and the list of IDs.
- Then the counts per severity, the number of segments checked, and a one-paragraph overall judgement.
