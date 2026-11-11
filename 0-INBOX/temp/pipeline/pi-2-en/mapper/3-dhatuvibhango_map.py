import pathlib
d = pathlib.Path(__file__).parent
ch = '3-dhatuvibhango'
NDE = '(no direct equivalent)'

# shared by the four primary-element definitions 2-173..2-177
PRIM = {
 'birth': NDE, 'element': 'dhātu', 'element is twofold': 'dhātudvayaṃ', 'else': 'aññampi',
 'external': 'bāhirā', 'externally': 'bāhiraṃ', 'gathered': 'abhisaññūhitvā', 'grouped': 'abhisaṅkhipitvā',
 'internal': 'ajjhattikā', 'internally': 'ajjhattaṃ', 'namely': 'seyyathidaṃ', 'oneself': 'paccattaṃ',
 'therein': 'Tattha', 'together': 'tadekajjhaṃ', 'twofold': 'dvayaṃ', 'whatever': 'yaṃ vā pana',
 'form': 'rūpassa', 'material': 'rūpassa', 'material form': 'rūpassa',
}

# the eighteen elements listed bare (2-183, 2-186)
LIST18 = {
 'body': 'kāya', 'body element': 'kāyadhātu', 'body-consciousness': 'kāyaviññāṇa',
 'body-consciousness element': 'kāyaviññāṇadhātu', 'consciousness element': 'viññāṇadhātu',
 'ear': 'sota', 'ear element': 'sotadhātu', 'ear-consciousness': 'sotaviññāṇa',
 'ear-consciousness element': 'sotaviññāṇadhātu', 'eighteen': 'Aṭṭhārasa', 'eighteen elements': 'Aṭṭhārasa dhātuyo',
 'element': 'dhātu', 'element of mental': 'dhammadhātu', 'element of sights': 'rūpadhātu',
 'element of smells': 'gandhadhātu', 'element of sounds': 'saddadhātu', 'element of tastes': 'rasadhātu',
 'element of things': 'phoṭṭhabbadhātu', 'elements': 'dhātuyo', 'eye': 'cakkhu', 'eye element': 'cakkhudhātu',
 'eye-consciousness': 'cakkhuviññāṇa', 'eye-consciousness element': 'cakkhuviññāṇadhātu', 'mental': 'dhamma',
 'mental objects': 'dhamma', 'mind': 'mano', 'mind element': 'manodhātu', 'mind-consciousness': 'manoviññāṇa',
 'mind-consciousness element': 'manoviññāṇadhātu', 'nose': 'ghāna', 'nose element': 'ghānadhātu',
 'nose-consciousness': 'ghānaviññāṇa', 'nose-consciousness element': 'ghānaviññāṇadhātu', 'objects': 'dhamma',
 'sights': 'rūpa', 'smells': 'gandha', 'sounds': 'sadda', 'tastes': 'rasa', 'things': 'phoṭṭhabba',
 'things touched': 'phoṭṭhabba', 'tongue': 'jivhā', 'tongue element': 'jivhādhātu',
 'tongue-consciousness': 'jivhāviññāṇa', 'tongue-consciousness element': 'jivhāviññāṇadhātu',
 'touched': 'phoṭṭhabba',
}

QA = {'answers': NDE, 'questions': 'Pañhā', 'Questions and Answers': 'Pañhāpucchakaṃ', 'section': NDE,
      'Section of Questions': 'Pañhāpucchakaṃ'}

M = {}
M['2-3-0'] = {'analysis': 'vibhaṅgo', 'elements': 'Dhātu'}
M['2-3-1-0'] = {'classification': 'bhājanīyaṃ', 'discourses': 'Suttanta'}
M['2-172'] = {
 'air': 'vāyo', 'air element': 'vāyodhātu', 'consciousness': 'viññāṇa', 'consciousness element': 'viññāṇadhātu',
 'earth': 'pathavī', 'earth element': 'pathavīdhātu', 'element': 'dhātu', 'elements': 'dhātuyo', 'fire': 'tejo',
 'fire element': 'tejodhātu', 'space': 'ākāsa', 'space element': 'ākāsadhātu', 'water': 'āpo',
 'water element': 'āpodhātu',
}
M['2-173'] = dict(PRIM, **{
 'body': 'lomā', 'bone': 'aṭṭhi', 'bones': 'aṭṭhi', 'cat': 'veḷuriyo', 'conch': 'saṅkho', 'contents': 'udariyaṃ',
 'copper': 'lohaṃ', 'coral': 'pavāḷaṃ', 'earth': 'bhūmi', 'earth element': 'pathavīdhātu', 'emerald': 'masāragallaṃ',
 'excrement': 'karīsaṃ', 'flesh': 'maṃsaṃ', 'gems': 'maṇi', 'grass': 'tiṇaṃ', 'gravel': 'sakkharā', 'hair': 'kesā',
 'hard': 'kakkhaḷaṃ', 'hardness': 'kakkhaḷattaṃ', 'head': 'kesā', 'heart': 'hadayaṃ', 'intestines': 'antaṃ',
 'iron': 'ayo', 'kidneys': 'vakkaṃ', 'liver': 'yakanaṃ', 'lungs': 'papphāsaṃ', 'marrow': 'miñjaṃ',
 'membranes': 'kilomakaṃ', 'mesentery': 'antaguṇaṃ', 'mountains': 'pabbato', 'nails': 'nakhā', 'ore': 'sajjhaṃ',
 'pearl': 'muttā', 'potsherds': 'kaṭhalaṃ', 'rock': 'pāsāṇo', 'ruby': 'lohitaṅko', 's-eye': 'veḷuriyo',
 'shell': 'saṅkho', 'silver': 'rajataṃ', 'sinews': 'nhāru', 'skin': 'taco', 'solid': 'kharigataṃ',
 'spleen': 'pihakaṃ', 'stomach': 'udariyaṃ', 'stone': 'silā', 'teeth': 'dantā', 'tin': 'tipu', 'wood': 'kaṭṭhaṃ'})
