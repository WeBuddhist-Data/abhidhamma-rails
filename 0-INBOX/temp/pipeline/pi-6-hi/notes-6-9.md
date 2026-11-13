# Notes: 6-01/6-02 (Saṅkhārayamaka), 9-01/9-02/9-03 (Dhammayamaka), Hindi plain zero-shot

Builders: build_6_hi.py, build_9_hi.py (shared: common_6_9_hi.py; checks: check_6_9_extra.py; helper: analyze_6_9.py).
New recurring terms and frames settled here (Pāli = Hindi):

## Saṅkhārayamaka items
kāyasaṅkhāro = शरीर की रचना (pi-2/pi-5)
vacīsaṅkhāro = वाणी की रचना (pi-2/pi-5)
cittasaṅkhāro = मन की रचना (pi-2/pi-5)
(subject feminine singular: verbs from VERBS_F, e.g. उत्पन्न होती है / समाप्त नहीं हुई थी)
kāyo (bare) = शरीर
vacī (bare) = वाणी
cittaṃ (bare) = मन
saṅkhāro (bare, sg.) = रचना
saṅkhārā (bare, pl.) = रचनाएँ
Assāsapassāsā = साँस लेना और छोड़ना (pi-5)
vitakkavicārā = आरंभिक विचार और सतत विचार (pi-2/pi-5)
cittasampayuttakā dhammā = मन से जुड़ी परिघटनाएँ
Uppajjittha. (short answer, fem. sg.) = उत्पन्न हुई थी।
Nirujjhittha. (short answer, fem. sg.) = समाप्त हुई थी।
yo X parijānāti so Y parijānāti? = जो X को पूरी तरह समझता है, क्या वह Y को पूरी तरह समझता है?

