# Abhidhamma Annex — vault-specific conventions

The methodology guidelines (`0-VAULT-Structure.md`, `../../1-SOURCES/About Sources.md`, `../../2-RAILS/About Rails.md`, `../../3-TRANSFORMATIONS/About Transformations.md`) are **text-agnostic** — they apply to any Railroads vault built on any classical text. This annex records the conventions that are specific to *this* vault: the Pāli Abhidhamma Piṭaka.

When the Guidelines and this annex disagree on a vault-specific detail, this annex wins.

---

## 1. The text

This vault serves the **Pāli Abhidhamma Piṭaka** — the third basket of the Pāli Canon. Source-text files in `1-SOURCES/Text/` correspond to the seven canonical books:

| Order | Book | Filename |
| ----- | -------------------- | ------------------------- |
| 1 | Dhammasaṅgaṇī | `pi-dhammasangani.md` |
| 2 | Vibhaṅga | `pi-vibhanga.md` |
| 3 | Dhātukathā | `pi-dhatukatha.md` |
| 4 | Puggalapaññatti | `pi-puggalapannatti.md` |
| 5 | Kathāvatthu | `pi-kathavatthu.md` |
| 6 | Yamaka | `pi-yamaka.md` |
| 7 | Paṭṭhāna | `pi-patthana.md` |

Only books that have been ingested are present in the folder. The Dhammasaṅgaṇī (book 1) is the primary text currently rails-out.

---

## 2. Bible-style addressing for Pāli canonical texts

> [!warning] Superseded in part
> The **block-ID construction rules** in this section (piṭaka anchor `^abhidhamma-0`, the `^1-0a-…` / `^1-0b-…` Mātikā sub-namespaces, and the "unlabelled sections get no verse ID" rule) are **superseded by [`block-id-spec.md`](block-id-spec.md)**, which is authoritative for all `^id` construction. See its §9 for a difference table.
>
> The conceptual material below — the Bible analogy, the single continuous verse counter, verse grouping, and verses spanning headings — remains accurate.

Pāli canonical texts in this vault use a Bible-inspired addressing scheme. This convention **overrides** the generic `^chapter-verse` rule in `../../1-SOURCES/About Sources.md` §4 for these texts.

### The analogy

| Bible | Tipiṭaka |
| --------------------------- | -------------------------------------------------------------- |
| The Bible (whole canon) | The Tipiṭaka |
| Book (Genesis, Matthew, …) | Piṭaka (Vinaya, Sutta, Abhidhamma) |
| Chapter (Genesis 1) | A canonical book within a piṭaka (Dhammasaṅgaṇī, Vibhaṅga, …) |
| Verse (Genesis 1:1) | A verse running continuously through the book |

### Heading hierarchy and anchors

| Markdown | Role | Anchor |
| ------------------------- | --------------------------------- | ----------------------------------------------------------------------- |
| (plain text, no heading) | Homage line (`Namo tassa…`) | — |
| `# <piṭaka>` | The piṭaka | `^<pitaka-slug>-0` (e.g. `^abhidhamma-0`) |
| `## <book>` | The canonical book | `^<book>-0` (book = position within piṭaka; `1` for Dhammasaṅgaṇī) |
| `### <title>` | Major book-internal section | `^<book>-<h3>-0` |
| `#### <title>` | Sub-section | `^<book>-<h3>-<h4>-0` (Mātikā exception below) |
| `##### <title>` | Deeper sub-section | `^<book>-<h3>-<h4>-<h5>-0` (Mātikā exception below) |

### Verse IDs — single continuous counter, with a Mātikā exception

The book has a **single, continuous verse counter** that runs through every section. Verses are `^<book>-V`, e.g. `^1-1`, `^1-2`, …, `^1-1616`. The counter does NOT reset at h3, h4 or h5 boundaries — the Cittuppādakaṇḍaṃ's last verse is followed immediately by Rūpakaṇḍaṃ's first verse with the next number. The counter value `V` is the source's own leading verse number (the `N.` prefix), so source-N and block-ID stay aligned.

