# notes-4-01: pi-1 4-01-nikkhepakandam (Nikkhepakaṇḍaṃ, part 1), Hindi plain zero-shot

Builder: build_4-01_hi.py (imports build_matika_hi: BARE, QUESTION, ANSWER, GROUPS; build_ch2_01_sample_hi: NAMES, S_ALOBHA, S_ADOSA, S_PANNA, V, DASH). Every string below is a constant there; copy from the builder, not from this file, if you need byte-identity.
Matrix items: always M.BARE[(id, letter)] with M.QUESTION / M.ANSWER. Format: Pāli = Hindi, one per line.

## Headings and closing lines
### Nikkhepakaṇḍaṃ = ### सारांश का अध्याय
#### Tikanikkhepaṃ = #### तीन-तीन के वर्गीकरणों का सारांश
#### Dukanikkhepaṃ = #### दो-दो के वर्गीकरणों का सारांश
##### gocchaka headings = M.GROUPS[...][0] (##### मूलों का वर्ग …)
Tikaṃ. = तीन-तीन के वर्गीकरण।
Nikkhepakaṇḍe paṭhamabhāṇavāro. = सारांश के अध्याय का पहला पाठ-खंड।

## Frames (shared with 4-02 / 4-03 / chapter 5)
Katame dhammā X? = M.QUESTION(X)  (हितकर परिघटनाएँ कौन-सी हैं?)
– ime dhammā X. = – M.ANSWER(X)  (– ये हितकर परिघटनाएँ हैं।)
Ime dhammā X. (closing line) = M.ANSWER(X)
Tattha katamo/katamā/katamaṃ X? = यहाँ X क्या है?   (approved Hindi pi-4 ^4-45, ^4-49 … frame)
– ayaṃ/idaṃ vuccati X. = – इसे X कहा जाता है।   (pi-4)
Tattha katamā X…pe… ayaṃ vuccati X. = यहाँ X क्या है … इसे X कहा जाता है।
Tattha katame tayo kusalahetū? = यहाँ तीन हितकर मूल कौन-से हैं?
Ime tayo kusalahetū. = ये तीन हितकर मूल हैं।
Yo/Yā/Yaṃ S – ayaṃ vuccati X. = जो <first word of S> है, <rest of S> – इसे X कहा जाता है।   (pi-4 ^4-45 form; JO() in the builder)
Yā/Yo/Yaṃ evarūpā/-o/-ṃ X … = जो इस प्रकार की/का X है, …
Sabbāpi micchādiṭṭhi X. = सारी ग़लत दृष्टि X है।
Ṭhapetvā Y sabbāpi micchādiṭṭhi X. = Y (oblique) को छोड़कर सारी ग़लत दृष्टि X है।
Teyeva āsavā āsavā ceva sāsavā ca. = वे ही मन के मैल, मन के मैल रूपी भी और मन के मैलों का विषय बनने वाली भी परिघटनाएँ हैं।  (Tāneva saṃyojanāni … = वे ही बंधन, …; Teva ganthā … = वे ही गाँठें, …)
X Y-ena Z ceva Z-sampayutto ca = X, Y (oblique) के साथ, Z भी है और Z से जुड़ा भी   (feminine गाँठ: … गाँठ भी है और गाँठ से जुड़ी भी)
Lobho mohena hetu ceva sahetuko ca = लोभ, मोह के साथ, मूल रूपी भी है और मूल वाला भी
… hetu ceva hetusampayutto ca = … मूल रूपी भी है और मूल से जुड़ा भी
alobho adoso amoho, te aññamaññaṃ hetū ceva sahetukā ca = लोभ का अभाव, द्वेष का अभाव, मोह का अभाव, ये एक-दूसरे के साथ मूल रूपी भी हैं और मूल वाले भी  (… और मूलों से जुड़े भी)
Tehi dhammehi ye dhammā sahetukā / ahetukā = उन परिघटनाओं के संबंध में जो परिघटनाएँ मूल वाली हैं / मूल से रहित हैं, यानी …
Tehi dhammehi ye dhammā na hetū sahetukā / ahetukā = उन परिघटनाओं के संबंध में जो परिघटनाएँ मूल रूपी नहीं हैं, पर मूल वाली हैं / मूल रूपी नहीं हैं और मूल से रहित हैं, यानी …
Tehi dhammehi ye dhammā sampayuttā / vippayuttā = उन परिघटनाओं से जो परिघटनाएँ जुड़ी हैं / अलग हैं, यानी …
Tehi dhammehi ye dhammā X, te dhamme ṭhapetvā (avasesā) = उन परिघटनाओं के संबंध में जो परिघटनाएँ X, उनमें से उन्हीं परिघटनाओं को छोड़कर (बाकी, …)
Tehi dhammehi ye dhammā sampayuttā, te dhamme ṭhapetvā = उन परिघटनाओं से जो परिघटनाएँ जुड़ी हैं, उनमें से उन्हीं परिघटनाओं को छोड़कर
Tehi dhammehi ye dhammā vippayuttā sāsavā kusalākusalābyākatā dhammā = उन परिघटनाओं से जो परिघटनाएँ अलग हैं और मन के मैलों का विषय बनने वाली हितकर, हानिकर और नैतिक रूप से अनिर्धारित परिघटनाएँ हैं
Te dhamme ṭhapetvā avasesā kusalākusalābyākatā dhammā = उन परिघटनाओं को छोड़कर बाकी हितकर, हानिकर और नैतिक रूप से अनिर्धारित परिघटनाएँ
ṭhapetvā = को छोड़कर; avasesa = बाकी
(yānī) linking a relative clause to the named list = यानी (no Pāli word; the Pāli just juxtaposes)