M['2-174'] = dict(PRIM, **{
 'bark': 'taca', 'bile': 'pittaṃ', 'blood': 'lohitaṃ', 'butter': 'navanītaṃ', 'cohesion': 'bandhanattaṃ',
 'curds': 'dadhi', 'earth': 'bhummāni', 'fat': 'medo', 'flowers': 'puppha', 'fluid': 'lasikā', 'fruits': 'phala',
 'ghee': 'sappi', 'grease': 'vasā', 'honey': 'madhu', 'juice': 'raso', 'leaves': 'patta', 'milk': 'khīraṃ',
 'moistness': 'sinehagataṃ', 'moisture': 'sineho', 'molasses': 'phāṇitaṃ', 'mucus': 'siṅghāṇikā',
 'phlegm': 'semhaṃ', 'pus': 'pubbo', 'roots': 'mūla', 'saliva': 'kheḷo', 'sky': 'antalikkhāni', 'stems': 'khandha',
 'sweat': 'sedo', 'tears': 'assu', 'urine': 'muttaṃ', 'water': 'āpo', 'water element': 'āpodhātu',
 'waters': 'udakāni', 'watery': 'āpogataṃ'})
M['2-175'] = dict(PRIM, **{
 'ages': 'jīrīyati', 'burned': 'pariḍayhati', 'chewed': 'khāyita', 'cow': 'gomayaggi', 'digested': 'pariṇāmaṃ gacchati',
 'drunk': 'pīta', 'dung': 'gomayaggi', 'eaten': 'asita', 'external fire': 'bāhirā tejo',
 'external fire element': 'bāhirā tejodhātu', 'fiery': 'tejogataṃ', 'fire': 'tejo', 'fire element': 'tejodhātu',
 'fully': 'sammā', 'grass': 'tiṇaggi', 'heap': 'sannicaya', 'heat': 'usmā', 'heatedness': 'usmāgataṃ',
 'husks': 'thusaggi', 'internal fire': 'ajjhattikā tejo', 'internal fire element': 'ajjhattikā tejodhātu',
 'lightning': 'indaggi', 'rubbish': 'saṅkāraggi', 'straw': 'palālaggi', 'sun': 'sūriya', 'tasted': 'sāyitaṃ',
 'warmed': 'santappati', 'warmness': 'usumagataṃ', 'warmth': 'usumaṃ', 'wood': 'kaṭṭhaggi'})
M['2-176'] = dict(PRIM, **{
 'air': 'vāyo', 'air element': 'vāyodhātu', 'airy': 'vāyogataṃ', 'belly': 'kucchisayā', 'bird': 'supaṇṇa',
 'birds': NDE, 'black': 'kāḷa', 'bowels': 'koṭṭhāsayā', 'breathing': 'assāso', 'cold': 'sītā',
 'coursing': 'ānusārino', 'cutting': 'satthaka', 'distension': 'thambhitattaṃ', 'downward': 'adhogamā',
 'dust-free': 'arajā', 'dusty': 'sarajā', 'east': 'puratthimā', 'external air': 'bāhirā vāyo',
 'external air element': 'bāhirā vāyodhātu', 'fan': 'vidhūpana', 'fans': 'tālavaṇṭa', 'gentle': 'parittā',
 'going': 'gamā', 'high-altitude': 'verambha', 'hot': 'uṇhā', 'internal air': 'ajjhattikā vāyo',
 'internal air element': 'ajjhattikā vāyodhātu', 'limbs': 'aṅgamaṅgānusārino', 'palm-leaf': 'tālavaṇṭa',
 'piercing': 'khuraka', 'throbbing': 'uppalaka', 'upward': 'uddhaṅgamā', 'winds': 'vātā', 'wings': 'pakkha',
 'winnowing': 'vidhūpana'})
