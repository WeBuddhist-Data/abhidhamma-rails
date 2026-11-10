# Marathi plain translations: shared style rules (pi-3 and later books)

Audience: AI_translation/audience_profile/plain.md. Readers have little or no Buddhist background, so make the text understandable. Write clear, modern, natural Marathi. Minor clarification through wording is OK, but add nothing that is absent from the source. Priority: understanding > accuracy > readability > consistency.

## Language and vocabulary
- Write modern standard Marathi (प्रमाण मराठी) in Devanagari, in a plain register that a general Marathi reader follows easily.
- Prefer common Marathi words. Use a Sanskrit-derived (tatsama) word where it is the normal Marathi word, but avoid rare or heavy Sanskritisms and needless English words. Everyday words win for the senses and their objects: आवाज, वास, चव, स्पर्श.
- **Technical terms:** translate the concept into understandable Marathi. Do not leave opaque Pāli terms (e.g. khandha, āyatana, dhātu) as bare transliterations. The audience must understand the term without a glossary.
- **Names and fixed Buddhist words:** use the forms familiar to Marathi readers (बुद्ध, भगवान, अर्हत, निर्वाण, भिक्षू). Honorific plural for the Buddha (बुद्धांना, भगवानांनी).
- **Book titles:** use only the Marathi name, no Pāli name and no bracketed gloss: तत्त्वांवरील चर्चा, घटनांची गणना, व्यक्तींचे वर्णन, चर्चेचे विषय, विश्लेषण (Vibhaṅga, user 2026-11-09). Mid-sentence, put the title in quotes (“तत्त्वांवरील चर्चा” ग्रंथ समाप्त). अभिधम्म पिटक stays. Citation brackets such as [पुग्गलपञ्ञत्ति 131] stay as references.
- Grammar, gender and number agreement, case endings and word order must be natural Marathi. Keep the chosen word for a term consistent within your work.
- Spelling: follow current Marathi orthography (तत्त्व, अनुभूती, उत्पत्ती, व्यक्ती, भिक्षू, शिकवण).

## Typography
- End statements with "." (Marathi uses the full stop, not "।"). Questions end with "?". Yes/no questions may open with «काय», which is natural Marathi.
- Quotes: “…” for the outer level and ‘…’ for the nested level.
- **DASH RULE (user, strict):** "–" appears ONLY where the Pāli has "–" or "—", at the same spot and with the same count on every line. Never add one anywhere else. Also no ":-". Rephrase instead. A normal hyphen inside a compound word (इंद्रिय-क्षेत्र, दोन-दोन) is not a dash and is fine.
- "…pe…" becomes "…" at the same spot.
- **Digits:** where the Pāli has digits, e.g. "(1)", keep international digits. Numbers written as Pāli words become Marathi words.
- **Variant brackets:** keep the sigla and the variant's Pāli, and translate the label:
  - «[पाठभेद (Sī., Syā.): …]» when a word differs;
  - «[लेखनभेद (Syā.): …]» for spelling-only differences.
- Translate editorial notes in square brackets.

## Structure (hard rules)
- Every block ID stays exactly as in the source, at the end of the last line of its segment, in the same order.
- Headings keep their #-level.
- Each segment has exactly the source's number of non-empty lines, with one blank line between segments and no double blank lines.
- Identical Pāli formulas get identical Marathi. A small helper script with fixed formula strings is a good way to guarantee this.
- Translate FROM THE PĀLI. The English zero-shot (AI_translation/english/pi-N-english-plain-zeroshot_split_chapters) and the Hindi zero-shot (AI_translation/hindi/pi-N-hindi-plain-zeroshot_split_chapters) may be used only as a cross-check of meaning and structure.
- Do not copy Hindi- or Russian-specific conventions: Hindi «।» becomes «.» here; Russian «…» quotes become “…”.

## Cross-book core terms (proposed with the pi-3 chapter-1 sample; binding once the user approves it)

### Text frame
- Namo tassa bhagavato arahato sammāsambuddhassa = त्या भगवान, अर्हत, पूर्णपणे जागृत बुद्धांना नमन
- Abhidhammapiṭake = अभिधम्म पिटकात

