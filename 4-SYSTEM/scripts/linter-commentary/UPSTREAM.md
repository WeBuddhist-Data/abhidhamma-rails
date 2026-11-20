# Upstream

| | |
|---|---|
| Generic version | https://github.com/WeBuddhist/rails-template, `4-SYSTEM/scripts/` at commit `b5e0c2e` (2026-11-19) |
| Common base | https://github.com/WeBuddhist/21-taras-rails, commit `9586df9` (2026-09-17), the copy both this vault and the template grew from |
| Merged | 2026-11-20, three-way (base → this vault, base → template) |

This vault's linter and parser are **not** byte-identical to the template's: they carry the
Abhidhamma specifics below. To take later template updates, merge again three-way with the
template's previous commit as the base (`b5e0c2e`), never copy the template files over these.
`durchen.py` is the template's, byte-identical (shared by the four tools).

## Abhidhamma specifics (kept)

- **Mātikā (matrix) IDs** (block-id-spec §6): a matrix zone `M`, `M1`, `M2` … (and the old Roman `MI`, `MII`) makes a block a verse (parser); the linter warns on matrix IDs still numbered in Roman.
- **Segment types**: a lowercase-letter part (`^1-a`, `^4-M-a`, `^a-1`) is back matter; a Roman part does not make front matter.
- **Headings below level 6** written `####### *Title* ^id`: the asterisks are display only (parser, with the template's `**Title**` rule).
- **Alignment**: back-to-back transclusion blocks form one group; transclusions of root headings are skipped with one warning (root-text parser: pending targets for the next block; commentary parser: a scope that stays open until the next transclusion or heading).
- **`<small>`** is dropped from the parsed copy (no yigchung for Pāli), and NBSP becomes a space.
- **Source field aliases**: `source_url`, `gretil_url`, `dsbc_url`, `suttacentral_id` are read as `source`; the linter renames `source_url` to `source`.
- **Parser input** `.lint.errors.json` accepted; output files named after the source file.
- **Pāli titles**: checked for Roman script only when the text's language is `pi`.
- **API base** `https://library.webuddhist.com` (template form kept; same address).

## Generic updates taken from the template

- Durchens `[^dN]` and footnotes `[^fN]` (`durchen.py`): linter checks, parser payloads (`durchens.json`, `footnotes.json`); note definitions are taken out before block IDs and alignment are read.
- Yigchung payloads for `<small>` runs (inert here: `<small>` is dropped first).
- A heading glued to text, a transclusion or another heading is a linter ERROR.
- Title and `alt_titles` language keys checked against the languages API.
- `tag_ids` checked more closely; not sent for a translation (it inherits the root's tags).
- Odd spaces and invisible characters reported; space-like characters normalised in the edition.
- A block of 2+ lines with no gap is typed `verse`.
- `translation_of` / `category_id` written back from `root_text` when missing.
