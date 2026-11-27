# Verification of the fixed Hindi pi-1 (Dhammasaṅgaṇī), 2026-11-27

Inputs: `review/changes.jsonl` (97 items, 52 kinds), `review/sample-after.jsonl` (166 blocks, 62 touched by the fix), the corrected book `AI_translation/hindi/pi-1-hindi-plain.md`, the backup `backup/pi-1-hindi-plain.md`, the Pāli `1-SOURCES/Text/pi-1.md` and the Aṭṭhasālinī `1-SOURCES/Commentaries/pi-dhammasangani-atthakatha.md`, which I used to check the fixes-log reasons. Read-only: no file other than this one was changed.

## 1. Verdict

**Plain audience (plain.md): yes, with corrections.**
- The fixes take out real traps from everyday Hindi: निडरता read as praise, मूर्छा as fainting, अशिक्षित as illiterate, अमानवीय as inhumane, आक्रोश as outcry, दुःखद as sad, सेवन as consuming, and "इच्छा-रहित और चाह की प्रधानता वाला", which contradicted itself. The new wording is natural modern Hindi.
- **विज्ञान is the one real risk.** Used alone or as "विज्ञान का समूह", it works: ^1-6 and its repeats list विज्ञान among the names for मन, and the five-group lists frame it. But in the genitive sense words, everyday Hindi reads "X का विज्ञान" as "the science of X". मन का विज्ञान sounds like psychology and शरीर का विज्ञान like physiology. This affects about 207 places ("आँख के विज्ञान का आधार", "मन के विज्ञान का तत्व"), and a plain reader would be misled on first reading.
- Two agreement errors came in with the fix (4 blocks).

**Scholar check (adapted): yes, with corrections.**
- The cetanā/viññāṇa distinction is now kept: इरादा = *cetanā*, विज्ञान = *viññāṇa*, and no चेतना is left anywhere.
- *paṭiccasamuppanna*, *idappaccayatā* (as two objects), *siyā*, *nāma*, *sīlabbata-*, *appaṇihita* and *maññanā* are all more accurate than before. The two-object reading of *idappaccayatā* matches the Aṭṭhasālinī ("idappaccayatāya ceva paṭiccasamuppannadhammesu ca"). आकांक्षा-रहित now matches *paṇidhi* = आकांक्षा in the lobha list (^1-1065, ^1-1141).
- The structure is faithful. In 1,927 of 1,930 blocks, the number of विज्ञान equals the number of *viññāṇ-* in the Pāli. The three exceptions (^1-M2-13, ^1-1101, ^1-1464) have the Hindi spelling out the *viññāṇa* that is implied in *kenaci viññeyyā*. That was already so before the fix.
- Remaining issues are minor:
  - The new *sakkāyadiṭṭhi* label is narrower than its own definition.
  - The "स्वयं" fix still leaves the mixed limited/unlimited cases ambiguous.
  - *amanussa* is narrowed to "beings".

## 2. Per change

