# pi-6 Pāli→Hindi keyword map: conventions beyond pi-1/pi-2 (settled on the sample: preamble, 1-mulayamaka, 2-01-khandhayamaka)

Read with `..\hi-mapper-brief.md`, the binding pi-1 file `..\..\pi-1-hi\mapper-hi\hi-map-conventions.md` and the pi-2 file `..\..\pi-2-hi\mapper-hi\hi-map-conventions-pi2.md`. Everything there still holds (dhammā = singular परिघटना, masculine direct singular for adjectives/participles, members of compounds, positive part for fragments that lost a negative, no ", " inside a value, " … " for gaps). The Hindi wording comes from `..\hi-zeroshot-terms.md`; the harmonise pass (`..\harmonise-notes.md`) did not touch 1-mulayamaka or 2-01, but it did change later chapters (I1 organs, I3 «चार या पाँच», I4 Natthi, B1-B11): the TRANSLATION FILE is the truth.

## Tooling (`map_sample_hi.py`, import it, do not edit it)
- Importing it writes nothing and prints nothing (it sets `sys.dont_write_bytecode`; set it in your own script too, before the import, so no `__pycache__` appears in the shared folder). It reads pi-1 `map_common_hi.py` and pi-2 `map_sample_hi.py` read-only (the pi-2 module is loaded by path under another name, because both are called map_sample_hi).
- `read_keywords / read_hindi / read_pali(f)` use the pi-6 paths.
- `PI6` is the default table. Lookup: lower-case first letter; PI6, then pi-2 `PI2`, then pi-1 `CH2`; then the same again after dropping the quotative -ti (kusalāti, uppajjatīti, uppajjitthāti, rūpanti, khandhoti, nāmāti) and the enclitics -ñca / -ñceva (kusalañca, ekamūlañceva, Rūpañca, nidānañca). So you rarely need entries for those forms.
- A table value may be a tuple of alternatives: the first one present in the segment's Hindi wins (else the first). Used for itaresaṃ, pacchimabhavikānaṃ, uppāda, nirodha.
- `BARE`: the bare words of the word-checking pairs, used when the segment also has a khandha keyword (see below).
- `pi6_value(kw, kws, table, bid, text)`; `make_resolver(f, table, ovr)` = `OVR[bid][kw]` first, then `pi6_value` with the segment's Hindi. Pattern: `build_part(f, make_resolver(f, {**PI6, **T}, OVR)); verify(f, allowed={(bid, kw): reason})`.
- `present(value, text)` = pi-1 present() plus three pi-6 tolerances: «नहीं» counts as the dropped negative (value «समाप्त हुआ था» ~ text «समाप्त नहीं हुआ था», needed where a separate `na` is not a keyword); tense endings agree in gender/number (हुआ था ~ हुई थी / हुए थे; होगा ~ होगी / होंगे; होता ~ होती / होते), for the feminine subjects of Indriya/Anusaya; «सबमें» = «सब में».
- `prior(kw)`: values in the pi-1/2/3/4/5 Hindi maps.
- Helpers: `show_sample_hi.py <f> id …` (Pāli, Hindi, keywords, mapped line), `audit_sample_hi.py <f> [multi]` (each keyword, its values, which table gave it, prior values), `strict_sample_hi.py <f>` (values that pass only through the pi-6 tolerances).