## Dhammayamaka items
kusalā / akusalā / abyākatā dhammā (subject) = हितकर / हानिकर / नैतिक रूप से अनिर्धारित परिघटनाएँ
kusalā (bare, paṇṇatti pairs) = हितकर; dhammā (bare) = परिघटनाएँ
Feminine plural verbs (परिघटनाएँ): uppajjanti = उत्पन्न होती हैं / न उप्प. = उत्पन्न नहीं होतीं; uppajjittha (with pl. subject) = उत्पन्न हुई थीं / उत्पन्न नहीं हुई थीं; uppajjissanti = उत्पन्न होंगी / उत्पन्न नहीं होंगी; nirujjhanti = समाप्त होती हैं / समाप्त नहीं होतीं; nirujjhittha = समाप्त हुई थीं / समाप्त नहीं हुई थीं; nirujjhissanti = समाप्त होंगी / समाप्त नहीं होंगी
C dhammā dhammā ceva C dhammā ca. = C, परिघटनाएँ भी हैं और C भी। (plural of the sample's QA_ANU_2)
Avasesā dhammā na C dhammā. = शेष परिघटनाएँ, C नहीं हैं।
Kusalaṃ ṭhapetvā avasesā dhammā na kusalā, dhammā. = हितकर को छोड़कर शेष परिघटनाएँ, हितकर नहीं हैं, पर परिघटनाएँ हैं।
Kusalañca dhamme ca ṭhapetvā avasesā na ceva kusalā na ca dhammā. = हितकर और परिघटनाओं को छोड़कर शेष न तो हितकर हैं, न परिघटनाएँ।
kusalaṃ dhammaṃ bhāveti = हितकर परिघटना का अभ्यास करता है; na bhāveti = … का अभ्यास नहीं करता
akusalaṃ dhammaṃ pajahati = हानिकर परिघटना को छोड़ता है; nappajahati = … को नहीं छोड़ता

## Short answers
No. = नहीं। (pi-2)
Natthi. = ऐसा कोई नहीं है।
Āmantā…pe…. = हाँ…।

## Section headings / markers
Suddhasaṅkhāravāro = केवल रचनाओं का खंड (terms file)
Suddhadhammavāro = केवल परिघटनाओं का खंड; Suddhadhammamūlacakkavāro = केवल परिघटनाओं पर आधारित चक्र का खंड
Pavattivāro = प्रक्रिया का खंड; Uppādavāro = उत्पन्न होने का खंड; Nirodhavāro = समाप्त होने का खंड; Uppādanirodhavāro = उत्पन्न होने और समाप्त होने का खंड
<X>vāro. (closing line) = <X का खंड>। (e.g. Uppādavāro. = उत्पन्न होने का खंड।, Paṇṇattivāro. = शब्दावली का खंड।)
Pavattivāro niṭṭhito. = प्रक्रिया का खंड पूरा हुआ।
1-6. Paccuppannavārādi = 1-6. वर्तमान का खंड आदि
yassaka / yatthaka / yassayatthaka (editorial notes) = व्यक्ति वाला भाग / स्थान वाला भाग / व्यक्ति और स्थान वाला भाग
sadisaṃ = समान; vitthāretabbaṃ = विस्तार देना चाहिए; vibhajitabbaṃ = विभाजित करना चाहिए; natthi nānākaraṇaṃ = कोई अंतर नहीं है
atītā pucchā = अतीत के प्रश्न

## Answer prefixes (who / where / when); chunks joined with ", "
Locative place + following phrase joined with a space; "vinā …", "pavatte", "tesaṃyeva" joined with a space to the next chunk; "dutiye citte vattamāne" joined with a space to the previous one.
uppādakkhaṇe / bhaṅgakkhaṇe = के उत्पन्न होने के क्षण में / के भंग होने के क्षण में (terms file)
Sabbesaṃ cittassa … = सभी के मन के …
tassa cittassa … = उस मन के …
assāsapassāsānaṃ … = साँस लेने और छोड़ने के …
vitakkavicārānaṃ … = आरंभिक विचार और सतत विचार के …
kusalānaṃ / akusalānaṃ / kusalākusalānaṃ … = हितकर / हानिकर / हितकर और हानिकर परिघटनाओं के …
kusalavippayuttacitta = हितकर से अलग मन; akusalavippayuttacitta = हानिकर से अलग मन; kusalavippayuttaakusalavippayuttacitta = हितकर से अलग और हानिकर से अलग मन
avitakkaavicāracitta = आरंभिक विचार और सतत विचार से रहित मन
pacchimacitta = अंतिम मन; savitakkasavicārapacchimacitta = आरंभिक विचार और सतत विचार वाला अंतिम मन; avitakkaavicārapacchimacitta = आरंभिक विचार और सतत विचार से रहित अंतिम मन
Kāmāvacarānaṃ pacchimacittassa … = इंद्रिय-सुखों के लोक के प्राणियों के अंतिम मन के …
aggamagga = सर्वोच्च मार्ग; Aggamaggasamaṅgīnaṃ = सर्वोच्च मार्ग से युक्त लोगों में; arahantānaṃ = अर्हतों में
pacchimacittasamaṅgīnaṃ = अंतिम मन से युक्त लोगों में; avitakkaavicārapacchimacittasamaṅgīnaṃ = आरंभिक विचार और सतत विचार से रहित अंतिम मन से युक्त लोगों में
vinā assāsapassāsehi = साँस लेने और छोड़ने के बिना; vinā vitakkavicārehi = आरंभिक विचार और सतत विचार के बिना
nirodhasamāpannānaṃ = समाप्ति की ध्यान-अवस्था में लीन लोगों में (pi-5 nirodhasamāpatti)
Paṭhamajjhānaṃ samāpannānaṃ = ध्यान की पहली अवस्था में लीन लोगों में; Dutiyajjhānaṃ tatiyajjhānaṃ samāpannānaṃ = ध्यान की दूसरी और तीसरी अवस्था में लीन लोगों में (runs: पहली, दूसरी और तीसरी)
Paṭhamajjhāne / Dutiyajjhāne tatiyajjhāne (place) = ध्यान की पहली अवस्था में / ध्यान की दूसरी और तीसरी अवस्था में
kāmāvacare / rūpāvacare / arūpāvacare = इंद्रिय-सुखों के लोक में / सूक्ष्म भौतिक लोक में / अभौतिक लोक में (runs: सूक्ष्म भौतिक लोक और अभौतिक लोक में)
kāmāvacarānaṃ / rūpāvacarānaṃ arūpāvacarānaṃ = इंद्रिय-सुखों के लोक के प्राणियों में / सूक्ष्म भौतिक लोक और अभौतिक लोक के प्राणियों में
Catuvokāre pañcavokāre = चार समूहों वाले और पाँच समूहों वाले अस्तित्व में; catuvokārānaṃ pañcavokārānaṃ = चार समूहों वाले और पाँच समूहों वाले अस्तित्व के प्राणियों में
Itaresaṃ (alone) = बाकी सबमें; itaresaṃ + beings = बाकी …
Sabbesaṃ upapajjantānaṃ = सभी जन्म लेने वालों में
suddhāvāsānaṃ dutiye citte vattamāne = शुद्ध निवास लोक के प्राणियों में दूसरे मन के चलते समय; dutiye akusale citte vattamāne = दूसरे हानिकर मन के चलते समय
pacchimabhavikānaṃ = अंतिम जन्म वालों में (terms file)
Savitakkasavicārabhūmiyaṃ / Avitakkaavicārabhūmiyaṃ = आरंभिक विचार और सतत विचार वाले स्तर पर / आरंभिक विचार और सतत विचार से रहित स्तर पर (bhūmi = स्तर, pi-1)
tesaṃyeva = उन्हीं में
yassa cittassa anantarā aggamaggaṃ paṭilabhissanti = जो इस मन के ठीक बाद सर्वोच्च मार्ग प्राप्त करेंगे, उनमें
… tassa cittassa uppādakkhaṇe = जिस मन के ठीक बाद वे सर्वोच्च मार्ग प्राप्त करेंगे, उस मन के उत्पन्न होने के क्षण में
yassa cittassa anantarā kāmāvacarānaṃ pacchimacittaṃ uppajjissati = इंद्रिय-सुखों के लोक के जिन प्राणियों में इस मन के ठीक बाद अंतिम मन उत्पन्न होगा, उनमें
yassa cittassa anantarā avitakkaavicāraṃ pacchimacittaṃ uppajjissati = जिनमें इस मन के ठीक बाद आरंभिक विचार और सतत विचार से रहित अंतिम मन उत्पन्न होगा, उनमें
rūpāvacare arūpāvacare pacchimabhavikānaṃ ye ca rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ = सूक्ष्म भौतिक लोक और अभौतिक लोक में अंतिम जन्म वालों में और जो सूक्ष्म भौतिक लोक या अभौतिक लोक में जन्म लेकर पूर्ण निर्वाण पाएँगे, उन मरने वालों में

## Source slips (translated as written)
6-02 ^6-6-121 (nirodhavāra, (6) Atītānāgatavāro, anulomapuggalokāsā): "kāyasaṅkhāro na nirujjhittha vacīsaṅkhāro ca nirujjhissati" (expected "kāyasaṅkhāro ca nirujjhittha") = शरीर की रचना समाप्त नहीं हुई थी और वाणी की रचना भी समाप्त होगी।
6-01 "4 (Ṅa) paccanīkaokāso ^6-6-65" is a plain line (not a heading) with a stray "4"; 9-01 "#### 3 Suddhadhammavāro", "#### 4 Suddhadhammamūlacakkavāro" carry stray numbers; kept.
6-01 "##### (Ṅa) paccanīkaokāsā" (plural form) = (ङ) नकारात्मक: स्थान.
