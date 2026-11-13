# pi-6 Yamaka, Hindi plain RAILS: sentence formulas

Authoritative for sentence shape (hi-rails-brief.md). Read-only for every agent except the sample agent; a NEW recurring formula goes in your own notes file rails\notes-<files>.md.
The same strings are Python constants in build_rails_sample.py (import it read-only: `sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\rails"); import build_rails_sample as S`). Its `translate_line()` raises ValueError on any line it has no formula for; it is a starting point, not a substitute for reading every line.
Built from: preamble.md, 1-mulayamaka.md (complete), 2-01-khandhayamaka.md lines 1-638 (to ^6-2-55). Lines marked **(not yet in the sample)** were checked in a dry run on the rest of 2-01 and on 2-02 (coverage_sample.py), not reviewed by the user.
Precedence: locked termbase (words) > this file (sentence shape) > hi-zeroshot-terms.md / harmonise-notes.md "Decisions".

## 0. Conventions
- One Hindi line per Pāli line; block ID at the end of the segment's last line; headings keep their #-level; one blank line between segments.
- Labels: (Ka) (Kha) (Ga) (Gha) (Ṅa) (Ca) = (क) (ख) (ग) (घ) (ङ) (च). Digits stay: "(1)", "2-10.", "1.".
- Questions end «?», statements «।». The quotative -ti is dropped (kusalāti, rūpanti, uppajjatīti, parijānitthāti).
- "…pe…" = "…" at the same spot. A sentence ending "…pe…." ends «…।»; an abbreviated question list ending "…pe…." or "…?" ends «…?» (^6-1-49, ^6-1-98, ^6-1-99).
- Dash: an en dash only where the Pāli has an en or em dash at that spot (in the sample only ^6-2-1). Never ":-".
- Variants: «[वर्तनी-भेद (Ka.): <Pāli>]» for spelling only, «[पाठभेद (Syā.): <Pāli>]» when words differ; sigla capitalised, several sigla «(Sī., Syā.)»; the bracket follows the Hindi word or clause it concerns. A Pāli editorial note inside the bracket is translated after a semicolon: "evamuparipi" = «; आगे भी इसी प्रकार».
- Commas: «X, Y है» (comma between subject and nominal predicate when two noun phrases meet); always «, पर» before the contrast.
- Identical Pāli = identical Hindi. Lines that differ only by a comma in the Pāli ("kusalamūlakaṃ na kusalaṃ" vs "…ekamūlaṃ, na kusalaṃ") get the same Hindi, comma included.

