# Kathāvatthu (`pi-5`) — root text and commentaries: structure, content, and upload

**Date:** 2026-10-29 (updated 2026-10-30)  
**Texts:**

- Root: `1-SOURCES/Text/pi-5.md` (Kathāvatthupāḷi, Abhidhamma book 5)
- `1-SOURCES/Commentaries/pi-kathavatthu-atthakatha.md`
- `1-SOURCES/Commentaries/pi-kathavatthu-mulatiika.md`
- `1-SOURCES/Commentaries/pi-kathavatthu-anutiika.md`

**Checked against:** tipitaka.app (`ap-kvu` for the root; `atta-ap-pp-6`, `tika-ap-pp-3`, `tika2-ap-pp-4` for the commentaries, through its `/api/children` and `/api/text` endpoints), tipitaka.lk for the irregular citations, `4-SYSTEM/Guidelines/block-id-spec.md`, the linters and parsers under `4-SYSTEM/scripts/`, and the live WeBuddhist library (content, segments, alignments, titles).

This note is for someone opening the project cold. It records what was checked, what was fixed, what differs from the website on purpose, and what to know before changing the live reader. The root text was not edited.

---

## Summary of changes

### What was fixed

| Issue | What was wrong | Fix | Example | Applied to |
|---|---|---|---|---|
| Glued words in the commentaries | 93 words were joined where the source has a space (25 / 47 / 21) | one space inserted in each | `Dibbenacakkhunā` → `Dibbena cakkhunā`; `Atītaṃatthīti` → `Atītaṃ atthīti`; `Ājānāhiniggaha` → `Ājānāhi niggaha` | the three commentary files, before upload |
| No links to the root text | the commentaries had no root-verse transclusions, so there was no alignment | one link per root verse above each numbered paragraph, from its printed citation (892 / 433 / 505 lines) | `621-624.` → links `^5-621` … `^5-624`; `627.` → link `^5-627` | the three commentary files and the library alignments |
| Three printed citations do not fit their section | they name verses outside the kathā the paragraph sits in (typos in the source) | linked exactly as printed, as the senior asked, and recorded in `known-source-irregularities.md`. They were first linked to the intended passage; on 2026-10-29 the live alignments were deleted and uploaded again with the as-printed links | `618-820.` → `^5-618` … `^5-820` (203 links); `541-545.` → `^5-541` … `^5-545`; `706-608.` → `^5-608` … `^5-706` | aṭṭhakathā and anuṭīkā files; library alignments |
| Abbreviated citations | the mūlaṭīkā prints two ranges in short form | written out and linked to both verses | `557-8.` → `557-558.`; `571-2.` → `571-572.` | mūlaṭīkā file; library text (`PATCH …/content`) |
| Missing licence and tag | not set | added | `license: cc0`; `tag_ids: [296WZOr8MXWteSqBBI7pl]` | commentary frontmatter and library |
| Titles not as in the source | the titles carried "(extract from …)", then the ṭīkā titles were shortened | set to the source's book headings | `Kathāvatthu-mūlaṭīkā (extract from Pañcapakaraṇa-mūlaṭīkā)` → `Kathāvatthupakaraṇa-mūlaṭīkā`; anuṭīkā likewise; aṭṭhakathā `Kathāvatthu-aṭṭhakathā` | frontmatter and library (`PATCH /v2/texts/{id}`, 2026-10-30) |

The commentaries were uploaded once these were fixed; their IDs are in the frontmatter.

### What was checked and left unchanged

| Item | Why nothing was changed |
|---|---|
| Root text `pi-5.md` | it matches tipitaka.app word for word, with the same 481 headings and 918 printed numbers, so no fix was needed |
| 13 possible compounds in the commentaries (`tenahi`, `dvepi` …) | they may be genuine compounds rather than glued words; left for a Pāli specialist |
| Particle "ti" written attached (`atthīti`) | the site only displays it apart (`atthī ti`); the source text has no space |
| Commentary hierarchy | it follows the source's numbering; where the site's sidebar is flat or misfiled, the vault keeps the cleaner tree |
| Live root edition in the older parser format | the text is correct; rebuilding it would delete every alignment on it, so it is a separate decision |

---

## What these files are

`pi-5.md` is the **root mūla** of the Kathāvatthu, ingested from tipitaka.org CSCD `abh03m3.mul.xml`. The three commentaries are its aṭṭhakathā, mūlaṭīkā and anuṭīkā, extracted from the combined Pañcapakaraṇa commentaries. Each commentary paragraph links to the root verses it explains, and those links become the alignment in the library.

---

## How IDs work

