# pi-7 Paṭṭhāna, Hindi plain RAILS: sentence formulas (read-only for every agent after the sample)

Every line is "Pāli = Hindi". All strings are importable constants in build_rails_sample.py (same folder):
`import build_rails_sample as R` (no side effects), then R.NAME, R.ABL, R.NABL, R.NNAME, R.LOC, R.NLOC, R.INS(k, g),
R.NINS(k, g), R.SADISA, R.NSADISA, R.MULAKA, R.DUKA, R.CH(chain), R.count_hi(line), R.ACC, R.NOM, R.DAT_ITEM,
R.paticca_frame, R.siya_frame, R.SUBJ_P, R.OBJ_P, R.SUBJ, R.DAT, R.CLAUSE, R.NOTE, R.HEAD, R.translate_line(line).
Lines marked "(not yet in the sample)" are binding proposals taken from hi-zeroshot-terms.md and harmonise-notes.md
with the termbase words; they are not in R yet. The locked termbase wins over any word here; a NEW recurring formula
goes in your own notes-<files>.md, never in this file.

## 0. Typography

- "…pe…" = "…" (same spot). Final "." = "।"; a question ends "?" (a Siyā question absorbs the Pāli "." after it).
- "–" only where the Pāli has "–" (same count per line). Pāli hyphens in headings (Anantara-samanantara…) are not dashes.
- Counts "(1)", "(3)" stay as digits. Number words: ekaṃ एक, dve दो, tīṇi तीन, cattāri चार, pañca पाँच, cha छह,
  satta सात, aṭṭha आठ, nava नौ (beyond nine: Hindi number words, e.g. tevīsati तेईस).
- Variants: {x (syā.)} = [वर्तनी-भेद (Syā.): x] for spelling-only, [पाठभेद (Syā.): x] otherwise; sigla capitalised and
  comma-separated in Pāli order: (ka. sī. syā.) = (Ka., Sī., Syā.). Untagged {x} = [पाठभेद: x]. The bracket goes
  after the Hindi words it replaces.
- (Ka) (Kha) (Ga) (Gha) = (क) (ख) (ग) (घ).
- Plain lists of 3+ datives share one «के लिए» at the end ("A, B और C के लिए"); two datives joined by ca repeat it
  ("A के लिए और B के लिए"). An asyndetic list of 3+ nominatives gets «और» before the last member.
- A subject that would touch an identical noun in the dative takes a comma: «हितकर परिघटना, हितकर परिघटना के लिए…».

## 1. Book frame and headings

Namo tassa bhagavato arahato sammāsambuddhassa = उन भगवान, अर्हत्, पूर्ण रूप से जागृत बुद्ध को नमन
Abhidhammapiṭake = अभिधम्म पिटक में
Paṭṭhānapāḷi = कारण-संबंध
(Paṭhamo bhāgo) = (पहला भाग)
(Dutiyo / Tatiyo / Catuttho / Pañcamo / Chaṭṭho bhāgo) = (दूसरा / तीसरा / चौथा / पाँचवाँ / छठा भाग) (not yet in the sample)
Dhammānulome = परिघटनाओं का सकारात्मक क्रम
Dhammapaccanīye / Dhammānulomapaccanīye / Dhammapaccanīyānulome = परिघटनाओं का नकारात्मक क्रम / परिघटनाओं का सकारात्मक-नकारात्मक क्रम / परिघटनाओं का नकारात्मक-सकारात्मक क्रम (not yet in the sample)
Tikapaṭṭhānaṃ = तीन-तीन के वर्गीकरणों के कारण-संबंध
Dukapaṭṭhānaṃ / Dukatikapaṭṭhānaṃ / Tikadukapaṭṭhānaṃ / Tikatikapaṭṭhānaṃ / Dukadukapaṭṭhānaṃ = दो-दो के वर्गीकरणों के कारण-संबंध / दो-दो और तीन-तीन के वर्गीकरणों के कारण-संबंध / तीन-तीन और दो-दो के वर्गीकरणों के कारण-संबंध / तीन-तीन और तीन-तीन के वर्गीकरणों के कारण-संबंध / दो-दो और दो-दो के वर्गीकरणों के कारण-संबंध (not yet in the sample)
Dhammānulome dukapaṭṭhānaṃ (one heading) = परिघटनाओं का सकारात्मक क्रम: दो-दो के वर्गीकरणों के कारण-संबंध (not yet in the sample)

### Sections
(1) Paccayuddeso = (1) कारणों की सूची
(2) Paccayaniddeso = (2) कारणों की व्याख्या
Paccayaniddeso. (closing) = कारणों की व्याख्या।
Pucchāvāro / Pucchāvāro. = पूछताछ का खंड / पूछताछ का खंड।
Niddesavāre tevīsatipaccayā. = व्याख्या के खंड में तेईस कारण।
Paṭiccavāro = निर्भरता का खंड
Vibhaṅgavāro = विश्लेषण का खंड
Saṅkhyāvāro = गणना का खंड
Pañhāvāro = प्रश्नों का खंड
Sahajātavāro / Paccayavāro / Nissayavāro / Saṃsaṭṭhavāro / Sampayuttavāro = सह-उत्पत्ति का खंड / कारण का खंड / आश्रय का खंड / घुले-मिले होने का खंड / जुड़ाव का खंड (not yet in the sample)
Paṭiccavārādi = निर्भरता का खंड आदि (not yet in the sample)
X-vārasadiso = X के खंड के समान (not yet in the sample)
2-6. …sampayuttavāro = … और जुड़ाव का खंड (not yet in the sample)
Paccanīyuddhāro = नकारात्मक क्रम के लिए कारणों की छँटाई (not yet in the sample)
Hetupaccayavāro. = मूल-कारण का खंड।

### Methods
Paccayānulomaṃ / Paccayapaccanīyaṃ / Paccayānulomapaccanīyaṃ / Paccayapaccanīyānulomaṃ = कारणों का सकारात्मक क्रम / कारणों का नकारात्मक क्रम / कारणों का सकारात्मक-नकारात्मक क्रम / कारणों का नकारात्मक-सकारात्मक क्रम
Anulomaṃ – hetupaccayo = सकारात्मक क्रम – मूल-कारण
Paccanīyaṃ – nahetupaccayo = नकारात्मक क्रम – मूल-कारण का अभाव
Anulomaṃ. (closing) = सकारात्मक क्रम।
anulome / paccanīye (in notes) = सकारात्मक क्रम में / नकारात्मक क्रम में
Paccayacatukkaṃ = कारणों के चार क्रम (not yet in the sample)

