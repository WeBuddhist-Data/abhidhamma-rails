# Notes: pi-1 part 2-03 (Hindi plain zero-shot, lokuttara kusala)

Builder: build_2-03_hi.py (imports build_matika_hi.py and build_ch2_01_sample_hi.py; all sample names, strings and frames reused unchanged). Helpers: tb_lookup_2-03_hi.py, kwic_2-03_hi.py (read-only lookups).
Format: Pāli = Hindi, one per line.

## New factor names (gender for «होता/होती है»)
anaññātaññassāmītindriyaṃ = “जो अब तक नहीं जाना, उसे मैं जान लूँगा” की क्षमता (स्त्री.) (pi-5 ^5-21 verbatim)
aññindriyaṃ = पूर्ण ज्ञान की क्षमता (स्त्री.) (pi-5 ^5-21)
sammāvācā = सही वाणी (स्त्री.) (pi-5 ^5-106)
sammākammanto = सही कर्म (पुं.) (pi-5 ^5-106)
sammāājīvo = सही आजीविका (स्त्री.) (pi-5 ^5-106)
saṅkhārakkhandho = मानसिक रचनाओं का समूह (पुं.)

## New string pieces
maggaṅgaṃ maggapariyāpannaṃ = मार्ग का अंग, मार्ग में समाया हुआ
X-sambojjhaṅgo = X नामक जागृति का अंग (pi-5 satisambojjhaṅgo = सजगता नामक जागृति का अंग): pīti = उल्लास, samādhi = एकाग्रता, vīriya = उत्साह, sati = सजगता, dhammavicaya = परिघटनाओं की छानबीन, passaddhi = प्रशांति
catūhi vacīduccaritehi / tīhi kāyaduccaritehi / micchāājīvā ārati = वाणी के चार दुराचरणों / शरीर के तीन दुराचरणों / ग़लत आजीविका से दूर रहना
ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto = (…से) दूर रहना, विरत रहना, पूरी तरह विरत रहना, बचना, न करना, न अपनाना, दोष में न पड़ना, मर्यादा का उल्लंघन न करना, पुल को तोड़ देना
tesaṃ dhammānaṃ anaññātānaṃ adiṭṭhānaṃ appattānaṃ aviditānaṃ asacchikatānaṃ sacchikiriyāya = अब तक न जानी गई, न देखी गई, न पाई गई, न समझी गई और न प्रत्यक्ष अनुभव की गई उन परिघटनाओं के साक्षात्कार के लिए (frame: «<this> जो S है – यह उस समय X है।», like the life-faculty frame)
tesaṃ dhammānaṃ ñātānaṃ diṭṭhānaṃ pattānaṃ viditānaṃ sacchikatānaṃ sacchikiriyāya = जानी जा चुकी, देखी जा चुकी, पाई जा चुकी, समझी जा चुकी और प्रत्यक्ष अनुभव की जा चुकी उन परिघटनाओं के साक्षात्कार के लिए

