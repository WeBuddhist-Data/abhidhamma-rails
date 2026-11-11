# pi-1 Hindi zero-shot: consistency pass (harmonise_hi.py), notes

Scripts: find_divergences_hi.py (divergences.md = before, `--bak`; divergences-after.md = after), harmonise_hi.py (reads backup-pre-harmonise/, so a rerun gives the same output; `--dry`), log harmonise-log.tsv. Helpers: hz_common.py, hz_kwic.py, hz_show.py, hz_where.py, hz_items.py, hz_lobha.py.
Protected: preamble, 1-matika, first 122 non-empty lines of 2-01 (the sample is its first 63 non-empty lines); no rule touched them.
Before: 12 segment / 12 line / 26 clause groups with identical Pāli and differing Hindi. After: 0 / 0 / 0. The 13 remaining (a4) item groups are comma-split misalignments (different Pāli items at the same position, e.g. the source's missing comma «jivhindriyaṃ kāyindriyaṃ» at ^1-591), not divergences.

## Choices
- D4 paṭipadā / adhipati: the 2-03 / 2-05 shape everywhere («जो ध्यान दुःखद प्रगति और धीमे / शीघ्र उच्च ज्ञान वाला है», «जो चाह की प्रधानता वाला है»). Reason: in the longest lines (2-05: paṭipadā + suññata / animitta / appaṇihita + adhipati) one relative clause with coordinated attributes («… वाला, शून्य और चाह की प्रधानता वाला है») reads well; the 2-01 shape («… के साथ, शून्य, जिसमें चाह प्रधान है») does not. Only 2-02 changed (50 + 8 lines). Adjacent items (…pe…) share one «जो ध्यान … है», as in 2-03; in the kasiṇa and paritta runs each item keeps its own clause («जो ध्यान … वाला है, जो सीमित है और सीमित विषय वाला है…»).
- D7 sārāga beside rāga = प्रबल राग (4-02). Reason: गहरा marks the pa-/sam- intensifiers in the same strings (padoso गहरा द्वेष, paligedho गहरी लालसा, sammoho गहरा मोह); प्रबल keeps sārāga distinct.
- D5 bhūmi: also X-bhūmiyaṃ in 4-01 (भूमि में → स्तर पर, gender of the qualifier fixed). Left: 2-03 / 2-05 «paṭhamāya bhūmiyā pattiyā» = «पहले चरण की प्राप्ति» (stage of the path, not a plane); heading Tebhūmaka (2-02).
- Rule 8 (4-01 vs 4-02/4-03, 4-01 kept unless the other form matches pi-3/4/5 or the terms file / matrix and 4-01's does not):
  - 4-02 → 4-01: sphere lists without repeated «हों»; Tehi dhammehi frames («उन परिघटनाओं से जो परिघटनाएँ जुड़ी / अलग हैं, यानी …», «उन परिघटनाओं के संबंध में जो परिघटनाएँ X का विषय बनती हैं, उनमें से उन्हीं परिघटनाओं को छोड़कर शेष, …»); tadekaṭṭha «और उनके साथ रहने वाले»; taṃsamuṭṭhāna «शारीरिक कर्म … मानसिक कर्म» (pi-5); taṃsampayutto «उनसे जुड़ा»; kiriyā clause; sāsavā … vipākā word order; «… से जुड़ी भी» without closing «है»; lobha, dosa, moha intro, kaṅkhā + Satthari intro, kāma, māna, sakkāyadiṭṭhi body; diṭṭhi string paṭiggāho / patiṭṭhāho = कसकर पकड़ना (pi-4 ^4-62; patiṭṭhāho treated as 4-01 / 2-04 do).
  - 4-01 → 4-02: avasesa = शेष (pi-4/5); nandī = आनंद, nandīrāga = आनंद और राग, kāmanandī / bhavanandī = … का आनंद (pi-5 nandī); upakkilesa = मलिनता (pi-5); ānantarika = «अगले ही जन्म में निश्चित फल देने वाले पाँच कर्म» (pi-4); the «Yo S – ayaṃ vuccati X» frame «जो S है – इसे X कहा जाता है» (terms file 3a / sample) instead of JO() «जो <first> है, <rest> –».
  - sīlabbata = सदाचार और व्रत (4-01): its parts match the terms file (sīla = सदाचार, parāmāsa = ग़लत धारणा); applied to sīlabbataparāmāsa (4-02, ch5) and sīlabbatupādāna (4-02, ch5 → «सदाचार और व्रतों के प्रति आसक्ति»), and the body «sīlena suddhi» (4-02 had कर्मकांड).
- Other parts (terms / sample, then earlier book, then more occurrences):
  - ch5 → ch4: diṭṭhāsava / diṭṭhisaṃyojana / kilesa diṭṭhi = दृष्टि (terms file), upādāna list «… के प्रति आसक्ति» (diṭṭhupādāna = दृष्टियों के प्रति आसक्ति), thina = आलस्य (pi-4, 4-02 majority), kabaḷīkāro āhāro = भोजन, «वे ही X, X रूपी भी» with comma, sekkhā line (4-01, keeps the Pāli comma).
  - 4-01 → ch5: asekkhā «सबसे ऊँचा फल, अर्हत्-पद का फल» (tie; no added «यानी»).
  - 4-02 → ch5: «Cittaṃ na vattabbaṃ» = «मन को कहा नहीं जा सकता – न …, न …» (ch5's frame for every na vattabbā).
  - kammassa katattā = «कर्म किए जाने के कारण (है / नहीं है)» (pi-5 katattā; 4-01 and ch5) in 3-02, 3-03, 4-02 (was «किए गए कर्म के कारण»); 4-01's «बना है» dropped.
  - rūpassa upacayo = वृद्धि (ch3; ācaya = संचय in the matrix) in ch5; rūpassa santati = धारा (ch3, ch5, pi-5) in 4-02.
  - kaṅkhā string: 4-01 items in 2-04 and 4-02; dveḷhaka spelled दुचित्तापन (2-04) rather than 4-01 दोचित्तापन.
- 4-01 ellipsis spacing «X … Y» → «X… Y» where the Pāli has «X…pe… Y» (80 places).

## Builder constants that would need the same change (if a part is ever rebuilt)
- build_2-01_2-02_hi.py: H_APPAMANANI (l. 523/527) → H_APPAMANANI_ALT; paṭipadā strings (l. 366/368) and adhipati strings (l. 428–431).
- build_2-03_hi.py TWENTY[2] (l. 250), build_2-05_hi.py (l. 176): सही परिश्रम.
- build_2-04_hi.py l. 119: kaṅkhā string tail.
- build_3-02_3-03_hi.py l. 245/246/251, build_4-02_4-03_hi.py l. 491: kammassa katattā.
- build_4-01_hi.py: JO() (l. 133), LOBHA (l. 199: गहरा राग, रस लेना, दूषण), kāma/bhava strings (l. 263/265), दोचित्तापन (l. 190), bhūmi frames (l. 332, 365–367), avasesa बाकी (l. 103, 274, 390, 400), बना है (l. 113), asekkhā (l. 407), ānantarika (l. 417), siglum (l. 429).
- build_4-02_4-03_hi.py: frames (l. 145/147 tadekaṭṭha + kamma, 173/178 Tehi, 576 उससे, 385 जुड़ी भी है), sphere lists, sīlabbata (l. 352/362), dosa (l. 211/759), kāma (l. 205/208), kaṅkhā (l. 245), moha (l. 250), diṭṭhi string अड़ जाना (l. 273), sakkāya (l. 295/296), lobha (l. 321 …), māna (l. 331), viññatti (l. 469), vattabba (l. 464/467), santati (l. 475), kiriyā (l. 492).
- build_5_hi.py: K4/V4 bhūmi (l. 90/93, 359/361), diṭṭhāsava etc. (l. 405/407), sīlabbata (l. 424/429), thina (l. 473/477, 570/574), viññatti (l. 508), upacaya (l. 524), āhāra (l. 525/541), sekkhā (l. 288), upādāna list.

## For the user's eye
- nandī = आनंद now also stands for pāmojja = आनंद in the approved sample's pīti string (rule 8 followed pi-5; 4-01 had avoided this with «रस लेना»).
- sīlabbata = «सदाचार और व्रत» departs from pi-5 «कर्मकांड और व्रत».
- ch5 kilesa line now reads «दृष्टि ग़लत दृष्टि से जुड़ी मन की चार उत्पत्तियों में उत्पन्न होती है» (diṭṭhi = दृष्टि, diṭṭhigata = ग़लत दृष्टि).
- 2-02 paritta runs: «जो ध्यान … उच्च ज्ञान वाला है, जो सीमित है और सीमित विषय वाला है…» is correct but heavy.
- परिश्रम is unused elsewhere in pi-1; pi-4 uses it for uṭṭhāna.
