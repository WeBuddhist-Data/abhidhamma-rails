---
title: Six irregular citations in the Abhidhamma commentaries
subtitle: What they should mean, and how that was established
scope: 1-SOURCES/Commentaries/pi-{3,4,5,6,7}-{atthakatha,mulatiika,anutiika}.md; pi-1 (pi-dhammasangani-*) and pi-2 (pi-vibhanga-*) added 2026-11-10
status: report
date: 2026-09-15
updated: 2026-11-10
---

# Six irregular citations in the Abhidhamma commentaries

Four paragraph numbers in the Chaṭṭha Saṅgāyana (CST/VRI) edition point somewhere their
own text contradicts, and two more follow conventions a parser has to be told about. Our
files reproduce all six exactly as printed. This is the record of what they should mean,
and how that was established.

| | |
|---|---|
| Citations checked | **1,786** — pi-3 to pi-7, all three commentary tiers |
| Differences from CST | **0** — the extraction is faithful |
| Numbers that misdirect | **4** — edition-level errors |
| Conventions to parse | **2** — not errors |

## Why this matters

Every commentary paragraph opens with a printed number naming the root paragraph it
discusses. That number is the only alignment the text itself asserts — it is what links
aṭṭhakathā, mūlaṭīkā and anuṭīkā back to the canonical text.

Where the number is wrong, an automated alignment silently attaches the paragraph to the
wrong passage. In one case below it would swallow two hundred root paragraphs at once.

> **Nothing in the source files has been altered.** All 1,786 citations are byte-identical
> to the tipitaka.org CST XML. The resolutions below belong in an exception list consulted
> at alignment time — never in the text.

## How each case was settled

A citation can be checked **without trusting any number**, because a commentary paragraph
almost always opens by quoting the words it is about. These four tests are ranked by how
much weight they carry.

1. **Lemma uniqueness.** Take the phrase the paragraph quotes and search the tier below.
   If it occurs exactly once, that is the parent — whatever number is printed.
2. **Meaning agreement.** Check that the gloss explains what the candidate passage actually
   says, in its own technical terms. Independent of the lemma, so it catches a phrase that
   recurs.
3. **Coverage.** Is the span already commented on elsewhere, or is there a hole where this
   paragraph would fit? A gap and a duplicate that match each other are strong evidence.
4. **Agreement between tiers — weakest, and actively misleading.** Two tiers printing the
   same number means nothing until you have confirmed they discuss the same passage.
   Case 4 below was first recorded backwards for exactly this reason.

---

## The four misdirecting numbers

### 1. A backwards range

`pi-kathavatthu-anutiika.md` · line 1098 · *Abyākatakathāvaṇṇanā*

**Printed `706-608.` — should resolve to 706–708.**

**Lemma.** The paragraph glosses a single word, *sabbathāpi*, which occurs **exactly once**
in the entire Kathāvatthu mūlaṭīkā — in its `706-708.` paragraph. There is no second
candidate.

```
mūlaṭīkā  706-708.  …tasmā sabbathāpi diṭṭhigataṃ "abyākata"nti na vattabbanti yuttaṃ.
anuṭīkā   706-608.  Sabbathāpīti avipākabhāvenapi sassatādibhāvenapi.
```

**Meaning.** The gloss unpacks *sabbathāpi* as *avipākabhāvenapi sassatādibhāvenapi* —
verbatim the two senses of *abyākata* the aṭṭhakathā develops at 706–708:

1. `…catubbidhaṃ abyākataṃ **avipākattā** abyākatanti vuttaṃ`
2. `Diṭṭhigataṃ "sassato loko…" **sassatādibhāvena** akathitattā`

Root 608 is *Na vattabbaṃ – "anusayā ahetukā"ti?* — the latent tendencies being rootless.
Unrelated to *abyākata* in either sense.

