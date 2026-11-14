# Notes for parts 2-01 / 2-02 (new recurring terms and formulas)

Builder: build_2-01_2-02.py (one shared builder; `python -I -X utf8 build_2-01_2-02.py` builds both parts and
runs a self-test that re-translates the approved sample's Pāli and must reproduce it byte for byte).
Importing it does not build. Load it for later parts with:

    import importlib.util as u
    s = u.spec_from_file_location("F", r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-en\build_2-01_2-02.py")
    F = u.module_from_spec(s); s.loader.exec_module(F)
    F.translate_line(pali_line_without_block_id)   # raises KeyError on unknown Pāli

Reusable pieces: F.N (factor names), F.NAMEINFO / F.info() (all Koṭṭhāsa / Suññata names), F.KOTTHASA_PLURAL,
F.KOTTHASA_FACTORED, F.SUNNATA_GROUPS, F.STR (synonym strings), F.STR_PREFIX, F.tail_tr(), F.there_list(),
F.name_list(), F.qa_en(), F.summary_en(), F.kusala_en() with the phrase table F.PH, F.EXACT (headings/closings),
F.var_en() (variant brackets). Extend by adding keys (N, STR, PH, EXACT, INTROS); do not change existing values.
Verify: verify_2-01_2-02.py <part.md ...> (true – / — count per line, '?' count, forbidden strings, CR, blank lines).
Note: dashcheck.py as saved counts '?' (twice), not dashes (its dash characters were lost in encoding); it
still passes, and verify_2-01_2-02.py does the real dash count.

## Koṭṭhāsavāra (section on categories) frames
##### Koṭṭhāsavāro = ##### The Section on Categories
Koṭṭhāsavāro. (closing line) = The section on categories.
Tasmiṃ kho pana samaye X honti, Y hoti, …; ye vā pana … – ime dhammā kusalā. = Now at that time there are X, there is Y, …; or whatever other dependently arisen immaterial states there are at that time – these states are wholesome.
cattāro khandhā honti = there are four aggregates
dvāyatanāni honti = there are two sense bases
dve dhātuyo honti = there are two elements
tayo āhārā honti = there are three nutriments
aṭṭhindriyāni / sattindriyāni / navindriyāni / pañcindriyāni / cattāri indriyāni / tīṇindriyāni honti = there are eight / seven / nine / five / four / three faculties
pañcaṅgikaṃ / caturaṅgikaṃ / tivaṅgikaṃ / duvaṅgikaṃ jhānaṃ hoti = there is a five-factored / four-factored / three-factored / two-factored absorption
aṭṭhaṅgiko / pañcaṅgiko / caturaṅgiko / tivaṅgiko / duvaṅgiko maggo hoti = there is an eight-factored / a five-factored / a four-factored / a three-factored / a two-factored path
satta / cha / cattāri / tīṇi balāni honti = there are seven / six / four / three powers
tayo hetū / dve hetū honti; eko hetu hoti = there are three roots / two roots; there is one root
eko phasso hoti, ekā vedanā hoti, … = there is one contact, there is one feeling, … (eko/ekā/ekaṃ X = one X)
Katame tasmiṃ samaye cattāro khandhā honti? = What are the four aggregates at that time?
Katamaṃ tasmiṃ samaye pañcaṅgikaṃ jhānaṃ hoti? = What is the five-factored absorption at that time?
Katamo tasmiṃ samaye eko phasso hoti? = What is the one contact at that time?
Ime tasmiṃ samaye cattāro khandhā honti. = These are the four aggregates at that time.
Idaṃ tasmiṃ samaye pañcaṅgikaṃ jhānaṃ hoti. = This is the five-factored absorption at that time.
(list answer) Vedanākkhandho, saññākkhandho, … = The aggregate of feeling, the aggregate of perception, …
(list answer) … – idaṃ tasmiṃ samaye dhammāyatanaṃ hoti. = … – this is the mental-object base at that time.
Katamo tasmiṃ samaye saṅkhārakkhandho hoti? Phasso cetanā …; ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā ṭhapetvā vedanākkhandhaṃ ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ – ayaṃ tasmiṃ samaye saṅkhārakkhandho hoti. = What is the aggregate of mental formations at that time? Contact, intention, …; or whatever other dependently arisen immaterial states there are at that time, except the aggregate of feeling, except the aggregate of perception, except the aggregate of consciousness – this is the aggregate of mental formations at that time.
ṭhapetvā = except

## Suññatavāra (section on emptiness) frames
##### Suññatavāro = ##### The Section on Emptiness
Suññatavāro. (closing line) = The section on emptiness.
Tasmiṃ kho pana samaye dhammā honti, khandhā honti, … = Now at that time there are states, there are aggregates, …
dhammā / khandhā / āyatanāni / dhātuyo / āhārā / indriyāni / balāni / hetū honti = there are states / aggregates / sense bases / elements / nutriments / faculties / powers / roots
jhānaṃ hoti / maggo hoti = there is absorption / there is a path
Katame tasmiṃ samaye dhammā honti? … – ime tasmiṃ samaye dhammā honti. = What are the states at that time? … – these are the states at that time.
Katamaṃ tasmiṃ samaye jhānaṃ hoti? … – idaṃ tasmiṃ samaye jhānaṃ hoti. = What is absorption at that time? … – this is absorption at that time.
Katamo tasmiṃ samaye maggo hoti? … – ayaṃ tasmiṃ samaye maggo hoti. = What is the path at that time? … – this is the path at that time.
Katamo tasmiṃ samaye phasso hoti…pe… ayaṃ tasmiṃ samaye phasso hoti. = What is contact at that time… this is contact at that time.

## Names (categories)
vedanākkhandho / saññākkhandho / saṅkhārakkhandho / viññāṇakkhandho = the aggregate of feeling / of perception / of mental formations / of consciousness
manāyatanaṃ = the mind base; dhammāyatanaṃ = the mental-object base
manoviññāṇadhātu = the mind-consciousness element; dhammadhātu = the mental-object element
phassāhāro / manosañcetanāhāro / viññāṇāhāro = the nutriment of contact / of mental intention / of consciousness
āhāra = nutriment
upekkhā (factor) = equanimity; upekkhindriyaṃ = the faculty of equanimity
(set for later parts, unused here) manodhātu = the mind element; cakkhuviññāṇadhātu = the eye-consciousness element; kāyaviññāṇadhātu = the body-consciousness element

## Strings
cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ cetosamphassajā adukkhamasukhā vedanā = the mental state that is neither comfortable nor uncomfortable, the experience born of mind-contact that is neither painful nor pleasant, the feeling born of mind-contact that is neither painful nor pleasant
paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi = wisdom, understanding… non-delusion, investigation of states, right view

## The eight wholesome minds of the sense sphere
sasaṅkhārena = with prompting
somanassasahagataṃ ñāṇavippayuttaṃ = accompanied by joy and dissociated from knowledge
upekkhāsahagataṃ ñāṇasampayuttaṃ / ñāṇavippayuttaṃ = accompanied by equanimity and associated with / dissociated from knowledge
rūpārammaṇaṃ vā…pe… dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha = with a visible form as its object… or a mental object as its object, or whatever it takes up as its object
Paṭhamaṃ … Aṭṭhamaṃ cittaṃ. = The first … The eighth type of mind.
Aṭṭha kāmāvacaramahākusalacittāni. = The eight great wholesome types of mind of the sense sphere.

## Absorptions (fine-material and immaterial spheres)
jhāna = absorption; paṭhamaṃ / dutiyaṃ / tatiyaṃ / catutthaṃ / pañcamaṃ jhānaṃ = the first / second / third / fourth / fifth absorption
upasampajja viharati = enters and dwells in
rūpūpapattiyā maggaṃ bhāveti = one develops the path to rebirth in the fine-material sphere (sentence: At a time when one develops the path to rebirth in the fine-material sphere and …)
arūpūpapattiyā maggaṃ bhāveti = one develops the path to rebirth in the immaterial sphere
vivicceva kāmehi vivicca akusalehi dhammehi savitakkaṃ savicāraṃ vivekajaṃ pītisukhaṃ paṭhamaṃ jhānaṃ upasampajja viharati = quite secluded from sensual pleasures, secluded from unwholesome states, enters and dwells in the first absorption, which has applied thought and sustained thought, and rapture and happiness born of seclusion
vitakkavicārānaṃ vūpasamā ajjhattaṃ sampasādanaṃ cetaso ekodibhāvaṃ avitakkaṃ avicāraṃ samādhijaṃ pītisukhaṃ dutiyaṃ jhānaṃ upasampajja viharati = with the stilling of applied thought and sustained thought, enters and dwells in the second absorption, which has inner confidence and unification of mind, is without applied thought and without sustained thought, and has rapture and happiness born of concentration
pītiyā ca virāgā upekkhako ca viharati sato ca sampajāno sukhañca kāyena paṭisaṃvedeti, yaṃ taṃ ariyā ācikkhanti – "upekkhako satimā sukhavihārī"ti tatiyaṃ jhānaṃ upasampajja viharati = with the fading away of rapture, dwells equanimous, mindful and clearly aware, experiences happiness with the body, and enters and dwells in the third absorption, of which the noble ones declare – "Equanimous and mindful, one dwells in happiness"
sukhassa ca pahānā dukkhassa ca pahānā pubbeva somanassadomanassānaṃ atthaṅgamā adukkhamasukhaṃ upekkhāsatipārisuddhiṃ catutthaṃ jhānaṃ upasampajja viharati = with the abandoning of pleasure and the abandoning of pain, and with the earlier disappearance of joy and sadness, enters and dwells in the fourth absorption, which is neither painful nor pleasant and has purity of mindfulness due to equanimity
avitakkaṃ vicāramattaṃ samādhijaṃ pītisukhaṃ dutiyaṃ jhānaṃ upasampajja viharati (fivefold method) = enters and dwells in the second absorption, which is without applied thought but with sustained thought only, and has rapture and happiness born of concentration
(abbreviated openings) vivicceva kāmehi / vitakkavicārānaṃ vūpasamā / pītiyā ca virāgā / sukhassa ca pahānā = quite secluded from sensual pleasures / with the stilling of applied thought and sustained thought / with the fading away of rapture / with the abandoning of pleasure
sukha / dukkha in the fourth-absorption formula = pleasure / pain (sukha as a factor stays "happiness")
upekkhaka = equanimous; sato ca sampajāno = mindful and clearly aware
kasiṇa = meditation device; pathavī / āpo / tejo / vāyo / nīla / pīta / lohita / odāta-kasiṇaṃ = using earth / water / fire / air / blue / yellow / red / white as the meditation device
dukkhapaṭipadaṃ / sukhapaṭipadaṃ = with painful progress / with pleasant progress; dandhābhiññaṃ / khippābhiññaṃ = and slow / quick direct knowledge
paṭipadā = mode of progress
parittaṃ parittārammaṇaṃ = limited and with a limited object (appamāṇaṃ = immeasurable; appamāṇārammaṇaṃ = with an immeasurable object)
ajjhattaṃ arūpasaññī bahiddhā rūpāni passati = not perceiving material form in oneself, sees visible forms outside
parittāni / appamāṇāni / suvaṇṇadubbaṇṇāni = limited ones / immeasurable ones / beautiful and ugly
nīlāni nīlavaṇṇāni nīlanidassanāni nīlanibhāsāni = blue ones, blue in colour, blue in appearance, shining blue (same for yellow, red, white)
tāni abhibhuyya jānāmi passāmīti = and, having mastered them, thinks "I know, I see"
abhibhāyatana = base of mastery; vimokkha = liberation
rūpī rūpāni passati = possessing material form, sees visible forms; subhanti = with the thought "beautiful"
brahmavihāra = divine abiding; mettā / karuṇā / muditā / upekkhā-sahagataṃ = accompanied by loving-kindness / compassion / sympathetic joy / equanimity
asubha = the unattractive; uddhumātaka / vinīlaka / vipubbaka / vicchiddaka / vikkhāyitaka / vikkhittaka / hatavikkhittaka / lohitaka / puḷavaka / aṭṭhika-saññāsahagataṃ = accompanied by the perception of a bloated corpse / a discoloured corpse / a festering corpse / a corpse cut apart / a gnawed corpse / a scattered corpse / a hacked and scattered corpse / a bleeding corpse / a worm-infested corpse / a skeleton
sabbaso rūpasaññānaṃ samatikkamā paṭighasaññānaṃ atthaṅgamā nānattasaññānaṃ amanasikārā = by completely passing beyond perceptions of material form, by the disappearance of perceptions of impact, by not attending to perceptions of diversity
sabbaso X samatikkamma = having completely passed beyond X
ākāsānañcāyatana / viññāṇañcāyatana / ākiñcaññāyatana / nevasaññānāsaññāyatana = the base of infinite space / of infinite consciousness / of nothingness / of neither perception nor non-perception; -saññāsahagataṃ = accompanied by the perception of …
hīnaṃ / majjhimaṃ / paṇītaṃ = inferior / middling / superior
chanda- / vīriya- / citta- / vīmaṃsā-dhipateyyaṃ = with desire / energy / mind / inquiry as the dominant factor
vīmaṃsā = inquiry (kept distinct from vicaya = investigation in the wisdom string)
Variant siglum (bahūsu) = (in many editions)

## Headings and closing lines (2-02)
##### Catukkanayo / Pañcakanayo = ##### The Fourfold Method / The Fivefold Method (closing: The fourfold method. / The fivefold method.)
##### Catasso paṭipadā = ##### The Four Modes of Progress (closing: The four modes of progress.)
##### Cattāri ārammaṇāni / Dve ārammaṇāni = ##### The Four Kinds of Object / The Two Kinds of Object
##### Soḷasakkhattukaṃ = ##### The Sixteenfold Set; Aṭṭhakkhattukaṃ = The Eightfold Set; Idampi aṭṭhakkhattukaṃ = This Too Is an Eightfold Set; Aparampi aṭṭhakkhattukaṃ = Another Eightfold Set
##### Aṭṭhakasiṇaṃ soḷasakkhattukaṃ = ##### The Eight Meditation Devices, Sixteenfold
##### Abhibhāyatanāni parittāni = ##### The Bases of Mastery over Limited Forms; ##### Appamāṇāni = ##### The Bases of Mastery over Immeasurable Forms
Imānipi abhibhāyatanāni soḷasakkhattukāni. = These bases of mastery too are sixteenfold.
##### Tīṇi vimokkhāni soḷasakkhattukāni = ##### The Three Liberations, Sixteenfold; Imānipi tīṇi vimokkhāni soḷasakkhattukāni. = These three liberations too are sixteenfold.
##### Cattāri brahmavihārajhānāni soḷasakkhattukāni = ##### The Four Absorptions of the Divine Abidings, Sixteenfold
##### Asubhajhānaṃ soḷasakkhattukaṃ = ##### The Absorption on the Unattractive, Sixteenfold
##### Cattāri arūpajhānāni soḷasakkhattukāni = ##### The Four Immaterial Absorptions, Sixteenfold
Kāmāvacarakusalaṃ. / Rūpāvacarakusalaṃ. / Arūpāvacarakusalaṃ. (closing lines) = The wholesome mind of the sense sphere. / … of the fine-material sphere. / … of the immaterial sphere.

## Source points translated as written
^1-135: the answer ends with "?" ("…ayaṃ tasmiṃ samaye cetanā hoti?"); kept, like ^1-33 in the sample.
^1-189: no comma before "tasmiṃ samaye" ("pathavīkasiṇaṃ tasmiṃ samaye"); kept without comma.
^1-150: "cittakammaññatā hoti kāyapāguññatā hoti" lacks a comma; normal comma used in English.
^1-167, 180, 182, 202: the Pāli uses "–" instead of "," before "tasmiṃ samaye"; the dash is kept (dash rule).
^1-191, 205, 210, 264 (puḷavaka): stray space before "…pe…"; spacing mirrored.
^1-270: the chain of the seven other minds lists no vīmaṃsādhipateyyaṃ; translated as written.
sukhañca kāyena paṭisaṃvedeti (third absorption) = "experiences happiness with the body": literal; the commentary reads kāya here as the mental body; not added.
