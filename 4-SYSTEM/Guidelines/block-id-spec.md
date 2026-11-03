# Block-ID Specification

Canonical reference for block-ID (`^anchor`) construction across this vault.

**Status:** authoritative. Where this file and any other document disagree about ID construction, **this file wins** — including `abhidhamma-annex.md` §2, whose scheme it supersedes (see §9).

**Audience:** anyone writing a skill, converter, or parser that emits or reads `^ids` — in this repo *or in a sibling repo sharing the same address space*. §4 is the reserved-character registry; read it before introducing any new marker.

---

## 1. Why a shared spec

Block IDs are a **shared, permanent address space**. Once a rail, translation, or commentary cites `^1-585`, that address must keep meaning the same thing forever, and no other tool may mint a colliding one.

Two failure modes this spec exists to prevent:

1. **Collision** — two different blocks resolving to the same ID.
2. **Semantic drift** — a marker meaning "unnumbered" in one skill and "matrix" in another.

---

## 2. Grammar

```
id          := "^" ( collection | top | body )

collection  := "0"                                  # the piṭaka root
top         := "T-" INT                             # pre-title prose
body        := BOOK "-" [ ZONE "-" ] LEAF           # content
             | BOOK "-" PATH "-0"                   # heading

BOOK        := 1..7
ZONE        := arabic | "M" roman | reserved        # see §4
LEAF        := INT | INT "x" INT | "U" INT
PATH        := segment ( "-" segment )*
```

Concrete shapes:

| Kind | Shape | Example |
|---|---|---|
| Piṭaka root | `^0` | `^0` |
| Pre-title prose | `^T-{n}` | `^T-1` |
| Book heading | `^{book}-0` | `^1-0` |
| Deeper heading | `^{book}-{path}-0` | `^1-2-3-0`, `^1-M-II-XIV-0` (root text); `^1-I-II-0` (commentary — §11a) |
| Content, principal run | `^{book}-{N}` | `^1-585` |
| Content, zoned run | `^{book}-{zone}-{N}` | `^1-MII-142` |
| Content, unnumbered | `^{book}-U{k}` | `^1-U1` |
| Content, repeated `N` | `^{book}-{N}x{k}` | `^1-5x1` |

---

## 3. The three positions

### Position 1 — `book`

Integer `1`–`7`, the Abhidhammapiṭaka order. **Reserved permanently**; never reuse for anything else.

| `book` | Treatise | | `book` | Treatise |
|---|---|---|---|---|
| `1` | Dhammasaṅgaṇī | | `5` | Kathāvatthu |
| `2` | Vibhaṅga | | `6` | Yamaka |
| `3` | Dhātukathā | | `7` | Paṭṭhāna |
| `4` | Puggalapaññatti | | | |

### Position 2 — `zone` (optional)

A **collision-breaker only.** It exists solely so two blocks carrying the same printed `N` do not collide inside one book.

It is **not** a genre label, **not** a position label, and carries no claim that content is "matrix", "intro", "front matter" or "body". Attaching meaning to this segment is the single most repeated design error in this vault's history — see §8.

- One numbering run in the book → **omit** the zone entirely.
- Several runs → the **principal** run (normally the body: longest, most-cited) keeps the bare namespace; every other run takes the next label per §4.

### Position 3 — `N` (the leaf)

**Always the source's own printed number, copied verbatim.** Never recomputed, never renumbered, never invented, never zero-padded.

If the source skips a number, the ID sequence skips it too (book 2 legitimately has no `^2-185`, `^2-252`, `^2-264`, `^2-298`). If the source repeats one, see `x` in §4.

---

## 4. Reserved character registry

**Check this table before inventing any marker.** Everything listed is claimed; treat unlisted letters as available but register them here when used.

| Token | Position | Means | Example |
|---|---|---|---|
| `0` | whole ID | Piṭaka/collection root | `^0` |
| `-0` | **suffix** | This ID is a **heading**, never content | `^1-2-0` |
| `T` | zone (after `^`) | **T**op — prose before the first `#` (homage) | `^T-1` |
| `1`–`7` | book | Abhidhamma book number | `^3-…` |
| `U` | leaf | **U**nnumbered — block has no printed number | `^1-U1` |
| `x` | leaf infix | Duplicate printed `N`; 1st bare, later `x1`, `x2` | `^1-5x1` |
| `M` | zone | **M**ātikā that opens the book's first counter (root-text books only) | `^1-M-0`, `^1-MI-1` |
| Roman | path | Sibling index **inside a designated front-matter subtree only** — root-text books: inside an `M` subtree (§6). Commentary files (`1-SOURCES/Commentaries/`): inside the single, manually-named `--frontmatter` heading's subtree, if any (§11a) | `^1-M-II-0` (root text); `^1-I-II-0` (commentary front matter) |
| Arabic | zone/path/leaf | Default for all headings outside a front-matter subtree (both root-text and commentary); sequential run label; every commentary content leaf (`N`), always, front matter or not | `^1-2-0` (ordinary heading, either file type); `^1-142` (commentary content) |
| `D`,`T`*,`A`,`P` | zone | **Reserved, book 7 only** — see §7 | `^7-D7T1-…` |

