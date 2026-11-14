# Notes: pi-1 parts 2-03 and 2-04 (English plain zero-shot)

Builders: build_2-03.py, build_2-04.py; shared constants and line translator: const_2_03_2_04.py
(imports build_ch2_01_sample.py; all sample strings, names and frames reused unchanged). Extra checks: verify_2-03_2-04.py.
Format: Pāli = English, one per line.

## Frames that 2-01 also defines (fixed constants here; checked against build_2-01_2-02.py and aligned where it differed)
Tasmiṃ kho pana samaye … = Now at that time …
cattāro khandhā honti, dvāyatanāni honti, dve dhātuyo honti, tayo āhārā honti = there are four aggregates, there are two sense bases, there are two elements, there are three nutriments
navindriyāni / pañcindriyāni / cattāri indriyāni / tīṇindriyāni honti = there are nine / five / four / three faculties
pañcaṅgikaṃ / caturaṅgikaṃ jhānaṃ hoti = there is a five-factored / four-factored absorption
aṭṭhaṅgiko / caturaṅgiko / tivaṅgiko / duvaṅgiko maggo hoti = there is an eight-factored / four-factored / three-factored / two-factored path
satta / cattāri / tīṇi balāni honti = there are seven / four / three powers
tayo hetū / dve hetū honti; eko hetu hoti = there are three roots / two roots; there is one root
eko phasso hoti … ekaṃ cittaṃ hoti = there is one contact … there is one mind
eko vedanākkhandho hoti (saññā-, saṅkhāra-, viññāṇa-) = there is one aggregate of feeling (perception, mental formations, consciousness)
ekaṃ manāyatanaṃ / ekaṃ manindriyaṃ / ekā manoviññāṇadhātu hoti = there is one mind base / one faculty of mind / one mind-consciousness element
ekaṃ dhammāyatanaṃ / ekā dhammadhātu hoti = there is one mental-object base / there is one mental-object element (as 2-01; I first had "base/element of mental objects", the pi-3 zero-shot wording)
ekā cakkhuviññāṇadhātu / ekā kāyaviññāṇadhātu / ekā manodhātu hoti = there is one eye-consciousness element / one body-consciousness element / one mind element
Katamo tasmiṃ samaye saṅkhārakkhandho hoti? Phasso cetanā … = What is the aggregate of mental formations at that time? Contact, intention, …
ye vā pana … arūpino dhammā ṭhapetvā vedanākkhandhaṃ ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ – ayaṃ tasmiṃ samaye saṅkhārakkhandho hoti = or whatever other dependently arisen immaterial states there are at that time, except the aggregate of feeling, except the aggregate of perception, except the aggregate of consciousness – this is the aggregate of mental formations at that time
…pe…. (ellipsis then full stop, e.g. "kusalā…pe….") = …. (as 2-01)
sasaṅkhārena = with prompting (placed after the accompaniment: "accompanied by joy and associated with wrong view, with prompting, with a visible form as its object…")
rūpārammaṇaṃ vā…pe… dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha = with a visible form as its object… or a mental object as its object, or whatever it takes up as its object
rūpārammaṇā vā…pe… phoṭṭhabbārammaṇā vā yaṃ yaṃ vā panārabbha = with a visible form as its object… or a touch as its object, or whatever it takes up as its object
rūpārammaṇaṃ vā…pe… yaṃ yaṃ vā panārabbha = with a visible form as its object… or whatever it takes up as its object
tasmiṃ samaye phasso hoti…pe… avikkhepo hoti…pe… ime dhammā kusalā. = at that time there is contact… there is non-distraction… these states are wholesome.
cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ cetosamphassajā adukkhamasukhā vedanā = the mental state that is neither comfortable nor uncomfortable, the experience born of mind-contact that is neither painful nor pleasant, the feeling born of mind-contact that is neither painful nor pleasant (as 2-01)
upekkhā / upekkhindriyaṃ = equanimity / the faculty of equanimity
ñāṇavippayutta = dissociated from knowledge
vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati = quite secluded from sensual pleasures… enters and dwells in the first absorption (as 2-02)
vitakkavicārānaṃ vūpasamā…pe… dutiyaṃ jhānaṃ…pe… pañcamaṃ jhānaṃ upasampajja viharati = with the stilling of applied thought and sustained thought… the second absorption… enters and dwells in the fifth absorption
sukhassa ca pahānā…pe… = with the abandoning of pleasure… (as 2-02)
rūpūpapattiyā / arūpūpapattiyā maggaṃ bhāveti = one develops the path to rebirth in the fine-material sphere / in the immaterial sphere (as 2-02)
pathavīkasiṇaṃ = using earth as the meditation device (as 2-02)
dukkhapaṭipadaṃ dandhābhiññaṃ (khippābhiññaṃ; sukhapaṭipadaṃ …) = with painful progress and slow direct knowledge (quick direct knowledge; with pleasant progress …) (as 2-02)
chanda- / vīriya- / citta- / vīmaṃsādhipateyyaṃ = with desire / energy / mind / inquiry as the dominant factor (as 2-02)
sabbaso rūpasaññānaṃ samatikkamā paṭighasaññānaṃ atthaṅgamā nānattasaññānaṃ amanasikārā = by completely passing beyond perceptions of material form, by the disappearance of perceptions of impact, by not attending to perceptions of diversity (as 2-02)
sabbaso ākāsānañcāyatanaṃ samatikkamma = having completely passed beyond the base of infinite space (likewise viññāṇañcāyatana = infinite consciousness, ākiñcaññāyatana = nothingness) (as 2-02)
ākāsānañcāyatana- … nevasaññānāsaññāyatanasaññāsahagataṃ = accompanied by the perception of the base of infinite space … of the base of neither perception nor non-perception (as 2-02)