### Series (mūlaka) and items (pada)
Ekamūlakaṃ / Dumūlakaṃ / Timūlakaṃ / Catumūlakaṃ / Pañcamūlakaṃ / Sabbamūlakaṃ / tevīsatimūlakaṃ = एक कारण वाली शृंखला / दो कारणों वाली शृंखला / तीन कारणों वाली शृंखला / चार कारणों वाली शृंखला / पाँच कारणों वाली शृंखला / सभी कारणों वाली शृंखला / तेईस कारणों वाली शृंखला (closing line: same + «।»)
Dumūlakādi = दो कारणों वाली शृंखला आदि
Pañcamūlakādikā = पाँच कारणों वाली शृंखला आदि
Hetumūlakaṃ = मूल-कारण से शुरू होने वाली शृंखला (any X: R.MULAKA[k] = «X-कारण से शुरू होने वाली शृंखला»)
Ārammaṇamūlakādi = विषय-कारण से शुरू होने वाली शृंखला आदि
Āsevanamūlake / Vipākamūlake (notes) = पुनरावृत्ति-कारण से शुरू होने वाली शृंखला में / कर्म-फल-कारण से शुरू होने वाली शृंखला में
Nahetumūlakaṃ = मूल-कारण के अभाव से शुरू होने वाली शृंखला (not yet in the sample)
(1.) Kusalapadaṃ / (2) Akusalapadaṃ / (3) Abyākatapadaṃ = (1.) हितकर पद / (2) हानिकर पद / (3) नैतिक रूप से अनिर्धारित पद
Kusalābyākatapadaṃ / Akusalābyākatapadaṃ / Kusalākusalapadaṃ / Kusalākusalābyākatapadaṃ = हितकर और नैतिक रूप से अनिर्धारित पद / हानिकर और नैतिक रूप से अनिर्धारित पद / हितकर और हानिकर पद / हितकर, हानिकर और नैतिक रूप से अनिर्धारित पद
Hetupadaṃ / Sahetukapadaṃ = मूल रूपी पद / मूल वाला पद (not yet in the sample)

### Triad and dyad names
Kusalattikaṃ = हितकर वाला तीन का वर्गीकरण
All other triad and dyad names (heading, combined heading, closing line, cross-reference): the table in
harmonise-notes.md §1 is binding, pattern «X वाला तीन का वर्गीकरण» / «X वाला दो का वर्गीकरण» (not yet in the sample).
Hetuduka-kusalattikaṃ = मूल वाला दो का वर्गीकरण और हितकर वाला तीन का वर्गीकरण (pattern for every combined name) (not yet in the sample)
Hetugocchakaṃ / Āsavagocchakaṃ = मूलों का वर्ग / मन के मैलों का वर्ग; Cūḷantaradukaṃ / Mahantaradukaṃ = बीच के छोटे दो-दो के वर्गीकरण / बीच के बड़े दो-दो के वर्गीकरण (pi-1) (not yet in the sample)
X niṭṭhitaṃ / niṭṭhito (closings) = X समाप्त। (no quotes around a name) (not yet in the sample)

## 2. The 24 conditions in every case form

Rule: name «X-कारण»; Xpaccayā «X-कारण से»; naXpaccayā «X-कारण के बिना»; naXpaccayo (heading, note) «X-कारण का अभाव»
(before a postposition «X-कारण के अभाव …»); Xpaccayena paccayo «X-कारण के रूप में कारण होता है / होती है / होते हैं /
होती हैं» (verb agrees with the subject); na Xpaccayena paccayo «X-कारण के रूप में कारण नहीं होता / होती / होते / होतीं»;
count locative «X-कारण में»; negative count locative «X-कारण के अभाव में». Negative prefix: na-, but no- for atthi,
natthi, vigata, avigata. Xpaccayoti (definition) = «X-कारण». Xpaccayaṃ / Xpaccayampi (notes) = «X-कारण» / «X-कारण भी».

