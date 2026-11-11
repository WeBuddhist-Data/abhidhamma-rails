# Notes: pi-1 part 2-05 (Hindi plain zero-shot, ^1-505 … ^1-582: lokuttara vipāka, akusala vipāka, kiriyā)

Builder: build_2-05_hi.py (imports build_matika_hi.py and build_ch2_01_sample_hi.py; mirrors pi-1-en/build_2-05.py: each line is split at «…pe…» and every chunk is translated by fixed rules, so the same Pāli chunk always gives the same Hindi). Helper: tb_lookup_2-05_hi.py + tb_pats_2-05_hi.txt (read-only termbase lookup).
Strings shared with other chapter-2 parts are copied byte-for-byte from build_2-03_hi.py (lokuttara clause), build_2-04_hi.py (vipāka frames) and build_2-01_2-02_hi.py (sasaṅkhārena, arūpa, kasiṇa), per the coordinator's note; they are marked [2-03] / [2-04] / [2-01_2-02 PH] in the builder.
Format: Pāli = Hindi, one per line.

## Frames
Katame dhammā abyākatā? = नैतिक रूप से अनिर्धारित परिघटनाएँ कौन-सी हैं? (M.QUESTION)
ime dhammā abyākatā = ये नैतिक रूप से अनिर्धारित परिघटनाएँ हैं (M.ANSWER_BARE)
ye vā pana … – ime dhammā abyākatā = या उस समय जो भी दूसरी परस्पर-आश्रित रूप से उत्पन्न अभौतिक परिघटनाएँ होती हैं – ये नैतिक रूप से अनिर्धारित परिघटनाएँ हैं (C.YEVAPANA)
…pe…. (at the end) = …।
Tasmiṃ kho pana samaye cattāro khandhā honti, dvāyatanāni honti, dve dhātuyo honti, tayo āhārā honti, tīṇindriyāni (pañcindriyāni) honti, eko phasso hoti = और उस समय चार समूह होते हैं, दो इंद्रिय-क्षेत्र होते हैं, दो तत्व होते हैं, तीन आहार होते हैं, तीन (पाँच) क्षमताएँ होती हैं, एक संपर्क होता है
ekā kāyaviññāṇadhātu / manodhātu / manoviññāṇadhātu hoti, ekaṃ dhammāyatanaṃ hoti, ekā dhammadhātu hoti = एक शरीर की चेतना का / मन का / मन की चेतना का तत्व होता है, एक मन के विषयों का इंद्रिय-क्षेत्र होता है, एक मन के विषयों का तत्व होता है
Katamo tasmiṃ samaye saṅkhārakkhandho hoti? Phasso cetanā … ; ye vā pana … ṭhapetvā vedanākkhandhaṃ ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ – ayaṃ … = उस समय मानसिक रचनाओं का समूह क्या है? संपर्क, इरादा, …; या उस समय जो भी … होती हैं, अनुभूति के समूह को छोड़कर, पहचान के समूह को छोड़कर, चेतना के समूह को छोड़कर – यह उस समय मानसिक रचनाओं का समूह है
alobho / adoso / amoho abyākatamūlaṃ = लोभ / द्वेष / मोह का अभाव, नैतिक रूप से अनिर्धारित मूल

## New factor names
dukkhaṃ = दुःख (पुं.); dukkhindriyaṃ = दुःख की क्षमता (स्त्री., pi-3)
upekkhā = समभाव (पुं.); upekkhindriyaṃ = समभाव की क्षमता (स्त्री., pi-3)
aññindriyaṃ = पूर्ण ज्ञान की क्षमता (स्त्री.)
aññātāvindriyaṃ = पूर्ण ज्ञान पा चुके व्यक्ति की क्षमता (स्त्री., pi-3 / pi-5)
saṅkhārakkhandho = मानसिक रचनाओं का समूह (पुं.)