## Recurring lists (the "mind-type" formulas used in the answers)
kāmāvacarā, rūpāvacarā, arūpāvacarā, apariyāpannā (after a plural noun) = चाहे वे इंद्रिय-सुखों के लोक से संबंधित, सूक्ष्म भौतिक लोक से संबंधित, अभौतिक लोक से संबंधित या अस्तित्व के लोकों में न समाई हुई हों   (after परिघटनाएँ; after masculine कर्म-फल: … न समाए हुए हों)
kāmāvacarā, rūpāvacarā, arūpāvacarā = चाहे वे इंद्रिय-सुखों के लोक से संबंधित, सूक्ष्म भौतिक लोक से संबंधित या अभौतिक लोक से संबंधित हों
<X>bhūmiyaṃ kāmāvacare, rūpāvacare, apariyāpanne, <X> ṭhapetvā = <X> की भूमि में, चाहे वह इंद्रिय-सुखों के लोक से संबंधित, सूक्ष्म भौतिक लोक से संबंधित या अस्तित्व के लोकों में न समाई हुई हो, <X> को छोड़कर   (one sphere: …भूमि में, जो इंद्रिय-सुखों के लोक से संबंधित है, …)
Sukhabhūmiyaṃ (^1-988, with sukhaṃ vedanaṃ) = सुखद अनुभूति की भूमि में; Sukhabhūmiyaṃ (^1-1004, with sukhaṃ) = सुख की भूमि में; Dukkha- = दुःखद अनुभूति की भूमि; Adukkhamasukha- = न दुःखद, न सुखद अनुभूति की भूमि; Pīti- = उल्लास की भूमि; Upekkhā- = समभाव की भूमि; Savitakkasavicāra- = आरंभिक विचार और सतत विचार वाली भूमि; Avitakkavicāramatta- = आरंभिक विचार से रहित, केवल सतत विचार वाली भूमि; Avitakkaavicāra- = आरंभिक विचार और सतत विचार दोनों से रहित भूमि
Kusalākusalānaṃ dhammānaṃ vipākā = हितकर और हानिकर परिघटनाओं के कर्म-फल
Sāsavā kusalākusalānaṃ dhammānaṃ vipākā = मन के मैलों का विषय बनने वाले, हितकर और हानिकर परिघटनाओं के कर्म-फल
Kusalākusalānaṃ dhammānaṃ avipakkavipākānaṃ vipākā = अनपके कर्म-फल वाली हितकर और हानिकर परिघटनाओं के कर्म-फल
kusalākusalā / kusalābyākatā / kusalākusalābyākatā dhammā = हितकर और हानिकर परिघटनाएँ / हितकर और नैतिक रूप से अनिर्धारित परिघटनाएँ / हितकर, हानिकर और नैतिक रूप से अनिर्धारित परिघटनाएँ
sāsavā (before those) = मन के मैलों का विषय बनने वाली …
Sabbeva kāmāvacarā kusalākusalābyākatā dhammā = इंद्रिय-सुखों के लोक से संबंधित सभी हितकर, हानिकर और नैतिक रूप से अनिर्धारित परिघटनाएँ
ye ca dhammā kiriyā neva kusalā nākusalā na ca kammavipākā = और वे परिघटनाएँ जो केवल क्रिया रूपी हैं, न हितकर हैं, न हानिकर, और न ही कर्म-फल रूपी   (sentence-initial at ^1-993 without «और»)
kiriyābyākatesu dhammesu = केवल क्रिया रूपी नैतिक रूप से अनिर्धारित परिघटनाओं में
Kusalānaṃ (vā) dhammānaṃ vipākato = हितकर परिघटनाओं के कर्म-फल के रूप में
sabbañca rūpaṃ, asaṅkhatā ca dhātu = सारा भौतिक रूप और अनिर्मित तत्व
asaṅkhatā dhātu = अनिर्मित तत्व
Apariyāpannā maggā ca, maggaphalāni ca, asaṅkhatā ca dhātu = अस्तित्व के लोकों में न समाए हुए मार्ग, मार्गों के फल और अनिर्मित तत्व
Cattāro maggā apariyāpannā = अस्तित्व के लोकों में न समाए हुए चार मार्ग
heṭṭhimāni ca tīṇi sāmaññaphalāni = और श्रमण-जीवन के तीन निचले फल
Upariṭṭhimaṃ arahattaphalaṃ = सबसे ऊपर का फल, यानी अर्हत्-पद का फल
yañca rūpaṃ kammassa katattā / na kammassa katattā / … uppajjissati = और जो भौतिक रूप कर्म किए जाने के कारण बना है / नहीं बना है / उत्पन्न होगा
yañca rūpaṃ anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ = और जो भौतिक रूप दिखाई न देने वाला, टकराव से रहित और मन के विषयों के इंद्रिय-क्षेत्र में समाया हुआ है
Tīṇi kusalamūlāni – alobho, adoso, amoho = तीन हितकर मूल – लोभ का अभाव, द्वेष का अभाव, मोह का अभाव
Tīṇi akusalamūlāni – lobho, doso, moho = तीन हानिकर मूल – लोभ, द्वेष, मोह
tadekaṭṭhā ca kilesā = और उनके साथ रहने वाले मन के क्लेश
Tadekaṭṭho lobho, doso, moho = उनके साथ रहने वाला लोभ, द्वेष, मोह
Avaseso lobho, doso, moho = बाकी लोभ, द्वेष, मोह
taṃsampayutto vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho = उनसे जुड़ा अनुभूति का समूह, पहचान का समूह, मानसिक रचनाओं का समूह, चेतना का समूह
taṃsampayutto vedanākkhandho…pe… viññāṇakkhandho = उनसे जुड़ा अनुभूति का समूह … चेतना का समूह
taṃsampayutto saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho = उनसे जुड़ा पहचान का समूह, मानसिक रचनाओं का समूह, चेतना का समूह
vedanākkhandho…pe… viññāṇakkhandho = अनुभूति का समूह … चेतना का समूह
rūpakkhandho…pe… viññāṇakkhandho = भौतिक रूप का समूह … चेतना का समूह
rūpakkhandho, vedanākkhandho, … viññāṇakkhandho = भौतिक रूप का समूह, अनुभूति का समूह, पहचान का समूह, मानसिक रचनाओं का समूह, चेतना का समूह
Pañcakkhandhā = पाँच समूह
taṃsamuṭṭhānaṃ kāyakammaṃ, vacīkammaṃ, manokammaṃ = उनसे उत्पन्न शारीरिक कर्म, वाणी का कर्म, मानसिक कर्म   (pi-5)
X dhamme ārabbha ye uppajjanti cittacetasikā dhammā = X परिघटनाओं को विषय बनाकर जो मन और मन की सहचर परिघटनाएँ उत्पन्न होती हैं
Ariyamaggaṃ ārabbha / adhipatiṃ karitvā = आर्य मार्ग को विषय बनाकर / आर्य मार्ग को प्रधान बनाकर
Ariyamaggasamaṅgissa = आर्य मार्ग से युक्त व्यक्ति में; maggaṅgāni = मार्ग के अंग; maggahetū = मार्ग के मूल
vīmaṃsādhipateyyaṃ maggaṃ bhāvayantassa = जाँच-परख की प्रधानता वाले मार्ग का अभ्यास करता है (vīmaṃsā = जाँच-परख, pi-5)
Pañca kammāni ānantarikāni, yā ca micchādiṭṭhiniyatā = तत्काल फल देने वाले पाँच घोर कर्म, और जो ग़लत दृष्टि निश्चित परिणाम वाली है
jātā bhūtā sañjātā nibbattā abhinibbattā pātubhūtā uppannā samuppannā uṭṭhitā samuṭṭhitā = जन्मी हुई, हो चुकी, भली-भाँति जन्मी, पैदा हुई, पूरी तरह पैदा हुई, प्रकट हुई, उत्पन्न, भली-भाँति उत्पन्न, उठी हुई, भली-भाँति उठी हुई (negatives: न + each)
atītā niruddhā vigatā vipariṇatā atthaṅgatā abbhatthaṅgatā uppajjitvā vigatā = बीत चुकी, समाप्त हो चुकी, जा चुकी, बदल चुकी, अस्त हो चुकी, पूरी तरह अस्त हो चुकी, उत्पन्न होकर जा चुकी
uppannā uppannaṃsena saṅgahitā = उत्पन्न हैं और “उत्पन्न” के अंतर्गत गिनी जाती हैं (likewise “उत्पन्न न हुई”, “अतीत”, “भविष्य”, “वर्तमान”)
rūpaṃ, vedanā, saññā, saṅkhārā, viññāṇaṃ = भौतिक रूप, अनुभूति, पहचान, मानसिक रचनाएँ, चेतना
tesaṃ tesaṃ sattānaṃ ajjhattaṃ paccattaṃ niyatā pāṭipuggalikā upādiṇṇā = उन-उन प्राणियों के भीतर, उनकी अपनी, उन्हीं से बँधी, हर व्यक्ति की निजी और कर्म से उत्पन्न (parasattānaṃ parapuggalānaṃ = दूसरे प्राणियों, दूसरे व्यक्तियों)
Tadubhayaṃ = ये दोनों
Cattāro ca mahābhūtā catunnañca mahābhūtānaṃ upādāya rūpaṃ = चार महाभूत और चार महाभूतों से व्युत्पन्न भौतिक रूप
Yeva te dhammā sappaccayā, teva te dhammā saṅkhatā = जो परिघटनाएँ कारणों पर निर्भर हैं, वही परिघटनाएँ निर्मित हैं
Yo eva so dhammo appaccayo, so eva so dhammo asaṅkhato = जो परिघटना कारणों पर निर्भर नहीं रहती, वही परिघटना अनिर्मित है
āyatanas = आँख / कान / नाक / जीभ / शरीर / दृश्य रूप / ध्वनि / गंध / स्वाद / स्पर्श का इंद्रिय-क्षेत्र (pi-3)
X-viññeyya = X की चेतना से जानी जा सकने वाली (आँख, कान, नाक, जीभ, शरीर)
Ye te dhammā cakkhuviññeyyā, na te dhammā sotaviññeyyā = जो परिघटनाएँ आँख की चेतना से जानी जा सकती हैं, वे कान की चेतना से नहीं जानी जा सकतीं
Katame dhammā kenaci viññeyyā, kenaci na viññeyyā? = <2-13 क> और <2-13 ख> कौन-सी हैं?

