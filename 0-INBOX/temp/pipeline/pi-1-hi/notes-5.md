# notes-5: 5-atthakathakandam.md (Aṭṭhakathākaṇḍaṃ), Hindi plain zero-shot

Builder: build_5_hi.py (imports build_matika_hi: BARE, QUESTION, ANSWER, GROUPS, MATRIX_ITEMS_HI). All strings below are constants there.
Matrix items in questions, answers and "na vattabbā" clauses are M.BARE names verbatim (plural); singular subjects (निर्वाण, सुख, सतत विचार, ग़लत धारणा, कुछ भी न होने का क्षेत्र) take the same name with परिघटनाएँ -> परिघटना; oblique subjects take परिघटनाओं.

## Headings and closings
### Aṭṭhakathākaṇḍaṃ = ### अर्थ-व्याख्या का अध्याय
#### Tikaatthuddhāro = #### तीन-तीन के वर्गीकरणों का अर्थ-निर्धारण
#### Dukaatthuddhāro = #### दो-दो के वर्गीकरणों का अर्थ-निर्धारण
gocchaka headings = M.GROUPS (##### मूलों का वर्ग …)
Tikaṃ. (closing line) = तीन-तीन के वर्गीकरण।
Atthuddhāro niṭṭhito. = अर्थ-निर्धारण पूरा हुआ।
Dhammasaṅgaṇīpakaraṇaṃ niṭṭhitaṃ. = “परिघटनाओं की गणना” ग्रंथ पूरा हुआ।

## Frames
Katame dhammā X? … – ime dhammā X. = M.QUESTION(X) … – M.ANSWER(X)
ime dhammā siyā X, siyā Y = ये कभी X हैं, कभी Y हैं
na X (inside a siyā list) = X नहीं हैं
(ime dhammā) na vattabbā Xtipi, Ytipi = इन्हें न X कहा जा सकता है, न Y
(ime dhammā) na vattabbā Xti (one item) = इन्हें X नहीं कहा जा सकता
siyā na vattabbā … = और कभी इन्हें न X कहा जा सकता है, न Y
<S> dhammā na vattabbā – Xtipi, Ytipi = <S परिघटनाओं> को कहा नहीं जा सकता – न X, न Y
Nibbānaṃ na vattabbaṃ Xntipi … = निर्वाण को न X (sg.) कहा जा सकता है, न Y (sg.) …
Cittaṃ na vattabbaṃ – cittena sampayuttantipi, cittena vippayuttantipi = मन को कहा नहीं जा सकता – न मन से जुड़ा, न मन से अलग
Cittaṃ na vattabbaṃ – cittena saṃsaṭṭhantipi, cittena visaṃsaṭṭhantipi = मन को कहा नहीं जा सकता – न मन से घुला-मिला, न मन से घुला-मिला न होने वाला
Pīti na pītisahagatā, sukhasahagatā … = उल्लास स्वयं उल्लास के साथ होने वाली परिघटना नहीं है, सुख के साथ होने वाली परिघटना है …
Teva āsavā / Tāneva saṃyojanāni / Teva ganthā / Tāneva nīvaraṇāni / Tāneva upādānāni / Teva kilesā … = वे ही मन के मैल / बंधन / गाँठें / बाधाएँ / आसक्तियाँ / मन के क्लेश <item> हैं
So eva parāmāso … = वही ग़लत धारणा <item sg.> है
Yattha dve tayo hetū (āsavā, kilesā; dve tīṇi saṃyojanāni, nīvaraṇāni) ekato uppajjanti = जहाँ दो या तीन मूल (मन के मैल, मन के क्लेश, बंधन / बाधाएँ) एक साथ उत्पन्न होते (होती) हैं
Yattha diṭṭhi ca lobho ca ekato uppajjanti = जहाँ ग़लत दृष्टि और लोभ एक साथ उत्पन्न होते हैं
X Y-esu cittuppādesu uppajjati = X <…> मन की <n> उत्पत्तियों में उत्पन्न होता/होती है
ṭhapetvā X = X को छोड़कर
Ṭhapetvā āsave (saṃyojane, ganthe, nīvaraṇe, parāmāsaṃ, upādāne, kilese, hetū) = मन के मैलों (बंधनों, गाँठों, बाधाओं, ग़लत धारणा, आसक्तियों, मन के क्लेशों, मूलों) को छोड़कर
etthuppannaṃ X ṭhapetvā = इनमें उत्पन्न X को छोड़कर
avasesaṃ akusalaṃ = शेष हानिकर मन
Rūpañca nibbānañca anārammaṇā. = भौतिक रूप और निर्वाण विषय से रहित परिघटनाएँ हैं।
Niyogā anāgatārammaṇā natthi. = कोई भी परिघटनाएँ ऐसी नहीं हैं जो अनिवार्य रूप से भविष्य के विषय वाली परिघटनाएँ हों।
Nibbānaṃ ṭhapetvā sabbe dhammā = निर्वाण को छोड़कर सभी परिघटनाएँ

## Mind classes
bhūmi (catūsu / tīsu bhūmīsu) = लोक (चारों / तीनों लोकों से संबंधित), following the approved heading Tebhūmaka = तीनों लोकों से संबंधित. NOTE: the fourth bhūmi is lokuttara; if the user prefers, swap K4/V4 to «चारों स्तरों» (one constant each).
catūsu bhūmīsu kusalaṃ = चारों लोकों से संबंधित हितकर मन (locative pl. kusalesu = … हितकर मनों में)
tīsu bhūmīsu kusalaṃ = तीनों लोकों से संबंधित हितकर मन
akusalaṃ / sabbaṃ akusalaṃ / sabbākusalesu = हानिकर मन / सारा हानिकर मन / सभी हानिकर मनों में
catūsu / tīsu bhūmīsu vipāko = चारों / तीनों लोकों से संबंधित कर्म-फल रूपी मन (vipākesu = … कर्म-फल रूपी मनों में)
tīsu bhūmīsu kiriyābyākataṃ = तीनों लोकों से संबंधित केवल क्रिया रूपी नैतिक रूप से अनिर्धारित मन (kiriyesu = … केवल क्रिया रूपी मनों में). From the heading Ahetukakiriyāabyākataṃ, commas dropped so lists stay readable.
kāmāvacarakusalaṃ = इंद्रिय-सुखों के लोक से संबंधित हितकर मन (ch2 heading)
sabbo kāmāvacarassa vipāko = इंद्रिय-सुखों के लोक से संबंधित सारा कर्म-फल रूपी मन
kāmāvacarakiriyābyākataṃ = इंद्रिय-सुखों के लोक से संबंधित केवल क्रिया रूपी नैतिक रूप से अनिर्धारित मन
kāmāvacarakusalato / akusalato / kiriyato = इंद्रिय-सुखों के लोक से संबंधित हितकर मन में से / हानिकर मन में से / केवल क्रिया रूपी मन में से
kāmāvacarakusalassa vipākato / akusalassa vipākato = इंद्रिय-सुखों के लोक से संबंधित हितकर मन के कर्म-फल में से / हानिकर मन के कर्म-फल में से
kāmāvacarassa vipākato / kāmāvacarakiriyato = इंद्रिय-सुखों के लोक से संबंधित कर्म-फल रूपी मन में से / … केवल क्रिया रूपी मन में से
kusalato ca vipākato ca kiriyato ca = (हितकर, कर्म-फल रूपी और केवल क्रिया रूपी); kusalato ca vipākato ca = (हितकर और कर्म-फल रूपी); kusalato ca kiriyato ca = (हितकर और केवल क्रिया रूपी)
kusalābyākatā (^1-1418) = हितकर तथा नैतिक रूप से अनिर्धारित
kusalahetu / akusalahetu / abyākatahetu / vipākahetu / kiriyahetu = हितकर मूल / हानिकर मूल / नैतिक रूप से अनिर्धारित मूल / कर्म-फल रूपी मूल / केवल क्रिया रूपी मूल; "Alobho kusalahetu" = लोभ का अभाव (हितकर मूल)
cittuppāda = मन की उत्पत्ति; <qual>cittuppādā = <qual> मन की <n> उत्पत्तियाँ (obl. उत्पत्तियों)
dvādasa akusalacittuppādā = हानिकर मन की बारह उत्पत्तियाँ
somanassa- / upekkhā- / domanassa- / lobha- / vicikicchā- / uddhacca-sahagata = प्रसन्नता / समभाव / उदासी / लोभ / संशय / बेचैनी के साथ होने वाली
ñāṇasampayutta / ñāṇavippayutta = ज्ञान से जुड़ी / ज्ञान से अलग
diṭṭhigatasampayutta = ग़लत दृष्टि से जुड़ी
diṭṭhigatavippayuttalobhasahagata = लोभ के साथ होने वाली और ग़लत दृष्टि से अलग; diṭṭhigatasampayuttalobhasahagata = लोभ के साथ होने वाली और ग़लत दृष्टि से जुड़ी
vicikicchāsahagato / uddhaccasahagato moho = संशय / बेचैनी के साथ होने वाला मोह
sasaṅkhārikesu akusalesu = प्रेरणा सहित होने वाले हानिकर मनों में (pi-5 sasaṅkhāra = प्रयास के साथ not used: प्रयास is reserved for vāyāma/padhāna)
ahetuke cittuppāde = मूल से रहित मन की उत्पत्तियों
dvepañcaviññāṇāni = दोनों प्रकार की पाँच-पाँच इंद्रिय-चेतनाएँ
manodhātu / tisso manodhātuyo / kiriyāmanodhātu = मन का तत्व / मन के तीन तत्व / केवल क्रिया रूपी मन का तत्व
manoviññāṇadhātu / pañca ahetukamanoviññāṇadhātuyo = मन की चेतना का तत्व / मूल से रहित मन की चेतना के पाँच तत्व
kiriyāhetukamanoviññāṇadhātu somanassa-/upekkhāsahagatā = मूल से रहित केवल क्रिया रूपी मन की चेतना का वह तत्व जो प्रसन्नता / समभाव के साथ होता है
cakkhu- / sota- / ghāna- / jivhā- / kāya-viññāṇaṃ = आँख / कान / नाक / जीभ / शरीर की चेतना (pi-3/pi-5)
dukkhasahagataṃ kāyaviññāṇaṃ = दुःख के साथ होने वाली शरीर की चेतना
yā ca vedanā upekkhā = समभाव रूपी अनुभूति

## Absorptions
jhāna = ध्यान; catukkanaya / pañcakanaya = चार-चार की विधि / पाँच-पाँच की विधि (terms headings)
rūpāvacaraṃ paṭhamaṃ / catutthaṃ jhānaṃ = सूक्ष्म भौतिक लोक से संबंधित पहला / चौथा ध्यान
lokuttaraṃ paṭhamaṃ / catutthaṃ jhānaṃ = लोकोत्तर पहला / चौथा ध्यान
rūpāvacara/lokuttara-<a><b>jjhānā = सूक्ष्म भौतिक लोक से संबंधित / लोकोत्तर वे ध्यान जो चार-चार की विधि में <a> और पाँच-पाँच की विधि में <b> हैं
pañcakanaye dutiyaṃ jhānaṃ = पाँच-पाँच की विधि में … दूसरा ध्यान
catutthassa jhānassa vipāko = चौथे ध्यान का कर्म-फल
cattāro āruppā = चार अभौतिक अवस्थाएँ (pi-5 निराकार अवस्थाएँ not used: arūpa = अभौतिक in this book)
cattāro arūpāvacarā = अभौतिक लोक से संबंधित चार मन
ākāsānañcāyatana / viññāṇañcāyatana / ākiñcaññāyatana / nevasaññānāsaññāyatana = अनंत आकाश का क्षेत्र / अनंत चेतना का क्षेत्र / कुछ भी न होने का क्षेत्र / न पहचान न अ-पहचान का क्षेत्र (pi-5)

## Paths, fruits, material form
cattāro maggā apariyāpannā = अस्तित्व के लोकों में न समाए हुए चार मार्ग
cattāro ariyamaggā = चार आर्य मार्ग
sāmaññaphala = श्रमण-जीवन का फल (pi-5 sāmañña); heṭṭhimāni tīṇi = निचले तीन
upariṭṭhimaṃ arahattaphalaṃ = सबसे ऊँचा फल, अर्हत्-पद का फल
yañca rūpaṃ (na) kammassa katattā = जो भी भौतिक रूप कर्म किए जाने के कारण है (नहीं है)
yañca rūpaṃ anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ = जो भी भौतिक रूप दिखाई न देने वाला, टकराव से रहित और मन के विषयों के इंद्रिय-क्षेत्र में समाया हुआ है
anindriyabaddharūpa = इंद्रियों से न बँधा भौतिक रूप
sabbañca rūpaṃ / avasesañca rūpaṃ = सारा भौतिक रूप / शेष भौतिक रूप
mahābhūtā / catunnaṃ mahābhūtānaṃ upādāya rūpaṃ = चार महाभूत / चार महाभूतों से व्युत्पन्न भौतिक रूप
kāyaviññatti / vacīviññatti = शारीरिक संकेत / वाचिक संकेत (pi-5 «प्रकट अभिव्यक्ति» not used: अभिव्यक्ति = nirutti in the matrix)
ākāsadhātu / āpodhātu = आकाश तत्व / जल तत्व (pi-5)
rūpassa lahutā / mudutā / kammaññatā / upacayo / santati = भौतिक रूप का हल्कापन / की मृदुता / की कार्य-योग्यता / का संचय (pi-5) / की धारा (pi-5)
kabaḷīkāro āhāro = कौर-कौर खाया जाने वाला आहार (pi-5)
cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ = मन से जन्मा, मन के कारण और मन से उत्पन्न
vedanākkhandho, saññākkhandho, saṅkhārakkhandho = अनुभूति का समूह, पहचान का समूह, मानसिक रचनाओं का समूह

## Lists of defilements
kāmāsava / bhavāsava / diṭṭhāsava / avijjāsava = इंद्रिय-सुखों का मैल / अस्तित्व का मैल / ग़लत दृष्टि का मैल / अज्ञान का मैल
kāmarāga / paṭigha / māna / diṭṭhi / vicikicchā / sīlabbataparāmāsa / bhavarāga / issā / macchariya / avijjā (-saṃyojana) = इंद्रिय-सुखों के राग / चिढ़ / अहंकार / ग़लत दृष्टि / संशय / कर्मकांडों और व्रतों से चिपकाव / अस्तित्व के राग / ईर्ष्या / कंजूसी / अज्ञान का बंधन (pi-4/pi-5)
abhijjhā / byāpādo / sīlabbataparāmāso / idaṃsaccābhiniveso kāyagantho = लालच / दुर्भावना / कर्मकांडों और व्रतों से चिपकाव / “यही सत्य है” इस आग्रह रूपी काया की गाँठ
kāmacchanda / byāpāda / thinamiddha / uddhaccakukkucca / vicikicchā / avijjā (-nīvaraṇa) = इंद्रिय-सुखों की चाह / दुर्भावना / सुस्ती और तंद्रा / बेचैनी और पछतावे / संशय / अज्ञान की बाधा; uddhacca- / kukkuccanīvaraṇa = बेचैनी / पछतावे की बाधा
diṭṭhiparāmāsa = दृष्टि रूपी ग़लत धारणा
kāmupādāna / diṭṭhupādāna / sīlabbatupādāna / attavādupādāna = इंद्रिय-सुखों की / ग़लत दृष्टि की / कर्मकांडों और व्रतों की / आत्मा के सिद्धांत की आसक्ति
dasa kilesavatthūni = मन के क्लेशों के दस आधार: लोभ, द्वेष, मोह, अहंकार, ग़लत दृष्टि, संशय, सुस्ती, बेचैनी, निर्लज्जता, बुराई के प्रति निडरता
diṭṭhi (as a defilement, diṭṭhigata) = ग़लत दृष्टि (pi-5); paṭigha (aversion) = चिढ़ (pi-5), distinct from sappaṭigha = टकराव वाली

## Source notes (translated as written)
- ^1-1389: «ya vedanāya sampayuttātipi» is a truncated «adukkhamasukhāya …»; rendered as the full matrix item T2c. Because T2c itself begins with «न …», the na-vattabbā clause there is phrased as a list («इन्हें A, B या C, इनमें से कुछ भी नहीं कहा जा सकता») to avoid «न न».
- ^1-1387: «akusalato cattāro kāmāvacarakusalassa vipākato ca kiriyato ca pañca» lacks a comma; split as in the English.
- ^1-1478: the question ends with «.» not «?»; kept as «।».
- ^1-1401: «[dutiyajjhāne (sī.)]» treated as spelling-only (वर्तनी-भेद); ^1-1464 «[sabbeva (syā.)]» adds the particle eva, so पाठभेद.
- ^1-1501 / ^1-1502 (floods, yokes) are abridged in the Pāli («…pe….»); kept abridged: «<item> कौन-सी हैं…।»
