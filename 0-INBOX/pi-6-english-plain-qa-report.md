# pi-6 English (plain) — translation QA, 2026-11-06

**File:** `AI_translation/english/pi-6-english-plain.md` (status: draft)
**Checked against:** `1-SOURCES/Text/pi-6.md` (Pāli), the termbase `AI_translation/english/pi-6-pali-english-termbase-plain.md` and the audience profile `AI_translation/audience_profile/plain.md`.
**Method:** first, scripted checks of all 3,128 blocks. Then 15 reviewers, none of whom made the translation, each read one group of chapters block by block against the Pāli. Every block was in a reviewer's batch. Major findings and the Pāli problems that change the English were then re-checked by hand, and each confirmed problem was searched for across the whole book.
**Fixes:** applied 2026-11-06 with `AI_translation/pi-6-rails-scripts/qa_fix.py`, in the split chapters and the merged file. 213 blocks changed. See "Fixes applied" below for what was left alone.

## Verdict

The translation is accurate and the question-and-answer logic holds. There are **no critical errors**: no lost negation, no wrong tense and no swapped terms were found, including in the double negatives (*no ca … nuppajjati* → "does arise").

There was **1 major** error, repeated in 17 blocks (141 places), and it is now **fixed**. There are also **9 blocks where the Pāli itself looks wrong and the English repeats it**; these still need an editor's decision. Most minor issues are fixed too, and the Pāli spelling slips don't affect the English.

## Scripted checks

| Check | Result |
|---|---|
| IDs, order, line counts and heading levels against the Pāli | 3,128 of 3,128 match |
| Split chapters against the merged file | identical; 44 files, no missing or duplicate IDs |
| *Āmantā* → "Yes" | 2,578 = 2,578 |
| *Na vattabbo* → "not to be called" | 221 = 221 |
| *Natthi* → "There is no such case" | 2 blocks flagged, both read correctly |
| (Ka)/(Kha) labels | same sequence in every block |
| Numbers | none missing |
| *…pe…* with no ellipsis in the English | 0 |
| Order of terms and of arise/cease verbs, clause by clause | 197 term and 81 verb flags; reviewers read each one and found no translation error behind them, though several trace to the Pāli problems below |

## Fixes applied

After the fixes, all 3,128 blocks still match the Pāli (IDs, order, line counts, heading levels), the split chapters still match the merged file, *Āmantā* → "Yes" is still 2,578 = 2,578, and every old wording is gone. The new wording was not re-read block by block by reviewers; it was checked by script and by sampling.

| Fix | Changes |
|---|---|
| Split groups joined (major) | 141 |
| "several existences" reworded ("remaining women, will pass through several more existences") | 142 |
| "in what is not included" → "in what is not included in the realms" | 311 |
| "wherever – does" → "in a given place – does" | 270 |
| ^6-9 questions ("Are wholesome phenomena wholesome?") | 69 |
| Run-on Pure Abodes group | 29 |
| Variant notes moved | 9 |
| Headings, punctuation, other small wording | 12 |

**Run `qa_fix.py` again after regenerating any chapter**, because the rule scripts don't contain these fixes.

**Left alone:**
- **The 9 doubtful Pāli blocks and the 4 copied wrong labels:** the English follows the printed text, which tipitaka.app also prints.
- **Headings stuck in a body block and the stray "4" (^6-6-65) and "9" (^6-7-311):** these sit on their own lines inside a block, line for line with the Pāli. Removing them means changing `1-SOURCES` and the block structure, so that is a separate decision.
- **"the faculty of displeasure":** optional and consistent, so unchanged.

**Corrected finding:** ^6-9-229 is not a real problem. The next book's homage is already on its own line, and the review format had only made it look joined.

## Major — meaning a reader would get wrong (now fixed)

**One group in the Pāli is split into two in the English.**

