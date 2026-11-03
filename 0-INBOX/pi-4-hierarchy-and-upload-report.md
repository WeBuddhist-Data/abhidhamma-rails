# Puggalapaññatti (`pi-4`) — root text and commentaries: structure, content, and upload

**Date:** 2026-10-28 (updated 2026-10-30)  
**Texts:**

- Root: `1-SOURCES/Text/pi-4.md` (Puggalapaññattipāḷi, Abhidhamma book 4)
- `1-SOURCES/Commentaries/pi-puggalapannatti-atthakatha.md`
- `1-SOURCES/Commentaries/pi-puggalapannatti-mulatiika.md`
- `1-SOURCES/Commentaries/pi-puggalapannatti-anutiika.md`

**Checked against:** tipitaka.app (`ap-pug` for the root; `atta-ap-pp-4`, `-5`, `tika-ap-pp-2`, `tika2-ap-pp-3` for the commentaries, through its `/api/children` and `/api/text` endpoints), `4-SYSTEM/Guidelines/block-id-spec.md`, the linters and parsers under `4-SYSTEM/scripts/`, and the live WeBuddhist library (content, segments, alignments, titles).

This note is for someone opening the project cold. It records what was checked, what was fixed, what differs from the website on purpose, and what to know before changing the live reader. pi-1, pi-2, pi-3, pi-5, pi-6 and pi-7 were not touched.

---

## Summary of changes

### What was fixed

| Issue | What was wrong | Fix | Example | Applied to |
|---|---|---|---|---|
| Glued words in the root text | 6 words were joined where the source has a space (a page marker sat between them and the conversion dropped the space) | one space inserted in each | `Dvepuggalā` → `Dve puggalā`; `Kittāvatāpuggalānaṃ` → `Kittāvatā puggalānaṃ`; `Navapuggalā` → `Nava puggalā` | `pi-4.md`, the live root edition (`PATCH …/content`, 2026-10-30) and the stored root output |
| Glued words in the commentaries | 21 words joined the same way (9 / 8 / 4) | one space inserted in each | `Labhantosappāyāni` → `Labhanto sappāyāni`; `Hīnohoti` → `Hīno hoti`; `Saddhānāma` → `Saddhā nāma` | the three commentary files, before upload |
| Missing licence | the linter refused all three commentaries: `license` is required | added, as on every other text | `license: cc0` | commentary frontmatter |
| Missing tag | no Abhidhamma tag on the commentaries | added | `tag_ids: [296WZOr8MXWteSqBBI7pl]` | commentary frontmatter and library |
| Titles not as in the source | the titles carried "(extract from …)", then the ṭīkā titles were shortened | set to the source's book headings | `Puggalapaññatti-mūlaṭīkā (extract from Pañcapakaraṇa-mūlaṭīkā)` → `Puggalapaññattipakaraṇa-mūlaṭīkā`; anuṭīkā likewise; aṭṭhakathā `Puggalapaññatti-aṭṭhakathā` | frontmatter and library (`PATCH /v2/texts/{id}`, 2026-10-30) |
| Linked fields empty | `commentary_of` and `category_id` were not set | filled by the linter from `pi-4.md` | `commentary_of: leKc1Ei0OBaZN2FNMqlpL` | commentary frontmatter |

The commentaries were uploaded once these were fixed; their IDs are in the frontmatter.

### What was checked and left unchanged

| Item | Why nothing was changed |
|---|---|
| Root-text structure (24 headings, IDs `^4-M-1` … `^4-M-16`, `^4-1` … `^4-209`) | it matches tipitaka.app in headings, nesting, paragraph count and printed numbers |
| Root-verse links in the commentaries (148 / 71 / 57 targets, added 2026-10-27) | every link resolves and names the same root verses as the site |
| Commentary hierarchy | it follows the source's numbering; where the site's sidebar files headings elsewhere, the vault keeps the cleaner tree (see "Intentional differences") |
| Live root edition in the older parser format | the text is correct; rebuilding it would delete every alignment on it, so it is a separate decision |

---

## What these files are

`pi-4.md` is the **root mūla** of the Puggalapaññatti, ingested from tipitaka.org CSCD `abh03m2.mul.xml`. The three commentaries are its aṭṭhakathā, mūlaṭīkā and anuṭīkā, extracted from the combined Pañcapakaraṇa commentaries. Each commentary paragraph links to the root verses it explains, and those links become the alignment in the library.

---

## How IDs work

| Track | Shape | Example | Meaning |
|---|---|---|---|
| Heading | ends in `-0` | `^4-2-8-0` | TOC node only (Dasakaniddesavaṇṇanā) |
| Root content | printed number | `^4-M-7`, `^4-209` | one numbered root paragraph; the mātikā has its own zone `M` |
| Commentary content | running counter | `^4-1` … `^4-272` | the Nth paragraph of that commentary file |
| Link to root | transclusion | `![[1-SOURCES/Text/pi-4.md#^4-203]]` | the root verse a commentary paragraph explains |

