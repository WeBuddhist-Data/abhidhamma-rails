import pathlib
d = pathlib.Path(__file__).parent
ch = '5-indriyavibhango'
NDE = '(no direct equivalent)'

# 2-219 / 2-221: bare list of the twenty-two faculties (sandhi compounds given whole)
LIST22 = {
 'body': 'kāyindriyaṃ', 'body faculty': 'kāyindriyaṃ', 'concentration': 'samādhindriyaṃ',
 'confidence': 'saddhindriyaṃ', 'ear': 'sotindriyaṃ', 'ear faculty': 'sotindriyaṃ',
 'equanimity': 'upekkhindriyaṃ', 'eye': 'cakkhundriyaṃ', 'eye faculty': 'cakkhundriyaṃ',
 'faculties': 'indriyāni', 'faculty': 'indriyaṃ', 'faculty of concentration': 'samādhindriyaṃ',
 'faculty of confidence': 'saddhindriyaṃ', 'faculty of energy': 'vīriyindriyaṃ',
 'faculty of equanimity': 'upekkhindriyaṃ', 'faculty of femininity': 'itthindriyaṃ',
 'faculty of final': 'aññindriyaṃ', 'faculty of gladness': 'somanassindriyaṃ',
 'faculty of masculinity': 'purisindriyaṃ', 'faculty of mindfulness': 'satindriyaṃ',
 'faculty of pain': 'dukkhindriyaṃ', 'faculty of pleasure': 'sukhindriyaṃ',
 'faculty of sadness': 'domanassindriyaṃ', 'faculty of wisdom': 'paññindriyaṃ',
 'femininity': 'itthindriyaṃ', 'fully': 'aññātāvindriyaṃ', 'gladness': 'somanassindriyaṃ',
 'know': 'anaññātaññassāmītindriyaṃ', 'knowledge': 'aññindriyaṃ', 'known': 'anaññātaññassāmītindriyaṃ',
 'life': 'jīvitindriyaṃ', 'life faculty': 'jīvitindriyaṃ', 'masculinity': 'purisindriyaṃ',
 'mind': 'manindriyaṃ', 'mind faculty': 'manindriyaṃ', 'mindfulness': 'satindriyaṃ',
 'nose': 'ghānindriyaṃ', 'nose faculty': 'ghānindriyaṃ', 'pain': 'dukkhindriyaṃ',
 'pleasure': 'sukhindriyaṃ', 'sadness': 'domanassindriyaṃ', 'tongue': 'jivhindriyaṃ',
 'tongue faculty': 'jivhindriyaṃ', 'twenty-two': 'Bāvīsatindriyāni',
 'twenty-two faculties': 'Bāvīsatindriyāni', 'wisdom': 'paññindriyaṃ',
}

QA = {'answers': NDE, 'questions': 'Pañhā', 'Questions and Answers': 'Pañhāpucchakaṃ', 'section': NDE,
      'Section of Questions': 'Pañhāpucchakaṃ'}

