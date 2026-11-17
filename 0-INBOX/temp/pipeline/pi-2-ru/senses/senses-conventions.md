# pi-2 (Vibhaṅga) Pāli→Russian senses: conventions from the sample (for parts 1–4)

The sample was agg-sample.tsv (120 headwords: the first 90 of part 1 plus the next 30 multi-value ones). Follow these conventions so all parts read as one file.
The brief (..\ru-senses-brief.md) and the skill (AI_translation\skills\word-sense-grouper.md) govern; this file fixes the choices they leave open. Base: the pi-1 file ..\..\pi-1-ru\senses\senses-conventions.md. Everything there still holds; this file repeats the essentials and records what pi-2 adds.

## 1. Workflow and tool

Files per part K (all in this folder): `decisions-partK.txt` (your hand-written tag table) → `partK-senses.md` (output).

```
python -I -X utf8 senses_tool_ru.py todo   --part K        # headwords still without a decision line
python -I -X utf8 senses_tool_ru.py prior  --part K        # each todo headword: agg row + approved pi-1/pi-4/pi-5 Russian
                                                           # senses lines + the pi-2 English senses line (start here)
python -I -X utf8 senses_tool_ru.py prior  <hw> [<hw> ...] # same for named headwords
python -I -X utf8 senses_tool_ru.py show   <hw> [<value>] [<max segs>] [<width>]   # ids + Pāli/Russian lines
python -I -X utf8 senses_tool_ru.py build  --part K        # builds partK-senses.md, then verifies
python -I -X utf8 senses_tool_ru.py verify --part K
python -I -X utf8 senses_tool_ru.py reuse  --part K        # lines reusing a pi-1 tag verbatim (for the report)
```

- pi-2 paragraphs are long: always pass a width (`show Hetu причина 3 200`) so each line is cut to 200 characters around the match. The value probe drops the last two letters of values longer than 5 characters, so inflected Russian forms are found.
- Decision lines, one per headword, any order (build writes agg order): `hw: {tag}` = one sense, every attested value filled in, most frequent first; `hw: {tag1: v1 / v2; tag2: v3 / *}` = explicit split, every attested value placed exactly once, `*` = all values not listed elsewhere on the line. Senses keep your order (main sense first); values are re-sorted by count inside a sense.
- An attested value containing " / " is written with " и " (the build lists every rewrite; the sample had none).
- `verify` fails on: headword list or order differs, duplicates, a missing/extra value, a tag equal to a value, a tag that is a bare copy of an English hint, Cyrillic in a tag, two senses with the same tag, a candidate containing "/" or "; ", an unparsable line.

## 2. Tags

Pattern: **short English gloss[, distinguishing context] (grammar)**, as in pi-1/pi-4/pi-5.

- **pi-1 first.** 1,341 pi-2 headwords have a line in AI_translation\russian\pi-1-pali-word-russian-senses-plain.md. Where pi-2 has the same Russian value in the same sense, copy the pi-1 tag verbatim (sample: 44 of the 59 shared headwords). Change only the grammar label or the example compound when the pi-1 one does not occur in pi-2 (pi-1 "as in dhammāyatana" → pi-2 "as in dhammadhātu and dhammataṇhā"); add a sense only for a value pi-1 does not have.
- pi-2 English senses (AI_translation\english\pi-2-english-senses-plain.md) are a hint for wording and for which headwords are polysemous; they are not binding.
- Context in every sense of a split headword (the compound, the list, or the chapter that identifies the use: "in kummagga", "of the knowledge chapter", "in the list of tastes").
- Grammar labels: the pi-1 set, plus `(phrase, nominative sg.)` for multi-word keys like `rūpaṃ atītaṃ`, `(verb phrase)` for `vuccati X`, `(present passive)` for `vuccati`, `(heading and heading member)`.
- Forbidden in a tag: ": ", "; ", "{", "}", Cyrillic, a bare English hint. Keep tags under ~15 words.

## 3. One sense or several

Merge (one sense, candidates " / "):
- grammatical variants: формирующие факторы / формирующий фактор (saṅkhāra, also the singular «формирующий фактор» of the dependent-origination chapter); тройки / тройка; четвёрка / четвёрки; возникать / возникший; проявившийся / проявиться; полностью угаснуть / полностью угасший; родиться / рождённый; после возникновения / возникновение (uppajjitvā);
- noun and adjective of one meaning: материальная форма / материальный (rūpa, rūpaṃ, rūpā: matter, also the predicate «является материальной» and Rūpadukaṃ «Пара о материальном»); болезненный / боль (Dukkha);
- sphere noun and sphere fragment: мир форм / форма (rūpa; «форма» is the rūpa part of «Мир форм» = Rūpadhātu);
- synonyms: внутренний / внутри себя / внутри; родные / родственники; появившийся / возникнуть (nibbattā); или же какой бы другой / а также любой другой; невозмутимость / виды невозмутимости («cha gehasitā upekkhā» = шесть видов невозмутимости).