### Core Abhidhamma terms
- dhamma (phenomenon) = घटना (plural घटना); dhamma (the Teaching) = शिकवण. Never धर्म.
- khandha = समूह. The five: भौतिक रूपाचा / अनुभूतीचा / ओळखीचा / मानसिक रचनांचा / चेतनेचा समूह.
- rūpa (matter) = भौतिक रूप; rūpa (visible object) = दृश्य रूप.
- āyatana = इंद्रिय-क्षेत्र (plural इंद्रिय-क्षेत्रे); a single one = X चे इंद्रिय-क्षेत्र (डोळ्याचे इंद्रिय-क्षेत्र, मनाच्या विषयांचे इंद्रिय-क्षेत्र).
- dhātu = तत्त्व (plural तत्त्वे); a single one = X चे तत्त्व (डोळ्याचे तत्त्व, डोळ्याच्या चेतनेचे तत्त्व).
- The six senses and objects: cakkhu डोळा, sota कान, ghāna नाक, jivhā जीभ, kāya शरीर, mano मन; rūpa दृश्य रूप, sadda आवाज, gandha वास, rasa चव, phoṭṭhabba स्पर्श, dhamma (object of mind) मनाचे विषय.
- sacca = सत्य (plural सत्ये).
- indriya (the 22 faculties) = क्षमता. Where indriya means the senses (indriyesu guttadvāro) = इंद्रिये.

### Mind and mental factors
- vedanā = अनुभूती; saññā = ओळख; saṅkhāra = मानसिक रचना; viññāṇa = चेतना.
- cetanā = इरादा; citta = मन; phassa = संपर्क; manasikāra = मनोयोग; adhimokkha = निश्चय.
- saddhā = श्रद्धा; vīriya = उत्साह; sati = सजगता; samādhi = एकाग्रता; paññā = प्रज्ञा.
- jhāna = ध्यान (the four: ध्यानाच्या चार अवस्था).

### Path, beings and attainments
- paṭiccasamuppāda = परस्परावलंबी उत्पत्ती.
- asaṅkhata = अनिर्मित.
- puggala = व्यक्ती.
- ariya = आर्य.
- magga / phala = मार्ग / फळ.
- sotāpanna = प्रवाहात प्रवेश केलेला; sakadāgāmī = एकदा परतणारा; anāgāmī = पुन्हा न परतणारा.
- arahant = अर्हत; arahatta = अर्हतपद.
- nibbāna = निर्वाण; parinibbāna = पूर्ण निर्वाण.
- bhagavā = भगवान; Tathāgata = तथागत; bhikkhu = भिक्षू; sāvaka = शिष्य.
- kappa = कल्प.

### Defilements and qualities
- kusala / akusala = हितकारक / हानिकारक.
- āsava = मनाचे मळ; saṃyojana = बंधने; kilesa = मनाचे क्लेश.
- avijjā = अज्ञान; uddhacca = अस्वस्थता; byāpāda = दुर्भावना.

### Lessons from the Russian bilingual review (apply from the start)
- abyākata means "neither wholesome nor unwholesome", not "neutral" in the feeling sense: नैतिकदृष्ट्या अनिर्धारित.
- Keep these pairs distinct, one word each, never swapped:
  - vicikicchā (संशय) vs kaṅkhā (शंका);
  - mettā (मैत्री) vs abyāpāda (दुर्भावनेचा अभाव);
  - kukkucca (पश्चात्ताप) vs uddhacca (अस्वस्थता);
  - vīriya (उत्साह) vs padhāna / vāyāma (प्रयत्न).
- samudaya = उत्पत्ती. yoni = जन्माचा प्रकार, distinct from saṃsāra = जन्म-मृत्यूचे चक्र.

## Verify (must pass)
```
python3 -I -X utf8 0-INBOX/temp/pipeline/check_chapter_ids.py <pali_split_dir> <marathi_split_dir> <ch>.md
python3 -I -X utf8 -c "import sys;f=lambda p:[l for l in open(p,encoding='utf-8').read().splitlines() if l.strip()];c=lambda t:t.count('—')+t.count('–');a,b=f(sys.argv[1]),f(sys.argv[2]);bad=[i for i,(x,y) in enumerate(zip(a,b)) if c(x)!=c(y)];print('lines',len(a),len(b),'dash-line mismatches',len(bad),bad[:5])" <pali_file> <marathi_file>
```
Both must pass: equal line counts and 0 dash mismatches. For a partial sample, compare against the same Pāli lines (e.g. write them to a scratch file first). Also check that no line ends a statement with "।".