## Frame and headings
- Abhidhammapiṭake = अभिधम्म पिटक; Namo नमन, bhagavato भगवान, arahato अर्हत्, sammāsambuddhassa पूर्ण रूप से जागृत बुद्ध (pi-1/pi-2 preamble).
- Book and chapter titles keep the plural concept of the Hindi title: Yamakapāḷi = प्रश्नों के जोड़े; Mūlayamakaṃ / Mūlayamakapāḷi = मूलों पर प्रश्नों के जोड़े; Khandhayamakaṃ = समूहों पर प्रश्नों के जोड़े (all ten chapters are in PI6). pāḷi alone = (no direct equivalent).
- vāro = खंड, nayo = विधि, uddeso = सूची, niddeso / niddesa = व्याख्या. Whole heading words map to the whole Hindi heading: Mūlavāro मूल का खंड, Mūlavārauddeso मूल के खंड की सूची, Mūlavāraniddeso मूल के खंड की व्याख्या, Uddesavāro सूची का खंड, Niddesavāro व्याख्या का खंड, Hetuvārādi हेतु का खंड आदि; Mūlanayo मूल की विधि, Mūlamūlanayo मूल के मूल की विधि, Mūlakanayo मूल पर आधारित होने की विधि, Mūlamūlakanayo मूल के मूल पर आधारित होने की विधि.
- Paṇṇattivāro शब्दावली का खंड, Paṇṇattivāraniddesa शब्दावली के खंड की व्याख्या, Paṇṇattiuddesavāro शब्दावली की सूची का खंड, Paṇṇattiniddesavāro शब्दावली की व्याख्या का खंड, Padasodhanavāro शब्दों की जाँच का खंड, Padasodhanamūlacakkavāro शब्दों की जाँच पर आधारित चक्र का खंड, Suddhakhandhavāro केवल समूहों का खंड, Suddhakhandhamūlacakkavāro केवल समूहों पर आधारित चक्र का खंड (the other Suddha-X are in PI6).
- anulomaṃ = सकारात्मक, paccanīkaṃ = नकारात्मक, paṭilomaṃ = विपरीत. puggala = व्यक्ति, okāsa = स्थान. The combined headings keep the Hindi colon: anulomapuggalo = सकारात्मक: व्यक्ति, anulomaokāso = सकारात्मक: स्थान, anulomapuggalokāsā = सकारात्मक: व्यक्ति और स्थान (paccanīka- नकारात्मक: …, paṭiloma- विपरीत: …).
- Pavattivāro प्रक्रिया का खंड, Pavatti प्रक्रिया; uppādavāro / Uppādavāro उत्पन्न होने का खंड, nirodhavāro समाप्त होने का खंड, uppādanirodhavāro उत्पन्न होने और समाप्त होने का खंड. The members: uppāda = उत्पन्न होना, nirodha = समाप्त होना (the Hindi «उत्पन्न होने का», not pi-1 cittuppāda «उत्पत्ति»; the tuple falls back to उत्पत्ति / निरोध where that is the Hindi). Paccuppanna-/Atīta-/Anāgata-/…vāro = वर्तमान / अतीत / भविष्य / वर्तमान और अतीत / … का खंड.
- niṭṭhito / niṭṭhitā = पूरा हुआ (the colophons are not keywords in the sample).

## The four kinds of dhamma and the roots (Mūlayamaka)
- kusalā / akusalā / abyākatā = हितकर / हानिकर / नैतिक रूप से अनिर्धारित; nāmā / nāmaṃ = मानसिक पक्ष; X dhammā = X परिघटना, nāmā dhammā = मानसिक पक्ष की परिघटना.
- mūla = मूल. Xmūlā / -mūlāni / -mūlena = «X मूल» (nāma: मानसिक पक्ष का मूल). The instrumental's «के साथ» is a postposition and is stripped: kusalamūlena = हितकर मूल.
- Xmūlamūlā = «X मूल का मूल» (direct sg; text «हितकर मूल के मूल»); nāma: मानसिक पक्ष के मूल का मूल.
- Xmūlakā = «X मूल पर आधारित»; Xmūlamūlakā = «X मूल के मूल पर आधारित».
- ekamūlā एक ही मूल वाला, ekamūlamūlā एक ही मूल के मूल वाला, ekamūlakā एक ही मूल पर आधारित, ekamūlamūlakā एक ही मूल के मूल पर आधारित; aññamañña- the same with परस्पर. All case/number forms (-ā, -āni, -aṃ, -añceva, -āti) get the same value (masc. sg.; «के» stays where the Hindi needs it before वाला / पर).
- Xmūlasahajātā (dhammā) = «X मूल के साथ उत्पन्न (परिघटना)» (sahajāta = के साथ उत्पन्न, a term, so «के साथ» stays). Xsamuṭṭhānaṃ rūpaṃ = «X से उत्पन्न» + भौतिक रूप. Ahetukaṃ = मूल से रहित, Sahetukaṃ = मूल वाला (pi-1/2 root sense). Avasesā = शेष, Mūlāni = मूल, uppajjanti = उत्पन्न होना.
- hetu / mūla: hetu = हेतु in the ten names of the Hetuvāra, where the text keeps it apart from mūla (brief). The ten names: Mūlaṃ मूल, hetu हेतु, nidāna(ñca) स्रोत, sambhavo उद्भव, pabhavena उद्गम, samuṭṭhāna उत्पादक, āhāra आहार, ārammaṇa विषय, paccayo कारण, samudayena उत्पत्ति; Samuṭṭhānāhārārammaṇā = उत्पादक आहार और विषय (comma dropped). Compounds: kusalahetū हितकर हेतु … kusalasamudayā हितकर उत्पत्ति; nāmahetū मानसिक पक्ष का हेतु … nāmasamudayā मानसिक पक्ष की उत्पत्ति. Everywhere else (sahetuka, ahetuka, hetusampayutta …) hetu is still मूल (pi-1/2).
- Enclitics: -ñca, -ñceva, ceva are dropped like pi-1 -meva: ekamūlañceva = एक ही मूल वाला, kusalañca = हितकर, nidānañca = स्रोत, Rūpañca = रूप.

