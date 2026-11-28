# pi-6 (Yamaka) Pāli→Russian keyword map: what pi-6 adds to the pi-1 / pi-2 conventions

Settled on the sample (preamble, 1-mulayamaka; 142 lines). Binding base: `..\..\pi-1-ru\mapper-ru\ru-map-conventions.md` (incl. the user decision of 2026-11-14) and `..\..\pi-2-ru\mapper-ru\ru-map-conventions-pi2.md` (incl. the user decision of 2026-11-16). This file lists only additions and changes. The translation file is the truth; the value is always the word or phrase found in THAT segment's Russian. The Russian was built from fixed phrase tables (`..\build_sample_ru.py`, `..\ru-zeroshot-terms.md`), so identical Pāli has identical Russian: a table plus per-segment overrides is the right tool.

## 1. Tooling
- `map_common_pi6_ru.py`: pi-6 paths; re-exports pi-1 `present()`, `CORE`, `CH2`, `MATRIX`, `lc` and pi-2 `KH`, `PREPOSITIONS`; `YM` (the pi-6 table); `root_family(member, sg, pl, loc, ins, neut)` generates every Mūlayamaka / Hetuvārādi compound of one member; `value(kw, kws, table)` = your table → `KH` → pi-1 `CH2` / `MATRIX`, with -ti / -ñca / -ñceva folded to the base keyword; `build_part`, `verify(part, allowed=allowed_for(part))`. Importing it writes nothing.
- `YM` already carries the pi-2 N-vidhena values WITHOUT «классификация» (pi-2 `KH` still has it in its FRAME; `YM` wins).
- `map_sample_ru.py`: pattern for a part script: `OVERRIDES[bid][kw]` → CORE (frame words) → `{**YM, ...}` → `value()`. Extend `YM` only in your own script; add members with `root_family()`.
- `verify()` prints: structural check (`bad []`), pairs, (no direct equivalent), presence misses, root-compound gap matches, listed exceptions, bare prepositions, cut-negation values (a value word found in the segment only with a glued «не»).

## 2. Root compounds (one value each, the phrase the text uses)
- ekamūla- = **имеющий общий корень**; aññamaññamūla- = **имеющий взаимный корень**; ekamūlamūla- / aññamaññamūlamūla- = имеющий общий / взаимный корень корней.
- ekamūlaka- = **основанный на общем корне**; aññamaññamūlaka- = основанный на взаимном корне; ekamūlamūlaka- / aññamaññamūlamūlaka- = основанный на общем / взаимном корне корней.
- All case/number forms and the particles take the same value: ekamūlā, ekamūlaṃ, ekamūlāni, ekamūlāti, ekamūlañceva. Reason: the text uses one verb phrase for all («имеют / имеет / имеющие / не имеет общего … корня»; «основаны / основано / основанные»); participle masc. sg. as in pi-1 (adjectives alone) and as the zero-shot terms list gives it.
- X-mūla(ā/āni) = **X-е корни** (plural: Pāli plural, text «являются благими корнями», «все благие корни», «три благих корня»): kusalamūlā = благие корни, akusalamūlāni = неблагие корни, nāmamūlā = умственные корни. X-mūlamūla- = благие корни корней. Mūlāni = корни.
- X-mūlaka- = **основанный на X-ом корне** (основанный на благом корне); X-mūlamūlaka- = основанный на благом корне корней.
- X-mūlasahajātā dhammā = явления возникшие вместе с благим корнем (pi-1 dhammā-phrase rule); without dhammā (nāmamūlasahajātā) = возникший вместе с умственным корнем.
- X-samuṭṭhānaṃ (Kusalasamuṭṭhānaṃ rūpaṃ «Материальная форма, порождённая благим») = порождённый благим; rūpaṃ = материальная форма.
- The value never contains the member's case ending from the text: the root compound values are the same whatever member stands in front of «корень».

## 3. Instrumental keywords
- X-mūlena (kusalamūlena, akusalamūlena, abyākatamūlena, nāmamūlena) = **X-ый корень** in the nominative: благой корень, этически неопределённый корень, умственный корень. The Russian has no «с» here (it says «имеют общий благой корень»); a «с …» phrase, where a later chapter has one, also goes to the nominative noun phrase, never a bare «с».
- X-mūlaṃ = благой корень (pi-1 kusalamūlaṃ).