M['2-177'] = dict(PRIM, **{
 'blood': 'lohitehi', 'chewed': 'khāyita', 'door': 'dvāraṃ', 'drunk': 'pīta', 'ear': 'kaṇṇa', 'eaten': 'asita',
 'elements': 'bhūtehi', 'external space': 'bāhirā ākāsa', 'external space element': 'bāhirā ākāsadhātu',
 'flesh': 'maṃsa', 'gap': 'vivaragataṃ', 'great elements': 'mahābhūtehi', 'hollow': 'aghagataṃ',
 'internal space': 'ajjhattikā ākāsa', 'internal space element': 'ajjhattikā ākāsadhātu', 'mouth': 'mukha',
 'nose': 'nāsa', 'opening': 'vivaro', 'passes': 'nikkhamati', 'space': 'ākāso', 'space element': 'ākāsadhātu',
 'spatial': 'ākāsagataṃ', 'stays': 'santiṭṭhati', 'swallows': 'ajjhoharati', 'tasted': 'sāyitaṃ',
 'touched': 'asamphuṭṭhaṃ', 'void': 'aghaṃ'})
M['2-178'] = {
 'body-consciousness': 'kāyaviññāṇa', 'body-consciousness element': 'kāyaviññāṇadhātu', 'consciousness': 'viññāṇa',
 'consciousness element': 'viññāṇadhātu', 'ear-consciousness': 'sotaviññāṇa',
 'ear-consciousness element': 'sotaviññāṇadhātu', 'element': 'dhātu', 'elements': 'dhātuyo',
 'eye-consciousness': 'Cakkhuviññāṇa', 'eye-consciousness element': 'Cakkhuviññāṇadhātu',
 'mind-consciousness': 'manoviññāṇa', 'mind-consciousness element': 'manoviññāṇadhātu',
 'nose-consciousness': 'ghānaviññāṇa', 'nose-consciousness element': 'ghānaviññāṇadhātu', 'therein': 'Tattha',
 'tongue-consciousness': 'jivhāviññāṇa', 'tongue-consciousness element': 'jivhāviññāṇadhātu',
}
M['2-179'] = {
 'element': 'dhātu', 'elements': 'dhātuyo', 'equanimity': 'upekkhā', 'equanimity element': 'upekkhādhātu',
 'gladness': 'somanassa', 'gladness element': 'somanassadhātu', 'ignorance': 'avijjā',
 'ignorance element': 'avijjādhātu', 'pain': 'dukkha', 'pain element': 'dukkhadhātu', 'pleasure': 'sukha',
 'pleasure element': 'sukhadhātu', 'sadness': 'domanassa', 'sadness element': 'domanassadhātu',
}
M['2-180'] = {
 'awakening': 'ananubodho', 'barrier': 'laṅgī', 'bewilderment': 'pamoho', 'bodily': 'kāyikaṃ',
 'body-contact': 'kāyasamphassa', 'born': 'kāyasamphassajaṃ', 'born of body-contact': 'kāyasamphassajaṃ',
 'born of mind-contact': 'cetosamphassajaṃ', 'clear': 'asampajaññaṃ', 'comfort': 'sātaṃ', 'comfortable': 'sātaṃ',
 'complete': 'sammoho', 'comprehending': 'anabhisamayo', 'confusion': 'sammoho', 'delusion': 'moho',
 'directly': 'apaccakkhakammaṃ', 'discernment': 'dummejjhaṃ', 'discomfort': 'asātaṃ', 'element': 'dhātu',
 'elements': 'dhātuyo', 'equanimity': 'upekkhā', 'equanimity element': 'upekkhādhātu', 'evenly': 'asamapekkhanā',
 'experience': 'vedayitaṃ', 'experience born': 'kāyasamphassajaṃ / vedayitaṃ', 'fathoming': 'apariyogāhaṇā',
 'feeling': 'vedanā', 'feeling born': 'kāyasamphassajā / vedanā', 'Feeling born': 'kāyasamphassajā / vedanā',
 'flood': 'ogho', 'foolishness': 'bālyaṃ', 'fully': 'asambodho', 'gladness': 'somanassa',
 'gladness element': 'somanassadhātu', 'grasping': 'asaṅgāhaṇā', 'ignorance': 'avijjā',
 'ignorance element': 'avijjādhātu', 'knowing': 'aññāṇaṃ', 'lack': 'asampajaññaṃ', 'Lack of clear': 'asampajaññaṃ',
 'lack of clear': 'asampajaññaṃ', 'mental': 'cetasikaṃ', 'mental comfort': 'cetasikaṃ sātaṃ',
 'Mental comfort': 'cetasikaṃ sātaṃ', 'mental discomfort': 'cetasikaṃ asātaṃ', 'mental pain': 'cetasikaṃ dukkhaṃ',
 'mentally': 'cetasikaṃ', 'mind-contact': 'cetosamphassa', 'obsession': 'pariyuṭṭhānaṃ', 'pain': 'dukkhaṃ',
 'pain element': 'dukkhadhātu', 'painful': 'dukkhaṃ', 'painful experience': 'dukkhaṃ vedayitaṃ',
 'painful experience born': 'kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ', 'painful feeling': 'dukkhā vedanā',
 'painful feeling born': 'kāyasamphassajā asātā dukkhā vedanā', 'painful nor pleasant': 'adukkhamasukhaṃ',
 'penetrating': 'appaṭivedho', 'pleasant': 'sukhaṃ', 'pleasant feeling': 'sukhā vedanā', 'pleasure': 'sukhaṃ',
 'pleasure element': 'sukhadhātu', 'poor': 'dummejjhaṃ', 'reflecting': 'apaccavekkhaṇā', 'root': 'mūlaṃ',
 'sadness': 'domanassa', 'sadness element': 'domanassadhātu', 'seeing': 'adassanaṃ', 'tendency': 'ānusayo',
 'therein': 'Tattha', 'uncomfortable': 'asātaṃ', 'underlying': 'ānusayo', 'underlying tendency': 'ānusayo',
 'understanding': 'asampajaññaṃ', 'unwholesome': 'akusala', 'weighing': 'asamapekkhanā', 'yoke': 'yogo',
}
M['2-181'] = {
 'cruelty': 'vihiṃsā', 'desire': 'kāma', 'element': 'dhātu', 'element of cruelty': 'vihiṃsādhātu',
 'element of goodwill': 'abyāpādadhātu', 'element of harmlessness': 'avihiṃsādhātu', 'element of ill': 'byāpādadhātu',
 'element of renunciation': 'nekkhammadhātu', 'element of sense': 'kāmadhātu', 'elements': 'dhātuyo',
 'goodwill': 'abyāpāda', 'harmlessness': 'avihiṃsā', 'ill': 'byāpāda', 'renunciation': 'nekkhamma', 'sense': 'kāma',
 'sense desire': 'kāma',
}
M['2-182'] = {
 'act': 'mettāyanā', 'aggregates': 'khandha', 'anger': 'kopo', 'angry': 'kujjhanā', 'attacking': 'ūpaghāto',
 'beings': 'sattesu', 'classification': 'bhājanīyaṃ', 'clod': 'leḍḍunā', 'compassion': 'karuṇā',
 'connected': 'paṭisaṃyutto', 'connected with sense': 'Kāmapaṭisaṃyutto', 'consciousness': 'viññāṇaṃ',
 'creations': 'nimmita', 'cruelty': 'vihiṃsā', 'desire': 'kāma', 'directing': 'abhiniropanā',
 'discourses': 'Suttanta', 'displeasure': 'anattamanatā', 'eighteen': 'aṭṭhārasa',
 'eighteen elements': 'aṭṭhārasa dhātuyo', 'element': 'dhātu', 'element of cruelty': 'vihiṃsādhātu',
 'element of goodwill': 'abyāpādadhātu', 'element of harmlessness': 'avihiṃsādhātu', 'element of ill': 'byāpādadhātu',
 'element of renunciation': 'nekkhammadhātu', 'element of sense': 'kāmadhātu', 'elements': 'dhātuyo',
 'feeling': 'vedanā', 'ferocity': 'caṇḍikkaṃ', 'finished': NDE, 'fixing': 'appanā', 'focusing': 'byappanā',
 'form': 'rūpā', 'formations': 'saṅkhārā', 'fury': 'sampakopo', 'gathered': 'abhisaññūhitvā', 'gods': 'deve',
 'gods who wield': 'vasavattī deve', 'goodwill': 'abyāpāda', 'grounds': 'vatthūsu', 'grouped': 'abhisaṅkhipitvā',
 'hand': 'pāṇinā', 'harassing': 'viheṭhanā', 'harmlessness': 'avihiṃsā', 'harms': 'viheṭheti',
 'harshness': 'asuropo', 'hating': 'dussanā', 'hatred': 'doso', 'hell': 'nirayaṃ', 'hostility': 'paṭighāto',
 'hurting': 'hiṃsanā', 'ill': 'byāpāda', 'indeed': NDE, 'injuring': 'vihiṃsanā', 'intention': 'saṅkappo',
 'irritation': 'āghāto', 'knife': 'satthena', 'liberation': 'vimutti', 'liberation of mind': 'cetovimutti',
 'limit': 'pariyantaṃ', 'living': 'sattesu', 'loving': 'mettāyanā', 'loving-kindness': 'metti',
 'malice': 'sampadoso', 'material': 'rūpā', 'material form': 'rūpā', 'mental': 'manopadoso',
 'Mental Formations': 'saṅkhārā', 'mental formations': 'saṅkhārā', 'mind': 'cittassa',
 'mind through compassion': 'karuṇācetovimutti', 'mind through loving-kindness': 'mettācetovimutti',
 'moves': 'āvacarā', 'opposition': 'paṭivirodho', 'others': 'parūpaghāto', 'perception': 'saññā',
 'power': 'vasavattī', 'provoking': 'rosanā', 'rage': 'pakopo', 'renunciation': 'nekkhamma',
 'resentment': 'manopadoso', 'resistance': 'paṭighaṃ', 'right': 'sammā', 'rope': 'rajjuyā',
 'sense': 'kāma', 'sense desire': 'kāma', 'sense-fields': 'āyatanā', 'someone': 'ekacco',
 'state of compassion': 'karuṇāyitattaṃ', 'stick': 'daṇḍena', 'taking': 'karitvā', 'ten': 'Dasasu',
 'ten grounds': 'Dasasu / vatthūsu', 'therein': 'Tattha', 'thing': 'aññataraññatarena', 'thinking': 'takko',
 'thought': 'vitakko', 'together': 'tadekajjhaṃ', 'tormenting': 'heṭhanā', 'towards': NDE, 'upper': 'uparito',
 'vexation': 'byāpatti', 'vexed': 'byāpajjanā', 'whatever': 'yaṃ', 'wholesome': 'kusalā',
 'wholesome states': 'kusalā dhammā', 'wield': 'vasavattī', 'wrong': 'micchā', 'wrong intention': 'micchāsaṅkappo',
}
M['2-3-2-0'] = {'abhidhamma': 'Abhidhamma', 'classification': 'bhājanīyaṃ'}
M['2-183'] = dict(LIST18, **{'eighteen': 'Aṭṭhārasa', 'eighteen elements': 'Aṭṭhārasa dhātuyo'})
M['2-184'] = {
 'abhidhamma': 'Abhidhamma', 'activity': 'mānasaṃ', 'aggregate': 'khandho',
 'aggregate of consciousness': 'viññāṇakkhandho', 'Aggregate of Consciousness': 'viññāṇakkhandho',
 'aggregate of feeling': 'vedanākkhandho', 'aggregate of mental': 'saṅkhārakkhandho',
 'Aggregate of Mental': 'saṅkhārakkhandho', 'aggregate of perception': 'saññākkhandho',
 'Aggregate of Perception': 'saññākkhandho', 'arises': 'uppajjati', 'arises mind': 'uppajjati cittaṃ',
 'arising': 'uppajjitvā', 'attention': 'samannāhāro', 'body': 'kāyo', 'body element': 'kāyadhātu',
 'body-consciousness': 'kāyaviññāṇa', 'body-consciousness element': 'kāyaviññāṇadhātu', 'bright': 'paṇḍaraṃ',
 'cause': 'hetuko', 'causes': 'hetu', 'ceasing': 'niruddha', 'class': 'vidhena', 'classification': 'bhājanīyaṃ',
 'classified': 'bahuvidhena', 'colour': 'vaṇṇa', 'consciousness': 'viññāṇaṃ', 'consciousness element': 'viññāṇadhātu',
 'contact': 'phassa', 'corresponding': 'tajjā', 'delusion': 'moha', 'depending': 'paṭicca', 'derived': 'upādāya',
 'desire': 'Rāga', 'ear': 'sotaṃ', 'ear element': 'sotadhātu', 'ear-consciousness': 'sotaviññāṇa',
 'ear-consciousness element': 'sotaviññāṇadhātu', 'earth': 'Pathavī', 'earth element': 'Pathavīdhātu',
 'element': 'dhātu', 'element of mental': 'dhammadhātu', 'element of sights': 'rūpadhātu',
 'element of smells': 'gandhadhātu', 'element of sounds': 'saddadhātu', 'element of tastes': 'rasadhātu',
 'element of things': 'phoṭṭhabbadhātu', 'element there arises': 'dhātuyā / uppajjati', 'elements': 'bhūtānaṃ',
 'empty': 'suñño', 'eye': 'cakkhu', 'eye element': 'cakkhudhātu', 'eye-consciousness': 'cakkhuviññāṇa',
 'eye-consciousness element': 'cakkhuviññāṇadhātu', 'faculty': 'indriyaṃ', 'faculty of femininity': 'Itthindriyaṃ',
 'feeling': 'vedanā', 'feeling is classified': 'bahuvidhena vedanākkhandho', 'femininity': 'Itthindriyaṃ',
 'finished': NDE, 'food': 'āhāro', 'form': 'rūpaṃ', 'formations': 'saṅkhāra',
 'formations is classified': 'bahuvidhena saṅkhārakkhandho', 'great elements': 'mahābhūtānaṃ', 'hatred': 'dosa',
 'heart': 'hadayaṃ', 'immediately': 'samanantarā', 'invisible': 'anidassano',
 'invisible and offering': 'anidassano sappaṭigho', 'invisible and offers': 'anidassanaappaṭighaṃ',
 'joined': 'sampayutto', 'joined with contact': 'phassasampayutto', 'joined with mind': 'cittasampayutto',
 'material': 'rūpaṃ', 'material form': 'rūpaṃ', 'mental': 'dhammāyatana', 'mental activity': 'mānasaṃ',
 'Mental Formations': 'saṅkhāra', 'mental formations': 'saṅkhāra', 'mental objects': 'dhamme', 'mentality': 'mano',
 'mind': 'cittaṃ', 'mind element': 'manodhātu', 'mind faculty': 'manindriyaṃ', 'mind sense-field': 'manāyatanaṃ',
 'mind-consciousness': 'manoviññāṇa', 'mind-consciousness element': 'manoviññāṇadhātu', 'neutral': 'abyākato',
 'neutral feeling': 'abyākato', 'neutral formations': 'abyākato', 'neutral perception': 'abyākato',
 'nose': 'ghānaṃ', 'nose element': 'ghānadhātu', 'nose-consciousness': 'ghānaviññāṇa',
 'nose-consciousness element': 'ghānaviññāṇadhātu', 'object': 'dhammesu', 'objects': 'dhamme',
 'offering': 'sappaṭigho', 'offering resistance': 'sappaṭigho', 'offers': 'appaṭighaṃ', 'perception': 'saññā',
 'perception is classified': 'bahuvidhena saññākkhandho', 'physical': 'kabaḷīkāro', 'resistance': 'sappaṭigho',
 'root': 'hetuko', 'sense-field': 'āyatanaṃ', 'sense-field of mental': 'dhammāyatana', 'sensitive': 'pasādo',
 'sensitive surface': 'pasādo', 'sensitive surface derived': 'upādāya pasādo', 'shining': 'nibhā', 'sight': 'rūpaṃ',
 'sights': 'rūpe', 'single': 'Ekavidhena', 'single class': 'Ekavidhena', 'smell': 'gandho', 'smells': 'gandhe',
 'sound': 'saddo', 'sounds': 'sadde', 'surface': 'pasādo', 'surface derived': 'upādāya pasādo', 'taste': 'raso',
 'tastes': 'rase', 'ten': 'dasa', 'therein': 'Tattha', 'things': 'phoṭṭhabbe', 'things touched': 'phoṭṭhabbe',
 'threefold': 'Tividhena', 'threefold class': 'Tividhena', 'tongue': 'jivhā', 'tongue element': 'jivhādhātu',
 'tongue-consciousness': 'jivhāviññāṇa', 'tongue-consciousness element': 'jivhāviññāṇadhātu',
 'touched': 'phoṭṭhabbe', 'towards': NDE, 'turning': 'samannāhāro', 'twofold': 'Duvidhena',
 'twofold class': 'Duvidhena', 'unconditioned': 'asaṅkhatā', 'unconditioned element': 'asaṅkhatā dhātu',
 'unwholesome': 'akusalo', 'Unwholesome feeling': 'akusalo', 'unwholesome feeling': 'akusalo',
 'unwholesome formations': 'akusalo', 'Unwholesome formations': 'akusalo', 'Unwholesome perception': 'akusalo',
 'unwholesome perception': 'akusalo', 'village': 'gāmopeso', 'ways': 'bahuvidhena', 'whatever': 'vā pana',
 'wholesome': 'kusalo', 'wholesome feeling': 'kusalo', 'wholesome formations': 'kusalo',
 'wholesome perception': 'kusalo',
}
M['2-3-3-0'] = dict(QA)
M['2-186'] = dict(LIST18, **{
 'conflict': 'saraṇā', 'free': 'araṇā', 'involve': 'saraṇā', 'neutral': 'abyākatā', 'unwholesome': 'akusalā',
 'wholesome': 'kusalā'})
