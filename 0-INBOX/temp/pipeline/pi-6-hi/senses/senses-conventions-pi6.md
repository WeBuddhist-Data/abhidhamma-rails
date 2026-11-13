# pi-6 (Yamaka) Pāli→Hindi senses: conventions beyond pi-1 (for parts 1–3)

Settled on the sample (agg-sample.tsv = the first 120 headwords of part 1) and a survey of agg-part1..3.
Still binding: the brief (`..\hi-senses-brief.md`), the skill (`AI_translation\skills\word-sense-grouper.md`), the pi-1 file `..\..\pi-1-hi\senses\senses-conventions.md` (tag style, grammar labels, the fixed tag patterns, the merge/split rules, the family table) and the approved pi-1/pi-2 senses files. This file only fixes what pi-6 adds. The values themselves are explained in `..\mapper-hi\hi-map-conventions-pi6.md`.

## 1. Workflow

```
python -I -X utf8 senses_tool_pi6.py todo   agg-partK.tsv decisions-partK.txt
python -I -X utf8 senses_tool_pi6.py show   <headword> "<hindi value>" [<max segs>]
python -I -X utf8 senses_tool_pi6.py build  agg-partK.tsv decisions-partK.txt partK-senses.md
python -I -X utf8 senses_tool_pi6.py verify agg-partK.tsv partK-senses.md
```
- `show` matches the headword case-insensitively, but under PowerShell an empty "" value is dropped and the next number is read as the value: always pass the full Hindi value (as in agg) when you use `show`.
- Part 1 copies the 120 decision lines of `decisions-sample.txt` verbatim for its first 120 headwords.
- Decision lines use the agg headword exactly (lower-case first letter, multi-word headwords such as `kusalā dhammā` included).
- A headword with ONE attested value is always ONE sense (every value is placed once, so it cannot be split). If the English column offers two meanings (dukkhaṃ: suffering / pain; kusalā: states / adjective), write one tag that covers what the Hindi shows; do not invent a second sense.
- Column 2 (English senses) is a hint only. Where it does not fit the Hindi, follow the Hindi and the segment: asaññattā (hint "perception") = the non-percipient beings' realm; uppajjantīnaṃ (hint "arise") = women being reborn; upapajjissati (hint "reborn") = will arise. For such variant or odd Pāli spellings say so in the tag: `…, variant spelling of upapajjantīnaṃ (…)`.

## 2. Inflected and enclitic forms of one stem

pi-6 has many headwords that are the same word with a case ending, the quotative -ti or an enclitic. Each is its own headword with one sense; keep the BASE GLOSS IDENTICAL across the family and change only the modifier and the grammar label:

| Form | Tag | Example (sample) |
|---|---|---|
| plain | `<base gloss> (<grammar>)` | ekamūlā `having one and the same root, sharing a root (nominative pl.)` |
| -ti | `<base gloss>, with quotative -ti (<grammar>)` | ekamūlāti `having one and the same root, with quotative -ti (nominative pl.)` |
| -ñca / ca | `and <base gloss>, with enclitic -ñca (<grammar>)` | kusalañca `and wholesome, with enclitic -ñca (neuter sg.)` |
| -ñceva / ceva | `<base gloss>, with enclitic -ñceva 'both' (<grammar>)` | ekamūlañceva |
| -pi / -mpi | `<base gloss>, with enclitic -pi 'also' (<grammar>)` | anulomampi, nirodhavārepi |
| -yeva | `<base gloss>, with emphatic -yeva (<grammar>)` | kāmadhātuṃyeva |
| -āni (neuter pl. predicated of mūlāni) | `<base gloss>, of the roots themselves (neuter nominative pl.)` | ekamūlāni |