Headings use **sibling position** under their parent, so Dasaka is `^4-2-8-0` although the site prints "10." This is by design (`block-id-spec.md` §5), the same as pi-3.

---

## Root text (`pi-4.md`)

### Outline

- **24 headings**, levels `#` to `####`, each with a `-0` anchor. Every child ID extends its parent's; siblings run 1…n with no gaps.
- The mātikā (Ekaka … Dasaka uddesa) sits in its own `M` zone with Roman sibling numbers (`^4-M-I-0` …); the niddesas follow as the body.

### Body

- Content IDs: homage `^T-1`, mātikā `^4-M-1` … `^4-M-16`, body `^4-1` … `^4-209`. No gaps, duplicates or resets beyond the mātikā zone.
- **311 continuation lines** (for example the numbered person lists `(1) Samayavimutto` …) have no ID of their own; they belong to the block whose ID follows.

### Compared with tipitaka.app (`ap-pug`)

- The site has **561 paragraphs**; the file has 24 headings + 226 ID lines + 311 continuation lines = **561**.
- All 24 headings match in title and order. The 225 printed paragraph numbers are identical.
- The text is identical to the site word for word (14,725 words) after the fixes below.

### Fixes made (2026-10-30)

Six words were glued together by the conversion where the site has a space. Each fix inserts one space:

`Kittāvatā puggalānaṃ`, `Dve puggalā`, `Tayo puggalā`, `Cattāro puggalā`, `Cha puggalā`, `Nava puggalā` (mātikā `^4-M-7` … `^4-M-15`).

The same six spaces were inserted in the live edition (`PATCH /v2/editions/4bCOP5KnJqlcTxSBZXYA3/content`), and the stored `parser-root-text/output/pi-4/` edition and TOC were updated to match. Live content and all 250 segment spans equal the stored files.

---

## Commentaries

### Outline (all three files)

```
# Abhidhammapiṭake                        ^0
## Puggalapaññatti…                       ^4-0
### Mātikāvaṇṇanā                         ^4-1-0
### Niddesavaṇṇanā                        ^4-2-0
#### Ekaka … Dasakaniddesavaṇṇanā         ^4-2-1-0 … ^4-2-8-0   (8 siblings)
### Nigamanakathā                         ^4-3-0   (aṭṭhakathā only)
```

- No heading level skips; every heading ID ends in `-0` and extends its parent's. The `^0` piṭaka root is the one ID without `-0` (`block-id-spec.md` §2).
- Content IDs are one continuous counter per file, with no gaps or duplicates: aṭṭhakathā `^4-1` … `^4-272`, mūlaṭīkā `^4-1` … `^4-90`, anuṭīkā `^4-1` … `^4-85`.
- The mūlaṭīkā and anuṭīkā have the same 12 heading nodes as the aṭṭhakathā, without Nigamanakathā (13 / 12 / 12).

### Compared with tipitaka.app

| Layer | Site node | What the site has |
|---|---|---|
| aṭṭhakathā | `atta-ap-pp-4`, `-5` | 1. Mātikāvaṇṇanā, 2. Niddesavaṇṇanā |
| | `atta-ap-pp-5-1` … `5-7`, `5-10` | Ekaka … Sattaka, "10." Dasaka; no Aṭṭhaka or Navaka vaṇṇanā |
| mūlaṭīkā | `tika-ap-pp-2`, `2-1` … `2-10` | the same 8-niddesa pattern |
| anuṭīkā | `tika2-ap-pp-3`, `3-1` … `3-10` | the same 8-niddesa pattern |

- Section titles, order and per-section paragraph counts match. The aṭṭhakathā Nigamanakathā has 14 paragraphs against 15 in the site range; the extra site paragraph is the next book's homage line.
- Text: 99.86 to 99.92 percent word match after the fixes; the only difference left is the homage line.

### Fixes made: 21 glued words

Found by comparing with tipitaka.app (usually a `|V0.00xx|` page marker sat between the two words); each fix inserts one space.

- aṭṭhakathā (9): Labhanto sappāyāni, Tesaṃ taṃ hotīti, Hīno hoti, Na kumbhimukhāti, Imesaṃ bhedāyāti, So abhikkante, evaṃ passatoti, Ummujjitvā pataratīti, Idha vihāyāti
- mūlaṭīkā (8): Khandhāti paññāpanāti, sabbākārenapi anupalabbhaneyya, jīvitindriyaṃ cuticittaṃ, Evaṃ maggakkhaṇepīti, Acchamaṃsaṃ labhitvā, Tattha tatthāti, Tattha sikkhanabhāvenāti, Saddhā nāma
- anuṭīkā (4): Pāḷiyaṃ anāgatatanti, Kiñci natthīti, Rūpato aññaṃ, rūpataṇhāvikkhambhanena rūpakāyato

A re-scan found no glued words left.

### Intentional differences from the website