Split (checked with `show`):
- **N-group vs N-fold division (new in pi-2):** Ekaka … Dasaka, Tikaṃ, Dukaṃ, catukkaṃ: the group or set (единицы, пары, тройки, четвёрки …) vs the division into N kinds of the knowledge chapter (Ñāṇavibhaṅga «Evaṃ duvidhena ñāṇavatthu. Dukaṃ.»; Ekakaniddesa …). The Russian value has no «классификация» (user decision 2026-11-16: по одному, на два вида … на десять видов), and the tag avoids the word too: `division into two kinds, …`, `one by one, the onefold classification, …` only for Ekaka.
- technical vs ordinary use (as pi-1): Magga путь vs дорога (kummagga); āhāro пища (kabaḷīkāro āhāro) vs питание (the three nutriments of contact, volition, consciousness); kiriyā функциональный vs деяние (pāpakiriyā); Khandha совокупность vs стебли (list of tastes); vitakko направленная мысль (the mental factor) vs мысль (the minor-topic headings ñātivitakko, janapadavitakko, amaravitakko …).
- different referent: Dhātu элемент vs мир (kāmadhātu, rūpadhātu, arūpadhātu = «мир чувственных желаний», «мир форм», «мир без форм»); Āyatana / āyatanaṃ сфера восприятия (sense base) vs сфера (head of a named base: «сфера глаза», and the formless bases «сфера бесконечного пространства»); rūpa / rūpaṃ / rūpā: matter vs visible form vs the fine-material sphere; Dhamma явление vs Учение (dhammacchanda) vs объекты ума (dhammadhātu, dhammataṇhā); pāda основа (iddhipāda) vs нога (pādatala); vatthu основа (ñāṇavatthu, physical base) vs тема (Khuddakavatthu title) vs повод (kusītavatthu); ādi прочее (X-ādi "and the rest") vs начало (pātimokkha definition); Māyā обман (deceit, the defilement) vs наваждение (illusion, in the craving synonym list).
- Hetu корень (root condition, "na hetu", hetusampayutta) vs причина (Hetucatukkaṃ and hetuka "имеющий причиной" in dependent origination; Hetuvāra of the paṭisambhidā chapter).
- Dukkha: страдание (suffering, dukkhasacca) vs болезненный / боль (painful feeling or contact, dukkhadhātu) vs трудный (dukkhapaṭipadā); dukkhā: болезненный vs страдание (predicate "the aggregates / sense pleasures are suffering").
- upādāya: производный (upādārūpa) vs в связи с ("ajjhattikassa upādāya", the currents of craving) vs в силу (by virtue of, the possible and the impossible).

## 4. Recurring headword families: the tags of the sample

Reuse these senses (wording and order) whenever the same Russian value turns up under any form of the headword; adapt only the grammar label and the example compound.

