# pi-4 English (plain) — translation QA, 2026-11-05

**File:** `3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/pi-4-english-plain.md` (status: draft)
**Checked against:** `1-SOURCES/Text/pi-4.md` (Pāli), the locked termbase `AI_translation/english/pi-4-pali-english-termbase-plain.md`, the audience profile `AI_translation/audience_profile/plain.md`, and the method in `AI_translation/skills/rails-verse-translator.md`.
**Method:** a scripted check of all 250 blocks, then a block-by-block reading of the English against the Pāli in five parts. The three major findings were then re-checked by hand. There is no `translation-qa` skill yet (it is listed as planned in `SKILLS-CATALOG.md`), so this follows the catalogue's description of one: accuracy, terminology, register, severity.

## Verdict

The translation is accurate and well made. No critical errors: no reversed negation, no swapped members in the two-variable fours, and no wrong subject in the stock formulas. The long lists and similes are complete and mapped correctly. **3 major** errors and about **45 minor** issues remain. Most of the minor ones, and two of the majors, come from the termbase rather than from the translating.

## Scripted checks — all pass

- 250/250 blocks have the same IDs, order and line count as the Pāli. All 226 content blocks have their root transclusion.
- Numbers match in every block. Every `…pe…` elision is kept.
- Variant readings are carried over consistently as `[variant: … (Syā.)]`, in 52/52 blocks.
- Each Pāli person-type name has a single English rendering; no name is rendered two ways.

## Major (meaning a reader would get wrong)

> **Fixed 2026-11-05** in the translation, the termbase, and the live prod edition `E9ox1ON9xZVrrjoaE5sHJ`.
> - ^4-57: "Since" → "Although" (×2); the positive formula in ^4-77 / ^4-181 was already correct.
> - "is (not) endowed with learning" → "(does not) live(s) up to their learning" (×12).
> - "judges by the teaching … the teaching" → "judges by spiritual qualities … spiritual qualities" (×6).
> - Applied live with 8 `PATCH /v2/editions/{id}/content` REPLACE ops. The server shifted the segment and TOC spans; segment IDs, TOC and alignment are unchanged.
> - The working copies under `AI_translation/english/` (`pi-4-english-plain.md` and the split chapters) still have the old wording.

| Block | Pāli | English now | Problem | Suggested fix |
|---|---|---|---|---|
| ^4-M-10, ^4-189 (all 4 members) | *appassuto / bahussuto sutena anupapanno / upapanno* | "one with (much) learning who is not endowed with learning" | Reads as a contradiction. The block itself defines *sutena upapanno* as knowing the meaning and practising accordingly. Comes from the termbase (`sutena upapanno → endowed with learning`). | "…who does not live up to their learning" / "…who lives up to their learning"; fix the termbase entry |
| ^4-57 (eye and mind sentences; parallel ^4-77) | *yatvādhikaraṇam enaṃ cakkhundriyaṃ asaṃvutaṃ viharantaṃ … anvāssaveyyuṃ, tassa saṃvarāya na paṭipajjati* | "Since, if they lived with the eye faculty unrestrained, covetousness … might flow in upon them, they do not practise to restrain it" | "Since" makes the danger the reason for *not* restraining. The Pāli says they fail to restrain the faculty through which, left unrestrained, bad states would flow in. | "They do not practise restraint of the eye faculty, even though, if they lived with it unrestrained, … might flow in upon them"; in ^4-77, "They practise restraint …, since if …" |
| ^4-172 | *dhammappamāṇo dhammappasanno* | "judges by the teaching and is won over by the teaching" | The definition is "having seen virtue, concentration or wisdom", i.e. a person's qualities, not the doctrine. | "judges by (spiritual) qualities and is won over by them" |

## Minor

**Terminology inconsistency** (mostly from the termbase)
- *sīla*: "moral discipline" vs "morality" within pairs — ^4-M-8, ^4-M-9, ^4-61/^4-81, ^4-92, ^4-116/117, ^4-121–123, ^4-126.
- *nirodha*: "ending" vs "cessation" — ^4-M-5 vs ^4-27/28; ^4-185, ^4-198.
- *sukha/dukkha*: "pleasure"/"happiness" and "suffering" for bodily pain, inside one formula — ^4-183; ^4-M-6 *dukkhindriya* "suffering faculty" (pain faculty).
- *hirī/ottappa*: "conscience"/"moral fear" vs termbase "moral shame"/"fear of wrongdoing" — ^4-203.
- *sovacassatā* "being amenable" vs pair "hard to correct" — ^4-55/^4-75.
- *sappuriso* vs *kalyāṇo*: "a good person" / "one who is good" — two different types are indistinguishable — ^4-134/138, ^4-135/139.
- *muṭṭhassati* "forgetful" vs *upaṭṭhitassati* "mindfulness established": the shared stem is hidden — ^4-59/^4-79.