The Mātikā / table-of-contents section (the source's first chapter) is the exception. Its h4 sub-sections (Tikamātikā, Dukamātikā, …) get **letter-suffixed sub-namespaces**:

- The h4 sub-sections of Mātikā are labelled `a`, `b`, `c`, … in document order.
- Verses in each get a 3-component ID: `^<book>-0<letter>-V`, e.g. `^1-0a-1` (Tikamātikā verse 1), `^1-0b-1` (Dukamātikā verse 1).
- `V` restarts at 1 for each h4, but does NOT restart at h5 boundaries (gocchakas under Dukamātikā continue Dukamātikā's verse count: Hetugocchakaṃ ends at `^1-0b-6`, Cūḷantaradukaṃ picks up at `^1-0b-7`).
- The Mātikā uses an internal counter (rather than the source's `N.` prefix) because the source itself restarts numbering across its TOC sub-sections.

Set `verse_id_format: book-verse` in the source-file frontmatter.

### Verse grouping rule

A body line that starts with `<digit>+. ` (e.g. `1.`, `583.`) opens a new verse and supplies its block-ID number. Subsequent body lines without a leading number — typically `(Ka)` / `(Kha)` / `(Ga)` triplet markers, intra-section intros like `Tividhena rūpasaṅgaho –`, or trailing summary words like `Hetugocchakaṃ.` — are merged into the current verse as additional lines, and the block ID goes on the verse's final line.

### Verses spanning subsections and headings

A single source verse can span multiple `####`/`#####` subsection headings — the headings are emitted at their structural position (with their own `^<book>-<h3>-<h4>(-<h5>)-0` anchor) but do NOT restart, advance, or otherwise affect the verse counter. The verse's block ID lands on the last continuation line, which may sit after one or more intervening headings.

Worked example — `^1-585` in Dhammasaṅgaṇī:

```markdown
##### Tikaṃ ^1-2-2-3-0

Tividhena rūpasaṅgaho –
585. Yaṃ taṃ rūpaṃ ajjhattikaṃ, taṃ upādā …
[many continuation lines]
Evaṃ tividhena rūpasaṅgaho.
Tikaṃ. ^1-585
```

The intro line `Tividhena rūpasaṅgaho –` appears before the numbered opening; the closing `Evaṃ … rūpasaṅgaho.` / `Tikaṃ.` appears after the body lines. Both are part of source verse 585 and share its block ID, which is placed once on the final line.

### Unlabelled sections

When the source itself leaves a sub-section unnumbered (no `N.` anywhere in the section, e.g. the `##### Dukaṃ` block inside the Rūpakaṇḍaṃ matrix), the section's body is emitted as a single block WITHOUT a verse-level block ID — only the structural heading `##### Dukaṃ ^1-2-2-2-0` is addressable. This preserves the invariant that every `^<book>-V` corresponds to a real source-N.

### Sub-verse citations

When downstream content (rails, transformations) cites a sub-portion of a verse, use Bible-style letter suffixes (`^1-1a`, `^1-1b` for lines a, b of verse 1). **These are not generated in `1-SOURCES/`** — the source file gives each verse one ID; sub-verse addressing is added at citation time in `2-RAILS/` and downstream.

### Conversion

Tipiṭaka book JSON exports from tipitaka.org are converted to this format by `4-SYSTEM/Skills/json-to-source-text/converters/tipitaka_org_book.py`. See that skill's `SKILL.md` for the full workflow.

---

## 3. Registered commentary IDs

Every commentary file in `1-SOURCES/Commentaries/` declares a `registered_id` in its frontmatter. That short ID is the only string used to attribute claims to the commentary throughout `2-RAILS/` (in `commentary_coverage:` fields, in Traditional Interpretation section headers, in citation paths).

Once assigned, a `registered_id` never changes. New commentaries must be added to the roster below before their `registered_id` is used in any rail.

| `registered_id` | Title | Tier | Language | File |
| ---------------------------- | ------------------------------ | ----------- | -------- | ------------------------------------------------------------------- |
| `dhammasangani-atthakatha` | Aṭṭhasālinī | commentary | Pāli | `1-SOURCES/Commentaries/pi-dhammasangani-atthakatha.md` |
| `dhammasangani-mulatiika` | Mūlaṭīkā on the Aṭṭhasālinī | sub-comm. | Pāli | `1-SOURCES/Commentaries/pi-dhammasangani-mulatiika.md` |
| `dhammasangani-anutiika` | Anuṭīkā on the Aṭṭhasālinī | sub-sub-c. | Pāli | `1-SOURCES/Commentaries/pi-dhammasangani-anutiika.md` |

Tier labels: **commentary** (aṭṭhakathā), **sub-commentary** (mūlaṭīkā), **sub-sub-commentary** (anuṭīkā). The tier ordering guides Traditional Interpretation section order within a verse package: aṭṭhakathā first, then mūlaṭīkā, then anuṭīkā.

When a new commentary is ingested, add a row here, declare the same ID in the source file's `registered_id` frontmatter, and include it in the commentary roster of any new verse package that covers verses it commentates on.

---

## 4. Language tracks

The vault publishes outputs across multiple target languages. Each track has both a translation in `3-TRANSFORMATIONS/Translations/` and (where applicable) a Daily-Tipitaka language stream in `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/days/`.

| Tag | Language | Translation track | Daily-Tipitaka stream |
| ---- | ----------------- | -------------------------------------------------- | --------------------- |
| `pi` | Pāli (source) | — | `days/pi/` |
| `en` | English | `en-Contemporary-English-Abhidhamma/` | `days/en/` |
| `bn` | Bengali | `bn-Contemporary-Bengali-Abhidhamma/` | — |
| `si` | Sinhala (modern) | `si-Contemporary-Sinhala-Abhidhamma/` | — |
| `bo` | Tibetan | — | `days/bo/` |
| `zh` | Chinese | — | `days/zh/` |
| `hi` | Hindi | — | `days/hi/` |

Each translation track's `requirements.md` is written in its own target language — the working language for its drafters and reviewers. New tracks are added by creating `Translation/<lang>-<descriptor>/requirements.md` plus a per-track `termbase.md` generated by the `glossary-select` skill from the consolidated `2-RAILS/Bilingual-Glossaries/pi-<lang>.md`.

The Contemporary-* translation series is modelled on the NIV's optimal-equivalence philosophy: faithful to the original meaning, accessible to a contemporary reader, reviewed by a committee.

---

## 5. Daily Tipitaka — vault-specific transformation track

The `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/` folder is a vault-specific transformation track prepared in collaboration with the **International Tipiṭaka Chanting Council (ITCC)** for the chanting gathering at Bodhgayā, December 2026. The track's brief, daily structure, plan organisation, and communications conventions live in that folder's own README and brief; this annex only notes that the track exists and that it relies on the rails like any other transformation.

---

## 6. Pāli language tags used in this vault

The vault uses the following Pāli tags (subset of the full ISO 639 / script taxonomy in `../../1-SOURCES/About Sources.md` §9):

| Tag | Script / System | Use in this vault |
| --------------- | ---------------------------------- | --------------------------------------------------- |
| `-pi` | Pāli romanisation (PTS standard) | All root texts and commentaries — **default** |
| `-pi-sinh` | Sinhala script | If a Sri Lankan witness edition is ingested |
| `-pi-mymr` | Myanmar script | If a Myanmar witness edition is ingested |
| `-pi-thai` | Thai script | If a Thai witness edition is ingested |
| `-pi-latn-cscd` | CSCD romanisation | If raw CSCD encoding is preserved before PTS normalisation |

The default for every Pāli source is `-pi`. Other tags appear only in `1-SOURCES/Text/` for script or encoding variants and are normalised before downstream skills consume them.

---

## 7. Where to look next

- [`0-VAULT-Structure.md`](0-VAULT-Structure.md) — the architecture in full.
- [`../../1-SOURCES/About Sources.md`](../../1-SOURCES/About Sources.md) — source-file rules (frontmatter, block IDs, language tags, per-type file format).
- [`../../2-RAILS/About Rails.md`](../../2-RAILS/About Rails.md) — rails schema and disambiguation stack.
- [`../../3-TRANSFORMATIONS/About Transformations.md`](../../3-TRANSFORMATIONS/About Transformations.md) — track and output rules.
- [Top-level `README.md`](README.md) — what rails are, why we build them, the translation workflow.