| Family | Sense tag (sample) | Russian |
|---|---|---|
| khandha | `aggregate, a group of phenomena (nominative sg.)`; pl. `aggregates, groups of phenomena (nominative pl.)` | совокупность / совокупности |
| | `stems, plant stalks, in the list of tastes (compound member)` | стебли |
| X-kkhandho | `the aggregate of X (nominative sg.)` (X = matter, feeling, perception, formations, consciousness) | совокупность X |
| rūpa | `matter, material form (…)`; rūpaṃ `matter, material form, also 'material' as predicate (nominative/accusative sg.)` | материальная форма / материальный |
| | `visible form, the object of the eye (…)`; rūpā `visible forms, the objects of the eye (nominative pl.)` | видимая форма / видимые формы |
| | `the fine-material sphere, as in rūpadhātu and rūpabhava (compound member)` | мир форм / форма |
| rūpaṃ + adjective | `X matter, Y material form (phrase, nominative sg.)`: `coarse matter, gross material form`, `matter gone by, past matter` | грубая / прошлая … материальная форма |
| saṅkhāra | `formations, the volitional factors of the fourth aggregate and of dependent origination (stem and compound member)` | формирующие факторы / формирующий фактор |
| dhātu | `element, an irreducible constituent (stem and compound final)` | элемент |
| | `world, plane of existence, in kāmadhātu, rūpadhātu and arūpadhātu (compound final)` | мир |
| āyatana | `sense bases, the sense fields, as in Āyatanavibhaṅga (stem and compound member)`; āyatanaṃ `sense base, sense field (nominative/accusative sg.)` | сфера восприятия |
| | `base of a formless attainment, as in ākāsānañcāyatana (compound final)`; āyatanaṃ `base, sphere, as head of a named base such as cakkhāyatana or ākāsānañcāyatana (compound final)` | сфера |
| Xāyatanaṃ | `the X base, the X as a sense field (nominative sg.)` (pi-1) | сфера X |
| dhamma | `phenomena, states, as in Dhammahadaya and dhammapaṭisambhidā (stem and compound member)` | явление |
| | `the Buddha's teaching, in dhammacchanda 'desire for the Dhamma' (compound member)` | Учение |
| | `mind-objects, what the mind as sixth sense knows (compound member, as in dhammadhātu and dhammataṇhā)` | объекты ума / объект ума |
| hetu | `root, a root condition, as in 'na hetu' and hetusampayutta (stem and compound member)` | корень |
| | `cause, in Hetucatukkaṃ of dependent origination and Hetuvāra of the analytical knowledges (heading member)` | причина |
| dukkha | `suffering in general, as in dukkhasacca 'the truth of suffering' (stem and compound member)` | страдание |
| | `pain, painful feeling or contact, as in dukkhasamphassa and dukkhadhātu (stem and compound member)` | болезненный / боль |
| | `difficult, of the mode of progress in dukkhapaṭipadā (compound member)` | трудный |
| magga | `path, as a noble path or set of factors (stem and compound member)` | путь |
| | `road, in kummagga 'crooked road', a name for the wrong eightfold practice (compound final)` | дорога |
| āhāra | `edible food, in kabaḷīkāro āhāro (nominative sg.)` / `nutriment, a sustaining condition (contact, volition, consciousness) (nominative sg.)` | пища / питание |
| N-groups | `pairs, the dyad groups (heading member)`, `triads, the groups of three (heading member)`, `fours, the groups of four items (heading member)` … `tens, the groups of ten items (heading member)`; Ekaka `ones, the single-item group, in Ekakamātikā (heading member)` | пары, тройки, четвёрки … десятки, единицы |
| N-fold division | `division into N kinds, in Nkaniddesa of the knowledge chapter (heading member)`; closing line: `division into N kinds, closing label of the N-fold section of the knowledge chapter (heading)`; Ekaka `one by one, the onefold classification, in Ekakaniddesa of the knowledge chapter (heading member)` | на N видов / по одному |
| vatthu | `basis, ground, …` / `topic, subject matter, in the title Khuddakavatthuvibhaṅga` / `occasion, reason, in kusītavatthu 'occasions for laziness' (compound final)` | основа / тема / повод |
| vitakka | `directed thought, initial application of mind (nominative sg.)` / `a thought about a topic, in the minor-topic headings such as ñātivitakko (compound final)` | направленная мысль / мысль |
| upādāya | `derived, dependent on the great elements (absolutive, as in upādārūpa)` / `with reference to, in 'ajjhattikassa upādāya' …` / `by virtue of, owing to, …` | производный / в связи с / в силу |
| past/future frame | atīta `past, gone by`, anāgata `future, not yet come`, paccuppanna `present, existing now`; niruddha `ceased, stopped`, vigata `disappeared, gone away`, vipariṇata `changed, altered`, abbhatthaṅgata `completely gone down, vanished`, jāta `born, come to birth`, nibbatta `produced, generated`, abhinibbatta `fully produced, brought wholly into being`, pātubhūta `become manifest, appeared`, uppanna `arisen, come into being`, uṭṭhita `risen up, emerged`, samuṭṭhita `fully risen up, originated`, saṅgahita `included, comprised in a category` (+ grammar label) | the pi-2 map values |
| quality pairs | oḷārika `gross, coarse`, sukhuma `subtle, fine`, hīna `inferior, low`, paṇīta `superior, excellent` (pi-1) | грубый, тонкий, низший, высший |
| headings | vibhaṅgo `analytical exposition, naming each chapter of the book (heading, nominative sg.)`; bhājanīyaṃ `analysis, the analytical section (heading member)` (pi-1); Suttanta `the discourses, as the method of Suttantabhājanīya (compound member)`; Pañhāpucchakaṃ `the question-and-answer section closing a chapter (heading)` | разбор, наставления, раздел вопросов |

Expected later (decide with `show`): saṅkhāra as "prompting" (sasaṅkhārika) vs the aggregate; vuṭṭhāna; bhava as existence vs becoming; kāma (sense sphere vs sensual desire, pi-1); sukha счастье vs удовольствие (pi-1: mental vs bodily); paṭisambhidā items (attha, dhamma, nirutti); the remaining N-vidhena headwords (Duvidhena … Bahuvidhena) are single-sense («на два вида» …), Ekavidhena «по одному».

## 5. Report items

Headword count and the verify line; headwords with >1 sense; senses with >1 candidate; the `reuse` line; any " / "→" и " rewrite; the most consequential splits and synonym clashes.