## Roots
Tayo kusala- / akusala- / abyākatahetū = तीन हितकर मूल / तीन हानिकर मूल / तीन नैतिक रूप से अनिर्धारित मूल
nava kāmāvacarahetū / cha rūpāvacara- / arūpāvacara- / apariyāpannahetū = इंद्रिय-सुखों के लोक से संबंधित नौ मूल / सूक्ष्म भौतिक लोक से संबंधित छह मूल / अभौतिक लोक से संबंधित छह मूल / अस्तित्व के लोकों में न समाए हुए छह मूल
pahātabbahetū = (सत्य-दर्शन / मानसिक अभ्यास) से छोड़े जाने वाले मूल

## Defilement names
sakkāyadiṭṭhi = स्थायी आत्मा की ग़लत दृष्टि (pi-5)
vicikicchā = संशय; kaṅkhā = शंका; kaṅkhati vicikicchati = शंका करता है, संशय करता है
sīlabbataparāmāsa = सदाचार और व्रतों के बारे में ग़लत धारणा (parāmāsa = ग़लत धारणा as in the matrix; departs from pi-5 कर्मकांडों और व्रतों से चिपकाव)
Tīṇi saṃyojanāni – sakkāyadiṭṭhi, vicikicchā, sīlabbataparāmāso = तीन बंधन – स्थायी आत्मा की ग़लत दृष्टि, संशय, सदाचार और व्रतों के बारे में ग़लत धारणा
āsava (singular) = मन का मैल; Cattāro āsavā = मन के चार मैल
kāmāsava / bhavāsava / diṭṭhāsava / avijjāsava = इंद्रिय-सुखों का मैल / अस्तित्व का मैल / दृष्टि का मैल / अज्ञान का मैल
Dasa saṃyojanāni = दस बंधन
kāmarāga- / paṭigha- / māna- / diṭṭhi- / vicikicchā- / sīlabbataparāmāsa- / bhavarāga- / issā- / macchariya- / avijjā-saṃyojanaṃ = इंद्रिय-सुखों के राग का बंधन / चिढ़ का बंधन / अहंकार का बंधन / दृष्टि का बंधन / संशय का बंधन / सदाचार और व्रतों के बारे में ग़लत धारणा का बंधन / अस्तित्व के राग का बंधन / ईर्ष्या का बंधन / कंजूसी का बंधन / अज्ञान का बंधन
Cattāro ganthā = चार गाँठें
abhijjhā / byāpādo / sīlabbataparāmāso / idaṃsaccābhiniveso kāyagantho = लालच रूपी काया की गाँठ / दुर्भावना रूपी काया की गाँठ / सदाचार और व्रतों के बारे में ग़लत धारणा रूपी काया की गाँठ / “केवल यही सत्य है” के आग्रह रूपी काया की गाँठ
micchādiṭṭhi = ग़लत दृष्टि; paṭigha = चिढ़ (pi-5); māna = अहंकार (pi-4/5); issā = ईर्ष्या; macchariya = कंजूसी (pi-4)

