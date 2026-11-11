import pathlib
d = pathlib.Path(__file__).parent
ch = '2-ayatanavibhango'
NDE = '(no direct equivalent)'

# 2-155 / 2-168: bare list of the twelve sense-fields (compounds only, cut to the part the keyword covers)
LIST12 = {
 'body': 'kāyāyatanaṃ', 'body sense-field': 'kāyāyatanaṃ', 'ear': 'sotāyatanaṃ', 'ear sense-field': 'sotāyatanaṃ',
 'eye': 'cakkhāyatanaṃ', 'eye sense-field': 'cakkhāyatanaṃ', 'mental': 'dhammāyatanaṃ', 'mental objects': 'dhammāyatanaṃ',
 'mind': 'manāyatanaṃ', 'mind sense-field': 'manāyatanaṃ', 'nose': 'ghānāyatanaṃ', 'nose sense-field': 'ghānāyatanaṃ',
 'objects': 'dhammāyatanaṃ', 'sense-field': 'āyatanaṃ', 'sense-field of mental': 'dhammāyatanaṃ',
 'sense-field of sights': 'rūpāyatanaṃ', 'sense-field of smells': 'gandhāyatanaṃ',
 'sense-field of sounds': 'saddāyatanaṃ', 'sense-field of tastes': 'rasāyatanaṃ',
 'sense-field of things': 'phoṭṭhabbāyatanaṃ', 'sense-fields': 'āyatanāni', 'sights': 'rūpāyatanaṃ',
 'smells': 'gandhāyatanaṃ', 'sounds': 'saddāyatanaṃ', 'tastes': 'rasāyatanaṃ', 'things': 'phoṭṭhabbāyatanaṃ',
 'things touched': 'phoṭṭhabbāyatanaṃ', 'tongue': 'jivhā', 'tongue sense-field': 'jivhāyatanaṃ',
 'touched': 'phoṭṭhabbāyatanaṃ', 'twelve': 'Dvādasāyatanāni', 'twelve sense-fields': 'Dvādasāyatanāni',
}

# shared by the five sense-organ definitions 2-156..2-160
ORGAN = {
 'body': 'attabhāva', 'bright': 'paṇḍara', 'bright surface': 'paṇḍara', 'derived': 'upādāya',
 'door': 'dvārā', 'element': 'dhātu', 'elements': 'bhūtānaṃ', 'empty': 'suñño', 'faculty': 'indriya',
 'field': 'khetta', 'great elements': 'mahābhūtānaṃ', 'invisible': 'anidassano',
 'invisible and offering': 'anidassano sappaṭigho', 'invisible and offers': 'anidassanaṃ sappaṭighaṃ',
 'itself': NDE, 'ocean': 'samuddo', 'offering': 'sappaṭigho', 'offering resistance': 'sappaṭigho',
 'offers': 'sappaṭighaṃ', 'offers resistance': 'sappaṭighaṃ', 'resistance': 'sappaṭigho',
 'sense-field': 'āyatanaṃ', 'sensitive': 'pasādo', 'sensitive surface': 'pasādo',
 'sensitive surface derived': 'upādāya pasādo', 'shore': 'tīra', 'surface': 'pasādo',
 'surface derived': 'upādāya pasādo', 'therein': 'Tattha', 'village': 'gāmo',
}

# shared by the five object definitions 2-162..2-166
OBJ = {
 'derived': 'upādāya', 'element': 'dhātu', 'elements': 'bhūtānaṃ', 'great elements': 'mahābhūtānaṃ',
 'invisible': 'anidassano', 'invisible and offering': 'anidassano sappaṭigho',
 'invisible and offers': 'anidassanena sappaṭighena', 'offering': 'sappaṭigho',
 'offering resistance': 'sappaṭigho', 'offers': 'sappaṭighena', 'offers resistance': 'sappaṭighena',
 'resistance': 'sappaṭigho', 'sense-field': 'āyatanaṃ', 'therein': 'Tattha', 'whatever': 'yo vā pana',
}