| Blocks | Pāli | English now | Problem | Suggested fix |
|---|---|---|---|---|
| ^6-10-368, ^6-10-369, ^6-10-378, ^6-10-379, ^6-10-387, ^6-10-388, ^6-10-397, ^6-10-398 (36 places) | *pacchimabhavikānaṃ purisānaṃ upapajjantānaṃ* / *itthīnaṃ upapajjantīnaṃ* | "For those in their final existence and those being reborn as men" / "those in their final existence, those being reborn as women" | The Pāli means men or women in their final existence who are being reborn. As written, the English says everyone being reborn as a man will have no further life faculty. In ^6-10-369 the next sentence then contradicts it: "For the others being reborn as men … the life faculty will arise too." | "For men in their final existence being reborn" / "For women in their final existence being reborn" |
| ^6-10-396 (1 place) | *pacchimabhavikānaṃ saghānakānaṃ upapajjantānaṃ* | "For those in their final existence and those being reborn with a nose" | Same error. | "For those in their final existence being reborn with a nose" |
| ^6-10-277 (1 place) | *suddhāvāsānaṃ upapajjantānaṃ asaññasattānaṃ* | "For those in the Pure Abodes, those being reborn and non-percipient beings" | Same error. The Pāli means beings in the Pure Abodes who are being reborn. | "For those being reborn in the Pure Abodes and for non-percipient beings" |

| ^6-10-366 – ^6-10-369, ^6-10-376 – ^6-10-379, ^6-10-385 – ^6-10-388, ^6-10-395 – ^6-10-398 (103 places) | *… parinibbāyissanti tāsaṃ upapajjantīnaṃ* / *tesaṃ cavantānaṃ* | "… and attain final nibbāna and those being reborn" / "and those passing away" | Same error, found while writing the fix: the Pāli means those same people, at the time they are being reborn or passing away. | "… and attain final nibbāna, when they are being reborn" / "when they are passing away" |

These most likely come from one list rule in the scripts. The reviewers flagged only part of this as minor; the whole-book search and the fix work found the full set of 17 blocks.

### Reported as major, rejected on re-check

^6-10-408, ^6-10-409, ^6-10-418, ^6-10-419, ^6-10-431 and parallels: *pacchimacittasamaṅgīnaṃ yassa cittassa anantarā … pacchimacittaṃ uppajjissati*. A reviewer said this is one group and the English wrongly makes it two.

The English is right, and these are two groups: those who have the final consciousness now, and those whose final consciousness is still to come (*uppajjissati*). Nobody can have the final consciousness and also have it still to come. ^6-10-418 and ^6-6-47 use a comma where others use "and", which is only a style difference.

## The Pāli looks wrong, and the English repeats it

In each of these the Pāli breaks the pattern of its neighbours. The English follows the Pāli as printed, so a reader gets the odd reading. **Checked on tipitaka.app on 2026-11-06: all of these, and the wrong labels below, are printed exactly the same there.** So they are not copying mistakes on our side, and the English matches the published text. tipitaka.app is the same Chaṭṭha Saṅgāyana text as the source, so this does not settle whether each reading is a slip in that edition. The English is left as printed.

| Block | Pāli as printed | English now | Likely reading |
|---|---|---|---|
| ^6-7-243 | *tato mānānusayaṃ parijānātīti?* | "does one fully understand the underlying tendency to conceit there?" | *na parijānātīti*: the question loses its "not", and the answer that follows no longer fits |
| ^6-6-121 | *kāyasaṅkhāro na nirujjhittha vacīsaṅkhāro ca nirujjhissati* | "the bodily formation has not ceased there, and the verbal formation will cease there" | *kāyasaṅkhāro ca nirujjhittha*: "has ceased … too" |
| ^6-9-192 | *no ca tesaṃ tattha kusalā dhammā uppajjissanti* | "but wholesome phenomena will not arise there" | *akusalā*: the question is about unwholesome phenomena |
| ^6-10-357 | *sotindriyañca na uppajjittha* | "the ear faculty has not arisen there either" | *somanassindriyañca*: the question is about the joy faculty |
| ^6-10-361 | *somanassindriyaṃ na uppajjati, no ca … jīvitindriyaṃ na uppajjittha* | "the joy faculty does not arise there, but the life faculty has arisen there" | The tenses are swapped against the question |
| ^6-10-240 | *purisindriyaṃ uppajjittha tattha cakkhundriyaṃ* | "has the eye faculty arisen there?" | *tassa*: "arisen for them?" |
| ^6-4-15 | *na dhātū na kāyadhātūti?* | "not the body element" | *na kāyo* (the pattern of its neighbours) |
| ^6-4-17 | *avasesā dhātū na cakkhudhātu* | "the remaining elements are not the eye element" | *na cakkhu, dhātu* (as ^6-4-15 and later in the same block) |
| ^6-9-49, ^6-9-55 | *dutiye akusale citte* | "the second unwholesome consciousness" | Possibly without *akusale*; low confidence |

