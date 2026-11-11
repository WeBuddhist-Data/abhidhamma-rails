# Notes: keyword map 4-02 / 4-03 (nikkhepakaṇḍa, clusters to the suttanta pairs)

Script: map_4-02_4-03_hi.py (BASE table + cluster tables + per-segment overrides; falls back to CH2).

## Recurring decisions (pāli = हिंदी (context))
vuccati X = X कहा जाता है (whole name + verb, as pi-4 «vuccati puggalo»)
Tattha = यहाँ (question frame «यहाँ X क्या है?»)
Yo / Yā / Yaṃ = जो; (no direct equivalent) where the Hindi has no relative (1-1349, 1-1352, 1-1354, 1-1368, 1-1370, 1-1372, and yaṃ in 1-1289 / 1-1291 «इस बीच»)
rūpa = सूक्ष्म भौतिक (segment with rūpāvacara-); दृश्य रूप (with rūpāyatanaṃ / rūpadhātu, and in the lobha string); rūpaṃ = भौतिक रूप
rūpakkhandho = भौतिक रूप का समूह
dhamma = मन के विषय (with dhammāyatanaṃ / dhammadhātu); मन का विषय (dhammataṇhā, 1-1236); शिक्षा (dhammapaṭisanthāra, 1-1351)
mano / kāya = मानसिक / शारीरिक where the segment has manokammaṃ / kāyakammaṃ; otherwise मन / शरीर
sāsavā = मन के मैलों का विषय बनने वाला; sāsavā kusalākusalābyākatā dhammā = मन के मैलों का विषय बनने वाली हितकर हानिकर और नैतिक रूप से अनिर्धारित परिघटना (comma dropped)
akusalābyākatā = हानिकर और नैतिक रूप से अनिर्धारित; avasesā kusala = शेष हितकर
tehi dhammehi = उन परिघटनाओं के संबंध में
asaṅkhatā ca dhātu = अनिर्मित तत्व; apariyāpannā maggā = अस्तित्व के लोकों में न समाए हुए मार्ग; phalāni = फल
apariyāpannā (alone, 1-1288/1290/1292) = अस्तित्व के लोकों में न समाई हुई (the text form; «समाया» cannot match «समाई»)
cluster frames: X-niyā = «Xों का विषय बनने वाला»; in the closing pair (1-1178/79, 1-1189/90, 1-1233/34) X-niyā = उनका / उसका विषय बनने वाला and «dhammā X-vippayuttā» = «X से अलग … परिघटना»; 1-1156/1157 (oghā / yogā, abbreviated) the same
X-vippayuttā X-niyā = «X से अलग पर उनका/उसका विषय बनने वाला» (comma dropped)
kilesa = क्लेश (in «क्लेशों से जुड़ा / अलग»), मन के क्लेश in 1-1235 / heading; kilesā = मन के क्लेश; kileso = मन का क्लेश
ekaṭṭhā ca kilesā = साथ रहने वाले मन के क्लेश; samuṭṭhānaṃ kāyakammaṃ = उत्पन्न शारीरिक कर्म; vacīkammaṃ manokammaṃ = वाणी का कर्म मानसिक कर्म
nīvaraṇa names: kāmacchandanīvaraṇaṃ इंद्रिय-सुखों की चाह की बाधा, byāpāda- दुर्भावना की बाधा, thinamiddha- आलस्य और तंद्रा की बाधा, uddhaccakukkucca- बेचैनी और पछतावे की बाधा, uddhacca- बेचैनी की बाधा, kukkucca- पछतावे की बाधा, vicikicchā- संशय की बाधा, avijjā- अज्ञान की बाधा
upādāna names: kāmupādānaṃ इंद्रिय-सुखों के प्रति आसक्ति, diṭṭhupādānaṃ दृष्टियों के प्रति आसक्ति, sīlabbatupādānaṃ सदाचार और व्रतों के प्रति आसक्ति, attavādupādānaṃ आत्मा के सिद्धांत के प्रति आसक्ति; vāda = सिद्धांत; sīlabbata = सदाचार और व्रत
sakkāyadiṭṭhi = स्थायी आत्मा की ग़लत दृष्टि (sakkāya = स्थायी आत्मा); sīlabbataparāmāso = सदाचार और व्रतों के बारे में ग़लत धारणा
diṭṭhi string (1-1181 etc.): parāmāso = ग़लत धारणा (pi-4 had चिपके रहना; this text says ग़लत धारणा); maggo = कुमार्ग (only inside kummaggo); tittha = मतवाद; vipariyāsa = उलटा
natthi = व्यर्थ / नहीं (as pi-4); atthi (fragment of natthi, 1-1369) = होना
pahātabbahetukā = छोड़ा जाने वाला मूल and hetukā = मूल in the «na …» segments 1-1272 / 1-1274 (Hindi «मूलों से रहित»); hetukā = मूलों वाला elsewhere
pītikā = उल्लास in 1-1280 («उल्लास से रहित»), उल्लास वाला in 1-1279
bhūtā = महाभूत (only inside «महाभूत»); purisānaṃ = सज्जन (only inside «सज्जनों»); patho = दोराहा in the vicikicchā string (dvedhāpatho)
āhāro = भोजन (kabaḷīkāro āhāro = कौर-कौर खाया जाने वाला भोजन)
vilekho = कुरेदना (manovilekho in kukkucca, 1-1166); खरोंच (vicikicchā string)
NAMING string (1-1313/14/15): saṅkhā गणना, samaññā संज्ञा, paññatti नामकरण, vohāro व्यवहार, nāmakammaṃ नाम देना, nāmadheyyaṃ अभिधान, nirutti अभिव्यक्ति, abhilāpo उच्चारण; dhammā adhivacanapathā = परिघटना … नाम के मार्ग रूपी
dovacassatā string: dovacassāyaṃ सलाह न मानना, dovacassiyaṃ सलाह न मानने का भाव, vippaṭikūla उलटा, gāhitā पकड़ना, vipaccanīka विरोध, sātatā रस लेना, agāravatā अगौरव, appaṭissavatā बात पर कान न देना; Sahadhammike = शिक्षा के अनुसार
santuṭṭhitā = संतोष (1-1353 / 1-1355 «(अ)संतोष»); संतुष्ट होना (1-1378)

## Presence-check exceptions (value correct, not matched by the checker)
- 4-02 1-1298 niyatā = निश्चित: the fragment lost its negative (aniyatā); the Hindi has «अनिश्चित» (one word), so the positive part is not a separate word.
- 4-03 1-1353 santuṭṭhitā = संतोष: same case (asantuṭṭhitā; Hindi «असंतोष»).