**Structure.** Kathāvatthu's root index runs flat 1–918 with no resets, so 608 cannot
follow 706 as a numbering epoch. The mūlaṭīkā has no paragraph anywhere near 608 to gloss
(its citations there run 598-600, 603-604, 614-615, 618-620).

**Tiers.** The aṭṭhakathā and mūlaṭīkā both print `706-708` for this same passage — the
edition contradicts itself across its own three tiers.

*Reading `608-706` as a transposed span is ruled out: it would cover ~98 root paragraphs
across eight kathās for a one-sentence gloss of one word, and would overlap the preceding
citation `703-705`.*

### 2. A range end two hundred paragraphs too far

`pi-kathavatthu-atthakatha.md` · line 1479 · *Idaṃ dukkhantikathāvaṇṇanā*

**Printed `618-820.` — should resolve to 618–620.**

**Lemma.** The paragraph quotes three phrases and walks them in order. Each is unique to
one root paragraph, and they stop at 620.

| quoted in the aṭṭhakathā | unique to root |
|---|---|
| `"ayaṃ dukkhasamudayo"ti vācaṃ bhāsato` (as *samudayādipañhesu paṭikkhipati*) | 618 |
| `Rūpaṃ aniccantiādi` | 619 |
| `Iti ca danti cātiādi … i-kāra daṃ-kāra du-kāra kha-kāresu` | 620 |

**Meaning.** It opens *Idāni idaṃ dukkhantikathā nāma hoti*, naming its own section; root
620 closes with the colophon *Idaṃ dukkhantikathā niṭṭhitā.* Root 820 is the
*jhānantarika* debate — and the paragraph contains no *jhāna*, *samādhi*, *vitakka* or
*vicāra* at all.

**Coverage.** Root 621–820 is **already tiled by 83 other aṭṭhakathā citations with zero
gaps**, including one that reads `820-822.` A literal span would comment on those two
hundred paragraphs twice.

**Tiers.** The mūlaṭīkā cites this passage as `618-620.`

### 3. A dropped leading digit

`pi-kathavatthu-atthakatha.md` · line 1547 · *Sattakkhattuparamakathāvaṇṇanā*

**Printed `541-545.` — should resolve to 641–645.**

**Lemma.** It quotes *"sattakkhattuparamo puggalo sattakkhattuparamatāya niyato"*, which
appears in root 641, 642, 643, 644 and 645 — the whole Sattakkhattuparamakathā — and
nowhere near 541. Its second lemma *ṭhapetvā ariyamaggaṃ añño tassa niyamo natthi* answers
root 642/643.

**Meaning.** It opens *Idāni sattakkhattuparamakathā nāma hoti*; root 645 closes
*Sattakkhattuparamakathā niṭṭhitā.* Root 541–545 is the Jīvitindriyakathā, on the life
faculty.

**Coverage — the decisive argument. A hole and a duplicate that fit each other:**

```
aṭṭhakathā   638-640  →  [ gap ]  →  646-647      641–645 has NO commentary
aṭṭhakathā   541.  542.  543.  544-545.           541–545 already fully commented
```

The aṭṭhakathā already covers 541–545 paragraph by paragraph with matching content
(`541.` *Rūpīnaṃ dhammānaṃ āyu arūpajīvitindriyanti pañhe…*, `542.`
*Nirodhasamāpannapañhesupi…*, `543.` *Asaññasattavārepi…*, `544-545.` *Ekadesaṃ
bhijjatīti pañhe…*). Reassigning to 641–645 fills the hole and removes the duplicate in
one move — the only assignment that makes the file's coverage consistent.

**Tiers.** Both ṭīkās cite this passage as `641-645.`

> Note the interaction with case 2: while `618-820` is read literally it spuriously
> "covers" 641–645 and hides this hole. Resolve case 2 first.

### 4. A transposition that looked legitimate

`pi-patthana-anutiika.md` · line 722 · *Upādinnattikavaṇṇanā*

**Printed `51.` — should resolve to 15.**