## Frames that 2-01 also uses (fixed here independently; harmonise with the 2-01 builder if it differs)
Tasmiṃ kho pana samaye … = और उस समय …
cattāro khandhā honti, dvāyatanāni honti, dve dhātuyo honti, tayo āhārā honti, navindriyāni honti = चार समूह होते हैं, दो इंद्रिय-क्षेत्र होते हैं, दो तत्व होते हैं, तीन आहार होते हैं, नौ क्षमताएँ होती हैं
pañcaṅgikaṃ jhānaṃ hoti, aṭṭhaṅgiko maggo hoti = पाँच अंगों वाला ध्यान होता है, आठ अंगों वाला मार्ग होता है
satta balāni honti, tayo hetū honti = सात बल होते हैं, तीन मूल होते हैं
eko phasso hoti … ekaṃ cittaṃ hoti = एक संपर्क होता है … एक मन होता है
eko vedanākkhandho … viññāṇakkhandho hoti = एक अनुभूति का समूह … एक चेतना का समूह होता है
ekaṃ manāyatanaṃ / ekaṃ manindriyaṃ / ekā manoviññāṇadhātu hoti = एक मन का इंद्रिय-क्षेत्र होता है / एक मन की क्षमता होती है / एक मन की चेतना का तत्व होता है
ekaṃ dhammāyatanaṃ / ekā dhammadhātu hoti = एक मन के विषयों का इंद्रिय-क्षेत्र होता है / एक मन के विषयों का तत्व होता है
āhāra = आहार (pi-5)
Katamo tasmiṃ samaye saṅkhārakkhandho hoti? Phasso cetanā … = उस समय मानसिक रचनाओं का समूह क्या है? संपर्क, इरादा, …
ye vā pana … arūpino dhammā ṭhapetvā vedanākkhandhaṃ ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ – ayaṃ tasmiṃ samaye saṅkhārakkhandho hoti = या उस समय जो भी दूसरी परस्पर-आश्रित रूप से उत्पन्न अभौतिक परिघटनाएँ होती हैं, अनुभूति के समूह को छोड़कर, पहचान के समूह को छोड़कर, चेतना के समूह को छोड़कर – यह उस समय मानसिक रचनाओं का समूह है
…pe… ime dhammā kusalā. = … ये हितकर परिघटनाएँ हैं।
ime dhammā kusalā…pe…. = ये हितकर परिघटनाएँ हैं…।
tasmiṃ samaye phasso hoti…pe… avikkhepo hoti…pe… ime dhammā kusalā. = उस समय संपर्क होता है… भटकाव का अभाव होता है… ये हितकर परिघटनाएँ हैं।
vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati = इंद्रिय-सुखों से अलग होकर… पहले ध्यान को प्राप्त करके उसमें रहता है (pi-4 ^4-198 wording)
vitakkavicārānaṃ vūpasamā…pe… dutiyaṃ jhānaṃ…pe… pañcamaṃ jhānaṃ upasampajja viharati = आरंभिक विचार और सतत विचार के शांत होने से… दूसरे ध्यान को… पाँचवें ध्यान को प्राप्त करके उसमें रहता है (pi-4 ^4-198 wording)
dukkhapaṭipadaṃ dandhābhiññaṃ (khippābhiññaṃ; sukhapaṭipadaṃ …), after the absorption = जो ध्यान दुःखद प्रगति और धीमे (शीघ्र) उच्च ज्ञान वाला है (सुखद प्रगति …); several in a row: «जो ध्यान A… B… C… D है»
paṭipadā = प्रगति (terms file: Catasso paṭipadā = प्रगति के चार ढंग); abhiññā = उच्च ज्ञान (pi-4/5); dandha / khippa = धीमा / शीघ्र
chanda- / vīriya- / citta- / vīmaṃsādhipateyyaṃ = चाह / उत्साह / मन / जाँच-परख की प्रधानता वाला (matrix maggādhipatino = मार्ग की प्रधानता वाली; vīmaṃsā = जाँच-परख, pi-5; chanda = चाह, terms file, not pi-5 इच्छा)