## 1. Book frame and chapter titles
- Namo tassa bhagavato arahato sammāsambuddhassa = उन भगवान, अर्हत्, पूर्ण रूप से जागृत बुद्ध को नमन
- # Abhidhammapiṭake = # अभिधम्म पिटक में
- ## Yamakapāḷi = ## प्रश्नों के जोड़े
- Yamakapāḷi niṭṭhitā = “प्रश्नों के जोड़े” ग्रंथ समाप्त। (not yet in the sample)
- Chapter titles (###): Mūlayamakaṃ = मूलों पर प्रश्नों के जोड़े; Khandhayamakaṃ = समूहों पर प्रश्नों के जोड़े; Āyatanayamakaṃ = इंद्रिय-क्षेत्रों पर प्रश्नों के जोड़े; Dhātuyamakaṃ = तत्वों पर प्रश्नों के जोड़े; Saccayamakaṃ = सत्यों पर प्रश्नों के जोड़े; Saṅkhārayamakaṃ = रचनाओं पर प्रश्नों के जोड़े; Anusayayamakaṃ = सुप्त प्रवृत्तियों पर प्रश्नों के जोड़े; Cittayamakaṃ = मन पर प्रश्नों के जोड़े; Dhammayamakaṃ = परिघटनाओं पर प्रश्नों के जोड़े; Indriyayamakaṃ = क्षमताओं पर प्रश्नों के जोड़े
- <X>yamakapāḷi niṭṭhitā / <X>yamakaṃ niṭṭhitaṃ = <chapter title> पूरे हुए। (sample: मूलों पर प्रश्नों के जोड़े पूरे हुए।; Khandhayamakapāḷi niṭṭhitā = समूहों पर प्रश्नों के जोड़े पूरे हुए। not yet in the sample)

## 2. Headings
- (Ka) uddeso = (क) सूची; (Kha) niddeso = (ख) व्याख्या
- Mūlavāro = मूल का खंड
- Kusalā dhammā = हितकर परिघटनाएँ
- (1) Mūlanayo = (1) मूल की विधि; (2) Mūlamūlanayo = (2) मूल के मूल की विधि; (3) Mūlakanayo = (3) मूल पर आधारित होने की विधि; (4) Mūlamūlakanayo = (4) मूल के मूल पर आधारित होने की विधि
- Akusalā / Abyākatā / Nāmā / Kusalā dhammā (1) mūlanayo = हानिकर / नैतिक रूप से अनिर्धारित / मानसिक पक्ष की / हितकर परिघटनाएँ (1) मूल की विधि
- 2-10. Hetuvārādi = 2-10. हेतु का खंड आदि
- Paṇṇattivāro = शब्दावली का खंड; Paṇṇattivāraniddesa = शब्दावली के खंड की व्याख्या
- Padasodhanavāro = शब्दों की जाँच का खंड; Padasodhanamūlacakkavāro = शब्दों की जाँच पर आधारित चक्र का खंड
- Suddhakhandhavāro = केवल समूहों का खंड; Suddhakhandhamūlacakkavāro = केवल समूहों पर आधारित चक्र का खंड
- (not yet in the sample) Suddhāyatana- / Suddhadhātu- / Suddhasacca- / Suddhasaṅkhāra- / Suddhadhamma- / Suddhindriya-vāro = केवल इंद्रिय-क्षेत्रों / तत्वों / सत्यों / रचनाओं / परिघटनाओं / क्षमताओं का खंड; …mūlacakkavāro = केवल … पर आधारित चक्र का खंड
- (Ka) anulomaṃ = (क) सकारात्मक; (Kha) paccanīkaṃ = (ख) नकारात्मक; paṭilomaṃ = विपरीत (not yet in the sample)
- Pavattivāro 1. uppādavāro = प्रक्रिया का खंड 1. उत्पन्न होने का खंड
- (not yet in the sample) Pavatti 2. nirodhavāro = प्रक्रिया 2. समाप्त होने का खंड; Pavatti 3. uppādanirodhavāro = प्रक्रिया 3. उत्पन्न होने और समाप्त होने का खंड; Uppādanirodhavāro = उत्पन्न होने और समाप्त होने का खंड
- (1) Paccuppannavāro = (1) वर्तमान का खंड
- (not yet in the sample) (2) Atītavāro = (2) अतीत का खंड; (3) Anāgatavāro = (3) भविष्य का खंड; (4) Paccuppannātītavāro = (4) वर्तमान और अतीत का खंड; (5) Paccuppannānāgatavāro = (5) वर्तमान और भविष्य का खंड; (6) Atītānāgatavāro = (6) अतीत और भविष्य का खंड; without the number (Pariññāvāra): वर्तमान का खंड, अतीत का खंड …
- (Ka) anulomapuggalo = (क) सकारात्मक: व्यक्ति; (Kha) anulomaokāso = (ख) सकारात्मक: स्थान; (Ga) anulomapuggalokāsā = (ग) सकारात्मक: व्यक्ति और स्थान; (Gha) paccanīkapuggalo = (घ) नकारात्मक: व्यक्ति; (Ṅa) paccanīkaokāso = (ङ) नकारात्मक: स्थान; (Ca) paccanīkapuggalokāsā = (च) नकारात्मक: व्यक्ति और स्थान
- (not yet in the sample) paṭilomapuggalo / paṭilomaokāso / paṭilomapuggalokāsā = विपरीत: व्यक्ति / विपरीत: स्थान / विपरीत: व्यक्ति और स्थान; Puggalavāro = व्यक्ति का खंड; Dhammavāro = परिघटना का खंड; Puggaladhammavāro = व्यक्ति और परिघटना का खंड; Pariññāvāro = पूरी तरह समझने का खंड; Pajahanavāro = छोड़ने का खंड; Pahīnavāro = छोड़ा जा चुका होने का खंड; Bhāvanāvāro = अभ्यास का खंड

## 3. Closing lines and short answers
- Mūlavārauddeso. = मूल के खंड की सूची।; Mūlavāraniddeso. = मूल के खंड की व्याख्या।
- Uddesavāro niṭṭhito. = सूची का खंड पूरा हुआ।; Niddesavāro niṭṭhito. = व्याख्या का खंड पूरा हुआ।
- Paṇṇattiuddesavāro. = शब्दावली की सूची का खंड।; Paṇṇattiniddesavāro. = शब्दावली की व्याख्या का खंड।
- (not yet in the sample) Uppādavāro niṭṭhito. = उत्पन्न होने का खंड पूरा हुआ।; Nirodhavāro. = समाप्त होने का खंड।; Uppādanirodhavāro. = उत्पन्न होने और समाप्त होने का खंड।; Pavattivāro niṭṭhito. = प्रक्रिया का खंड पूरा हुआ।; Pariññāvāro. = पूरी तरह समझने का खंड।
- Āmantā. = हाँ।
- (not yet in the sample) No. = नहीं।; Natthi. = ऐसा कोई नहीं है।
- Short process answers agree with the subject of the question's second clause: Uppajjati. = उत्पन्न होता है। (sample); (not yet in the sample) Uppajjittha. = उत्पन्न हुआ था।; Uppajjissati. = उत्पन्न होगा।; Nirujjhati. = समाप्त होता है।; Nirujjhittha. = समाप्त हुआ था।; feminine / plural subjects: see §9.

## 4. Mūlayamaka: questions
<T> = kusala हितकर, akusala हानिकर, abyākata नैतिक रूप से अनिर्धारित, nāma मानसिक पक्ष.
<T>ā dhammā = हितकर / हानिकर / नैतिक रूप से अनिर्धारित / मानसिक पक्ष की परिघटनाएँ. Predicate "sabbe te dhammā <T>ā" = वे सब परिघटनाएँ हितकर / हानिकर / नैतिक रूप से अनिर्धारित / मानसिक पक्ष की हैं.
<R> (the root, plural or oblique) = हितकर मूल, हानिकर मूल, नैतिक रूप से अनिर्धारित मूल, मानसिक पक्ष के मूल.
- (Ka) ye keci <T>ā dhammā, sabbe te <P>? = (क) जो भी <T> परिघटनाएँ हैं, क्या वे सब <P> हैं?
- (Ka) ye keci <P1> dhammā, sabbe te <P2>? = (क) जो भी <P1> परिघटनाएँ हैं, क्या वे सब <P2> हैं?
- (Kha) ye vā pana <P>, sabbe te dhammā <T>ā? = (ख) और जो <P> हैं, क्या वे सब परिघटनाएँ <T> हैं?
- Example: (क) जो भी हितकर मूल के साथ एक ही मूल वाली परिघटनाएँ हैं, क्या वे सब हितकर मूल के साथ परस्पर मूल वाली हैं?

Root predicates <P> (agreement: f = परिघटनाएँ «वाली»; m = neuter singular subject «वाला»; mpl = the roots «वाले»; «पर आधारित» does not inflect):
- <T>mūlā = <R>; <T>mūlamūlā = <R> के मूल; <T>mūlakā = <R> पर आधारित; <T>mūlamūlakā = <R> के मूल पर आधारित
- <T>mūlena ekamūlā = <R> के साथ एक ही मूल वाली; …ekamūlamūlā = <R> के साथ एक ही मूल के मूल वाली; …ekamūlakā = <R> के साथ एक ही मूल पर आधारित; …ekamūlamūlakā = <R> के साथ एक ही मूल के मूल पर आधारित
- <T>mūlena aññamaññamūlā / …mūlamūlā / …mūlakā / …mūlamūlakā = <R> के साथ परस्पर मूल वाली / परस्पर मूल के मूल वाली / परस्पर मूल पर आधारित / परस्पर मूल के मूल पर आधारित
- bare ekamūlāni / aññamaññamūlāni (the roots, no <T>mūlena) = एक ही मूल वाले / परस्पर मूल वाले (likewise …मूल के मूल वाले, …मूल पर आधारित)

## 5. Mūlayamaka: answers
- Tīṇeva <T>mūlāni. = <R> तीन ही हैं।; Tīṇeva <T>mūlamūlāni. = <R> के मूल तीन ही हैं।; Naveva nāmamūlāni. = मानसिक पक्ष के मूल नौ ही हैं।
- Avasesā <T>ā dhammā na <P>. = शेष <T> परिघटनाएँ <P> नहीं हैं। (शेष हितकर परिघटनाएँ हितकर मूल नहीं हैं।)
- <T>samuṭṭhānaṃ rūpaṃ <P>, na <T>aṃ. = <T> से उत्पन्न भौतिक रूप, <P m> है, पर <T> नहीं है। (हितकर से उत्पन्न भौतिक रूप, हितकर मूल के साथ एक ही मूल वाला है, पर हितकर नहीं है।)
- <T>aṃ <P>ñceva <T>añca. = <T>, <P m> भी है और <T> भी। (हितकर, हितकर मूल पर आधारित भी है और हितकर भी।)
- Mūlāni yāni ekato uppajjanti <T>mūlāni <X>āni ceva <Y>āni ca. = जो मूल एक साथ उत्पन्न होते हैं, वे <R> <X mpl> भी हैं और <Y mpl> भी।
- Avasesā <T>mūlasahajātā dhammā <T>mūlena <X>ā, na ca <Y>ā. = <R> के साथ उत्पन्न शेष परिघटनाएँ, <R> के साथ <X f> हैं, पर <Y f> नहीं हैं।
- Ahetukaṃ <T>aṃ [<T>mūlena] na <P>. = मूल से रहित <T>, <P m> नहीं है।; Sahetukaṃ <T>aṃ [<T>mūlena] <P>. = मूल वाला <T>, <P m> है।

## 6. The ten names of a root (Hetuvārādi)
- mūla मूल, hetu हेतु (only here; elsewhere a root is मूल), nidāna स्रोत, sambhava उद्भव, pabhava उद्गम, samuṭṭhāna उत्पादक, āhāra आहार, ārammaṇa विषय, paccaya कारण, samudaya उत्पत्ति. With <T>: हितकर हेतु, हितकर स्रोत …; with nāma: मानसिक पक्ष के हेतु … मानसिक पक्ष की उत्पत्ति.
- Mūlaṃ hetu nidānañca, sambhavo pabhavena ca; = मूल, हेतु और स्रोत, उद्भव और उद्गम;
- Samuṭṭhānāhārārammaṇā, paccayo samudayena cāti. = उत्पादक, आहार और विषय, कारण और उत्पत्ति।
- Ye keci kusalā dhammā, sabbe te kusalahetū…pe… kusalanidānā…pe… … kusalasamudayā…pe…. = जो भी हितकर परिघटनाएँ हैं, क्या वे सब हितकर हेतु हैं… हितकर स्रोत… … हितकर उत्पत्ति…?
- Tayo eva kusalahetū, avasesā kusalā dhammā na kusalahetū…pe… kusalanidānā… = हितकर हेतु तीन ही हैं, शेष हितकर परिघटनाएँ हितकर हेतु नहीं हैं… हितकर स्रोत… …।
- Ye keci akusalā dhammā… ye keci abyākatā dhammā… = जो भी हानिकर परिघटनाएँ हैं… जो भी नैतिक रूप से अनिर्धारित परिघटनाएँ हैं…

## 7. Paṇṇattivāra (term-checking pairs)
Bare words stay bare; the aggregate names take the full term:
- rūpaṃ रूप (oblique रूप); vedanā अनुभूति; saññā पहचान; saṅkhārā रचनाएँ (plural; oblique रचनाओं); viññāṇaṃ चेतना; khandho समूह; khandhā समूह (plural; oblique समूहों)
- rūpakkhandho भौतिक रूप का समूह (oblique भौतिक रूप के समूह); vedanākkhandho अनुभूति का समूह; saññākkhandho पहचान का समूह; saṅkhārakkhandho मानसिक रचनाओं का समूह; viññāṇakkhandho चेतना का समूह
- Pañcakkhandhā – rūpakkhandho, vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho. = पाँच समूह – भौतिक रूप का समूह, अनुभूति का समूह, पहचान का समूह, मानसिक रचनाओं का समूह, चेतना का समूह।
- Piyarūpaṃ sātarūpaṃ = प्रिय और सुहावना लगने वाला रूप; Diṭṭhisaññā = दृष्टि के अर्थ में पहचान
- (not yet in the sample, from the termbase) cakkhu आँख / cakkhāyatanaṃ आँख का इंद्रिय-क्षेत्र; sotaṃ कान; raso स्वाद; cakkhundriyaṃ आँख की क्षमता; Dibbasotaṃ taṇhāsotaṃ … = दिव्य कान और तृष्णा की धारा, कान हैं (harmonise I2)

Questions (copula: plural if either side is plural, so «रचनाएँ» takes «हैं»):
- (Ka) X Y? = (क) क्या X, Y है? (क्या रूप, भौतिक रूप का समूह है? / क्या रचनाएँ, मानसिक रचनाओं का समूह हैं? / क्या मानसिक रचनाओं का समूह, रचनाएँ हैं? / क्या समूह, अनुभूति का समूह हैं?)
- (Ka) na X na Y? = (क) जो X नहीं है, क्या वह Y नहीं है? (plural X: जो रचनाएँ नहीं हैं, क्या वे … नहीं हैं? / जो समूह नहीं हैं, क्या वे … नहीं हैं?; plural Y only: जो मानसिक रचनाओं का समूह नहीं है, क्या वह रचनाएँ नहीं हैं?)
Answers:
- A B, na C. = A, B है, पर C नहीं है। (प्रिय और सुहावना लगने वाला रूप, रूप है, पर भौतिक रूप का समूह नहीं है।)
- C B ceva C ca. = C, B भी है और C भी। (भौतिक रूप का समूह, रूप भी है और भौतिक रूप का समूह भी। / अनुभूति का समूह, समूह भी है और अनुभूति का समूह भी। / plural B: मानसिक रचनाओं का समूह, रचनाएँ भी हैं और मानसिक रचनाओं का समूह भी।)
- A na C, B. = A, C नहीं है, पर B है। (plural A: … नहीं हैं, पर B हैं।)
- X ṭhapetvā avasesā [khandhā] = X को छोड़कर शेष[ समूह], always followed by a comma: मानसिक रचनाओं के समूह को छोड़कर शेष, रचनाएँ हैं, पर मानसिक रचनाओं का समूह नहीं हैं। / मानसिक रचनाओं के समूह को छोड़कर शेष, मानसिक रचनाओं का समूह नहीं हैं, पर रचनाएँ हैं। / रूप को छोड़कर शेष समूह, रूप नहीं हैं, पर समूह हैं।
- Bañca Cañca ṭhapetvā avasesā na ceva B na ca C. = B और C को छोड़कर शेष न तो B हैं, न C। (both oblique before को: रूप और भौतिक रूप के समूह को …; रचनाओं और मानसिक रचनाओं के समूह को …; रूप और समूहों को छोड़कर शेष न तो रूप हैं, न समूह।)
- Avasesā khandhā na C. = शेष समूह, C नहीं हैं।
- Variants of ^6-2-26 / ^6-2-28: «शेष, रचनाएँ हैं [पाठभेद (Syā.): avasesā saṅkhārā saṅkhārā], पर …»; «शेष समूह [पाठभेद (Syā.): avasesā khandhā khandhā; आगे भी इसी प्रकार], अनुभूति का समूह नहीं हैं।»

## 8. Pavattivāra: questions and answers (any tense, any verb)
Questions (V1, V2 from §9, positive or negative, each in its own tense):
- (Ka) yassa X V1 tassa Y V2ti? = (क) जिस व्यक्ति में X V1, क्या उसमें Y V2?
- (Kha) yassa vā pana Y V1 tassa X V2ti? = (ख) और जिस व्यक्ति में Y V1, क्या उसमें X V2?
- (Ka) yattha X V1 tattha Y V2ti? = (क) जिस स्थान पर X V1, क्या वहाँ Y V2?; (Kha) yattha vā pana … = (ख) और जिस स्थान पर …, क्या वहाँ …?
- (Ka) yassa yattha X V1 tassa tattha Y V2ti? = (क) जिस व्यक्ति में जिस स्थान पर X V1, क्या उसमें वहाँ Y V2?; (Kha) yassa vā pana yattha … = (ख) और जिस व्यक्ति में जिस स्थान पर …, क्या उसमें वहाँ …?
- Sample: (क) जिस व्यक्ति में भौतिक रूप का समूह उत्पन्न नहीं होता, क्या उसमें अनुभूति का समूह उत्पन्न नहीं होता?
- (not yet in the sample) mixed tense: (क) जिस व्यक्ति में भौतिक रूप का समूह उत्पन्न होता है, क्या उसमें अनुभूति का समूह उत्पन्न हुआ था?; uppāda + nirodha: (क) जिस व्यक्ति में भौतिक रूप का समूह उत्पन्न होता है, क्या उसमें अनुभूति का समूह समाप्त होता है? नहीं।
- (not yet in the sample) abbreviated: Yattha X V…pe…. = जिस स्थान पर X V…। (जिस स्थान पर भौतिक रूप का समूह उत्पन्न हुआ था…।)
Answers ("no ca … V" is always rendered by flipping the polarity of V, in V's own tense):
- <beings> tesaṃ X V1, no ca tesaṃ Y V2. = <beings> X V1, पर उनमें Y <V2 flipped>।
- <beings> tesaṃ X ca V1 Y ca V2. = <beings> X भी V1 और Y भी V2।
- <beings> tesaṃ tattha … = <beings> वहाँ X V1, पर उनमें वहाँ Y <V2 flipped>। / <beings> वहाँ X भी V1 और Y भी V2।
- <place> tattha X V1, no ca tattha Y V2. = <place> X V1, पर वहाँ Y <V2 flipped>। (the first tattha is not translated; the place already has «में»)
- <place> tattha X ca V1 Y ca V2. = <place> X भी V1 और Y भी V2।
- Sample: पहचान-रहित प्राणियों के लोक में जन्म लेने वालों में भौतिक रूप का समूह उत्पन्न होता है, पर उनमें अनुभूति का समूह उत्पन्न नहीं होता। / अभौतिक लोक में जन्म लेने वालों में भौतिक रूप का समूह उत्पन्न नहीं होता, पर उनमें अनुभूति का समूह उत्पन्न होता है। / सभी मरने वालों में वहाँ भौतिक रूप का समूह भी उत्पन्न नहीं होता और अनुभूति का समूह भी उत्पन्न नहीं होता।
- (not yet in the sample) mixed tense: सभी मरने वालों में और अभौतिक लोक में जन्म लेने वालों में अनुभूति का समूह उत्पन्न हुआ था, पर उनमें भौतिक रूप का समूह उत्पन्न नहीं होता।

## 9. Process verbs (copy exactly)
| Pāli | masculine sg (समूह, इंद्रिय-क्षेत्र, तत्व, सत्य, मन) | feminine sg (क्षमता, सुप्त प्रवृत्ति) | plural (masc.) |
|---|---|---|---|
| uppajjati / nuppajjati | उत्पन्न होता है / उत्पन्न नहीं होता | उत्पन्न होती है / उत्पन्न नहीं होती | उत्पन्न होते हैं / उत्पन्न नहीं होते |
| uppajjittha / nuppajjittha | उत्पन्न हुआ था / उत्पन्न नहीं हुआ था | उत्पन्न हुई थी / उत्पन्न नहीं हुई थी | उत्पन्न हुए थे / उत्पन्न नहीं हुए थे |
| uppajjissati / nuppajjissati | उत्पन्न होगा / उत्पन्न नहीं होगा | उत्पन्न होगी / उत्पन्न नहीं होगी | उत्पन्न होंगे / उत्पन्न नहीं होंगे |
| nirujjhati / na nirujjhati | समाप्त होता है / समाप्त नहीं होता | समाप्त होती है / समाप्त नहीं होती | समाप्त होते हैं / समाप्त नहीं होते |
| nirujjhittha / na nirujjhittha | समाप्त हुआ था / समाप्त नहीं हुआ था | समाप्त हुई थी / समाप्त नहीं हुई थी | समाप्त हुए थे / समाप्त नहीं हुए थे |
| nirujjhissati / na nirujjhissati | समाप्त होगा / समाप्त नहीं होगा | समाप्त होगी / समाप्त नहीं होगी | समाप्त होंगे / समाप्त नहीं होंगे |
Only the masculine present uppajjati / nuppajjati is in the sample; the rest is (not yet in the sample).
(not yet in the sample) Participles: uppajjamāna उत्पन्न होता हुआ; uppanna उत्पन्न हो चुका; nirujjhamāna समाप्त होता हुआ; niruddha समाप्त हो चुका. Anusaya (fem. सुप्त प्रवृत्ति): anuseti = सोई रहती है, nānuseti = सोई नहीं रहती (termbase सोया रहना, inflected); pahīna = छोड़ा जा चुका; appahīna = छोड़ा नहीं गया (termbase; the zeroshot «छोड़ा न गया» is superseded); pajahati = छोड़ता है; bhāveti = अभ्यास करता है; sacchikaroti = साक्षात्कार करता है.

## 10. Beings, places, moments
Every chunk ends in «में»; the chunks of a chain are joined «A में, B में और C में» (harmonise B8, B9).
- Places (oblique) + postposition: «में» for the accusative of rebirth and the locative, «से» for the ablative of dying:
  asaññasatta = पहचान-रहित प्राणियों के लोक; pañcavokāra = पाँच समूहों वाले अस्तित्व; catuvokāra = चार समूहों वाले अस्तित्व; catuvokāraṃ pañcavokāraṃ / catuvokārā pañcavokārā = चार या पाँच समूहों वाले अस्तित्व (one chunk, «या», harmonise I3); ekavokāra = एक समूह वाले अस्तित्व; arūpa / arūpāvacara = अभौतिक लोक; suddhāvāsa = शुद्ध निवास लोक; kāmāvacara = इंद्रिय-सुखों के लोक; rūpāvacara = सूक्ष्म भौतिक लोक; apāya = दुर्गति के लोक
- <place-acc> upapajjantānaṃ = <place> में जन्म लेने वालों में (sample: Asaññasattaṃ / Pañcavokāraṃ / Arūpaṃ upapajjantānaṃ)
- Sabbesaṃ cavantānaṃ = सभी मरने वालों में (sample); Sabbesaṃ upapajjantānaṃ = सभी जन्म लेने वालों में (not yet in the sample)
- Okāsa answers: Asaññasatte = पहचान-रहित प्राणियों के लोक में; Pañcavokāre = पाँच समूहों वाले अस्तित्व में; Arūpe = अभौतिक लोक में (sample)
- (not yet in the sample) <place-abl> cavantānaṃ = <place> से मरने वालों में (B1: पाँच समूहों वाले अस्तित्व से मरने वालों में); <place-loc> parinibbantānaṃ = <place> में पूर्ण निर्वाण पाने वालों में; Parinibbantānaṃ = पूर्ण निर्वाण पाने वालों में
- (not yet in the sample) genitive beings: Asaññasattānaṃ = पहचान-रहित प्राणियों में; Pañcavokārānaṃ = पाँच समूहों वाले अस्तित्व के प्राणियों में; Arūpānaṃ = अभौतिक लोक के प्राणियों में; Suddhāvāsānaṃ = शुद्ध निवास लोक के प्राणियों में; kāmāvacarānaṃ / rūpāvacarānaṃ / arūpāvacarānaṃ = इंद्रिय-सुखों के लोक / सूक्ष्म भौतिक लोक / अभौतिक लोक के प्राणियों में (B7: «… के प्राणियों में और … के प्राणियों में»)
- (not yet in the sample) Pacchimabhavikānaṃ = अंतिम जन्म वालों में; Pacchimabhavikānaṃ [X] upapajjantānaṃ = [X में] अंतिम जन्म लेने वालों में (one chunk, B2); <loc> pacchimabhavikānaṃ = <place> में अंतिम जन्म वालों में
- (not yet in the sample) Itaresaṃ (alone) = बाकी सबमें; Itaresaṃ <chunk> = बाकी <chunk>
- (not yet in the sample) Ye X upapajjitvā parinibbāyissanti tesaṃ = जो X में जन्म लेकर पूर्ण निर्वाण पाएँगे, उनमें; … ye ca X upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ / upapajjantānaṃ = … और जो X में जन्म लेकर पूर्ण निर्वाण पाएँगे, उनमें से मरने / जन्म लेने वालों में (B3)
- (not yet in the sample) women: itthīnaṃ upapajjantīnaṃ / cavantīnaṃ = जन्म लेने / मरने वाली स्त्रियों में; purisānaṃ = पुरुषों में
- (not yet in the sample) moments (termbase): pavatte = जीवन के दौरान; cittassa uppādakkhaṇe / bhaṅgakkhaṇe = मन के उत्पन्न होने / भंग होने के क्षण में; upapatticittassa uppādakkhaṇe = जन्म के मन के उत्पन्न होने के क्षण में; sabbesaṃ cittassa … = सभी के मन के … होने के क्षण में (B5); anantarā = ठीक बाद (B6: जिनमें इस मन के ठीक बाद X उत्पन्न होगा, उनमें); nirodhasamāpannānaṃ = समाप्ति की ध्यान-अवस्था में लीन लोगों में

## 11. Pariññā / pajahana / bhāvanā (not yet in the sample; harmonise B10)
- (Ka) yo X parijānāti so Y parijānātīti? = (क) जो व्यक्ति X को पूरी तरह समझता है, क्या वह Y को पूरी तरह समझता है?
- past: (Ka) yo X parijānittha so Y parijānitthāti? = (क) जिस व्यक्ति ने X को पूरी तरह समझा था, क्या उसने Y को पूरी तरह समझा था?
- future: … पूरी तरह समझेगा, क्या वह … पूरी तरह समझेगा?; negative: पूरी तरह नहीं समझता / नहीं समझा था / नहीं समझेगा
- mixed: the relative follows the first verb, the correlative the second: (क) जो व्यक्ति भौतिक रूप के समूह को पूरी तरह समझता है, क्या उसने अनुभूति के समूह को पूरी तरह समझा था?
- answer shape: Arahā X na parijānāti, no ca Y na parijānittha. = अर्हत् X को पूरी तरह नहीं समझता, पर उसने Y को पूरी तरह समझा था। (aggamaggasamaṅgī = सर्वोच्च मार्ग से युक्त व्यक्ति; puthujjanā = साधारण व्यक्ति; maggaṃ paṭilabhissanti = मार्ग प्राप्त करेंगे)

## 12. Abbreviation notes (not yet in the sample; harmonise N-notes)
yassakaṃ / yatthakaṃ / yassayatthakaṃ = व्यक्ति वाला भाग / स्थान वाला भाग / व्यक्ति और स्थान वाला भाग; …sadisaṃ = … के समान; vitthāretabbaṃ = … का (इसी प्रकार) विस्तार करना चाहिए; vibhajitabbaṃ / vibhattaṃ = … का विभाजन करना चाहिए / किया गया है; cakkaṃ bandhitabbaṃ = चक्र पूरा करना चाहिए; saṃkhittaṃ (of the text) = संक्षिप्त किया गया है; anulomampi paccanīkampi = सकारात्मक भी और नकारात्मक भी; asammohantena = बिना भ्रम के.
