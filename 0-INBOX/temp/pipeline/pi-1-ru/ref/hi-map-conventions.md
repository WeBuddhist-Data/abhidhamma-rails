# pi-1 Pāli→Hindi keyword map: conventions settled on the sample (preamble, 1-matika, 2-01)

Read with `..\hi-mapper-brief.md`. These are the decisions the sample applied; map the other parts the same way so one Pāli word in one sense gets one Hindi value across the book. Examples are taken from the sample's `*.mapped.md` files.

## Tooling (reuse it)
- `map_common_hi.py` (importing it writes nothing):
  - `read_keywords(part)`, `read_hindi(part)`, `read_pali(part)`.
  - `present(value, text)` checks presence. It tolerates regular inflection (परिघटना ~ परिघटनाएँ/परिघटनाओं, जुड़ा ~ जुड़ी, का/की/के, है/हैं, गया/गए, हुआ/हुई, -ना ~ -ता/-ने), ignores commas and variant brackets, and lets a dropped «न» sit between two words (उथला होना ~ «उथला न होना»).
  - `CH2` + `ch2_value(kw, kws)`: the default table for the cittuppāda chapters, with its context rules.
  - `build_part(part, resolver)` writes `<part>.mapped.md`. It stops on any unmapped keyword and refuses a ", " inside a value.
  - `verify(part)`: the brief's check plus the presence check.
  - `matrix_names()`: Pāli matrix keyword → Hindi, as settled in 1-matika.
- Pattern for a part script (see `map_2-01_hi.py`): `resolver = OVERRIDES[bid][kw]`, falling back to your own table, then to `ch2_value`. Extend `CH2` only in your own script (`table = {**CH2, ...}`; `ch2_value(kw, kws, table)`). Do not edit `map_common_hi.py`; the other agents import it at the same time.
- Lookup is case-insensitive on the first letter only (Vedanā, Phasso, Mana, Saddhindriyaṃ, Koṭṭhāsa use the lower-case entry).

## Value form
- Nouns: direct case, **singular**, including `dhammā` = **परिघटना**. So kusalā dhammā / dhammā kusalā = हितकर परिघटना, arūpino dhammā = अभौतिक परिघटना, akusalānaṃ dhammānaṃ = हानिकर परिघटना, indriyāni = क्षमता, balāni = बल, āhārā = आहार, dhātuyo = तत्व, khandhā = समूह.
  - Fixed plural-concept terms keep their fixed form: āsava = मन के मैल, kilesa = मन के क्लेश, saṅkhāra = मानसिक रचनाएँ, duka/dukaṃ = दो-दो के वर्गीकरण.
  - A genitive inside a term stays as the term has it: dhammavicayo = परिघटनाओं की छानबीन, dhammāyatanaṃ = मन के विषयों का इंद्रिय-क्षेत्र, mittatā = मित्रों की संगति.
- Adjectives and participles: masculine direct singular. sampayuttā = जुड़ा, vippayuttā = अलग, pahātabbā = छोड़ा जाने वाला, saṃyojaniyā = बंधनों का विषय बनने वाला, sahagatā = के साथ होने वाला, ārammaṇā (in X-ārammaṇā) = विषय वाला, pāpakānaṃ = बुरा.
  - In a phrase with `dhammā`, the Hindi agrees with परिघटना: sahagatā dhammā = के साथ होने वाली परिघटना, vipākadhammadhammā = कर्म-फल उत्पन्न करने वाली परिघटना.
- Verbs: the infinitive (sahagataṃ = के साथ होना, ārabbha = विषय बनाना, phusanā = छूना, ottappati = डरना, hirīyati = लज्जा आना), or the participle the text uses when the infinitive does not fit (niṭṭhitā = पूरा हुआ, ṭhapetvā = छोड़कर, uppannaṃ = उत्पन्न).
- Discontinuous Hindi: join the parts with " … ": samaye phasso = उस समय … संपर्क, antaradukaṃ = बीच के … दो-दो के वर्गीकरण (the Hindi has «बीच के छोटे दो-दो के वर्गीकरण»).
- Never ", " inside a value. Drop the comma: adukkhamasukhaṃ = न दुःखद न सुखद (text «न दुःखद, न सुखद»). The sample needed no " / ".
- The sample has 0 (no direct equivalent). Use it for a particle with no Hindi word, or a word that only survives inside a variant bracket kept in Pāli.

