# pi-2 Hindi zero-shot: consistency (harmonise) pass

Scripts: find_divergences_hi.py (report: divergences.md = before, `--bak`; divergences-after.md = after), harmonise_hi.py
(rules, reads backup-pre-harmonise/, writes the 19 chapter files, log: harmonise-log.tsv), helpers hz_*.py
(hz_pp_units.py = Pañhāpucchaka predicate survey, pp-units*.md). The pass edits the outputs; the builders were NOT rerun.
A rebuild would drop the pass unless the builder constants listed below get the same change.

## Decisions (brief step 2)

1. Suttanta definitions (ch4 ^2-191 ff. = ch6 ^2-235 ff.). No pi-1/3/4/5 source except jarā (pi-1 ^1-643, already equal) and an
   equal number of occurrences, so per string: frame from ch4 (singular «उस-उस प्राणी-वर्ग में/से» as the Pāli tamhi tamhi
   sattanikāye; byasana phrase repeats «… से पीड़ित» for each phuṭṭhassa, «… व्यक्ति का जो»); the synonym lists from ch6
   (pi-1 conventions: -itattaṃ = «… से भरा होना», -tā = «… की अवस्था», maraṇaṃ in its own list = मृत्यु): jāti «गर्भ में उतरना»,
   maraṇa, soka «शोक से भरा होना», parideva, upāyāsa «हताशा, निराशा, हताशा से भरा होना, निराशा से भरा होना».
   appiyehi / piyehi / yampicchaṃ occur only in ch4 (unchanged); the compound list was already equal.
2. dukkhanirodhagāminī paṭipadā = «दुःख के अंत की ओर ले जाने वाला प्रगति का ढंग» (oblique «… वाले प्रगति के ढंग»): pi-1 rails
   (4-01/4-02 amoha and moha lists) wins over pi-5 «… मार्ग»; ch6, ch11, ch15, ch17 already had it; ch4 (incl. the Noble Truth
   name) and ch16 changed. magga itself (maggasacca, aṭṭhaṅgiko maggo) stays मार्ग.
3. Pañhāpucchaka frames (one shape per frame, agreement by the subject noun):
   - question: «… में से कितने X हैं, कितने Y हैं, … कितने संघर्ष से रहित हैं?» (ch1–5, 7, 10, 11, 14, 15).
   - no added subject on subjectless sentences (Pāli has none; ch8, 9, 12, 13): «ये …» (ch7, 10, 11), «वे …» (ch14, 15),
     «सभी क्षमताएँ …» (ch5), «पाँचों समूह …» (ch1) and «वे» before the kenaci clause removed.
   - siyā: «कभी A होते हैं, कभी B होते हैं» with the verb on every member (pi-1 ^1-1406; ch9 had elided verbs).
   - negation: «<label> नहीं है/हैं», «कभी <label> नहीं होता/होते/होती/होतीं» (ch1, 3, 8, 12–15; pi-1 «… नहीं होतीं» for a
     noun-less negative), also for B-ceva-no-ca-A as predicate («B, पर स्वयं A रूपी नहीं हैं», ch3); na pahātabbahetukā =
     «… मूलों वाले नहीं» (not «मूलों से रहित»). Quoted labels, neither-nor labels («न कर्म-फल रूपी, न …»), «… न होने वाले और …»,
     «… न होने वाले, पर …» and a-labels with another verb («मुक्ति की ओर न ले जाने वाले», «विषय न बनने वाले») keep the matrix wording.
   - sahagata keeps its label: «कभी उल्लास के साथ होने वाले होते हैं / … होने वाले नहीं होते», bare «… होने वाले हैं / नहीं हैं»
     (ch2, 4, 5, 7, 9–11, 13 over ch1, 3, 8, 14, 15).
   - na vattabbā: object «उन्हें/उसे», the clause after it «वे/वह» (ch1–4, 8, 14, 15; pi-1 ^1-1427 «वे … उन्हें»).
   - kenaci viññeyyā, kenaci na viññeyyā = «… जाने जा सकने वाले भी हैं, … न जाने जा सकने वाले भी हैं» (pi-1 ^1-1464; ch1–4, 15).
   - anupādinnaanupādāniyā = «न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाले हैं» (ch8, ch9 changed).
4. niddesa = «… की व्याख्या» (pi-1 3-01 «एकल वर्गीकरण की व्याख्या», ch16, ch17); ch6, ch7 changed (agreement «शुरू होने वाली»).
5. Ekaka … Dasaka: the pi-1 Rūpakaṇḍa scheme (= ch16): «एकल वर्गीकरण», «दो-दो के वर्गीकरण» …, «… के वर्गीकरणों की मूल सूची»,
   «… के वर्गीकरणों की व्याख्या»; ch17 changed (40 lines).
6. upekkhā upekkhanā ajjhupekkhanā majjhattatā cittassa: not in pi-1 -> majority «समभाव, समभाव रखना, तटस्थ भाव से देखना, मन की
   तटस्थता» (ch10 4 lines, notes 5/7/10/11); ch12 changed.
