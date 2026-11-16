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

### pi-4 additions (approved with the pi-4 run, 2026-11-10; full list in AI_translation/marathi/pi-4-pali-marathi-termbase-plain.md)
- paññatti = वर्णन (व्यक्तींचे वर्णन, समूहांचे वर्णन).
- Atthekacco puggalo = एखादी व्यक्ती अशी असते जी …; Idhekacco puggalo = इथे एखादी व्यक्ती …
- sekkha / asekkha = अजून शिकत असलेला / शिकणे पूर्ण झालेला (as pi-3).
- vippaṭisāra = पस्तावा, distinct from kukkucca = पश्चात्ताप.
- saṅkhāra as exertion (asaṅkhāra-, sasaṅkhāraparinibbāyī) = प्रयास, distinct from padhāna / vāyāma = प्रयत्न and uṭṭhāna = परिश्रम.
- hiri / ottappa = लज्जा / वाईट कृत्याची भीती; sīla = सदाचार; diṭṭhi = दृष्टी.

### pi-5 additions (pi-5 run, 2026-11-11; full list in AI_translation/marathi/pi-5-pali-marathi-termbase-plain.md)
- niggaha = खंडन; Āmantā = हो; Na hevaṃ vattabbe = असे म्हणू नये; tena hi = तर मग; upalabbhati = आढळणे.
- cavati = मृत्यू पावणे (not च्युत होणे; bilingual review); cuti = मृत्यू.
- dhamma as righteousness (dhammena, dhammarājā) = न्याय, never धर्म.
- nirodhasamāpatti = लोप पावण्याची ध्यान-प्राप्ती; niyāma = निश्चित मार्ग; parinipphanna = पूर्णपणे निर्माण झालेला; upādā (anupādā°) = धरून ठेवणे.
- Citation brackets keep canon references in Pāli names in Devanagari with numbers: [पुग्गलपञ्ञत्ति मातिका 4.24; अंगुत्तर निकाय 4.95-96], [धम्मसंगणी तिकमातिका …].

### pi-6 additions (pi-6 run, 2026-11-12; full list in AI_translation/marathi/pi-6-pali-marathi-termbase-plain.md)
- Yamaka = जोड्या; chapter titles «X च्या जोड्या» (मुळांच्या, समूहांच्या, इंद्रिय-क्षेत्रांच्या, तत्त्वांच्या, सत्यांच्या, रचनांच्या, सुप्त प्रवृत्तींच्या, मनाच्या, घटनांच्या, क्षमतांच्या जोड्या); colophon «“X च्या जोड्या” समाप्त.»; book end «“जोड्या” ग्रंथ समाप्त.».
- «Natthi.» by question type: person «असे कोणी नाही.», place «असे कोणतेही स्थान नाही.», mind «असे कोणतेही मन नाही.»; «no ca» = «पण … नाही» / «… नाही असे नाही».
- parijānāti = «Xचे पूर्ण आकलन करतो» (genitive object); ṭhapetvā = वगळून; vitthāretabbaṃ = विस्ताराने मांडावे; «tesaṃ» after a moment / place phrase = «त्यांच्या बाबतीत».
- dhātu as element = तत्त्व, as sphere = लोक (kāmadhātu = इंद्रियसुखांचा लोक); dhamma as phenomena = घटना, beside dhammāyatana / dhammadhātu = मनाचा विषय; saṅkhāra (Saṅkhārayamaka) = रचना; anusaya = सुप्त प्रवृत्ती; indriya = क्षमता.
- diṭṭhisaññā = मतांच्या स्वरूपातील ओळख (a view, not eyesight); the sota pun = «“सोत” (कान किंवा प्रवाह)», the one allowed gloss.
- «ye … rūpāvacaraṃ arūpāvacaraṃ upapajjitvā» = «सूक्ष्म भौतिक किंवा अभौतिक लोकात» (either world); person qualifiers joined with «आणि».
- Capital «…Pe…» = one «…», like «…pe…».

