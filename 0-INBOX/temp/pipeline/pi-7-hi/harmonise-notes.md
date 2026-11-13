# pi-7 Hindi zero-shot: harmonise pass notes

Scripts (this folder): find_divergences_hi.py (divergences.md = before, divergences-after.md = after), harmonise_hi.py
(reads backup-pre-harmonise/, rerunnable; `--dry`; `--names-table` prints the table below), log harmonise-log.tsv,
helpers hz7_common.py, hz7_names.py, hz7_explore.py, hz7_ctx.py, hz7_win.py, hz7_diff.py, hz7_numcheck.py, post_checks_hi.py.
Protected and unchanged: preamble.md, 1-00-paccaya.md, 1-01 non-empty lines 1-190 and 1235-1262.

Result: 2331 lines changed in 71 files. Identical-Pāli line groups with differing Hindi: 158 -> 0; names with more than
one form: 105 -> 2; heading groups: 194 -> 1 (the 3 left are listed under "kept on purpose").

## 1. Triad and dyad names (rule N1, every heading, combined heading, closing line and cross-reference)

Starting point = the name in the triad's / dyad's own file. Six names were a participle with a complement + «वाला»
(«कर्म से उत्पन्न वाला»); they get the pi-1 item noun «परिघटनाओं». Pāli short forms (dassanattika, sanidassanattika,
micchattattika …) take the full name. «…दोनों तीन के वर्गीकरण» (ttikadvaya) follows the triad.

