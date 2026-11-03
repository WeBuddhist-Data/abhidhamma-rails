# Paṭṭhāna (`pi-7`) — root text and commentaries: structure, content, and upload readiness

**Date:** 2026-10-30  
**Texts:**

- Root: `1-SOURCES/Text/pi-7.md` (Paṭṭhānapāḷi, Abhidhamma book 7)
- `1-SOURCES/Commentaries/pi-patthana-atthakatha.md`
- `1-SOURCES/Commentaries/pi-patthana-mulatiika.md`
- `1-SOURCES/Commentaries/pi-patthana-anutiika.md`

**Checked against:** tipitaka.app (`ap-pat-1` … `-5` for the root; Pañcapakaraṇa-aṭṭhakathā paras 1877–2610, `tika-ap-pp-5` paras 1059–1486 and `tika2-ap-pp-6` paras 1139–1510 for the commentaries, through its `/api/children` and `/api/text` endpoints), `4-SYSTEM/Guidelines/block-id-spec.md`, the linters and parsers under `4-SYSTEM/scripts/`, and the live WeBuddhist library (root text only; the commentaries are not uploaded yet).

This note is for someone opening the project cold. It records what was checked, what was fixed, what differs from the website on purpose, and what is still open before upload. **Nothing is uploaded or committed.**

---

## Summary of changes

### What was fixed

| Issue | What was wrong | Fix | Example | Applied to |
|---|---|---|---|---|
| Commentaries in the old import format | heading levels skipped (`##` straight to `####`), old heading IDs (`^7-0-1-0`), no root links | each file rebuilt from the source paragraphs: text, headings, printed numbers and verse grouping exactly as on tipitaka.app, IDs by the block-ID spec | `#### Ganthārambhavaṇṇanā ^7-0-1-0` → `### Ganthārambhavaṇṇanā ^7-1-0` | the three commentary files |
| Glued words in the commentaries | 17 / 29 / 27 places where a page marker and the spaces around it had been dropped | the source's word boundary restored | `Arūpinodhammā` → `Arūpino dhammā`; `Uppajjamānovasahuppādabhāvenāti` → `Uppajjamānova sahuppādabhāvenāti`; `Yaṃkiñci` → `Yaṃ kiñci` | the three commentary files |
| No links to the root text | the commentaries had no root-verse transclusions, so there was no alignment | one link per root verse above each numbered paragraph, from its printed citation (616 / 460 / 433 lines) | aṭṭhakathā `1.` (Paccayaniddeso) → `^7-1-1`; `25-34.` (Pucchāvāro) → `^7-1-25` … `^7-1-34`; `79.` "Vitakkattike …" → `^7-7-79` | the three commentary files |
| Links that are not in the source | the mūlaṭīkā had 113 links to the aṭṭhakathā | removed; pi-3 to pi-6 have no links between commentary layers | `![[…pi-patthana-atthakatha.md#^7-21]]` removed | mūlaṭīkā |
| Titles not as in the source | the titles carried "(extract from Pañcapakaraṇa-…)" | set to the source's book headings | `Paṭṭhānapakaraṇa-mūlaṭīkā (extract from Pañcapakaraṇa-mūlaṭīkā)` → `Paṭṭhānapakaraṇa-mūlaṭīkā`; `Paṭṭhānappakaraṇa-aṭṭhakathā`; `Paṭṭhānapakaraṇa-anuṭīkā` | commentary frontmatter |
| Missing licence and tag; linked fields empty | not set | added; the linter filled the linked fields from `pi-7.md` | `license: cc0`; `tag_ids: [296WZOr8MXWteSqBBI7pl]`; `commentary_of: XtTiyeogM96K1Chqpbccr` | commentary frontmatter |
| Root: missing space before `…pe…` | 7 places where a page marker was removed together with the space before it | space restored as in the source | `pakatūpanissayo…pe….` → `pakatūpanissayo …pe….`; `sahajātādhipati…pe….` → `sahajātādhipati …pe….` | `pi-7.md` and the stored root output; library pending |
| Root: curly-brace notes changed to square brackets | the source marks some notes with `{…}`; the conversion had turned 27 of them into `[…]`, which the source uses for a different kind of note | `{…}` restored | `[kabaḷiṅkāro (ka. sī. syā.)]` → `{kabaḷiṅkāro (ka. sī. syā.)}`; `[thīnaṃ (sī. syā.)]` → `{thīnaṃ (sī. syā.)}` | `pi-7.md` and the stored root output; library pending |