M = {}
M['2-2-0'] = {'analysis': 'vibhaṅgo', 'sense-fields': 'Āyatana'}
M['2-2-1-0'] = {'classification': 'bhājanīyaṃ', 'discourses': 'Suttanta'}
M['2-154'] = {
 'body': 'Kāyo', 'body sense-field': 'kāyāyatanaṃ', 'classification': 'bhājanīyaṃ', 'discourses': 'Suttanta',
 'ear': 'Sotaṃ', 'ear sense-field': 'sotāyatanaṃ', 'eye': 'Cakkhuṃ', 'eye sense-field': 'cakkhāyatanaṃ',
 'finished': NDE, 'impermanent': 'aniccaṃ', 'mental': 'Dhammā', 'mental objects': 'Dhammā', 'mind': 'Mano',
 'mind sense-field': 'manāyatanaṃ', 'nose': 'Ghānaṃ', 'nose sense-field': 'ghānāyatanaṃ', 'objects': 'Dhammā',
 'self': 'anattā', 'sense-field': 'āyatanaṃ', 'sense-field of mental': 'dhammāyatanaṃ',
 'sense-field of sights': 'rūpāyatanaṃ', 'sense-field of smells': 'gandhāyatanaṃ',
 'sense-field of sounds': 'saddāyatanaṃ', 'sense-field of tastes': 'rasāyatanaṃ',
 'sense-field of things': 'phoṭṭhabbāyatanaṃ', 'sense-fields': 'āyatanāni', 'sights': 'Rūpā',
 'smells': 'Gandhā', 'sounds': 'Saddā', 'subject to change': 'vipariṇāmadhammaṃ', 'tastes': 'Rasā',
 'things': 'Phoṭṭhabbā', 'things touched': 'Phoṭṭhabbā', 'tongue': 'Jivhā', 'tongue sense-field': 'jivhāyatanaṃ',
 'touched': 'Phoṭṭhabbā', 'twelve': 'Dvādasāyatanāni', 'twelve sense-fields': 'Dvādasāyatanāni', 'unsatisfactory': 'dukkhaṃ',
}
M['2-2-2-0'] = {'abhidhamma': 'Abhidhamma', 'classification': 'bhājanīyaṃ'}
M['2-155'] = dict(LIST12)
M['2-156'] = dict(ORGAN, **{
 'eye': 'cakkhu', 'eye element': 'cakkhudhātu', 'eye faculty': 'cakkhundriya', 'faculty': 'cakkhundriya',
 'eye sense-field': 'cakkhāyatanaṃ', 'guide': 'netta', 'sight': 'rūpaṃ', 'visible': 'sanidassanaṃ'})
M['2-157'] = dict(ORGAN, **{
 'ear': 'sotaṃ', 'ear element': 'sotadhātu', 'ear faculty': 'sotindriya', 'ear sense-field': 'sotāyatanaṃ',
 'hear': 'suṇissati', 'heard': 'suṇi', 'hears': 'suṇāti', 'sound': 'saddaṃ'})
M['2-158'] = dict(ORGAN, **{
 'nose': 'ghānaṃ', 'nose element': 'ghānadhātu', 'nose faculty': 'ghānindriya', 'nose sense-field': 'ghānāyatanaṃ',
 'smell': 'gandhaṃ', 'smelled': 'ghāyi', 'smells': 'ghāyati'})
M['2-159'] = dict(ORGAN, **{
 'tongue': 'jivhā', 'tongue element': 'jivhādhātu', 'tongue faculty': 'jīvhindriya',
 'tongue sense-field': 'jivhāyatanaṃ', 'taste': 'rasaṃ', 'tasted': 'sāyi', 'tastes': 'sāyati'})
M['2-160'] = dict(ORGAN, **{
 'body': 'kāyo', 'body element': 'kāyadhātu', 'body faculty': 'kāyindriya', 'body sense-field': 'kāyāyatanaṃ',
 'something': NDE, 'touch': 'phusissati', 'touchable': 'phoṭṭhabbaṃ', 'touched': 'phusi', 'touches': 'phusati'})
