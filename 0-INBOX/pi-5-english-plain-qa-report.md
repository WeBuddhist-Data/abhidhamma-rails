# pi-5 English (plain) — translation QA, 2026-11-05

**File:** `AI_translation/english/pi-5-english-plain.md` (status: draft; not yet published to the track)
**Checked against:** `1-SOURCES/Text/pi-5.md` (Pāli), the termbase `AI_translation/english/pi-5-pali-english-termbase-plain.md`, the audience profile `AI_translation/audience_profile/plain.md`, and the fixed debate-formula sheet used for the run.
**Method:** first, a scripted check of all 1,400 blocks. Then seven reviewers, none of whom made the translation, each read one chapter group block by block against the Pāli. Every major finding was then re-checked by hand against the Pāli before it was fixed. There is still no `translation-qa` skill, so this follows the pi-4 QA report: accuracy, terminology, register, severity.

## Verdict

The translation is accurate, and the debate logic holds throughout. There are **no critical errors**: no lost negation, no question turned into a statement, no thesis given to the wrong side, and no X/Y terms swapped in the paired and permuted question sets.
- Those sets include the past/present/future grids, the fixed/unfixed grid, the passing-from-jhāna-to-jhāna sets, and the mundane/supramundane faculty sets.
- Long lists, sutta quotations and verses are complete and correctly mapped.

**7 major** errors were found, and all 7 are now **fixed**. About **95 minor** issues were found. Most of them, and two of the majors, came from the termbase rather than from the translating. They were applied on 2026-11-06, except for the few that would override a locked termbase rendering; those are listed below.

## Scripted checks — all pass

- All 1,400 blocks match the source: same IDs, same order, same line count.
- Each block keeps the same count as the Pāli of each of these:
  - Āmantā → "Yes"
  - Na hevaṃ vattabbe → "That should not be said"
  - Ājānāhi niggahaṃ / paṭikammaṃ
  - micchā → "is wrong"
  - Hañci → "If"
  - …pe… elisions
  - variant notes
  - numbers
- 16 blocks were flagged, and all were checked by hand. They are false positives: editorial notes that were translated, *nanu* rendered "isn't it the case", and source oddities such as an empty "( )" answer slot.
- Citations match the Pāli count exactly: 44 Ma. Ni., 54 Saṃ. Ni., 59 A. Ni., 22 Dī. Ni.
- Every *ābhoga* rendering was checked one by one against the Pāli before the "concern" fix.

## Major — all fixed in the split chapters and the merged file

| Block | Pāli | Was | Problem | Now |
|---|---|---|---|---|
| ^5-14, ^5-15, ^5-16 (×5 each) | *sabbattha / sabbadā / sabbesu … nupalabbhati* | "not found everywhere / at all times / in all things" | Reads as "found in some places but not all", which changes the thesis being pressed. | "not found anywhere / at any time / in anything" |
| ^5-296 | *ukkalā vassabhaññā ahetukavādā akiriyavādā natthikavādā* | "those people of Ukkalā, Vassa and Bhañña, who taught … that there is no action, that nothing exists" | *Natthikavāda* is moral nihilism, not "nothing exists". In the chapter on "everything exists", the wrong reading puts these teachers on the opposite side. Vassa and Bhañña are two teachers from Ukkalā. | "Vassa and Bhañña of Ukkalā, who taught that there is no cause, that actions have no effect, and that good and bad deeds bear no fruit" |
| ^5-576, ^5-580, ^5-584 | *na apubbaṃ acarimaṃ uppajjanti* | "they do not arise neither before nor after one another" | The double negative reads as "they arise at the same time", the opposite of the Pāli. | "they do not arise simultaneously with one another" |
| ^5-527 – ^5-604 and heading ^5-18-5-1-0 (49 places) | *ābhoga / anābhoga / sābhoga* | "concern", "without concern", "Discussion of Having Concern" | A plain reader hears "worry", so "the five kinds of consciousness are without concern" reads as "indifferent". From the termbase (`ābhoga → concern`). | "mental engagement", "without mental engagement", "one who (does not) mentally engage(s) with it", "Discussion of Having Mental Engagement" |
| ^5-401 (×2) | *samantā byāmaṃ obhāsati* | "shines a span all around" | A *byāma* is the length of the outstretched arms, not a hand-span. From the termbase (`byāmaṃ → span`). | "shines an arm-span all around" |
| ^5-317, ^5-321, ^5-325 (×9) | *maggāmaggaṃ na jāneyya / kaṅkheyya* | "the right path from/and the wrong one" | A worldly matter, listed with people's names and plant names. As "the right path", our own school appears to concede that an arahant may not know the spiritual path. | "the right road from/and the wrong one" |
| ^5-379 (×5) | *atthi devesu asaṃvaro, yamhā asaṃvarā saṃvaro sīlaṃ* | "non-restraint among the gods, restraint from which non-restraint is moral discipline" | The doubled "non-restraint" garbles the thesis that the refutation targets. | "non-restraint among the gods, such that restraint from that non-restraint is moral discipline" |