**Small meaning or clarity slips**
- ^4-M-7, ^4-37 *upahaccaparinibbāyī* "on arrival": a recognised rendering, but ambiguous for lay readers; the definition means "near death". Reviewers disagreed on it.
- ^4-3–8 *na nikāmalābhī*: "have not gained them at will" — this is an ability ("cannot attain them at will").
- ^4-12/13: "hindered by results" (of past actions); *niyāma* dropped from "course of rightness".
- ^4-M-11 *datvā avajānāti*: "looks down on others" — it is the recipient.
- ^4-M-13 *ummujjitvā ṭhito*: "stays established" → "stays in place".
- ^4-M-10 *āsīvisūpamā*: "snakes" → "venomous snakes".
- ^4-116: "Even old coarse cloth is used for scouring pots" — "Even" inverts the point.
- ^4-124/126: "a bad reputation still spreads about them" — the referent is ambiguous (the companion is meant).
- ^4-137/139/141/143: "encourages others to divisive speech / to covetousness …" is ungrammatical.
- ^4-145/146 *vajjabahulo*: "with much blame" reads as being blamed by others (→ "mostly blameworthy").
- ^4-152–155 *yutta/mutta-paṭibhāno*: "ready understanding … fluent" — opaque (about replies).
- ^4-166: "they do not speak of it truthfully, accurately, at the right time" can be read as speaking untruthfully.
- ^4-167 *uṭṭhahato*: "getting up" → "rousing effort".
- ^4-171 *ghosappamāṇo*: "judges by voice" — the definition is about reputation.
- ^4-173 *vimuttiñāṇadassana*: "vision of liberation" drops "knowledge" (×10).
- ^4-182 *sutte jāgarite*: "asleep, awake" → "falling asleep and waking up".
- ^4-193/197 *haññati byāpajjati*: "struck and wounded" understates it ("struck down and ruined").

**Plain-register problems** (opaque for a reader with no background)
- Untranslated, unglossed: *Tathāgata* (^4-27/28, ^4-90, ^4-94/96/97, ^4-177, ^4-208 — no termbase entry), *jhāna* (^4-183, ^4-198), *Sangha* (^4-116/117).
- Jargon: "becoming" (*bhava*, ^4-33, ^4-M-9, ^4-110–112), "aggregate of moral discipline" (*sīlakkhandha*, ^4-123), "the course of rightness" (^4-94), "doors of the faculties" (^4-M-8), "a tangible" (^4-57/77), "displeasure / tight hold of consciousness" (^4-45/65, ^4-50/70), "upturned" wisdom (*avakujja*, ^4-M-9, ^4-107 — can mean face-up), "There is nothing given …" (^4-62/82, read literally).

## Termbase problems (root cause of many items above)

- **Junk (rendering = Pāli or wrong):** `vuccati → vuccati`, `kho → kho`, `neva → neva`, `ceva → ceva`, `karoti → karoti`, `paranimmitavasavattideve`, `paccekabuddho` (left in Pāli; conflicts with `paccekasambuddho → Solitary Buddha`), `na → cannot`, `sā → dog` (right only in ^4-174; elsewhere *sā* = "she/that").
- **Fragments, unusable as locked terms** (about 50): e.g. `Katamo → kind`, `kāyena → body`, `lābhī → gained`, `appameyyo → cannot`, `suppameyyo → easy`, `byāpatti → ill`, `kodhano → angry`, `akkodhano / anissukī / amaccharī → free`, `sampajānakārī → act with clear`, `cetovimuttiṃ paññāvimuttiṃ → mind and liberation`, `vuccati ahirikaṃ / anottappaṃ / asampajaññaṃ → called lack`, `ummujjati → comes`, `ārabhati → wrong`, `bhagavatā → blessed`.
- **Wrong or misleading:**
  - `sutena upapanno → endowed with learning`
  - `upahacca → arrival` (contradicts its own gloss)
  - `dhammā → teachings` (in this book often "states")
  - `ghosa → voice`
  - `vimuttiñāṇadassana → vision of liberation`
  - `byāpajjati → wounded`
  - `vaṇṇo → appearance` (also "praise")
  - `appa → few`
  - `dukkha → suffering` for bodily pain
  - `narassa → city`
  - `potthake → manuscript` vs `potthaka → cloth`
- **Self-contradicting:** *sīla* (moral discipline / morality), *nirodha* (ending / cessation), *hirī* (moral shame / conscience), *ottappa* (fear of wrongdoing / moral fear).
- **Missing:** *tathāgata*, *kalyāṇo*, *diṭṭhippatto*, *nirāso / vigatāso*, *sīlakkhandha*.

The translator correctly overrode many of the junk entries (e.g. it uses "states" for *dhammā*, "praise" for *vaṇṇo*, and the full name of the Paranimmitavasavatti gods). The rails-verse-translator skill says such cases should be flagged and the termbase fixed, rather than quietly overridden.