### What was checked and left unchanged

| Item | Why nothing was changed |
|---|---|
| Root heading **nesting** (424 places where tipitaka.app's tree nests headings differently) | neither our tree nor the site's is fully right, and the printed numbering alone does not settle it (see "Root heading nesting — open"). A correct tree needs a decision on the Paṭṭhāna's structure |
| Order of the headings at the start of each site volume (6 headings) | the site prints the volume label and `Dhammānulome` / `Tikapaṭṭhānaṃ` before the chapter heading; the file has the chapter first. Reordering would mean rewriting the live root text, which still stores headings inside it |
| Repeated homage and title lines of volumes 2–5 | the vault keeps the five volumes as one book, as for the three Yamaka volumes in pi-6 |
| Homage line `^T-1` at the top of the two ṭīkās | same convention as pi-4 to pi-6; the site prints it once at the start of each combined ṭīkā |
| Printed numbers on headings (`1.`, `5-22.`, `(1)`) | dropped from heading titles as in pi-4 to pi-6; the heading ID records the position |
| `Paccayavāravaṇṇanā niṭṭhitā.` (aṭṭhakathā) | the site shows this end-line as a heading; it is kept as body text, as in pi-5 |
| Live root edition in the older parser format | the text is correct; rebuilding it would delete every alignment on it, so it is a separate decision |

---

## What these files are

`pi-7.md` is the **root mūla** of the Paṭṭhāna, merged from tipitaka.org CSCD `abh03m7` … `abh03m11` (the site's five volumes, `ap-pat-1` … `-5`). It is already in the library. The three commentaries are its aṭṭhakathā, mūlaṭīkā and anuṭīkā, taken from the combined Pañcapakaraṇa commentaries on tipitaka.app. Each commentary paragraph links to the root verses it explains, and those links become the alignment in the library.

---

## How IDs work

| Track | Shape | Example | Meaning |
|---|---|---|---|
| Heading | ends in `-0` | `^7-4-1-1-0` | TOC node only |
| Root content | numbering run + printed number | `^7-2-53` | root paragraph 53 of the 2nd numbering run; 76 runs, each restarting where the source restarts its count |
| Root content without a number | `U` | `^7-U1` | unnumbered root block (459) |
| Commentary content | running counter | `^7-1` … `^7-590` | the Nth paragraph of that commentary file |
| Link to root | transclusion | `![[1-SOURCES/Text/pi-7.md#^7-2-53]]` | the root verse a commentary paragraph explains |

The root's numbering runs do not line up with its `###` sections: for example run 1 covers both Paccayaniddeso (1–24) and Pucchāvāro (25–52), and run 2 starts in Kusalattika at 53. The commentaries cite exactly these numbers.

---

## Root text (`pi-7.md`)

### Outline

- **8,170 headings**, levels `#` to `#####`, each with a `-0` anchor. Every child ID extends its parent's; siblings run 1…n with no gaps; no level skips.
- 76 top-level sections: (1) Paccayuddeso, (2) Paccayaniddeso, Pucchāvāro, the 22 tikas, the duka gocchakas, the dukatika, tikaduka, tikatika and dukaduka paṭṭhānas, and the paccanīya, anulomapaccanīya and paccanīyānuloma paṭṭhānas.

### Body

- **8,079 content IDs** (homage `^T-1`, 459 unnumbered `^7-U…`, the rest in 76 numbering runs), each run 1…max with no gaps or duplicates.
- **11,500 continuation lines** have no ID of their own; they belong to the block whose ID follows.

### Compared with tipitaka.app (`ap-pat-1` … `-5`)

- The site has **27,761 paragraphs**; the file has 8,170 headings + 8,079 ID lines + 11,500 continuation lines = **27,749**. The 12 extra on the site are the homage and title lines repeated at the start of volumes 2–5.
- Headings match in title and order, apart from those volume lines.
- The **7,619 printed paragraph numbers** are identical.
- After the fixes, all **19,579 body lines are identical to the site character for character**.

### Fixes made (2026-10-30)

7 spaces restored before `…pe…` (file lines 5806, 6792, 7642, 7647, 8091, 16461, 20549) and 27 `{…}` notes restored in 25 lines. No word, number or heading changed. The stored `parser-root-text/output/pi-7/` edition and TOC have the same 61 edits (spans shifted for the 7 inserted spaces).

### Root heading nesting — open

tipitaka.app's own tree gives 7,735 of 8,159 headings the same parent as the file. In the 424 others:

| Count | File | Site |
|---|---|---|
| 102 | `Anulomaṃ – hetupaccayo`, `Ārammaṇapaccayo` … beside `Vibhaṅgavāro` under `Paccayānulomaṃ` | under `Vibhaṅgavāro` |
| 145 | the same pattern with `Saṅkhyāvāro` / `Vibhaṅgavāro` | under them |
| 70 | subsections beside `4. Paccayapaccanīyānulomaṃ` | under it |
| 107 | other places of the same kind, and the volume starts | |

The source numbers `1. Vibhaṅgavāro` and `2. Saṅkhyāvāro`, and the unnumbered headings after each are their contents, so on these the **site is right and the file is flat**. But the site's tree is wrong elsewhere: it puts the nayas `2. Paccayapaccanīyaṃ`, `3.` and `4.` inside `Dumūlakādi` (they are siblings of `1. Paccayānulomaṃ`), and files the whole Dukatika-paṭṭhāna inside Kilesagocchaka. Following the printed numbers alone does not work either: the Paṭṭhāna reuses several "1., 2., …" series inside one section (vāras, nayas, vibhaṅga/saṅkhyā), and the source's heading types are not consistent, so the result ran to 10 levels with level skips.

A correct tree needs the Paṭṭhāna's structure modelled — tika → vāra → naya → vibhaṅga/saṅkhyā → paccaya — and checked against the commentaries, which already follow it. That is deeper than markdown's six heading levels, so it needs a decision before it is changed. The headings were therefore left as they are. Changing them later does not affect the commentary links, which point only at content IDs.

---

## Commentaries

### Outline (all three files)

```
# Abhidhammapiṭake (…)                          ^0
## Paṭṭhāna…                                    ^7-0
### Ganthārambhavaṇṇanā                         (ṭīkās only)
### Paccayuddesavaṇṇanā
### Paccayaniddeso
#### Hetupaccayaniddesavaṇṇanā … Pakiṇṇakavinicchaya   the paccaya-niddesas
### Pucchāvāro
#### Paccayānulomavaṇṇanā … Paccanīyānulomavaṇṇanā    the four nayas
### Kusalattikavaṇṇanā
#### Paṭiccavāravaṇṇanā … Pañhāvāravibhaṅgavaṇṇanā    the vāras
##### Paccayānulomaṃ, Paccayapaccanīyavaṇṇanā …        nayas, gaṇanā parts
###### Vibhaṅgavāro, Saṅkhyāvāro
### Vedanāttika … the later tikas and paṭṭhānas
### Nigamanakathā                                (aṭṭhakathā only)
```

- The tree follows the source's heading types (chapter / title / subhead) and its printed numbering; the mūlaṭīkā and anuṭīkā trees are identical heading for heading.
- No level skips; every heading ID ends in `-0` and extends its parent's; siblings run 1…n with no gaps.
- Content IDs are one continuous counter per file: aṭṭhakathā `^7-1` … `^7-590` (67 headings), mūlaṭīkā `^7-1` … `^7-343` (56), anuṭīkā `^7-1` … `^7-317` (55).

### Compared with tipitaka.app

| Layer | Site paragraphs | Body lines identical (incl. punctuation) | Headings (title, order) | Printed numbers |
|---|---|---|---|---|
| aṭṭhakathā | 1877–2610 | 667 of 667 | 65 of 65 | 185 identical |
| mūlaṭīkā | 1059–1486 | 374 of 374 | 54 of 54 | 119 identical |
| anuṭīkā | 1139–1510 | 319 of 319 | 53 of 53 | 112 identical |

The only extra line is the homage at the top of the two ṭīkās. The site's sidebar trees are not used for nesting: they put, for example, Vedanāttika under Paṭiccavāro under Kusalattika.

---

## Links to the root text (alignment)

Each numbered commentary paragraph has one `![[1-SOURCES/Text/pi-7.md#^7-{run}-{N}]]` line per root verse directly above it; a printed range becomes consecutive lines.

**How each target was found.** The commentary section was matched by name to its root section (Kusalattikavaṇṇanā → Kusalattikaṃ, Saṅkiliṭṭhattikādivaṇṇanā → the tikas from Saṃkiliṭṭhattikaṃ to Sanidassanattikaṃ, Dukapaṭṭhānavaṇṇanā → the duka gocchakas, and so on), and the printed number was looked up in the numbering runs inside that section. 411 of 416 citations matched exactly one place. The other 5 were settled by meaning:

| Paragraph | Possible places | Linked to | Why |
|---|---|---|---|
| aṭṭhakathā `79.` (Saṅkiliṭṭhattikādi) | 4 tikas | `^7-7-79` | the paragraph opens "Vitakkattike …" |
| aṭṭhakathā `82.` | 4 tikas | `^7-7-82` | it sits between `79.` and "Dassanattike …"; root 82 (cuti and upapatti citta) fits its "tadārammaṇa-bhavaṅga" remark |
| aṭṭhakathā `1.` (Paccanīyapaṭṭhāna) | 6 sub-paṭṭhānas | `^7-57-1` | quotes "nakusalaṃ dhammaṃ paṭicca nakusalo dhammo uppajjati hetupaccayā", the first line of `^7-57-1` |
| aṭṭhakathā `1.` (Anulomapaccanīyapaṭṭhāna) | 6 | `^7-63-1` | quotes "kusalaṃ dhammaṃ paṭicca na kusalo …" |
| aṭṭhakathā `1.` (Paccanīyānulomapaṭṭhāna) | 6 | `^7-69-1` | quotes "nakusalaṃ dhammaṃ paṭicca akusalo …" |

| | Numbered paragraphs | Link lines | Distinct root targets | Alignment pairs |
|---|---|---|---|---|
| aṭṭhakathā | 185 | 616 | 616 | 1,285 |
| mūlaṭīkā | 119 | 460 | 460 | 869 |
| anuṭīkā | 112 | 433 | 433 | 893 |

**Checks:**

- Every link resolves in `pi-7.md`, and no linked range crosses into another root section. All 3,047 alignment targets exist as segments in the live root edition.
- Meaning: in 143 of 146 aṭṭhakathā paragraphs, at least half of the quoted (bold) words occur in the linked root verses. The other 3 were read: `191-195.` and `543-544.` quote the same phrases with the other spelling of the sandhi (`nārammaṇa` / `naārammaṇa`, `nāhāra` / `naāhāra`), and Vedanāttika `6.` discusses the counts its root verse lists.
- Layers agree: the 113 mūlaṭīkā paragraphs that the aṭṭhakathā also comments on point to the same root numbering run, and the 110 anuṭīkā paragraphs that the mūlaṭīkā also comments on have identical links.
- There is no alignment between commentary layers, as for pi-3 to pi-6.

---

## Titles

`Paṭṭhānappakaraṇa-aṭṭhakathā`, `Paṭṭhānapakaraṇa-mūlaṭīkā`, `Paṭṭhānapakaraṇa-anuṭīkā`: the book headings as printed in the source, which tipitaka.app uses too. All three carry `tag_ids: [296WZOr8MXWteSqBBI7pl]`. The root `Paṭṭhānapāḷi` already has that tag in the library.

---

## Linter, parser and upload

All three commentaries lint OK and parse OK. Warnings only: author/translator and `alt_titles` missing. The linter filled `commentary_of: XtTiyeogM96K1Chqpbccr` and `category_id: MZUUxphQ0yFwLBon3Vng8` from `pi-7.md`. A fresh lint and parse gives identical output.

| | aṭṭhakathā | mūlaṭīkā | anuṭīkā |
|---|---|---|---|
| Content (characters) | 276,755 | 141,785 | 178,001 |
| Segments | 591 | 344 | 318 |
| TOC nodes / max depth | 67 / 5 | 56 / 5 | 55 / 5 |
| Alignment pairs | 1,285 | 869 | 893 |

**Not uploaded yet.** Before upload:

1. Apply the 61 text edits to the live root edition (`PATCH /v2/editions/03TkdCHL1y2qqnI0aVBNG/content`, listed in `0-INBOX/pi7-root-patch/pi-7-content-patches.jsonl`, from the end of the text backwards). Simulated on the live text, they give exactly the stored output.
2. Upload each commentary: `POST /v2/texts`, `POST /v2/texts/{id}/editions`, `PUT /v2/editions/03TkdCHL1y2qqnI0aVBNG/alignments/{edition}` (root as the source side), `POST /v2/editions/{edition}/table-of-contents`; then save `text_id`, `edition_id` and `toc_id` in each file's frontmatter.

Root IDs: `text_id XtTiyeogM96K1Chqpbccr`, `edition_id 03TkdCHL1y2qqnI0aVBNG`, `toc_id jHY9LvtNGWKb3xSVcyn14`.

---

## Important: the live root edition uses the older parser

Like pi-3 to pi-6, the root edition in the library was built with an older parser that puts headings inside the edition text:

| | Live / stored (older parser) | Current `parser.py` |
|---|---|---|
| Segments | 16,249 (8,079 content + **8,170 heading**) | 8,079 (no heading segments) |
| Heading text inside the content | yes | no |

The text itself is the same. The commentary alignments point only at content segments, so they are not affected. Re-uploading the root edition would delete every alignment on it, so changing it is a separate decision. The root TOC in the library matches the file node for node; its spans shift by themselves when the 7 spaces are inserted.

---

## Things to know

- 1,691 root headings have no text of their own (titles directly followed by the next heading); they are in the TOC with an empty span.
- Running the linter rewrites the tracked `4-SYSTEM/scripts/linter-commentary/languages.py`; restore it with `git checkout`.
- `0-INBOX/pi7-root-patch/` is a helper for the library update; do not commit it.
- Not looked at: the WeBuddhist reader. Open the texts there after upload to see the TOC and the commentary panel.

## Files to commit

`1-SOURCES/Text/pi-7.md`, `4-SYSTEM/scripts/parser-root-text/output/pi-7/`, the three commentary `.md` files, their `.lint.json` files, the three commentary parser output folders and this report. Never `.env`.

## Related

- ID rules: `4-SYSTEM/Guidelines/block-id-spec.md`
- Source typos and stray numbers: `4-SYSTEM/Guidelines/known-source-irregularities.md`
- Earlier reports: `0-INBOX/pi-3-hierarchy-and-upload-report.md` … `pi-6-hierarchy-and-upload-report.md`