| Ours | Site | Note |
|---|---|---|
| Dasaka `^4-2-8-0` (sibling position) | printed "10." | by design, same as pi-3 |
| `## ^4-0` book parent | the aṭṭhakathā book heading is filed under the end of Dhātukathā; Mātikā and Niddesa sit flat | the vault is cleaner |
| niddesas nested under `^4-2-0` | the mūlaṭīkā and anuṭīkā list them as siblings of Niddesavaṇṇanā | the vault is cleaner |
| Nigamanakathā `^4-3-0` under the book | nested under Dasaka | placement is a judgement call |
| homage `^T-1` at the top of each file | "Namo tassa…" at the end of the previous section | left out of the word comparison |

---

## Links to the root text (alignment)

- Every transclusion resolves in `pi-4.md`: **148 / 71 / 57** root targets (aṭṭhakathā / mūlaṭīkā / anuṭīkā), each under the right niddesa heading.
- The root references in each section are the same as the site's (for example `^4-209` in Dasaka, `^4-203` and `^4-207` in Sattaka).
- Alignment pairs: **267 / 91 / 86**. The alignment is commentary paragraph to root verse; there is no alignment between commentary layers.

---

## Titles

`Puggalapaññatti-aṭṭhakathā`, `Puggalapaññattipakaraṇa-mūlaṭīkā`, `Puggalapaññattipakaraṇa-anuṭīkā`: the book headings as printed in the source, which tipitaka.app uses too. They replace the earlier "(extract from …)" titles. All three carry `tag_ids: [296WZOr8MXWteSqBBI7pl]`.

---

## Linter, parser and upload

The linter required `license`; `license: cc0` was added (as on every other text, including `pi-4.md`). It filled `commentary_of: leKc1Ei0OBaZN2FNMqlpL` and `category_id: MZUUxphQ0yFwLBon3Vng8` from `pi-4.md`. Warnings only: author/translator and `alt_titles` missing.

| | aṭṭhakathā | mūlaṭīkā | anuṭīkā |
|---|---|---|---|
| Content (characters) | 139,279 | 30,006 | 32,807 |
| Segments | 273 (272 + 1 top) | 91 (90 + 1) | 86 (85 + 1) |
| TOC nodes / max depth | 13 / 3 | 12 / 3 | 12 / 3 |
| Alignment pairs | 267 | 91 | 86 |

Uploaded per file: `POST /v2/texts`, `POST /v2/texts/{id}/editions`, `PUT /v2/editions/{root_edition}/alignments/{edition}` (root as the source side), `POST /v2/editions/{edition}/table-of-contents`. Root edition: `4bCOP5KnJqlcTxSBZXYA3`.

| | text_id | edition_id | toc_id |
|---|---|---|---|
| root `pi-4.md` | `leKc1Ei0OBaZN2FNMqlpL` | `4bCOP5KnJqlcTxSBZXYA3` | `Cmp5KOPdf1Q1YOtThwOPM` |
| aṭṭhakathā | `zFpVKiUlHeRzziqpg6eeM` | `OslFzzW2jMdRIk8CuYIKx` | `XMG53zN2ej55HHK6cw5d5` |
| mūlaṭīkā | `2l1OAALDrKc9eEb4y8w7T` | `OBfpVFQNrYSWvCzFyvFiL` | `36JZciSCTXV9iqLvclMl9` |
| anuṭīkā | `kERYN9A8Z6DUE4kuEIu1R` | `VMuk7Vt3e5Ip9xM9ayJb4` | `9X2gXaqsGMOTic318C639` |

**Live library, checked 2026-10-30:** all titles match the files and all four texts carry the Abhidhamma tag `296WZOr8MXWteSqBBI7pl` (the root file itself has no `tag_ids` line); the mūlaṭīkā and anuṭīkā titles were updated with `PATCH /v2/texts/{text_id}`; the alignments match the files pair for pair (267 / 91 / 86), and the root content matches the stored output.

---

## Important: the live root edition uses the older parser

Like pi-3, the root edition in the library was built with an older parser that puts headings inside the edition text:

| | Live / stored (older parser) | Current `parser.py` |
|---|---|---|
| Segments | 250 (225 numbered + **24 heading** + 1 top) | 226 (no heading segments) |
| Heading text inside the content | yes | no |

The text itself is the same. The commentary alignments point only at content segments, so they are not affected. Re-uploading the root edition would delete every alignment on it, so changing it is a separate decision.

---

## Things to know

- Running the linter rewrites the tracked `4-SYSTEM/scripts/linter-commentary/languages.py`; restore it with `git checkout`.
- Not looked at: the rendered pages on tipitaka.app or the WeBuddhist reader. Open each text in the reader to see the TOC tree.

## Files to commit

`1-SOURCES/Text/pi-4.md`, the three commentary `.md` files, their `.lint.json` files, `4-SYSTEM/scripts/parser-root-text/output/pi-4/`, the three commentary parser output folders and this report. Never `.env`.

## Related

- ID rules: `4-SYSTEM/Guidelines/block-id-spec.md`
- Source typos and stray numbers: `4-SYSTEM/Guidelines/known-source-irregularities.md`
- Root-text audit pattern: `0-INBOX/pi-3-hierarchy-and-upload-report.md`
