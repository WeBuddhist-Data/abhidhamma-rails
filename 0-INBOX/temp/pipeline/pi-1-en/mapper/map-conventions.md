# pi-1 English→Pāli keyword map: conventions

Settled on the sample chapters `preamble` and `1-matika` (see `preamble.mapped.md`, `1-matika.mapped.md`,
built by `map_preamble_1-matika.py`, checked by `check_preamble_1-matika.py`). Follow these for the other
chapters so all maps agree. The brief (`../en-mapper-brief.md`) still governs; this file only fixes the
choices the brief leaves open.

## 0. Where the Pāli comes from

- Only the Pāli of THAT segment (`AI_translation/pali/pi-1_split_chapters/<ch>.md`, same `^id`).
- Ignore variant brackets `[... (syā.)]` as a source: a keyword that only exists because of a bracket
  (always `variant`) is `(no direct equivalent)`. When a bracket stands between two words you span,
  write the span without it (`upādiṇṇā dhammā`, not `upādiṇṇā [upādinnā (sī. syā.)] dhammā`).
- Labels `(Ka)/(Kha)/(Ga)` and heading marks are not text.

## 1. Spelling of the Pāli value

1. **Copy the text letter for letter, including capitals.** A heading or line-initial word keeps its
   capital, also when cut: `Abhidhamma=abhidhamma` (from `Abhidhammapiṭake`), `Dhamma=phenomena`,
   `Hetu=roots` (from `Hetugocchakaṃ`), `Duka=pairs` (from `Dukamātikā`), `Namo=homage`.
   (The pi-3/pi-4 maps lowercased some cuts, e.g. `abhidhamma`, `namo`; pi-1 does not.)
2. **Whole word / final member keeps the ending the text has**: `kusalā`, `vedanāya`, `dhammesu`,
   `sahagatā` (from `pītisahagatā`), `hetukā` (from `sahetukā`), `vippayuttā` (from `āsavavippayuttā`),
   `sambuddhassa` (from `sammāsambuddhassa`).
3. **A non-final compound member is written in its stem form** (it has no ending of its own):
   `hetu` (from `hetusampayuttā`), `pahātabba` (from `pahātabbahetukā`), `vitakka` (from
   `savitakkasavicārā`), `citta`, `ācaya`, `magga`, `sīla` (from `sīlavipatti`), `diṭṭhi` (from
   `diṭṭhivisuddhi`).
4. **Sandhi at the joint**: when two vowels fuse (`paritta+ārammaṇā` → `parittārammaṇā`), the cut
   member is still written in its own form (`paritta`, `ārammaṇā`; `kāma`, `avacarā` from `kāmāvacarā`;
   `adhipatino` from `maggādhipatino`; `anuparivattino` from `cittānuparivattino`). Such values are not
   literal substrings; the check script lists them as `SANDHI`, which is expected, not an error.
5. **Enclitics**: drop a separate `ca` and a suffixed `-pi` (`avijjā ca` → `avijjā`; `anāsavāpi` →
   `anāsavā`). Where `ca` is fused by sandhi (`rūpañca`, `nāmañca`, `balañca`, `sampajaññañca`), keep the
   word as written, since separating it would change letters.
6. Never `", "` inside a value. One space between words of a phrase.

## 2. How far to cut a compound

- **Cut at member boundaries when the English renders the members with separate words**:
  `ācaya=accumulation` + `gāmino dhammā=States leading` (from `ācayagāmino dhammā`); `pāpa=bad`,
  `mittatā=friends` (`pāpamittatā`); `saha=together`, `bhuno=existing` (`sahabhuno`); `matta=moderation`,
  `ññutā=knowing`, `mattaññutā=knowing moderation`; `uttarā=transcend` (`lokuttarā`); `yathā=keeping`
  (`yathādiṭṭhissa`).
- **Do not cut when the English renders the word as a whole** (no member-for-member match):
  `vipākadhamma=produce`, `vipākadhamma=produce results`; `sahagatā=accompanied`; `sauttarā=surpassable`;
  `cetasikā=mental` / `=factors`; `tapanīyā=cause` / `=torment`; `niyyānikā=liberation`;
  `uppādino=bound` / `=arise`; `adhipatino=factor`; `saṃvego=sense` / `=urgency`.