### pi-7 additions (pi-7 run, 2026-11-14; full list in AI_translation/marathi/pi-7-pali-marathi-termbase-plain.md)
- Paṭṭhāna = कारण-संबंध; book end «“कारण-संबंध” ग्रंथ समाप्त.»; part and section colophons quote the whole title phrase.
- paccaya = आधार: Xpaccayā «Xच्या आधाराने», na-Xpaccayā «Xचा आधार नसताना», counts «Xच्या आधारात N», Xpaccayena paccayo «Xच्या रूपाने आधार असतो / असते / असतात»; paṭicca = «…वर अवलंबून»; the 24 names: मूळ, विषय, प्रमुखता, लगेच नंतर येणे, अगदी लगेच नंतर येणे, एकत्र उत्पन्न होणे, परस्परता, आश्रय, प्रबळ आश्रय, आधी उत्पन्न होणे, नंतर उत्पन्न होणे, पुनरावृत्ती, कर्म, परिणाम, आहार, क्षमता, ध्यान, मार्ग, जोडलेले असणे, वेगळे असणे, अस्तित्व, अभाव, निघून जाणे, निघून न जाणे. Condition-kind labels are participles («एकत्र उत्पन्न होणारा»).
- anuloma / paccanīya (order) = होकारार्थी / नकारार्थी क्रम; anuloma as the cognitive moment = अनुरूपता. vatthu (physical base) = भौतिक स्थान.
- Dyad terms «स्वतः X असलेला / नसलेला», «Xचा विषय होणारा», «Xशी जोडलेला / Xपासून वेगळा»; dyad names «… घटनांचा दुहेरी गट», triad names «… इत्यादींचा तिहेरी गट»; gocchaka = गुच्छ.
- Inside one compound term join with «व» («X व Yही» for ceva … ca; contrastive «…नसलेला, पण …»); between separate terms or list items «आणि»; a comma between the two parts of a combined (dyad-triad, triad-dyad …) term; two objects of one postposition «A व B यांवर अवलंबून».
- Negated terms: an adjective + «नसलेला» (हितकारक नसलेला); «…असलेला» → «…नसलेला»; «न» before a participle; multi-member or already-negative terms quoted («“स्वतः मूळ नसलेले” नसलेला», inner quotes ‘…’).
- upādāna = धरून ठेवणे (pi-5 / pi-6, not pi-3's आसक्ती); kilesa term = «स्वतः क्लेश असलेला», noun = मनाचे क्लेश; cetasika dyad = «मनाचे सहचर असलेला»; sotadhātu = कानाचे तत्त्व.
- Variant readings in curly braces as the source: «{पाठभेद (Syā.): …}»; editorial queries kept as queries («{मुळाच्या आधारात आठ?}»).

### pi-1 additions (pi-1 run, 2026-11-15; full list in AI_translation/marathi/pi-1-pali-marathi-termbase-plain.md)
- Dhammasaṅgaṇī = घटनांची गणना; book end «“घटनांची गणना” ग्रंथ समाप्त.».
- Definition frame «त्या वेळी कोणता X असतो? त्या वेळी जो A, B, C – हा त्या वेळी असणारा X आहे.» (question word, pronoun and verb agree with X). Each Pāli synonym of a list keeps its own Marathi word; within one list no two synonyms share a word (bare mano in the citta list = अंतःकरण beside citta = मन; paṇḍaraṃ = निर्मळपणा; avitthanatā = मंदपणा नसणे).
- New factors: passaddhi प्रशांती, samatha शांती, paggāha उभारी, avikkhepa अविचलता, sampajañña स्पष्ट जाणीव, kammaññatā कामासाठी योग्यता; kāya- in kāyapassaddhi … = «मनाच्या सहचरांची» (the mental body); ekodibhāva मनाची एकरूपता.
- bhāveti = «Xची साधना करतो»; paṭipadā = वाटचाल; the jhāna clause «… प्राप्त करून राहतो»; bhūmi = टप्पा (stage of the path) / स्तर (plane); suññata / animitta / appaṇihita = शून्यतेची / चिन्हांचा अभाव असलेली / आकांक्षांचा अभाव असलेली.
- thina / middha = आळस / सुस्ती; rāga = आसक्ती, sārāga = अनुराग; abhijjhā = हव्यास; āghāta = चीड.
- nāma = मानसिक बाजू (nāmarūpa = मानसिक बाजू आणि भौतिक रूप); upacaya = वाढ; jarā = वार्धक्य; X-viññeyya rūpa = «Xच्या चेतनेने जाणता येणारे भौतिक रूप»; upādāna dyad term = «स्वतः धरून ठेवण्याचा प्रकार असलेला».

### pi-2 additions (pi-2 run, 2026-11-16; full list in AI_translation/marathi/pi-2-pali-marathi-termbase-plain.md)
- Vibhaṅga = विश्लेषण; chapter titles «X चे विश्लेषण» (परस्परावलंबी उत्पत्तीचे, किरकोळ बाबींचे, घटनांच्या गाभ्याचे विश्लेषण …); book end «“विश्लेषण” ग्रंथ समाप्त.».
- The three parts: सूत्रांनुसार विभागणी, अभिधम्मानुसार विभागणी, प्रश्नोत्तरे; suttanta frame «त्यांपैकी X म्हणजे काय? … – याला X म्हणतात»; «na vattabbā» = «Xला म्हणता येत नाही – …» (dative subject); siyā = «कधी …».
- Identical Pāli = pi-1's final Marathi (the Dhammasaṅgaṇī definitions and lists).
- The eleven qualifiers: भूतकाळातील / भविष्यकाळातील / वर्तमानकाळातील, स्वतःमधील / इतरांमधील (bahiddhā of nibbāna and the path's object = बाह्य), स्थूल / सूक्ष्म, हीन / उत्कृष्ट, दूर / जवळ.
- Dependent origination: the chain «Xमुळे Y»; jarā = वार्धक्य; the fourth truth «दुःखाच्या अंताकडे नेणारा मार्ग»; nirodha = अंत.
- ātāpī = उत्कट प्रयत्नशील (not तळमळ, which is lālappa); padhānasaṅkhāra = «निकराच्या प्रयत्नाची रचना»; tiracchānayoni = पशुयोनी; iriyāpatha = शरीराची स्थिती; manussarāhasseyyaka = माणसांच्या नजरेआड असलेले.
- Edition punctuation that misplaces quotation marks: keep the marks, translate the words by their meaning (the «na vattabbo – "A"ti, "B"» dyad lines).

## Verify (must pass)
```
python3 -I -X utf8 0-INBOX/temp/pipeline/check_chapter_ids.py <pali_split_dir> <marathi_split_dir> <ch>.md
python3 -I -X utf8 -c "import sys;f=lambda p:[l for l in open(p,encoding='utf-8').read().splitlines() if l.strip()];c=lambda t:t.count('—')+t.count('–');a,b=f(sys.argv[1]),f(sys.argv[2]);bad=[i for i,(x,y) in enumerate(zip(a,b)) if c(x)!=c(y)];print('lines',len(a),len(b),'dash-line mismatches',len(bad),bad[:5])" <pali_file> <marathi_file>
```
Both must pass: equal line counts and 0 dash mismatches. For a partial sample, compare against the same Pāli lines (e.g. write them to a scratch file first). Also check that no line ends a statement with "।".