| stem | name | ablative | negative ablative | count locative | negative count locative |
|---|---|---|---|---|---|
| hetu | मूल-कारण | मूल-कारण से | मूल-कारण के बिना | hetuyā = मूल-कारण में | nahetuyā = मूल-कारण के अभाव में |
| ārammaṇa | विषय-कारण | विषय-कारण से | विषय-कारण के बिना | ārammaṇe = विषय-कारण में | naārammaṇe = विषय-कारण के अभाव में |
| adhipati | प्रधानता-कारण | प्रधानता-कारण से | प्रधानता-कारण के बिना | adhipatiyā = प्रधानता-कारण में | naadhipatiyā = प्रधानता-कारण के अभाव में |
| anantara | निकटता-कारण | निकटता-कारण से | निकटता-कारण के बिना | anantare = निकटता-कारण में | naanantare = निकटता-कारण के अभाव में |
| samanantara | पूर्ण निकटता-कारण | पूर्ण निकटता-कारण से | पूर्ण निकटता-कारण के बिना | samanantare = पूर्ण निकटता-कारण में | nasamanantare = पूर्ण निकटता-कारण के अभाव में |
| sahajāta | सह-उत्पत्ति-कारण | सह-उत्पत्ति-कारण से | सह-उत्पत्ति-कारण के बिना | sahajāte = सह-उत्पत्ति-कारण में | nasahajāte = सह-उत्पत्ति-कारण के अभाव में |
| aññamañña | परस्पर-कारण | परस्पर-कारण से | परस्पर-कारण के बिना | aññamaññe = परस्पर-कारण में | naaññamaññe = परस्पर-कारण के अभाव में |
| nissaya | आश्रय-कारण | आश्रय-कारण से | आश्रय-कारण के बिना | nissaye = आश्रय-कारण में | nanissaye = आश्रय-कारण के अभाव में |
| upanissaya | प्रबल आश्रय-कारण | प्रबल आश्रय-कारण से | प्रबल आश्रय-कारण के बिना | upanissaye = प्रबल आश्रय-कारण में | naupanissaye = प्रबल आश्रय-कारण के अभाव में |
| purejāta | पूर्व-उत्पत्ति-कारण | पूर्व-उत्पत्ति-कारण से | पूर्व-उत्पत्ति-कारण के बिना | purejāte = पूर्व-उत्पत्ति-कारण में | napurejāte = पूर्व-उत्पत्ति-कारण के अभाव में |
| pacchājāta | पश्चात्-उत्पत्ति-कारण | पश्चात्-उत्पत्ति-कारण से | पश्चात्-उत्पत्ति-कारण के बिना | pacchājāte = पश्चात्-उत्पत्ति-कारण में | napacchājāte = पश्चात्-उत्पत्ति-कारण के अभाव में |
| āsevana | पुनरावृत्ति-कारण | पुनरावृत्ति-कारण से | पुनरावृत्ति-कारण के बिना | āsevane = पुनरावृत्ति-कारण में | naāsevane = पुनरावृत्ति-कारण के अभाव में |
| kamma | कर्म-कारण | कर्म-कारण से | कर्म-कारण के बिना | kamme = कर्म-कारण में | nakamme = कर्म-कारण के अभाव में |
| vipāka | कर्म-फल-कारण | कर्म-फल-कारण से | कर्म-फल-कारण के बिना | vipāke = कर्म-फल-कारण में | navipāke = कर्म-फल-कारण के अभाव में |
| āhāra | आहार-कारण | आहार-कारण से | आहार-कारण के बिना | āhāre = आहार-कारण में | naāhāre = आहार-कारण के अभाव में |
| indriya | क्षमता-कारण | क्षमता-कारण से | क्षमता-कारण के बिना | indriye = क्षमता-कारण में | naindriye = क्षमता-कारण के अभाव में |
| jhāna | ध्यान-कारण | ध्यान-कारण से | ध्यान-कारण के बिना | jhāne = ध्यान-कारण में | najhāne = ध्यान-कारण के अभाव में |
| magga | मार्ग-कारण | मार्ग-कारण से | मार्ग-कारण के बिना | magge = मार्ग-कारण में | namagge = मार्ग-कारण के अभाव में |
| sampayutta | जुड़ाव-कारण | जुड़ाव-कारण से | जुड़ाव-कारण के बिना | sampayutte = जुड़ाव-कारण में | nasampayutte = जुड़ाव-कारण के अभाव में |
| vippayutta | अलगाव-कारण | अलगाव-कारण से | अलगाव-कारण के बिना | vippayutte = अलगाव-कारण में | navippayutte = अलगाव-कारण के अभाव में |
| atthi | उपस्थिति-कारण | उपस्थिति-कारण से | उपस्थिति-कारण के बिना | atthiyā = उपस्थिति-कारण में | noatthiyā = उपस्थिति-कारण के अभाव में |
| natthi | अनुपस्थिति-कारण | अनुपस्थिति-कारण से | अनुपस्थिति-कारण के बिना | natthiyā = अनुपस्थिति-कारण में | nonatthiyā = अनुपस्थिति-कारण के अभाव में |
| vigata | विलीनता-कारण | विलीनता-कारण से | विलीनता-कारण के बिना | vigate = विलीनता-कारण में | novigate = विलीनता-कारण के अभाव में |
| avigata | अविलीनता-कारण | अविलीनता-कारण से | अविलीनता-कारण के बिना | avigate = अविलीनता-कारण में | noavigate = अविलीनता-कारण के अभाव में |

Combined headings: Anantara-samanantarapaccayā = निकटता-कारण और पूर्ण निकटता-कारण; Jhāna-maggapaccayā = ध्यान-कारण और
मार्ग-कारण; Natthi-vigatapaccayā = अनुपस्थिति-कारण और विलीनता-कारण; Naanantara-nasamanantarapaccayā = निकटता-कारण का अभाव
और पूर्ण निकटता-कारण का अभाव; Napacchājāta-naāsevanapaccayā = पश्चात्-उत्पत्ति-कारण का अभाव और पुनरावृत्ति-कारण का अभाव;
Nonatthi-novigatapaccayā = अनुपस्थिति-कारण का अभाव और विलीनता-कारण का अभाव. Hetu-ārammaṇapaccayādi = मूल-कारण और
विषय-कारण आदि (not yet in the sample).
Chains of ablatives (R.CH): words joined by ", "; "…" and "…pe…" become "…" with the Pāli spacing:
hetupaccayā naārammaṇapaccayā = मूल-कारण से, विषय-कारण के बिना.

## 3. Kusalattika items (R.ACC, R.NOM, R.DAT_ITEM)

kusalaṃ / akusalaṃ / abyākataṃ dhammaṃ = हितकर / हानिकर / नैतिक रूप से अनिर्धारित परिघटना
kusalañca abyākatañca dhammaṃ = हितकर परिघटना और नैतिक रूप से अनिर्धारित परिघटना
akusalañca abyākatañca dhammaṃ = हानिकर परिघटना और नैतिक रूप से अनिर्धारित परिघटना
kusalañca akusalañca dhammaṃ = हितकर परिघटना और हानिकर परिघटना
kusalañca akusalañca abyākatañca dhammaṃ = हितकर परिघटना, हानिकर परिघटना और नैतिक रूप से अनिर्धारित परिघटना
kusalo / akusalo / abyākato dhammo = हितकर / हानिकर / नैतिक रूप से अनिर्धारित परिघटना
kusalo ca abyākato ca dhammā = हितकर और नैतिक रूप से अनिर्धारित परिघटनाएँ
akusalo ca abyākato ca dhammā = हानिकर और नैतिक रूप से अनिर्धारित परिघटनाएँ
kusalo ca akusalo ca dhammā = हितकर और हानिकर परिघटनाएँ
kusalo ca akusalo ca abyākato ca dhammā = हितकर, हानिकर और नैतिक रूप से अनिर्धारित परिघटनाएँ
kusalassa / akusalassa / abyākatassa dhammassa = हितकर / हानिकर / नैतिक रूप से अनिर्धारित परिघटना के लिए
kusalassa ca abyākatassa ca dhammassa = हितकर परिघटना और नैतिक रूप से अनिर्धारित परिघटना के लिए
akusalassa ca abyākatassa ca dhammassa = हानिकर परिघटना और नैतिक रूप से अनिर्धारित परिघटना के लिए
Other triads and dyads: the pi-1 1-matika.md Hindi item, singular in frames (सुखद अनुभूति से जुड़ी परिघटना) (not yet in the sample)