## Strings
kāyikaṃ asātaṃ kāyikaṃ dukkhaṃ kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ kāyasamphassajā asātā dukkhā vedanā = शारीरिक असुहावनापन, शारीरिक दुःख, शरीर के संपर्क से उत्पन्न असुहावना, दुःखद अनुभव, शरीर के संपर्क से उत्पन्न असुहावनी, दुःखद अनुभूति (asāta = असुहावना, as 2-01/2-04)
tajjākāyaviññāṇadhātusamphassajaṃ = उसके अनुरूप शरीर की चेतना के तत्व के संपर्क से उत्पन्न
samādhi / vīriya string without sammāsamādhi / sammāvāyāmo (functional mind) = the sample strings without «, सही एकाग्रता» / «, सही प्रयास»
Yā tesaṃ aññātāvīnaṃ dhammānaṃ aññā S … = उन पूर्ण ज्ञान पा चुकी परिघटनाओं की जो पूर्ण ज्ञान, S, … है
dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ = परिघटनाओं की छानबीन नामक जागृति का अंग, मार्ग का अंग, मार्ग में समाया हुआ (as 2-03)

## World-transcending results (kusala clause = build_2-03_hi.py)
Yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ = जिस समय कोई लोकोत्तर ध्यान का अभ्यास करता है, जो मुक्ति की ओर ले जाने वाला और संचय घटाने की ओर ले जाने वाला है, और …
diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā = दृष्टियों में फँसने को छोड़ने के लिए, पहले चरण की प्राप्ति के लिए (stages 2–4 as 2-03)
vivicceva kāmehi / vitakkavicārānaṃ vūpasamā = इंद्रिय-सुखों से अलग होकर / आरंभिक विचार और सतत विचार के शांत होने से
X jhānaṃ upasampajja viharati / X jhānaṃ = X ध्यान को प्राप्त करके उसमें रहता है / X ध्यान को
qualifiers after the absorption = «जो ध्यान … है»; a run of unlabelled qualifier chunks shares one «जो ध्यान» and one «है» (as 2-03 «जो ध्यान A… B… C है»); two in one chunk joined «A और B», three «A, B और C»
dukkhapaṭipadaṃ dandhābhiññaṃ (…) = दुःखद प्रगति और धीमे (शीघ्र) उच्च ज्ञान वाला (सुखद प्रगति …) (as 2-03)
suññataṃ / animittaṃ / appaṇihitaṃ = शून्य / चिह्नों से रहित (pi-5 animitto) / इच्छा-रहित
chanda- / vīriya- / citta- / vīmaṃsādhipateyyaṃ = चाह / उत्साह / मन / जाँच-परख की प्रधानता वाला (as 2-03)
…nti kusalaṃ / …nti vipāko = … (हितकर) / … (कर्म-फल)
Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ = उसी लोकोत्तर हितकर ध्यान के किए जाने और अभ्यास किए जाने के कारण, उसके फल के रूप में, जब वह … (cf. 2-04 RES_OF «… उसके फल के रूप में, जब वह»)
lokuttaraṃ X bhāveti (twenty methods) = लोकोत्तर X का अभ्यास करता है (list as 2-03)

## Unwholesome results and functional minds
akusalassa kammassa katattā upacitattā vipākaṃ/vipākā X uppannaṃ/uppannā hoti = जिस समय हानिकर कर्म के किए जाने और संचित होने के कारण कर्म-फल रूपी X उत्पन्न होता/होती है (pattern of 2-04 RES_KAMA)
upekkhāsahagataṃ rūpārammaṇaṃ (a viññāṇa) = जो समभाव के साथ होती है, जिसका विषय दृश्य रूप है (2-04 F_ACC / OBJ); dukkhasahagataṃ = जो दुःख के साथ होती है
upekkhāsahagatā / somanassasahagatā (an element) = जो समभाव / प्रसन्नता के साथ होता है
kiriyā (kiriyaṃ) neva kusalā nākusalā na ca kammavipākā = जो केवल क्रिया रूपी है, न हितकर, न हानिकर और न कर्म-फल
sasaṅkhārena = जो प्रेरणा के साथ उत्पन्न होता है (own clause, as 2-01/2-02)
rūpāvacaraṃ / arūpāvacaraṃ jhānaṃ bhāveti = कोई सूक्ष्म भौतिक / अभौतिक लोक से संबंधित ध्यान का अभ्यास करता है
diṭṭhadhammasukhavihāraṃ = इसी जीवन में सुख से रहने के लिए (pi-5)
pathavīkasiṇaṃ = पृथ्वी के ध्यान-मंडल को आधार बनाकर (as 2-01/2-02, 2-04)
arūpa formulas and sukhassa ca pahānā = as build_2-01_2-02_hi.py PH (… पूरी तरह पार कर जाने से …; सुख के त्याग से)