\* `T` is overloaded: `^T-{n}` at the *start* of an ID means top-matter; `T` inside a book-7 zone means *tika*. They never occupy the same position, so no ambiguity arises — but do not introduce a third meaning.

### Deliberate reuse of `U`

`U` appears in two places with the *same* underlying meaning ("no printed number here"), distinguished by segment count:

- `^1-U1` — 2 segments — an unnumbered **content block**.
- `^1-U1-5` — 3 segments — hypothetical unnumbered **zone**, number 5.

This is intentional, not a collision. Do not assign `U` a second meaning.

---

## 5. Headings vs content

Two **independent tracks**. Do not make one mirror the other.

|  | Heading | Content |
|---|---|---|
| Terminator | always ends `-0` | never ends `-0` |
| Depth | unlimited (4, 5, 6+ segments fine) | **maximum 3 segments** |
| Numbering | sibling position under its parent | verbatim printed `N` |

Because the tracks are independent, the same digits may appear in both meaning different things — e.g. Dukamātikā's **content** is `^1-MII-{N}` while its **heading** is `^1-M-II-0`. No literal collision is possible, since content never ends in `-0`.

**Headings use sibling position even when the source prints a number on them.** Book 2 has ~170 headings like `##### (25. Ka) arati`; those printed numbers collide with each other and desync where lettered sub-headings intervene. Verbatim-number preservation (§3) is a **content-ID rule only**.

The `###` counter runs continuously across *all* `###` siblings in a book. There is no separate counter for "front" and "body" sections.

**The `M`/front-matter exception exists in both file types, with the same shape.** Root-text books render heading sibling position in Arabic, except inside an `M` subtree (§6) — a mātikā that opens the book's first counter, Roman inside that subtree only. Commentary files render heading sibling position in Arabic too, except inside a single, manually-named front-matter subtree (§11a) — Roman inside that subtree only, everywhere else Arabic. Content stays Arabic in both file types, always. Neither file type uses Roman as its default — it is always the narrow exception for a genuinely separate opening section, never the baseline.

---

## 6. The `M` zone

The one place a zone carries meaning. When a **mātikā/matrix section opens the book's first numbering run** — it precedes the body and owns its own counter(s) — it is genuinely introductory and takes `M`:

| Track | Shape | Book 1 |
|---|---|---|
| Matrix parent heading | `^{book}-M-0` | `### Mātikā ^1-M-0` |
| Child headings | `^{book}-M-{Roman}-0` | `^1-M-I-0`, `^1-M-II-0` |
| Deeper headings | Roman throughout | `^1-M-II-I-0` … `^1-M-II-XIV-0` |
| Content | `^{book}-M{Roman}-{N}` | `^1-MI-1`…`^1-MI-22`, `^1-MII-1`…`^1-MII-142` |

Heading and content share the same Roman label (`^1-M-I-0` ↔ `^1-MI-{N}`); content merely fuses `M`+Roman into one token to respect the 3-segment cap.

Body `###` numbering starts at `1` *after* the `M` section, since `M` occupies its own slot.

### The test is counter behaviour, not the word "mātikā"

Matrices are **common and recurring**, not once-per-book. Observed:

| Book | Matrices | Gets `M`? |
|---|---|---|
| 1 | opening `### Mātikā`; **plus** a second `#### Mātikā` mid-body in Rūpakaṇḍaṃ | only the opening one |
| 2 | 23 mātikā headings, **none at the front**; 14 `Pañhāpucchakaṃ` | **no** — nothing opens a counter |
| 3 | five inside `Uddesa` (Naya-, Abbhantara-, Nayamukha-, Lakkhaṇa-, Bāhira-) | **no** — numbering flows into the body |

A matrix qualifies **only** if it opens the book's numbering. Every other matrix is ordinary content under ordinary zones.

---

## 7. Reserved for book 7 (Paṭṭhāna) — provisional

