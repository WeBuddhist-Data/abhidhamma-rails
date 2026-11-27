# Hindi pi-1: error fixes of 2026-11-27

Source of the findings: `0-INBOX/temp/language-priority/pi1-verify/`:
- `pi-1-verification-report.md`
- `pi-1-alignment-report.md`
- `profile/pi-1-profile-review.md`

Decisions by the user:
- *viññāṇa* = विज्ञान.
- Also fix the words whose everyday meaning is clearly different.

## How

- **Text:** `fix_pi1_hi.py` changes the 14 rails chapter files. Every rule has an expected count, and the script stops before writing if any count differs. `vinnana.py` makes the *viññāṇa* change with gender agreement: चेतना is feminine, विज्ञान masculine.
- **Rebuild:**
  - The book file `AI_translation/hindi/pi-1-hindi-plain.md` was rebuilt from the chapters with `merge_rails.py`. Before the fixes, this rebuild reproduced the old file byte for byte.
  - The track copy `3-TRANSFORMATIONS/Translations/hi-Contemporary-Hindi-Abhidhamma/pi-1-hindi-plain.md` was rebuilt as the book file plus `add_transclusions.py`.
- **Termbase:** `fix_termbase_hi.py` changes `AI_translation/hindi/pi-1-pali-hindi-termbase-plain.md`. The track termbase is an identical copy.
- **Backup:** the scripts run from `backup/`, so they can be rerun. That folder is not committed: the originals are in git at commit `000a27b5`. To restore it, check out the pre-fix files from that commit into `backup/` (the track copies as `track-pi-1-hindi-plain.md` and `track-pi-1-pali-hindi-termbase-plain.md`).

## What changed in the text

| Fix | Places | Reason |
|---|---|---|
| *viññāṇa*: चेतना → विज्ञान, with agreement (की→का/के, की चेतनाओं→के विज्ञानों, होती→होता, हो चुकी→हो चुका, वाली→वाला, also before the noun: होने वाली शरीर की चेतना → होने वाला शरीर का विज्ञान) | 515 | In every Hindi Buddhist source (Tripathi, Lucknow 1960, Kausalyāyan, Narendra Dev, Rahul Sankrityayan), चेतना is *cetanā* and *viññāṇa* is विज्ञान |
| *paṭiccasamuppanna*: परस्पर-आश्रित रूप से → कारणों पर आश्रित होकर | 112 | "Mutual" is a different condition (*aññamañña*) |
| *idappaccayatā paṭiccasamuppannesu*: two objects (law of conditionality, and the conditioned phenomena) | 11 | As the commentary reads it; the text had "by the law" |
| *paṭiccasamuppāda*: परस्पर-आश्रित उत्पत्ति → कारणों पर आश्रित उत्पत्ति | 3 | as above |
| *sīlabbataparāmāsa* → नियमों और व्रतों को ही शुद्धि का मार्ग मानने की ग़लत धारणा | 30 | was "a wrong idea about good conduct and vows"; now its own definition (purity through rules and vows). *parāmāsa* stays ग़लत धारणा |
| *sīlabbatupādāna* → नियमों और व्रतों के प्रति आसक्ति | 8 | rules, not good conduct |
| the view *sīlena suddhi …* → नियमों से …, व्रतों से …, नियमों और व्रतों से … | 6 | same word as the compound |
| *sakkāyadiṭṭhi*: स्थायी आत्मा की → पाँच समूहों के संबंध में आत्मा की ग़लत दृष्टि | 14 | "Permanent" belongs to *sassatadiṭṭhi*; ^1-1007 defines this view as regarding each of the five groups in terms of a self in four ways (as self, self having it, it in self, self in it) |
| *appaṇihita*: इच्छा-रहित → आकांक्षा-रहित; headings इच्छाओं का/के अभाव → आकांक्षाओं का/के अभाव | 76 + 6 | the old text read "desireless yet ruled by desire" (इच्छा = चाह) |
| *siyā*: कभी → कुछ स्थितियों में | 52 | modal "in some cases", not "sometimes" |
| *mucchā*: मूर्छा → मदहोशी | 9 | मूर्छा = fainting |
| *assutavā*: अशिक्षित → उपदेश से अनजान | 4 | अशिक्षित = illiterate; «उपदेश न सुनने वाला» would read "won't listen to advice" |
| *anottappa*: बुराई के प्रति निडरता → बुराई से न डरने की वृत्ति | 66 | निडरता reads as praise |
| *āghāta*: आक्रोश → रोष | 35 | आक्रोश = outcry |
| *maññanā, maññitatta*: मान लेना, मान चुका होना → अपने को कुछ मानना, अपने को कुछ मान बैठना | 2 | "assume", not conceit |
| *āsevanā*: निरंतर सेवन → निरंतर आचरण | 2 | सेवन = consuming |
| *dukkhapaṭipadā*: दुःखद प्रगति → कष्टदायक प्रगति | 147 | दुःखद = sad |
| *amanussa*: अमानवीय → मनुष्येतर प्राणियों | 4 | अमानवीय = inhumane |
| *khārika*: खारा → क्षारीय | 4 | खारा = salty, the same as *loṇika* |
| *nāma*: मानसिक पक्ष → अभौतिक पक्ष | 5 | *nāma* includes the unconditioned element |
| *nevasaññānāsaññā*: न अ-पहचान → न पहचान के अभाव | 9 | अ-पहचान is not a Hindi word |
| *paritta* / *appamāṇa* jhāna with its object: «स्वयं X और X विषय वाला» (40), «स्वयं सीमित, पर अपरिमित विषय वाला» / «स्वयं अपरिमित, पर सीमित विषय वाला» (40) | 80 | it read as one object both limited and unlimited |
| kamma-born and mind-born lists: , जैसे → , यानी | 48 | a closed list, not examples. No dash: dash counts follow the Pāli |
| ^1-1050, ^1-1051 *ajjhattaṃ paccattaṃ*: grammatical Hindi | 2 | «के स्वयं में, अपनी» was not grammatical |
| title, heading ^1-0 and colophon: धम्मसंगणी (परिघटनाओं की गणना) | 3 | the book's name was missing |