| Pāli | Hindi |
|---|---|
| Kusalattikaṃ | हितकर वाला तीन का वर्गीकरण |
| Vedanāttikaṃ | अनुभूति वाला तीन का वर्गीकरण |
| Vipākattikaṃ | कर्म-फल वाला तीन का वर्गीकरण |
| Upādinnattikaṃ | कर्म से उत्पन्न परिघटनाओं वाला तीन का वर्गीकरण (fixed) |
| Saṃkiliṭṭhattikaṃ | क्लेशों से मलिन परिघटनाओं वाला तीन का वर्गीकरण (fixed) |
| Vitakkattikaṃ | आरंभिक विचार वाला तीन का वर्गीकरण |
| Pītittikaṃ | उल्लास वाला तीन का वर्गीकरण |
| Dassanenapahātabbattikaṃ (also dassanattika) | सत्य-दर्शन से छोड़ी जाने वाली परिघटनाओं वाला तीन का वर्गीकरण |
| Dassanenapahātabbahetukattikaṃ (also dassanahetuttika) | सत्य-दर्शन से छोड़े जाने वाले मूलों वाला तीन का वर्गीकरण |
| Ācayagāmittikaṃ | संचय की ओर ले जाने वाला तीन का वर्गीकरण |
| Sekkhattikaṃ | सीखने के चरण वाला तीन का वर्गीकरण |
| Parittattikaṃ | सीमित वाला तीन का वर्गीकरण |
| Parittārammaṇattikaṃ | सीमित विषय वाला तीन का वर्गीकरण |
| Hīnattikaṃ | हीन वाला तीन का वर्गीकरण |
| Micchattaniyatattikaṃ (also micchattattika) | ग़लत दिशा में निश्चित परिघटनाओं वाला तीन का वर्गीकरण (fixed) |
| Maggārammaṇattikaṃ | मार्ग को विषय बनाने वाला तीन का वर्गीकरण |
| Uppannattikaṃ | उत्पन्न वाला तीन का वर्गीकरण |
| Atītattikaṃ | अतीत वाला तीन का वर्गीकरण |
| Atītārammaṇattikaṃ | अतीत के विषय वाला तीन का वर्गीकरण |
| Ajjhattattikaṃ | स्वयं से संबंधित परिघटनाओं वाला तीन का वर्गीकरण (fixed) |
| Ajjhattārammaṇattikaṃ | स्वयं से संबंधित विषय वाला तीन का वर्गीकरण |
| Sanidassanasappaṭighattikaṃ (also sanidassanattika) | दिखाई देने वाला और टकराव वाला तीन का वर्गीकरण |
| Hetudukaṃ | मूल वाला दो का वर्गीकरण |
| Sahetukadukaṃ | मूल वाली परिघटनाओं वाला दो का वर्गीकरण |
| Hetusampayuttadukaṃ | मूलों से जुड़ी परिघटनाओं वाला दो का वर्गीकरण |
| Hetusahetukadukaṃ | मूल रूपी भी और मूल वाली भी परिघटनाओं वाला दो का वर्गीकरण |
| Hetuhetusampayuttadukaṃ | मूल रूपी भी और मूलों से जुड़ी भी परिघटनाओं वाला दो का वर्गीकरण |
| Nahetusahetukadukaṃ | मूल रूपी न होने वाली, पर मूल वाली परिघटनाओं वाला दो का वर्गीकरण |
| Sappaccayadukaṃ | कारणों पर निर्भर रहने वाली परिघटनाओं वाला दो का वर्गीकरण |
| Saṅkhatadukaṃ | निर्मित परिघटनाओं वाला दो का वर्गीकरण |
| Sanidassanadukaṃ | दिखाई देने वाली परिघटनाओं वाला दो का वर्गीकरण |
| Sappaṭighadukaṃ | टकराव वाली परिघटनाओं वाला दो का वर्गीकरण |
| Rūpīdukaṃ | भौतिक परिघटनाओं वाला दो का वर्गीकरण |
| Lokiyadukaṃ | लौकिक परिघटनाओं वाला दो का वर्गीकरण |
| Kenaciviññeyyadukaṃ | किसी एक प्रकार की चेतना से जानी जा सकने वाली परिघटनाओं वाला दो का वर्गीकरण |
| Āsavadukaṃ | मन के मैल वाला दो का वर्गीकरण |
| Sāsavadukaṃ | मन के मैलों के विषय वाला दो का वर्गीकरण |
| Āsavasampayuttadukaṃ | मन के मैलों से जुड़ाव वाला दो का वर्गीकरण |
| Āsavasāsavadukaṃ | मन के मैल और मन के मैलों के विषय वाला दो का वर्गीकरण |
| Āsavaāsavasampayuttadukaṃ | मन के मैल और मन के मैलों से जुड़ाव वाला दो का वर्गीकरण |
| Āsavavippayuttasāsavadukaṃ | मन के मैलों से अलगाव और मन के मैलों के विषय वाला दो का वर्गीकरण |
| Saññojana- / Saññojaniya- / Saññojanasampayutta- / Saññojanasaññojaniya- / Saññojanasaññojanasampayutta- / Saññojanavippayuttasaññojaniyadukaṃ | बंधन / बंधनों के विषय / बंधनों से जुड़ाव / बंधन और बंधनों के विषय / बंधन और बंधनों से जुड़ाव / बंधनों से अलगाव और बंधनों के विषय वाला दो का वर्गीकरण |
| Gantha- … (same six) | गाँठ / गाँठों के विषय / गाँठों से जुड़ाव / गाँठ और गाँठों के विषय / गाँठ और गाँठों से जुड़ाव / गाँठों से अलगाव और गाँठों के विषय वाला दो का वर्गीकरण |
| Nīvaraṇa- … (same six) | बाधा / बाधाओं के विषय / बाधाओं से जुड़ाव / बाधा और बाधाओं के विषय / बाधा और बाधाओं से जुड़ाव / बाधाओं से अलगाव और बाधाओं के विषय वाला दो का वर्गीकरण |
| Parāmāsa- / Parāmaṭṭha- / Parāmāsasampayutta- / Parāmāsaparāmaṭṭha- / Parāmāsavippayuttaparāmaṭṭhadukaṃ | ग़लत धारणा / ग़लत धारणा के विषय / ग़लत धारणा से जुड़ाव / ग़लत धारणा और ग़लत धारणा के विषय / ग़लत धारणा से अलगाव और ग़लत धारणा के विषय वाला दो का वर्गीकरण |
| Sārammaṇadukaṃ | विषय वाली परिघटनाओं वाला दो का वर्गीकरण |
| Cittadukaṃ | मन रूपी परिघटनाओं वाला दो का वर्गीकरण |
| Cetasikadukaṃ | मन की सहचर परिघटनाओं वाला दो का वर्गीकरण |
| Cittasampayuttadukaṃ | मन से जुड़ी परिघटनाओं वाला दो का वर्गीकरण |
| Cittasaṃsaṭṭhadukaṃ | मन से घुली-मिली परिघटनाओं वाला दो का वर्गीकरण |
| Cittasamuṭṭhānadukaṃ | मन से उत्पन्न परिघटनाओं वाला दो का वर्गीकरण |
| Cittasahabhūdukaṃ | मन के साथ-साथ होने वाली परिघटनाओं वाला दो का वर्गीकरण |
| Cittānuparivattidukaṃ | मन का अनुसरण करने वाली परिघटनाओं वाला दो का वर्गीकरण |
| Cittasaṃsaṭṭhasamuṭṭhānadukaṃ | मन से घुली-मिली और मन से उत्पन्न परिघटनाओं वाला दो का वर्गीकरण |
| Cittasaṃsaṭṭhasamuṭṭhānasahabhūdukaṃ | मन से घुली-मिली, मन से उत्पन्न और मन के साथ-साथ होने वाली परिघटनाओं वाला दो का वर्गीकरण |
| Cittasaṃsaṭṭhasamuṭṭhānānuparivattidukaṃ | मन से घुली-मिली, मन से उत्पन्न और मन का अनुसरण करने वाली परिघटनाओं वाला दो का वर्गीकरण |
| Ajjhattikadukaṃ | आंतरिक परिघटनाओं वाला दो का वर्गीकरण |
| Upādādukaṃ | व्युत्पन्न परिघटनाओं वाला दो का वर्गीकरण |
| Upādinnadukaṃ | कर्म से उत्पन्न परिघटनाओं वाला दो का वर्गीकरण |
| Upādānadukaṃ | आसक्ति वाला दो का वर्गीकरण |
| Upādāniyadukaṃ | आसक्ति का विषय बनने वाली परिघटनाओं वाला दो का वर्गीकरण |
| Upādānasampayuttadukaṃ | आसक्ति से जुड़ी परिघटनाओं वाला दो का वर्गीकरण |
| Upādānaupādāniyadukaṃ | आसक्ति रूपी भी और आसक्ति का विषय बनने वाली भी परिघटनाओं वाला दो का वर्गीकरण |
| Upādānaupādānasampayuttadukaṃ | आसक्ति रूपी भी और आसक्ति से जुड़ी भी परिघटनाओं वाला दो का वर्गीकरण |
| Upādānavippayuttaupādāniyadukaṃ | आसक्ति से अलग, पर उसका विषय बनने वाली परिघटनाओं वाला दो का वर्गीकरण |
| Kilesadukaṃ | मन के क्लेश वाला दो का वर्गीकरण |
| Saṃkilesikadukaṃ | क्लेशों का विषय बनने वाला दो का वर्गीकरण |
| Saṃkiliṭṭhadukaṃ | क्लेशों से मलिन परिघटनाओं वाला दो का वर्गीकरण (fixed) |
| Kilesasampayuttadukaṃ | क्लेशों से जुड़ाव वाला दो का वर्गीकरण |
| Kilesasaṃkilesikadukaṃ | मन के क्लेश और क्लेशों का विषय बनने वाला दो का वर्गीकरण |
| Kilesasaṃkiliṭṭhadukaṃ | मन के क्लेश और क्लेशों से मलिन परिघटनाओं वाला दो का वर्गीकरण (fixed) |
| Kilesakilesasampayuttadukaṃ | मन के क्लेश और क्लेशों से जुड़ाव वाला दो का वर्गीकरण |
| Kilesavippayuttasaṃkilesikadukaṃ | क्लेशों से अलगाव और क्लेशों का विषय बनने वाला दो का वर्गीकरण |
| Dassanenapahātabbadukaṃ | सत्य-दर्शन से छोड़े जाने वाला दो का वर्गीकरण |
| Bhāvanāyapahātabbadukaṃ | मानसिक अभ्यास से छोड़े जाने वाला दो का वर्गीकरण |
| Dassanenapahātabbahetukadukaṃ | सत्य-दर्शन से छोड़े जाने वाले मूलों वाला दो का वर्गीकरण |
| Bhāvanāyapahātabbahetukadukaṃ | मानसिक अभ्यास से छोड़े जाने वाले मूलों वाला दो का वर्गीकरण |
| Savitakka- / Savicāra- / Sappītika- / Pītisahagata- / Sukhasahagata- / Upekkhāsahagatadukaṃ | आरंभिक विचार / सतत विचार / उल्लास / उल्लास के साथ होने / सुख के साथ होने / समभाव के साथ होने वाला दो का वर्गीकरण |
| Kāmāvacara- / Rūpāvacara- / Arūpāvacaradukaṃ | इंद्रिय-सुखों के लोक / सूक्ष्म भौतिक लोक / अभौतिक लोक वाला दो का वर्गीकरण |
| Pariyāpanna- / Niyyānika- / Niyata- / Sauttara- / Saraṇadukaṃ | अस्तित्व के लोकों में समाए होने / मुक्ति की ओर ले जाने / निश्चित / सर्वोच्च न होने / संघर्ष वाला दो का वर्गीकरण |

