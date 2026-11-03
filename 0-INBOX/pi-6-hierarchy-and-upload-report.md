# Yamaka (`pi-6`) — root text and commentaries: structure, content, and upload

**Date:** 2026-10-29 (updated 2026-10-30)  
**Texts:**

- Root: `1-SOURCES/Text/pi-6.md` (Yamakapāḷi, Abhidhamma book 6)
- `1-SOURCES/Commentaries/pi-yamaka-atthakatha.md`
- `1-SOURCES/Commentaries/pi-yamaka-mulatiika.md`
- `1-SOURCES/Commentaries/pi-yamaka-anutiika.md`

**Checked against:** tipitaka.app (`ap-yam-1`, `-2`, `-3` for the root; `atta-ap-pp-6-34` … `-43`, `tika-ap-pp-4`, `tika2-ap-pp-5` for the commentaries, through its `/api/children` and `/api/text` endpoints), `4-SYSTEM/Guidelines/block-id-spec.md`, the linters and parsers under `4-SYSTEM/scripts/`, and the live WeBuddhist library (content, segments, alignments, titles).

This note is for someone opening the project cold. It records what was checked, what was fixed, what differs from the website on purpose, and what to know before changing the live reader. The root text was not edited.

---

## Summary of changes

### What was fixed

| Issue | What was wrong | Fix | Example | Applied to |
|---|---|---|---|---|
| Two root headings one level too high | `(Kha) anulomaokāso` (Saṅkhārayamaka) and `(Ka) uddeso` (Dhammayamaka) were marked one level higher in the source than everywhere else in the Yamaka, so the TOC nested them wrongly | moved down one level; the later headings in those two yamakas renumbered by sibling position (196 heading IDs). No content ID changed | `#### (Kha) anulomaokāso ^6-6-21-0` → `##### … ^6-6-20-2-0`; `#### (Ka) uddeso ^6-9-2-0` → `##### … ^6-9-1-1-0`; `(6) Atītānāgatavāro ^6-6-22-0` → `^6-6-21-0` | `pi-6.md`, the stored root TOC and edition, and the live TOC (replaced 2026-10-30, new `toc_id` `Jn8erKpW4PQSv9NcjBEwU`) |
| Glued words in the commentaries | 41 words were joined where the source has a space (14 / 12 / 15), always around a page marker | one space inserted in each | `Yassarūpakkhandho` → `Yassa rūpakkhandho`; `Desanāsaṃkiṇṇā` → `Desanā saṃkiṇṇā`; `vāpana` → `vā pana` | the three commentary files, before upload |
| No links to the root text | the commentaries had no root-verse transclusions, so there was no alignment | one link per root verse, from each paragraph's printed citation and its yamaka (1,276 / 979 / 1,009 lines); because the root restarts its numbers in every yamaka, each paragraph was also checked by meaning and context, and all were confirmed | mūlaṭīkā `22-254.` (Āyatanayamaka) → `^6-3-22` … `^6-3-254`; aṭṭhakathā `99.` → `^6-9-99`, not `^6-8-99` | the three commentary files and the library alignments |
| Missing licence and tag | not set | added | `license: cc0`; `tag_ids: [296WZOr8MXWteSqBBI7pl]` | commentary frontmatter and library |
| Titles not as in the source | the titles carried "(extract from …)", then were shortened | set to the source's book headings | `Yamaka-mūlaṭīkā` → `Yamakapakaraṇa-mūlaṭīkā`; `Yamaka-aṭṭhakathā` → `Yamakappakaraṇa-aṭṭhakathā` | frontmatter and library (`PATCH /v2/texts/{id}`, 2026-10-30) |

The commentaries were uploaded once these were fixed; their IDs are in the frontmatter.

### What was checked and left unchanged

| Item | Why nothing was changed |
|---|---|
| Root text wording (182,657 words) | it matches tipitaka.app word for word, so no fix was needed |
| Two stray numbers in the root text (`4` in `^6-6-65`, `9` in `^6-7-311`) | the source itself prints them between correctly numbered paragraphs; they are kept as printed and recorded in `known-source-irregularities.md` |
| The site's three volumes | the site splits Yamaka into three volumes with their own title lines; the vault keeps one book, which is the intended form |
| 196 heading segments in the live root edition still carry the old heading IDs | the API cannot rename a segment, and replacing the segmentation would delete the three commentary alignments; nothing uses these segments |
| Two "Paṇṇattivāro" headings in the anuṭīkā Khandhayamaka | the source prints the heading twice |
| The aṭṭhakathā paragraph `1-86.` under Pavattivāravaṇṇanā | the source places it there; it is linked as printed |
| Places where the site's tree nests headings differently | in each case the site breaks the Yamaka's own pattern; the vault follows the pattern |
| Live root edition in the older parser format | the text is correct; rebuilding it would delete every alignment on it, so it is a separate decision |