## 4. Paṭicca-type frames

X dhammaṃ paṭicca Y dhammo uppajjati Cpaccayā = X परिघटना पर निर्भर होकर Y परिघटना C-कारण से उत्पन्न होती है
… dhammā uppajjanti … = … परिघटनाएँ … उत्पन्न होती हैं
Negative: … uppajjati naCpaccayā = … C-कारण के बिना उत्पन्न होती है
Two conditions with "…": uppajjati anantarapaccayā… samanantarapaccayā = निकटता-कारण से… पूर्ण निकटता-कारण से उत्पन्न होती है
Frame without verb: Akusalaṃ dhammaṃ paṭicca… tīṇi. = हानिकर परिघटना पर निर्भर होकर… तीन।
uppajjati navipākapaccayā… tīṇi. = कर्म-फल-कारण के बिना उत्पन्न होती है… तीन।
X dhammaṃ sahajāto Y dhammo uppajjati = X परिघटना के साथ जन्म लेकर Y परिघटना … उत्पन्न होती है (not yet in the sample)
X dhammaṃ paccayā Y dhammo uppajjati = X परिघटना के कारण Y परिघटना … उत्पन्न होती है (not yet in the sample)
X dhammaṃ nissāya Y dhammo uppajjati = X परिघटना के आश्रय से Y परिघटना … उत्पन्न होती है (not yet in the sample)
X dhammaṃ saṃsaṭṭho Y dhammo uppajjati = X परिघटना से घुल-मिलकर Y परिघटना … उत्पन्न होती है (not yet in the sample)
X dhammaṃ sampayutto Y dhammo uppajjati = X परिघटना से जुड़कर Y परिघटना … उत्पन्न होती है (not yet in the sample)

### Bodies: khandha and matter clauses (R.SUBJ_P «… पर निर्भर होकर» + R.OBJ_P)
kusalaṃ / akusalaṃ ekaṃ khandhaṃ paṭicca tayo khandhā = एक हितकर / एक हानिकर समूह पर निर्भर होकर तीन समूह
tayo khandhe paṭicca eko khandho = तीन समूहों पर निर्भर होकर एक समूह
dve khandhe paṭicca dve khandhā = दो समूहों पर निर्भर होकर दो समूह
kusale / akusale khandhe paṭicca cittasamuṭṭhānaṃ rūpaṃ = हितकर / हानिकर समूहों पर निर्भर होकर मन से उत्पन्न भौतिक रूप
… cittasamuṭṭhānañca rūpaṃ / kaṭattā ca rūpaṃ / vatthu ca = … और मन से उत्पन्न भौतिक रूप / और किए गए कर्म से उत्पन्न भौतिक रूप / और आधार
vipākābyākataṃ kiriyābyākataṃ ekaṃ khandhaṃ = कर्म-फल रूपी या केवल क्रिया रूपी नैतिक रूप से अनिर्धारित एक समूह
vipākābyākataṃ / kiriyābyākataṃ ekaṃ khandhaṃ = कर्म-फल रूपी / केवल क्रिया रूपी नैतिक रूप से अनिर्धारित एक समूह
ahetukaṃ vipākābyākataṃ kiriyābyākataṃ ekaṃ khandhaṃ = मूल से रहित, कर्म-फल रूपी या केवल क्रिया रूपी नैतिक रूप से अनिर्धारित एक समूह
vipākābyākate kiriyābyākate khandhe = कर्म-फल रूपी और केवल क्रिया रूपी नैतिक रूप से अनिर्धारित समूहों (plural pair = «और», singular pair = «या»)
pañcaviññāṇasahagataṃ ekaṃ khandhaṃ paṭicca = पाँच प्रकार की चेतना के साथ होने वाले एक समूह पर निर्भर होकर
vicikicchāsahagate uddhaccasahagate khandhe paṭicca vicikicchāsahagato uddhaccasahagato moho = संशय के साथ होने वाले और बेचैनी के साथ होने वाले समूहों पर निर्भर होकर संशय के साथ होने वाला या बेचैनी के साथ होने वाला मोह
kusale khandhe ca mahābhūte ca paṭicca = हितकर समूहों और महाभूतों पर निर्भर होकर
khandhe paṭicca vatthu, vatthuṃ paṭicca khandhā = समूहों पर निर्भर होकर आधार, आधार पर निर्भर होकर समूह
ekaṃ mahābhūtaṃ paṭicca tayo mahābhūtā = एक महाभूत पर निर्भर होकर तीन महाभूत
tayo mahābhūte paṭicca ekaṃ mahābhūtaṃ = तीन महाभूतों पर निर्भर होकर एक महाभूत
dve mahābhūte paṭicca dve mahābhūtā = दो महाभूतों पर निर्भर होकर दो महाभूत
mahābhūte paṭicca cittasamuṭṭhānaṃ rūpaṃ kaṭattārūpaṃ upādārūpaṃ = महाभूतों पर निर्भर होकर मन से उत्पन्न भौतिक रूप, किए गए कर्म से उत्पन्न भौतिक रूप और व्युत्पन्न भौतिक रूप
… cittasamuṭṭhānaṃ rūpaṃ upādārūpaṃ / kaṭattārūpaṃ upādārūpaṃ = … मन से उत्पन्न भौतिक रूप और व्युत्पन्न भौतिक रूप / किए गए कर्म से उत्पन्न भौतिक रूप और व्युत्पन्न भौतिक रूप
bāhiraṃ / āhārasamuṭṭhānaṃ / utusamuṭṭhānaṃ / asaññasattānaṃ ekaṃ mahābhūtaṃ = एक बाह्य महाभूत / आहार से उत्पन्न एक महाभूत / तापमान से उत्पन्न एक महाभूत / पहचान-रहित प्राणियों में एक महाभूत
bāhiraṃ… āhārasamuṭṭhānaṃ… utusamuṭṭhānaṃ… = बाह्य… आहार से उत्पन्न… तापमान से उत्पन्न…
bāhire / āhārasamuṭṭhāne / utusamuṭṭhāne / asaññasattānaṃ mahābhūte = बाह्य / आहार से उत्पन्न / तापमान से उत्पन्न महाभूतों / पहचान-रहित प्राणियों में महाभूतों
asaññasattānaṃ mahābhūte paṭicca rūpajīvitindriyaṃ = पहचान-रहित प्राणियों में महाभूतों पर निर्भर होकर भौतिक जीवन-क्षमता
kusale khandhe paṭicca kusalā cetanā = हितकर समूहों पर निर्भर होकर हितकर इरादा (akusalā / kiriyābyākatā cetanā likewise)
paṭisandhikkhaṇe / ahetukapaṭisandhikkhaṇe / arūpe = पुनर्जन्म के क्षण में / मूल से रहित पुनर्जन्म के क्षण में / अभौतिक लोक में
Vatthuṃ purejātapaccayā. = आधार पर पूर्व-उत्पत्ति-कारण से।
Khandhe / Vatthuṃ vippayuttapaccayā. = समूहों / आधार पर अलगाव-कारण से।
Khandhā vatthuṃ vippayuttapaccayā. = समूह आधार पर अलगाव-कारण से।
Cittasamuṭṭhānaṃ rūpaṃ / Kaṭattārūpaṃ / Vatthu khandhe vippayuttapaccayā. = मन से उत्पन्न भौतिक रूप / किए गए कर्म से उत्पन्न भौतिक रूप / आधार समूहों पर अलगाव-कारण से।
akusalā abyākatā tayo khandhā = हानिकर और नैतिक रूप से अनिर्धारित तीन समूह (not yet in the sample)