**Lemma.** The paragraph quotes the mūlaṭīkā's `15.` word for word —
*"nādhipatipaccayāti sayaṃ adhipatibhūtattā"ti* — so it is commenting on that paragraph,
which is itself anchored to root 15.

**Meaning.** Its subject is *na-adhipati-paccaya*. Root `^7-5-15` is the Paṭiccavāra's
*naadhipatipaccayo*; root `^7-5-51` is the Pañhāvāra's *hetupaccaya*. Different conditions
entirely. Only roots 15 and 38 mention *na-adhipati-paccaya* in this section, and only 15
has it in the **Paṭiccavāra** (*paṭicca*) — 38 is the Paccayavāra (*paccayā*).

**Caution — this case was first recorded backwards.** The aṭṭhakathā and anuṭīkā both print
`51.` against the mūlaṭīkā's `15.`, which reads as two witnesses against one. But the
aṭṭhakathā's `51.` is a different paragraph on a different condition that merely shares a
number — it was never a witness.

```
aṭṭhakathā  51.  72.    pañhāvāra, purejāta    → root 51   correct
mūlaṭīkā    15.  72.    paṭiccavāra, adhipati  → root 15   correct
anuṭīkā     51.  72.    glosses mūlaṭīkā's 15  → root 15   WRONG
```

The mūlaṭīkā here comments directly on the root, skipping the aṭṭhakathā, which has no
paragraph on root 15 at all. That tier-skipping is normal and is why the aṭṭhakathā's
number was never evidence.

### A plausible mechanism

VRI typesets from a Devanagari master, where three numerals are easily confused. Two of
the four errors are exactly these substitutions, which points to transcription rather than
scribal reasoning:

| | |
|---|---|
| ६२० → ८२० | 620 → 820 (case 2) |
| ६४१ → ५४१ | 641 → 541 (case 3) |

---

## Two that are not errors

### 5. Truncated-tail ranges

`pi-kathavatthu-mulatiika.md` · lines 798 and 832

**`557-8.` = 557–558 · `571-2.` = 571–572**

The range end repeats only the digits that change. Confirmed by direct witness, not
inference: for these same two passages the aṭṭhakathā and anuṭīkā write `557-558.` and
`571-572.` in full. Lemma check confirms both — *Bhavaṅgacittassa bhaṅgakkhaṇena sahevā*ti
occurs in exactly one aṭṭhakathā paragraph, `571-572.`; *Tassa ñāṇassā*ti resolves to
`557-558.` These are the only two such ranges in the corpus.

> **Scope the expansion rule carefully.** Apply it only where the root index is flat
> (pi-3, pi-4, pi-5). In pi-6 and pi-7 the root is segmented into numbering epochs, so a
> range whose end is smaller than its start could be a genuine reset crossing rather than
> an abbreviation. None exist yet — the first to appear needs a human decision, not an
> automatic expansion.

### 6. An umbrella citation

`pi-kathavatthu-atthakatha.md` · line 1591 · *Anantarāpayuttakathāvaṇṇanā*

```
660-662.  Idāni anantarāpayuttakathā nāma hoti…   names the whole section → root 660
   661.  Idāni yassa aniyatāṇattikassāpi…                                 → root 661
   662.  Puna anantarāpayuttoti pariyosānapañhe…                          → root 662
```

The section opener cites the section's full span, then individual paragraphs follow inside
it. This is the standard behaviour of the *Idāni … kathā nāma hoti* formula — `658-659.`,
`706-708.`, `618-620.` and `641-645.` all do the same. This is simply the one place where
the opener is also followed by per-paragraph citations.

Each of the three lands on its own root paragraph. The shared lemma *Nanu taṃ kamman*ti
occurs in both 660 and 662, but the gloss separates them: the umbrella explains kukkucca
**arising** (root 660), while `662.` explains having **previously been engaged** in the
deed (root 662).

**Any overlap checker will flag `661.` as overlapping `660-662.` — whitelist the entry
rather than editing it.**

---

