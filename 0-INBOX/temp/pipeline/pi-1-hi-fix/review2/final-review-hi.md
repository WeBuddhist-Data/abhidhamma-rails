# Final review: corrected Hindi pi-1 (Dhammasaṅgaṇī), plain version

Date: 2026-11-27. Read-only review. Inputs: `review2/changes.jsonl` (all 105 items, covering the 56 kinds of change), `review2/sample.jsonl` (all 163 blocks), `fixes-log.md`, the full current text `AI_translation/hindi/pi-1-hindi-plain.md`, the backup, and the Dhammasaṅgaṇī-aṭṭhakathā (`1-SOURCES/Commentaries/pi-dhammasangani-atthakatha.md`) wherever a reading had to be checked. `review/verify-hi.md` was not read.

## 1. Verdicts

**Audience (plain.md): suitable with corrections.**
- The register is modern, plain Hindi. The fixes take out the words that would have misled a lay reader: अशिक्षित, मूर्छा, आक्रोश, अमानवीय, निडरता, दुःखद प्रगति, the "desireless yet ruled by desire" clash, and "मन का विज्ञान" read as "psychology".
- The sentences stay long and repetitive, but that is the source itself.
- Two remaining faults touch readability: a grammar slip in ^1-579 to ^1-581, and a list item in ^1-1388 and ^1-1404 that reads as two items.
- The main remaining risk is bare विज्ञान, which a lay reader may take as "science" (for example विज्ञान का समूह, अनंत विज्ञान का क्षेत्र). That was the user's decision, so it is listed for the reviewers below, not as a correction.

**Scholar check: holds up with corrections.**
- Every change kind I checked against the Pāli and the aṭṭhakathā is correct and consistent. Examples: the two objects of *idappaccayatā paṭiccasamuppannesu*; *paṇidhi* = आकांक्षा in ^1-1141 matching *appaṇihita* = आकांक्षा-रहित; *sīla* in *sīlabbata* = नियम, where the commentary glosses it as *gosīlādinā*; the *paritta*/*appamāṇa* object lines.
- Structure (lists, …pe… → …, variant brackets, block IDs) and display are clean.
- One meaning error remains, older than the fixes: *upādiṇṇā* in ^1-1050 and ^1-1051. It goes against the commentary and against ^1-1218 of the same text.
- One open item (*amanussasadda*) is settled by the commentary.

## 2. Necessary corrections

| ref | perspective | severity | current | corrected | justification |
|---|---|---|---|---|---|
| ^1-1050, ^1-1051 | both | major | «…हर व्यक्ति की निजी और कर्म से उत्पन्न हैं, यानी भौतिक रूप, अनुभूति, पहचान, मानसिक रचनाएँ, विज्ञान» | «…हर व्यक्ति की निजी और अपनाई हुई हैं, यानी भौतिक रूप, …» (or «ग्रहण की हुई») | **Wrong meaning.** The aṭṭhakathā on ^1-1050 says *upādiṇṇā* here means "located in the body": *Upādiṇṇāti sarīraṭṭhakā. Te hi kammanibbattā vā hontu mā vā, ādinnagahitaparāmaṭṭhavasena pana idha upādiṇṇāti vuttā* ("kamma-born or not, here called *upādiṇṇa* in the sense of taken up and grasped"). As it stands, the text says that all five aggregates of a being, wholesome mind included, are kamma-born. That contradicts ^1-1218 (wholesome phenomena are «कर्म से उत्पन्न न होने वाली»). The termbase sense कर्म से उत्पन्न is right for the duka (^1-1217) and the matter sections, but not here. 2 places; the text had this wording before the fixes. |
| ^1-579, ^1-580, ^1-581 | both | minor | «…की पहचान के साथ होने वाला चौथे ध्यान को प्राप्त करके» (4×) | «…की पहचान के साथ होने वाले चौथे ध्यान को प्राप्त करके» | **Ungrammatical.** The participle must be oblique before «ध्यान को». ^1-501 already has «होने वाले चौथे ध्यान को». The text had this before the fixes. |
| ^1-1388, ^1-1404 | both | minor | «उदासी के साथ होने वाली मन की दो उत्पत्तियाँ, दुःख के साथ होने वाला, शरीर से होने वाला विज्ञान, …» | «उदासी के साथ होने वाली मन की दो उत्पत्तियाँ, शरीर से होने वाला वह विज्ञान जो दुःख के साथ होता है, …» | **List structure.** Inside a comma-separated list, «दुःख के साथ होने वाला,» reads as a separate item, so the reader counts four items for the Pāli's three (*dve domanassasahagatacittuppādā, dukkhasahagataṃ kāyaviññāṇaṃ, …*). A relative clause keeps it one item, with no dash added and no Hindi word for "physiology". 2 places; brought in by the last fix step. |
| ^1-621, ^1-622 | scholar | minor | «मनुष्यों की ध्वनि, मनुष्येतर प्राणियों की ध्वनि» (4×) | «मनुष्यों की ध्वनि, मनुष्येतर ध्वनि» | **Narrowed meaning.** The aṭṭhakathā: *Manussānaṃ sallāpādisaddo manussasaddo. Taṃ ṭhapetvā seso sabbopi amanussasaddo. Iminā padadvayena sabbopi saddo pariyādinno*: every sound other than human speech, so that the two words cover all sound. «प्राणियों» restricts it to non-human beings. This settles the item the fixes-log leaves open, and the reviewer it cites was right. |

Count: 1 major, 3 minor (4 corrections, 12 places).

## 3. Checked and fine

- ***viññāṇa* = विज्ञान:** agreement across the whole text. There are no leftover feminine forms (की विज्ञान, विज्ञान उत्पन्न होती/हो चुकी/सकती, वाली … विज्ञान, होने वाला विज्ञान का), and no चेतना is left anywhere. The «X से होने वाला/वाले विज्ञान» forms are correct. मन का तत्व (*manodhātu*) and मन से होने वाले विज्ञान का तत्व (*manoviññāṇadhātu*) are kept distinct. इंद्रिय-विज्ञान, «पाँच प्रकार का विज्ञान» and «छह प्रकार के विज्ञानों» are fine.
- ***paṭiccasamuppanna* and *paṭiccasamuppāda*:** कारणों पर आश्रित is correct throughout.
- ***idappaccayatā*:** split into two objects in ^1-1008, ^1-1123, ^1-1238 and ^1-1241, as the aṭṭhakathā reads it (*idappaccayatāya ca paṭiccasamuppannesu ca dhammesu*).
- ***sīlabbataparāmāsa*, *sīlabbatupādāna* and the view *sīlena suddhi …*:** consistent. सदाचार is kept for *sīla* elsewhere (^1-1349, ^1-1368 to ^1-1372), which is a sound split of senses.
- ***sakkāyadiṭṭhi*:** the wording fits the four-mode definition in ^1-1007.
- ***assutavā*:** उपदेश से अनजान is fine.
- ***appaṇihita*:** आकांक्षा-रहित, with chanda kept as चाह, is consistent with *paṇidhi* = आकांक्षा in ^1-1141. The commentary reads it as the absence of *rāga*, *dosa* and *moha* *paṇidhi*.
- ***siyā*:** कुछ स्थितियों में reads well, including «कुछ स्थितियों में उसे … नहीं कहा जा सकता» (^1-1404).
- **Other word changes:**
  - मदहोशी, रोष, बुराई से न डरने की वृत्ति (paired with बुराई का डर)
  - «अपने को कुछ मानना / मान बैठना»
  - निरंतर आचरण, कष्टदायक प्रगति, क्षारीय (the commentary's *vātiṅgaṇakaḷīrādi*), अभौतिक पक्ष (which includes the unconditioned element, ^1-1316)
  - न पहचान, न पहचान के अभाव
- **The *paritta*/*appamāṇa* object lines:** «स्वयं X और X विषय वाला», «स्वयं X, पर Y विषय वाला».
- **List markers:** «, यानी» for the closed kamma-born, not-kamma-born and mind-born lists. «जैसे» is kept only before the open lists of colour, sound, smell and taste, which end «या जो भी अन्य …» (16 places, ^1-616 to ^1-631), which is right.
- **^1-1050 and ^1-1051 grammar:** fixed; only the *upādiṇṇā* word above is wrong.
- **Book name:** title, heading ^1-0 and colophon ^1-1616.
- **Display and structure across the full text:**
  - no Latin outside the variant-reading brackets;
  - brackets and quotation marks balanced on every line;
  - no double spaces, stray danda or doubled punctuation;
  - the only visarga is in दुःख, पुनः, स्वतः.