## 5. Counting frames (R.count_hi)

Hetuyā nava, ārammaṇe tīṇi = मूल-कारण में नौ, विषय-कारण में तीन
Hetupaccayā ārammaṇe tīṇi = मूल-कारण से, विषय-कारण में तीन (an ablative before an ablative or a locative takes ", ")
adhipatiyā tīṇi anantare tīṇi (no comma in the Pāli) = प्रधानता-कारण में तीन निकटता-कारण में तीन (no comma added)
avigate tīṇi…pe…. = अविलीनता-कारण में तीन…।
Ārammaṇapaccayā hetuyā tīṇi = विषय-कारण से, मूल-कारण में तीन
Nahetuyā dve = मूल-कारण के अभाव में दो (not yet in the sample)
Nahetupaccayā naārammaṇe ekaṃ = मूल-कारण के बिना, विषय-कारण के अभाव में एक (not yet in the sample)
Hetupaccayā naārammaṇe … / Nahetupaccayā ārammaṇe … = मूल-कारण से, विषय-कारण के अभाव में … / मूल-कारण के बिना, विषय-कारण में … (not yet in the sample)
Gaṇanā hetumūlakā / Gaṇanā hetumūlakā. = मूल-कारण से शुरू होने वाली गणना / मूल-कारण से शुरू होने वाली गणना।
Suddhaṃ = अकेले-अकेले कारण
Dukaṃ / Tikaṃ / Catukkaṃ / Pañcakaṃ … Dvādasakaṃ / Terasakaṃ … Bāvīsakaṃ / Tevīsakaṃ = दो कारणों का मेल / तीन कारणों का मेल / चार कारणों का मेल / पाँच कारणों का मेल … बारह कारणों का मेल / तेरह कारणों का मेल … बाईस कारणों का मेल / तेईस कारणों का मेल
Xdukaṃ (counting heading) = X-कारण के साथ दो कारणों का मेल (Āsevanadukaṃ, Kammadukaṃ, Vipākadukaṃ, Avigatadukaṃ …)
naXdukaṃ = X-कारण के अभाव के साथ दो कारणों का मेल (not yet in the sample)
Ārammaṇādidukāni / Āhārādidukāni = विषय-कारण आदि के साथ दो कारणों के मेल / आहार-कारण आदि के साथ दो कारणों के मेल
Naanantarādidukāni = निकटता-कारण के अभाव आदि के साथ दो कारणों के मेल (not yet in the sample)
(sāsevanaṃ) / (savipākaṃ) = (पुनरावृत्ति-कारण सहित) / (कर्म-फल-कारण सहित) (not yet in the sample)
ghaṭanā / Xghaṭanā = संयोजन / X-कारण के संयोजन; «A-B-…nti n» = A-कारण, B-कारण … और Z-कारण के संयोजन में n (not yet in the sample)
sāmañña / pakiṇṇaka / sabhāga = सामान्य / फुटकर / X-कारण के साथी कारण (not yet in the sample)

## 6. Pañhāvāra frame and kind labels