## New in 2-03 (world-transcending mind)
Lokuttarakusalaṃ (heading) = The World-Transcending Wholesome Mind (term file)
lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ = one develops world-transcending absorption, which leads to liberation and leads away from accumulation
diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā = for the abandoning of wrong views, for reaching the first stage
kāmarāgabyāpādānaṃ tanubhāvāya dutiyāya bhūmiyā pattiyā = for the weakening of sensual lust and ill will, for reaching the second stage
kāmarāgabyāpādānaṃ anavasesappahānāya tatiyāya bhūmiyā pattiyā = for the abandoning without remainder of sensual lust and ill will, for reaching the third stage
rūparāgaarūparāgamānauddhaccaavijjāya anavasesappahānāya catutthāya bhūmiyā pattiyā = for the abandoning without remainder of lust for fine-material existence, lust for immaterial existence, conceit, restlessness and ignorance, for reaching the fourth stage
suññataṃ (qualifying the absorption) = which is empty
appaṇihitaṃ (qualifying the absorption) = which is desireless
Suddhikapaṭipadā (heading / closing) = Plain Progress / Plain progress.
Suññataṃ (heading / closing) = Emptiness / Emptiness.
Suññatamūlakapaṭipadā = Progress Rooted in Emptiness / Progress rooted in emptiness.
Appaṇihitaṃ = The Desireless / The desireless.
Appaṇihitamūlakapaṭipadā = Progress Rooted in the Desireless / Progress rooted in the desireless.
Vīsati mahānayā = The Twenty Great Methods / The twenty great methods.
Adhipati = The Dominant Factors / The dominant factors.
Paṭhamo / Dutiyo / Tatiyo / Catuttho maggo. = The first / second / third / fourth path.
Lokuttaraṃ cittaṃ. = The world-transcending mind.
lokuttaraṃ maggaṃ / satipaṭṭhānaṃ / sammappadhānaṃ / iddhipādaṃ / indriyaṃ / balaṃ / bojjhaṅgaṃ / saccaṃ / samathaṃ / dhammaṃ / khandhaṃ / āyatanaṃ / dhātuṃ / āhāraṃ / phassaṃ / vedanaṃ / saññaṃ / cetanaṃ / cittaṃ bhāveti = one develops a world-transcending path… develops a world-transcending foundation of mindfulness / right striving / basis of spiritual power / faculty / power / awakening factor / truth / world-transcending calm / a … state / aggregate / sense base / element / nutriment / world-transcending contact / feeling / perception / intention / a world-transcending mind
anaññātaññassāmītindriyaṃ = the faculty of coming to know what is not yet known (plain wording; pi-2 zero-shot and pi-6 termbase have the quoted form 'I shall know what is not yet known')
aññindriyaṃ = the faculty of final knowledge
tesaṃ dhammānaṃ anaññātānaṃ adiṭṭhānaṃ appattānaṃ aviditānaṃ asacchikatānaṃ sacchikiriyāya = for the realization of those states not yet known, not yet seen, not yet reached, not yet discovered and not yet realized (frame: "Whatever, <this>, is <string> – this is X at that time.")
tesaṃ dhammānaṃ ñātānaṃ diṭṭhānaṃ pattānaṃ viditānaṃ sacchikatānaṃ sacchikiriyāya = for the realization of those states known, seen, reached, discovered and realized
sammāvācā / sammākammanto / sammāājīvo = right speech / right action / right livelihood
maggaṅgaṃ maggapariyāpannaṃ = a path factor, included in the path
pīti- / samādhi- / vīriya- / sati- / dhammavicaya- / passaddhi-sambojjhaṅgo = the awakening factor of rapture / concentration / energy / mindfulness / investigation of states / tranquillity
catūhi vacīduccaritehi / tīhi kāyaduccaritehi / micchāājīvā ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto = avoidance of the four kinds of verbal misconduct / the three kinds of bodily misconduct / wrong livelihood, abstaining, refraining, abstinence, not doing, not performing, not committing, not overstepping the boundary, destroying the causeway
vīmaṃsā = inquiry (kept apart from vicaya = investigation)
sammappadhāna = right striving (kept apart from sammāvāyāma = right effort); iddhipāda = basis of spiritual power (kept apart from bala = power)