## Compounds and their members
Map the whole compound to the whole Hindi phrase, and each member to the Hindi part that renders it:
- cittamudutā = मन की मृदुता, mudutā = मृदुता, citta = मन
- somanassasahagataṃ = प्रसन्नता के साथ होना, somanassa = प्रसन्नता, sahagataṃ = के साथ होना
- ñāṇavippayuttaṃ = ज्ञान से अलग, ñāṇa = ज्ञान
- kāmāvacaraṃ = इंद्रिय-सुखों के लोक से संबंधित, kāma = इंद्रिय-सुख, avacaraṃ = लोक से संबंधित (rūpāvacarā = सूक्ष्म भौतिक लोक से संबंधित, arūpāvacarā = अभौतिक लोक से संबंधित)
- paṭiccasamuppannā arūpino = परस्पर-आश्रित रूप से उत्पन्न अभौतिक, paṭicca = परस्पर-आश्रित, samuppannā = उत्पन्न, samuppannā arūpino dhammā = उत्पन्न अभौतिक परिघटना
- manoviññāṇadhātu = मन की चेतना का तत्व, manoviññāṇa = मन की चेतना, dhātu = तत्व, tajjā = उसके अनुरूप; samphassajaṃ = संपर्क से उत्पन्न; cetosamphassajaṃ/-jā = मन के संपर्क से उत्पन्न
- vedanākkhandho / -khandhaṃ / -khandhassa = अनुभूति का समूह (likewise saññā- पहचान का समूह, saṅkhāra- मानसिक रचनाओं का समूह, viññāṇa- चेतना का समूह), khandho / khandhā / khandhassa = समूह
- paññāsatthaṃ = प्रज्ञा रूपी शस्त्र, satthaṃ = शस्त्र (same for pāsādo महल, āloko आलोक, obhāso आभा, pajjoto दीपक, ratanaṃ रत्न)
- kusalamūlaṃ = हितकर मूल, mūlaṃ = मूल, kusala = हितकर
- dhamma as the stem of dhammārammaṇa = मन का विषय. In a segment that also has dhammāyatanaṃ or dhammadhātu it is मन के विषय. `ch2_value` applies this rule.
- kāya (of kāyapassaddhi, kāyalahutā, …) = मानसिक काया; citta / cittassa / cetaso / mānasatā = मन; mana = मन.
- mano: मानस in the citta string; मानसिक where the segment has manosañcetanā (manosañcetanāhāro = मानसिक इरादा रूपी आहार). sañcetanā: इरादा करना in the cetanā string; इरादा where it only occurs inside manosañcetanā.
- ṭhiti: स्थिरता in the samādhi string (cittassa ṭhiti = मन की स्थिरता); टिके रहना in the jīvitindriya string (a segment with āyu).
- cetasikaṃ: मानसिक (cetasikaṃ sātaṃ = मानसिक सुहावनापन); मानसिक भाव in the upekkhā string «cetasikaṃ neva sātaṃ nāsātaṃ» (a segment with adukkhamasukhaṃ).
- Matrix fragments: uttarā (of lokuttarā) = लोकोत्तर; raṇā (of saraṇā/araṇā) = संघर्ष; antara = बीच का; pathā = मार्ग; upamā = जैसा; Piṭṭhi = अंतिम; Suttantika = उपदेश.

## Fragments that lost a negative prefix: the positive part
pilāpanatā = उथला होना, sammussanatā = भूल जाना, nikkhitta = छोड़ना, lubbhanā = लोभ करना, sārajjanā = राग करना, dussanā = द्वेष करना, byāpajjo = दुर्भावना रखना (abyāpajjo = दुर्भावना न रखना), kakkhaḷatā = कठोरता, kathinatā = कड़ापन, dandhanatā = सुस्ती, vitthanatā = जड़ता, jimhatā = टेढ़ापन, vaṅkatā = वक्रता, kuṭilatā = कुटिलता, mattaññutā = मात्रा का ज्ञान, gutta = रक्षा करना, vacassatā = सलाह मानने की प्रवृत्ति, santuṭṭhitā = संतुष्ट होना. A fragment that keeps its a- maps with the negative: avisāhaṭa = न बिखरा, asithila = ढीला न पड़ने वाला.