M['2-161'] = {
 'accompanied': 'sahagataṃ', 'belonging': NDE, 'body-consciousness': 'kāyaviññāṇaṃ', 'cause': 'hetukaṃ',
 'class': 'vidhena', 'classified': 'bahuvidhena', 'consciousness element': 'viññāṇadhātu', 'contact': 'phassa',
 'ear-consciousness': 'sotaviññāṇaṃ', 'eightfold': 'Aṭṭhavidhena', 'eightfold class': 'Aṭṭhavidhena',
 'element': 'dhātu', 'equanimity': 'upekkhindriya', 'eye-consciousness': 'cakkhuviññāṇaṃ', 'faculty': 'indriya',
 'faculty of equanimity': 'upekkhindriya', 'faculty of gladness': 'somanassindriya',
 'faculty of pain': 'dukkhindriya', 'faculty of pleasure': 'sukhindriya', 'faculty of sadness': 'domanassindriya',
 'feeling': 'vedanāya', 'fine-material': 'rūpāvacaraṃ', 'fine-material sphere': 'rūpāvacaraṃ',
 'fivefold': 'Pañcavidhena', 'fivefold class': 'Pañcavidhena', 'fourfold': 'Catubbidhena', 'gladness': 'somanassindriya',
 'immaterial': 'arūpāvacaraṃ', 'immaterial sphere': 'arūpāvacaraṃ', 'joined': 'sampayuttaṃ',
 'joined with contact': 'phassasampayuttaṃ', 'joined with feeling': 'vedanāya sampayuttaṃ',
 'joined with painful': 'dukkhāya vedanāya sampayuttaṃ', 'joined with pleasant': 'sukhāya vedanāya sampayuttaṃ',
 'mind': 'manāyatanaṃ', 'mind element': 'manodhātu', 'mind joined': 'sampayuttaṃ', 'mind sense-field': 'manāyatanaṃ',
 'mind-consciousness': 'manoviññāṇaṃ', 'mind-consciousness element': 'manoviññāṇadhātu', 'neutral': 'abyākataṃ',
 'ninefold': 'Navavidhena', 'ninefold class': 'Navavidhena', 'nose-consciousness': 'ghānaviññāṇaṃ',
 'pain': 'dukkha', 'painful': 'dukkhāya', 'painful feeling': 'dukkhāya vedanāya',
 'painful nor pleasant': 'adukkhamasukhāya', 'pleasant': 'sukhāya', 'pleasant feeling': 'sukhāya vedanāya',
 'pleasure': 'sukha', 'root': 'hetukaṃ', 'sadness': 'domanassindriya', 'sense': 'kāmāvacaraṃ', 'sense sphere': 'kāmāvacaraṃ',
 'sense-field': 'āyatanaṃ', 'sevenfold': 'Sattavidhena', 'sevenfold class': 'Sattavidhena',
 'single': 'Ekavidhena', 'single class': 'Ekavidhena', 'sixfold': 'Chabbidhena', 'sixfold class': 'Chabbidhena',
 'sphere': 'āvacaraṃ', 'tenfold': 'Dasavidhena', 'tenfold class': 'Dasavidhena', 'therein': 'Tattha',
 'threefold': 'Tividhena', 'threefold class': 'Tividhena', 'tongue-consciousness': 'jivhāviññāṇaṃ',
 'twofold': 'Duvidhena', 'twofold class': 'Duvidhena', 'unwholesome': 'akusalaṃ', 'unwholesome mind': 'akusalaṃ',
 'ways': 'bahuvidhena', 'wholesome': 'kusalaṃ', 'wholesome mind': 'kusalaṃ',
}
M['2-162'] = dict(OBJ, **{
 'black': 'kāḷakaṃ', 'blue': 'nīlaṃ', 'cat': 'veḷuriyassa', 'circular': 'parimaṇḍalaṃ', 'cloud': 'abbhā',
 'colour': 'vaṇṇa', 'conch': 'saṅkha', 'crimson': 'mañjiṭṭhakaṃ', 'darkness': 'andhakāro', 'disc': 'maṇḍalassa',
 'dust': 'rajo', 'eight-sided': 'aṭṭhaṃsaṃ', 'element of sights': 'rūpadhātu', 'eye': 'cakkhunā', 'gems': 'maṇi', 'invisible': 'anidassanena',
 'greenish': 'harivaṇṇaṃ', 'leaf-green': 'hari', 'light': 'āloko', 'mango': 'amba', 'mirror': 'ādāsa',
 'mist': 'mahikā', 'moon': 'canda', 'offering': 'sappaṭighaṃ', 'offering resistance': 'sappaṭighaṃ',
 'pearls': 'mutta', 'red': 'lohitakaṃ', 'resistance': 'sappaṭighaṃ', 'round': 'vaṭṭaṃ', 's-eye': 'veḷuriyassa',
 'sense-field of sights': 'rūpāyatanaṃ', 'shade': 'chāyā', 'shells': 'saṅkha', 'shining': 'nibhā',
 'shining colour': 'vaṇṇanibhā', 'shoot': 'aṅkura', 'sight': 'rūpaṃ', 'sights': 'rūpa', 'silver': 'rajatassa',
 'six-sided': 'chaḷaṃsaṃ', 'sixteen-sided': 'soḷasaṃsaṃ', 'smoke': 'dhūmo', 'square': 'caturassaṃ',
 'stars': 'tārakarūpānaṃ', 'sun': 'sūriya', 'sunshine': 'ātapo', 'visible': 'sanidassanaṃ',
 'visible and offering': 'sanidassanaṃ sappaṭighaṃ', 'whatever': 'yaṃ vā pana', 'white': 'odātaṃ',
 'yellow': 'pītakaṃ'})