## New in 2-04 (unwholesome minds and results)
Dvādasa akusalāni (heading) = The Twelve Unwholesome Minds (term file); Dvādasa akusalacittāni. = The twelve unwholesome minds.
Katame dhammā akusalā / abyākatā? = What states are unwholesome / indeterminate?
akusalaṃ cittaṃ uppannaṃ hoti = an unwholesome mind has arisen
diṭṭhigatasampayuttaṃ / diṭṭhigatavippayuttaṃ = associated with wrong view / dissociated from wrong view
domanassasahagataṃ paṭighasampayuttaṃ = accompanied by sadness and associated with aversion
vicikicchāsampayuttaṃ / uddhaccasampayuttaṃ = associated with doubt / associated with restlessness
ime dhammā akusalā / abyākatā = these states are unwholesome / these states are indeterminate
micchādiṭṭhi / micchāsaṅkappo / micchāvāyāmo / micchāsamādhi = wrong view / wrong thought / wrong effort / wrong concentration
ahirikabalaṃ / anottappabalaṃ = the power of shamelessness / the power of fearlessness of wrongdoing
ahirikaṃ / anottappaṃ = shamelessness / fearlessness of wrongdoing (matrix wording)
lobho / doso / moho / abhijjhā / byāpādo = greed / hate / delusion / covetousness / ill will
vicikicchā / uddhaccaṃ = doubt / restlessness
dukkhaṃ (factor) = pain; domanassindriyaṃ = the faculty of sadness; sukhindriyaṃ = the faculty of pleasure
na hirīyati hiriyitabbena na hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā = not being ashamed of what one should be ashamed of, not being ashamed of engaging in bad, unwholesome states (frame "At that time, … – this is X at that time.")
na ottappati ottappitabbena na ottappati … = not fearing what one should fear, not fearing engaging in bad, unwholesome states
akusalamūlaṃ = the unwholesome root; abyākatamūlaṃ = the indeterminate root
diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ diṭṭhikantāro diṭṭhivisūkāyikaṃ diṭṭhivipphanditaṃ diṭṭhisaṃyojanaṃ gāho patiṭṭhāho abhiniveso parāmāso kummaggo micchāpatho micchattaṃ titthāyatanaṃ vipariyāsaggāho = view, holding views, the thicket of views, the wilderness of views, the contortion of views, the vacillation of views, the fetter of views, grasping, fixation, adherence, misapprehension, a wrong path, a false way, wrongness, a basis for sectarian doctrines, a distorted grasp
lobho lubbhanā lubbhitattaṃ sārāgo sārajjanā sārajjitattaṃ abhijjhā lobho akusalamūlaṃ = greed, being greedy, the state of being greedy, lust, lusting, the state of lusting, covetousness, greed, the unwholesome root
aññāṇaṃ adassanaṃ anabhisamayo ananubodho asambodho appaṭivedho asaṃgāhanā apariyogāhanā asamapekkhanā apaccavekkhanā apaccakkhakammaṃ dummejjhaṃ bālyaṃ asampajaññaṃ moho pamoho sammoho avijjā avijjogho avijjāyogo avijjānusayo avijjāpariyuṭṭhānaṃ avijjālaṅgī moho akusalamūlaṃ = lack of knowledge, lack of vision, lack of breakthrough, lack of understanding, lack of awakening, lack of penetration, failure to take in, failure to fathom, failure to consider, failure to review, failure to see for oneself, stupidity, foolishness, lack of clear awareness, delusion, deep delusion, confusion, ignorance, the flood of ignorance, the yoke of ignorance, the underlying tendency to ignorance, the obsession of ignorance, the bar of ignorance, delusion, the unwholesome root
doso dussanā dussitattaṃ byāpatti byāpajjanā byāpajjitattaṃ virodho paṭivirodho caṇḍikkaṃ asuropo anattamanatā cittassa = hate, hating, the state of hating, malice, being malicious, the state of being malicious, hostility, antagonism, fierceness, abusiveness, discontent of mind
kaṅkhā kaṅkhāyanā kaṅkhāyitattaṃ vimati vicikicchā dveḷhakaṃ dvedhāpatho saṃsayo anekaṃsaggāho āsappanā parisappanā apariyogāhanā thambhitattaṃ cittassa manovilekho = uncertainty, being uncertain, the state of being uncertain, perplexity, doubt, indecision, a fork in the road, wavering, failure to take a definite stand, hesitation, faltering, failure to fathom, stiffness of mind, scratching of the mind
cittassa uddhaccaṃ avūpasamo cetaso vikkhepo bhantattaṃ cittassa = restlessness of mind, disquiet, distraction of the mind, agitation of mind
cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ cetosamphassajā asātā dukkhā vedanā = mental discomfort, mental pain, the uncomfortable, painful experience born of mind-contact, the uncomfortable, painful feeling born of mind-contact
kāyikaṃ sātaṃ kāyikaṃ sukhaṃ kāyasamphassajaṃ sātaṃ sukhaṃ vedayitaṃ kāyasamphassajā sātā sukhā vedanā = bodily comfort, bodily pleasure, the comfortable, pleasant experience born of body-contact, the comfortable, pleasant feeling born of body-contact
cittassa ṭhiti (abbreviated string) = the stability of mind
takko … cetaso abhiniropanā (no final item) = thinking, applied thought, thought, fixing, firm fixing, the directing of the mind
tajjācakkhuviññāṇadhātusamphassajaṃ/-jā = born of the contact of the corresponding eye-consciousness element (likewise body-consciousness element, mind element)
tajjācakkhuviññāṇadhātu (end of the citta string) = the corresponding eye-consciousness element (likewise body-consciousness, mind element)
kāmāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ cakkhuviññāṇaṃ uppannaṃ hoti = as a result of wholesome action of the sense sphere that has been done and accumulated, eye-consciousness has arisen ("At a time when, as a result of …, …")
vipākā manodhātu / manoviññāṇadhātu uppannā hoti = the mind element / the mind-consciousness element has arisen (after the same "as a result of" clause)
cakkhu- / sota- / ghāna- / jivhā- / kāyaviññāṇaṃ = eye- / ear- / nose- / tongue- / body-consciousness
sukhasahagataṃ = accompanied by happiness (matrix)
Tasseva rūpāvacarassa (arūpāvacarassa) kusalassa kammassa katattā upacitattā vipākaṃ … = As a result of that same wholesome action of the fine-material (immaterial) sphere that has been done and accumulated, when one, …
Abyākatavipāko (heading) = Indeterminate Results (term file)
Kusalavipākapañcaviññāṇāni / Kusalavipākāni pañcaviññāṇāni. = The Five Kinds of Consciousness Resulting from Wholesome Action / The five kinds of consciousness resulting from wholesome action.
Kusalavipākamanodhātu / Kusalavipākā manodhātu. = The Mind Element Resulting from Wholesome Action / The mind element resulting from wholesome action.
Kusalavipākamanoviññāṇadhātusomanassasahagatā (and closing) = The Mind-Consciousness Element Resulting from Wholesome Action, Accompanied by Joy
Kusalavipākamanoviññāṇadhātuupekkhāsahagatā (and closing) = The Mind-Consciousness Element Resulting from Wholesome Action, Accompanied by Equanimity
Aṭṭhamahāvipākā = The Eight Great Results / The eight great results.
Rūpāvacaravipākā / Arūpāvacaravipākā = Results of the Fine-Material Sphere / Results of the Immaterial Sphere
paṭigha = aversion (paṭighasampayutta); in paṭighasaññā = impact (as 2-02)

