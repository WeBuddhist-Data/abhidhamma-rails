# Notes: pi-1 English plain zero-shot, parts 2-05 and 3-01

Builders: build_2-05.py (imports NAMES, STRINGS, S_*, Q/A from build_ch2_01_sample.py; translates each '…pe…' chunk by fixed rules, so the same Pāli chunk always gives the same English) and build_3-01.py (sentence patterns with fixed predicate strings). Extra checker: check_2-05_3-01.py.
Format: Pāli = English, one per line. '…pe…' = '…' attached to the preceding word.

## 2-05: frames (fixed constants; 2-01 / 2-04 may define these first, consistency pass to align)
Katame dhammā abyākatā? = What states are indeterminate?
ime dhammā abyākatā = these states are indeterminate
ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā – ime dhammā abyākatā = or whatever other dependently arisen immaterial states there are at that time – these states are indeterminate
Tasmiṃ kho pana samaye cattāro khandhā honti, dvāyatanāni honti, dve dhātuyo honti, tayo āhārā honti, tīṇindriyāni (pañcindriyāni) honti, eko phasso hoti = Now at that time there are four aggregates, there are two sense bases, there are two elements, there are three nutriments, there are three (five) faculties, there is one contact
ekā X-dhātu hoti, ekaṃ dhammāyatanaṃ hoti, ekā dhammadhātu hoti = there is one X element, there is one mental-object base, there is one mental-object element
Katamo tasmiṃ samaye saṅkhārakkhandho hoti? = What is the aggregate of mental formations at that time?
ye vā pana … arūpino dhammā ṭhapetvā vedanākkhandhaṃ ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ – ayaṃ tasmiṃ samaye saṅkhārakkhandho hoti = or whatever other dependently arisen immaterial states there are at that time, apart from the aggregate of feeling, apart from the aggregate of perception, apart from the aggregate of consciousness – this is the aggregate of mental formations at that time
Yā tesaṃ aññātāvīnaṃ dhammānaṃ S = Whatever, in those states of one who has final knowledge, is S
aññā (before the paññā string) = final knowledge
dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ = the awakening factor of investigation of states, a factor of the path, included in the path
kāyikaṃ asātaṃ kāyikaṃ dukkhaṃ kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ kāyasamphassajā asātā dukkhā vedanā = bodily discomfort, bodily pain, the uncomfortable, painful experience born of body-contact, the uncomfortable, painful feeling born of body-contact
tajjākāyaviññāṇadhātusamphassajaṃ = born of the contact of the corresponding body-consciousness element
samādhi string without sammāsamādhi / vīriya string without sammāvāyāmo (functional mind) = the sample strings with ", right concentration" / ", right effort" removed

## 2-05: world-transcending absorption
Yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ = At a time when one develops world-transcending absorption that leads to liberation and leads away from accumulation
diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā = for the abandoning of wrong views, for reaching the first stage
kāmarāgabyāpādānaṃ tanubhāvāya dutiyāya bhūmiyā pattiyā = for the weakening of sensual lust and ill will, for reaching the second stage
kāmarāgabyāpādānaṃ anavasesappahānāya tatiyāya bhūmiyā pattiyā = for the abandoning without remainder of sensual lust and ill will, for reaching the third stage
rūparāgaarūparāgamānauddhaccaavijjāya anavasesappahānāya catutthāya bhūmiyā pattiyā = for the abandoning without remainder of lust for the fine-material, lust for the immaterial, conceit, restlessness and ignorance, for reaching the fourth stage
vivicceva kāmehi = quite secluded from sensual pleasures (kusala clause: "…, and, quite secluded from sensual pleasures… enters and dwells in …")
vitakkavicārānaṃ vūpasamā = with the stilling of applied thought and sustained thought
X jhānaṃ upasampajja viharati = enters and dwells in the X absorption (paṭhamaṃ … pañcamaṃ = first … fifth)
Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ = Because that same world-transcending wholesome absorption has been done and developed, as its result one, (quite secluded …) [enters and dwells …]
dukkhapaṭipadaṃ dandhābhiññaṃ = with difficult practice and slow direct knowledge (khippābhiññaṃ = quick direct knowledge; sukhapaṭipadaṃ = with easy practice)
suññataṃ / animittaṃ / appaṇihitaṃ = empty / signless / desireless
chandādhipateyyaṃ / vīriyā- / cittā- / vīmaṃsādhipateyyaṃ = with desire / energy / mind / inquiry as the dominant factor (vīmaṃsā = inquiry, kept apart from vicaya = investigation)
…nti kusalaṃ / …nti vipāko = … (wholesome) / … (result)
aññindriyaṃ = the faculty of final knowledge; aññātāvindriyaṃ = the faculty of one who has final knowledge
lokuttaraṃ X bhāveti (twenty great methods) = develops the world-transcending path / a world-transcending foundation of mindfulness / right striving / basis of spiritual power / faculty / power / awakening factor / truth / calm / state / aggregate / sense base / element / nutriment / contact / feeling / perception / intention / mind
sammappadhāna = right striving (kept apart from sammāvāyāma = right effort)