- **Never cut off a derivational suffix** (`-iya`, `-ika`, `-tā`, `-in`), and do not split a prefixed
  word (`vi-`, `saṃ-`, `anu-`, `pa-`, `pari-`...) that the English renders as one word:
  `saṃyojaniyā=fetters` (not `saṃyojan`), `vippayuttā=dissociated`, `samuṭṭhānā=arising`,
  `anuparivattino=accompanying`. Only the next rule strips a prefix.
- **Negative / possessive / evaluative prefixes `a-`, `an-`, `sa-`, `du-`/`do-`, `su-`/`so-`**: when the
  English gives the prefix its own word ("not", "without", "with", "free of", "subject to", "lack of",
  "hard to", "easy to"), the base keyword maps to the base with the prefix stripped, and the prefix's
  English word maps to the whole word:
  `āsavā=taints` + `anāsavā=free` (from `anāsavā`); `hetukā=roots` (from `sahetukā`); `raṇā=conflict`
  (`saraṇā`); `pītikā=rapture` (`sappītikā`); `vitakkā=applied` (`savitakkā`); `santuṭṭhitā=content`
  (`asantuṭṭhitā`); `gutta=guarding` (`aguttadvāratā`); `sampajaññañca=clear awareness` +
  `asampajaññañca=lack`; `vacassatā=correct` + `dovacassatā=hard`, `sovacassatā=easy`. The same applies
  to any prefix the English renders by its own word: `diṭṭhi=view` + `anudiṭṭhi=concerning` (from
  `pubbantānudiṭṭhi`, "the view concerning the past").
  When the English word itself contains the negation (`unwholesome`, `invisible`, `undefiled`,
  `unconditioned`, `impossible`, `non-existence`, `non-arising`, `unsurpassable`, `beyond` for `asekkhā`),
  map the whole word: `akusalā`, `anidassanā`, `asaṃkiliṭṭha`, `asaṅkhatā`, `aṭṭhāna`, `vibhava`,
  `anuppāde`, `anuttarā`, `asekkhā`.

## 3. Multiword keywords (fragments)

- A multiword keyword maps to the **smallest contiguous stretch of Pāli that contains every Pāli
  element it renders**, cut by §2 at its edges, taken from the FIRST item where it occurs:
  `kusalā dhammā=Wholesome states`, `sampayuttā dhammā=States associated` (from `sukhāya vedanāya
  sampayuttā dhammā`), `vippayuttā dhammā=states dissociated` (from `hetuvippayuttā dhammā`),
  `savitakkasavicārā dhammā=States with applied`, `no cittasamuṭṭhānā dhammā=states not arising`,
  `saṃyojanā ceva dhammā saṃyojaniyā=fetters and subject`,
  `saṃyojanavippayuttā kho pana dhammā saṃyojaniyā=fetters but subject`,
  `vippayuttā kho pana dhammā=states dissociated` (in the 6th pair of a group, where `kho pana`
  stands between).
- A fragment that splits a single Pāli word maps to that word: `upādiṇṇa=produced by past`,
  `upādiṇṇupādāniyā=action and subject`, `adukkhamasukhāya=painful nor pleasant`.
- Case variants of one keyword (`States dissociated` / `states dissociated`) get the same value.

## 4. One English keyword, several Pāli sources in the segment

- Same lemma (incl. its compounds/derivatives): use the FIRST occurrence in the segment. E.g. 1-M2-4
  `hetū=roots` (not `sahetukā`); 1-M2-19 `āsava=taints` (first is `āsavavippayuttā`); 1-M2-138
  `diṭṭhi=view` (first is `diṭṭhivisuddhi`, not `yathādiṭṭhissa`).
- Different lemmas: join with `" / "` (pi-3 precedent): 1-M1-6 `vitakka / vicāra=thought`.
- Identical formulaic segments get identical values (the six-pair groups are generated from one template
  in the script).

## 5. `(no direct equivalent)`