## Source slips and oddities (translated as written)
^1-377: the answer ends with "hoti?" instead of "hoti." (English ends with "?").
^1-473: the question ends with "hoti." instead of "hoti?" (English: "What is intention at that time.").
^1-364: "maggapariyāpannaṃ, idaṃ tasmiṃ samaye aññindriyaṃ hoti" has a comma where every other answer has " – " (English keeps the comma).
^1-314: the lokuttara non-delusion answer has no "amoho kusalamūlaṃ" (unlike ^1-34); not added.
^1-433: the feeling of eye-consciousness is defined with the mental string (cetasikaṃ … cetosamphassajaṃ … = mental, born of mind-contact); kept, while ^1-445 (body-consciousness) has the bodily string.
^1-501 to ^1-504: unlike 2-02 (^1-265 …), the immaterial absorptions here lack "upekkhāsahagataṃ"; nothing added.

## Unsure renderings (review)
patiṭṭhāho = fixation; titthāyatanaṃ = a basis for sectarian doctrines; diṭṭhivisūkāyikaṃ = the contortion of views; vipariyāsaggāho = a distorted grasp
asaṃgāhanā = failure to take in; apaccakkhakammaṃ = failure to see for oneself; avijjālaṅgī = the bar of ignorance; anabhisamayo = lack of breakthrough
dveḷhakaṃ / dvedhāpatho / saṃsayo / āsappanā / parisappanā = indecision / a fork in the road / wavering / hesitation / faltering; manovilekho = scratching of the mind
velāanatikkamo = not overstepping the boundary; setughāto = destroying the causeway
suññataṃ / appaṇihitaṃ as adjectives of the absorption = which is empty / which is desireless (headings: Emptiness / The Desireless)