## Synonym strings (all in build_4-01_hi.py; copy from there)
diṭṭhi string (yā evarūpā diṭṭhi diṭṭhigataṃ … vipariyāsaggāho) = जो इस प्रकार की दृष्टि है, दृष्टि में पड़ जाना, दृष्टि का घना जंगल, दृष्टि का बीहड़, दृष्टि का टेढ़ापन, दृष्टि की छटपटाहट, दृष्टि का बंधन, पकड़, कसकर पकड़ना, आग्रह, ग़लत धारणा, कुमार्ग, ग़लत रास्ता, ग़लतपन, मतवादों का अड्डा, उलटी पकड़   (pi-4 ^4-62 with parāmāso = ग़लत धारणा)
Dukkhe ñāṇaṃ … idappaccayatā paṭiccasamuppannesu dhammesu ñāṇaṃ = दुःख का ज्ञान, दुःख की उत्पत्ति का ज्ञान, दुःख के अंत का ज्ञान, दुःख के अंत की ओर ले जाने वाले मार्ग का ज्ञान, अतीत का ज्ञान, भविष्य का ज्ञान, अतीत और भविष्य दोनों का ज्ञान, कार्य-कारण के नियम से परस्पर-आश्रित रूप से उत्पन्न परिघटनाओं का ज्ञान
Dukkhe aññāṇaṃ … = दुःख को न जानना, दुःख की उत्पत्ति को न जानना, … परिघटनाओं को न जानना
yā evarūpā paññā pajānanā … sammādiṭṭhi = जो इस प्रकार की प्रज्ञा है, जानना, … सही दृष्टि  (sample S_PANNA without its first word)
dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ = परिघटनाओं की छानबीन रूपी जागृति का अंग, मार्ग का अंग, मार्ग में समाया हुआ
moha string (yaṃ evarūpaṃ aññāṇaṃ adassanaṃ … moho akusalamūlaṃ) = जो इस प्रकार का न जानना है, न देखना, सत्य तक न पहुँचना, बोध न होना, पूर्ण बोध न होना, भेद न पाना, न समेट पाना, गहराई में न उतर पाना, निष्पक्ष रूप से न देखना, पुनः विचार न करना, प्रत्यक्ष न करना, दुर्बुद्धि, मूर्खता, स्पष्ट समझ का अभाव, मोह, गहरा मोह, घोर मोह, अज्ञान, अज्ञान की बाढ़, अज्ञान की जकड़न, अज्ञान की सुप्त प्रवृत्ति, अज्ञान का आवेश, अज्ञान की रुकावट, मोह, हानिकर मूल   (pi-4 ^4-60 with yoga = जकड़न, akusalamūlaṃ = हानिकर मूल)
akusalamūlaṃ = हानिकर मूल
metti mettāyanā mettāyitattaṃ anuddā anuddāyanā anudāyitattaṃ hitesitā anukampā = मैत्री, मैत्री करना, मैत्री से भरा होना, दया, दया करना, दया से भरा होना, हित की कामना, सहानुभूति   (inserted into the sample's adosa string after «द्वेष से भरा न होना,»)
Yo adoso adussanā adussitattaṃ…pe… abyāpādo … = जो द्वेष का अभाव है, द्वेष न करना, द्वेष से भरा न होना … दुर्भावना का अभाव, दुर्भावना न रखना, द्वेष का अभाव, हितकर मूल
lobha string (rāgo sārāgo … abhijjhā lobho akusalamūlaṃ) = LOBHA in the builder (राग, गहरा राग, झुकाव, … लालच, लोभ, हानिकर मूल)
  key words: sārāgo = गहरा राग (next to rāgo = राग); nandī = रस लेना; ajjhosānaṃ = चिपके रहना; mucchā = मूर्छा; gedho = लालसा; māyā = कपट (pi-4); paṇidhi = आकांक्षा (pi-5); bandhanaṃ = बेड़ी (बंधन is saṃyojana); upakkileso = दूषण; anusayo = सुप्त प्रवृत्ति; pariyuṭṭhānaṃ = आवेश; vevicchaṃ = लोभीपन (pi-4); kāmataṇhā / bhavataṇhā / vibhavataṇhā = इंद्रिय-सुखों / अस्तित्व / अनस्तित्व की तृष्णा; rūpataṇhā (1st) / arūpataṇhā = सूक्ष्म भौतिक / अभौतिक अस्तित्व की तृष्णा; nirodhataṇhā = समाप्ति की तृष्णा; rūpa-…dhammataṇhā (2nd set) = दृश्य रूपों … मन के विषयों की तृष्णा; Māra = मार
Yo kāmesu kāmacchando … kāmajjhosānaṃ = इंद्रिय-सुखों के प्रति जो इंद्रिय-सुखों की चाह है, इंद्रिय-सुखों का राग, इंद्रिय-सुखों में रस लेना, इंद्रिय-सुखों की तृष्णा, इंद्रिय-सुखों का स्नेह, इंद्रिय-सुखों का ताप, इंद्रिय-सुखों की मूर्छा, इंद्रिय-सुखों से चिपके रहना
Yo bhavesu bhavachando … bhavajjhosānaṃ = अस्तित्व के प्रति जो अस्तित्व की चाह है, अस्तित्व का राग, अस्तित्व में रस लेना, अस्तित्व की तृष्णा, अस्तित्व का स्नेह, अस्तित्व का ताप, अस्तित्व की मूर्छा, अस्तित्व से चिपके रहना
dosa intro (Anatthaṃ me acarīti āghāto jāyati …) = “उसने मेरा अहित किया” इस विचार से आक्रोश उत्पन्न होता है, … या बिना कारण भी आक्रोश उत्पन्न होता है।
dosa string (Yo evarūpo cittassa āghāto … anattamanatā cittassa) = जो इस प्रकार का मन का आक्रोश है, प्रतिघात, चिढ़, प्रतिविरोध, कोप, प्रकोप, तीव्र प्रकोप, द्वेष, गहरा द्वेष, तीव्र द्वेष, मन की दुर्भावना, मन का द्वेष, क्रोध, क्रोध करना, क्रुद्ध होना, द्वेष, द्वेष करना, द्वेष से भरा होना, दुर्भावना, दुर्भावना रखना, दुर्भावना से भरा होना, विरोध, प्रतिविरोध, उग्रता, कटु वचन, मन की अप्रसन्नता   (kodho … tail = pi-4 ^4-45 verbatim)
āghāta = आक्रोश; paṭighāta = प्रतिघात; paṭigha = चिढ़
vicikicchā intro (Satthari kaṅkhati vicikicchati …) = कोई गुरु के बारे में शंका करता है, संशय करता है, शिक्षा …, संघ …, प्रशिक्षण …, अतीत …, भविष्य …, अतीत और भविष्य दोनों …, कार्य-कारण के नियम से परस्पर-आश्रित रूप से उत्पन्न परिघटनाओं के बारे में शंका करता है, संशय करता है  (satthā = गुरु, sikkhā = प्रशिक्षण, pi-5)
kaṅkhā string (yā evarūpā kaṅkhā … manovilekho) = जो इस प्रकार की शंका है, शंका करना, शंका से भरा होना, दुविधा, संशय, दोचित्तापन, दोराहा, संदेह, किसी एक बात को पक्का न पकड़ पाना, हिचकिचाना, बार-बार हिचकिचाना, गहराई में न उतर पाना, मन का जड़ हो जाना, मन की खरोंच
Ito bahiddhā samaṇabrāhmaṇānaṃ sīlena suddhi, vatena suddhi, sīlabbatena suddhīti = इस शिक्षा से बाहर के श्रमण और ब्राह्मण मानते हैं कि “सदाचार से शुद्धि होती है, व्रत से शुद्धि होती है, सदाचार और व्रत से शुद्धि होती है”
sakkāyadiṭṭhi body (assutavā puthujjano … rūpaṃ attato samanupassati …) = यहाँ कोई अशिक्षित साधारण व्यक्ति, जिसने आर्यों के दर्शन नहीं किए, … भौतिक रूप को आत्मा के रूप में देखता है, या आत्मा को भौतिक रूप वाला, या आत्मा में भौतिक रूप को, या भौतिक रूप में आत्मा को। (sappurisa = सज्जन, pi-4)
ten views (sassato loko … neva hoti na na hoti tathāgato paraṃ maraṇā) = “लोक शाश्वत है” या “लोक शाश्वत नहीं है” या “लोक सीमित है” या “लोक असीम है” या “जो जीव है, वही शरीर है” या “जीव अलग है, शरीर अलग है” या “मृत्यु के बाद तथागत रहता है” या “मृत्यु के बाद तथागत नहीं रहता” या “मृत्यु के बाद तथागत रहता भी है और नहीं भी रहता” या “मृत्यु के बाद तथागत न रहता है, न नहीं रहता”   (pi-5 wording)
idameva saccaṃ moghamaññaṃ = केवल यही सत्य है, बाकी सब झूठ है
māna body = “मैं श्रेष्ठ हूँ” यह अहंकार, “मैं बराबर हूँ” यह अहंकार, “मैं हीन हूँ” यह अहंकार। जो इस प्रकार का अहंकार है, मान लेना, मान चुका होना, ऊँचा उठना, अकड़, झंडा, स्वयं को ऊपर उठाना, मन की झंडा फहराने की इच्छा
issā body = pi-4 ^4-49 verbatim (दूसरों को मिलने वाले लाभ, सत्कार, सम्मान, आदर, वंदना और पूजा को लेकर जो ईर्ष्या है, …)
macchariya body = pi-4 ^4-50 verbatim (कंजूसी पाँच प्रकार की होती है – …)

## Departures from earlier Hindi (pi-4 / pi-5)
- parāmāso inside the diṭṭhi string = ग़लत धारणा (pi-4 ^4-62: चिपके रहना). Reason: parāmāsa = ग़लत धारणा in the approved matrix; chapter 4 names the parāmāsa group with that word.
- sīlabbataparāmāsa = सदाचार और व्रतों के बारे में ग़लत धारणा (pi-5: कर्मकांडों और व्रतों से चिपकाव). Same reason; sīla = सदाचार (core term).
- avijjāyogo / yogo = अज्ञान की जकड़न / जकड़न (pi-4, pi-5: जुआ). Reason: yoga = जकड़न in the matrix.
- akusalamūlaṃ = हानिकर मूल (pi-4 ^4-60: हानिकर अवस्थाओं की जड़). Reason: kusalamūlaṃ = हितकर मूल in the sample; the pi-4 trailing «है» before the dash is dropped.
- sārāgo (lobha string, next to rāgo) = गहरा राग; the sample's asārāgo = राग का अभाव stays as is.
- nandī = रस लेना (pi-5: आनंद), because pāmojjaṃ = आनंद in the sample's pīti string.
- nikanti = रुचि (pi-5: चाह), because chanda = चाह.
- diṭṭhisaṃyojanaṃ = दृष्टि का बंधन (pi-5 once: ग़लत दृष्टि का बंधन), to match the same word inside the diṭṭhi string (pi-4).

## Source notes (translated as written)
- ^1-1106, ^1-1123, ^1-1128, ^1-1143, ^1-1144: a Devanāgarī visarga «ः» stands where a punctuation mark belongs; rendered as «;».
- ^1-1124, ^1-1143, ^1-1144: «patiṭṭhāho» for paṭiggāho in the diṭṭhi string; rendered like paṭiggāho (कसकर पकड़ना).
- ^1-1022: question spelled «neva ācayagāmi na apacayagāmino» (matrix: nevācayagāmināpacayagāmino); the matrix item is used.
- ^1-1041: variant «[rūpā (bahūsu)]» = [पाठभेद (अनेक संस्करण): rūpā].
- ^1-1024: «[uparimaṃ (syā.)]» treated as पाठभेद (different word form, not spelling).
- ^1-1065: «[puñcikatā (syā.) pucchikatā (sī.)]» = [वर्तनी-भेद (Syā.): puñcikatā; (Sī.): pucchikatā].
- ^1-1130, ^1-1146 (and ^1-1135, ^1-1138, ^1-1151, ^1-1154): the fetter and tie groups say «sāsavā» (subject to taints), not "subject to fetters/ties"; kept (मन के मैलों का विषय बनने वाली).
- ^1-1108 has no «Sāsavā» (it defines sāsavā itself); kept.
- ^1-1059: missing comma «nava kāmāvacarahetū cha rūpāvacarahetū»; Hindi has the comma.
