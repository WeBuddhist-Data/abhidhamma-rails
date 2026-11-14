# Hindi pi-1, parts 2-01 (from ^1-1-1-2-0) and 2-02: new recurring terms and formulas

Builder: build_2-01_2-02_hi.py (`python -I -X utf8 build_2-01_2-02_hi.py` runs a self-test that re-translates the
sample's Pāli and must reproduce ch2-01-sample.md line for line, then writes both parts). Importing it does not build:
    sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi")
    import importlib; F = importlib.import_module("build_2-01_2-02_hi")
    F.translate_line(pali_line_without_block_id)   # raises KeyError on unknown Pāli
Reusable: F.NAMEINFO / F.info(), F.STR, F.STR_PREFIX, F.tail_tr(), F.there_list(), F.name_list(), F.qa_hi(),
F.summary_hi(), F.kusala_hi() with F.PH and F.INTROS, F.EXACT, F.var_hi(). Extend by adding keys; do not change values.

## Frames
Katamo/Katamā/Katamaṃ tasmiṃ samaye X hoti? = उस समय X क्या है? (sample)
Katame/Katamāni/Katamā tasmiṃ samaye X honti? = उस समय X क्या हैं?
ayaṃ/idaṃ tasmiṃ samaye X hoti = यह उस समय X है; ime/imāni/imā tasmiṃ samaye X honti = ये उस समय X हैं
X hoti / X honti (in lists) = X होता है / होती है; X होते हैं / होती हैं
Katamo tasmiṃ samaye X hoti…pe… ayaṃ tasmiṃ samaye X hoti. = उस समय X क्या है… यह उस समय X है।
Tasmiṃ kho pana samaye … = और उस समय …
(list answer) Vedanākkhandho, saññākkhandho, … = अनुभूति का समूह, पहचान का समूह, … (names joined by commas, also where the Pāli has none)
ṭhapetvā X = X को छोड़कर
ye vā pana … dhammā ṭhapetvā vedanākkhandhaṃ ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ = या उस समय जो भी दूसरी परस्पर-आश्रित रूप से उत्पन्न अभौतिक परिघटनाएँ होती हैं, अनुभूति के समूह को छोड़कर, पहचान के समूह को छोड़कर, चेतना के समूह को छोड़कर
…pe…. (sentence end) = …।
eko/ekā/ekaṃ X = एक X (एक संपर्क, एक अनुभूति का समूह, एक मन के विषयों का तत्व; same as 2-03)

## Names (Koṭṭhāsavāra / Suññatavāra)
vedanākkhandho / saññākkhandho / saṅkhārakkhandho / viññāṇakkhandho = अनुभूति का समूह / पहचान का समूह / मानसिक रचनाओं का समूह / चेतना का समूह
manāyatanaṃ = मन का इंद्रिय-क्षेत्र; dhammāyatanaṃ = मन के विषयों का इंद्रिय-क्षेत्र
manoviññāṇadhātu = मन की चेतना का तत्व (pi-3); dhammadhātu = मन के विषयों का तत्व (pi-5)
āhāra = आहार (pi-5); phassāhāro = संपर्क रूपी आहार; manosañcetanāhāro = मानसिक इरादा रूपी आहार; viññāṇāhāro = चेतना रूपी आहार
upekkhā (factor) = समभाव (पुं.); upekkhindriyaṃ = समभाव की क्षमता (स्त्री.)
cattāro khandhā = चार समूह; dvāyatanāni = दो इंद्रिय-क्षेत्र; dve dhātuyo = दो तत्व; tayo āhārā = तीन आहार
aṭṭhindriyāni / sattindriyāni / navindriyāni / pañcindriyāni / cattāri indriyāni / tīṇindriyāni = आठ / सात / नौ / पाँच / चार / तीन क्षमताएँ
satta / cha / cattāri / tīṇi balāni = सात / छह / चार / तीन बल
tayo hetū / dve hetū / eko hetu = तीन मूल / दो मूल / एक मूल
pañcaṅgikaṃ / caturaṅgikaṃ / tivaṅgikaṃ / duvaṅgikaṃ jhānaṃ = पाँच / चार / तीन / दो अंगों वाला ध्यान
aṭṭhaṅgiko / pañcaṅgiko / caturaṅgiko / tivaṅgiko / duvaṅgiko maggo = आठ / पाँच / चार / तीन / दो अंगों वाला मार्ग
(Suññata) dhammā / khandhā / āyatanāni / dhātuyo / āhārā / indriyāni / jhānaṃ / maggo / balāni / hetū = परिघटनाएँ / समूह / इंद्रिय-क्षेत्र / तत्व / आहार / क्षमताएँ / ध्यान / मार्ग / बल / मूल

## Strings
cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ cetosamphassajā adukkhamasukhā vedanā = न सुहावना, न असुहावना मानसिक भाव, मन के संपर्क से उत्पन्न न दुःखद, न सुखद अनुभव, मन के संपर्क से उत्पन्न न दुःखद, न सुखद अनुभूति
paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi = प्रज्ञा, जानना… मोह का अभाव, परिघटनाओं की छानबीन, सही दृष्टि

## The eight wholesome minds of the sense sphere
somanassasahagataṃ ñāṇavippayuttaṃ = जो प्रसन्नता के साथ होता है और ज्ञान से अलग होता है
upekkhāsahagataṃ ñāṇasampayuttaṃ / ñāṇavippayuttaṃ = जो समभाव के साथ होता है और ज्ञान से जुड़ा / अलग होता है
sasaṅkhārena = जो प्रेरणा के साथ उत्पन्न होता है (pi-5 has प्रयास के साथ; प्रयास is reserved for vāyāma/padhāna)
rūpārammaṇaṃ vā…pe… dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha = जिसका विषय दृश्य रूप हो… या मन का विषय, या चाहे वह जिस किसी को भी विषय बनाए (cut from the sample's string)
Paṭhamaṃ … Aṭṭhamaṃ cittaṃ. = पहले … आठवें प्रकार का मन।
Aṭṭha kāmāvacaramahākusalacittāni. = इंद्रिय-सुखों के लोक से संबंधित आठ महान हितकर मन।

## Absorptions (the approved Hindi pi-4 jhāna formula reused, without «वह», with परिघटनाओं for akusalehi dhammehi as in the terms file)
rūpūpapattiyā maggaṃ bhāveti = जिस समय कोई सूक्ष्म भौतिक लोक में जन्म की ओर ले जाने वाले मार्ग का अभ्यास करता है और …
arūpūpapattiyā maggaṃ bhāveti = … अभौतिक लोक में जन्म की ओर ले जाने वाले मार्ग का अभ्यास करता है और …
X jhānaṃ upasampajja viharati = X ध्यान को प्राप्त करके उसमें रहता है (पहले / दूसरे / तीसरे / चौथे / पाँचवें)
vivicceva kāmehi vivicca akusalehi dhammehi savitakkaṃ savicāraṃ vivekajaṃ pītisukhaṃ paṭhamaṃ jhānaṃ upasampajja viharati = इंद्रिय-सुखों से अलग होकर, हानिकर परिघटनाओं से अलग होकर, पहले ध्यान को प्राप्त करके उसमें रहता है, जो आरंभिक विचार और सतत विचार सहित है, अलगाव से उत्पन्न है, और जिसमें उल्लास और सुख है
vitakkavicārānaṃ vūpasamā ajjhattaṃ sampasādanaṃ cetaso ekodibhāvaṃ avitakkaṃ avicāraṃ samādhijaṃ pītisukhaṃ dutiyaṃ jhānaṃ upasampajja viharati = आरंभिक विचार और सतत विचार के शांत होने से दूसरे ध्यान को प्राप्त करके उसमें रहता है, जिसमें भीतरी निर्मलता और मन का एक बिंदु पर टिकना होता है, जो आरंभिक विचार और सतत विचार से रहित है, एकाग्रता से उत्पन्न है, और जिसमें उल्लास और सुख है
pītiyā ca virāgā … tatiyaṃ jhānaṃ upasampajja viharati = उल्लास के फीके पड़ने से समभाव के साथ, सजग और स्पष्ट समझ रखते हुए रहता है, शरीर से सुख का अनुभव करता है, और उस तीसरे ध्यान को प्राप्त करके उसमें रहता है जिसके विषय में आर्य कहते हैं – “समभाव वाला, सजग, सुख से रहने वाला”
sukhassa ca pahānā … catutthaṃ jhānaṃ upasampajja viharati = सुख के त्याग और दुःख के त्याग से, और पहले ही प्रसन्नता और उदासी के मिट जाने से, चौथे ध्यान को प्राप्त करके उसमें रहता है, जो न दुःखद, न सुखद है, और जिसमें समभाव से सजगता पूरी तरह शुद्ध होती है
avitakkaṃ vicāramattaṃ samādhijaṃ pītisukhaṃ dutiyaṃ jhānaṃ upasampajja viharati = दूसरे ध्यान को प्राप्त करके उसमें रहता है, जो आरंभिक विचार से रहित है, केवल सतत विचार वाला है, एकाग्रता से उत्पन्न है, और जिसमें उल्लास और सुख है
(openings before …pe…) vivicceva kāmehi / vitakkavicārānaṃ vūpasamā / pītiyā ca virāgā / sukhassa ca pahānā = इंद्रिय-सुखों से अलग होकर / आरंभिक विचार और सतत विचार के शांत होने से / उल्लास के फीके पड़ने से / सुख के त्याग से
(chains) dutiyaṃ jhānaṃ…pe… = दूसरे ध्यान को… (as pi-4)
kasiṇa = ध्यान-मंडल (pi-5); pathavī / āpo / tejo / vāyo / nīla / pīta / lohita / odāta-kasiṇaṃ = पृथ्वी के / जल के / अग्नि के / वायु के / नीले / पीले / लाल / सफ़ेद ध्यान-मंडल को आधार बनाकर
paṭipadā = प्रगति; abhiññā = उच्च ज्ञान (pi-4, pi-5); dukkha/sukha-paṭipadaṃ dandha/khippābhiññaṃ = दुःखद / सुखद प्रगति और धीमे / तीव्र उच्च ज्ञान के साथ
parittaṃ parittārammaṇaṃ = जो सीमित है और सीमित विषय वाला है (appamāṇaṃ = अपरिमित, matrix)
ajjhattaṃ arūpasaññī bahiddhā rūpāni passati = स्वयं में भौतिक रूप की पहचान न रखते हुए बाहर दृश्य रूपों को देखता है
parittāni / appamāṇāni / suvaṇṇadubbaṇṇāni = जो सीमित हैं / जो अपरिमित हैं / सुंदर और कुरूप
nīlāni nīlavaṇṇāni nīlanidassanāni nīlanibhāsāni = जो नीले हैं, नीले रंग वाले, नीले दिखने वाले, नीली आभा वाले (same for पीले / लाल / सफ़ेद)
tāni abhibhuyya jānāmi passāmīti = और उन पर विजय पाकर सोचता है, “मैं जानता हूँ, मैं देखता हूँ”
abhibhāyatana = विजय का आधार; vimokkha = मुक्ति-अवस्था (pi-4)
rūpī rūpāni passati = स्वयं भौतिक रूप वाला होकर दृश्य रूपों को देखता है; subhanti = “सुंदर” इस भाव के साथ
brahmavihāra = ब्रह्म-विहार; mettā / karuṇā / muditā / upekkhā-sahagataṃ = जो मैत्री / करुणा / दूसरों के सुख पर प्रसन्नता / समभाव के साथ होता है
asubha = असुंदरता (pi-5 असुंदर); X-saññāsahagataṃ = जो X की पहचान के साथ होता है: uddhumātaka फूली हुई लाश, vinīlaka नीली पड़ चुकी लाश, vipubbaka पीप से भरी लाश, vicchiddaka बीच से कटी लाश, vikkhāyitaka जानवरों द्वारा नोची गई लाश, vikkhittaka बिखरी हुई लाश, hatavikkhittaka काटकर बिखेरी गई लाश, lohitaka खून से सनी लाश, puḷavaka कीड़ों से भरी लाश, aṭṭhika कंकाल
sabbaso rūpasaññānaṃ samatikkamā paṭighasaññānaṃ atthaṅgamā nānattasaññānaṃ amanasikārā = भौतिक रूप की पहचानों को पूरी तरह पार कर जाने से, टकराव की पहचानों के मिट जाने से, विविधता की पहचानों पर मनोयोग न करने से
sabbaso X samatikkamma = X को पूरी तरह पार करके
ākāsānañcāyatana / viññāṇañcāyatana / ākiñcaññāyatana / nevasaññānāsaññāyatana = अनंत आकाश का क्षेत्र / अनंत चेतना का क्षेत्र / कुछ भी न होने का क्षेत्र / न पहचान न अ-पहचान का क्षेत्र (pi-5); -saññāsahagataṃ = … की पहचान के साथ
hīnaṃ / majjhimaṃ / paṇītaṃ = जो हीन / मध्यम / उत्तम है
chanda- / vīriya- / citta- / vīmaṃsā-dhipateyyaṃ = जिसमें चाह / उत्साह / मन / जाँच-परख प्रधान है (vīmaṃsā = जाँच-परख, pi-5)
Variant siglum (bahūsu) = (कई संस्करणों में) (pi-3); jhānaṃ/jjhānaṃ, paṭipadaṃ/āpaṭipadaṃ, puḷavaka/puḷuvaka, ṭhapetvā/thapetvā = वर्तनी-भेद

## Headings and closing lines (2-02; level-4/5 headings from hi-zeroshot-terms.md verbatim)
Aṭṭhakasiṇaṃ soḷasakkhattukaṃ = आठ ध्यान-मंडल, सोलह गुना
Idampi aṭṭhakkhattukaṃ = यह भी आठ गुना (closing: यह भी आठ गुना है।); Aparampi aṭṭhakkhattukaṃ = एक और आठ गुना
Abhibhāyatanāni parittāni = सीमित रूपों पर विजय के आधार
Appamāṇāni = असीम भाव (terms file, verbatim; see report: probably should be अपरिमित रूपों पर विजय के आधार, F.H_APPAMANANI_ALT)
Imānipi abhibhāyatanāni soḷasakkhattukāni. = विजय के ये आधार भी सोलह गुना हैं।
Tīṇi vimokkhāni soḷasakkhattukāni = तीन मुक्ति-अवस्थाएँ, सोलह गुना; Imānipi tīṇi vimokkhāni soḷasakkhattukāni. = ये तीन मुक्ति-अवस्थाएँ भी सोलह गुना हैं।
Cattāri brahmavihārajhānāni soḷasakkhattukāni = ब्रह्म-विहारों के चार ध्यान, सोलह गुना
Asubhajhānaṃ soḷasakkhattukaṃ = असुंदरता पर ध्यान, सोलह गुना
Cattāri arūpajhānāni soḷasakkhattukāni = चार अभौतिक ध्यान, सोलह गुना
Koṭṭhāsavāro. / Suññatavāro. / Catukkanayo. … (closing lines) = the heading wording + «।»

## Source points translated as written
^1-135: the answer ends with «?» (…ayaṃ tasmiṃ samaye cetanā hoti?); kept, like ^1-33.
^1-150 (cittakammaññatā hoti kāyapāguññatā hoti) and ^1-165 (manindriyaṃ hoti upekkhindriyaṃ hoti): comma missing in the Pāli; a normal comma is used.
^1-189: no comma before tasmiṃ samaye; none added.
^1-167, 180, 182, 202: «–» instead of a comma before tasmiṃ samaye; kept (dash rule).
^1-191, 205, 210, 264: stray space before …pe…; mirrored.
^1-270: the chain of the other seven minds has no vīmaṃsādhipateyyaṃ; translated as written.