| Track | Shape | Example | Meaning |
|---|---|---|---|
| Heading | ends in `-0` | `^5-12-4-0` | TOC node only (a kathā) |
| Root content | printed number | `^5-618` | one numbered root paragraph; one flat run `1…918` |
| Commentary content | running counter | `^5-544` | the Nth paragraph of that commentary file |
| Link to root | transclusion | `![[1-SOURCES/Text/pi-5.md#^5-618]]` | the root verse a commentary paragraph explains |

Headings use **sibling position** under their parent, not the "1.", "2." the site prints. This is by design (`block-id-spec.md` §5), the same as pi-3 and pi-4.

---

## Root text (`pi-5.md`)

### Outline

- **481 headings**, levels `#` to `#####`, each with a `-0` anchor: the book, its vaggas, and the kathās inside them. Every child ID extends its parent's; siblings run 1…n with no gaps.

### Body

- Content IDs: homage `^T-1` and `^5-1` … `^5-918`, one flat run with no reset, gaps or duplicates.
- **2,060 continuation lines** (the questions and answers inside each numbered paragraph) have no ID of their own; they belong to the block whose ID follows.

### Compared with tipitaka.app (`ap-kvu`)

- The site has **3,460 paragraphs**; the file has 481 headings + 919 ID lines + 2,060 continuation lines = **3,460**.
- All 481 headings match in title and order. The 918 printed paragraph numbers are identical.
- The text is identical to the site word for word (75,800 words). No fixes were needed.

---

## Commentaries

### Outline (all three files)

```
# Abhidhammapiṭake (…)                       ^0
## Kathāvatthu…                              ^5-0
### Nidānakathā / Ganthārambha…              ^5-1-0 …
### Mahāvaggo … Tevīsatimavaggo              ^5-2-0 … (vaggas)
#### kathā (e.g. Puggalakathā)               ^5-2-1-0 …
##### … ###### sub-sections                  up to 6 levels
### Nigamanakathā                            ^5-25-0 (aṭṭhakathā only)
```

- No heading level skips; every heading ID ends in `-0` and extends its parent's; siblings run 1…n with no gaps.
- Content IDs are one continuous counter per file, with no gaps or duplicates: aṭṭhakathā `^5-1` … `^5-815` (278 headings), mūlaṭīkā `^5-1` … `^5-453` (211), anuṭīkā `^5-1` … `^5-491` (206).

### Compared with tipitaka.app

| Layer | Site node | Headings matching in title and order |
|---|---|---|
| aṭṭhakathā | `atta-ap-pp-6` | 277 of 277 |
| mūlaṭīkā | `tika-ap-pp-3` | 210 of 210 |
| anuṭīkā | `tika2-ap-pp-4` | 205 of 205 |

- Numbered paragraphs: the same count, order, heading and text as the site (388 / 223 / 208).
- Text: the only differences are the centred colophon lines the site shows as headings, which the vault keeps as body text.

### Fixes made: 93 glued words

Words fused by the conversion where tipitaka.app has a word boundary; only spaces were added: aṭṭhakathā 25, mūlaṭīkā 47, anuṭīkā 21. Examples: `Dibbenacakkhunā` → `Dibbena cakkhunā`, `Atītaṃatthīti` → `Atītaṃ atthīti`, `Ājānāhiniggaha` → `Ājānāhi niggaha`.

**⚑ Specialist review:** 13 forms may be genuine compounds and were left as they are: `tenahi`, `dvepi`, `navattabbaṃ`, `mahāpathavīādīni`, `rūpantiādi`, `maggotiādi`, `sakkāyadiṭṭhiādīsupi`, `satipaṭṭhānādīsupi`, `somādayo`, `kusalādipañhaṃ`, `sammutiñāṇapañhesu`, `suññatādiatthaṃ`, `liṅgākappabhedaṃ`.

### Intentional differences from the website

| Ours | Site | Note |
|---|---|---|
| vaggas group their kathās | the site trees are flat or misfiled | the vault is cleaner |
| Nigamanakathā `^5-25-0` as a sibling of the vaggas | nested under the last vagga | same pattern as pi-3 and pi-4 |
| heading IDs by sibling position | the site prints "1.", "2." | by design |
| particle "ti" attached (`atthīti`) | the site writes `atthī ti` | site display convention |

---

## Links to the root text (alignment)

Each numbered commentary paragraph has one `![[1-SOURCES/Text/pi-5.md#^5-N]]` line per root verse directly above it; a printed range becomes consecutive lines.

| | Numbered paragraphs | Transclusion lines | Distinct root targets | Alignment pairs |
|---|---|---|---|---|
| aṭṭhakathā | 388 | 892 | 890 | 1,841 |
| mūlaṭīkā | 223 | 433 | 433 | 903 |
| anuṭīkā | 208 | 505 | 505 | 1,124 |

- Every target exists in `pi-5.md`. Each paragraph links to the root verses its printed citation names, exactly as on tipitaka.app.
- There is no alignment between commentary layers.