---

## What these files are

`pi-6.md` is the **root mūla** of the Yamaka, merged from tipitaka.org CSCD `abh03m4`, `abh03m5` and `abh03m6` (the site's three volumes). The three commentaries are its aṭṭhakathā, mūlaṭīkā and anuṭīkā, extracted from the combined Pañcapakaraṇa commentaries. Each commentary paragraph links to the root verses it explains, and those links become the alignment in the library.

---

## How IDs work

| Track | Shape | Example | Meaning |
|---|---|---|---|
| Heading | ends in `-0` | `^6-3-1-0` | TOC node only |
| Root content | zone + printed number | `^6-3-22` | root paragraph 22 of the 3rd yamaka (Āyatana); numbering restarts in each yamaka |
| Commentary content | running counter | `^6-1` … `^6-195` | the Nth paragraph of that commentary file |
| Link to root | transclusion | `![[1-SOURCES/Text/pi-6.md#^6-3-22]]` | the root verse a commentary paragraph explains |

Headings use **sibling position** under their parent, not the numbers the site prints. This is by design (`block-id-spec.md` §5), the same as pi-3 to pi-5.

---

## Root text (`pi-6.md`)

### Outline

- **1,039 headings**, levels `#` to `#####`, each with a `-0` anchor: the book, ten yamakas, their vāras and sub-sections. Every child ID extends its parent's; siblings run 1…n with no gaps.

### Body

- Content IDs: homage `^T-1` and ten yamaka zones `^6-1-N` … `^6-10-N`, each running 1…max with no gaps or duplicates: Mūla 99, Khandha 211, Āyatana 254, Dhātu 19, Sacca 170, Saṅkhāra 159, Anusaya 349, Citta 116, Dhamma 229, Indriya 482.
- **11,085 continuation lines** (the paired questions and answers) have no ID of their own; they belong to the block whose ID follows.

### Compared with tipitaka.app (`ap-yam-1`, `-2`, `-3`)

- The site splits Yamaka into three volumes, each opening with its own homage and title lines; the vault merges them into one book. Apart from those 6 lines, the file's 14,213 lines (1,039 headings + 2,089 ID lines + 11,085 continuation lines) match the site paragraph for paragraph.
- All 1,039 headings match in title and order. The printed paragraph numbers are identical.
- The text is identical to the site word for word (182,657 words), apart from the two stray numbers below.

### Kept as the source prints it

The source prints two stray paragraph numbers between correctly numbered paragraphs. They are kept as text at the end of the preceding block and recorded in `4-SYSTEM/Guidelines/known-source-irregularities.md`:

- `4` on "(Ṅa) paccanīkaokāso" (`ap-yam-2` para 373, between 65 and 66) → last line of `^6-6-65`
- `9` on an empty paragraph (`ap-yam-2` para 2999, between 311 and 312) → last line of `^6-7-311`

The first `(5) Paccuppannānāgatavāro` of Saṅkhārayamaka (`^6-6-13-0`) therefore has five sub-headings, not six: its `(Ṅa) paccanīkaokāso` is that stray body line.

### Heading levels fixed (2026-10-30)

The Yamaka repeats one heading pattern in every yamaka. Two headings in the source were marked one level too high, and the file had followed them:

| Heading | Was | Now | Pattern it now follows |
|---|---|---|---|
| `(Kha) anulomaokāso` (Saṅkhārayamaka) | `####` `^6-6-21-0`, with (Ga) … (Ca) nested under it | `#####` `^6-6-20-2-0`, with (Ga) … (Ca) as its siblings `^6-6-20-3-0` … `-6-0` | the other 9 `(Kha) anulomaokāso` headings sit under their vāra next to (Ka) … (Ca) |
| `(Ka) uddeso` (Dhammayamaka) | `####` `^6-9-2-0`, a sibling of Paṇṇattivāro | `#####` `^6-9-1-1-0`, under Paṇṇattivāro | the other 6 yamakas with a Paṇṇattivāro have `(Ka) uddeso` under it |

Heading IDs are numbered by sibling position, so the later headings of those two yamakas moved up by one: 196 heading IDs in all (42 in Saṅkhārayamaka, 154 in Dhammayamaka), for example `(6) Atītānāgatavāro` `^6-6-22-0` → `^6-6-21-0` and `Padasodhanavāro` `^6-9-3-0` → `^6-9-2-0`. No content ID changed, and nothing in the vault links to a root heading ID, so the commentary links are not affected. The stored `parser-root-text/output/pi-6/` TOC was rebuilt with the same span rule as before (it reproduces all 1,039 earlier spans), and the 196 heading references in the stored edition were updated.

After the fix the root TOC matches tipitaka.app's tree for both headings. The remaining differences from the site's tree are places where the site breaks the pattern: it nests (Ga) … (Ca) under this one `(Kha) anulomaokāso`, puts Cittayamaka's `(Kha) niddeso` under a vāra, puts `Suddhadhammavāro` and `Suddhadhammamūlacakkavāro` under `Padasodhanamūlacakkavāro`, and files `Indriyayamakaṃ` under a stray "9a" node.

---

## Commentaries

### Outline (all three files)

```
# Abhidhammapiṭake (…)                         ^0
## Yamaka…                                     ^6-0
### Ganthārambhavaṇṇanā                        ^6-1-0   (mūlaṭīkā, anuṭīkā only)
### Mūlayamakaṃ … Indriyayamakaṃ               10 yamakas
#### Paṇṇatti- / Pavatti- / Pariññāvāra…       vāras
##### Uddesa- / Niddesavāra…, Mahāvāra parts   up to 5 levels
### Nigamanakathā                              ^6-11-0  (aṭṭhakathā only)
```

- No heading level skips; every heading ID ends in `-0` and extends its parent's; siblings run 1…n with no gaps.
- Content IDs are one continuous counter per file, with no gaps or duplicates: aṭṭhakathā `^6-1` … `^6-195` (46 headings), mūlaṭīkā `^6-1` … `^6-146` (49), anuṭīkā `^6-1` … `^6-174` (48).
- Yamaka positions differ by file because of sibling numbering: Mūlayamakaṃ is `^6-1-0` in the aṭṭhakathā and `^6-2-0` in the ṭīkās (after Ganthārambhavaṇṇanā).

### Compared with tipitaka.app

| Layer | Site node | Range | Headings matching in title and order |
|---|---|---|---|
| aṭṭhakathā | `atta-ap-pp-6-34` … `-43` | paras 1620–1876 | 45 of 45 |
| mūlaṭīkā | `tika-ap-pp-4` | paras 864–1057 | 48 of 48 |
| anuṭīkā | `tika2-ap-pp-5` | paras 916–1137 | 47 of 47 |

- Numbered paragraphs: the same count, order and printed numbers as the site (78 / 48 / 48).
- Text: with printed numbers compared separately, the body text is identical to the site word for word (9,053 / 8,104 / 10,779 words). The only extra line is the homage `^T-1` at the top of the two ṭīkā files, which the site prints once at the start of each combined Pañcapakaraṇa ṭīkā.
- The site's sidebar tree is mis-nested for pi-6 (for example, in both ṭīkās "3. Āyatanayamakaṃ" to "9. Dhammayamakaṃ" hang under a "1. Paṇṇattivāro" node). The hierarchy was therefore checked against the site's printed numbering, which the vault follows in all three files.

### Fixes made: 41 glued words

In every case the site has a bold lemma split by a page marker (for example `**Yassa** |V0.0296| **rūpakkhandho**`), and the conversion dropped the spaces around it. Each fix inserts one space.

- aṭṭhakathā (14): Satte vāti (`^6-155`, split as the site prints it; the same paragraph keeps `sattevāti` twice, also as printed), Tīṇeva kusalamūlānīti, Ahetukaṃ abyākatanti, Sahetukaṃ nāmaṃ, Yassa rūpakkhandho, na parijānitthāti, Cittassa bhaṅgakkhaṇeti, Dvinnaṃ puggalānaṃ, kāmarāgānusayo nānusetīti, Na kāmadhātunti, Uppādakkhaṇe anāgatañcāti, anantarā aggamagganti, Yassa cittassa, Pavatte somanassavippayuttacittassa
- mūlaṭīkā (12): Kusalākusalamūlasaṅkhātānaṃ dvinnaṃ, Aññamaññayamake ye, ca ṭhapetvā, Imināyeva ca, Puggalokāsavāro labbhamānopīti, Dukkhaṃ dukkhasaccanti, Antamaso suddhāvāsānampīti, vā pana, Anuseti uppajjatīti, Pahīnavāre phalaṭṭhavaseneva, Tathārūpasseva khīṇāsavassa, Sacakkhukānaṃ vinā
- anuṭīkā (15): Vuttabyañjanatthasseva sambhavatoti, Mūlayogaṃ dīpetunti, Evaṃ vuttanti, vedanādayo daṭṭhabbā, tīraṇapariññāva vuttā, Saṅkhārānaṃ puggalānañca, bhūmīnaṃ okāsabhāvasseva, Samudāyavasena gahetvāti, Desanā saṃkiṇṇā, Yathā mūlayamake, Sanniṭṭhānena gahitesu, Indriyayamake vibhaṅge, Koci sabhāvo, Apāye opapātikavasenāti, Bhāvetabbapahātabbabhāvehi vināpi

A re-scan against the site found no other glued words, and nothing is left for specialist review.

### Intentional differences from the website

| Ours | Site | Note |
|---|---|---|
| each yamaka is a `###` sibling with its vāras nested | the ṭīkā sidebars nest later yamakas inside earlier vāras | the vault is cleaner |
| aṭṭhakathā Cittayamaka: Puggalavāravaṇṇanā `^6-8-2-1-0` under Niddeso | flat siblings | Niddeso has no body of its own; its child is printed "1." |
| Nigamanakathā `^6-11-0` as a sibling of the yamakas | nested under Indriyayamakaṃ | same pattern as pi-3 to pi-5 |
| aṭṭhakathā opening verses `^6-1` … `^6-3` directly under `## ^6-0` | the same (the source has no Ganthārambha heading here) | matches the site |
| heading IDs by sibling position | the site prints "1.", "2.", and skips numbers in Mahāvāro (1, 2, 3, 5, 7) | by design |
| centred end-lines ("Uddesavāravaṇṇanā.", "… niṭṭhitā.") | the same | kept as body text |

**Kept as the source prints it:** the anuṭīkā Khandhayamaka has two "Paṇṇattivāro" headings (`^6-3-1-0` › Uddesavāravaṇṇanā, `^6-3-2-0` › Niddesavāravaṇṇanā), because the site prints "1. Paṇṇattivāro" twice (https://tipitaka.app/latn/tika2-ap-pp-5-4 and https://tipitaka.app/latn/tika2-ap-pp-5-5). The mūlaṭīkā prints it once, and the vault follows that too.

---

## Links to the root text (alignment)

Each numbered commentary paragraph has one `![[1-SOURCES/Text/pi-6.md#^6-{yamaka}-{N}]]` line per root verse directly above it; a printed range becomes consecutive lines. The yamaka zone comes from the `###` yamaka the paragraph sits under.

| | Numbered paragraphs | Transclusion lines | Distinct root targets | Alignment pairs |
|---|---|---|---|---|
| aṭṭhakathā | 78 | 1,276 | 1,276 | 6,517 |
| mūlaṭīkā | 48 | 979 | 979 | 5,499 |
| anuṭīkā | 48 | 1,009 | 1,009 | 6,162 |

- Every target exists in `pi-6.md`. No printed range runs backwards and none is abbreviated, so no citation needed an entry in `known-source-irregularities.md`.
- Each citation's first root verse sits in the matching root section (Paṇṇatti → Paṇṇattivāro, Pavatti → Paccuppanna/Atīta/…, Pariññā → Pariññāvāro, Mahāvāra parts → the same vāra).
- **Check for the numbering restarts (2026-10-30).** Because the root restarts its numbers in every yamaka, a printed number `A` can match up to ten blocks (`^6-1-A` … `^6-10-A`). For each paragraph, every possible yamaka was scored on meaning (the paragraph's quoted words appear in that yamaka's verses) and context (the yamaka's subject appears in the paragraph and its neighbours). 147 of 174 paragraphs had a clear winner, which was the block already linked. The other 27 were read by hand and all confirmed the current block. Examples: aṭṭhakathā `1-19.` says "dhātuyamakassa vaṇṇanā" → `^6-4`; aṭṭhakathā `99.` "kusalākusalānaṃ ekato anirujjhanato 'no'" matches `^6-9-99`, not `^6-8-99`; mūlaṭīkā `22-254.` cites "(yama. 1.āyatanayamaka.22)" → `^6-3-22`; anuṭīkā `74-85.` "abyākatamūlena na ekamūlakaṃ" matches `^6-1-74`, not `^6-9-74`. No link was changed.
- One placement to know about: the aṭṭhakathā Indriyayamaka paragraph printed `1-86.` (root Paṇṇattivāro) sits under Pavattivāravaṇṇanā. The site places it the same way, and it is linked as printed.
- Alignment pairs are high because a paragraph that follows a large group (for example `22-254.`, 233 verses) aligns to every verse in the group. There is no alignment between commentary layers.

---

## Titles

`Yamakappakaraṇa-aṭṭhakathā`, `Yamakapakaraṇa-mūlaṭīkā`, `Yamakapakaraṇa-anuṭīkā`: the book headings as printed in the source, which tipitaka.app uses too. All three carry `tag_ids: [296WZOr8MXWteSqBBI7pl]`.

---

## Linter, parser and upload

`license: cc0` and the tag were added; the linter filled `commentary_of: IZ74xHeWa9xortlOhL6cc` and `category_id: MZUUxphQ0yFwLBon3Vng8` from `pi-6.md`. Warnings only: author/translator and `alt_titles` missing.

| | aṭṭhakathā | mūlaṭīkā | anuṭīkā |
|---|---|---|---|
| Content (characters) | 92,417 | 83,787 | 114,816 |
| Segments | 196 | 147 | 175 |
| TOC nodes / max depth | 46 / 4 | 49 / 4 | 48 / 4 |
| Alignment pairs | 6,517 | 5,499 | 6,162 |

Uploaded per file: `POST /v2/texts`, `POST /v2/texts/{id}/editions`, `PUT /v2/editions/{root_edition}/alignments/{edition}` (root as the source side), `POST /v2/editions/{edition}/table-of-contents`. Root edition: `vYtNelE9z5AWQ0jAv82cC`.

| | text_id | edition_id | toc_id |
|---|---|---|---|
| root `pi-6.md` | `IZ74xHeWa9xortlOhL6cc` | `vYtNelE9z5AWQ0jAv82cC` | `Jn8erKpW4PQSv9NcjBEwU` |
| aṭṭhakathā | `cUpbK3Y0ljPyLDcAirNbP` | `kocWHwHRuH3lc5Odf6Xfy` | `uO0m1mTDQ4fPsefPOPQxC` |
| mūlaṭīkā | `mTZwGbmllr9P0WOwBj6DI` | `2GNMKB0g0zr1YzbBosLuE` | `IWi4VypR4Mb369LOT6sJr` |
| anuṭīkā | `1dUcj3Ct12ccgItOuslPV` | `GwnGsBoL586jz6lrD0Va6` | `zr3RFZ2uHXESixIYIXGAf` |

**Live library, checked 2026-10-30:** all titles match the files and all four texts carry the Abhidhamma tag `296WZOr8MXWteSqBBI7pl` (the root file itself has no `tag_ids` line); the three commentary titles were updated with `PATCH /v2/texts/{text_id}`; the alignments match the files pair for pair (6,517 / 5,499 / 6,162), and the root content matches the stored output.

---

## Important: the live root edition uses the older parser

Like pi-3, the root edition in the library was built with an older parser that puts headings inside the edition text:

| | Live / stored (older parser) | Current `parser.py` |
|---|---|---|
| Segments | 3,128 (2,088 numbered + **1,039 heading** + 1 top) | 2,089 (no heading segments) |
| Heading text inside the content | yes | no |

The text itself is the same. The commentary alignments point only at content segments, so they are not affected. Re-uploading the root edition would delete every alignment on it, so changing it is a separate decision.

Because of the heading fix above, the live TOC was replaced with the rebuilt one on 2026-10-30 (`Jn8erKpW4PQSv9NcjBEwU`, which replaces `VaANYhf8m9tC5XdbtBgcv`). The 196 heading segments in the live edition keep their old references (for example `6-6-21-0`): the API cannot rename a segment, and replacing the segmentation would delete the three commentary alignments. Nothing uses those heading segments. They will be renewed if the root edition is ever rebuilt in the current format.

---

## Things to know

- Running the linter rewrites the tracked `4-SYSTEM/scripts/linter-commentary/languages.py`; restore it with `git checkout`.
- Not looked at: the rendered pages on tipitaka.app or the WeBuddhist reader. Open each text in the reader to see the TOC tree.

## Files to commit

The three commentary `.md` files, their `.lint.json` files, the three commentary parser output folders and this report. Never `.env`.

## Related

- ID rules: `4-SYSTEM/Guidelines/block-id-spec.md`
- Source stray numbers: `4-SYSTEM/Guidelines/known-source-irregularities.md`
- Root-text audit pattern: `0-INBOX/pi-3-hierarchy-and-upload-report.md`