## 2-05: results and functional minds
akusalassa kammassa katattā upacitattā vipākaṃ/vipākā X uppannaṃ hoti = because unwholesome action has been done and accumulated, X has arisen as its result
cakkhu-/sota-/ghāna-/jivhā-/kāyaviññāṇaṃ = eye-/ear-/nose-/tongue-/body-consciousness (hyphenated, like mind-consciousness element; notes-5 writes "eye consciousness")
dukkhasahagataṃ = accompanied by pain; dukkhaṃ (factor) = pain; dukkhindriyaṃ = the faculty of pain
upekkhā (factor) = equanimity; upekkhindriyaṃ = the faculty of equanimity
manodhātu = the mind element; dhammāyatana / dhammadhātu = the mental-object base / the mental-object element
kiriyā (kiriyaṃ) neva kusalā nākusalā na ca kammavipākā = functional, neither wholesome nor unwholesome nor a result of action
sasaṅkhārena = with prompting (… "accompanied by joy, associated with knowledge and with prompting")
abyākatamūlaṃ = the indeterminate root
rūpāvacaraṃ / arūpāvacaraṃ jhānaṃ bhāveti = one develops absorption of the fine-material / immaterial sphere
diṭṭhadhammasukhavihāraṃ = for a pleasant abiding here and now
pathavīkasiṇaṃ = using the earth meditation device
sabbaso rūpasaññānaṃ samatikkamā paṭighasaññānaṃ atthaṅgamā nānattasaññānaṃ amanasikārā = with the complete surmounting of perceptions of material form, with the disappearance of perceptions of impact, with non-attention to perceptions of diversity
sabbaso X samatikkamma = completely surmounting X
ākāsānañcāyatana / viññāṇañcāyatana / ākiñcaññāyatana / nevasaññānāsaññāyatana = the base of infinite space / of infinite consciousness / of nothingness / of neither perception nor non-perception (same as notes-5)
X-saññāsahagataṃ = accompanied by the perception of X
sukhassa ca pahānā = with the abandoning of happiness (sukha as a factor = happiness)

## 2-05: headings and closing lines
#### Lokuttaravipāka-paṭhamamaggavipākā = World-Transcending Results: The Results of the First Path
##### Suddhikapaṭipadā = The Simple Modes of Practice; ##### Suddhikasuññataṃ = Simple Emptiness; ##### Suññatapaṭipadā = Emptiness with the Modes of Practice; ##### Suddhikaappaṇihitaṃ = Simple Desirelessness; ##### Appaṇihitapaṭipadā = Desirelessness with the Modes of Practice; ##### Vīsati mahānayā = The Twenty Great Methods; ##### Chandādhipateyyasuddhikapaṭipadā = Desire as the Dominant Factor: The Simple Modes of Practice; ##### Chandādhipateyyasuddhikasuññatā = Desire as the Dominant Factor: Simple Emptiness (closing lines: same words, sentence case, final full stop)
Paṭhamamaggavipāko. = The result of the first path.
##### Dutiyādimaggavipāko = The Result of the Second and Later Paths
Lokuttaravipāko. = The world-transcending result.
#### Akusalavipākaabyākataṃ = Indeterminate Results of the Unwholesome
##### Akusalavipākapañcaviññāṇāni = The Five Kinds of Consciousness Resulting from the Unwholesome
##### Akusalavipākamanodhātu / -manoviññāṇadhātu = The Mind Element / The Mind-Consciousness Element Resulting from the Unwholesome
Vipākā abyākatā. = Indeterminate results.
#### Ahetukakiriyāabyākataṃ = Functional Indeterminate Minds without Roots; Ahetukā kiriyā abyākatā. = Functional indeterminate minds without roots.
##### Kiriyāmanodhātu = The Functional Mind Element
##### Kiriyāmanoviññāṇadhātusomanassasahagatā / -upekkhāsahagatā = The Functional Mind-Consciousness Element Accompanied by Joy / by Equanimity
##### Sahetukakāmāvacarakiriyā = Functional Minds of the Sense Sphere with Roots
##### Rūpāvacarakiriyā / Arūpāvacarakiriyā = Functional Minds of the Fine-Material Sphere / of the Immaterial Sphere
Kiriyā abyākatā. = Functional indeterminate minds.
Cittuppādakaṇḍaṃ niṭṭhitaṃ. = The chapter on the arising of mind is complete.