| kind of change | verdict | audience | scholar | note |
|---|---|---|---|---|
| *viññāṇa* चेतना → विज्ञान, all forms (207 + 139 + 27 + 25 + 17 + 6 + 2 …: bare, का/के/की, "पाँच प्रकार का", इंद्रिय-चेतनाएँ → इंद्रिय-विज्ञान) | better | risky in the sense-word compounds (see P1); fine alone, in "विज्ञान का समूह" and in "अनंत विज्ञान का क्षेत्र" with its context | yes: restores the *cetanā*/*viññāṇa* distinction and the Hindi Buddhist standard | ^1-6, ^1-49, ^1-123, ^1-1007 read well |
| Agreement after विज्ञान: होती→होता, हो चुकी→हो चुका, होगी→होगा, सकती→सकता, वाली→वाला (30 / 20 / 20 / 20 / 10) | better | natural | – | correct in every checked context (^1-599, ^1-611, ^1-615, ^1-631, ^1-431, ^1-443, ^1-556), with **two misses** (P2, P3) |
| *paṭiccasamuppanna* परस्पर-आश्रित रूप से → कारणों पर आश्रित होकर (62 ×2) | better | clear, natural | yes: "mutual" is *aññamañña*, a different condition | ^1-1, ^1-62, ^1-150, ^1-163 |
| *paṭiccasamuppāda* परस्पर-आश्रित → कारणों पर आश्रित उत्पत्ति (3) | better | clear | yes | ^1-1343 |
| *idappaccayatā paṭiccasamuppannesu*: two objects ("के बारे में और …", "को और …") (4 + 1 + …) | better | clear | yes: the Aṭṭhasālinī reads it as two | ^1-1123, ^1-1167, ^1-1238, ^1-1241 |
| *sīlabbataparāmāsa* … के बारे में ग़लत धारणा → नियमों और व्रतों को ही शुद्धि का मार्ग मानने की ग़लत धारणा (29 + 49) | better | clear | yes: matches the definition at ^1-1009 and ^1-1264. ही is an allowed plain clarification | |
| *sīlena suddhi, vatena suddhi*: सदाचार→नियमों, व्रत→व्रतों (49 / 12) | better | clear | yes: the same word as in the compound | सदाचार is left only for real *sīla* (sīlavisuddhi and the like), which is correct |
| *sīlabbatupādāna* → नियमों और व्रतों के प्रति आसक्ति | better | clear | yes | |
| *sakkāyadiṭṭhi* स्थायी आत्मा की → पाँच समूहों को आत्मा मानने की ग़लत दृष्टि (14) | better | clear | partly: removes the wrong "permanent", but covers only 1 of the 4 modes in its own definition (P4) | the fixes-log reason is overstated: ^1-1007 has four modes for each group |
| *appaṇihita* इच्छा-रहित → आकांक्षा-रहित, headings इच्छाओं → आकांक्षाओं (42 + 6 + 6 + 4 + 1) | better | clear: the contradiction with "चाह की प्रधानता" is gone | yes: agrees with *paṇidhi* = आकांक्षा | ^1-351, ^1-354, ^1-546, ^1-1-5-5-0 |
| *siyā* कभी → कुछ स्थितियों में (52) | better | clear | yes: modal and distributive, not temporal | every one of the 52 sits on a *siyā*; no कभी is left; ^1-1406, ^1-1435, ^1-1583 |
| *mucchā* मूर्छा → मदहोशी (9) | better | clear | yes | ^1-1065, ^1-1103, ^1-1119, ^1-1141 |
| *assutavā* अशिक्षित → उपदेश न सुनने वाला (4) | better | mostly clear, but see P6 | yes (lacking learning, the commentary's *āgama*) | |
| *anottappa* बुराई के प्रति निडरता → बुराई से न डरने की वृत्ति (49 + 6 + 3 …) | better | clear: no longer reads as praise | yes: pairs with *ottappa* = बुराई का डर | feminine agreement kept (^1-1257 "…वृत्ति … क्लेशों से जुड़ी भी") |
| *āghāta* आक्रोश → रोष (30 + 5) | better | clear | yes | ^1-1066, ^1-1120, ^1-1160, ^1-1237 |
| *maññanā, maññitatta* → अपने को कुछ मानना, अपने को कुछ मान बैठना | better | natural idiom | yes: conceit, not "assume" (the Aṭṭhasālinī calls them the mode and the state of *māna*) | ^1-1121, ^1-1239 |
| *āsevanā* निरंतर सेवन → निरंतर आचरण | better | clear | yes | ^1-1361, ^1-1379 |
| *dukkhapaṭipadā* दुःखद → कष्टदायक प्रगति (71 + 36 + …) | better | clear | yes | |
| *amanussa* अमानवीय → मनुष्येतर प्राणियों (4) | better | clear | the fix is correct; "प्राणियों" is a pre-existing narrowing (P7) | |
| *khārika* खारा → क्षारीय (4) | better | understandable ("alkaline") | yes: no longer the same as *loṇika* | ^1-628, ^1-630 |
| *nāma* मानसिक पक्ष → अभौतिक पक्ष (5) | better / same | clear | yes: includes the unconditioned element; still right in the *paṭiccasamuppāda* list | ^1-1343 |
| *nevasaññānāsaññā* न अ-पहचान → न पहचान के अभाव (9) | better | real Hindi now | yes | ^1-1291, ^1-1421, ^1-1436 |
| *paritta / appamāṇa* + object: "स्वयं X और Y विषय वाला" (40 ×2) | better | clear when X = Y; still ambiguous when X ≠ Y (P5) | yes | |
| Kamma-born and mind-born lists ", जैसे" → ", यानी" (48) | better | clear | yes: the list after *yaṃ vā panaññampi atthi …* names that rūpa and gives no examples | ^1-652, ^1-887, ^1-911, ^1-916, ^1-917, ^1-923, ^1-935 |
| ^1-1050, ^1-1051 *ajjhattaṃ paccattaṃ* → भीतर की, उनकी अपनी, उन्हीं से बँधी | better | grammatical now | yes | |
| Title, heading ^1-0 and colophon ^1-1616 → धम्मसंगणी (परिघटनाओं की गणना) | better | clear | yes: the book's name is restored | |

## 3. Problems

| ref | severity | current | suggested | reason |
|---|---|---|---|---|
| P1: sense-word compounds, about 207 places (आँख/कान/नाक/जीभ/शरीर का or के विज्ञान: 121; मन के विज्ञान: 86), e.g. ^1-6, ^1-281, ^1-681, ^1-693, ^1-793, ^1-1527 | major (audience) | "शरीर के विज्ञान का आधार", "उसके अनुरूप मन के विज्ञान का तत्व", "आँख का विज्ञान उत्पन्न होता है" | Keep विज्ञान (the user's decision), but say what it is through: "आँख से होने वाला विज्ञान", "शरीर से होने वाले विज्ञान का आधार", "मन से होने वाले विज्ञान का तत्व". The text itself already has "आँख का विज्ञान, आँख के सहारे, उत्पन्न" (*nissāya*). If that change is too wide, at least add a one-line reader's note in the publication text that विज्ञान here means "knowing / consciousness", not science | In Hindi, "X का विज्ञान" is how the names of sciences are formed (मनोविज्ञान, शरीर-विज्ञान). Plain.md puts understanding first and allows clarification by wording. "X से होने वाला" adds nothing beyond the Pāli compound (*cakkhu-viññāṇa* = consciousness through the eye) |
| P2: ^1-1388, ^1-1404 | minor (regression) | "दुःख के साथ होने वाली शरीर का विज्ञान" | "दुःख के साथ होने वाला शरीर का विज्ञान" | विज्ञान is masculine; the participle before the noun was missed by the agreement script |
| P3: ^1-584, ^1-594 | minor (regression) | "छह प्रकार की विज्ञानों से जाना जा सकने वाला" | "छह प्रकार के विज्ञानों से जाना जा सकने वाला" | the same: was "की चेतनाओं"; the oblique plural needs के |
| P4: *sakkāyadiṭṭhi*, ^1-1006, ^1-1007, ^1-1013, ^1-1014, ^1-1017, ^1-1261, ^1-1262, ^1-1268, ^1-1269, ^1-1271 | minor (scholar) | "पाँच समूहों को आत्मा मानने की ग़लत दृष्टि" | "पाँच समूहों के संबंध में आत्मा की ग़लत दृष्टि" | The definition at ^1-1007 has four modes for each group: the group as self, self as having it, it in self, self in it. "Taking the groups as self" covers only the first, so the label is narrower than its own definition. Also update the termbase gloss (P8) |
| P5: mixed *paritta/appamāṇa*, about 32 places: ^1-182, ^1-183, ^1-185, ^1-187, ^1-188, ^1-191, ^1-192, ^1-195, ^1-196, ^1-199, ^1-200, ^1-202, ^1-212 … ^1-243 | minor | "स्वयं सीमित और अपरिमित विषय वाला", "स्वयं अपरिमित और सीमित विषय वाला" | "स्वयं सीमित और विषय में अपरिमित", "स्वयं अपरिमित और विषय में सीमित". The same-value cases can stay | "सीमित और अपरिमित विषय वाला" still groups naturally as two modifiers of विषय, and स्वयं can be read as emphasis. The ambiguity the fix aimed at stays where the two values differ |
| P6: *assutavā*, ^1-1007, ^1-1223, ^1-1262, ^1-1269 | minor | "उपदेश न सुनने वाला साधारण व्यक्ति" | "उपदेश से अनजान साधारण व्यक्ति" (or "जिसने उपदेश नहीं सुना है, ऐसा साधारण व्यक्ति") | The habitual "न सुनने वाला" reads as "one who won't listen to advice" (disobedient). The Aṭṭhasālinī defines *assutavā* as lacking learning and attainment (*āgamādhigamābhāvā*), not as refusing |
| P7: *amanussasadda*, ^1-620, ^1-621, ^1-622, ^1-623 | minor (scholar, pre-existing) | "मनुष्येतर प्राणियों की ध्वनि" | "मनुष्येतर ध्वनि" | The Aṭṭhasālinī says that, apart from human sound, all other sound is *amanussasadda*, so the two words together cover all sound. "प्राणियों" narrows this to beings. It was already in the old wording |
| P8: termbase entry *sakkāyadiṭṭhi* | minor | English gloss "the wrong view of a lasting self" | "personality view: the wrong view of a self in relation to the five groups" | The gloss still has the "lasting" that the text fix removed |

## 4. Regression check

What I looked for, across the whole corrected book (not only the 166 blocks):
- **Agreement around every विज्ञान:** all 516 hits, in 171 distinct contexts, each read with the words around it. I searched for feminine forms before and after it (वाली, होती, हुई, चुकी, होगी, सकती, जुड़ी, की …) and for the plural forms (विज्ञानों, इंद्रिय-विज्ञान). Found P2 (2 blocks) and P3 (2 blocks). Everything else agrees, including the relative clauses ("…उत्पन्न होता है, जो समभाव के साथ होने वाला है") and "मन के विज्ञान का प्रसन्नता / समभाव के साथ होने वाला तत्व".
- **Old wording left behind:** चेतना 0, कभी 0, अ-पहचान 0, निडरता 0, मूर्छा 0, आक्रोश 0, इच्छा-रहित 0. सदाचार is left only for real *sīla*.
- **Counts against the Pāli:** per-block count of विज्ञान against *viññāṇ-* for all 1,930 blocks. They match everywhere except ^1-M2-13, ^1-1101 and ^1-1464 (*kenaci viññeyyā*, where the Hindi spells out the implied viññāṇa; it was so before the fix) and the front-matter line.
- **Wrong targets:** every "कुछ स्थितियों में" stands on a *siyā*; every inserted "स्वयं" sits in a *paritta/appamāṇa* + *-ārammaṇa* pair; each of the 48 "यानी" the fix added (9 → 57) stands after *yaṃ vā panaññampi atthi rūpaṃ …*.
- **Other genders:** *anottappa* (निडरता f → वृत्ति f), *āghāta* (m → m), *mucchā* (f → f), *āsevanā* (m → m): agreement is unchanged and correct, e.g. ^1-1257, ^1-411, ^1-426.

What I found in the 166 sample blocks:
- All 166 read in full; 62 were changed by the fix.
- One regression is in the sample: ^1-1388 (P2).
- No sentence elsewhere became ungrammatical or unclear. The fixed blocks (^1-6, ^1-62, ^1-163, ^1-182, ^1-238, ^1-281, ^1-556, ^1-652, ^1-887, ^1-1007, ^1-1051, ^1-1065, ^1-1066, ^1-1121, ^1-1241, ^1-1257, ^1-1435, ^1-1583, ^1-1616) read as correct, natural Hindi.
- Problems the fixes missed that the profile would require: P1 (the main one; the fix brought it in by design, so it needs a wording decision), P5, P6 and P7.
- The vocabulary-policy items (मन, एकाग्रता, मोह, क्लेश, समभाव, क्षमता, तत्परता, जकड़न, मानसिक क्रिया) were not made worse by any fix.