Cluster names were already uniform (pi-1: मूलों का वर्ग, बीच के छोटे / बड़े दो-दो के वर्गीकरण, अंतिम दो-दो के वर्गीकरण …).
Oghādidukāni = «बाढ़ आदि वाले दो-दो के वर्गीकरण» (3-06).

## 2. Other forms chosen (order of authority: sample/terms, 1-01, pi-1/pi-2/pi-6, majority)

| Pāli | Hindi | why |
|---|---|---|
| Paccanīyuddhāro | नकारात्मक क्रम के लिए कारणों की छँटाई | 1-01 (5 other forms) |
| niṭṭhitaṃ / niṭṭhito (closings) | … समाप्त। (no quotes around a name) | 1-01 (was also पूरा हुआ / पूरे हुए) |
| sahajātaṃ, purejātaṃ, pacchājātaṃ, āhāraṃ, indriyaṃ (labels) | सह-उत्पत्ति, पूर्व-उत्पत्ति, पश्चात्-उत्पत्ति, आहार, क्षमता (no «रूपी») | 1-01; compounds keep «रूपी» (सह-उत्पत्ति रूपी प्रधानता) |
| nānākkhaṇikā | भिन्न क्षण | 1-01 (was भिन्न क्षण रूपी / भिन्न-क्षणिक / भिन्न क्षणों वाला) |
| anulomaṃ (moment) | अनुरूपता | 1-01 (was अनुकूलता (का क्षण)) |
| bhavaṅga | जीवन-धारा (fem.: «X वाली जीवन-धारा … कारण होती है») | 1-01..1-05 (was जीवन-धारा का मन / जीवन-प्रवाह) |
| cuticitta / upapatticitta | मृत्यु का मन / जन्म का मन | 1-02..1-05, 2-01..2-03 (was मृत्यु-क्षण / जन्म-क्षण / उत्पत्ति का मन) |
| vuṭṭhāna | बाहर आना / बाहर आने के लिए | 1-01 (was उत्थान, बाहर आने वाला मन) |
| nirodhā vuṭṭhahantassa | समाप्ति की ध्यान-अवस्था से बाहर आने वाले व्यक्ति में | 1-01 |
| parikamma | प्रारंभिक तैयारी | 1-01 (was तैयारी / प्रारंभिक अभ्यास) |
| āvajjanā | मन को विषय की ओर मोड़ना | 1-01 (was … मोड़ने की क्रिया) |
| ghaṭanā / Xghaṭanā / sāmañña / pakiṇṇaka | संयोजन / X-कारण के संयोजन / सामान्य / फुटकर | 1-01 (was मेल, वाले, साझा, मिश्रित) |
| ghaṭanā count «A-B-…nti n» | A-कारण, B-कारण … और Z-कारण के संयोजन में n (no quotes) | sample count_hi |
| sabhāga | X-कारण के साथी कारण | 1-01 |
| mūla / mūlaka (series start) | … से शुरू होने वाली शृंखला (में) | terms file (was आरंभ-बिंदु, से शुरू होने वाले में) |
| Mūlaṃ kātabbaṃ / pucchitabbaṃ | मूल वाक्य | majority (was आरंभिक पद, मूल पद) |
| gamana | प्रसंग | majority; «क्रम» is anuloma/paccanīya (was दौर, क्रम) |
| (cakkaṃ) / cakkaṃ kātabbaṃ / bandhitabbaṃ | (चक्र) / चक्र बनाना चाहिए / चक्र बाँधना चाहिए | 1-01 (was बारी-बारी से, चक्र जोड़ना) |
| ninnānākaraṇaṃ / ninnānaṃ | बिना किसी अंतर के | majority |
| number words beyond 23 | already uniform (checked by hz7_numcheck.py) | |
| nanahetu etc. | मूल रूपी न होने वाली न होने वाली (no quotes, nested quotes too) | brief |
| na + a pi-1 item (nadassanena / nabhāvanāya pahātabba(hetuka), napīti- / nasukha- / naupekkhāsahagata) | सत्य-दर्शन से न छोड़ी जाने वाली, … मूलों से रहित, उल्लास के साथ न होने वाली | pi-1 dyads 83-86, 90-92 (5-04, 5-13..5-20); 5-05..5-12 had «<item> न होने वाली» |
| X ceva na ca Y | pi-1 wording (was already uniform) | |
| {…} without siglum | [पाठभेद: <Pāli>] | 5-15 (5-07, 5-10, 5-12 had translated it) |
| count lines | sample count_hi: no comma between consecutive locatives the Pāli does not separate | 4-02..4-07 had added them |
| pañhā chains «…Xpaccayena paccayo… Ypaccayena paccayo» | verb after each condition | 1-01 and all files but 3-01, 3-02, 3-10 |
| 2-6. …sampayuttavāro | … और जुड़ाव का खंड | majority |
| Hetu-ārammaṇapaccayādi etc. | मूल-कारण और विषय-कारण आदि | terms file «X-कारण और Y-कारण» |
| X-vārasadiso | X के खंड के समान | grammar (2-10, 2-15 had «का खंड के समान») |
| identical notes (Yathā kusalattike…, Evaṃ itare dve gaṇanāpi…, Sahajātavārampi… etc.) | majority form, by whole line (W1) | |