## Termbase

- **Same changes as the text:** 43 *viññāṇa* entries, plus the entries for the words above.
- **New senses:** *sīla* (नियम, in *sīlabbata*) and *dukkha* (कष्टदायक, in *dukkhapaṭipadā*).
- **Termbase-only defects** (the text was already right):
  - *Natthi*: «व्यर्थ और नहीं» → नहीं.
  - *(an)indriyabaddha*: बँधा → न बँधा, and its gloss corrected.

## Checks after the fixes (all pass)

- **Rebuild:** `merge_rails.py`: OK, 1,930 segments, dashes 1,497 (as before).
- **Links:** `verify_transclusions.py`: 1,782 links, all OK.
- **Structure:** `verify_hi.py` (IDs, line counts, headings, dashes and brackets per line, as the Pāli): 14/14 chapters. `check_chapter_ids.py`: 14/14.
- **Alignment:** `align_check.py`: 339 repeated Pāli sentences, none translated differently.
- **Termbase adherence:** 32,529 checks, 27 misses. That is the same set as before the fixes, all inflected forms; one entry now carries its new wording.
- **Old wording:** none of it is left in the text.

## Independent verification (2026-11-27)

The corrected text was reviewed again, against plain.md and the scholar check: 52 kinds of change, two examples each, plus 166 blocks across the book. Report: `review/verify-hi.md`. Verdict: safe for the plain audience and for the scholar check, with corrections.

Corrections made after that review:
- **Two agreement errors the first run had introduced:** «होने वाली शरीर का विज्ञान» (2 places) and «छह प्रकार की विज्ञानों» (2 places).
- ***sakkāyadiṭṭhi* wording:** it now covers all four modes.
- ***assutavā* wording:** उपदेश से अनजान.
- **The mixed limited/unlimited lines:** «स्वयं X, पर Y विषय वाला».
- **Termbase:** the *sakkāya* and *sakkāyadiṭṭhi* glosses.

