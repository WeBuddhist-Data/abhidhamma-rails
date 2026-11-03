# Known source irregularities (CST / tipitaka.app print)

Printed citation labels in Pañcapakaraṇa commentaries sometimes disagree with the root block they gloss. **Do not edit the printed label in the markdown.** Transclusions follow the printed label exactly, as the source has it.

## pi-5 Kathāvatthu commentaries

| Printed label | File(s) | Transclusion targets | Note |
|---|---|---|---|
| `618-820.` | aṭṭhakathā `^5-544` | `^5-618` … `^5-820` (203) | linked as printed; the paragraph sits under Idaṃdukkhantikathā (root 618–620) |
| `541-545.` | aṭṭhakathā `^5-568` | `^5-541` … `^5-545` | linked as printed; the paragraph sits under Sattakkhattuparamakathā (root 641–645) |
| `706-608.` | anuṭīkā `^5-381` | `^5-608` … `^5-706` (99) | linked as printed, read low to high; the paragraph sits under Abyākatakathā (root 706–708) |
| `557-8.` | mūlaṭīkā `^5-270` | `^5-557`, `^5-558` | CST truncated-tail range, printed text expanded to `557-558.` |
| `571-2.` | mūlaṭīkā `^5-281` | `^5-571`, `^5-572` | CST truncated-tail range, printed text expanded to `571-572.` |

## pi-6 Yamaka root text

The source prints two stray paragraph numbers (tipitaka.app `ap-yam-2`), each between correctly numbered paragraphs. They get no block ID of their own; the line is kept as text at the end of the preceding block, as the source has it.

| Source paragraph | Stray number | Kept in block | Note |
|---|---|---|---|
| `ap-yam-2` para 373, "(Ṅa) paccanīkaokāso" (Saṅkhārayamaka), between 65 and 66 | `4` | `^6-6-65` | last line `4 (Ṅa) paccanīkaokāso`; elsewhere this label is a heading, here the source prints it as numbered body text |
| `ap-yam-2` para 2999, empty paragraph (Anusayayamaka), between 311 and 312 | `9` | `^6-7-311` | a bare `9` line at the end of the block |

Root `pi-5.md` uses a flat run `^5-1` … `^5-918` (no reset). pi-6 / pi-7 may use segmented root IDs; do not apply pi-5 truncated-tail rules there without checking for genuine B<A resets.