## The aggregates and the bare words (Paṇṇattivāra)
- X-kkhandho (any case, -ti, -ñca) = «X का समूह» (pi-2). khandha / khandho / khandhā / khandhe / khandhoti = समूह; Pañcakkhandhā = पाँच समूह; Avasesā khandhā = शेष समूह; avasesā = शेष; ṭhapetvā = छोड़कर.
- The bare words of the word-checking pairs keep their bare Hindi (brief): rūpaṃ = रूप, saṅkhārā / Saṅkhāre = रचनाएँ, vedanā / Vedanaṃ = अनुभूति, saññā / Saññaṃ = पहचान, viññāṇaṃ = चेतना. Rule in `pi6_value`: rūpa/saṅkhāra forms are bare when the segment also has a khandha keyword; otherwise rūpaṃ = भौतिक रूप (1-mulayamaka «हितकर से उत्पन्न भौतिक रूप») and saṅkhārā = मानसिक रचनाएँ. For the Saṅkhārayamaka (saṅkhāra = रचना) and the Āyatana/Dhātu bare sense words, put the chapter's own entries into your table.
- Diṭṭhisaññā = दृष्टि के अर्थ में पहचान.

## Process verbs (Pavattivāra)
- Present = the infinitive: uppajjati / uppajjatīti / Uppajjati (answer) / uppajjanti = उत्पन्न होना; nirujjhati = समाप्त होना (pi-1/2).
- Past and future keep the tense, as pi-1 did (uppajjissati = उत्पन्न होगा): the finite form the text uses, masculine, in the Pāli's number: uppajjittha = उत्पन्न हुआ था, uppajjissati = उत्पन्न होगा, nirujjhittha = समाप्त हुआ था, nirujjhissati = समाप्त होगा; plural uppajjiṃsu उत्पन्न हुए थे, uppajjissanti उत्पन्न होंगे, parinibbāyissanti = पूर्ण निर्वाण पाएँगे. Feminine/plural text forms (हुई थी, होगी, होंगे) pass the presence check; do not change the value.
- A fused negative keeps the Hindi «नहीं» (pi-2 «… उत्पन्न नहीं होना», PP3 rule): nuppajjati = उत्पन्न नहीं होना, nuppajjittha = उत्पन्न नहीं हुआ था, nuppajjissati = उत्पन्न नहीं होगा. A separate `na` (na nirujjhati) is its own word and is not a keyword: nirujjhati there is the positive part, समाप्त होना / समाप्त हुआ था, even where the segment only has «समाप्त नहीं …» (6-2-113; passes through the «नहीं» tolerance).
- The polarity flip of «no ca tesaṃ … » (terms file) does not change the keyword's value: the keyword maps to its own verb form.
- Participles: uppajjamāna उत्पन्न होता हुआ, uppanna उत्पन्न हो चुका, nirujjhamāna समाप्त होता हुआ, niruddha समाप्त हो चुका.
- Natthi (short answer «ऐसा कोई नहीं है।») = ऐसा कोई नहीं (copula dropped; the Hindi supplies the subject).

## Beings and places
- Place sense (accusative of destination with upapajjantānaṃ, locative, ablative with cavantānaṃ) = the realm, direct case: Asaññasattaṃ / Asaññasatte / asaññasattā = पहचान-रहित प्राणियों का लोक; Pañcavokāraṃ / -e / -ā = पाँच समूहों वाला अस्तित्व (also inside «चार या पाँच समूहों वाले अस्तित्व»); catuvokāra- = चार समूहों वाला अस्तित्व; Arūpaṃ / Arūpe / Arūpā = अभौतिक लोक; Suddhāvāsaṃ / Suddhāvāse = शुद्ध निवास लोक.
- Beings sense (genitive plural) = the beings: Asaññasattānaṃ = पहचान-रहित प्राणी; Pañcavokārānaṃ = पाँच समूहों वाले अस्तित्व के प्राणी; Arūpānaṃ = अभौतिक लोक के प्राणी; Suddhāvāsānaṃ = शुद्ध निवास लोक के प्राणी.
- Participle nouns, masc. direct sg.: upapajjantānaṃ = जन्म लेने वाला, cavantānaṃ = मरने वाला, parinibbantānaṃ = पूर्ण निर्वाण पाने वाला; upapajjitvā = जन्म लेकर; (women: upapajjantīnaṃ जन्म लेने वाली स्त्री, cavantīnaṃ मरने वाली स्त्री).
- pacchimabhavikānaṃ = अंतिम जन्म वाला («अंतिम जन्म वालों में»); where B2 fused it with upapajjantānaṃ («… अंतिम जन्म लेने वालों में») = अंतिम जन्म (tuple). itaresaṃ = बाकी सब («बाकी सबमें»), बाकी before a place («बाकी पाँच समूहों वाले अस्तित्व में …») (tuple).

## Results of the sample
- preamble 3 lines, 1-mulayamaka 139, 2-01-khandhayamaka 195: brief verifier bad [] for all; 0 (no direct equivalent); 0 presence misses, 0 exceptions, 0 overrides. Only 2 values pass through a pi-6 tolerance (6-2-113 nirujjhittha / nirujjhitthāti = समाप्त हुआ था on «समाप्त नहीं हुआ था»).
