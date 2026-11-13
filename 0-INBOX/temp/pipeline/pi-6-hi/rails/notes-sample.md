# Notes of the sample agent (pi-6 Hindi plain RAILS)

Files: AI_translation\hindi\pi-6-hindi-plain-rails_split_chapters\preamble.md, 1-mulayamaka.md; rails\sample-1\2-01-pali-sample.md (byte-exact prefix of 2-01, lines 1-638, CRLF kept as in the source) and 2-01-sample.md; rails\hi-rails-formulas.md; rails\build_rails_sample.py.
Helpers: tb_lookup_sample.py (termbase entries by segment / word), post_check_sample.py (double blanks, CR, Latin outside brackets, banned strings, same Pāli line = same Hindi line), adherence_sample.py (termbase adherence on explicit files), coverage_sample.py (dry run of the builder on any Pāli file, writes nothing).

## Choices made in the sample (beyond hi-zeroshot-terms.md / harmonise Decisions)
- Avasesā <T>mūlasahajātā dhammā = «<R> के साथ उत्पन्न शेष परिघटनाएँ, …» («शेष» moved next to परिघटनाएँ so it cannot be read as «शेष हितकर मूल»).
- Copula in the Paṇṇatti pairs is plural when either side is plural: «क्या मानसिक रचनाओं का समूह, रचनाएँ हैं?», «… रचनाएँ भी हैं और …».
- «X को छोड़कर शेष,» always takes a comma before its predicate.
- ^6-1-49 / ^6-1-99 end with «…?» (abbreviated question lists; the Pāli ends "…pe…."); ^6-1-98 line 2 ends «…।».
- evamuparipi (^6-2-28 variant) = «; आगे भी इसी प्रकार» inside the bracket.

## Source slips seen
- 2-01 ^6-2-36 line 1: "(Ka) na saṅkhārā na saṅkhārakkhandhoti." ends with "." Rendered as a question «?».
- 1-mulayamaka: comma missing before "na" in ^6-1-56, ^6-1-59, ^6-1-68, ^6-1-71 ("…mūlakaṃ na kusalaṃ") and ^6-1-70 ("ekamūlakā na ca"); rendered like the comma form.
- (later, for the next agents) 2-01 ^6-2-61: second question labelled "(Ka)" (should be Kha); ^6-2-87: variant bracket inside the being chain; ^6-2-111: "nirujjhattha" (read as nirujjhittha, VERB_SLIPS); 2-02: line 111 and 261 "ca" missing before the second verb; line 198 stray comma in a "both" clause; line 372 "vadanākkhandho"; line 85 and 375 parenthetical notes.

## Known gaps of the builder (later agents add their own formulas)
Answers of the pariññā section (Arahā …, Aggamaggasamaṅgiñca … ṭhapetvā avasesā puggalā …), variant brackets inside being chains, parenthetical notes, the other chapters' word tables (āyatana, dhātu, sacca, saṅkhāra, anusaya, citta, dhamma, indriya). Dry run: rest of 2-01 240/241 lines, 2-02 354/366 lines translate; the failures are the cases above.