X dhammo Y dhammassa Cpaccayena paccayo = X परिघटना, Y परिघटना के लिए C-कारण के रूप में कारण होती है
kusalā hetū sampayuttakānaṃ khandhānaṃ hetupaccayena paccayo = हितकर मूल जुड़े हुए समूहों के लिए मूल-कारण के रूप में कारण होते हैं
cittasamuṭṭhānānaṃ rūpānaṃ = मन से उत्पन्न भौतिक रूपों के लिए
sampayuttakānaṃ khandhānaṃ cittasamuṭṭhānānañca rūpānaṃ = जुड़े हुए समूहों के लिए और मन से उत्पन्न भौतिक रूपों के लिए
sampayuttakānaṃ khandhānaṃ kaṭattā ca rūpānaṃ = जुड़े हुए समूहों के लिए और किए गए कर्म से उत्पन्न भौतिक रूपों के लिए
vipākābyākatā kiriyābyākatā hetū = कर्म-फल रूपी और केवल क्रिया रूपी नैतिक रूप से अनिर्धारित मूल
Ārammaṇādhipati, sahajātādhipati. = विषय रूपी प्रधानता, सह-उत्पत्ति रूपी प्रधानता।
kusalādhipati / akusalādhipati / vipākābyākatakiriyābyākatādhipati = हितकर प्रधानता / हानिकर प्रधानता / कर्म-फल रूपी या केवल क्रिया रूपी नैतिक रूप से अनिर्धारित प्रधानता
dānaṃ datvā sīlaṃ samādiyitvā uposathakammaṃ katvā = दान देकर, सदाचार ग्रहण करके, उपवास-व्रत का पालन करके
taṃ paccavekkhati / paccavekkhanti = उस पर पुनः विचार करता है / करते हैं; X garuṃ katvā paccavekkhati = X को महत्व देकर पुनः विचार करता है
pubbe suciṇṇāni = पहले भली-भाँति किए गए कार्यों (पर / का / को)
jhānā / maggā vuṭṭhahitvā = ध्यान से / मार्ग से उठकर
sekkhā / sekkhā vā puthujjanā vā / arahā = सीखने के चरण वाले व्यक्ति / सीखने के चरण वाले या साधारण व्यक्ति / अर्हत्
gotrabhu / vodāna / phala / nibbāna = गोत्र-परिवर्तन / शुद्धि / फल / निर्वाण
X aniccato dukkhato anattato vipassati = X को अनित्य, दुःख और आत्मा से रहित के रूप में अंतर्दृष्टि से देखता है
cetopariyañāṇena kusalacittasamaṅgissa cittaṃ jānāti = दूसरों के मन को जानने के ज्ञान से हितकर मन से युक्त व्यक्ति के मन को जानता है
X assādeti abhinandati = X का रस लेता है, उसमें (plural object: उनमें) आनंद लेता है; taṃ = उसका …
taṃ ārabbha rāgo / diṭṭhi / vicikicchā / uddhaccaṃ / domanassaṃ uppajjati = उसे विषय बनाकर राग उत्पन्न होता है / दृष्टि उत्पन्न होती है / संशय उत्पन्न होता है / बेचैनी उत्पन्न होती है / उदासी उत्पन्न होती है
taṃ garuṃ katvā rāgo uppajjati = उसे महत्व देकर राग उत्पन्न होता है
Jhāne parihīne vippaṭisārissa domanassaṃ uppajjati = ध्यान के छूट जाने पर ग्लानि से भरे व्यक्ति में उदासी उत्पन्न होती है
kusale / akusale niruddhe vipāko tadārammaṇatā uppajjati = हितकर / हानिकर के समाप्त होने पर कर्म-फल उसी विषय को लेकर उत्पन्न होता है
pahīne / vikkhambhite / pubbe samudāciṇṇe kilese = छोड़े जा चुके / दबाए जा चुके / पहले बार-बार उठे मन के क्लेशों
Ākāsānañcāyatanakusalaṃ viññāṇañcāyatanakusalassa = अनंत आकाश के क्षेत्र का हितकर मन, अनंत चेतना के क्षेत्र के हितकर मन के लिए
Ākiñcaññāyatana… nevasaññānāsaññāyatana… = कुछ भी न होने के क्षेत्र का … न पहचान न अ-पहचान के क्षेत्र के …
…vipākassa ca, kiriyassa ca = … कर्म-फल रूपी मन के लिए और केवल क्रिया रूपी मन के लिए; …kiriyaṃ = … का केवल क्रिया रूपी मन
iddhividha- / cetopariya- / pubbenivāsānussati- / yathākammūpaga- / anāgataṃsa-ñāṇassa, āvajjanāya = अलौकिक शक्तियों के ज्ञान, दूसरों के मन को जानने के ज्ञान, पूर्व जन्मों के अनुस्मरण के ज्ञान, प्राणियों के अपने कर्मों के अनुसार जाने के ज्ञान, भविष्य को जानने के ज्ञान और मन को विषय की ओर मोड़ने के लिए
Nibbānaṃ phalassa āvajjanāya = निर्वाण फल के लिए और मन को विषय की ओर मोड़ने के लिए
Nibbānaṃ gotrabhussa vodānassa maggassa = निर्वाण गोत्र-परिवर्तन, शुद्धि और मार्ग के लिए
Rūpāyatanaṃ cakkhuviññāṇassa = दृश्य रूप का इंद्रिय-क्षेत्र आँख की चेतना के लिए (sadda / gandha / rasa / phoṭṭhabba: ध्वनि / गंध / स्वाद / स्पर्श का इंद्रिय-क्षेत्र कान / नाक / जीभ / शरीर की चेतना के लिए)
Sotaṃ… ghānaṃ… jivhaṃ… kāyaṃ… rūpe… sadde… gandhe… rase… phoṭṭhabbe… vatthuṃ… = कान… नाक… जीभ… शरीर… दृश्य रूपों… ध्वनियों… गंधों… स्वादों… स्पर्शों… आधार…
dibbena cakkhunā rūpaṃ passati / dibbāya sotadhātuyā saddaṃ suṇāti = दिव्य आँख से दृश्य रूप को देखता है / दिव्य कान के तत्व से ध्वनि को सुनता है
Kind labels (not yet in the sample): Ārammaṇūpanissayo / Anantarūpanissayo / Pakatūpanissayo = विषय रूपी प्रबल आश्रय / निकटता रूपी प्रबल आश्रय / स्वाभाविक प्रबल आश्रय; Ārammaṇapurejātaṃ / Vatthupurejātaṃ = विषय रूपी पूर्व-उत्पत्ति / आधार रूपी पूर्व-उत्पत्ति; labels sahajātaṃ, purejātaṃ, pacchājātaṃ, āhāraṃ, indriyaṃ = सह-उत्पत्ति, पूर्व-उत्पत्ति, पश्चात्-उत्पत्ति, आहार, क्षमता (no «रूपी»; compounds keep «रूपी»); nānākkhaṇikā = भिन्न क्षण; upanissāya = के प्रबल आश्रय से; anulomaṃ (moment) = अनुरूपता; bhavaṅga = जीवन-धारा; āvajjanā = मन को विषय की ओर मोड़ना; parikamma = प्रारंभिक तैयारी; nirodhā vuṭṭhahantassa = समाप्ति की ध्यान-अवस्था से बाहर आने वाले व्यक्ति में; uppannaṃ = उत्पन्न हो चुका
Hetu dhammo hetussa dhammassa hetupaccayena paccayo = मूल रूपी परिघटना, मूल रूपी परिघटना के लिए मूल-कारण के रूप में कारण होती है (not yet in the sample)

