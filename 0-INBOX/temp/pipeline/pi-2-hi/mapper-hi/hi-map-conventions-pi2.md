# pi-2 Pāli→Hindi keyword map: conventions beyond pi-1 (settled on the sample: preamble, 1-khandhavibhango)

Read with `..\hi-mapper-brief.md` and the binding pi-1 file `..\..\pi-1-hi\mapper-hi\hi-map-conventions.md`. Everything there still holds (dhammā = singular परिघटना, masculine direct singular for adjectives/participles, members of compounds, positive part for fragments that lost a negative, no ", " inside a value, " … " for gaps). This file only adds what pi-2 needs.

## Tooling (`map_sample_hi.py`, import it, do not edit it)
- Importing it writes nothing and prints nothing. It reads `map_common_hi.py` (pi-1) read-only for `present()` and `CH2`.
- `read_keywords / read_hindi / read_pali(ch)` use the pi-2 paths.
- `PI2` is the default table settled on the sample. Lookup is case-insensitive on the first letter. `CH2` (pi-1 cittuppāda table) is the last fallback.
- `pi2_value(kw, kws, table, bid, text)` applies the table plus the context rules below. Pass `text` (the segment's Hindi) so the two fallback variants can apply.
- `prior(kw)` returns the values the same Pāli got in the pi-1/3/4/5 Hindi maps. Use it to stay consistent with the earlier books.
- `build_part(ch, resolver)` and `verify(ch, allowed={(bid, kw): reason})` work like the pi-1 helpers. `verify` lists the allowed presence exceptions separately.
- Chapter script pattern: `OVR[bid][kw]` first, then `pi2_value(kw, kws, {**PI2, **YOUR_T}, bid, text)`. Put Pañhāpucchaka segment ids into `PP_SEGMENTS` (see na below).
- Helpers: `show_1-khandhavibhango_hi.py <ch> id …` prints the Pāli, Hindi and keywords. `audit_1-khandhavibhango_hi.py <ch> [multi]` lists every keyword with the distinct values it got. `kwlist_1-khandhavibhango_hi.py <ch>` lists the unique keywords with their pi-1/3/4/5 values.

## Book frame and headings
- Vibhaṅga = Vibhaṅgapāḷi = विस्तृत विश्लेषण (book title). pāḷi = (no direct equivalent), because the Hindi title has no word for "book".
- vibhaṅgo (Khandhavibhaṅgo «समूहों का विश्लेषण») = विश्लेषण. bhājanīyaṃ = विश्लेषण. Suttanta = उपदेश (the Hindi has «उपदेशों के अनुसार»). Abhidhamma = अभिधम्म.
- Pañhāpucchakaṃ = प्रश्नोत्तर. Pañhā = प्रश्न (part of प्रश्नोत्तर, pi-3 precedent).
- Tikaṃ / Tika / tikā = तीन-तीन के वर्गीकरण. Dukaṃ / Duka = दो-दो के वर्गीकरण. tike (kusalattike) = तीन के वर्गीकरण. mūlakaṃ (Duka-/Tikamūlakaṃ) = पर आधारित क्रम. Ubhato = दोनों ओर से. vaḍḍhakaṃ = बढ़ने वाला क्रम. vitthāro = विस्तार.
- (Yathā rūpakaṇḍe vibhattaṃ …): kaṇḍe = अध्याय, vibhattaṃ = विश्लेषण किया गया. niṭṭhito = पूरा हुआ.

## The aggregates (khandha = समूह)
- khandha / khandho / khandhā / khandhānaṃ = समूह. X-kkhandho (any case) = «X का समूह»: rūpa भौतिक रूप का समूह, vedanā अनुभूति का समूह, saññā पहचान का समूह, saṅkhāra मानसिक रचनाओं का समूह, viññāṇa चेतना का समूह.
- The bare members: rūpa / rūpaṃ = भौतिक रूप, vedanā = अनुभूति, saññā = पहचान, saṅkhāra / saṅkhārā = मानसिक रचनाएँ (pi-1 fixed plural form), viññāṇa / viññāṇaṃ = चेतना, cetanā = इरादा.

## Number of ways
- vidhena = प्रकार (pi-1). Ekavidhena … Dasavidhena = एक … दस प्रकार, Ekādasa- ग्यारह, Catuvīsati- चौबीस, Tiṃsa-/Tiṃsati- तीस, Bahu- अनेक. Catubbidhena = चार प्रकार, Chabbidhena = छह प्रकार.
- «dasavidhena X-kkhandho» = «दस प्रकार से X का समूह» (likewise for the other numbers).

## Suttanta definitions (atīta … santike strings)
- Tattha = यहाँ. Yaṃ kiñci / Yā kāci / Ye keci = जो भी. yaṃ vā panaññampi = या जो भी अन्य.
- tadekajjhaṃ = उस सबको एक साथ. For a plural subject (saṅkhārā) the Hindi has उन सबको, so the value follows it. abhisaññūhitvā = इकट्ठा करके. abhisaṅkhipitvā = संक्षेप में समेटकर.
- The synonym string, each member to its own item, masculine singular: niruddha समाप्त हो चुका, vigata जा चुका, vipariṇata बदल चुका, abbhatthaṅgata पूरी तरह अस्त हो चुका, uppajjitvā उत्पन्न होकर, atītaṃsena अतीत के अंतर्गत, saṅgahita वर्गीकृत, jāta जन्मा हुआ, nibbatta पैदा हुआ, abhinibbatta पूरी तरह पैदा हुआ, pātubhūta प्रकट हुआ, uppanna उत्पन्न, uṭṭhita उठा हुआ, samuṭṭhita भली-भाँति उठा हुआ. The negative members (anibbattaṃ …) are fragments: the positive part.
- atīta / anāgata / paccuppanna = अतीत का / भविष्य का / वर्तमान का. upādāya = व्युत्पन्न. bhūtā = महाभूत (pi-1). upādāyarūpaṃ = व्युत्पन्न भौतिक रूप.
- ajjhattaṃ = स्वयं में (pi-1). paccattaṃ = अपना. pāṭipuggalika = हर व्यक्ति का निजी. parapuggalānaṃ = दूसरा व्यक्ति.
- oḷārika स्थूल, sukhuma सूक्ष्म, hīna हीन, paṇīta उत्तम. upādāyupādāya = तुलना करके. daṭṭhabba = समझना चाहिए. upakaṭṭhe = समीप. samāpannassa = ध्यान-अवस्था में लीन व्यक्ति (pi-1).
- The hīna/paṇīta string (2-6): uññāta तुच्छ समझा गया, avaññāta तिरस्कृत, hīḷita निंदित, paribhūta अपमानित, acittīkata असम्मानित, cittīkata सम्मानित, hīnamata हीन माना गया, aniṭṭha अनचाहा, akanta अप्रिय, amanāpa मन को न भाने वाला, iṭṭha मनचाहा, kanta प्रिय, manāpa मनभावन.
- Noun plus attribute phrases agree with the noun, as in pi-1 (परिघटना). rūpaṃ atītaṃ = अतीत का भौतिक रूप, vedanā atītā = अतीत की अनुभूति, Sāsavā vedanā = मन के मैलों का विषय बनने वाली अनुभूति, sampayuttā saññā = जुड़ी पहचान, Akusalaṃ viññāṇaṃ = हानिकर चेतना. Where the Hindi makes the attribute a predicate («कौन-सी अनुभूति स्थूल है»), the phrase follows the Hindi order: vedanā oḷārikā = अनुभूति स्थूल, vedanā hīnā = अनुभूति हीन.
- vuccati / vuccanti alone = कहा जाना (infinitive). With a noun, the whole clause as in pi-1/pi-4, agreeing with the noun: vuccati rūpakkhandho = भौतिक रूप का समूह कहा जाता है, vuccati vedanā = अनुभूति कही जाती है, vuccanti saṅkhārā = मानसिक रचनाएँ कही जाती हैं.
- paṭighasamphassa = टकराव वाला संपर्क, adhivacanasamphassa = नाम वाला संपर्क (-jā = … वाले संपर्क से उत्पन्न). Sukhadukkhā(hi) = सुखद और दुःखद, kusalābyākatā = हितकर और नैतिक रूप से अनिर्धारित, Kusalākusalā = हितकर और हानिकर. Member fragments such as ābyākatāhi vedanāhi or dukkhāhi vedanāhi map to their own part of the Hindi (नैतिक रूप से अनिर्धारित अनुभूति, दुःखद अनुभूति).

## Abhidhammabhājanīya (classification frames)
- The labels are the pi-1 mātikā wording in the masculine singular that the builder used to agree with समूह (`LEX` in build_1-khandhavibhango_hi.py = `LABELS` in PI2). Examples: sahetuko मूल वाला, ahetuko मूल से रहित, hetusampayutto मूलों से जुड़ा, sāsavo मन के मैलों का विषय बनने वाला, saṃkilesiko क्लेशों का विषय बनने वाला (the pi-2 Hindi, not pi-1 1-matika «क्लेशों की ओर ले जाने वाला»), pariyāpanno अस्तित्व के लोकों में समाया हुआ, uppanno उत्पन्न हो चुका.
- «atthi X» = «कुछ X है»: map X only (atthi is not a keyword).
- phassasampayutto = संपर्क से जुड़ा, cittasampayutto = मन से जुड़ा. sukhindriyasampayutto = सुख की क्षमता से जुड़ा (likewise for the other four faculties). The fragments sukhindriya … upekkhindriya = X की क्षमता, indriya = क्षमता.
- X-samphassa = «X का संपर्क», X-samphassajā = «X के संपर्क से उत्पन्न», with the noun «… उत्पन्न अनुभूति / पहचान / इरादा». manodhātu = मन का तत्व, manoviññāṇadhātu = मन की चेतना का तत्व, viññāṇadhātu = चेतना का तत्व, dhātu = तत्व, mano = मन. X-samphassapaccayā: paccayā = के कारण होने वाला.
- The sense words of the rūpa string: X-viññeyyaṃ = «X से जाना जा सकने वाला», X-indriyaṃ = «X की क्षमता», X-āyatanaṃ = «X का इंद्रिय-क्षेत्र» (pi-1 Rūpakaṇḍa). samphassaṃ (sukha-/dukkhasamphassaṃ) = संपर्क वाला, sutaṃ सुना हुआ, mutaṃ अनुभव किया हुआ, viññātaṃ जाना हुआ, jarābhibhūtaṃ बुढ़ापे से ग्रस्त (ābhibhūtaṃ ग्रस्त), mattaṃ (avitakkavicāramattaṃ) केवल, saha साथ.
- The fragments of the matrix compounds, as in pi-1: ācaya संचय, apacaya / āpacaya संचय घटाना, gāmī की ओर ले जाने वाला, sekkha सीखने के चरण का, āsekkhaṃ सीखना पूरा होने के चरण का, ādhipati प्रधानता वाला, magga मार्ग, sammatta सही दिशा, micchatta ग़लत दिशा, saṃkiliṭṭha क्लेशों से मलिन, asaṃkiliṭṭha क्लेशों से मलिन न होने वाला, vitakka आरंभिक विचार, vicāro सतत विचार, sukha सुख, pīti उल्लास, upekkhā समभाव, uttaro / uttarā (lokuttara) लोकोत्तर, āvacaro लोक से संबंधित, kilesa क्लेश, āsava / āsavo मन के मैल. dukkha (dukkhasamphassaṃ) = दुःखद.
- Context rules in `pi2_value`:
  - hetuko = मूलों वाला where the segment has a pahātabb- keyword, मूल बनाने वाला where it has magga, otherwise मूल वाला.
  - ārammaṇo = विषय बनाने वाला where magga is the only -ārammaṇo source, otherwise विषय वाला.
- Cluster pairs «Y-vippayutta-X-niya» (āsava, saṃyojana, gantha, ogha, yoga, nīvaraṇa, parāmāsa, upādāna): the whole compound = «Yों से अलग पर उनका (उसका) विषय (न) बनने वाला» (comma dropped). When the bare X-niya / aX-niya fragment only occurs inside such a pair in that segment, its value is «उनका / उसका विषय (न) बनने वाला» (pi-1 closing-pair rule). `pi2_value` does this automatically when the full label is absent.
- kenaci viññeyyo = किसी एक प्रकार की चेतना से जाना जा सकने वाला (kenaci na …: … से न जाना …). kenaci = किसी एक प्रकार की चेतना, viññeyyo = जाना जा सकने वाला.

## Pañhāpucchaka frames
- Pañcannaṃ khandhānaṃ kati X: khandhānaṃ = समूह, X = the label (saraṇā संघर्ष वाला …).
- khandhā siyā = समूह कभी («चार समूह कभी …»). khandhā cittasaṃsaṭṭhā = समूह मन से घुला-मिला. Rūpakkhandho hetuvippayutto = भौतिक रूप का समूह मूलों से अलग.
- vattabbo / vattabbā = कहा जा सकना (pi-1). na = नहीं in these segments («नहीं कहा जा सकता», «मूल रूपी नहीं हैं»). List the segment ids in `PP_SEGMENTS`; elsewhere na = न.
- Predicate negation (harmonise rule PP3): where the Hindi says a «… न होने वाला» label as «… नहीं है / नहीं होते», the value follows the Hindi. sauttaro / sauttarā = सर्वोच्च नहीं, asaṃkiliṭṭho = क्लेशों से मलिन नहीं (2-153). `pi2_value` tries this variant automatically when the full label is absent.
- The cluster nouns of the «X रूपी» predicates keep the pi-1 term: āsavā मन के मैल, saṃyojanaṃ बंधन, gantho गाँठ, oghā बाढ़, yogā जकड़न, nīvaraṇaṃ बाधा, parāmāso ग़लत धारणा, upādānā आसक्ति, kilesā मन के क्लेश, hetu / hetū मूल, cittaṃ मन.
- ceva-pairs: «X ceva X-sampayutto» = «X रूपी भी और Xों से जुड़ा भी» (masculine singular, like pi-1 «गाँठ रूपी भी और …»). For example hetu ceva hetusampayutto = मूल रूपी भी और मूलों से जुड़ा भी.
- The PP of this chapter uses the matrix label even where the Suttanta part used a plain participle: uppannā = उत्पन्न हो चुका in 2-152 (Suttanta uppannā = उत्पन्न).

## Presence exceptions (sample)
- 2-153 apariyāpannā = अस्तित्व के लोकों में न समाया हुआ. The text has «न समाए हुए», and the checker does not model समाया ~ समाए.

## Note
- The presence check accepts «मूल» inside «मूलों», so «मूल वाला» also passes on «मूलों वाला». The hetuko rule above decides the reading, not the checker.