## Addendum: pi-1 Dhammasaṅgaṇī commentaries (2026-11-10)

`pi-dhammasangani-{atthakatha,mulatiika,anutiika}.md`. Their leading numbers had been stripped
in an older conversion and were restored from the CST XML `paranum` values (286 / 236 / 195,
identical to CST). Every paragraph was then read against the root paragraphs it cites (693
pairs, root ↔ each tier, `verify-transclusion-citation-digit-alignment`): 685 fit. Root
numbering runs flat in three epochs — `^1-M1-N` (Tikamātikā), `^1-M2-N` (Dukamātikā),
`^1-N` (body) — so the expansion rule for truncated tails applies. The ṭīkās' opening
`1.`–`20.` (Vīsatigāthā/Nidāna) gloss the aṭṭhakathā's own twenty verses, not the root, and
carry no root link. **All numbers stay as printed and are linked as printed**, as for pi-5.

### 7. A misread final digit

`pi-dhammasangani-atthakatha.md` · line 3674 · *Akusalapadaṃ › Dhammuddesavārakathā*

**Printed `386.` — should resolve to 381.**

**Lemma and tiers.** The mūlaṭīkā's `381.` quotes this paragraph word for word —
*"Diṭṭhiyā virūpaṃ phanditanti…"* — so the same edition numbers this passage 381 one tier down.

**Meaning.** It opens *Micchādiṭṭhiniddese ayāthāvadassanaṭṭhena micchādiṭṭhi* and glosses
*diṭṭhigataṃ, diṭṭhigahanaṃ, diṭṭhikantāro, diṭṭhivisūkāyikaṃ, diṭṭhivipphanditaṃ* — the
definition of micchādiṭṭhi at root 381. Root 386 is samādhibala; none of those words occur in it.

**Structure.** The aṭṭhakathā runs `375. 384. 385. 386. 389.`; its topics run cittekaggatā
(375), samādhi words, vīriya (376/385), micchādiṭṭhi (381), lobha/moha (389–390). Same family
as cases 2 and 3: ३८१ → ३८६.

### 8. A ṭīkā number that names neither candidate

`pi-dhammasangani-mulatiika.md` · line 1252 · *Akusalapadaṃ*

**Printed `377.` — should resolve to 376 or 385 (vīriya); undecided.**

**Lemma.** *"Sahajātadhammesu akampanaṃ na kosajjesu akampanaṃ viya … ussahanavasena pana
thiratā"* glosses the aṭṭhakathā's `385.` (*Vīriyindriyaniddese … sahajātadhammesu
akampanaṭṭheneva vīriyabalaṃ*). That aṭṭhakathā paragraph itself names the vīriyindriya
definition (root 376) and ends on vīriyabala (root 385), whose word lists are identical.

**Meaning.** Root 377 is samādhindriya; the gloss is about firmness of effort (*kosajja* is
its opposite), not concentration.

### Grouped comments filed under a neighbouring number (conventions, not errors)

CST sometimes files a comment on a group of root paragraphs under one number in or beside the
group. These read as mismatches in a pair-by-pair check; they are linked as printed and need
no resolution.

| File · line | Printed | What it covers |
|---|---|---|
| aṭṭhakathā · 3808, mūlaṭīkā · 1334 | `439.` | cittekaggatā (root 438), then the saṅgaha/suññata vāras and the next viññāṇas — the group whose last padabhājanī paragraph is 439 |
| mūlaṭīkā · 798 | `5.` | glosses the aṭṭhakathā's unnumbered *Cittaniddese…* paragraph, which follows aṭṭhakathā `5.` (cetanā) — content is root 6 (citta) |
| mūlaṭīkā · 1638 | `975.` | the Rūpakaṇḍa's closing *Pakiṇṇakakathā* (middha, nīvaraṇa), filed under the kaṇḍa's last root paragraph 975 |
| aṭṭhakathā · 3666, 3670 | `384.`, `385.` | glosses on word lists shared by several root paragraphs (avisāhāra: 375/377/384/386; vīriya: 376/383/385) — acceptable as printed |