## 7. Definitions (Paccayaniddesa, R.SUBJ / R.DAT)

Xpaccayoti – … = X-कारण – …
hetū hetusampayuttakānaṃ dhammānaṃ taṃsamuṭṭhānānañca rūpānaṃ = मूल, मूलों से जुड़ी परिघटनाओं के लिए और उनसे उत्पन्न भौतिक रूपों के लिए
X-dhātuyā taṃsampayuttakānañca dhammānaṃ = X के तत्व के लिए और उससे जुड़ी परिघटनाओं के लिए (two dhātus: … और उनसे जुड़ी परिघटनाओं के लिए)
cakkhu- / sota- / ghāna- / jivhā- / kāya-viññāṇadhātu; manodhātu; manoviññāṇadhātu = आँख / कान / नाक / जीभ / शरीर की चेतना का तत्व; मन का तत्व; मन की चेतना का तत्व
X taṃsampayuttakā ca dhammā = X और उससे जुड़ी परिघटनाएँ (verb «होती हैं»)
sampayuttakānaṃ dhammānaṃ taṃsamuṭṭhānānañca rūpānaṃ = जुड़ी हुई परिघटनाओं के लिए और उनसे उत्पन्न भौतिक रूपों के लिए
chanda- / vīriya- / citta- / vīmaṃsādhipati = प्रधान बनी हुई चाह / प्रधान बना हुआ उत्साह / प्रधान बना हुआ मन / प्रधान बनी हुई जाँच-परख (+ comma, then «चाह से जुड़ी परिघटनाओं के लिए …»)
Yaṃ yaṃ dhammaṃ ārabbha (garuṃ katvā) ye ye dhammā uppajjanti cittacetasikā dhammā, te te dhammā tesaṃ tesaṃ dhammānaṃ … = जिस-जिस परिघटना को विषय बनाकर (महत्व देकर) जो-जो परिघटनाएँ उत्पन्न होती हैं, यानी मन और मन की सहचर परिघटनाएँ, वह-वह परिघटना उन-उन परिघटनाओं के लिए … कारण होती है
Yesaṃ yesaṃ dhammānaṃ anantarā (samanantarā) … te te dhammā … = जिन-जिन परिघटनाओं के ठीक बाद (बिलकुल ठीक बाद) … वे-वे परिघटनाएँ … कारण होती हैं
purimā purimā X dhammā pacchimānaṃ pacchimānaṃ Y dhammānaṃ (kesañci) = पहले-पहले की X परिघटनाएँ बाद-बाद की (कुछ) Y परिघटनाओं के लिए
cattāro khandhā arūpino / cattāro mahābhūtā aññamaññaṃ = चार अभौतिक समूह / चार महाभूत एक-दूसरे के लिए
Okkantikkhaṇe nāmarūpaṃ = गर्भ में उतरने के क्षण में मानसिक पक्ष और भौतिक रूप
cittacetasikā dhammā / pacchājātā cittacetasikā dhammā = मन और मन की सहचर परिघटनाएँ / बाद में उत्पन्न मन और मन की सहचर परिघटनाएँ
Mahābhūtā upādārūpānaṃ = महाभूत व्युत्पन्न भौतिक रूपों के लिए
Rūpino dhammā arūpīnaṃ dhammānaṃ = भौतिक परिघटनाएँ अभौतिक परिघटनाओं के लिए
kiñci kāle …, kiñci kāle na … = किसी समय … कारण होती हैं, किसी समय … कारण नहीं होतीं
Yaṃ rūpaṃ nissāya manodhātu ca manoviññāṇadhātu ca vattanti, taṃ rūpaṃ = जिस भौतिक रूप के आश्रय से मन का तत्व और मन की चेतना का तत्व क्रियाशील होते हैं, वह भौतिक रूप
Utubhojanampi / Puggalopi / Senāsanampi = तापमान और भोजन भी / व्यक्ति भी / निवास-स्थान भी
purejātassa imassa kāyassa = पहले उत्पन्न इस शरीर के लिए
kusalākusalaṃ kammaṃ vipākānaṃ khandhānaṃ kaṭattā ca rūpānaṃ = हितकर और हानिकर कर्म, कर्म-फल रूपी समूहों के लिए और किए गए कर्म से उत्पन्न भौतिक रूपों के लिए
kabaḷīkāro āhāro / Arūpino āhārā = कौर-कौर खाया जाने वाला भोजन / अभौतिक आहार
cakkhundriyaṃ … kāyindriyaṃ / Rūpajīvitindriyaṃ / Arūpino indriyā = आँख की क्षमता … शरीर की क्षमता / भौतिक जीवन-क्षमता / अभौतिक क्षमताएँ
jhānaṅgāni / maggaṅgāni = ध्यान के अंग / मार्ग के अंग
samanantaraniruddhā / samanantaravigatā cittacetasikā dhammā paṭuppannānaṃ cittacetasikānaṃ dhammānaṃ = बिलकुल ठीक पहले समाप्त हो चुके / विलीन हो चुके मन और मन की सहचर परिघटनाएँ वर्तमान मन और मन की सहचर परिघटनाओं के लिए

## 8. Siyā questions (R.siya_frame)

