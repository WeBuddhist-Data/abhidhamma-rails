# Notes for 8-cittayamaka.md (pi-6 Hindi plain RAILS)

Builder: build_8_cittayamaka.py (imports build_rails_sample.py read-only; `--dry` prints instead of writing).
Checks: check_chapter_ids OK (209 segments), dashcheck 0, verify_hi OK, post_check_sample OK, adherence 14/821 misses, all inflection («होते हुए»).

## New recurring formulas (for the alignment pass)
Subject «मन» is masculine singular; process verbs from hi-rails-formulas.md §9.
- Dhammavāra question: (Ka) yaṃ cittaṃ V1 taṃ cittaṃ V2? = (क) जो मन V1, क्या वह मन V2?; (Kha) yaṃ vā pana … = (ख) और जो मन …, क्या वह मन …?
- Puggaladhammavāra question: (Ka) yassa yaṃ cittaṃ V1 tassa taṃ cittaṃ V2? = (क) जिस व्यक्ति में जो मन V1, क्या उसमें वह मन V2?
- Two verbs in one slot (uppajjati na nirujjhati / na uppajjati nirujjhati) = «उत्पन्न होता है और समाप्त नहीं होता» / «उत्पन्न नहीं होता और समाप्त होता है».
- Participles as predicates: uppannaṃ = उत्पन्न हो चुका है / na uppannaṃ = उत्पन्न हो चुका नहीं है; uppajjamānaṃ = उत्पन्न होता हुआ है / … नहीं है; nirujjhamānaṃ = समाप्त होता हुआ है / … नहीं है; niruddhaṃ = समाप्त हो चुका है / समाप्त हो चुका नहीं है. Short answer Uppannaṃ. = उत्पन्न हो चुका है।
- Same subject, two verbs, "V1 ceva V2 ca" / "P1ñceva P2ñca" = «मन V1 भी … और V2 भी …», भी after the first word: उत्पन्न भी होता है, समाप्त भी होगा, उत्पन्न भी हो चुका है, but उत्पन्न होता हुआ भी है / समाप्त होता हुआ भी है; negative first verb: समाप्त भी नहीं होता और उत्पन्न भी होता है.
- "na ceva V1 na ca V2" = «न तो V1 (positive), न V2 (positive)»: मन न तो उत्पन्न होता है, न उत्पन्न हो चुका है।
- (11) "yassa X V1 no ca tassa X V2, tassa X V3?" = «जिस व्यक्ति में मन V1, पर उसमें मन <V2 flipped>, क्या उसमें मन V3?» (Dhamma: «जो मन V1, पर वह मन <V2 flipped>, क्या वह मन V3?»).
- (12)/(13) bare questions: (Ka) uppannaṃ uppajjamānaṃ? = (क) जो उत्पन्न हो चुका है, क्या वह उत्पन्न होता हुआ है?; negative: जो … नहीं है, क्या वह … नहीं है?
- Answers in the Dhammavāra: "<subj> cittaṃ V1, no ca taṃ cittaṃ V2" = «<subj> मन V1, पर वह मन <V2 flipped>।»; Puggaladhamma "no ca tassa taṃ cittaṃ" = «पर उसमें वह मन».
  Subjects: Bhaṅgakkhaṇe / Uppādakkhaṇe cittaṃ = भंग होने के / उत्पन्न होने के क्षण का मन; Atītaṃ / Anāgataṃ / Paccuppannaṃ / Atītānāgataṃ cittaṃ = अतीत का / भविष्य का / वर्तमान / अतीत और भविष्य का मन; "Bhaṅgakkhaṇe anāgatañca cittaṃ" = भंग होने के क्षण का और भविष्य का मन (one noun, two modifiers, singular).
  Without cittaṃ (^6-8-81/82): Bhaṅgakkhaṇe / Uppādakkhaṇe = भंग होने के / उत्पन्न होने के क्षण में (no subject in Hindi either).
- Puggala answers with moments (BUT_BEINGS / BOTH_BEINGS kept): Cittassa uppādakkhaṇe / bhaṅgakkhaṇe tesaṃ = मन के उत्पन्न होने / भंग होने के क्षण में; Pacchimacittassa … = अंतिम मन के … होने के क्षण में; joined with beings as chunks: «मन के भंग होने के क्षण में, समाप्ति की ध्यान-अवस्था में लीन लोगों में और पहचान-रहित प्राणियों में». A moment-only subject still takes «, पर उनमें …» (persons understood).
- Itaresaṃ + moment (itaresaṃ stands alone): «बाकी सबमें मन के उत्पन्न होने के क्षण में»; Itaresaṃ + group: «बाकी मन से युक्त लोगों में»; Cittasamaṅgīnaṃ = मन से युक्त लोगों में; Pacchimacittasamaṅgīnaṃ = अंतिम मन से युक्त लोगों में.
- ^6-8-63 type: "<who> tesaṃ cittaṃ uppajjati na nirujjhati, nirujjhissati na uppajjissati." = «<who> मन उत्पन्न होता है और समाप्त नहीं होता, समाप्त होगा और उत्पन्न नहीं होगा।»
- (14) Atikkantakāla: "uppajjamānaṃ khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ" = «उत्पन्न होते हुए क्षण-क्षण से आगे निकल चुका है और उसका समय बीत चुका है»; negative «… आगे नहीं निकला है और उसका समय नहीं बीता है»; answers vītikkanta = आगे निकल चुका है, avītikkanta = आगे नहीं निकला है.
- Kinds of mind (termbase + pi-2 ^7 satipaṭṭhāna Hindi): राग-युक्त, राग से मुक्त, द्वेष-युक्त, द्वेष से मुक्त, मोह-युक्त, मोह से मुक्त, सिमटा हुआ, बिखरा हुआ, उन्नत, उन्नत न होने वाला, सर्वोच्च न होने वाला, सर्वोच्च, एकाग्र, एकाग्रता से रहित, मुक्त, अमुक्त; sukhāya vedanāya sampayuttaṃ = सुखद अनुभूति से जुड़ा (pi-1 mātikā); araṇaṃ = संघर्ष से रहित.
- Abbreviated question lists end «…?»; "Yassa vā pana…pe…? Āmantā …pe…." = «और जिस व्यक्ति में…? हाँ…।»

## Not in the termbase (built here)
vītadosaṃ, vītamohaṃ (pi-2), sukhāya (pi-1 «सुखद»), vītikkantaṃ / avītikkantaṃ («आगे निकल चुका / आगे नहीं निकला»), atikkantakālaṃ as an adjective («उसका समय बीत चुका है»), upāyena («तरीके से»), uddharitabbā («निकाले जाने चाहिए»), sakabhāvena («अपने ही ढंग से»), ekattena («एक ही रूप में»), gacchanti («जाते हैं»).

## Source slips
- ^6-8-82: "(14) Atikkantakālavāro" stands as a plain text line at the end of the segment (no heading mark, no own ID); kept there as «(14) समय बीत चुकने का खंड».
- ^6-8-83 line 2: "vītakkantaṃ" for vītikkantaṃ (^6-8-104 has the correct form); same Hindi.
- Heading (7) spelled "Uppajjamāna-nanirodhavāro" and "Uppajjamānananirodhavāro"; "Suddhacittasāmañña" and "-sāmaññaṃ": same Hindi.
- ^6-8-61: stray space in "uppajjati … yassa"; ^6-8-115 "Āmantā …pe…." space: normalised.