7. akaniṭṭha = «अकनिष्ठ देवता» (pi-1 4-02); ch18 «सबसे ऊँचे» dropped (2 lines).
8. Others: samudaya-/maggasacca = «दुःख की उत्पत्ति का सत्य», «दुःख के अंत के मार्ग का सत्य» (pi-3, pi-4; = ch18; ch4 changed);
   Tena vuccati = «इसीलिए “X” कहा जाता है» (ch12/13 order, इसीलिए 108 of 129 lines); avasesā dhammā = «शेष परिघटनाएँ» (pi-1);
   iriyati string = ch12/13; ātāpī … = «उद्यमी, … लोक में …» (ch7, ch11); adinnādāna «बिना दी गई चीज़ लेने से» and kāmesumicchācāra
   «इंद्रिय-सुखों में दुराचार से» (pi-4 = ch14), pisuṇā/pharusā «चुगली करने से», «कठोर वचन बोलने से» (ch11, nearest pi-4);
   aṭṭhaṅgiko maggo = «आठ अंगों वाला (आर्य) मार्ग» (pi-1 2-03); metti/karuṇā «… करना» (pi-1 4-01); upādānakkhandha «आसक्ति का
   विषय बनने वाले» (ch4, pi-1 upādāniya); body parts = ch7; the four paṭisambhidā = ch15; yañca rūpaṃ … = ch2; upeto hoti …
   samannāgato = ch8 wording (samannāgata = युक्त, pi-5, ch10, ch16); chando chandikatā … = ch8; phassasampayuttaṃ «… जुड़ी है»;
   gloss frames: "X"ti <definition> = «“X”: …» (ch12/13, 109 lines) over «“X” का अर्थ है …» (ch9, ch16, 59);
   "X"ti. Tattha katamo …? = «“X”। यहाँ … क्या है?» (ch6–8, 39 lines; ch12/13 lines with the Pāli full stop changed).

## Left on purpose

- Agreement differences (the subject noun decides): all residual (a3) groups and most (a4) items; the rest of (a4) are
  alignment artefacts (lines whose item counts happen to match).
- ch12 "Catukkaṃ. / Pañcakaṃ." = «चार-चार / पाँच-पाँच की विधि।» (jhāna by the fourfold/fivefold method; pi-1 Catukkanayo), vs
  ch16/17 «चार-चार के वर्गीकरण» (groups of fours; pi-1 Rūpakaṇḍa): same word, different referent.
- seyyathidaṃ «जैसे –» before open examples (ch3, ch16) vs «यानी –» before a closed list (ch4, ch11).
- atthi X, atthi Y: «कुछ X है» for classes (terms file, ch1, 5) vs «X भी है, Y भी है» for components (ch6, 12, 13); no identical Pāli.
- "X"ti tattha … without a full stop (ch12/13) keeps «“X”: यहाँ …»; rūpadhātu realm vs element; pi-1 ^1-1389 «और उन्हें … भी नहीं
  कहा जा सकता» (ch18); source slips listed in the notes files, translated as written.
- notes-*.md were not edited (agent records); they still show the pre-pass renderings.

## Builder constants that would need the same change

- build_saccavibhango_hi.py (ch4): lines 81–94 (jāti, maraṇa, soka, parideva, upāyāsa), PATIPADA, PATIPADA_OBL, l.410, HEAD and
  l.29/l.409 (sacca names), SATI_TAIL, l.209/l.298 (aṭṭhaṅgika), l.213/l.215 (veramaṇī), QUESTION; matrix_ch2_ch4_hi.py (negation,
  sahagata, pronouns, kenaci).
- build_6-paticcasamuppadavibhango_hi.py: SATTANAM, l.285–286 (byasana), l.450–455 (niddesa), Tena vuccati strings.
- build_7-satipatthanavibhango_hi.py: l.249–271 (niddesa), VIHARATI_DEF, l.148/l.152 (upeto), FIVE_UPADANA, SP_JOINED;
  pp_5_7_10_11_hi.py (ch5, 7, 10, 11): AVASESA, ALL_FACULTIES, the «ये» subject, negation (l.189–231), pronouns (l.348), kenaci.
- build_10-bojjhangavibhango_hi.py: SAMPAYUTTA7; build_11-maggangavibhango_hi.py: l.75 (veramaṇī).
- build_8-sammappadhanavibhango_hi.py: QUESTION, «ये केवल हितकर», sahagata, ceva-compound, Tena vuccati.
- build_9_iddhipadavibhango_hi.py: l.124 (upeto), CHANDA_DEF, IDDHI_LINE/BHAVETI_LINE/IP_* (gloss), l.134/l.151 (Tena vuccati),
  the Pañhāpucchaka strings (l.185–247, l.311).
- build_12_13_hi.py: UPEKKHA_J, UPETA_FULL/UPETA_PE/UPETA_PE2, l.469 (upādānakkhandha), SAHAGATA_TAIL, the gloss «”:» before
  questions, l.762/l.993 (question), l.1004–1029 (pronouns, negation).
- build_3-dhatuvibhango_hi.py: METTA, l.63 (body parts), the ch2-style yañca rūpaṃ line; hz_3_14_15_common.py (ch3, 14, 15: «वे»
  subject, sahagata short form).
- build_1-khandhavibhango_hi.py: l.537/l.574 (sahagata), l.609–613 (question, «पाँचों समूह»), negation l.123–152 (PP part);
  build_ayatanavibhango_hi.py (ch2): QUESTION, l.152.
- build_5-indriyavibhango_hi.py: l.80 (phassasampayutta).
- build_16_nanavibhango_hi.py: PATIPADA and l.331/l.343 (paṭipadā), l.683/l.685 (paṭisambhidā), l.1004–1026 (gloss).
- khuddaka17_a.py / _b.py / _c.py (ch17 headings and closings, l.97–134 and the mātikā/niddesa lines).
- build_18-dhammahadayavibhango_hi.py: l.687 (akaniṭṭha), l.116–119/l.1025–1027 (questions).
