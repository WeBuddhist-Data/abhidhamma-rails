# Dhātukathā (`pi-3.md`) — structure, content, and upload readiness

**Date:** 2026-10-27  
**Text:** `1-SOURCES/Text/pi-3.md` (Dhātukathāpāḷi, Abhidhamma book 3)  
**Also reviewed:** tipitaka.app (`ap-dhk`), parser/linter under `4-SYSTEM/scripts/`, stored `output/pi-3/`, webuddhist.com API (metadata only)

This note is for someone opening the project cold. It records what was checked, what passed, what is intentional vs stale, and what to do before changing the live reader.

**No source file was edited for this report.** A fresh parser run was tried only in a scratch folder, not committed into `output/pi-3/`.

---

## What this file is

`pi-3.md` is the **root mūla** of the Dhātukathā. It is the canonical markdown in the vault. Everything else (parser JSON, WeBuddhist edition, rails) is derived from it or cites it.

Frontmatter already links the text to the platform:

- `text_id: Us3yilUt8Q4I8m3JuCOhk`
- `edition_id`, `toc_id` (see frontmatter in `pi-3.md`)

Ingest source: tipitaka.org CSCD `abh03m1.mul.xml`.

---

## How IDs work (two tracks)

Readers see **headings** (outline) and **segments** (numbered Pāli blocks). They use different ID shapes on purpose (`block-id-spec.md`):

| Track | Shape | Example | Meaning |
|--------|--------|---------|--------|
| **Heading** | ends in `-0` | `^3-1-0` | TOC node only (e.g. Uddeso) |
| **Content** | no trailing `-0` | `^3-1`, `^3-6` | One numbered segment in book 3 |

Book **3** = Dhātukathā. Content numbers **1…518** run through the whole book; they do **not** restart at each chapter. Headings use **sibling position** under the parent (`^3-2-0` = Paṭhamanayo as the second major section), which can differ from tipitaka.app’s printed “1.” on the first naya — that offset is **by design**.

---

## Result: structure and content

**Verdict: `pi-3.md` passes.** No hierarchy fix is required for this file.

### Outline (parent / child / siblings)

- **59 headings**, markdown levels `#` through `#####`, each with a `-0` anchor.
- Every child is **one heading level** below its parent; each child ID **extends** the parent prefix (e.g. `^3-2-0` → `^3-2-1-0` → `^3-2-1-1-0`).
- Siblings are numbered **1…n** without gaps. Repeated titles (e.g. several `Tikaṃ` / `Dukaṃ` sections) live under **different** parents, so IDs stay unique.
- **`pi-3.toc.json`** (59 nodes) matches the markdown titles and depth.

### Body (segments)

- Verse references **`^3-1` through `^3-518`**: contiguous, no resets, no gaps, no spurious `x` / `U` IDs on this book.
- **95 continuation lines** (e.g. `(Ekamūlakaṃ.)`, `…pe…`) have **no** separate ID; they belong to the segment whose `^` appears on a later line in the same block.
- **tipitaka.app:** 57 TOC entries under the book match ours in **title and order** (Uddeso + 5 mātikās, 14 nayas with title nodes, 23 sub-sections). The site counts **673** paragraphs; our file counts as **578 block IDs + 95 continuation lines = 673**. All **37 leaf sections** match the site’s paragraph spans.

### Intentional differences from the website display

- **Section numbering:** Uddeso is `^3-1-0`; Paṭhamanayo is `^3-2-0` while the site labels Paṭhamanayo as “1.”
- **Paragraph splits:** Some site lines (e.g. centred labels) appear as **continuations** inside one segment in markdown (e.g. `(Ekamūlakaṃ.)` with `^3-10`). Same Pāli; different visual paragraph count inside a segment.

---

## Commentaries (sanity check, not root structure)

Three Dhātukathā commentary files transclude root blocks with `![[1-SOURCES/Text/pi-3.md#^…]]`:

- **106 links** total (54 aṭṭhakathā, 26 mūlaṭīkā, 26 anuṭīkā); all resolve and sit under the correct naya.
- Commentary **file IDs are separate** from root IDs (e.g. `^3-2-1-0` in the aṭṭhakathā is not the same node as in `pi-3.md`). Always cite with full path.
- Markers are **span-based:** text after `![[…#^3-N]]` applies until the next marker or end of that naya. Last root marker **`^3-456`** covers root **`^3-456`–`^3-518`**. Aṭṭhakathā for that tail uses its own blocks **`^3-100`–`^3-105`** (not root IDs); book end commentary also has **Nigamanakathā** `^3-3-0` with `^3-106`–`^3-111`.

**⚑ Specialist review:** Aṭṭhakathā gāthā `^3-101`–`^3-103` differs in wording from the root closing gāthā at `pi-3.md` ~1265, while `^3-104` treats the gāthā as explaining that meaning. Record both; do not flatten without a Pāli reviewer.

---

## Headings with no text under them

Many nodes are **titles only** (e.g. `^3-1-0` Uddeso): the Pāli starts in **child** headings (`^3-1-1-0` Nayamātikā → `^3-1`). That is normal.

**Current `parser.py` behaviour:**

- Headings are **TOC-only**: they are **not** copied into edition `content` and do **not** become segments.
- Each TOC section spans from that heading’s offset to the next heading of the **same or higher** level (or end of file). A heading with no body of its own **inherits** the span of its first descendant content.
- A heading immediately followed by a same-or-higher-level heading may get an **empty span** (allowed by the backend). **Stored `pi-3` TOC has no empty spans.**

**Fresh parser note:** With headings excluded from content, several nested TOC entries can share the **same start offset** (e.g. after homage `^T-1`, content begins at character 46). How the reader displays stacked titles at one offset was **not** verified in the UI.

Backend validation on a freshly built TOC: nested spans, non-overlapping siblings, unique segment references, contiguous lines — **passed**.

---

## WeBuddhist reader (pattern vs this text)

The reader pattern is: **nested TOC** + **segment labels** from edition references (e.g. `3-6` for Khandho’s first paragraph). Dhātukathā uses **`text_id` `Us3yilUt8Q4I8m3JuCOhk`**, not other example texts on the site.

Compared to a simple two-level translation (e.g. Diamond Cutter sūtra in docs): Dhātukathā has **deeper TOC** (four levels under the book), **Pali mūla**, and a **homage line** (`^T-1`) before the book body. Same UI idea; different depth and labels.

---

## Important: stored parser output and live edition are stale

On disk, `4-SYSTEM/scripts/parser-root-text/output/pi-3/` and the **live edition** tied to `edition_id` in frontmatter were built with an **older parser** that treated headings differently from **today’s** `parser.py`:

| | Stored / live (old parser) | Current `parser.py` (fresh run) |
|---|---|---|
| Segment count | 578 (518 verse + **59 `title`** + 1 top) | **519** (518 verse + 1 top) |
| Heading text inside edition `content` | Yes | **No** |
| Character length | 147,005 | 146,102 |
| First TOC span (Abhidhammapiṭake) | 62–147,005 | 46–146,102 |
| Heading-type segments | Yes (e.g. `3-1-0`) | **None** |

**TOC titles and depth are the same** in both runs; only spans and segment typing change. Re-uploading without re-parsing would keep old behaviour; re-parse + update edition/TOC aligns the site with current rules.

Live **`pi-3` reader layout** (e.g. duplicate titles in the flow) was **not** confirmed in the browser during this audit.

---

## Recommended follow-up (only if you touch upload or rails)

1. Re-run **linter** and **parser** on `pi-3.md`; review new `pi-3.edition.json` and `pi-3.toc.json` under `4-SYSTEM/scripts/*/output/`.
2. **Update** the platform edition and TOC from that output; open Dhātukathā in the reader and check stacked headings.
3. Before rails for **`^3-457`–`^3-518`**, resolve the commentary gāthā ⚑ with a domain specialist.

---

## Related

- Shorter verification log (if present): `0-INBOX/pi-3-structural-audit.md`
- ID rules: `4-SYSTEM/Guidelines/block-id-spec.md`
- Parser behaviour: `4-SYSTEM/scripts/parser-root-text/README.md` and `parser.py`