## 3-01
Uddeso ^1-583: kusalākusalānaṃ dhammānaṃ vipākā … = the results of wholesome and unwholesome states, of the sense sphere, …, and not included in the spheres of existence: …; kiriyā … kammavipākā (plural) = functional, neither wholesome nor unwholesome nor results of action; asaṅkhatā dhātu = the unconditioned element
Tattha = Among these
Cattāro ca mahābhūtā, catunnañca mahābhūtānaṃ upādāya rūpaṃ = The four great elements and the material form derived from the four great elements
idaṃ vuccati = this is called
X-vidhena rūpasaṅgaho – (opening line) = Material form classified in X ways –
Evaṃ X-vidhena rūpasaṅgaho. = Thus material form is classified in X ways. (as notes-3-02_3-03)
Atthi rūpaṃ X, atthi rūpaṃ Y. = There is material form that is X; there is material form that is Y. (verb items: that makes impact; arising from mind / existing together with mind / accompanying mind, matrix wording)
Yaṃ taṃ rūpaṃ A, taṃ X. = Material form that is A is X.
Yaṃ taṃ rūpaṃ A, taṃ atthi X, atthi Y. = Of material form that is A, some is X and some is Y.
Predicates: identical to notes-3-02_3-03.md (derived, produced by past action, … intimation, a basis for eye-contact, an object of eye-contact, the eye base, the faculty of the eye, lightness of material form …, edible food).
Ekaka (sabbaṃ rūpaṃ …, ^1-584): the matrix items in singular, "is …": is not a root, is without roots, …, has conditions, neither is a result nor produces results, leads neither to nor away from accumulation, does not lead to liberation; two items that cannot be made singular keep the matrix item verbatim: "is among the states whose roots are to be abandoned neither by seeing nor by development", "is not among the states not included in the spheres of existence"
chahi viññāṇehi viññeyyaṃ = is knowable by the six kinds of consciousness; jarābhibhūtaṃ = is overcome by ageing; aniccaṃ = is impermanent
-meva (Ekakaniddesa ^1-594) = indeed ("is indeed not a root", "indeed has conditions")
uppannaṃ chahi viññāṇehi viññeyyameva (one item in ^1-594) = is indeed knowable, once arisen, by the six kinds of consciousness
diṭṭhaṃ sutaṃ mutaṃ viññātaṃ rūpaṃ = Material form that is seen, heard, sensed, cognized.
X-viññeyyaṃ rūpaṃ = material form knowable by the eye (…, the mind element, the mind-consciousness element)
atthi sukhasamphassaṃ, atthi dukkhasamphassaṃ = some pleasant to touch, some painful to touch
yañca rūpaṃ upādā / na indriyaṃ = and the material form that is derived / that is not a faculty
anidassanaappaṭighaṃ dhammāyatanapariyāpannaṃ = that is invisible and makes no impact … and is included in the mental-object base
Headings: ### Rūpakaṇḍaṃ = The Chapter on Material Form; #### Uddeso = The Opening Statement; #### Mātikā = The Matrix (closing "Mātikā." = The matrix.); ##### Ekakaṃ = The Sets of One; Dukaṃ = The Pairs; Tikaṃ = The Sets of Three; Catukkaṃ = The Sets of Four; Pañcakaṃ … Ekādasakaṃ = The Set of Five … The Set of Eleven (closing lines in sentence case, as notes-3-02_3-03 / notes-5); #### Rūpavibhatti = The Classification of Material Form; ##### Ekakaniddeso = The Exposition of the Sets of One

## Source slips / oddities (translated as written)
- ^1-528: "ime dhammā kusalā tasseva …" has no full stop; rendered with a semicolon.
- ^1-553: "kāmarā gabyāpādānaṃ" split word; read as kāmarāgabyāpādānaṃ.
- ^1-553: the wholesome clause of the second to fourth paths lists aññindriyaṃ; the result clause lists aññātāvindriyaṃ (fits only the fourth path); kept as written.
- ^1-544: stray comma "viharati, animittaṃ"; ^1-574: missing comma "samādhindriyaṃ hoti manindriyaṃ"; ^1-579: no comma before "tasmiṃ samaye"; normal English punctuation used.
- ^1-584 lists "uppannaṃ, chahi viññāṇehi viññeyyaṃ" as two items, ^1-594 as one ("uppannaṃ chahi viññāṇehi viññeyyameva"); each translated as written.
- ^1-591/^1-592: no comma after jivhindriyaṃ; ^1-586 (line 112): no comma before the second "atthi".
- ^1-U1: odd block ID in the source, kept.

## For the consistency pass
- kabaḷīkāro āhāro: "edible food" here and in notes-3-02_3-03; notes-5 has "the nutriment of solid food".
- notes-5 frames "Katame dhammā X?" as "What are <matrix item>?"; this part follows the approved sample ("What states are indeterminate?").
- The Koṭṭhāsavāro line ("Now at that time there are four aggregates …") and the sasaṅkhārena / jhāna formulas are defined by 2-01 … 2-04 at the same time; align there or here.