## Headings and closing lines
#### Lokuttaravipāka-paṭhamamaggavipākā / Akusalavipākaabyākataṃ / Ahetukakiriyāabyākataṃ = terms file verbatim
Suddhikapaṭipadā = केवल प्रगति के ढंग (as 2-03); Suddhikasuññataṃ = केवल शून्यता; Suññatapaṭipadā = शून्यता के साथ प्रगति के ढंग; Suddhikaappaṇihitaṃ = केवल इच्छाओं का अभाव; Appaṇihitapaṭipadā = इच्छाओं के अभाव के साथ प्रगति के ढंग; Vīsati mahānayā = बीस मुख्य विधियाँ; Chandādhipateyyasuddhikapaṭipadā = चाह की प्रधानता के साथ केवल प्रगति के ढंग; Chandādhipateyyasuddhikasuññatā = चाह की प्रधानता के साथ केवल शून्यता
Paṭhamamaggavipāko. = पहले मार्ग का कर्म-फल।; Dutiyādimaggavipāko = दूसरे और आगे के मार्गों का कर्म-फल; Lokuttaravipāko. = लोकोत्तर कर्म-फल।
Akusalavipākapañcaviññāṇāni / -manodhātu / -manoviññāṇadhātu = हानिकर कर्म के फल रूपी पाँच प्रकार की चेतना / मन का तत्व / मन की चेतना का तत्व (pattern of 2-04)
Vipākā abyākatā. = नैतिक रूप से अनिर्धारित कर्म-फल। (= terms' Abyākatavipāko)
Kiriyāmanodhātu = केवल क्रिया रूपी मन का तत्व; Kiriyāmanoviññāṇadhātusomanassasahagatā / upekkhā- = केवल क्रिया रूपी, प्रसन्नता / समभाव के साथ होने वाला मन की चेतना का तत्व
Ahetukā kiriyā abyākatā. = मूल से रहित, केवल क्रिया रूपी, नैतिक रूप से अनिर्धारित मन।; Kiriyā abyākatā. = केवल क्रिया रूपी, नैतिक रूप से अनिर्धारित मन।
Sahetukakāmāvacarakiriyā = मूल वाला, इंद्रिय-सुखों के लोक से संबंधित केवल क्रिया रूपी मन; Rūpāvacara- / Arūpāvacarakiriyā = सूक्ष्म भौतिक / अभौतिक लोक से संबंधित केवल क्रिया रूपी मन
Cittuppādakaṇḍaṃ niṭṭhitaṃ. = मन की उत्पत्ति का अध्याय पूरा हुआ।

## For the consistency pass
- 2-01/2-02 and 2-03 differ on the paṭipadā and adhipati strings: 2-01_2-02 «दुःखद प्रगति और धीमे/तीव्र उच्च ज्ञान के साथ», «जिसमें चाह प्रधान है»; 2-03 «… धीमे/शीघ्र उच्च ज्ञान वाला», «चाह की प्रधानता वाला» inside «जो ध्यान … है». 2-05 follows 2-03 (same lokuttara formula); change ATTR in the builder if 2-01's wording is chosen.
- sammappadhāna = सही प्रयास (pi-3, as 2-03) coincides with sammāvāyāma = सही प्रयास.

## Source notes (translated as written)
- ^1-528: «ime dhammā kusalā tasseva …» has no full stop; rendered with a semicolon.
- ^1-553: «kāmarā gabyāpādānaṃ» split word; read as kāmarāgabyāpādānaṃ.
- ^1-553: the wholesome clause of the second to fourth paths lists aññindriyaṃ, the result clause aññātāvindriyaṃ (fits only the fourth path); kept.
- ^1-544 stray comma «viharati, animittaṃ»; ^1-574 missing comma «samādhindriyaṃ hoti manindriyaṃ»; ^1-579 no comma before «tasmiṃ samaye»; normal Hindi punctuation used.
- ^1-576: the Pāli has «…pe… ime dhammā abyākatā…pe… alobho abyākatamūlaṃ…» (two answers); kept.