### Truncated-tail ranges in pi-1

aṭṭhakathā `156-9.` (line 2785) and `972-4.` (line 4539), mūlaṭīkā `161-2.` (line 1014) —
the same abbreviation as case 5. pi-1's root runs are flat, so each is linked to the full
range (156–159, 972–974, 161–162). Unlike pi-5's mūlaṭīkā, where `557-8.` and `571-2.` were
written out in the text, the pi-1 files keep the printed form.

## Addendum: pi-2 Vibhaṅga commentaries (2026-11-10)

`pi-vibhanga-{atthakatha,mulatiika,anutiika}.md`. CST packs the mūlaṭīkā and anuṭīkā into one book, `abh02t.tik`
(the anuṭīkā starts at its own homage, paragraph 1152). Leading numbers had been stripped as in pi-1 and were
restored from the CST `paranum` values (325 / 264 / 228). The text now matches the tipitaka-xml repository line for
line. Every paragraph was read against its linked root span (817 pairs): 814 fit; the rest are below. pi-2's root
runs flat (`^2-1` … `^2-1044`), so truncated tails expand. **Numbers stay as printed and are linked as printed.**

### 9. A number from the previous chapter

`pi-vibhanga-mulatiika.md` · line 302 · *Āyatanavibhaṅgo › Suttantabhājanīyavaṇṇanā*

**Printed `152.` — should resolve to 154.**

**Lemma.** *"Visesatoti … Assādetīti cakkhati-saddo …"* glosses the aṭṭhakathā's `154.` (*Tattha visesato tāva
cakkhatīti cakkhu; rūpaṃ assādeti, vibhāveti cāti attho*), the opening of the Āyatanavibhaṅga commentary.

**Structure.** It sits under the Āyatanavibhaṅga heading, right after *Khandhavibhaṅgavaṇṇanā niṭṭhitā*; root 152 is
the Khandhavibhaṅga's Pañhāpucchaka. **Tiers.** The aṭṭhakathā and anuṭīkā both number this passage 154.

### Root paragraphs CST leaves unnumbered (no root block of that number)

The CST root prints no number on three paragraphs that the commentaries cite: 185 (the Dhātuvibhaṅga's
Pañhāpucchaka opening), 252 (the third round of the Paccayākāra's first method), 264 (the Sampayuttacatukka
opening). pi-2.md has no `^2-185`, `^2-252`, `^2-264` (also none for 298, which no commentary cites); the text sits
in a neighbouring block. Linking as printed is impossible, so each citation is linked to the block holding the words
it quotes: `185.` → `^2-186` (*aṭṭhārasannaṃ dhātūnaṃ … kati kusalā*), `252.` → `^2-253` (*cakkhāyatanassa
upacayo*), `264.` → `^2-265` (*… viññāṇasampayuttaṃ*). Confirmed by reading in all three tiers.

### Unnumbered root segments folded into the preceding number

After root 924–950 (Khuddakavatthuvibhaṅga) CST prints whole runs of items without numbers (e.g. 924 *Tayo kiñcanā*,
then *Tīṇi aṅgaṇāni*, *Tīṇi malāni* … *Tayo aggī* unnumbered until 925). pi-2.md gives each its own `^2-U<k>`
segment (72 in all). They belong to the number before them, so a citation of N is linked to `^2-N` and the `^2-U`
segments that follow it (e.g. aṭṭhakathā `946.` on *somanassupavicāra* lands in `^2-U64`).

### Conventions read as acceptable

| File · line | Printed | Note |
|---|---|---|
| aṭṭhakathā · 3510 | `553.` | explains the synonym list *cattattā vantattā muttattā …*, which root 547 (*vigatathinamiddho*) and 553 (*anuddhato*) share |
| mūlaṭīkā · 1891 | `550.` | defines ālokasaññā, quoting root 549 (*ayaṃ saññā ālokā hoti*); the mūlaṭīkā has no 549 |