## 3. Kept on purpose

- «Hetudukaṃ» as a counting heading = «मूल-कारण के साथ दो कारणों का मेल», as a dyad title = «मूल वाला दो का वर्गीकरण» (same Pāli, two meanings).
- «Parāmāsadukāni» (plural heading, 5-10) = «ग़लत धारणा वाले दो के वर्गीकरण».
- Quotation marks around quoted words inside notes (“कर्म-फल” निश्चित करना चाहिए …) and around «“कारण-संबंध”».
- 5-04 / 5-13..5-20 «X ceva nano/nana ca Y» (negated items, fused slips in 5-04): mixed «… भी और … भी» / «…, पर स्वयं …» left as built.
- kātabba renderings (बनाना / तैयार करना / करना / शामिल करना) differ with the object; only identical lines unified.
- Dyad names: own-file styles kept (noun style in 3-03..3-08 and 4-01: «मन के मैलों के विषय / से जुड़ाव / से अलगाव»; item style in 3-01, 3-02, 3-09, 3-10).
- Source slips translated as written (agent notes) untouched.

## 4. Builders that would need the same change (outputs were edited, builders were not rerun)

- names: build_1-02_1-05 (upādinna, saṃkiliṭṭha), build_2-01_2-03 (closing quotes), build_2-09_2-17 (micchattaniyata, ajjhatta),
  build_4-01 (saṃkiliṭṭha, kilesasaṃkiliṭṭha dyads), build_4-02_4-07, build_4-08_4-15 (DUKA_X / TIKA_X), build_4-16_5-04,
  build_5-05_5-12 (heading labels), build_5-13_5-20 (triad / dyad names).