## Factor names (cittuppāda; the `CH2` table holds them all)
phasso संपर्क · vedanā अनुभूति · saññā पहचान · cetanā इरादा · cittaṃ मन · vitakko आरंभिक विचार · vicāro सतत विचार · pīti उल्लास · sukhaṃ सुख · upekkhā समभाव · cittassekaggatā मन की एकाग्रता (ekaggatā एकाग्रता) · saddhindriyaṃ श्रद्धा की क्षमता · vīriyindriyaṃ उत्साह की क्षमता · satindriyaṃ सजगता की क्षमता · samādhindriyaṃ एकाग्रता की क्षमता · paññindriyaṃ प्रज्ञा की क्षमता · manindriyaṃ मन की क्षमता · somanassindriyaṃ प्रसन्नता की क्षमता · upekkhindriyaṃ समभाव की क्षमता · jīvitindriyaṃ जीवन-क्षमता (indriyaṃ क्षमता) · sammā सही (sammādiṭṭhi → sammā सही + diṭṭhi दृष्टि; saṅkappo संकल्प; vāyāmo प्रयास; sati सजगता; samādhi एकाग्रता) · X-balaṃ = X का बल (saddhā श्रद्धा, vīriya उत्साह, sati सजगता, samādhi एकाग्रता, paññā प्रज्ञा, hiri लज्जा का बल, ottappa बुराई के डर का बल; balaṃ बल) · alobho लोभ का अभाव · adoso द्वेष का अभाव · amoho मोह का अभाव · anabhijjhā लालच का अभाव · abyāpādo दुर्भावना का अभाव · hirī लज्जा · ottappaṃ बुराई का डर · passaddhi प्रशांति · lahutā हल्कापन · mudutā मृदुता · kammaññatā कार्य-योग्यता · pāguññatā दक्षता · ujukatā सीधापन · sampajaññaṃ स्पष्ट समझ · samatho शांति · vipassanā अंतर्दृष्टि · paggāho तत्परता · avikkhepo भटकाव का अभाव. Summaries: jhānaṃ ध्यान, maggo मार्ग, pañcaṅgikaṃ/-ko पाँच अंगों वाला, caturaṅgikaṃ/-ko चार अंगों वाला, hetū मूल, āyatanāni इंद्रिय-क्षेत्र, āhāro/āhārā आहार, ñāṇa ज्ञान, saṅkhārena (sasaṅkhārena) प्रेरणा.

## Synonym strings
Each word maps to its own item in the fixed Hindi string, never to the whole string. Examples:
- phasso संपर्क, phusanā छूना, saṃphusanā भली-भाँति छूना
- saññā पहचान, sañjānanā पहचानना, sañjānitattaṃ पहचान चुका होना; cetanā इरादा, sañcetanā इरादा करना, cetayitattaṃ इरादा कर चुका होना
- citta string: cittaṃ मन, mano मानस, mānasaṃ मानसिक क्रिया, hadayaṃ हृदय, paṇḍaraṃ उज्ज्वलता, manāyatanaṃ मन का इंद्रिय-क्षेत्र, viññāṇaṃ चेतना, viññāṇakkhandho चेतना का समूह
- vitakka string: takko सोचना, saṅkappo संकल्प, appanā टिकाना, abhiniropanā विषय की ओर ले जाना, cetaso मन. vicāra string: cāro विचरण, anusandhānatā विषय से जुड़े रहना, anupekkhanatā लगातार निहारते रहना
- pīti string: pāmojjaṃ आनंद, āmodanā आनंदित होना, pamodanā प्रमुदित होना, hāso हर्ष, pahāso महाहर्ष, vitti तृप्ति, odagyaṃ उमंग, attamanatā खिल उठना
- vīriya string: cetasiko vīriyārambho मानसिक रूप से उत्साह जगाना (cetasiko मानसिक, ārambho जगाना), nikkamo आगे बढ़ना, parakkamo प्रयत्न, uyyāmo उद्यम, ussāho जोश, ussoḷhī लगन, thāmo शक्ति, dhiti धैर्य, chandatā चाह, dhuratā भार, sampaggāho दृढ़ता से उठाए रखना
- sati string: anussati बार-बार स्मरण, paṭissati पुनः स्मरण, saraṇatā याद रखना, dhāraṇatā धारण करना
- paññā string: pajānanā जानना, vicayo छानबीन, pavicayo गहरी छानबीन, sallakkhaṇā पहचानना, upalakkhaṇā भली-भाँति पहचानना, paccupalakkhaṇā हर पहलू को पहचानना, paṇḍiccaṃ पांडित्य, kosallaṃ कुशलता, nepuññaṃ निपुणता, vebhabyā विवेक, cintā चिंतन, upaparikkhā परख, bhūrī व्यापक बुद्धि, medhā मेधा, pariṇāyikā मार्गदर्शक बुद्धि, patodo अंकुश
- jīvita string: āyu आयु, ṭhiti टिके रहना, yapanā चलते रहना, yāpanā चलाए रखना, iriyanā गतिशील रहना, vattanā बने रहना, pālanā पालन, jīvita जीवन
- feeling string: sātaṃ सुहावना, asātaṃ असुहावना, sukhaṃ सुख, sukhā सुखद, vedayitaṃ अनुभव, sukhaṃ vedayitaṃ सुखद अनुभव, sukhā vedanā सुखद अनुभूति
- In an abbreviated segment («प्रज्ञा, जानना… मोह का अभाव»), map only the keywords listed. They are all still in the Hindi.