**Not implemented.** `pi-7.md` does not exist yet; this reserves the namespace so nothing else claims these letters. Do not apply to books 1–6.

Paṭṭhāna has hundreds of resets and its own compound cross-reference numbering, so plain sequential zones may not suffice:

| Layer | Zone | Example |
|---|---|---|
| Tika *n* | `T{n}` | `^7-T2-1` |
| Duka *n* (flat 1–100) | `D{n}` | `^7-D7-…` |
| Duka×tika, duka-led | `D{d}T{t}` | `^7-D7T1-…` |
| Tika×duka, tika-led | `T{t}D{d}` | `^7-T1D99-…` |
| Mode × pairing | `{A\|P\|AP\|PA}{T\|D\|TT\|DD\|DT\|TD}` | `^7-PDT-…` |

Known unresolved: Kusalattikaṃ's counter never resets (starts at `53`), so its zone boundary is a manual decision no reset-detector can find; the flat duka numbers are only partly known; the 20 mode×pairing sections likely nest further and may not fit 3 segments.

---

## 8. Invariants

1. `N` is verbatim from the source. Never recomputed.
2. Content IDs ≤ 3 segments. Headings unbounded.
3. `-0` suffix ⇒ heading. No exceptions.
4. Every heading gets an ID.
5. Zones are collision-breakers, not genre labels (sole exception: `M`, §6).
6. Every content block gets exactly one ID, on its **last** line; strip the `N.` prefix from the rendered text.
7. Never assign IDs to `![[...]]` transclusions.
8. YAML front-matter delimiters are never tagged.
9. IDs are permanent once published downstream.

---

## 9. Supersedes `abhidhamma-annex.md` §2

That section documents the pre-2026-08 scheme. Where they differ, **this spec wins**. Differences:

| Item | Annex (superseded) | This spec |
|---|---|---|
| Piṭaka root | `^abhidhamma-0` | `^0` |
| Homage line | no anchor | `^T-1` |
| Mātikā sub-headings | `^1-0a-0`, `^1-0b-0` | `^1-M-I-0`, `^1-M-II-0` |
| Mātikā content | `^1-0a-1`, `^1-0b-1` | `^1-MI-1`, `^1-MII-1` |
| Unnumbered block | no verse-level ID | `^{book}-U{k}` |
| Mātikā counter | "internal counter" | source's printed `N`, verbatim |

Agreements worth noting: the body is one continuous counter that does not reset at heading boundaries; gocchakas under Dukamātikā continue its count rather than restarting; a verse may span headings, with its ID on the final line.

Files already carrying superseded IDs (e.g. untouched `1-SOURCES/Text/*.md` sources) are re-derived on the next skill run — `apply.py` strips all pre-existing `^ids` before assigning, so re-running is always safe.

---

## 10. Implementing skills

- `4-SYSTEM/Skills/add-block-id-root-text/` — Pali Abhidhamma root-text books (prose/mātikā-kaṇḍa; formerly named `add-block-id-pali-matika`). `SKILL.md` + `apply.py` (audit / apply).
- `4-SYSTEM/Skills/add-block-id-commentary/` — Pali Aṭṭhakathā/Ṭīkā commentary files. `SKILL.md` + `apply.py` (content IDs fully automatic — §11; heading IDs Arabic by default, with an optional `--frontmatter` flag for a Roman front-matter subtree — §11a).
- `4-SYSTEM/Skills/format-root-text/` — note: its `^chapter-verse` / `^0-verse` convention is **generic** and predates this spec; for Abhidhamma sources this spec governs.

New skills touching `^ids` must register any new marker in §4 before use.

---

## 11. Commentary content IDs — an exception to §3 Position 3

Commentary/sub-commentary files in `1-SOURCES/Commentaries/` (Aṭṭhasālinī, Mūlaṭīkā, Anuṭīkā, and further tiers) carry no reliable per-paragraph counter of their own to preserve verbatim:

- Most commentary prose is unnumbered outright.
- Where a Ṭīkā paragraph does start with a printed digit, that digit is a **citation back to the root-text verse being glossed** (e.g. Mūlaṭīkā paragraph `"3. Tatthāpi …"` glosses root verse 3), not a running paragraph count. It does not increment sequentially and is left untouched in the rendered text — it is not a source-N to extract.

Content IDs for these files are therefore a single **internal, continuous, document-order counter**, `^{book}-{N}`, one unbroken run for the whole file — never reset by a heading, never derived from a printed digit. This is the one place in the vault where §3 Position 3 ("`N` always the source's own printed number, copied verbatim") does not hold; `N` here is assigned by the skill, not read off the page.