Extra grammar labels used in pi-6 (add to the pi-1 set): `(neuter nominative pl.)`, `(3rd sg. present)`, `(3rd pl. present)`, `(3rd sg. aorist)`, `(3rd pl. aorist)`, `(3rd sg. future)`, `(3rd pl. future)`, `(present participle)`, `(past participle)`, `(genitive pl. present participle)`, `(feminine genitive pl. present participle)`, `(genitive pl. past participle)`, `(genitive pl.)`, `(compound)`, `(stem)`.

## 3. The Mūlayamaka families (from the sample; reuse the base glosses)

| Pāli shape | Base gloss | Hindi |
|---|---|---|
| Xmūlā / -mūlāni | `X roots, the X root conditions` (kusala wholesome, akusala unwholesome, abyākata `indeterminate roots, roots neither wholesome nor unwholesome`, nāma `roots of mentality, roots on the mental side`) | X मूल |
| Xmūlena | `the X root, in 'of one root with the X root' (instrumental)` | X मूल |
| Xmūlamūlā | `roots of the X roots, in the root-of-roots method` | X मूल का मूल |
| Xmūlakā | `based on a(n) X root` | X मूल पर आधारित |
| Xmūlamūlakā | `based on a root of the X roots` | X मूल के मूल पर आधारित |
| ekamūla- / ekamūlamūla- / ekamūlaka- / ekamūlamūlaka- | `having one and the same root` / `… root-of-roots` / `based on one and the same root` / `… root-of-roots` | एक ही मूल वाला / … के मूल वाला / … पर आधारित |
| aññamañña- (same four) | `mutually rooted, each the root of the other` / `mutually rooted in roots-of-roots` / `mutually based on a root, each based on the other's root` / `mutually based on roots-of-roots` | परस्पर … |
| Xmūlasahajātā dhammā | `phenomena born together with a(n) X root (nominative pl.)` | X मूल के साथ उत्पन्न परिघटना |
| Xsamuṭṭhānaṃ | `originated from the X, said of matter (neuter sg.)` | X से उत्पन्न |
| kusala / akusala / abyākata / nāma bare | pi-1/pi-2 tags (`wholesome, said of phenomena (nominative pl.)`, `wholesome, a wholesome phenomenon (neuter sg.)`, `mentality, the mental side of phenomena (nominative pl.)`) | हितकर / हानिकर / नैतिक रूप से अनिर्धारित / मानसिक पक्ष |
| ahetukaṃ / sahetukaṃ | `without roots, rootless` / `having roots, rooted` (neuter sg.) | मूल से रहित / मूल वाला |

The ten names for a root (6-1-49, 6-1-98/99): `<name>, <ordinal> of the ten names for a root` for the kusala-/akusala- compounds (kusalahetū `wholesome causes, second of the ten names for a root (nominative pl.)`), and `<name>, <ordinal> of the ten names, in the summary verse (<case>)` for the bare words of the closing verse (pabhavena, paccayo, sambhavo, samudayena, mūlaṃ, nidānañca, samuṭṭhānāhārārammaṇā). Order: mūla 1, hetu 2, nidāna 3, sambhava 4, pabhava 5, samuṭṭhāna 6, āhāra 7, ārammaṇa 8, paccaya 9, samudaya 10. hetu here is `cause, … kept apart from mūla` (हेतु); everywhere else hetu-/-hetuka stays the pi-1 root sense (मूल).

## 4. Process verbs: tenses and negatives

- One headword = one Pāli tense form = one sense. Never merge across headwords; the keyword already fixes the tense, and the Hindi tense form follows it.
- Number/gender variants of the SAME tense under one headword are one sense, most frequent first: uppajjissanti `they will arise, will come into being (3rd pl. future)`: उत्पन्न होंगे / उत्पन्न होगा.
- Tags (reuse pi-1 wording where it exists):
  - present = Hindi infinitive: uppajjati `arises, comes into being (3rd sg. present)`; uppajjanti `they arise, come into being (3rd pl. present)`; nirujjhati `ceases, comes to an end (3rd sg. present)`.
  - aorist (Hindi «… हुआ था»): uppajjittha `arose, had come into being (3rd sg. aorist)`; nirujjhittha `ceased, had come to an end (3rd sg. aorist)`.
  - future: uppajjissati `will arise, will come into being (3rd sg. future)`; nirujjhissati `will cease, will come to an end (3rd sg. future)`; parinibbāyissanti `they will attain final nibbāna (3rd pl. future)`.
  - participles: uppajjamānaṃ `arising, in the process of arising (present participle)`; uppannaṃ `arisen, already come into being (past participle)`; nirujjhamānaṃ `ceasing, in the process of ceasing (present participle)`; niruddhaṃ `ceased, already come to an end (past participle)`; upapajjitvā `having been reborn (absolutive)`.