## New in 2-03
Yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti = जिस समय कोई लोकोत्तर ध्यान का अभ्यास करता है (bhāveti = का अभ्यास करता है, as bhāvanā = मानसिक अभ्यास)
niyyānikaṃ apacayagāmiṃ = जो मुक्ति की ओर ले जाने वाला और संचय घटाने की ओर ले जाने वाला है (matrix wording, built from M.BARE)
diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā = दृष्टियों में फँसने को छोड़ने के लिए, पहले चरण की प्राप्ति के लिए (diṭṭhigata = दृष्टियों में फँसना, pi-5; bhūmi = चरण)
kāmarāgabyāpādānaṃ tanubhāvāya dutiyāya bhūmiyā pattiyā = इंद्रिय-सुखों के राग और दुर्भावना को क्षीण करने के लिए, दूसरे चरण की प्राप्ति के लिए (pi-5 kāmarāga; pi-4 tanubhāvāya)
kāmarāgabyāpādānaṃ anavasesappahānāya tatiyāya bhūmiyā pattiyā = इंद्रिय-सुखों के राग और दुर्भावना को पूरी तरह छोड़ने के लिए, तीसरे चरण की प्राप्ति के लिए
rūparāgaarūparāgamānauddhaccaavijjāya anavasesappahānāya catutthāya bhūmiyā pattiyā = सूक्ष्म भौतिक लोक के राग, अभौतिक लोक के राग, अहंकार, बेचैनी और अज्ञान को पूरी तरह छोड़ने के लिए, चौथे चरण की प्राप्ति के लिए (māna = अहंकार, pi-4)
suññataṃ / appaṇihitaṃ (qualifying the absorption) = शून्य / इच्छा-रहित (pi-5 appaṇihito = इच्छा-रहित)
lokuttaraṃ maggaṃ / satipaṭṭhānaṃ / sammappadhānaṃ / iddhipādaṃ / indriyaṃ / balaṃ / bojjhaṅgaṃ / saccaṃ / samathaṃ / dhammaṃ / khandhaṃ / āyatanaṃ / dhātuṃ / āhāraṃ / phassaṃ / vedanaṃ / saññaṃ / cetanaṃ / cittaṃ bhāveti = लोकोत्तर मार्ग / सजगता के आधार / सही प्रयास / सिद्धि के आधार / क्षमता / बल / जागृति के अंग / सत्य / शांति / परिघटना / समूह / इंद्रिय-क्षेत्र / तत्व / आहार / संपर्क / अनुभूति / पहचान / इरादे / मन का अभ्यास करता है (pi-5 ^5-348 for satipaṭṭhāna, sammappadhāna, iddhipāda)
#### Lokuttarakusalaṃ = #### लोकोत्तर हितकर मन (terms file)
Suddhikapaṭipadā (heading / closing) = केवल प्रगति के ढंग
Suññataṃ (heading / closing) = शून्यता
Suññatamūlakapaṭipadā = शून्यता पर आधारित प्रगति के ढंग
Appaṇihitaṃ = इच्छाओं का अभाव (pi-5 appaṇihita)
Appaṇihitamūlakapaṭipadā = इच्छाओं के अभाव पर आधारित प्रगति के ढंग
Vīsati mahānayā = बीस मुख्य विधियाँ (terms file); Adhipati = प्रधानता (terms file)
Paṭhamo / Dutiyo / Tatiyo / Catuttho maggo. = पहला / दूसरा / तीसरा / चौथा मार्ग।
Lokuttaraṃ cittaṃ. = लोकोत्तर मन।

## Choices to review
- sammappadhāna = सही प्रयास, as pi-5 ^5-348; it coincides with sammāvāyāma = सही प्रयास (terms file: padhāna and vāyāma both प्रयास). The English splits them (right striving / right effort). If they must differ in Hindi, change TWENTY[2] in the builder.
- dukkha/sukha paṭipadā = दुःखद / सुखद प्रगति (literal, like the feeling terms). «कठिन / सुगम प्रगति» would be a commentarial reading.
- setughāto = पुल को तोड़ देना (literal, as the English 'destroying the causeway'); velāanatikkamo = मर्यादा का उल्लंघन न करना; anajjhāpatti = दोष में न पड़ना (āpatti = दोष, terms file).
- The qualifiers of the absorption stand in a relative clause after «उसमें रहता है»: «…, जो ध्यान … है, उस समय …» (Pāli order kept).

## Source notes (translated as written)
- ^1-364: «maggapariyāpannaṃ, idaṃ tasmiṃ samaye aññindriyaṃ hoti» has a comma where every other answer has « – »; the Hindi keeps the comma («… है, यह उस समय पूर्ण ज्ञान की क्षमता है…»).
- ^1-314: the lokuttara non-delusion answer lacks «amoho kusalamūlaṃ» (unlike ^1-34); nothing added.
- ^1-342, ^1-359: stray spaces before «…pe…» («vūpasamā …pe…», «paṭhamaṃ jhānaṃ …pe…»); rendered like the other lines.
