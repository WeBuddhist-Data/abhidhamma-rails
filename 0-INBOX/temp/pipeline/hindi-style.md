# Hindi plain translations: shared style rules (pi-3, pi-4, pi-5)

Audience: AI_translation\audience_profile\plain.md. Readers have little or no Buddhist background, so make the text understandable. Write clear, modern, natural Hindi. Minor clarification through wording is OK, but add nothing that is absent from the source. Priority: understanding > accuracy > readability > consistency.

## Language and vocabulary
- Write modern standard Hindi (खड़ी बोली) in Devanagari, in a plain register that a general Hindi reader follows easily.
- Prefer common Hindi words. Use a Sanskrit-derived (tatsama) word where it is the normal Hindi word, but avoid rare or heavy Sanskritisms and needless Perso-Arabic or English words.
- **Technical terms:** translate the concept into understandable Hindi. Do not leave opaque Pāli terms (e.g. khandha, āyatana, dhātu) as bare transliterations. The audience must understand the term without a glossary.
- **Names and fixed Buddhist words:** use the forms familiar to Hindi readers (बुद्ध, भगवान, अर्हत्, निर्वाण, भिक्षु).
- **Book titles (user, 2026-11-09):** use only the Hindi name, no Pāli name and no bracketed gloss, as the English and Russian do: तत्वों पर चर्चा, परिघटनाओं की गणना, व्यक्तियों का विवरण, चर्चा के विषय. Mid-sentence, put the title in quotes (“तत्वों पर चर्चा” ग्रंथ समाप्त). अभिधम्म पिटक stays. Citation brackets such as [पुग्गलपञ्ञत्ति 131] stay as references.
- Grammar, gender agreement and word order must be natural Hindi. Keep the chosen word for a term consistent within your work.

## Typography
- End statements with "।". Questions end with "?". Yes/no questions may open with «क्या», which is natural Hindi.
- Quotes: “…” for the outer level and ‘…’ for the nested level.
- **DASH RULE (user, strict):** "–" appears ONLY where the Pāli has "–" or "—", at the same spot and with the same count on every line. Never add one anywhere else, even though Hindi prose often uses "—". Also no ":-". Rephrase instead.
- "…pe…" becomes "…" at the same spot.
- **Digits:** where the Pāli has digits, e.g. "(1)", keep international digits. Numbers written as Pāli words become Hindi words.
- **Variant brackets:** keep the sigla and the variant's Pāli, and translate the label:
  - «[पाठभेद (Sī., Syā.): …]» when a word differs;
  - «[वर्तनी-भेद (Syā.): …]» for spelling-only differences.
- Translate editorial notes in square brackets.

## Structure (hard rules)
- Every block ID stays exactly as in the source, at the end of the last line of its segment, in the same order.
- Headings keep their #-level.
- Each segment has exactly the source's number of non-empty lines, with one blank line between segments and no double blank lines.
- Identical Pāli formulas get identical Hindi. A small helper script with fixed formula strings is a good way to guarantee this.
- Translate FROM THE PĀLI. The English zero-shot (AI_translation\english\pi-N-english-plain-zeroshot_split_chapters) and the user-approved Russian term files may be used only as a cross-check of meaning and structure.
- Do not copy Russian-specific conventions:
  - the «ли» ban is Russian-only;
  - Russian «…» quotes become “…” here.

## Cross-book core terms (chapter-1 samples approved by the user on 2026-11-07; use them in all three books)

### Text frame
- Namo tassa bhagavato arahato sammāsambuddhassa = उन भगवान, अर्हत्, पूर्ण रूप से जागृत बुद्ध को नमन
- Abhidhammapiṭake = अभिधम्म पिटक में

### Core Abhidhamma terms
- dhamma (phenomenon) = परिघटना; dhamma (the Teaching) = शिक्षा. Never धर्म.
- khandha = समूह. The five: भौतिक रूप / अनुभूति / पहचान / मानसिक रचनाओं / चेतना का समूह.
- rūpa (matter) = भौतिक रूप; rūpa (visible object) = दृश्य रूप.
- āyatana = इंद्रिय-क्षेत्र; a single one = X का इंद्रिय-क्षेत्र (आँख का इंद्रिय-क्षेत्र, मन के विषयों का इंद्रिय-क्षेत्र).
- dhātu = तत्व.
- sacca = सत्य.
- indriya (the 22 faculties) = क्षमता. Where indriya means the senses (indriyesu guttadvāro) = इंद्रिय.

### Mind and mental factors
- vedanā = अनुभूति; saññā = पहचान; saṅkhāra = मानसिक रचनाएँ; viññāṇa = चेतना.
- cetanā = इरादा; citta = मन; phassa = संपर्क; manasikāra = मनोयोग; adhimokkha = निश्चय.
- saddhā = श्रद्धा; vīriya = उत्साह; sati = सजगता; samādhi = एकाग्रता; paññā = प्रज्ञा.
- jhāna = ध्यान (the four: ध्यान की चार अवस्थाएँ).

### Path, beings and attainments
- paṭiccasamuppāda = परस्पर-आश्रित उत्पत्ति.
- asaṅkhata = अनिर्मित.
- puggala = व्यक्ति.
- ariya = आर्य.
- magga / phala = मार्ग / फल.
- sotāpanna = धारा में प्रवेश कर चुका; sakadāgāmī = एक बार लौटने वाला; anāgāmī = फिर न लौटने वाला.
- arahant = अर्हत्; arahatta = अर्हत्-पद.
- nibbāna = निर्वाण; parinibbāna = पूर्ण निर्वाण.
- bhagavā = भगवान; Tathāgata = तथागत; bhikkhu = भिक्षु; sāvaka = शिष्य.
- kappa = कल्प.

### Defilements and qualities
- kusala / akusala = हितकर / हानिकर.
- āsava = मन के मैल; saṃyojana = बंधन; kilesa = मन के क्लेश.
- avijjā = अज्ञान; uddhacca = बेचैनी; byāpāda = दुर्भावना.

### Lessons from the Russian bilingual review (apply from the start)
- abyākata means "neither wholesome nor unwholesome", not "neutral" in the feeling sense. Suggested: नैतिक रूप से अनिर्धारित.
- Keep these pairs distinct, one word each, never swapped:
  - vicikicchā (संशय) vs kaṅkhā (शंका);
  - mettā (मैत्री) vs abyāpāda (दुर्भावना का अभाव);
  - kukkucca (पछतावा) vs uddhacca (बेचैनी);
  - vīriya (उत्साह) vs padhāna / vāyāma (प्रयास).
- samudaya = उत्पत्ति. yoni = जन्म का प्रकार, distinct from saṃsāra = जन्म-मरण का चक्र.

## Verify (must pass)
```
python -I 0-INBOX\temp\pipeline\check_chapter_ids.py <pali_split_dir> <hindi_split_dir> <ch>.md
python -I -X utf8 -c "import sys;f=lambda p:[l for l in open(p,encoding='utf-8').read().splitlines() if l.strip()];c=lambda t:t.count('—')+t.count('–');a,b=f(sys.argv[1]),f(sys.argv[2]);bad=[i for i,(x,y) in enumerate(zip(a,b)) if c(x)!=c(y)];print('lines',len(a),len(b),'dash-line mismatches',len(bad),bad[:5])" <pali_file> <hindi_file>
```
Both must pass: equal line counts and 0 dash mismatches. For a partial sample, compare against the same Pāli lines (e.g. write them to a scratch file first).