**Irregular citations**, linked as the source prints them (recorded in `4-SYSTEM/Guidelines/known-source-irregularities.md`):

| Block | Printed | Linked to |
|---|---|---|
| aṭṭhakathā `^5-544` | `618-820.` | `^5-618` … `^5-820` (the paragraph sits under Idaṃ dukkhantikathā, root 618–620) |
| aṭṭhakathā `^5-568` | `541-545.` | `^5-541` … `^5-545` (it sits under Sattakkhattuparamakathā, root 641–645) |
| anuṭīkā `^5-381` | `706-608.` | `^5-608` … `^5-706`, read low to high (it sits under Abyākatakathā, root 706–708) |
| mūlaṭīkā `^5-270` | `557-8.`, written out as `557-558.` | `^5-557`, `^5-558` |
| mūlaṭīkā `^5-281` | `571-2.`, written out as `571-572.` | `^5-571`, `^5-572` |

---

## Titles

`Kathāvatthu-aṭṭhakathā`, `Kathāvatthupakaraṇa-mūlaṭīkā`, `Kathāvatthupakaraṇa-anuṭīkā`: the book headings as printed in the source, which tipitaka.app uses too. All three carry `tag_ids: [296WZOr8MXWteSqBBI7pl]`.

---

## Linter, parser and upload

`license: cc0` and the tag were added; the linter filled `commentary_of` and `category_id` from `pi-5.md`.

| | aṭṭhakathā | mūlaṭīkā | anuṭīkā |
|---|---|---|---|
| Content (characters) | 264,111 | 76,777 | 142,897 |
| Segments | 816 | 454 | 492 |
| TOC nodes | 278 | 211 | 206 |
| Alignment pairs | 1,841 | 903 | 1,124 |

Uploaded per file: `POST /v2/texts`, `POST /v2/texts/{id}/editions`, `PUT /v2/editions/{root_edition}/alignments/{edition}` (root as the source side), `POST /v2/editions/{edition}/table-of-contents`. Root edition: `WjnE60LMIzQETFlXoh9Hd`.

| | text_id | edition_id | toc_id |
|---|---|---|---|
| root `pi-5.md` | `HE6FGm4AAqwlDOTnCT0Yd` | `WjnE60LMIzQETFlXoh9Hd` | `UwzJZr7LmXMa0E72H9e1k` |
| aṭṭhakathā | `ynjwNOhnRKJzbfpL8fMY1` | `v5HrRlZFp7thp2aGTJJLm` | `bMmNIN47MJsaZlv02IyYT` |
| mūlaṭīkā | `Awq6BwDSyKA3BEvodcEmk` | `4rL7eOexrXBXN7UydZNnI` | `t4pwbvl4zFrGIx3hQe20b` |
| anuṭīkā | `s2GMCzOo9FrV9znoTCAM7` | `nkSDSS7ezbdrXo0XCxdvo` | `Cl385DCm70UPWZbQ1A5O1` |

Later updates to the live library: the written-out mūlaṭīkā citations (`557-558.`, `571-572.`) were inserted with `PATCH /v2/editions/{id}/content`; the aṭṭhakathā and anuṭīkā alignments were replaced when the irregular citations were relinked as printed; the mūlaṭīkā and anuṭīkā titles were updated with `PATCH /v2/texts/{text_id}`.

**Live library, checked 2026-10-30:** all titles match the files and all four texts carry the Abhidhamma tag `296WZOr8MXWteSqBBI7pl` (the root file itself has no `tag_ids` line), the alignments match the files pair for pair (1,841 / 903 / 1,124), and the root content matches the stored output.

---

## Important: the live root edition uses the older parser

Like pi-3, the root edition in the library was built with an older parser that puts headings inside the edition text:

| | Live / stored (older parser) | Current `parser.py` |
|---|---|---|
| Segments | 1,400 (918 numbered + **481 heading** + 1 top) | 919 (no heading segments) |
| Heading text inside the content | yes | no |

The text itself is the same. The commentary alignments point only at content segments, so they are not affected. Re-uploading the root edition would delete every alignment on it, so changing it is a separate decision.

---

## Things to know

- Running the linter rewrites the tracked `4-SYSTEM/scripts/linter-commentary/languages.py`; restore it with `git checkout`.
- Not looked at: the rendered pages on tipitaka.app or the WeBuddhist reader. Open each text in the reader to see the TOC tree.

## Files to commit

The three commentary `.md` files, their `.lint.json` files, the three commentary parser output folders and this report. Never `.env`.

## Related

- ID rules: `4-SYSTEM/Guidelines/block-id-spec.md`
- Source typos and shorthand: `4-SYSTEM/Guidelines/known-source-irregularities.md`
- Root-text audit pattern: `0-INBOX/pi-3-hierarchy-and-upload-report.md`