Only for a keyword with no Pāli source in the segment:
- `variant` (the editorial bracket) – always.
- English function/auxiliary words: `having` ("Having bad friends"), `regarding` ("Skill regarding
  offences").
- Clarifying additions with no Pāli word behind them: `kinds`, `consciousness` in "States that some kinds
  of consciousness can know" (`kenaci viññeyyā`); `spheres`, `existence`, `spheres of existence` in
  "States included in the spheres of existence" (`pariyāpannā`).
- NOT for a word that is part of the multiword rendering of one Pāli term: `factor` (dominant factor) =
  `adhipatino`, `thought` (applied thought) = `vitakka`, `kinds` in "kinds of clinging" = `upādānā`
  (it renders the plural), `bound` (bound to arise) = `uppādino`, `wrongdoing` (fear of wrongdoing) =
  `ottappañca`, `liberation` (lead to liberation) = `niyyānikā`. (pi-3 used nde for `factor`/`bound`;
  pi-1 does not.)

## 6. Fixed values for headings and recurring fragments

| English keyword | Pāli value | Note |
|---|---|---|
| matrix | `Mātikā` (heading 1-M-0), else `mātikā` | from `Tikamātikā`, `Dukamātikā`, `Suttantikadukamātikā`, `Abhidhammadukamātikā` |
| pairs | `Duka` (heading `Dukamātikā`), `dukaṃ` (`...dukaṃ`), `duka` (`...dukamātikā`) | the form inside the source word |
| sets of three / three | `Tika` / `tika` | (not extracted as keywords in the matrix, use if it appears) |
| intermediate / Intermediate Pairs | `antara` / `antaradukaṃ` | `Cūḷantaradukaṃ`, `Mahantaradukaṃ` ("short"/"long" not keywords) |
| closing | `Piṭṭhi` | `Piṭṭhidukaṃ` |
| discourse | `Suttantika` | |
| group names (roots, taints, fetters, ties, floods, yokes, hindrances, misapprehension, clinging, defilements) | capitalised first member of `...gocchakaṃ`: `Hetu`, `Āsava`, `Saṃyojana`, `Gantha`, `Ogha`, `Yoga`, `Nīvaraṇa`, `Parāmāsa`, `Upādāna`, `Kilesa` | "group" = `gocchaka`, if extracted |
| abhidhamma (in "Abhidhamma pairs") | `Abhidhamma` | |
| complete ("The matrix is complete") | `niṭṭhitā` | |
| states (bare, if extracted) | the `dhammā` / `dhammesu` / `dhammaṃ` form in the text | |
| X states / States X | `<X-word> dhammā` | §3 |
| associated / dissociated | `sampayuttā` / `vippayuttā` | the final member, ending kept |
| subject to X | the `-iya`/`-ika`/`sa-` word: `saṃyojaniyā`, `upādāniyā`, `saṃkilesikā`, `sāsavā` | |
| States subject / States not subject | `saṃyojaniyā dhammā` / `asaṃyojaniyā dhammā` | |
| abandoned (by seeing / by development) | `pahātabbā`, or `pahātabba` inside `pahātabbahetukā` | `dassanena=seeing`, `bhāvanāya pahātabbā=abandoned by development` |
| object | `ārammaṇā` | `sārammaṇā` → `ārammaṇā` |
| mind | `cittā` (whole word) or `citta` (member) | |
| Fully Awakened Buddha etc. (homage line) | `sammāsambuddhassa`; `awakened`/`buddha`/`Awakened Buddha` = `sambuddhassa`; `fully` = `sammā` | `bhagavato=blessed`, `arahato=worthy`, `Namo=homage` |
| Abhidhamma Piṭaka | `Abhidhammapiṭake` | |
| Enumeration of Phenomena | `Dhammasaṅgaṇī` (`pāḷi` untranslated, cut off) | `saṅgaṇī=enumeration`, `Dhamma=phenomena` |

## 7. Checking

- Run the brief's verifier per chapter (must print `bad []`).
- Run a presence check like `check_preamble_1-matika.py <ch>`: every value (each side of `" / "`)
  must be a case-sensitive substring of the segment's Pāli (brackets/labels removed). Expected misses
  are only `SANDHI` (§1.4); anything labelled `MISSING` is an error to fix or justify.

## 8. User decision (2026-11-10): keep compounds whole rather than cut them into non-words

Cut a compound only where every piece is itself a Pāli word or a normal compound member (`kāma`, `rūpa`, `citta`, `paritta`, `saṃsaṭṭha`). Never produce a bound fragment that is not a word on its own (`ññutā`, `bhuno`, `saha` from `sahabhuno`, `tā`, `tta`): when the English renders the parts of such a compound with separate words, map each of those English words to the WHOLE compound, e.g. `mattaññutā=moderation`, `mattaññutā=knowing`, `cittasahabhuno=together`, `cittasahabhuno=existing`. The sample (1-matika.mapped.md) was fixed this way.