- **Sample blocks not touched by the fixes:** read in full. The only fault found is the agreement error above.

## 4. For the human reviewers

- **Bare विज्ञान** (user decision; not reopened). For a lay reader the everyday sense is "science", most visibly in «विज्ञान का समूह», «अनंत विज्ञान का क्षेत्र» and «विज्ञान को आत्मा के रूप में देखता है». A native reader should judge whether this is clear enough without a note.
- **Vocabulary policy** (मन, एकाग्रता, मोह, क्लेश, समभाव, क्षमता, तत्परता, जकड़न, मानसिक क्रिया): none is a real obstacle for this audience in the sample.
- ***niyatā* «उन्हीं से बँधी»** (^1-1050, ^1-1051): the aṭṭhakathā glosses it *attani jātā* ("arisen in oneself"). «उन्हीं में उत्पन्न» would be closer. A specialist should decide.
- ***sīlabbataparāmāsa* «…को ही शुद्धि का मार्ग मानने की…»**: a specialist should decide whether मार्ग here could be confused with मार्ग = *magga*, and whether «ही» is an acceptable plain-profile clarification.
- **«चार-चार की विधि / पाँच-पाँच की विधि»** (*catukkanaya*/*pañcakanaya*, about 35 places each): a native reader should say whether this is clear without the headings at ^1-1-2-1-0 and ^1-1-2-2-0.
- **Pāli source, not the Hindi:** `1-SOURCES/Text/pi-1.md` has a stray Devanāgarī visarga in «vicikicchatiः» (2 places, ^1-1123 and ^1-1241). It is not reproduced in the Hindi.