All checks were rerun after these, with the same results as listed above.

Then, on the user's go-ahead:
- **"X का / के विज्ञान" → "X से होने वाला / वाले विज्ञान"** for the six senses (आँख, कान, नाक, जीभ, शरीर, मन): 207 places in the text, 30 in the termbase. It stops a plain reader taking मन का विज्ञान as "psychology" or शरीर का विज्ञान as "physiology". In the 2 places after a participle there is a comma: «दुःख के साथ होने वाला, शरीर से होने वाला विज्ञान». All checks were rerun with the same results.

## Final review (2026-11-27)

A fresh reviewer, who had not seen the earlier review, checked the whole corrected text from the two perspectives: plain.md, and a scholar reading it against the Pāli. It looked at all 56 kinds of change and 163 blocks across the book. Report: `review2/final-review-hi.md`.

Verdicts:
- **Audience:** suitable, with 4 corrections.
- **Scholar check:** holds up, with the same corrections.
- **Display:** correct (structure identical to the original; only the title, now with the book's name, and the revision note changed).

The 4 corrections, each confirmed by hand and applied:
- **^1-1050, ^1-1051 *upādiṇṇā*:** «कर्म से उत्पन्न» → «ग्रहण की हुई» (2 places). The vault's own aṭṭhakathā on 1050: *"Upādiṇṇāti sarīraṭṭhakā. Te hi kammanibbattā vā hontu mā vā … idha upādiṇṇāti vuttā"*. This was in the text before the fixes. The termbase entry gets this as a second sense.
- ***amanussasadda*:** «मनुष्येतर प्राणियों की ध्वनि» → «मनुष्येतर ध्वनि» (4). The aṭṭhakathā says *"Taṃ ṭhapetvā seso sabbopi amanussasaddo"*: every sound other than human speech.
- **^1-579 to ^1-581:** «होने वाला चौथे ध्यान को» → «होने वाले चौथे ध्यान को» (4; agreement, older than the fixes).
- **^1-1388, ^1-1404:** «दुःख के साथ होने वाला, शरीर से होने वाला विज्ञान» → «शरीर से होने वाला वह विज्ञान जो दुःख के साथ होता है» (2). The comma version read as two items in the list.

All checks were rerun after these, with the same results as listed above.

For the human reviewers (only a native reader or a specialist can settle these):
- Plain readers may still read the bare विज्ञान in lists as "science".
- *niyatā* «उन्हीं से बँधी»: the commentary glosses it *attani jātā*, "arisen in oneself".
- In the *sīlabbataparāmāsa* wording, «शुद्धि का मार्ग» uses मार्ग, which is also the word for *magga*, the path.
- Is «चार-चार / पाँच-पाँच की विधि» (the four- and five-fold jhāna method) clear?
- The Pāli source has a stray «ः» at ^1-1123 and ^1-1241. That is a source-file matter, not a translation one.

## Not changed, on purpose

- **For the reviewers' term list (vocabulary policy):**
  - *citta* / *mano* (मन)
  - *samādhi* / *ekaggatā* (एकाग्रता)
  - मोह, क्लेश, समभाव (*upekkhā*), क्षमता (*indriya*), तत्परता (*paggāha*), जकड़न (*yoga*)
  - *mānasa* (मानसिक क्रिया): मानस is already the word for *mano*
- **Third-jhāna *kāyena*:** the text says काया से, a literal and faithful rendering. "Mental body" is the commentary's reading.
- **^1-850 «…मन वाले व्यक्ति की जो वाणी»:** *kusalacittassa* has the same form as in the bodily-expression line, where it agrees with the participles ("of one who has a wholesome mind").
- **Termbase phrases with "…":** a deliberate gap marker the adherence check relies on.
- **Pipeline intermediates not updated:** the zero-shot draft, the Hindi keyword map and the senses file.
