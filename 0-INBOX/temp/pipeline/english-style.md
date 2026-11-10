# English plain translations: shared style rules (pi-1 zero-shot)

Audience: AI_translation\audience_profile\plain.md. Readers have little or no Buddhist background, so make the text understandable. Write clear, modern, natural English. Minor clarification through wording is OK, but add nothing that is absent from the source. Priority: understanding > accuracy > readability > consistency.

## Language and vocabulary
- Plain modern English. Prefer common words over Latinate or scholarly ones where the meaning is the same.
- **Technical terms:** translate the concept. Do not leave Pāli terms (khandha, āyatana, dhātu, jhāna …) as bare transliterations in the running text. Fixed words that English readers know stay: Buddha, Blessed One, arahant, Nibbāna, bhikkhu.
- **Book titles:** English name only, no Pāli name and no bracketed gloss: The Enumeration of Phenomena, The Book of Analysis, The Discussion of Elements, The Description of Persons, Points of Discussion, The Book of Pairs. Citation brackets such as [Puggalapaññatti 131] stay as references.
- Keep the chosen word for a term consistent within your work and with the approved term list.

## Typography (as in the existing English books pi-2 to pi-6)
- Straight double quotes "…" for the outer level and single quotes '…' for the nested level.
- **DASH RULE (user, strict):** "–" appears ONLY where the Pāli has "–" or "—", at the same spot and with the same count on every line. Never add one anywhere else. Also no ":-". Rephrase instead (comma, colon, parentheses, new sentence).
- "…pe…" becomes "…" at the same spot.
- **Digits:** where the Pāli has digits, e.g. "(1)" or "1.", keep them. Numbers written as Pāli words become English words.
- **List letters:** the Pāli list markers (Ka), (Kha), (Ga), (Gha) … become (a), (b), (c), (d) … in English.
- **Variant brackets:** keep the sigla and the variant's Pāli, translate the label only: "[variant: arahattāya (Sī.)]". Translate other editorial notes in square brackets.

## Structure (hard rules)
- Every block ID stays exactly as in the source, at the end of the last line of its segment, in the same order.
- Headings keep their #-level.
- Each segment has exactly the source's number of non-empty lines, with one blank line between segments and no double blank lines.
- Identical Pāli formulas get identical English. The Dhammasaṅgaṇī repeats its matrix items and its synonym strings hundreds of times: use a helper script with fixed formula strings so the repeats are byte-identical.
- Translate FROM THE PĀLI.

## Cross-book references (meaning and wording only)
- The English zero-shots of the other books: AI_translation\english\pi-2 … pi-6-english-plain-zeroshot_split_chapters\. pi-3 chapter 1 quotes this book's matrix headings.
- The approved English termbases AI_translation\english\pi-3 … pi-6-pali-english-termbase-plain.md, for example:
  - kusala / akusala = wholesome / unwholesome;
  - khandha = aggregate; vedanā = feeling; saññā = perception; saṅkhāra = mental formations; viññāṇa = consciousness;
  - rūpa = material form (matter), visible form (the sense object);
  - āyatana = sense base; dhātu = element; indriya = faculty;
  - phassa = contact; cetanā = intention; citta = mind; manasikāra = attention;
  - vitakka = applied thought; vicāra = sustained thought; pīti = rapture; upekkhā = equanimity; somanassa = joy; domanassa = sadness;
  - saddhā = faith; sati = mindfulness; samādhi = concentration; paññā = wisdom; jhāna = absorption;
  - āsava = taints; saṃyojana = fetters; ogha = floods; yoga = yokes; nīvaraṇa = hindrances; parāmāsa = misapprehension; upādāna = clinging; kilesa = defilements;
  - saṅkhata / asaṅkhata = conditioned / unconditioned; sanidassana = visible; paritta = limited; mahaggata = exalted; appamāṇa = immeasurable; hīna / paṇīta = inferior / superior; niyata = fixed.
  Follow these unless the plain audience clearly needs something better. Where you depart, list it in the term file with the reason.

## Lessons from the Russian and Hindi bilingual reviews (apply from the start)
- abyākata means "neither wholesome nor unwholesome", not "neutral" in the feeling sense. Use "indeterminate" (or "ethically indeterminate" where the context needs it), never "neutral".
- Keep these pairs distinct, one word each, never swapped:
  - vicikicchā (doubt) vs kaṅkhā (uncertainty);
  - mettā (loving-kindness) vs abyāpāda (non-ill-will);
  - kukkucca (remorse) vs uddhacca (restlessness);
  - vīriya (energy) vs padhāna / vāyāma (effort).
- samudaya = arising (origin of suffering in the truths). yoni = mode of birth, distinct from saṃsāra = the round of rebirth.
- dhamma: "phenomena" / "states" as the book's subject, "objects" for dhammāyatana / dhammadhātu, "the Teaching" for the Buddha's teaching. Never "Dhamma" untranslated in the running text.

## Verify (must pass)
```
python -I 0-INBOX\temp\pipeline\check_chapter_ids.py <pali_split_dir> <english_split_dir> <ch>.md
python -I -X utf8 -c "import sys;f=lambda p:[l for l in open(p,encoding='utf-8').read().splitlines() if l.strip()];c=lambda t:t.count('—')+t.count('–');a,b=f(sys.argv[1]),f(sys.argv[2]);bad=[i for i,(x,y) in enumerate(zip(a,b)) if c(x)!=c(y)];print('lines',len(a),len(b),'dash-line mismatches',len(bad),bad[:5])" <pali_file> <english_file>
```
Both must pass: equal line counts and 0 dash mismatches. For a partial sample, compare against the same Pāli lines (write them to a scratch file first).
