# pi-1 Hindi measured against the scholar profile, as a target (2026-11-27)

The question: is the current Hindi pi-1 (commit 329f385e) a translation that meets the scholar profile?

Profiles used:
- `AI_translation/audience_profile/scholars.md`
- `pali-english/audience_requirments/skills/audience_scholarly.md`, for what "scholarly" means in practice

Each criterion was measured on the text. Scholarly Hindi terms are taken from the Hindi Abhidhamma books (Tripathi and the Lucknow 1960 Abhidhammattha-saṅgaha), counted locally.

| # | Criterion (scholars.md) | Measured on the Hindi pi-1 | Result |
|---|---|---|---|
| 1 | Technical terms retained in transliteration at first occurrence, with a gloss (*vedanā* (वेदना)) | 0 Pāli terms in transliteration in the running text | **Fails** |
| 2 | Technical terminology: the most precise term, no paraphrase "for accessibility", do not simplify | Of 73 key terms checked, 26 use the scholarly Hindi term and 47 use a plain paraphrase. Examples: समूह for स्कन्ध, अनुभूति for वेदना, पहचान for संज्ञा, मानसिक रचनाएँ for संस्कार, हितकर for कुशल, परिघटना for धर्म, कर्म के फल रूपी for विपाक, इंद्रिय-सुखों के लोक से संबंधित for कामावचर. In the termbase, 681 of 1,945 single Pāli words are rendered by a phrase of 3 or more words | **Fails** |
| 3 | No simplification of philosophical distinctions | *samādhi* and *ekaggatā* are both एकाग्रता (25 lines). मन stands for *citta* and in places for *mano* / *mānasatā*. Kept apart: *cetanā* इरादा and *viññāṇa* विज्ञान, *phassa* संपर्क and *phoṭṭhabba* स्पर्श | **Partly fails** |
| 4 | No explanatory additions, no clarifying words | Plain-profile clarifications in the text, for example: «X से होने वाला विज्ञान» (about 175–207), «कारणों पर आश्रित» (70+ lines), «कुछ स्थितियों में» (52), «, यानी» (57), «को ही शुद्धि का मार्ग मानने की» (29), «स्वयं …» (40), «पाँच समूहों के संबंध में» (14) | **Fails** |
| 5 | Literal, close syntax; argument structure kept | Line-by-line structure, list order and numbering match the Pāli (verify_hi 14/14, block IDs, 1,782 links, repeated sentences identical). The sentence wording is idiomatic, not literal | **Structure passes, syntax partly** |
| 6 | Preserve ambiguity rather than resolving it silently | Kept where it could be (*kāyena* = काया से). Some readings follow the commentary (*upādiṇṇā* = ग्रहण की हुई, *idappaccayatā* as two objects), which is a reasoned resolution, not a silent one | **Mostly passes** |
| 7 | Formal academic register | A plain, modern register, by design | **Fails** |
| 8 | Accuracy (priority 1) | Two independent reviews: holds up; the clear errors are fixed | **Passes** |
| 9 | Terminological consistency (priority 2) | Termbase adherence: 32,529 checks, 27 misses, all inflected forms | **Passes** |
| 10 | Source apparatus: variant readings, …pe… abbreviations | Variant brackets kept (69); an ellipsis is kept in all 612 blocks with …pe…, but shown as «…», not marked as *pe* | **Passes; …pe… unmarked** |
| 11 | Dhamma / Nibbāna as technical terms (scholarly English profile) | *dhamma* = परिघटना / मन का विषय / शिक्षा; *nibbāna* = निर्वाण | **Partly** |

## Verdict

- **Against the scholar profile as its target: not verified.** It fails criteria 1, 2, 4 and 7 and partly fails 3. These are the defining features of a scholars' version.
- **Not a defect of this translation.** It was made for `plain.md`, and those features are exactly what `plain.md` asks for: everyday words, small clarifications, a modern register.
- **What does pass is the part both profiles share:** accuracy, consistency, structure and the source apparatus (criteria 5, 8, 9, 10).
- **A text that meets the scholar profile has to be a separate Hindi scholar version,** built from the same rails, with:
  - a scholar termbase: the Pāli term in transliteration at first use, plus the scholarly Hindi term (स्कन्ध, वेदना, संज्ञा, संस्कार, विपाक, आलम्बन …);
  - none of the clarifying additions;
  - *…pe…* marked;
  - *samādhi* / *ekaggatā* and *citta* / *mano* kept apart.

  In the vault this is a separate track, the same way the English pipeline has a separate scholarly version (`pali-english/en-dhammasangani-ai-auto-scholarly-1.md`, Mātikā only, with its own termbase).