M['2-3-3-1-0'] = {'triads': 'Tikaṃ'}
M['2-187'] = {
 'abandoned': 'pahātabbā', 'able': 'upādāniyā', 'accompanied': 'sahagatā',
 'accompanied by equanimity': 'upekkhāsahagatā', 'accompanied by happiness': 'sukhasahagatā',
 'accompanied by joy': 'pītisahagatā', 'accumulation': 'ācaya', 'arise': 'uppādino', 'arisen': 'uppannā',
 'belong': NDE, 'beyond': 'asekkhā', 'birth': NDE, 'body-consciousness': 'Kāyaviññāṇa',
 'body-consciousness element': 'Kāyaviññāṇadhātu', 'bound': 'uppādino', 'cannot': 'na', 'cause': 'hetukā',
 'causes': 'hetukā', 'clung': 'upādāniyā', 'consciousness element': 'viññāṇadhātu', 'defiled': 'saṃkiliṭṭha',
 'defilement': 'saṃkilesikā', 'describable': 'vattabbā', 'described': 'vattabbā', 'dismantling': 'apacaya',
 'dominant': 'ādhipatino', 'dominant factor': 'ādhipatino', 'element': 'dhātu', 'element of mental': 'Dhammadhātu',
 'element of sights': 'Rūpadhātu', 'element of sounds': 'Saddadhātu', 'elements': 'dhātuyo',
 'elements belong': 'dhātuyo', 'elements may belong': 'dhātuyo siyā', 'equanimity': 'upekkhā',
 'examination': 'vicāra', 'expanded': 'mahaggatā', 'expanded object': 'mahaggatārammaṇā', 'external': 'bahiddhā',
 'external object': 'bahiddhārammaṇā', 'factor': 'ādhipatino', 'feeling': 'vedanāya', 'fifteen': 'Pannarasa',
 'Fifteen elements': 'Pannarasa dhātuyo', 'fixed': 'niyatā', 'future object': 'anāgatārammaṇā',
 'happiness': 'sukha', 'having': NDE, 'inferior': 'hīnā', 'internal': 'ajjhattā',
 'internal and external': 'ajjhattabahiddhā', 'internal object': 'ajjhattārammaṇā', 'invisible': 'anidassana',
 'invisible and offer': 'anidassanaappaṭighā', 'joined': 'sampayuttā', 'joined with feeling': 'vedanāya sampayuttā',
 'joined with painful': 'dukkhāya vedanāya sampayuttā', 'joined with pleasant': 'sukhāya vedanāya sampayuttā',
 'joy': 'pīti', 'limited': 'parittā', 'limited object': 'parittārammaṇā', 'measureless': 'appamāṇā',
 'measureless object': 'appamāṇārammaṇā', 'meditative': 'bhāvanāya', 'meditative development': 'bhāvanāya',
 'mental': 'Dhammadhātu', 'mental objects': 'Dhammadhātu', 'middling': 'majjhimā', 'mind': 'Mano',
 'mind element': 'Manodhātu', 'mind-consciousness': 'Manoviññāṇa', 'mind-consciousness element': 'Manoviññāṇadhātu',
 'neutral': 'abyākatā', 'object': 'ārammaṇā', 'object both internal': 'ajjhattabahiddhārammaṇā',
 'objects': 'Dhammadhātu', 'offers': 'sappaṭighā', 'offers resistance': 'sappaṭighā',
 'open to defilement': 'saṃkilesikā', 'outcome': NDE, 'painful': 'dukkhāya', 'painful feeling': 'dukkhāya vedanāya',
 'painful nor pleasant': 'adukkhamasukhāya', 'past object': 'atītārammaṇā', 'path': 'magga', 'pleasant': 'sukhāya',
 'pleasant feeling': 'sukhāya vedanāya', 'present object': 'paccuppannārammaṇā', 'produce': 'vipākadhammadhammā',
 'produces': 'vipākadhammadhammā', 'resistance': 'sappaṭighā',
 'results nor things': 'nevavipākanavipākadhammadhammā', 'rightness': 'sammatta', 'root': 'hetukā',
 'seeing': 'dassanena', 'seventeen': 'Sattarasa', 'Seventeen elements': 'Sattarasa dhātuyo', 'sights': 'Rūpadhātu',
 'sixteen': 'Soḷasa', 'Sixteen elements': 'Soḷasa dhātuyo', 'Sixteen elements belong': 'Soḷasa dhātuyo',
 'something': NDE, 'sounds': 'Saddadhātu', 'superior': 'paṇītā', 'ten': 'Dasa', 'Ten elements': 'Dasa dhātuyo',
 'ten elements': 'Dasa dhātuyo', 'things': 'dhammā', 'thought': 'vitakka',
 'thought and examination': 'savitakkasavicārā', 'trainees': 'sekkhā', 'training': 'asekkhā',
 'undefiled': 'asaṃkiliṭṭha', 'unwholesome': 'akusalā', 'visible': 'sanidassana', 'wholesome': 'kusalā',
 'wrongness': 'micchatta',
}
M['2-3-3-2-0'] = {'pairs': 'Dukaṃ'}
M['2-188'] = dict(QA, **{
 'abandoned': 'pahātabbā', 'able': 'saṃyojaniyā', 'accompanied': 'sahagatā',
 'accompanied by equanimity': 'upekkhāsahagatā', 'accompanied by happiness': 'sukhasahagatā',
 'accompanied by joy': 'pītisahagatā', 'along': 'ānuparivattino', 'analysis': 'vibhaṅgo', 'arise': 'sahabhuno',
 'arising': 'sahabhū', 'belong': NDE, 'beyond': 'uttarā', 'birth': NDE, 'bound': 'saṃyojaniyā', 'cannot': 'na',
 'cause': 'hetu', 'causes': 'hetū', 'clinging': 'upādānā', 'clinging joined': 'upādānā ceva upādānasampayuttā',
 'clung': 'upādāniyā', 'compounded': 'saṅkhatā', 'conflict': 'saraṇā', 'consciousness': NDE,
 'consciousness element': 'viññāṇadhātu', 'defiled': 'saṃkiliṭṭhā', 'defilement': 'saṃkilesikā',
 'defilement joined': 'kileso ceva kilesasampayuttā', 'defilements': 'kilesā',
 'defilements joined': 'kilesā ceva kilesasampayuttā', 'derived': 'upādā', 'describable': 'vattabbā',
 'described': 'vattabbā', 'dissociated': 'vippayuttā', 'dissociated from clinging': 'upādānavippayuttā',
 'dissociated from wrong': 'parāmāsavippayuttā', 'element': 'dhātu', 'element of mental': 'Dhammadhātu',
 'element of sights': 'Rūpadhātu', 'element of sounds': 'Saddadhātu', 'elements': 'dhātuyo',
 'elements are dissociated': 'dhātuyo hetuvippayuttā', 'elements are included': 'dhātuyo pariyāpannā',
 'elements belong': 'dhātuyo', 'elements may belong': 'dhātuyo siyā', 'elements offer': 'dhātuyo sappaṭighā',
 'eleven': 'Ekādasa', 'Eleven elements': 'Ekādasa dhātuyo', 'eleven elements': 'Ekādasa dhātuyo',
 'equanimity': 'upekkhā', 'examination': 'vicārā', 'existence': NDE, 'external': 'bāhirā', 'factor': 'cetasikā',
 'factors': 'cetasikā', 'fetter': 'saṃyojanaṃ', 'fetter joined': 'saṃyojanañceva saṃyojanasampayuttā',
 'fetters': 'saṃyojanā', 'fetters joined': 'saṃyojanā ceva saṃyojanasampayuttā', 'fifteen': 'Pannarasa',
 'Fifteen elements': 'Pannarasa dhātuyo', 'fine-material': 'rūpāvacarā', 'fine-material sphere': 'rūpāvacarā',
 'finished': 'niṭṭhito', 'fixed': 'niyatā', 'floods': 'oghā', 'follow': 'ānuparivattino', 'free': 'araṇā',
 'grasped': 'parāmaṭṭhā', 'grasping': 'parāmāsā', 'happiness': 'sukha', 'having': 'sahetukā',
 'hindrance': 'nīvaraṇaṃ', 'hindrance joined': 'nīvaraṇañceva nīvaraṇasampayuttā', 'hindrances': 'nīvaraṇā',
 'hindrances joined': 'nīvaraṇā ceva nīvaraṇasampayuttā', 'immaterial': 'arūpā',
 'immaterial sphere': 'arūpāvacarā', 'internal': 'ajjhattikā', 'invisible': 'anidassanā', 'involve': 'saraṇā',
 'joined': 'sampayuttā', 'joined with clinging': 'upādānasampayuttā', 'joined with mind': 'cittasampayuttā',
 'joined with root': 'hetusampayuttā', 'joy': 'pīti', 'kinds': NDE, 'kinds of consciousness': 'kenaci',
 'knowable': 'viññeyyā', 'material': 'rūpā', 'meditative': 'bhāvanāya', 'meditative development': 'bhāvanāya',
 'mental': 'Dhammadhātu', 'mental factor': 'cetasikā', 'mental factors': 'cetasikā', 'mental objects': 'Dhammadhātu',
 'mental taints': 'āsavā', 'mind': 'cittā', 'mind element': 'Manodhātu', 'mind-consciousness': 'Manoviññāṇa',
 'mind-consciousness element': 'Manoviññāṇadhātu', 'mingled': 'saṃsaṭṭhā', 'mingled with mind': 'cittasaṃsaṭṭhā',
 'object': 'ārammaṇā', 'objects': 'Dhammadhātu', 'obstructed': 'nīvaraṇiyā', 'open to defilement': 'saṃkilesikā',
 'others': 'kenaci', 'outcome': NDE, 'outside': 'apariyāpannā', 'produced': 'samuṭṭhānā', 'resistance': 'sappaṭighā',
 'root': 'hetu', 'root cause joined': 'hetu ceva hetusampayuttā', 'root causes joined': 'hetū ceva hetusampayuttā',
 'round': NDE, 'seeing': 'dassanena', 'sense': 'kāmāvacarā', 'sense sphere': 'kāmāvacarā', 'seventeen': 'Sattarasa',
 'Seventeen elements': 'Sattarasa dhātuyo', 'sights': 'Rūpadhātu', 'sixteen': 'Soḷasa',
 'Sixteen elements': 'Soḷasa dhātuyo', 'Sixteen elements belong': 'Soḷasa dhātuyo', 'sounds': 'Saddadhātu',
 'sphere': 'āvacarā', 'surpassable': 'sauttarā', 'surpassed': 'sauttarā', 'taint': 'āsavo',
 'taint joined': 'āsavo ceva āsavasampayuttā', 'taints': 'āsavā', 'taints joined': 'āsavā ceva āsavasampayuttā',
 'ten': 'Dasa', 'Ten elements': 'Dasa dhātuyo', 'ten elements': 'Dasa dhātuyo', 'thought': 'vitakkā',
 'tie': 'gantho', 'tie joined': 'gantho ceva ganthasampayuttā', 'tied': 'ganthaniyā', 'ties': 'ganthā',
 'ties joined': 'ganthā ceva ganthasampayuttā', 'together': 'saha', 'twelve': 'Dvādasa',
 'Twelve elements': 'Dvādasa dhātuyo', 'unable': 'asaṃyojaniyā', 'uncompounded': 'asaṅkhatā',
 'undefiled': 'asaṃkiliṭṭhā', 'unsurpassable': 'anuttarā', 'visible': 'sanidassanā', 'worldly': 'lokiyā',
 'wrong': 'parāmāsā', 'wrong grasping': 'parāmāsā', 'wrongly': 'parāmaṭṭhā', 'wrongly grasped': 'parāmaṭṭhā',
 'yokes': 'yogā',
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