M['2-163'] = dict(OBJ, **{
 'beings': 'sattānaṃ', 'clapping': NDE, 'colliding': 'sannighāta', 'conches': 'saṅkha', 'cries': 'nigghosa',
 'cymbals': 'samma', 'drums': 'bheri', 'ear': 'sotena', 'element of sounds': 'saddadhātu', 'elements': 'dhātūnaṃ',
 'hands': 'pāṇi', 'hear': 'suṇissati', 'heard': 'suṇi', 'hears': 'suṇāti', 'humans': 'manussa',
 'instruments': 'vādita', 'living': 'sattānaṃ', 'non-humans': 'amanussa', 'sense-field of sounds': 'saddāyatanaṃ',
 'singing': 'gīta', 'sound': 'saddo', 'sounds': 'sadda', 'tom-toms': 'paṇava', 'water': 'udaka', 'wind': 'vāta'})
M['2-164'] = dict(OBJ, **{
 'bark': 'taca', 'element of smells': 'gandhadhātu', 'flowers': 'puppha', 'fruits': 'phala', 'heartwood': 'sāra',
 'leaves': 'patta', 'nose': 'ghānena', 'pleasant': 'sugandho', 'putrid': 'vissa', 'raw': 'āma', 'roots': 'mūla',
 'sense-field of smells': 'gandhāyatanaṃ', 'smell': 'gandho', 'smelled': 'ghāyi', 'smells': 'ghāyati',
 'unpleasant': 'duggandho'})
M['2-165'] = dict(OBJ, **{
 'acrid': 'lambikaṃ', 'alkaline': 'khārikaṃ', 'astringent': 'kasāvo', 'bark': 'taca', 'bitter': 'tittakaṃ',
 'element of tastes': 'rasadhātu', 'flowers': 'puppha', 'fruits': 'phala',
 'invisible and offers': 'anidassanāya sappaṭighāya', 'leaves': 'patta', 'offers': 'sappaṭighāya',
 'offers resistance': 'sappaṭighāya', 'pungent': 'kaṭukaṃ', 'roots': 'mūla', 'salty': 'loṇikaṃ',
 'sense-field of tastes': 'rasāyatanaṃ', 'sour': 'ambilaṃ', 'stems': 'khandha', 'sweet': 'madhuraṃ',
 'taste': 'raso', 'tasted': 'sāyi', 'tastes': 'sāyati', 'tasty': 'sādu', 'tongue': 'jivhāya',
 'unappetising': 'asādu'})