The script that applied these fixes is `0-INBOX/temp/pipeline/pi-5/qa_fix_majors.py`. After the fixes, all 32 chapters pass the alignment check, and the merged file was rebuilt (1,400 blocks, IDs identical to the source).

## Minor — applied 2026-11-06

The fixes were applied with `0-INBOX/temp/pipeline/pi-5/qa_fix_minors.py`. Each fix is either scoped to its blocks or checked against the Pāli line. Every fix printed a count, and none was zero. Afterwards all 32 chapters still pass the alignment check, the scripted QA is unchanged, and the merged file was rebuilt (1,400 blocks, IDs identical to `1-SOURCES/Text/pi-5.md`).

**Terms made consistent across the whole book**
- *rāga* is now "lust" everywhere. That is 207 changes, including 10 for *rajjati* "feels lust", plus 42 for *vītarāga* "free of lust". It was applied only where the Pāli line has *rāga*/*rajj-* and no *lobha*, because *lobha* = "greed" is locked.
- *kāmarāga* is "sensual lust" (147 changes). *kāmacchanda* stays "the hindrance of sensual desire".
- *nirodha* is "cessation" everywhere (66 changes, 205 uses in total). ⚑ This goes against the Daily-Tipitaka plan's locked row `nirodha → ending`. The text already used "cessation" 139 times against 58 for "ending", the termbase's own phrase entries say "cessation", and every reviewer asked for "cessation". The same applies to *asaṅkhata* = "unconditioned" against the plan's "the unconstructed". If you want the plan rows followed, both need a book-wide reversal.
- Other renderings now used throughout the book:

  | Term | Rendering | Changes |
  |---|---|---|
  | *phoṭṭhabba* | "tangible(s)" (locked) | 76 |
  | *ānantarika* | "with immediate result" | 30 |
  | *rūpakkhandha* | "aggregate of material form" | 25 |
  | *parassa cittaṃ* | "another person's mind" | 23 |
  | *kāmabhava* | "sense-pleasure existence" | 17 |
  | *dussīla* / *dussilya* | "without / lack of moral discipline" (to match locked *sīla*) | 10 |
  | *sīlabbata* | "rites and rituals" (locked) | 3 |
  | *sabbe dhammā* | "all phenomena" (locked *dhamma*) | 7 |
  | *anantarapaccaya* | "Proximity Condition" | 2 |

- Capitals: "divine ear", "family to family" and "dhamma-follower" are no longer capitalised. "dhamma-follower" is now "follower by the teaching".

**Glosses at first use in each chapter**
- "Tathāgata (the Buddha)" / "Tathāgatas (Buddhas)"
- "peta(s) (hungry ghost(s))", in line with the locked row
- "kasiṇa (a focus disc for meditation)", in line with the locked plan row
- One-off glosses:
  - Jambudīpa, Uttarakuru and the Thirty-Three
  - the four embryo stages
  - bodhisatta, Nigaṇṭhas
  - change of lineage, "accomplished in vision"
  - *pārājika* "defeat"
  - "single seed (one more rebirth)"

**Block-level slips fixed**
- Summary verses: ^5-238 (consciousness and the good) and ^5-918 (the five sets of fifty).
- ^5-195/220/224: "a person". ^5-116/117: "a second moment of consciousness". ^5-233: "nothing but a heap of formations".
- ^5-237/238: "permanent (that is, regular) meal". ^5-53: "distinguishing marks".
- ^5-282: *ayoga* and "the opposing view". ^5-269: *chandikā* "aspiration", the locked *chanda* rendering. ^5-271: "do not go". ^5-273: "at one and the same time". ^5-289: "the physical base".
- The *saṃsāra/yoni* lists in the Asaññakathā. "neither kill … nor take …". ^5-367: *dussamānaṃ* "hateful". "sleep in a bed". The "what is not X" pattern at ^5-353. "faculties of beings". "while they remain in that existence". "a (mundane) meditative attainment". "eye of the teaching".
- ^5-436: quotation-mark placement, and "a mind that is not sublime" (locked *mahaggata*). ^5-390: "the consciousness that seeks rebirth". ^5-493: "wheel-turning king".
- ^5-538: "non-material". ^5-523: "outward form". ^5-558/617: "at the moment of". ^5-605: "indeterminate results". ^5-547: "the benefit in nibbāna". ^5-562: "pleasure / pain / joy / sadness".
- ^5-740: "consciousness breaks up". ^5-702: "unwholesome mind". ^5-747: "the giver's own" and "happiness and suffering". ^5-641: "in the meantime". ^5-665/668: "lustful … lust". ^5-718: "formations". ^5-795: "rice gruel to drink".
- ^5-860–862: "believing that this accords with the Dhamma". ^5-868: "now … now". ^5-877: "things not heard before". ^5-842: "formations". ^5-906: "last for just one moment of consciousness". ^5-897: "doors of the senses".

**Not applied, because they would override a locked termbase rendering** (this needs a decision on the track or plan termbase, not on this text)
- *saḷāyatana*: "six sense-fields" (plan), not "six sense bases".
- *anottappa*: "fearlessness of wrongdoing" (both termbases), not "lack of fear of wrongdoing".
- *domanassa*: "displeasure" (plan), not "grief".
- *bhava*: "becoming" (plan), not "existence", at ^5-217, ^5-273, ^5-455, ^5-719.
- *vicāra*: "holding the thought" (fixed resolution), at ^5-441.
- *upādinna*: "grasped-at" (fixed resolution).
- The realm names "sense-pleasure / material-form / immaterial element", not "realm". This is a book-wide termbase decision, and reviewer 6 notes deliberate puns on *rūpadhātu* at ^5-703/771.

**Not applied for another reason**
- *Nanu …ti?* rendered "But doesn't X…?" instead of the sheet's "But isn't it the case that…?" (about 22 blocks in ch. 16–19). The meaning and polarity are kept, and normalising it would mean rewriting each sentence.

The original minor rows are still in `0-INBOX/temp/pipeline/pi-5/qa5/part1.md` … `part7.md`. The summary below is the state before the fixes.

**Terminology rendered two ways** (mostly from the termbase)
- *rāga*: "lust" (*rāgo*) vs "greed" (compounds), and once "passion". This happens in every chapter group.
- *nirodha*: "ending" vs "cessation". The Nirodhakathā debates "two endings" under a "Cessation" heading, and the third truth is "ending" in prose but "cessation" in the sutta quotations.
- *bhava*: "becoming" vs "existence". The realms: "sense-desire existence" vs "sense-pleasure element"; *arūpa* "formless" vs "non-material".
- *sīlabbata*: "rules and rituals" vs "rites and rituals". *sīla*: "moral discipline" vs its opposite "lack of virtue".
- *dhammā*: "phenomena" vs "states" (*sabbe dhammā*, ^5-887–891 vs ^5-906/907).
- *citta*: "mind" vs "consciousness" inside one argument (^5-116/117, ^5-740).
- *saḷāyatana* "six sense-fields" vs "eye base …". *kāmarāga* and *kāmacchanda* are both "sensual desire".
- "with immediate retribution" (ch. 28) vs "with immediate result" (ch. 16, 21).
- "Divine Ear" vs "divine eye". *Nanu …ti?* appears as both "But doesn't X…?" and the sheet's "But isn't it the case that…?" (about 22 blocks in ch. 16–19; the meaning is kept either way).

**Small meaning or clarity slips**
- ^5-238: the closing summary verse makes consciousness the fifth item; it should be "the good".
- ^5-918: "The great fixed course" merges two of the five sets of fifty.
- ^5-282: "this view is a right view" should be "the opposing view". ^5-273: "neither before nor after" should be "at one and the same time".
- ^5-868: *sakimpi … sakimpi* is "once … once"; it should be "now up, now down".
- ^5-906: "stay for just one consciousness" should be "one moment of consciousness".
- ^5-195/220/224: "that very person" has nothing to refer back to.
- ^5-233: "pure formations" should be "nothing but formations".
- ^5-269: *acchandikā* "without desire" should be "without zeal".
- ^5-641: "intermediate period" can be confused with the intermediate existence of ch. 16.
- ^5-795: "rice gruel and drinks" should be "rice gruel to drink".
- ^5-881/892: "fearlessness of wrongdoing" can read as a virtue (from the termbase).

**Plain-register problems** (opaque for a reader with no background)
- Unglossed: *Tathāgata* (81× in ch. 11 alone; no termbase entry), peta, kasiṇa, bodhisatta, Nigaṇṭhas, Jambudīpa / Uttarakuru, the embryo stages (kalala, abbuda, pesi, ghana), "change of lineage", "Family to Family" / "Single Seed".
- Jargon: "becoming", "grasped-at", "doors of the faculties", "incurred defeat" (Vinaya), "the base" (*vatthu*), "permanent meal … stable gruel" (^5-237).

## Termbase problems (root cause of many items above)

> **Corrected 2026-11-06** in `AI_translation/english/pi-5-pali-english-termbase-plain.md`: 59 terms now match the fixed text (*rāga* family → lust, *nirodha* family → cessation, *ābhoga* → mental engagement, *byāmaṃ* → arm-span, *dussamānaṃ* → hateful, *sīlabbata* → rites and rituals, *dussilya* → lack of moral discipline, *phoṭṭhabba* compounds → tangible(s), `dhammā niyatā` → phenomena are fixed). The termbase still passes its check (5,470 words, 5,614 senses). The locked project termbases under `3-TRANSFORMATIONS/` are unchanged.

- **Wrong or misleading:** `ābhoga → concern` and `byāmaṃ → span` (both caused majors, now fixed in the text but not yet in the termbase); `sā → dog`, `na → nothing`, `kammaṃ → conduct`, `avitathāni → unreal`, `adukkhamasukhaṃ vedanaṃ → pleasant feeling`, `sataṃ → hundred`, `dussamānaṃ → corrupted`. The translators overrode these entries and logged each change.
- **Self-contradicting:** *rāga*, *nirodha*, *bhava*, *sīlabbata*, *dhammā*, *lokiya/lokuttara* (the text uses "mundane/supramundane" throughout), *asaṅkhata* (the text uses "unconditioned" throughout, against the locked plan row "the unconstructed").
- **Missing:** *tathāgata*, *maggāmagga*, *natthikavāda*, *akiriyavāda*.
- **Cut-off fragments:** about 580 logged completions across the seven translator notes (`0-INBOX/temp/pipeline/pi-5/rails5-notes-all.txt`).

As the pi-4 report also noted, the rails-verse-translator skill says such cases should be fixed in the termbase rather than overridden quietly in the text.