## 4. Members
- kusala / akusala / abyākata = благой / неблагой / этически неопределённый in every form (kusalā, kusalaṃ, kusalāti, kusalañca), as pi-1 / pi-2.
- nāma: **nāmā** (adjective of «nāmā dhammā» = «умственные явления») = умственный; **nāmaṃ / nāmañca** (the Pāli noun, «Умственное, не имеющее корней») = умственное (pi-2 has nāmaṃ = умственное on 81 lines; pi-1 nāmañca = умственное). So the noun keeps the neuter form, the adjective the masculine.
- `X dhammā` = X-е явления (благие явления; heading «Kusalā dhammā» the same).
- Ahetukaṃ / Sahetukaṃ = не имеющий корней / имеющий корни (pi-2). avasesā (Avasesā) = остальной (pi-1/2). uppajjanti = возникать.

## 5. Hetuvārādi series and verse
- Member + series noun = plural phrase as the text: kusalahetū(ti) = благие причины, -nidānā благие источники, -sambhavā благие начала, -ppabhavā благие истоки, -samuṭṭhānā благие порождающие факторы, -āhārā **благое питание** (text «благим питанием», singular), -ārammaṇā благие объекты, -paccayā благие условия, -samudayā благие возникновения. Same with nāma- (умственные причины …, умственное питание).
- Verse «Mūlaṃ hetu nidānañca, sambhavo pabhavena ca; Samuṭṭhānāhārārammaṇā, paccayo samudayena cāti»: Mūlaṃ корень, hetu **причина** (user decision: hetu in the hetuvāra series = причина; hetu stays корень in ahetuka / sahetuka), nidānañca источник, sambhavo начало, pabhavena исток, Samuṭṭhānāhārārammaṇā = порождающий фактор питание объект (commas dropped), paccayo условие, samudayena возникновение.

## 6. Headings and colophons
- A heading keyword maps to the heading phrase that renders it, without the label or number («(а)», «(1)», «2-10.»), first letter lower-case (proper names keep theirs: Абхидхамма, Благословенный, Будда). Where a heading has two keywords, each gets its own part: «Akusalā dhammā (1) mūlanayo» = Akusalā dhammā=неблагие явления, mūlanayo=метод корней.
- Yamakapāḷi = парные вопросы (-pāḷi not rendered; pāḷi alone = (no direct equivalent), pi-2). Mūlayamakaṃ / Mūlayamakapāḷi = парные вопросы о корнях (the other yamakas: «парные вопросы о совокупностях» … from ru-zeroshot-terms.md).
- uddeso = перечень, niddeso = разъяснение, -nayo = метод, -vāro = раздел (pi-1/2/3). Mūlavāro = раздел о корнях; Hetuvārādi = раздел о причинах и другие; Mūlanayo = метод корней, Mūlamūlanayo = метод корней корней, Mūlakanayo = метод основания на корне, Mūlamūlakanayo = метод основания на корне корней.
- Colophons: Uddesavāro = раздел перечня, Niddesavāro = раздел разъяснения, Mūlavārauddeso = перечень раздела о корнях, Mūlavāraniddeso = разъяснение раздела о корнях; niṭṭhito / niṭṭhitā = завершённый (pi-1/2). Compound heading keywords = the whole phrase; their members, if listed, = their own part.

## 7. Question frames and answers (one rule; later chapters)
- `Āmantā` = **да** (pi-5, 875 lines). `Natthi` («Такого нет.») = **такого нет** (coordinator: keeps it apart from No = нет). `na` = не. `No` as the answer «No.» = нет (pi-5); `no` inside a sentence (no ca …) = the word the Russian uses (не), or (no direct equivalent) where the coordinator's rule says the denied negative plainly («но у них возникает Y»); not in `YM`, decide per segment.
- `(Ka) ye keci X dhammā, sabbe te Y?` = «Все X явления Y?»; `(Kha) ye vā pana Y, sabbe te dhammā X?` = «А все Y …» / «А всё, что Y, …». Rule: **sabbe / sabbe te = все** (one value; «всё» is the same word, ё = е); **ye keci = (no direct equivalent)** (the relative has no word of its own: «все» renders ye keci … sabbe te together; user decision 2026-11-14); `vā pana` = а. The quotation -ti adds nothing (kusalāti = благой).
- Partial answers («Tīṇeva kusalamūlāni» «Есть только три благих корня»): map the listed keywords only; numbers, if listed, as the Russian word (tīṇi три, nava девять).

## 8. Presence check (pi-6 addition)
- Root compounds (ekamūla-, aññamaññamūla-) are checked with `present_gap`: the value's words in order with up to three words between them, because the member («благой», «этически неопределённый») or the «и …, и …» of ceva … ca stands inside the phrase («имеют общий благой корень», «имеют и общий корень, и взаимный корень»). Everything else uses pi-1 `present()` unchanged. pi-2 `EXCEPTIONS` are inherited (none was needed in the sample).