### Truncated-tail ranges in pi-2

aṭṭhakathā `196-7.` (962), `517-8.` (3280); mūlaṭīkā `196-7.` (597); anuṭīkā `196-7.` (631), `248-9.` (1256),
`468-9.` (1615), `470-1.` (1630), `542-3.` (1787), `843-4.` (2254). Kept as printed, linked to the full range.

---

## The exception list

| File | Line | As printed | Resolve to | Basis |
|---|---|---|---|---|
| `pi-kathavatthu-atthakatha.md` | 1479 | `618-820.` | 618–620 | lemma ×3, coverage |
| `pi-kathavatthu-atthakatha.md` | 1547 | `541-545.` | 641–645 | lemma, gap/duplicate |
| `pi-kathavatthu-anutiika.md` | 1098 | `706-608.` | 706–708 | unique lemma, meaning |
| `pi-patthana-anutiika.md` | 722 | `51.` | 15 | lemma, root section |
| `pi-kathavatthu-mulatiika.md` | 798 | `557-8.` | 557–558 | abbreviation — parse rule |
| `pi-kathavatthu-mulatiika.md` | 832 | `571-2.` | 571–572 | abbreviation — parse rule |
| `pi-kathavatthu-atthakatha.md` | 1591 | `660-662.` | 660–662 | umbrella — whitelist overlap |
| `pi-dhammasangani-atthakatha.md` | 3674 | `386.` | 381 | lemma (mūlaṭīkā `381.` quotes it), meaning |
| `pi-dhammasangani-mulatiika.md` | 1252 | `377.` | 376 or 385 (undecided) | lemma (glosses aṭṭhakathā `385.`), meaning |
| `pi-dhammasangani-atthakatha.md` | 2785, 4539 | `156-9.`, `972-4.` | 156–159, 972–974 | abbreviation — parse rule |
| `pi-dhammasangani-mulatiika.md` | 1014 | `161-2.` | 161–162 | abbreviation — parse rule |
| `pi-vibhanga-mulatiika.md` | 302 | `152.` | 154 | lemma (glosses aṭṭhakathā `154.`), heading, tiers |
| `pi-vibhanga-*.md` | — | `185.`, `252.`, `264.` | ^2-186, ^2-253, ^2-265 (linked) | root number does not exist; block holding the quoted words |
| `pi-vibhanga-*.md` | — | `196-7.` and 8 more | full range | abbreviation — parse rule |

## Provenance

Every citation was diffed against the `<hi rend="paranum">` values in the tipitaka.org CST
XML — **0 differences across all fifteen files**:

```
pi-3 att/mul/anu   54 /  26 /  26     IDENTICAL
pi-4 att/mul/anu  145 /  70 /  56     IDENTICAL
pi-5 att/mul/anu  388 / 223 / 208     IDENTICAL
pi-6 att/mul/anu   78 /  48 /  48     IDENTICAL
pi-7 att/mul/anu  185 / 119 / 112     IDENTICAL
```

The same readings — including all four errors — were confirmed in four further places,
none of them independent witnesses:

- `github.com/VipassanaTech/tipitaka-xml`, current `romn/` master
- the same repository's `deva/` Devanagari master, which VRI typesets from
- tipitakapali.org
- tipitaka.app and tipitaka.sutta.org

**No non-CST digital edition of these commentaries appears to exist.** Each reading is
therefore *attested* but cannot be corroborated against another edition. The resolutions
above are reconstructions from the text's own evidence — no source prints them. A printed
Sixth Council, PTS or Sinhala edition would settle them outright.

## Related

- `4-SYSTEM/Guidelines/known-source-irregularities.md` — working guideline, with the
  reproduction recipe and the scanner's false-positive traps
- `4-SYSTEM/Guidelines/alignment-star-vs-chain.md` — why alignment anchors each tier to the
  root rather than chaining tier to tier