## Question frames, relatives, particles
- `Yo / Yā / Yaṃ / ye / Ye` = जो. `yaṃ yaṃ` (yaṃ yaṃ vā panārabbha) = जिस किसी.
- `samaye X` (from «Yo/Yā/Yaṃ tasmiṃ samaye X …») = **उस समय … X**, always with " … ", even where the question has «उस समय X क्या है?». Examples: samaye cittaṃ = उस समय … मन, samaye takko = उस समय … सोचना, samaye cetasikaṃ = उस समय … मानसिक. A bare `samaye` (2-03) = उस समय.
- The sample's keyword lists had no Katame/Katamo/ime/ayaṃ/idaṃ. If they occur: Katame (Katame dhammā kusalā? = «हितकर परिघटनाएँ कौन-सी हैं?») = कौन-सा. Katamo/Katamā/Katamaṃ in «Katamo tasmiṃ samaye X hoti?» = «उस समय X क्या है?» = क्या. ime = ये, ayaṃ/idaṃ = यह.
- hoti / honti: the verb the segment's Hindi uses (होना). Use (no direct equivalent) only if the Hindi has no verb there. Multiword keywords with hoti map to the whole Hindi clause, with " … " for gaps (cf. pi-4 «vuccati puggalo=व्यक्ति … कहा जाता है»).
- na / no (negation) = न (1-M2-13 na = न). Use नहीं where the Hindi has नहीं. neva … na = न … न.
- eva / -meva: ही where the Hindi has ही (e.g. «वे ही»), otherwise (no direct equivalent). For X-meva (3-01) map to the Hindi of X. vivicceva = अलग होकर (eva unrendered), vivicceva kāmehi = इंद्रिय-सुखों से अलग होकर (builder VIVEKA).
- ceva … ca pairs (ganthā ceva ganthaniyā, 4-0x / 5): the matrix pair, e.g. «गाँठ रूपी भी और गाँठों का विषय बनने वाली भी» → ganthā ceva ganthaniyā = गाँठ रूपी भी और गाँठों का विषय बनने वाला भी (check the segment's actual Hindi).

## Matrix item names (1-matika; full table: `matrix_names()`)
- mātikā: मूल सूची where the Hindi says so (1-M-0, Mātikā niṭṭhitā). Otherwise सूची, in the sub-list titles «तीन-तीन / दो-दो के वर्गीकरणों की सूची» and Tikamātikā at the end of 1-M1-22.
- Core: kusalā dhammā हितकर परिघटना, akusalā हानिकर, abyākatā नैतिक रूप से अनिर्धारित; vipākadhamma कर्म-फल उत्पन्न करने वाला; upādiṇṇa कर्म से उत्पन्न, upādāniyā आसक्ति का विषय बनने वाला; saṃkiliṭṭha क्लेशों से मलिन, saṃkilesikā क्लेशों की ओर ले जाने वाला; dassanena सत्य-दर्शन, bhāvanāya pahātabbā मानसिक अभ्यास से छोड़ा जाने वाला; hetukā (pahātabbahetukā) मूलों वाला; ācaya संचय, apacaya संचय घटाना, gāmino dhammā की ओर ले जाने वाली परिघटना; sekkhā सीखने के चरण का, asekkhā सीखना पूरा होने के चरण का; paritta सीमित, mahaggata उन्नत, appamāṇa अपरिमित; hīna हीन, majjhima मध्यम, paṇīta उत्तम; micchatta ग़लत दिशा, sammatta सही दिशा, niyatā निश्चित; magga मार्ग, adhipatino प्रधानता वाला; uppannā उत्पन्न हो चुका, uppādino उत्पन्न होने वाला; atīta अतीत, anāgata भविष्य, paccuppanna वर्तमान; bahiddhā दूसरों से संबंधित; sanidassana दिखाई देने वाला, anidassana दिखाई न देने वाला, sappaṭighā टकराव वाला.
- Clusters (gocchaka): X = the term (āsava मन के मैल, saṃyojana बंधन, gantha गाँठ, ogha बाढ़, yoga जकड़न, nīvaraṇa बाधा, parāmāsa ग़लत धारणा, upādāna आसक्ति, kilesa मन के क्लेश / क्लेश); X-niyā (sāsavā, parāmaṭṭhā) = «Xों का विषय बनने वाला»; X-vippayuttā = «Xों से अलग»; in the closing pair («X-vippayuttā kho pana dhammā X-niyāpi / aX-niyāpi»), X-niyā = उनका (उसका for parāmāsa, upādāna) विषय बनने वाला.
- Intermediate pairs: sappaccayā कारणों पर निर्भर, saṅkhatā निर्मित, asaṅkhatā अनिर्मित, rūpino भौतिक, arūpino अभौतिक, lokiyā लौकिक, lokuttarā लोकोत्तर, viññeyyā जाना जा सकने वाला; sārammaṇā विषय वाला, cittā मन, cetasikā मन का सहचर, cittasaṃsaṭṭhā मन से घुला-मिला, cittasamuṭṭhānā मन से उत्पन्न, cittasahabhuno मन के साथ-साथ होने वाला, cittānuparivattino मन का अनुसरण करने वाला, ajjhattikā आंतरिक, bāhirā बाह्य, upādā व्युत्पन्न; kāmāvacarā इंद्रिय-सुखों के लोक से संबंधित, pariyāpannā अस्तित्व के लोकों में समाई हुई (परिघटना), niyyānikā मुक्ति की ओर ले जाने वाला, sauttarā सर्वोच्च न होने वाला, anuttarā सर्वोच्च, saraṇā संघर्ष वाली (परिघटना).
- Suttanta pairs: vijjā विद्या, avijjā अज्ञान, nāma मानसिक पक्ष, rūpa भौतिक रूप, bhava अस्तित्व, vibhava अनस्तित्व, sassata शाश्वतता, uccheda विनाश, diṭṭhi दृष्टि, ahirika निर्लज्जता, anottappa बुराई के प्रति निडरता, hirī लज्जा, ottappa बुराई का डर, dovacassatā सलाह न मानने की प्रवृत्ति, kusalatā कुशलता, āpatti दोष, samāpatti ध्यान-अवस्था, sīla सदाचार, vipatti विफलता, sampadā संपन्नता, visuddhi शुद्धि, padhāna प्रयास, samatha शांति, paggāha तत्परता, nimitta चिह्न, khaye ñāṇaṃ = क्षय + ज्ञान, anuppāde = उत्पन्न न होना.

## Headings and colophons (2-01)
Cittuppāda = मन की उत्पत्ति, kaṇḍaṃ = अध्याय, bhājanī/bhājanīyaṃ = विश्लेषण, Koṭṭhāsa = भाग, Suññata = शून्यता, vāro = खंड, bhāṇa = पाठ (bhāṇavāro = पाठ-खंड). Ordinals use the masculine direct form: Pañcamaṃ पाँचवाँ, Chaṭṭhaṃ छठा, Sattamaṃ सातवाँ, Aṭṭhamaṃ आठवाँ. cittāni (… kusalacittāni) = मन.