Siyā X dhammaṃ paṭicca Y dhammo uppajjeyya Cpaccayā. = क्या X परिघटना पर निर्भर होकर Y परिघटना C-कारण से उत्पन्न हो सकती है?
… dhammā uppajjeyyuṃ … = … परिघटनाएँ … उत्पन्न हो सकती हैं?
Chains: hetupaccayā ārammaṇapaccayā = मूल-कारण से, विषय-कारण से; adhipatipaccayā… anantarapaccayā… = प्रधानता-कारण से… निकटता-कारण से…
"…pe… siyā" or "… siyā" inside a line = "?… क्या"; a chain ending "…." = "…" before the verb, then "?".
Continuation lines without Siyā (Hetupaccayā ārammaṇapaccayā … noavigatapaccayā.) = the ablative chain + «।».
(verify_hi's "final '?' differs" on these segments is expected: the question form is user-approved.)

## 9. Negated items (Dhammapaccanīya) (not yet in the sample)

nakusalaṃ dhammaṃ / nakusalo dhammo = हितकर न होने वाली परिघटना
naakusalo / naabyākato dhammo = हानिकर न होने वाली परिघटना / नैतिक रूप से अनिर्धारित न होने वाली परिघटना
Nakusalaṃ dhammaṃ paṭicca nakusalo dhammo uppajjati hetupaccayā = हितकर न होने वाली परिघटना पर निर्भर होकर हितकर न होने वाली परिघटना मूल-कारण से उत्पन्न होती है
nakusalañca naabyākatañca dhammaṃ = हितकर न होने वाली परिघटना और नैतिक रूप से अनिर्धारित न होने वाली परिघटना
nahetu dhammo = मूल रूपी न होने वाली परिघटना; nahetuṃ nakusalaṃ dhammaṃ = मूल रूपी न होने वाली, हितकर न होने वाली परिघटना
nanahetu = मूल रूपी न होने वाली न होने वाली (no quotes)
na + a pi-1 item (nadassanena pahātabba …) = the pi-1 negated wording (सत्य-दर्शन से न छोड़ी जाने वाली …)
Kusalaṃ dhammaṃ paṭicca nakusalo dhammo … / Nakusalaṃ dhammaṃ paṭicca akusalo dhammo … = हितकर परिघटना पर निर्भर होकर हितकर न होने वाली परिघटना … / हितकर न होने वाली परिघटना पर निर्भर होकर हानिकर परिघटना …
Duka-tika, tika-duka, tika-tika, duka-duka: two items in Pāli order joined by a comma, one noun: Hetuṃ kusalaṃ dhammaṃ = मूल रूपी, हितकर परिघटना

## 10. Notes (editorial, in parentheses, R.NOTE)

(Xpaccayaṃ Ypaccayasadisaṃ.) = (X-कारण Y-कारण के समान है।)
(Xpaccayampi Ypaccayampi Zpaccayasadisaṃ.) = (X-कारण और Y-कारण भी Z-कारण के समान हैं।)
(Anantarampi samanantarampi ārammaṇapaccayasadisaṃ.) = (निकटता-कारण और पूर्ण निकटता-कारण भी विषय-कारण के समान हैं।)
naXpaccayasadisaṃ = X-कारण के अभाव के समान; (Naārammaṇapaccayasadisaṃ.) = (विषय-कारण के अभाव के समान।)
(Saṅkhitaṃ. …) = (संक्षिप्त। …)
(Yathā hetupaccayo vitthārito, evaṃ Xpaccayopi vitthāretabbo vācanāmaggena.) = (जैसे मूल-कारण का विस्तार किया गया है, वैसे ही X-कारण का भी पाठ के क्रम से विस्तार करना चाहिए।)
(Yathā anulome hetupaccayo vitthārito, evaṃ paccanīyepi nahetupaccayo vitthāretabbo.) = (जैसे सकारात्मक क्रम में मूल-कारण का विस्तार किया गया है, वैसे ही नकारात्मक क्रम में भी मूल-कारण के अभाव का विस्तार करना चाहिए।)
(… evaṃ anulomapaccanīyepi padaṃ vitthāretabbaṃ.) = (… वैसे ही सकारात्मक-नकारात्मक क्रम में भी पद का विस्तार करना चाहिए।)
(Ekekassa padassa ekamūlakaṃ, … sabbamūlakaṃ asammuyhantena vitthāretabbaṃ.) = (हर एक पद की एक कारण वाली शृंखला, … और सभी कारणों वाली शृंखला का बिना भ्रमित हुए विस्तार करना चाहिए।)
(Pañcamūlakādikā saṃkhittā. …) = (पाँच कारणों वाली शृंखला आदि संक्षिप्त हैं। …)
(… yāva tevīsatimūlakaṃ evaṃ paccanīyepi vitthāretabbaṃ.) = (… और इसी तरह तेईस कारणों वाली शृंखला तक है, वैसे ही नकारात्मक क्रम में भी विस्तार करना चाहिए।)
(Ime tevīsatipaccayā sajjhāyantena vitthāretabbā.) = (इन तेईस कारणों का पाठ करते हुए विस्तार करना चाहिए।)
(Ārammaṇe ṭhitena sabbattha tīṇeva pañhā.) = (विषय-कारण पर टिके रहने पर हर जगह तीन ही प्रश्न हैं।)
(Xmūlake Y natthi.) = (X-कारण से शुरू होने वाली शृंखला में Y-कारण नहीं है।)
(Ekekaṃ paccayaṃ mūlakaṃ kātūna sajjhāyantena gaṇetabbāti.) = (हर एक कारण से शुरू होने वाली शृंखला बनाकर पाठ करते हुए गिनना चाहिए।)
asammuyhantena vitthāretabbaṃ / sajjhāyantena gaṇetabbā = बिना भ्रमित हुए विस्तार करना चाहिए / पाठ करते हुए गिनना चाहिए
(sabbattha ekaṃ) = (हर जगह एक) (not yet in the sample)
Mūlaṃ kātabbaṃ / pucchitabbaṃ = मूल वाक्य …; gamana = प्रसंग; (cakkaṃ) / cakkaṃ kātabbaṃ / bandhitabbaṃ = (चक्र) / चक्र बनाना चाहिए / चक्र बाँधना चाहिए; ninnānākaraṇaṃ = बिना किसी अंतर के (not yet in the sample)

## 11. The "six methods" stanza

(Ka) tikañca paṭṭhānavaraṃ dukuttamaṃ, = (क) तीन-तीन के वर्गीकरणों के श्रेष्ठ कारण-संबंध और दो-दो के वर्गीकरणों के उत्तम कारण-संबंध,
Dukaṃ tikañceva tikaṃ dukañca; = दो-दो के साथ तीन-तीन, और तीन-तीन के साथ दो-दो;
Tikaṃ tikañceva dukaṃ dukañca, = तीन-तीन के साथ तीन-तीन, और दो-दो के साथ दो-दो,
Cha anulomamhi / paccanīyamhi / anulomapaccanīyamhi / paccanīyānulomamhi nayā sugambhīrāti. = सकारात्मक क्रम / नकारात्मक क्रम / सकारात्मक-नकारात्मक क्रम / नकारात्मक-सकारात्मक क्रम में ये छह विधियाँ अत्यंत गहन हैं।