**Wrong labels copied into the English** (*Ka* where *Kha* is expected, or the reverse, so the English shows the same letter twice): ^6-2-61, ^6-3-50, ^6-10-140, ^6-10-293.

**Pāli slips where the English is already right** (no English change):
^6-2-36, ^6-2-111, ^6-2-134, ^6-2-163, ^6-2-185, ^6-3-13, ^6-3-43, ^6-3-75, ^6-3-100, ^6-3-116, ^6-3-118 (a stray "=93"), ^6-3-212, ^6-3-244, ^6-5-74, ^6-5-76, ^6-5-125, ^6-7-7-0, ^6-7-21, ^6-7-25, ^6-7-35, ^6-7-130, ^6-7-335, ^6-7-349, ^6-8-83, ^6-10-3, ^6-10-206, ^6-10-309, ^6-10-385, ^6-10-398, ^6-10-452, ^6-10-454, ^6-10-480.

## Minor (as found; see "Fixes applied" for what changed)

**Headings stuck to the end of a body block** (in both the Pāli and the English; the fix also touches segmentation):
- ^6-6-2, ^6-6-4 ("(b) Negative")
- ^6-6-65 ("4 (e) Negative: Place", with a stray "4")
- ^6-8-82 ("(14) The Section on Time Having Passed")
- ^6-9-16 ("(b) Explanation")
- ^6-9-120 ("(f) Negative: Person and Place")
- ^6-9-135 ("(c) Positive: Person and Place")
- ^6-9-229 (the next book's opening homage)

**Stray characters and punctuation:**
- ^6-7-311: stray "9"
- ^6-7-325: ". ;"
- ^6-10-434: missing ")"
- ^6-2-130: an ellipsis the Pāli does not have

**Variant note in the wrong place** (it should follow the word it varies): ^6-5-33, ^6-5-61, ^6-5-69, ^6-7-270, ^6-10-441, ^6-10-465, ^6-10-466.

**Same heading worded two ways:**
- ^6-7-5-0, ^6-7-6-0, ^6-7-7-0
- ^6-7-8-0, ^6-7-9-0
- ^6-7-10-0, ^6-7-11-0
- ^6-8-82 against the other (14) headings

**Hard for a plain reader:**
- ^6-9-1, ^6-9-2, ^6-9-6 – ^6-9-8, ^6-9-17, ^6-9-18, ^6-9-22 – ^6-9-24: "Is wholesome phenomena what is wholesome?" and "Is what is not what is wholesome not wholesome phenomena?"
- ^6-7-46 – ^6-7-65: "in what is not included" does not say in what
- ^6-7-88 – ^6-7-98: "Whoever … wherever"
- ^6-7-343, ^6-7-349: "no such thing as rebirth in neither … nor"
- ^6-10-95, ^6-10-124, ^6-10-125: "but it is a woman" / "but it is a man"
- ^6-10-281 – ^6-10-284, ^6-10-300 – ^6-10-302, ^6-10-308 – ^6-10-311, ^6-10-326 – ^6-10-329: "will show several existences", in two word orders
- ^6-10-255, ^6-10-276: a list of two groups reads as one run-on phrase

**Style:** "the faculty of displeasure" breaks the "X faculty" pattern used by the other faculties. It is consistent, so this is optional.

## Still open

- **Six term choices not yet confirmed:**
  - *aññindriya* = "faculty of knowledge" (a placeholder)
  - *dhamma* = "phenomena"
  - the *-dhātu* spheres = "element"
  - *vitakka* / *vicāra* = "thought and holding the thought"
  - *nirodha* = "ending" beside "cease"
  - *sukha* = "pleasure"
- **Pāli problems:** they match tipitaka.app, but no different edition has been compared.
- **The method:** reviewers can miss things. They caught only part of the major error, and the whole-book search and fix work found the rest. A clean result here is strong evidence, not proof.