- Fused negatives (nuppajjati, nuppajjittha, nuppajjissati, nappajahati, nānuseti; also appahīno, nāyatanaṃ): `does not arise, with fused negative na (3rd sg. present)`, `did not arise, …`, `will not arise, …`; for a- / na- nouns follow the pi-1 `absence of X` / `not a X` pattern (nāyatanaṃ `not a sense base, with fused negative na (nominative sg.)`).
- A verb after a SEPARATE na is mapped to its positive part (mapper rule); its tag is the positive gloss; do not mention the negation.
- -ti forms add `, with quotative -ti` before the grammar label (uppajjatīti `arises, comes into being, with quotative -ti (3rd sg. present)`).

## 5. Realms vs beings

- They are separate headwords already (case decides): the place sense (accusative of destination, locative, ablative, and the realm nouns rūpāvacare, kāmadhātuyā …) vs the beings sense (genitive pl.). Keep the two tag shapes apart so the termbase can see them:
  - realm: `the X realm, as a place (accusative sg.)` / `(locative)` / `(ablative)`: arūpaṃ `the immaterial realm, as a place of rebirth (accusative sg.)`; asaññasattaṃ `the realm of non-percipient beings, as a place (accusative sg.)`; pañcavokāraṃ `five-aggregate existence, as a place (accusative sg.)`; suddhāvāsaṃ `the Pure Abodes, as a place (accusative sg.)`. Use "immaterial", "fine-material", "sense-sphere" (pi-1 words), not "formless" / "form realm".
  - beings: `beings of the X realm (genitive pl.)`: arūpānaṃ `beings of the immaterial realm (genitive pl.)`; asaññasattānaṃ `non-percipient beings (genitive pl.)`; pañcavokārānaṃ `beings of five-aggregate existence (genitive pl.)`; āpāyikānaṃ `beings of the states of misery (genitive pl.)`.
  - persons by process: `those being reborn (genitive pl. present participle)` upapajjantānaṃ; `those dying, passing away (…)` cavantānaṃ; `those attaining final nibbāna (…)` parinibbantānaṃ; women: `women being reborn (feminine genitive pl. present participle)`.
- rūpadhātuṃ is the one headword where both meanings share a form: SPLIT. `the fine-material realm, as a place (accusative sg.)`: सूक्ष्म भौतिक लोक; `the visible-form element, in the element pairs (accusative sg.)`: दृश्य रूप का तत्व (6-4-10/11). Check other -dhātu forms with `show` the same way.

## 6. «लोग» and the bare participle

- «X लोग» and bare «X» / «X वाला» for the same group of persons are ONE sense, «लोग» form first only if it is more frequent (the tool sorts by count): nirodhasamāpannānaṃ `those absorbed in the attainment of cessation (genitive pl. past participle)`: समाप्ति की ध्यान-अवस्था में लीन लोग / समाप्ति की ध्यान-अवस्था में लीन; likewise abhisametāvīnaṃ, anabhisametāvīnaṃ, pacchimacittasamaṅgīnaṃ.
- Same rule for a fused variant of the same phrase: pacchimabhavikānaṃ `those in their last existence (genitive pl.)`: अंतिम जन्म वाला / अंतिम जन्म (the second is the B2 fusion «… अंतिम जन्म लेने वालों में»).
- Gapped and ungapped forms are one sense (pi-1 rule): kāmāvacarānaṃ, yassa yattha, catutthajjhānaṃ.
- caññe = दूसरे लोग: `and others, the other persons, ca + aññe (nominative pl.)`.
- itaresaṃ is a SPLIT (brief): `the rest, all the others, standing alone (genitive pl.)`: बाकी सब; `the other ones of a named group, before that group (genitive pl.)`: बाकी. itarāsaṃ (only बाकी) takes the second tag shape, feminine.