M['2-166'] = {
 'air': 'vāyo', 'air element': 'vāyodhātu', 'body': 'kāyena', 'earth': 'Pathavī', 'earth element': 'Pathavīdhātu',
 'element': 'dhātu', 'element of things': 'phoṭṭhabbadhātu', 'fire': 'tejo', 'fire element': 'tejodhātu',
 'hard': 'kakkhaḷaṃ', 'heavy': 'garukaṃ', 'invisible': 'anidassanaṃ',
 'invisible and offering': 'anidassanaṃ sappaṭighaṃ', 'invisible and offers': 'anidassanena sappaṭighena',
 'light': 'lahukaṃ', 'offering': 'sappaṭighaṃ', 'offering resistance': 'sappaṭighaṃ', 'offers': 'sappaṭighena',
 'offers resistance': 'sappaṭighena', 'painful': 'dukkha', 'pleasant': 'sukha', 'resistance': 'sappaṭighaṃ',
 'rough': 'pharusaṃ', 'sense-field': 'āyatanaṃ', 'sense-field of things': 'phoṭṭhabbāyatanaṃ',
 'smooth': 'saṇhaṃ', 'soft': 'mudukaṃ', 'therein': 'Tattha', 'thing': 'phoṭṭhabbaṃ', 'things': 'phoṭṭhabba',
 'things touched': 'phoṭṭhabba', 'touch': 'phusissati', 'touchable': 'phoṭṭhabbaṃ', 'touched': 'phusi',
 'touches': 'phusati',
}
M['2-167'] = {
 'abhidhamma': 'Abhidhamma', 'aggregate': 'khandho', 'aggregate of feeling': 'vedanākkhandho',
 'aggregate of mental': 'saṅkhārakkhandho', 'Aggregate of Mental': 'saṅkhārakkhandho',
 'Aggregate of Perception': 'saññākkhandho', 'aggregate of perception': 'saññākkhandho', 'cause': 'hetuko',
 'causes': 'hetu', 'class': 'vidhena', 'classification': 'bhājanīyaṃ', 'classified': 'bahuvidhena',
 'contact': 'phassa', 'delusion': 'moha', 'desire': 'Rāga', 'element': 'dhātu', 'faculty': 'indriyaṃ',
 'faculty of femininity': 'Itthindriyaṃ', 'faculty of masculinity': 'purisindriyaṃ', 'feeling': 'vedanā',
 'feeling is classified': 'bahuvidhena vedanākkhandho', 'femininity': 'Itthi', 'finished': NDE, 'food': 'āhāro',
 'form': 'rūpaṃ', 'formations': 'saṅkhāra', 'formations is classified': 'bahuvidhena saṅkhārakkhandho',
 'hatred': 'dosa', 'invisible': 'anidassana', 'invisible and offers': 'anidassanaappaṭighaṃ',
 'joined': 'sampayutto', 'joined with contact': 'phassasampayutto', 'joined with mind': 'cittasampayutto',
 'masculinity': 'purisindriyaṃ', 'material': 'rūpaṃ', 'material form': 'rūpaṃ', 'mental': 'dhammāyatanaṃ',
 'Mental Formations': 'saṅkhāra', 'mental formations': 'saṅkhāra', 'mental objects': 'dhammāyatanaṃ', 'mind': 'citta',
 'neutral': 'abyākato', 'neutral feeling': 'abyākato', 'neutral formations': 'abyākato',
 'neutral perception': 'abyākato', 'objects': 'dhammāyatanaṃ', 'offers': 'appaṭighaṃ', 'perception': 'saññā',
 'perception is classified': 'bahuvidhena saññākkhandho', 'physical': 'kabaḷīkāro', 'resistance': 'appaṭighaṃ',
 'root': 'hetuko', 'sense-field': 'āyatanaṃ', 'sense-field of mental': 'dhammāyatanaṃ', 'single': 'Ekavidhena',
 'single class': 'Ekavidhena', 'ten': 'dasa', 'therein': 'Tattha', 'threefold': 'Tividhena',
 'threefold class': 'Tividhena', 'twofold': 'Duvidhena', 'twofold class': 'Duvidhena',
 'unconditioned': 'asaṅkhatā', 'unconditioned element': 'asaṅkhatā dhātu', 'unwholesome': 'akusalo',
 'Unwholesome feeling': 'akusalo', 'unwholesome feeling': 'akusalo', 'unwholesome formations': 'akusalo',
 'Unwholesome formations': 'akusalo', 'Unwholesome perception': 'akusalo', 'unwholesome perception': 'akusalo',
 'ways': 'bahuvidhena', 'wholesome': 'kusalo', 'wholesome feeling': 'kusalo', 'wholesome formations': 'kusalo',
 'wholesome perception': 'kusalo',
}
QA = {'answers': NDE, 'questions': 'Pañhā', 'Questions and Answers': 'Pañhāpucchakaṃ', 'section': NDE,
      'Section of Questions': 'Pañhāpucchakaṃ'}