M = {}
M['2-5-0'] = {'analysis': 'vibhaṅgo', 'faculties': 'Indriya'}
M['2-5-1-0'] = {'abhidhamma': 'Abhidhamma', 'classification': 'bhājanīyaṃ'}
M['2-219'] = dict(LIST22)
M['2-220'] = {
 'abhidhamma': 'Abhidhamma', 'accompanied': 'sahagataṃ', 'arousing': 'ārambho', 'awakening': 'sambojjhaṅgo',
 'awakening factor': 'sambojjhaṅgo', 'bearing': 'dhāraṇatā', 'belonging': NDE, 'bodily': 'kāyikaṃ',
 'body': 'kāyo', 'body faculty': 'kāyindriyaṃ', 'body-consciousness': 'kāyaviññāṇaṃ',
 'body-contact': 'kāyasamphassa', 'born': 'kāyasamphassajaṃ', 'born of body-contact': 'kāyasamphassajaṃ',
 'born of mind-contact': 'cetosamphassajaṃ', 'burden': 'dhura', 'calm': 'samatho', 'cause': 'hetukaṃ',
 'class': 'vidhena', 'classification': 'bhājanīyaṃ', 'classified': 'bahuvidhena', 'comfort': 'sātaṃ',
 'comfortable': 'sātaṃ', 'concentration': 'samādhi', 'confidence': 'saddhā',
 'consciousness element': 'viññāṇadhātu', 'contact': 'phassa', 'continuing': 'iriyanā',
 'deep': 'abhippasādo', 'derived': 'upādāya', 'desire': 'chanda', 'discomfort': 'asātaṃ',
 'ear': 'sotindriyaṃ', 'ear faculty': 'sotindriyaṃ', 'effort': 'vāyāmo', 'eightfold': 'Aṭṭhavidhena',
 'eightfold class': 'Aṭṭhavidhena', 'element': 'dhātu', 'elements': 'bhūtānaṃ', 'empty': 'suñño',
 'endeavour': 'parakkamo', 'equanimity': 'upekkhindriyaṃ', 'exertion': 'nikkamo',
 'experience': 'vedayitaṃ', 'experience born': 'kāyasamphassajaṃ / vedayitaṃ', 'eye': 'cakkhu',
 'eye faculty': 'cakkhundriyaṃ', 'eye-consciousness': 'cakkhuviññāṇaṃ', 'factor': 'aṅgaṃ',
 'factor of investigation': 'dhammavicayasambojjhaṅgo', 'faculty': 'indriyaṃ',
 'faculty of concentration': 'samādhindriyaṃ', 'faculty of confidence': 'saddhindriyaṃ',
 'faculty of energy': 'vīriyindriyaṃ', 'faculty of equanimity': 'upekkhindriyaṃ',
 'faculty of femininity': 'itthindriyaṃ', 'faculty of final': 'aññindriyaṃ',
 'faculty of gladness': 'somanassindriyaṃ', 'faculty of masculinity': 'purisindriyaṃ',
 'faculty of mindfulness': 'satindriyaṃ', 'faculty of pain': 'dukkhindriyaṃ',
 'faculty of pleasure': 'sukhindriyaṃ', 'faculty of sadness': 'domanassindriyaṃ',
 'faculty of wisdom': 'paññindriyaṃ', 'features': 'liṅgaṃ', 'feeling': 'vedanā',
 'feeling born': 'kāyasamphassajā / vedanā', 'Feeling born': 'kāyasamphassajā / vedanā',
 'feminine': 'itthi', 'femininity': 'itthattaṃ', 'fine-material': 'rūpāvacaraṃ',
 'fine-material sphere': 'rūpāvacaraṃ', 'finished': NDE, 'fivefold': 'Pañcavidhena',
 'fivefold class': 'Pañcavidhena', 'found': 'viditānaṃ', 'fourfold': 'Catubbidhena',
 'fully': 'aññātāvindriyaṃ', 'gladness': 'somanassindriyaṃ', 'going': 'yapanā',
 'great elements': 'mahābhūtānaṃ', 'immaterial': 'arūpāvacaraṃ',
 'immaterial life faculty': 'arūpajīvitindriyaṃ', 'immaterial sphere': 'arūpāvacaraṃ',
 'investigation': 'vicayo', 'investigation of states': 'dhammavicayo', 'joined': 'sampayuttaṃ',
 'joined with contact': 'phassasampayuttaṃ', 'keeping': 'yapanā', 'kept': 'yāpanā',
 'know': 'anaññātaññassāmītindriyaṃ', 'knowledge': 'aññindriyaṃ', 'known': 'ñātānaṃ',
 'life': 'jīvitaṃ', 'life faculty': 'jīvitindriyaṃ', 'maintenance': 'pālanā', 'man': 'purisassa',
 'manner': 'ākappo', 'marks': 'nimittaṃ', 'masculine': 'purisa', 'masculinity': 'purisattaṃ',
 'material': 'rūpīnaṃ', 'material life faculty': 'rūpajīvitindriyaṃ', 'mental': 'cetasikaṃ',
 'mental comfort': 'cetasikaṃ sātaṃ', 'Mental comfort': 'cetasikaṃ sātaṃ',
 'mental discomfort': 'cetasikaṃ asātaṃ', 'mental pain': 'cetasikaṃ dukkhaṃ', 'mentally': 'cetasikaṃ',
 'mind': 'manindriyaṃ', 'mind element': 'manodhātu', 'mind faculty': 'manindriyaṃ',
 'mind joined': 'sampayuttaṃ', 'mind-consciousness': 'manoviññāṇaṃ',
 'mind-consciousness element': 'manoviññāṇadhātu', 'mind-contact': 'cetosamphassa',
 'mindfulness': 'sati', 'neutral': 'abyākataṃ', 'ninefold': 'Navavidhena', 'ninefold class': 'Navavidhena',
 'non-delusion': 'amoho', 'non-distraction': 'avikkhepo', 'non-drifting': 'apilāpanatā',
 'non-forgetting': 'asammussanatā', 'non-scattering': 'avisāhāro', 'nose': 'ghānindriyaṃ',
 'nose faculty': 'ghānindriyaṃ', 'pain': 'dukkhaṃ', 'painful': 'dukkhaṃ',
 'painful experience': 'dukkhaṃ vedayitaṃ', 'painful experience born': 'kāyasamphassajaṃ / dukkhaṃ vedayitaṃ',
 'painful feeling': 'dukkhā vedanā', 'painful feeling born': 'kāyasamphassajā / dukkhā vedanā',
 'painful nor pleasant': 'adukkhamasukhaṃ', 'path': 'magga', 'path factor': 'maggaṅgaṃ',
 'persistence': 'ṭhiti', 'pleasant': 'sukhaṃ', 'pleasant feeling': 'sukhā vedanā', 'pleasure': 'sukhaṃ',
 'power': 'balaṃ', 'proceeding': 'vattanā', 'putting': 'anikkhitta', 'realized': 'sacchikatānaṃ',
 'realizing': 'sacchikiriyāya', 'recollecting': 'paṭissati', 'reliance': 'okappanā',
 'remembering': 'anussati', 'right': 'sammā', 'root': 'hetukaṃ', 'sadness': 'domanassindriyaṃ',
 'sense': 'kāmāvacaraṃ', 'sense sphere': 'kāmāvacaraṃ', 'sensitive': 'pasādo', 'sensitive surface': 'pasādo',
 'sensitive surface derived': 'upādāya pasādo', 'sevenfold': 'Sattavidhena', 'sevenfold class': 'Sattavidhena',
 'single': 'Ekavidhena', 'single class': 'Ekavidhena', 'sixfold': 'Chabbidhena', 'sixfold class': 'Chabbidhena',
 'span': 'āyu', 'sphere': 'āvacaraṃ', 'stability': 'saṇṭhiti', 'standing': 'avaṭṭhiti',
 'steadiness': 'ṭhiti', 'striving': 'uyyāmo', 'surface': 'pasādo', 'surface derived': 'upādāya pasādo',
 'taking': 'sampaggāho', 'tenfold': 'Dasavidhena', 'tenfold class': 'Dasavidhena', 'therein': 'Tattha',
 'threefold': 'Tividhena', 'threefold class': 'Tividhena', 'tongue': 'jivhindriyaṃ',
 'tongue faculty': 'jivhindriyaṃ', 'trusting': 'saddahanā', 'twofold': 'Duvidhena',
 'twofold class': 'Duvidhena', 'uncomfortable': 'asātaṃ', 'understanding': 'pajānanā',
 'undistracted': 'avisāhaṭamānasatā', 'unslackening': 'asithilaparakkamatā', 'unwholesome': 'akusalaṃ',
 'unwholesome mind': 'akusalaṃ', 'view': 'diṭṭhi', 'vigour': 'thāmo', 'village': 'gāmopeso',
 'ways': 'bahuvidhena', 'wholesome': 'kusalaṃ', 'wholesome mind': 'kusalaṃ', 'wisdom': 'paññā',
 'woman': 'itthiyā', 'zeal': 'ussāho',
}
M['2-5-2-0'] = dict(QA)
M['2-221'] = dict(LIST22)
M['2-222'] = {
 'conflict': 'saraṇā', 'faculties': 'indriyānaṃ', 'free': 'araṇā', 'involve': 'saraṇā', 'neutral': 'abyākatā',
 'twenty-two': 'Bāvīsatīnaṃ', 'twenty-two faculties': 'Bāvīsatīnaṃ indriyānaṃ', 'unwholesome': 'akusalā',
 'wholesome': 'kusalā',
}
M['2-5-2-1-0'] = {'triads': 'Tikaṃ'}
M['2-223'] = {
 'abandoned': 'pahātabbā', 'able': 'upādāniyā', 'accompanied': 'sahagatā', 'accompanied by joy': 'pītisahagatā',
 'accumulation': 'ācaya', 'arise': 'uppādino', 'arisen': 'uppannā', 'belong': NDE, 'belongs': NDE,
 'beyond': 'asekkhā', 'birth': NDE, 'bound': 'uppādino', 'cannot': 'na', 'cause': 'hetukā', 'causes': 'hetukā',
 'clung': 'upādāniyā', 'defiled': 'saṃkiliṭṭha', 'defilement': 'saṃkilesikā', 'describable': 'vattabbaṃ',
 'described': 'vattabbā', 'dismantling': 'apacaya', 'dominant': 'ādhipatino', 'dominant factor': 'ādhipatino',
 'eleven': 'Ekādasindriyā', 'Eleven faculties': 'Ekādasindriyā', 'equanimity': 'upekkhā',
 'examination': 'vicāra', 'expanded': 'mahaggatā', 'expanded object': 'mahaggatārammaṇā',
 'external': 'bahiddhā', 'external object': 'bahiddhārammaṇā', 'factor': 'ādhipatino', 'faculties': 'indriyā',
 'faculties belong': 'indriyā', 'faculties may belong': 'indriyā siyā', 'faculty': 'indriyaṃ',
 'faculty of equanimity': 'Upekkhindriyaṃ', 'faculty of final': 'Aññindriyaṃ',
 'faculty of gladness': 'Somanassindriyaṃ', 'faculty of sadness': 'Domanassindriyaṃ', 'feeling': 'vedanāya',
 'fifteen': 'Pannarasindriyā', 'Fifteen faculties': 'Pannarasindriyā', 'fixed': 'niyatā',
 'fully': 'Aññātāvindriyaṃ', 'future object': 'anāgatārammaṇā', 'gladness': 'Somanassindriyaṃ',
 'happiness': 'sukha', 'having': NDE, 'inferior': 'hīnaṃ', 'internal': 'ajjhattā',
 'internal and external': 'ajjhattabahiddhā', 'internal object': 'ajjhattārammaṇā', 'invisible': 'anidassana',
 'invisible and offer': 'anidassanasappaṭighā', 'joined': 'sampayuttā',
 'joined with feeling': 'vedanāya sampayuttā', 'joined with painful': 'dukkhāya vedanāya sampayuttā',
 'joined with pleasant': 'sukhāya vedanāya sampayuttā', 'joy': 'pīti',
 'know': 'Anaññātaññassāmītindriyaṃ', 'knowledge': 'Aññindriyaṃ', 'known': 'Anaññātaññassāmītindriyaṃ',
 'leads': 'gāmi', 'life': 'Jīvitindriyaṃ', 'life faculty': 'Jīvitindriyaṃ', 'limited': 'parittā',
 'limited object': 'parittārammaṇā', 'measureless': 'appamāṇā', 'measureless object': 'appamāṇārammaṇā',
 'meditative': 'bhāvanāya', 'meditative development': 'bhāvanāya', 'middling': 'majjhimā',
 'neutral': 'abyākatā', 'object': 'ārammaṇā', 'object both internal': 'ajjhattabahiddhārammaṇā',
 'open to defilement': 'saṃkilesikā', 'outcome': NDE, 'painful': 'dukkhāya',
 'painful feeling': 'dukkhāya vedanāya', 'painful nor pleasant': 'adukkhamasukhāya',
 'past object': 'atītārammaṇā', 'path': 'magga', 'pleasant': 'sukhāya', 'pleasant feeling': 'sukhāya vedanāya',
 'present object': 'paccuppannārammaṇā', 'produce': 'vipākadhammadhammā', 'produces': 'vipākadhammadhammaṃ',
 'resistance': 'sappaṭighā', 'results nor things': 'nevavipākanavipākadhammadhammā', 'rightness': 'sammatta',
 'root': 'hetukā', 'sadness': 'Domanassindriyaṃ', 'seeing': 'dassanena', 'seventeen': 'Sattarasindriyā',
 'something': NDE, 'superior': 'paṇītā', 'ten': 'Dasindriyā', 'ten faculties': 'Dasindriyā',
 'Ten faculties': 'Dasindriyā', 'things': 'dhammā', 'thought': 'vitakka',
 'thought and examination': 'savitakkasavicāraṃ', 'trainees': 'sekkhā', 'training': 'asekkhā',
 'twelve': 'Dvādasindriyā', 'Twelve faculties': 'Dvādasindriyā', 'undefiled': 'asaṃkiliṭṭha',
 'unwholesome': 'akusalaṃ', 'wholesome': 'kusalaṃ', 'wrongness': 'micchatta',
}
M['2-5-2-2-0'] = {'pairs': 'Dukaṃ'}
M['2-224'] = dict(QA, **{
 'abandoned': 'pahātabbā', 'able': 'saṃyojaniyā', 'accompanied': 'sahagatā',
 'accompanied by equanimity': 'upekkhāsahagatā', 'accompanied by happiness': 'sukhasahagatā',
 'accompanied by joy': 'pītisahagatā', 'along': 'ānuparivattino', 'analysis': 'vibhaṅgo',
 'arise': 'sahabhuno', 'arising': 'sahabhū', 'belong': NDE, 'beyond': 'uttarā', 'birth': NDE,
 'bound': 'saṃyojaniyā', 'cannot': 'na', 'causes': 'hetū', 'clinging': 'upādānā',
 'clinging joined': 'upādānā ceva upādānasampayuttā', 'clung': 'upādāniyā', 'compounded': 'Saṅkhatā',
 'conflict': 'saraṇā', 'consciousness': NDE, 'defiled': 'saṃkiliṭṭhā', 'defilement': 'saṃkilesikā',
 'defilement joined': 'kileso ceva kilesasampayuttañcā', 'defilements': 'kilesā',
 'defilements joined': 'kilesā ceva kilesasampayuttā', 'derived': 'upādā', 'describable': 'vattabbaṃ',
 'described': 'vattabbā', 'dissociated': 'vippayuttā', 'dissociated from clinging': 'upādānavippayuttā',
 'dissociated from wrong': 'parāmāsavippayuttā', 'eighteen': 'Aṭṭhārasindriyā', 'eleven': 'Ekādasindriyā',
 'Eleven faculties': 'Ekādasindriyā', 'equanimity': 'upekkhā', 'examination': 'vicārā', 'existence': NDE,
 'external': 'bāhirā', 'factor': 'cetasikaṃ', 'factors': 'cetasikā', 'faculties': 'indriyā',
 'faculties are dissociated': 'indriyā / vippayuttā', 'faculties are joined': 'indriyā / sampayuttā',
 'faculties are mingled': 'indriyā / saṃsaṭṭhā', 'faculties are root': 'indriyā hetū',
 'faculties belong': 'indriyā', 'faculties may belong': 'indriyā siyā', 'faculties offer': 'indriyā sappaṭighā',
 'faculty': 'indriyaṃ', 'faculty of sadness': 'Domanassindriyaṃ', 'fetter': 'saṃyojanaṃ',
 'fetter joined': 'saṃyojanañceva saṃyojanasampayuttañcā', 'fetters': 'saṃyojanā',
 'fetters joined': 'saṃyojanā ceva saṃyojanasampayuttā', 'fifteen': 'Pannarasindriyā',
 'Fifteen faculties': 'Pannarasindriyā', 'fine-material': 'rūpāvacarā', 'fine-material sphere': 'rūpāvacarā',
 'finished': 'niṭṭhito', 'fixed': 'niyatā', 'floods': 'oghā', 'follow': 'ānuparivattino',
 'fourteen': 'Cuddasindriyā', 'Fourteen faculties': 'Cuddasindriyā', 'free': 'araṇā',
 'grasped': 'parāmaṭṭhā', 'grasping': 'parāmāsā', 'happiness': 'sukha', 'having': 'sahetukā',
 'hindrance': 'nīvaraṇaṃ', 'hindrance joined': 'nīvaraṇañceva nīvaraṇasampayuttañcā',
 'hindrances': 'nīvaraṇā', 'hindrances joined': 'nīvaraṇā ceva nīvaraṇasampayuttā', 'immaterial': 'arūpā',
 'immaterial sphere': 'arūpāvacarā', 'internal': 'ajjhattikā', 'invisible': 'Anidassanā',
 'involve': 'saraṇā', 'involves': 'saraṇaṃ', 'joined': 'sampayuttā', 'joined with clinging': 'upādānasampayuttā',
 'joined with mind': 'cittasampayuttā', 'joined with root': 'hetusampayuttā', 'joy': 'pīti', 'kinds': NDE,
 'kinds of consciousness': 'kenaci', 'know': 'Anaññātaññassāmītindriyaṃ', 'knowable': 'viññeyyā',
 'known': 'Anaññātaññassāmītindriyaṃ', 'leads': 'niyyānikaṃ', 'life': 'Jīvitindriyaṃ',
 'life faculty': 'Jīvitindriyaṃ', 'material': 'rūpā', 'meditative': 'bhāvanāya',
 'meditative development': 'bhāvanāya', 'mental': 'cetasikā', 'mental factor': 'cetasikaṃ',
 'mental factors': 'cetasikā', 'mental taints': 'āsavā', 'mind': 'cittaṃ', 'mind faculty': 'Manindriyaṃ',
 'mingled': 'saṃsaṭṭhā', 'mingled with mind': 'cittasaṃsaṭṭhā', 'none': 'No', 'object': 'ārammaṇā',
 'objects': 'sārammaṇā', 'obstructed': 'nīvaraṇiyā', 'open to defilement': 'saṃkilesikā', 'others': 'kenaci',
 'outcome': NDE, 'outside': 'apariyāpannā', 'produced': 'samuṭṭhānā', 'resistance': 'sappaṭighā',
 'root': 'hetu', 'root causes joined': 'hetū ceva hetusampayuttā', 'round': NDE,
 'sadness': 'Domanassindriyaṃ', 'seeing': 'dassanena', 'sense': 'kāmāvacarā', 'sense sphere': 'kāmāvacarā',
 'seventeen': 'Sattarasindriyā', 'sixteen': 'Soḷasindriyā', 'Sixteen faculties': 'Soḷasindriyā',
 'sphere': 'āvacarā', 'surpassable': 'sauttarā', 'surpassed': 'sauttarā', 'taint': 'āsavo',
 'taint joined': 'āsavo ceva āsavasampayuttañcā', 'taints': 'āsavā',
 'taints joined': 'āsavā ceva āsavasampayuttā', 'ten': 'Dasindriyā', 'ten faculties': 'Dasindriyā',
 'Ten faculties': 'Dasindriyā', 'thirteen': 'Terasindriyā', 'thirteen faculties': 'Terasindriyā',
 'Thirteen faculties': 'Terasindriyā', 'thought': 'vitakkā', 'tie': 'gantho',
 'tie joined': 'gantho ceva ganthasampayutta', 'tied': 'ganthaniyā', 'ties': 'ganthā',
 'ties joined': 'ganthā ceva ganthasampayuttā', 'together': 'saha', 'twelve': 'Dvādasindriyā',
 'Twelve faculties': 'Dvādasindriyā', 'twenty-one': 'Ekavīsatindriyā', 'unable': 'asaṃyojaniyā',
 'undefiled': 'asaṃkiliṭṭhā', 'unsurpassable': 'anuttarā', 'worldly': 'lokiyā', 'wrong': 'parāmāsā',
 'wrong grasping': 'parāmāsā', 'wrongly': 'parāmaṭṭhā', 'wrongly grasped': 'parāmaṭṭhā', 'yokes': 'yogā',
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