## 7. Bare words vs full terms

- The word-checking pairs (Paṇṇattivāra «rūpaṃ rūpakkhandho?», «cakkhu cakkhāyatanaṃ?») use the bare word, which is wider than the technical term. Its tag says so: `the bare word 'X' in the word-checking pairs, wider than the aggregate or sense base (…)`. Bare-word headwords with one value (vedanā अनुभूति, saññā पहचान, saṅkhārā रचनाएँ, viññāṇaṃ चेतना, cakkhu आँख, sotaṃ कान, kāyo शरीर, mano मन, dhātu तत्व, saccaṃ सत्य, indriyaṃ क्षमता …) get that tag shape too, with the word's gloss: `feeling, the bare word in the word-checking pairs (nominative sg.)`.
- Where the same headword also carries the full term, SPLIT: rūpaṃ `the bare word 'form' in the word-checking pairs, wider than the aggregate or sense base (nominative sg.)`: रूप; `matter, material form, as in 'matter originated from the wholesome' (nominative sg.)`: भौतिक रूप. Same test for saṅkhāra forms (रचनाएँ vs मानसिक रचनाएँ) if both turn up.
- khandha / khandhā / khandho = समूह: `aggregate, group of phenomena (…)` (pi-1). X-kkhandho follows the pi-1 pattern `the aggregate of X`.

## 8. Heading terms

| Pāli | Tag shape | Hindi |
|---|---|---|
| X-yamakaṃ / -yamakapāḷi / -yamake / -yamakassa | `the Pairs on X, title of chapter N (heading)` (case label if not nominative) | X पर प्रश्नों के जोड़े |
| yamakapāḷi / yamakapakaraṇaṃ | `the Book of Pairs, title of the whole book (heading)` | प्रश्नों के जोड़े (ग्रंथ) |
| vāro, X-vāro | `the section on X (heading)`; uddesavāro `the summary section, the round that lists the questions`; niddesavāro `the exposition section` | X का खंड |
| nayo, X-nayo | `the X method (heading)` | X की विधि |
| uddeso | `the summary statement, opening list of a section (heading)`; never "outline" | सूची |
| niddeso / niddesa | `detailed exposition, section heading (nominative)` | व्याख्या |
| paṇṇatti-, padasodhana-, suddha-X-, -mūlacakka- | `terminology`, `checking the words`, `the X alone`, `the cycle based on …` | शब्दावली / शब्दों की जाँच / केवल X / … पर आधारित चक्र |
| anulomaṃ / paccanīkaṃ / paṭilomaṃ | `the positive part` / `the negative part` / `the reversed part` (heading) | सकारात्मक / नकारात्मक / विपरीत |
| anuloma-puggalo / -okāso / -puggalokāsā | `the positive part, by person` / `… by place` / `… by person and place` (heading) | सकारात्मक: व्यक्ति … (the colon stays in the value; never put ": " in a tag) |
| uppāda- / nirodha- / pavatti-vāro | `the section on arising` / `on ceasing` / `on the process of occurrence` | उत्पन्न होने का / समाप्त होने का / प्रक्रिया का खंड |
| -ādi | `…, and the rest` | … आदि |

## 9. Report items (same as pi-1)

Headword count and the verify line; headwords with >1 sense; senses with >1 candidate; any " / "→" और " rewrite the build prints; the most consequential splits and synonym clashes.