M['2-2-3-0'] = dict(QA)
M['2-168'] = dict(LIST12)
M['2-169'] = {
 'conflict': 'saraṇā', 'free': 'araṇā', 'involve': 'saraṇā', 'neutral': 'abyākatā', 'sense-fields': 'āyatanānaṃ',
 'twelve': 'Dvādasannaṃ', 'twelve sense-fields': 'Dvādasannaṃ āyatanānaṃ', 'unwholesome': 'akusalā',
 'wholesome': 'kusalā',
}
M['2-2-3-1-0'] = {'triads': 'Tikaṃ'}
M['2-170'] = {
 'abandoned': 'pahātabbā', 'able': 'upādāniyā', 'accompanied': 'sahagatā', 'accompanied by joy': 'pītisahagatā',
 'accumulation': 'ācaya', 'arise': 'uppādino', 'arisen': 'uppannā', 'belong': NDE, 'beyond': 'asekkhā',
 'birth': NDE, 'bound': 'uppādino', 'cannot': 'na', 'cause': 'hetukā', 'causes': 'hetukā', 'clung': 'upādāniyā',
 'defiled': 'saṃkiliṭṭha', 'defilement': 'saṃkilesikā', 'describable': 'vattabbaṃ', 'described': 'vattabbā',
 'dismantling': 'apacaya', 'dominant': 'ādhipatino', 'dominant factor': 'ādhipatino', 'eleven': 'Ekādasāyatanā',
 'eleven sense-fields': 'Ekādasāyatanā', 'Eleven sense-fields': 'Ekādasāyatanā', 'equanimity': 'upekkhā',
 'examination': 'vicāra', 'expanded': 'mahaggatā', 'expanded object': 'mahaggatārammaṇā', 'external': 'bahiddhā',
 'external object': 'bahiddhārammaṇā', 'factor': 'ādhipatino', 'feeling': 'vedanāya', 'fixed': 'niyatā',
 'future object': 'anāgatārammaṇā', 'happiness': 'sukha', 'having': NDE, 'inferior': 'hīnā',
 'internal': 'ajjhattā', 'internal and external': 'ajjhattabahiddhā', 'internal object': 'ajjhattārammaṇā',
 'invisible': 'anidassana', 'invisible and offer': 'anidassanasappaṭighā', 'joined': 'sampayuttā',
 'joined with feeling': 'vedanāya sampayuttā', 'joined with painful': 'dukkhāya vedanāya sampayuttā',
 'joined with pleasant': 'sukhāya vedanāya sampayuttā', 'joy': 'pīti', 'limited': 'parittā',
 'limited object': 'parittārammaṇā', 'measureless': 'appamāṇā', 'measureless object': 'appamāṇārammaṇā',
 'meditative': 'bhāvanāya', 'meditative development': 'bhāvanāya', 'mental': 'Dhammāyatanaṃ', 'mental objects': 'Dhammāyatanaṃ',
 'middling': 'majjhimā', 'mind': 'Manāyatanaṃ', 'mind sense-field': 'Manāyatanaṃ', 'neutral': 'abyākatā',
 'object': 'ārammaṇā', 'object both internal': 'ajjhattabahiddhārammaṇā', 'objects': 'Dhammāyatanaṃ',
 'offers': 'sappaṭighaṃ', 'offers resistance': 'sappaṭighaṃ', 'open to defilement': 'saṃkilesikā',
 'outcome': NDE, 'painful': 'dukkhāya', 'painful feeling': 'dukkhāya vedanāya',
 'painful nor pleasant': 'adukkhamasukhāya', 'past object': 'atītārammaṇā', 'path': 'magga', 'pleasant': 'sukhāya',
 'pleasant feeling': 'sukhāya vedanāya', 'present object': 'paccuppannārammaṇā', 'produce': 'vipākadhammadhammā',
 'resistance': 'sappaṭigha', 'results nor things': 'nevavipākanavipākadhammadhammā', 'rightness': 'sammatta',
 'root': 'hetukā', 'seeing': 'dassanena', 'sense-field': 'āyatanaṃ', 'sense-field of mental': 'Dhammāyatanaṃ',
 'sense-field of sights': 'Rūpāyatanaṃ', 'sense-field of sounds': 'Saddāyatanaṃ', 'sense-fields': 'āyatanā',
 'sense-fields are invisible': 'āyatanā anidassana', 'sense-fields belong': 'āyatanā',
 'sense-fields may belong': 'āyatanā siyā', 'sights': 'Rūpāyatanaṃ', 'sounds': 'Saddāyatanaṃ', 'superior': 'paṇītā',
 'ten': 'Dasāyatanā', 'ten sense-fields': 'Dasāyatanā', 'Ten sense-fields': 'Dasāyatanā',
 'Ten sense-fields belong': 'Dasāyatanā', 'things': 'dhammā', 'thought': 'vitakka',
 'thought and examination': 'savitakkasavicāraṃ', 'trainees': 'sekkhā', 'training': 'asekkhā',
 'undefiled': 'asaṃkiliṭṭha', 'unwholesome': 'akusalā', 'visible': 'sanidassana', 'wholesome': 'kusalā',
 'wrongness': 'micchatta',
}
M['2-2-3-2-0'] = {'pairs': 'Dukaṃ'}
M['2-171'] = dict(QA, **{
 'abandoned': 'pahātabbā', 'able': 'saṃyojaniyā', 'accompanied': 'sahagatā',
 'accompanied by equanimity': 'upekkhāsahagatā', 'accompanied by happiness': 'sukhasahagatā',
 'accompanied by joy': 'pītisahagatā', 'along': 'ānuparivattino', 'analysis': 'vibhaṅgo', 'arise': 'sahabhuno',
 'arising': 'sahabhū', 'belong': NDE, 'beyond': 'uttarā', 'birth': NDE, 'bound': 'saṃyojaniyā', 'cannot': 'na',
 'cause': 'hetu', 'causes': 'hetū', 'clinging': 'upādānā', 'clinging joined': 'upādānā ceva upādānasampayuttā',
 'clung': 'upādāniyā', 'compounded': 'saṅkhatā', 'conflict': 'saraṇā', 'consciousness': NDE,
 'defiled': 'saṃkiliṭṭhā', 'defilement': 'saṃkilesikā', 'defilement joined': 'kileso ceva kilesasampayuttañca',
 'defilements': 'kilesā', 'defilements joined': 'kilesā ceva kilesasampayuttā', 'derived': 'upādā',
 'describable': 'vattabbaṃ', 'described': 'vattabbā', 'dissociated': 'vippayuttā',
 'dissociated from clinging': 'upādānavippayuttā', 'dissociated from wrong': 'parāmāsavippayuttā',
 'eleven': 'Ekādasāyatanā', 'eleven sense-fields': 'Ekādasāyatanā', 'Eleven sense-fields': 'Ekādasāyatanā',
 'equanimity': 'upekkhā', 'examination': 'vicārā', 'existence': NDE, 'external': 'bāhirā', 'factor': 'cetasikaṃ',
 'factors': 'cetasikā', 'fetter': 'saṃyojanaṃ', 'fetter joined': 'saṃyojanañceva saṃyojanasampayuttañca',
 'fetters': 'saṃyojanā', 'fetters joined': 'saṃyojanā ceva saṃyojanasampayuttā', 'fine-material': 'rūpāvacarā',
 'fine-material sphere': 'rūpāvacarā', 'finished': 'niṭṭhito', 'fixed': 'niyatā', 'floods': 'oghā',
 'follow': 'ānuparivattino', 'free': 'araṇā', 'grasped': 'parāmaṭṭhā', 'grasping': 'parāmāsā',
 'happiness': 'sukha', 'having': 'sahetukā', 'hindrance': 'nīvaraṇaṃ',
 'hindrance joined': 'nīvaraṇañceva nīvaraṇasampayuttañca', 'hindrances': 'nīvaraṇā',
 'hindrances joined': 'nīvaraṇā ceva nīvaraṇasampayuttā', 'immaterial': 'arūpaṃ',
 'immaterial sphere': 'arūpāvacarā', 'internal': 'ajjhattikā', 'invisible': 'anidassanā', 'involve': 'saraṇā',
 'joined': 'sampayuttā', 'joined with clinging': 'upādānasampayuttā', 'joined with mind': 'cittasampayuttaṃ',
 'joined with root': 'hetusampayuttā', 'joy': 'pīti', 'kinds': NDE, 'kinds of consciousness': 'kenaci',
 'knowable': 'viññeyyā', 'material': 'rūpā', 'meditative': 'bhāvanāya', 'meditative development': 'bhāvanāya',
 'mental': 'Dhammāyatanaṃ', 'mental factor': 'cetasikaṃ', 'mental factors': 'cetasikā', 'mental objects': 'Dhammāyatanaṃ',
 'mental taints': 'āsavā', 'mind': 'cittaṃ', 'mind sense-field': 'Manāyatanaṃ', 'mingled': 'saṃsaṭṭhaṃ',
 'mingled with mind': 'cittasaṃsaṭṭhaṃ', 'object': 'ārammaṇā', 'objects': 'Dhammāyatanaṃ', 'obstructed': 'nīvaraṇiyā',
 'open to defilement': 'saṃkilesikā', 'others': 'kenaci', 'outcome': NDE, 'outside': 'apariyāpannā',
 'produced': 'samuṭṭhānā', 'resistance': 'sappaṭighā', 'root': 'hetu',
 'root cause joined': 'hetu ceva hetusampayuttañca', 'root causes joined': 'hetū ceva hetusampayuttā',
 'round': NDE, 'seeing': 'dassanena', 'sense': 'kāmāvacarā', 'sense sphere': 'kāmāvacarā', 'sense-field': 'āyatanaṃ',
 'sense-field of mental': 'Dhammāyatanaṃ', 'sense-field of sights': 'Rūpāyatanaṃ',
 'sense-field of sounds': 'Saddāyatanaṃ', 'sense-fields': 'āyatanā',
 'sense-fields are dissociated': 'āyatanā / vippayuttā', 'sense-fields are invisible': 'āyatanā anidassanā',
 'sense-fields belong': 'āyatanā', 'sense-fields may belong': 'āyatanā siyā',
 'sense-fields offer': 'āyatanā sappaṭighā', 'sights': 'Rūpāyatanaṃ', 'sounds': 'Saddāyatanaṃ', 'sphere': 'āvacarā',
 'surpassable': 'sauttarā', 'surpassed': 'sauttarā', 'taint': 'āsavo',
 'taint joined': 'āsavo ceva āsavasampayuttañca', 'taints': 'āsavā',
 'taints joined': 'āsavā ceva āsavasampayuttā', 'ten': 'Dasāyatanā', 'ten sense-fields': 'Dasāyatanā',
 'Ten sense-fields': 'Dasāyatanā', 'Ten sense-fields belong': 'Dasāyatanā',
 'Ten sense-fields offer': 'Dasāyatanā sappaṭighā', 'thought': 'vitakkā', 'tie': 'gantho',
 'tie joined': 'gantho ceva ganthasampayuttañca', 'tied': 'ganthaniyā', 'ties': 'ganthā',
 'ties joined': 'ganthā ceva ganthasampayuttā', 'together': 'saha', 'unable': 'asaṃyojaniyā',
 'uncompounded': 'asaṅkhataṃ', 'undefiled': 'asaṃkiliṭṭhā', 'unsurpassable': 'anuttarā',
 'visible': 'sanidassanaṃ', 'worldly': 'lokiyā', 'wrong': 'parāmāsā', 'wrong grasping': 'parāmāsā',
 'wrongly': 'parāmaṭṭhā', 'wrongly grasped': 'parāmaṭṭhā', 'yokes': 'yogā',
})

out, missing = [], []
for line in (d / f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines():
    sid, kws = line.split('] ', 1)
    sid = sid[1:]
    m = M[sid]
    pairs = []
    for k in kws.split(', '):
        k = k.strip()
        if k not in m:
            missing.append((sid, k)); pairs.append(f'???={k}')
        else:
            pairs.append(f'{m[k]}={k}')
    out.append(f'[{sid}] ' + ', '.join(pairs))
(d / f'{ch}.mapped.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
print('written', len(out), 'missing', missing)