Everything else is unchanged from the root-text scheme: `book` is the Abhidhammapiṭaka position (1–7) of the text being commented on, taken from the commentary's own `root_text:` frontmatter; headings use the same sibling-position *hierarchy* (§5), Arabic by default with an optional Roman front-matter subtree (see §11a); pre-title prose is `^T-{n}`; transclusions and frontmatter are never tagged (§8 invariants #7–#8).

Because IDs always resolve as `file#^id`, a commentary's `^{book}-{N}` does not collide with the root text's own `^{book}-{N}` in a different file — the digits mean "the Nth content block of *this* file," scoped per file, same as the root text's own counter is scoped to `1-SOURCES/Text/`. Each commentary tier (aṭṭhakathā, mūlaṭīkā, anuṭīkā, …) on the same book keeps its own independent counter in its own file.

See `4-SYSTEM/Skills/add-block-id-commentary/SKILL.md` for the workflow. Its `apply.py` assigns content IDs and (by default) heading IDs fully automatically, with no run/zone ambiguity or printed-number verification step to resolve (unlike `add-block-id-root-text`'s content-run `--zones`). The one manual decision is the same kind root-text's `M`-zone requires: whether to pass `--frontmatter "<heading text>"` naming a genuinely separate opening section (§11a) — omitted by default, and never inferred automatically.

---

## 11a. Commentary front-matter heading IDs — a commentary-side `M`-zone

Commentary headings are **Arabic by default** — same sibling-position logic as root-text headings (§5), same numeral system. The one exception: a single, manually-identified front-matter heading and its whole descendant subtree may use **Roman** numerals instead, in their own counter namespace, mirroring root-text's `M`-zone (§6) exactly:

```
### Sumedhakathāvaṇṇanā          ^1-I-0      front matter — 1st Roman sibling in its own namespace
#### Vīsatigāthāvaṇṇanā          ^1-I-I-0    front matter — nested under it
#### Nidānakathāvaṇṇanā          ^1-I-II-0   front matter — nested under it
### Cittuppādakaṇḍaṃ              ^1-1-0      body — 1st Arabic sibling; the front-matter subtree
                                              did NOT consume a slot in this counter
### Tikamātikāpadavaṇṇanā         ^1-2-0      body — 2nd Arabic sibling
```

This is opt-in, not automatic: `4-SYSTEM/Skills/add-block-id-commentary/apply.py` takes an optional `--frontmatter "<exact heading text>"` argument naming the one heading that opens the front-matter subtree. Everything nested under that heading (at any depth) gets Roman sibling IDs in a counter namespace independent of the body's Arabic one; the body's own `###` counter then starts fresh at `1` after the front-matter subtree, exactly as root-text's body numbering starts at `1` after its `M` section (§6). Omit the flag and the file gets no front matter at all — every heading is Arabic, matching root-text's own default when there is no `M`.

**Deciding whether a section qualifies is the same judgment call as `M`-zone detection, not a text-pattern match.** Per §6's own framing: *"the test is counter behaviour, not the word 'mātikā'."* The commentary analogue: the test is whether a section genuinely precedes and stands structurally apart from the substantive commentary — not whether it happens to read as introductory. A section that merely discusses background material *within* the ongoing exposition does not qualify, the same way book 1's mid-body `#### Mātikā` inside Rūpakaṇḍaṃ does not get `M` treatment (§6) even though the word is right there in its title.

This is deliberately narrower than an earlier draft of this section, which applied Roman numerals to *every* heading unconditionally. That version reasoned it avoided the genre-classification problem because it wasn't selective — but it was replaced because unconditional Roman numerals still visually read as "this file's headings are all front matter," which is not the intended signal and caused confusion. The current design is selective on purpose, exactly as narrow as `M`-zone is for root text: Roman numerals mark *only* a genuinely separate front-matter subtree, nothing else, and the default for every other heading is the same plain Arabic sibling numbering root-text uses outside its own `M` subtree.

Content-block IDs (`^{book}-{N}`, §11) are unaffected either way — always the plain continuous Arabic counter, whether the content sits inside or outside a front-matter subtree. `book`, `T-{n}` pre-title IDs, and transclusion/frontmatter exclusions are all unchanged.

`4-SYSTEM/Skills/add-block-id-commentary/apply.py`'s `to_roman()` helper renders the Roman path segments; `_next_sibling()` tracks two independent counter namespaces (Arabic and Roman) and switches between them based on whether the current heading is inside the named front-matter subtree.