- Paccanīyuddhāro: all builders except build_1-01 and build_1-02_1-05.
- niṭṭhita «समाप्त»: build_4-02_4-07, build_4-08_4-15, build_5-05_5-12.
- labels without «रूपी», nānākkhaṇikā: build_1-02_1-05, build_3-09, build_4-01, build_2-01_2-03, build_2-04_2-08.
- anuloma: build_1-02_1-05, build_3-01_3-02_3-10, build_4-01. bhavaṅga: build_2-01_2-03, build_2-04_2-08, build_2-09_2-17,
  build_3-01_3-02_3-10, build_4-01. cuti / upapatti: build_4-01, build_2-09_2-17. parikamma: build_1-02_1-05, build_3-01_3-02_3-10,
  build_4-01. vuṭṭhāna: build_2-04_2-08, build_3-01_3-02_3-10, build_3-03_3-08. nirodhā vuṭṭhahantassa: build_1-02_1-05,
  build_2-01_2-03, build_2-04_2-08, build_2-09_2-17, build_3-01_3-02_3-10, build_3-03_3-08, build_3-09, build_4-01.
  āvajjanā: build_2-04_2-08.
- ghaṭanā / sabhāga: build_1-02_1-05, build_2-09_2-17, build_3-01_3-02_3-10, build_3-09, build_4-08_4-15.
- mūla: build_5-13_5-20, build_4-08_4-15, build_3-01_3-02_3-10, build_3-09. gamana: build_2-04_2-08, build_2-09_2-17,
  build_3-01_3-02_3-10, build_3-03_3-08, build_4-01, build_4-02_4-07, build_4-08_4-15. cakkaṃ: build_3-01_3-02_3-10,
  build_3-03_3-08, build_4-01. ninnāna: build_2-04_2-08, build_2-09_2-17, build_4-01.
- quotes in negations: build_5-13_5-20. pi-1 na-items: build_5-05_5-12. {…}: build_5-05_5-12. count commas: build_4-02_4-07.
  chain verbs: build_3-01_3-02_3-10. «का खंड» heading: build_2-01_2-03, build_2-04_2-08, build_3-03_3-08.
  «X और Y आदि» headings: build_4-08_4-15, build_4-16_5-04, build_5-13_5-20. «के खंड के समान»: build_2-09_2-17.
