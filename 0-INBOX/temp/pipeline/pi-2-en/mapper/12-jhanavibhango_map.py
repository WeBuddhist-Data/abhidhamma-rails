import pathlib
d = pathlib.Path(__file__).parent
ch = '12-jhanavibhango'
NDE = '(no direct equivalent)'

# first-to-fourth jhāna formula (shared by 2-508 and the jhāna segments later on)
JHANA = {
 'abandoning': 'pahānā', 'abandoning of happiness': 'sukhassa ca pahānā', 'absorption': 'jhānaṃ', 'away': 'virāgā',
 'born': 'vivekajaṃ', 'clearly': 'sampajāno', 'comprehending': 'sampajāno', 'concentration': 'samādhi',
 'confidence': 'sampasādanaṃ', 'declare': 'ācikkhanti', 'disappearance': 'atthaṅgamā', 'dwells': 'viharati',
 'dwells happily': 'sukhavihārī', 'enters': 'upasampajja', 'enters and dwells': 'upasampajja viharati',
 'equanimity': 'upekkhā', 'equanimous': 'upekkhako', 'examination': 'vicāraṃ', 'experiences': 'paṭisaṃvedeti',
 'experiences happiness': 'sukhañca / paṭisaṃvedeti', 'fading': 'virāgā', 'fourth meditative': 'catutthaṃ jhānaṃ',
 'fourth meditative absorption': 'catutthaṃ jhānaṃ', 'grief': 'domanassānaṃ', 'happily': 'sukhavihārī',
 'happiness': 'sukhaṃ', 'inner': 'ajjhattaṃ', 'joy': 'pīti', 'Joy and happiness': 'pītisukhaṃ', 'meditative': 'jhānaṃ',
 'Meditative absorption': 'jhānaṃ', 'meditative absorption': 'jhānaṃ', 'mindful': 'sato', 'noble': 'ariyā',
 'ones': 'ariyā', 'pain': 'dukkhassa', 'painful': 'adukkhamasukhaṃ', 'painful nor pleasant': 'adukkhamasukhaṃ',
 'pleasant': 'adukkhamasukhaṃ', 'pleasures': 'kāmehi', 'purity': 'pārisuddhiṃ', 'secluded': 'vivicca',
 'secluded from sense': 'vivicceva kāmehi', 'seclusion': 'viveka', 'sense': 'kāmehi', 'sense pleasures': 'kāmehi',
 'stilling': 'vūpasamā', 'stilling of thought': 'vitakkavicārānaṃ vūpasamā', 'thought': 'vitakkaṃ',
 'thought and examination': 'vitakkavicārānaṃ', 'unification': 'ekodibhāvaṃ', 'unwholesome': 'akusalehi',
 'unwholesome things': 'akusalehi dhammehi',
}
# clear-comprehension list (2-508, 2-523, 2-525)
SAMPAJ = {
 'ahead': 'ālokite', 'away': 'vilokite', 'bending': 'samiñjite', 'bowl': 'patta', 'carrying': 'dhāraṇe',
 'chewing': 'khāyite', 'defecating': 'uccāra', 'drinking': 'pīte', 'eating': 'asite', 'forward': 'abhikkante',
 'going': 'abhikkante', 'keeping': 'tuṇhībhāve', 'looking': 'ālokite', 'outer': 'saṅghāṭi', 'returning': 'paṭikkante',
 'robe': 'saṅghāṭi', 'robes': 'cīvara', 'silent': 'tuṇhī', 'sitting': 'nisinne', 'sleeping': 'sutte',
 'speaking': 'bhāsite', 'standing': 'ṭhite', 'stretching': 'pasārite', 'tasting': 'sāyite', 'urinating': 'passāva',
 'waking': 'jāgarite', 'walking': 'gate', 'acts': 'sampajānakārī', 'acts with clear': 'sampajānakārī',
 'act': 'sampajānakārī', 'act with clear': 'sampajānakārī', 'clear': 'sampajāna', 'clear comprehension': 'sampajāna',
 'comprehension': 'sampajāna', 'clearly': 'sampajāno', 'comprehending': 'sampajāno', 'mindful': 'sato',
 'acts mindful': 'sato sampajānakārī', 'goes': 'abhikkamati', 'returns': 'paṭikkamati', 'looks': 'āloketi',
 'bends': 'samiñjeti', 'stretches': 'pasāreti', 'monk': 'bhikkhu',
}
DWELLS = {'carries': 'yāpeti', 'conducts': 'carati', 'dwells': 'viharati', 'goes': 'vattati', 'going': 'pāleti',
          'himself': NDE, 'keeps': 'pāleti', 'maintains': 'yapeti', 'moves': 'iriyati', 'therefore': 'Tena'}

M = {}
M['2-12-0'] = {'absorption': 'Jhāna', 'analysis': 'vibhaṅgo', 'meditative': 'Jhāna', 'Meditative absorption': 'Jhāna',
               'meditative absorption': 'Jhāna'}
M['2-12-1-0'] = {'classification': 'bhājanīyaṃ', 'discourses': 'Suttanta'}
M['2-508'] = dict(JHANA)
M['2-508'].update(SAMPAJ)
M['2-508'].update({
 'abandoned': 'pahāya', 'abandoned doubt': 'Vicikicchaṃ pahāya', 'abandoned dullness': 'Thinamiddhaṃ pahāya',
 'abandoned restlessness': 'Uddhaccakukkuccaṃ pahāya', 'air': 'abbhokāsaṃ', 'attending': 'amanasikārā',
 'awakening': 'bodhi', 'aware': NDE, 'beings': 'bhūta', 'beyond': 'samatikkamā', 'body': 'kāyaṃ',
 'breath': 'vātaṃ', 'care': 'nepakkaṃ', 'cave': 'guhaṃ', 'charnel': 'susānaṃ', 'code': 'pātimokkha',
 'compassionate': 'ānukampī', 'completely': 'sabbaso', 'Completely passing': 'sabbaso / samatikkamā',
 'completely passing': 'sabbaso / samatikkamma', 'conduct': 'ācāra', 'consciousness': 'viññāṇa',
 'corruptions': 'upakkilese', 'covetousness': 'abhijjhaṃ', 'crossed': 'tiṇṇa', 'crosswise': 'pallaṅkaṃ',
 'crowds': 'vijanavātaṃ', 'danger': 'bhaya', 'devoted': 'anuyutto', 'diversity': 'nānatta', 'doors': 'dvāro',
 'doubt': 'Vicikicchaṃ', 'drowsiness': 'middhaṃ', 'dullness': 'Thina', 'dullness and drowsiness': 'Thinamiddhaṃ',
 'dwelling': 'senāsanaṃ', 'dwelling place': 'senāsanaṃ', 'empty': 'suññāgāragato', 'endowed': 'sampanno',
 'established': 'upaṭṭhapetvā', 'faculties': 'indriyesu', 'faults': 'vajjesu', 'field': 'āyatanaṃ',
 'field of infinite': 'ākāsānañcāyatanaṃ', 'field of nothingness': 'ākiñcaññāyatanaṃ', 'folded': 'ābhujitvā',
 'food': 'bhojane', 'foot': 'mūlaṃ', 'forest': 'araññaṃ', 'form': 'rūpa', 'free': 'vigatābhijjhena',
 'front': 'parimukhaṃ', 'glen': 'kandaraṃ', 'gone': 'gato', 'ground': 'susānaṃ', 'guards': 'gutta',
 'hatred': 'padosaṃ', 'having': NDE, 'heap': 'puñjaṃ', 'hidden': 'rāhasseyyakaṃ', 'himself': NDE,
 'hindrances': 'nīvaraṇe', 'hut': 'āgāra', 'ill': 'Byāpāda', 'infinite': 'ananto',
 'infinite consciousness': 'viññāṇañcāyatanaṃ', 'infinite space': 'ākāsānañcāyatanaṃ', 'inwardly': 'ajjhattaṃ',
 'knows': 'mattaññū', 'legs': 'pallaṅkaṃ', 'light': 'āloka', 'living': 'pāṇa', 'material': 'rūpa',
 'material form': 'rūpa', 'mind': 'cetasā', 'mind free': 'vigatābhijjhena cetasā', 'mindfulness': 'satiṃ',
 'moderation': 'mattaññū', 'moderation in food': 'bhojane mattaññū', 'monastic': 'pātimokkha',
 'monk dwells': 'bhikkhu / viharati', 'mountain': 'pabbataṃ',
 'neither-perception-nor-non-perception': 'nevasaññānāsaññāyatanaṃ', 'night': 'pubbarattāpararattaṃ',
 'noise': 'nigghosaṃ', 'nothing': 'natthi kiñcī', 'nothingness': 'ākiñcaññāyatanaṃ',
 'parts': 'pubbarattāpararattaṃ', 'passing': 'samatikkamā', 'people': 'manussa', 'perceptions': 'saññānaṃ',
 'perceptions of diversity': 'nānattasaññānaṃ', 'perceptions of material': 'rūpasaññānaṃ',
 'perceptions of resistance': 'paṭighasaññānaṃ', 'percipient': 'saññī', 'perplexity': 'akathaṃkathī',
 'perseverance': 'sātaccaṃ', 'place': 'senāsanaṃ', 'proper': NDE, 'proper conduct': 'ācāra',
 'proper resort': 'gocara', 'purifies': 'parisodheti', 'purifies his mind': 'cittaṃ parisodheti', 'regard': 'loke',
 'remorse': 'kukkuccaṃ', 'remote': 'patthaṃ', 'Remote forest': 'vanapatthaṃ', 'resistance': 'paṭigha',
 'resort': 'gocara', 'resorts': 'bhajati', 'restlessness': 'Uddhacca', 'restlessness and remorse': 'Uddhaccakukkuccaṃ',
 'restrained': 'saṃvuto', 'restraint': 'saṃvara', 'retreat': 'paṭisallāna', 'rules': 'padesu',
 'secluded': 'vivittaṃ', 'secluded dwelling': 'vivittaṃ senāsanaṃ', 'secluded dwelling place': 'vivittaṃ senāsanaṃ',
 'seeing': 'dassāvī', 'side': 'pakkhikānaṃ', 'side with awakening': 'bodhipakkhikānaṃ', 'sits': 'nisīdati',
 'slightest': 'aṇumattesu', 'slightest faults': 'aṇumattesu vajjesu', 'sound': 'saddaṃ', 'space': 'ākāso',
 'stilled': 'vūpasanta', 'straight': 'ujuṃ', 'straw': 'palāla', 'suitable': 'sāruppaṃ', 'things': 'dhammānaṃ',
 'things that side': 'bodhipakkhikānaṃ dhammānaṃ', 'training': 'sikkhā', 'trains': 'sikkhati', 'tree': 'rukkha',
 'unagitated': 'anuddhato', 'undertaken': 'samādāya', 'wakefulness': 'jāgariyānuyogamanuyutto',
 'weaken': 'dubbalīkaraṇe', 'welfare': 'hitānukampī', 'wholesome': 'kusalesu', 'wholesome things': 'kusalesu dhammesu',
 'wisdom': 'paññāya',
})
M['2-12-1-1-0'] = {'matrix': 'Mātikā'}
M['2-509'] = {
 'acceptance': 'khantiyā', 'discipline': 'vinaye', 'dispensation': 'sāsane', 'doctrine': 'pāvacane',
 'holy': 'brahmacariye', 'holy life': 'brahmacariye', 'life': 'cariye', 'preference': 'ruciyā', 'taking-up': 'ādāye',
 'teacher': 'satthu', 'teaching': 'dhamme', 'teaching-and-discipline': 'dhammavinaye', 'therefore': 'Tena',
 'view': 'diṭṭhiyā',
}
M['2-510'] = {
 'abandoning': 'pahānā', 'acknowledgement': 'paṭiññāya', 'act': 'kammena', 'announcements': 'ñatticatutthena',
 'beggar': 'bhikkhakoti', 'begging': 'bhikkhā', 'begs': 'bhikkhatīti', 'beyond': 'asekkho', 'breaks': 'bhindati',
 'broken': 'bhinnattā', 'cloth': 'paṭa', 'complete': 'anodhiso', 'defilements': 'kilesānaṃ', 'designation': 'samaññāya',
 'evil': 'pāpakānaṃ', 'excellent': 'bhadro', 'fit': 'ārahena', 'foremost': 'aggo', 'fully': 'upasampanno',
 'life': 'cariyaṃ', 'monk': 'bhikkhu', 'motion': 'ñatti', 'ordained': 'upasampanno', 'order': 'saṅghena',
 'partial': 'odhiso', 'patched': 'bhinna', 'stand': 'ṭhānārahena', 'substance': 'sāro', 'things': 'dhammānaṃ',
 'training': 'sekkho', 'united Order': 'samaggena saṅghena', 'unshakeable': 'akuppena', 'unwholesome': 'akusalānaṃ',
 'unwholesome things': 'akusalānaṃ dhammānaṃ', 'wears': 'dharoti',
}
M['2-511'] = {
 'attainment': 'samāpattiyā', 'beginning': 'ādi', 'body': 'Kāyiko', 'code': 'Pātimokkha', 'complete': 'sampanno',
 'conduct': 'caraṇaṃ', 'endowed': 'upeto', 'foremost': 'pāmokkhaṃ', 'foundation': 'patiṭṭhā', 'fully': 'samupeto',
 'fully endowed': 'samupeto', 'furnished': 'samannāgato', 'having': NDE, 'monastic': 'pātimokkha',
 'non-transgression': 'avītikkamo', 'non-transgression in body': 'Kāyiko avītikkamo', 'possessed': 'upapanno',
 'release': 'mokkhaṃ', 'restrained': 'Saṃvutoti', 'restraint': 'saṃvaro', 'self-control': 'saṃyamo',
 'speech': 'vācasiko', 'therefore': 'Tena', 'thing': NDE, 'things': 'dhammānaṃ', 'virtue': 'sīlaṃ',
 'wholesome': 'kusalānaṃ', 'wholesome things': 'kusalānaṃ dhammānaṃ',
}
M['2-512'] = dict(DWELLS)
M['2-513'] = {
 'bad': 'dussīlyaṃ', 'bad conduct': 'dussīlyaṃ', 'bamboo': 'veḷu', 'bathing': 'sināna', 'body': 'Kāyiko',
 'buddhas': 'buddha', 'carrying': 'pesanikena', 'children': 'pāribhaṭayatāya', 'condemned': 'paṭikuṭṭhena',
 'conduct': 'ācāro', 'endowed': 'sampanno', 'flattery': 'cāṭukamyatāya', 'flowers': 'puppha',
 'fondling': 'pāribhaṭayatāya', 'foot': 'jaṅgha', 'fruits': 'phala', 'giving': 'dānena',
 'half-truthful': 'muggasūpyatāya', 'improper': 'anācāro', 'improper conduct': 'anācāro', 'leaves': 'patta',
 'livelihood': 'ājīvena', 'living': 'jīvikaṃ', 'makes': 'kappeti', 'means': NDE, 'messages': 'pesanikena',
 'non-transgression': 'avītikkamo', 'non-transgression in body': 'Kāyiko avītikkamo', 'proper': NDE,
 'proper conduct': 'ācāro', 'proper resort': 'gocara', 'resort': 'gocara', 'restraint': 'saṃvaro',
 'someone': 'ekacco', 'speech': 'vācasiko', 'supplies': NDE, 'talk': 'muggasūpyatāya', 'therein': 'Tattha',
 'tooth-sticks': 'dantakaṭṭha', 'transgression': 'vītikkamo', 'virtue': 'sīla', 'wrong': 'micchā',
}
M['2-514'] = {
 'abuse': 'akkosaka', 'associating': 'saṃsaṭṭho', 'attends': 'payirupāsati', 'bondage': 'yoga', 'breeze': 'vāta',
 'comfort': 'phāsuka', 'conduct': 'ācārena', 'confidence': 'saddhāni', 'disciples': 'sāvakehi',
 'discomfort': 'aphāsuka', 'dwells': 'viharati', 'endowed': 'upeto', 'eunuchs': 'paṇḍaka', 'families': 'kulāni',
 'fanned': 'paṭivātāni', 'frequent': 'gocaro', 'frequents': 'gocaro', 'furnished': 'samannāgato', 'grown-up': 'thulla',
 'harm': 'anattha', 'ill': 'ahita', 'improper': 'agocaro', 'improper resort': 'agocaro', 'king': 'rāja',
 'kings': 'rājūhi', 'laymen': 'upāsakānaṃ', 'laywomen': 'upāsikānaṃ', 'like': 'bhūtāni', 'ministers': 'mahāmattehi',
 'monks': 'bhikkhūnaṃ', 'nuns': 'bhikkhunīnaṃ', 'ochre': 'kāsāva', 'proper': NDE, 'proper conduct': 'ācārena',
 'proper resort': 'gocarena', 'prostitutes': 'vesiyā', 'resort': 'gocaro', 'resorts': 'sevati',
 'revile': 'paribhāsakāni', 'robe': 'kāsāva', 'sages': 'isi', 'sects': 'titthiyehi', 'security': 'khema',
 'shine': 'pajjotāni', 'someone': 'ekacco', 'taverns': 'pānāgāra', 'teachers': 'titthiyehi', 'therefore': 'Tena',
 'therein': 'Tattha', 'unmarried': 'kumāri', 'unsuitable': 'ananulomikena', 'welfare': 'hita', 'widows': 'vidhavā',
 'wish': 'kāmāni', 'women': 'kumāri',
}
M['2-515'] = {
 'arising': 'uppāda', 'attentiveness': 'manasikāra', 'bound': 'paṭibaddhāni', 'considered': 'sammatāni',
 'dealt': 'karaṇīyāni', 'danger': 'bhaya', 'drawback': 'ādīnava', 'escape': 'nissaraṇa', 'fault': 'vajja',
 'faults': 'vajjesu', 'light': 'lahusāni', 'mind': 'cittuppādakaraṇīyāni', 'minor': 'oramattakāni',
 'restraint': 'saṃvara', 'right': NDE, 'seeing': 'dassāvī', 'self-control': 'saṃyama', 'slight': 'appamattakāni',
 'slightest': 'aṇumattesu', 'slightest faults': 'aṇumattesu vajjesu', 'therefore': 'Tena', 'therein': 'tattha',
}
M['2-516'] = {
 'completely': 'sabbena sabbaṃ', 'every': 'sabbathā', 'fully': 'asesaṃ', 'having': NDE, 'himself': NDE,
 'laymen': 'upāsakānaṃ', 'laywomen': 'upāsikānaṃ', 'monks': 'bhikkhūnaṃ', 'nuns': 'bhikkhunīnaṃ',
 'proceeds': 'vattati', 'remainder': 'nissesaṃ', 'respect': NDE, 'rules': 'padesū', 'therefore': 'Tena',
 'therein': 'tattha', 'training': 'sikkhā', 'trainings': 'sikkhāyo', 'trains': 'sikkhati', 'undertaken': 'Samādāya',
}
M['2-517'] = {
 'body': 'kāyena', 'covetousness': 'abhijjhā', 'covetousness and grief': 'abhijjhādomanassā', 'doors': 'dvāro',
 'dwelt': 'viharantaṃ', 'ear': 'Sotena', 'endowed': 'upeto', 'evil': 'pāpakā', 'eye': 'cakkhunā',
 'eye faculty': 'cakkhundriyaṃ', 'faculties': 'indriyesu', 'faculty': 'indriyaṃ',
 'faculty unrestrained': 'cakkhundriyaṃ asaṃvutaṃ', 'flow': 'anvāssaveyyuṃ', 'fully': 'samupeto',
 'fully endowed': 'samupeto', 'furnished': 'samannāgato', 'grasp': 'gāhī', 'grasps': 'gāhī', 'grief': 'domanassā',
 'guard': 'rakkhati', 'guarding': 'gutti', 'guarding the doors': 'guttadvāratā', 'guards': 'gutta', 'having': NDE,
 'heard': 'sutvā', 'known': 'viññāya', 'lack': 'agutti', 'mental': 'dhammaṃ', 'mental object': 'dhammaṃ',
 'mind': 'manasā', 'mind faculty': 'manindriyaṃ', 'mind faculty unrestrained': 'manindriyaṃ asaṃvutaṃ',
 'nose': 'ghānena', 'object': 'dhammaṃ', 'practise': 'paṭipajjati', 'practises': 'paṭipajjati',
 'protection': 'gopanā', 'restraint': 'saṃvarāya', 'sight': 'rūpaṃ', 'signs': 'nimitta', 'smell': 'gandhaṃ',
 'smelled': 'ghāyitvā', 'someone': 'ekacco', 'sound': 'saddaṃ', 'tangible': 'phoṭṭhabbaṃ',
 'tangible thing': 'phoṭṭhabbaṃ', 'taste': 'rasaṃ', 'tasted': 'sāyitvā', 'therefore': 'Tena', 'therein': 'Tattha',
 'thing': 'phoṭṭhabbaṃ', 'things': 'dhammā', 'tongue': 'jivhāya', 'touched': 'phusitvā', 'undertake': 'āpajjati',
 'undertake restraint': 'saṃvaraṃ āpajjati', 'undertakes': 'āpajjati', 'undertakes restraint': 'saṃvaraṃ āpajjati',
 'unrestrained': 'asaṃvutaṃ', 'unwholesome': 'akusalā', 'unwholesome things': 'akusalā dhammā', 'watching': 'ārakkho',
}
M['2-518'] = {
 'adornment': 'maṇḍanāya', 'amusement': 'davāya', 'beautification': 'vibhūsanāya', 'blameless': 'anavajjatā',
 'body': 'kāyassa', 'comfort': 'phāsu', 'contentment': 'santuṭṭhitā', 'discomfort': 'vihiṃsūparatiyā',
 'dwell': 'vihāro', 'endowed': 'upeto', 'feeling': 'vedanaṃ', 'food': 'bhojane', 'furnished': 'samannāgato',
 'going': 'yātrā', 'holy': 'brahmacariyānuggahāya', 'holy life': 'brahmacariyānuggahāya',
 'intoxication': 'madāya', 'keep': 'yātrā', 'knowing': 'mattaññutā', 'knowing moderation': 'mattaññutā',
 'knows': 'mattaññū', 'lack': 'asantuṭṭhitā', 'life': 'brahmacariyānuggahāya', 'maintenance': 'yāpanāya',
 'moderation': 'mattaññutā', 'moderation in food': 'bhojane mattaññutā', 'old': 'purāṇañca',
 'persistence': 'ṭhitiyā', 'reflection': 'paṭisaṅkhā', 'regard': 'bhojane', 'someone': 'ekacco',
 'supporting': 'ānuggahāya', 'takes': 'āhāreti', 'therefore': 'Tena', 'therein': 'Tattha', 'thinking': 'iti',
 'unwisely': 'ayoniso', 'wisely': 'yoniso',
}
M['2-519'] = {
 'attended': 'manasikaritvā', 'clearly': 'sampajāno', 'comprehending': 'sampajāno',
 'devoted': 'anuyutto', 'foot': 'pāde', 'having': NDE, 'idea': 'saññaṃ', 'lies': 'kappeti', 'lion': 'sīha',
 'middle': 'majjhima', 'mind': 'cittaṃ', 'mind of obstructive': 'āvaraṇīyehi dhammehi cittaṃ', 'mindful': 'sato',
 'monk': 'bhikkhu', 'night': 'rattiyā', 'obstructive': 'āvaraṇīyehi', 'obstructive things': 'āvaraṇīyehi dhammehi',
 'parts': 'pubbarattāpararattaṃ', 'placing': 'accādhāya', 'posture': 'seyyaṃ', 'purifies': 'parisodheti',
 'purifies his mind': 'cittaṃ parisodheti', 'right': 'dakkhiṇena', 'risen': 'paccuṭṭhāya', 'side': 'passena',
 'sitting': 'nisajjāya', 'things': 'dhammehi', 'wakefulness': 'jāgariyānuyogamanuyutto', 'walking': 'caṅkamena',
 'watch': 'yāmaṃ',
}
M['2-520'] = {'effort': 'vāyāmo', 'initiation': 'ārambho', 'initiation of energy': 'vīriyārambho',
              'mental': 'cetasiko', 'mental initiation': 'cetasiko vīriyārambho', 'perseverance': 'Sātacca',
              'right': 'sammā'}
M['2-521'] = {'care': 'Nepakka', 'investigation': 'vicayo', 'investigation of things': 'dhammavicayo',
              'non-delusion': 'amoho', 'right': 'sammā', 'things': 'dhamma', 'understanding': 'pajānanā',
              'view': 'diṭṭhi', 'wisdom': 'paññā'}
M['2-522'] = {
 'awakening': 'bodhi', 'awakening factor': 'sambojjhaṅgo', 'Awakening Factors': 'bojjhaṅgā',
 'awakening factors': 'bojjhaṅgā', 'concentration': 'samādhi', 'cultivates': 'bahulīkaroti', 'develops': 'bhāveti',
 'devoted': 'anuyutto', 'equanimity': 'upekkhā', 'factor': 'aṅgo', 'factor of concentration': 'samādhisambojjhaṅgo',
 'factor of energy': 'vīriyasambojjhaṅgo', 'factor of equanimity': 'upekkhāsambojjhaṅgo',
 'factor of investigation': 'dhammavicayasambojjhaṅgo', 'factor of joy': 'pītisambojjhaṅgo',
 'factor of mindfulness': 'satisambojjhaṅgo', 'factor of tranquillity': 'passaddhisambojjhaṅgo', 'factors': 'aṅgā',
 'investigation': 'vicaya', 'investigation of things': 'dhammavicaya', 'joy': 'pīti', 'mindfulness': 'sati',
 'practises': 'āsevati', 'side': 'pakkhikānaṃ', 'side with awakening': 'bodhipakkhikānaṃ', 'therefore': 'Tena',
 'therein': 'Tattha', 'things': 'dhammānaṃ', 'things that side': 'bodhipakkhikānaṃ dhammānaṃ',
 'tranquillity': 'passaddhi',
}
M['2-523'] = dict(SAMPAJ, **{'monk act': 'bhikkhu / sampajānakārī'})
M['2-524'] = {
 'away': 'apilāpanatā', 'bearing': 'saraṇatā', 'faculty': 'indriyaṃ', 'faculty of mindfulness': 'satindriyaṃ',
 'floating': 'apilāpanatā', 'forgetting': 'asammusanatā', 'keeping': 'dhāraṇatā', 'mind': NDE, 'mindfulness': 'sati',
 'power': 'balaṃ', 'recollection': 'anussati', 'remembering': 'paṭissati', 'right': 'sammā', 'therein': 'Tattha',
}
M['2-525'] = dict(SAMPAJ, **{
 'ahead': 'āloketi', 'away': 'viloketi', 'breadth': 'bhūrī', 'clarification': 'vebhabyā',
 'clear': 'sampajaññaṃ', 'clear comprehension': 'sampajaññaṃ', 'comprehension': 'sampajaññaṃ',
 'cleverness': 'medhā', 'consideration': 'cintā', 'differentiation': 'paccupalakkhaṇā', 'discerning': 'sallakkhaṇā',
 'discrimination': 'upalakkhaṇā', 'endowed': 'upeto', 'erudition': 'paṇḍiccaṃ', 'examination': 'upaparikkhā',
 'faculty': 'indriyaṃ', 'faculty of wisdom': 'paññindriyaṃ', 'forward': 'abhikkamati', 'furnished': 'samannāgato',
 'goad': 'patodo', 'guidance': 'pariṇāyikā', 'insight': 'vipassanā', 'investigation': 'vicayo',
 'investigation of things': 'dhammavicayo', 'jewel': 'ratanaṃ', 'lamp': 'pajjoto', 'light': 'āloko',
 'mindfulness': 'satiyā', 'non-delusion': 'amoho', 'power': 'balaṃ', 'proficiency': 'kosallaṃ',
 'radiance': 'obhāso', 'right': 'sammā', 'subtlety': 'nepuññaṃ', 'sword': 'satthaṃ', 'therein': 'tattha',
 'things': 'dhamma', 'tower': 'pāsādo', 'understanding': 'pajānanā', 'view': 'diṭṭhi', 'wisdom': 'paññā',
})
M['2-526'] = {'away': 'Dūre', 'crowded': 'anākiṇṇaṃ', 'dwelling': 'senāsanaṃ', 'dwelling place': 'senāsanaṃ',
              'householders': 'gahaṭṭhehi', 'nearby': 'santike', 'place': 'senāsanaṃ', 'renunciants': 'pabbajitehi',
              'secluded': 'vivittaṃ'}
M['2-527'] = {
 'bamboo': 'veḷu', 'bed': 'mañcopi', 'cave': 'guhāpi', 'cave-dwelling': 'leṇampi', 'chair': 'pīṭhampi',
 'dwelling': 'senāsanaṃ', 'dwelling place': 'senāsanaṃ', 'foot': 'mūlampi', 'lean-to': 'aḍḍhayogopi',
 'mansion': 'pāsādopi', 'mattress': 'bhisipi', 'monastery': 'vihāropi', 'monks': 'bhikkhū', 'pavilion': 'māḷopi',
 'pillow': 'bibbohanampi', 'place': 'senāsanaṃ', 'retire': 'paṭikkamanti', 'thicket': 'gumbopi', 'tree': 'rukkha',
 'watchtower': 'aṭṭopi', 'wherever': 'Yattha vā pana',
}
M['2-528'] = {'closely': 'nisevati', 'dwelling': 'senāsanaṃ', 'dwelling place': 'senāsanaṃ', 'frequents': 'sevati',
              'fully': 'sambhajati', 'place': 'senāsanaṃ', 'resorts': 'bhajati', 'secluded': 'vivittaṃ',
              'secluded dwelling': 'vivittaṃ senāsanaṃ', 'secluded dwelling place': 'vivittaṃ senāsanaṃ',
              'therefore': 'Tena', 'thoroughly': 'saṃsevati'}
M['2-529'] = {'beyond': 'bahi', 'boundary': 'indakhīlā', 'forest': 'araññaṃ', 'gone': 'nikkhamitvā', 'having': NDE,
              'post': 'indakhīlā'}
M['2-530'] = {'air': 'abbhokāso', 'cave': 'guhā', 'charnel': 'susānaṃ', 'foot': 'mūlaṃ', 'glen': 'kandarā',
              'ground': 'susānaṃ', 'heap': 'puñjo', 'mountain': 'pabbato', 'straw': 'palāla', 'tree': 'rukkha'}
# "stilled, calmed, quieted, gone to rest ... brought to an end" (santā samitā ... byantīkatā)
STILL = {'brought': 'byantīkatā', 'calmed': 'samitā', 'completely': 'abbhatthaṅgatā', 'completely dried': 'visositā',
         'dried': 'sositā', 'extinguished': 'appitā', 'fully': 'byappitā', 'fully extinguished': 'byappitā',
         'gone': 'atthaṅgatā', 'quieted': 'vūpasantā', 'rest': 'atthaṅgatā', 'stilled': 'santā', 'having': NDE,
         'therefore': 'Tena'}
# "the mind, mentality, mental activity ... corresponding mind-consciousness element" (cittaṃ mano mānasaṃ ...)
CITTA = {'activity': 'mānasaṃ', 'consciousness element': 'viññāṇadhātu', 'corresponding': 'tajjā', 'element': 'dhātu',
         'mental': 'mānasaṃ', 'mental activity': 'mānasaṃ', 'mentality': 'mano', 'mind': 'cittaṃ',
         'mind-consciousness': 'manoviññāṇa', 'mind-consciousness element': 'manoviññāṇadhātu', 'therefore': 'Tena',
         'therein': 'Tattha'}
# "cleanses, purifies, thoroughly purifies, frees, releases, fully releases" (sodheti ... parimoceti)
CLEANSE = {'cleanses': 'sodheti', 'frees': 'moceti', 'fully': 'parimoceti', 'fully releases': 'parimoceti',
           'purifies': 'parisodhetī', 'purifies his mind': 'cittaṃ parisodhetī', 'releases': 'vimoceti',
           'thoroughly': 'parisodheti', 'mind': 'cittaṃ', 'therefore': 'Tena', 'therein': 'Tattha'}
# "given up, vomited out, let go, abandoned, relinquished" (cattattā vantattā ...)
GIVEN = {'abandoned': 'pahīnattā', 'let': 'muttattā', 'relinquished': 'paṭinissaṭṭhattā', 'vomited': 'vantattā',
         'therefore': 'Tena'}
VIH = {'dwells': 'Viharatī', 'therefore': 'tena'}
# vitakka / vicāra definitions
VV = {'careful': 'anupekkhanatā', 'connection': 'anusandhanatā', 'consideration': 'anupekkhanatā',
      'continuous': 'anusandhanatā', 'examination': 'vicāro', 'intention': 'saṅkappo', 'mind': 'cittassa',
      'moving': 'cāro', 'right': 'sammā', 'scrutiny': 'upavicāro', 'therefore': 'Tena', 'therein': 'Tattha',
      'thinking': 'takko', 'thought': 'vitakko'}
BORN = {'born': 'jātā', 'brought': 'sañjātā', 'forth': 'sañjātā', 'manifest': 'pātubhūtā', 'produced': 'nibbattā',
        'therefore': 'Tena'}
PITISUKHA = {'accompanied': 'sahagataṃ', 'arisen': 'sahajātaṃ', 'associated': 'sampayuttaṃ',
             'conjoined': 'saṃsaṭṭhaṃ', 'happiness': 'sukhaṃ', 'joy': 'pīti', 'Joy and happiness': 'Pītisukha',
             'therefore': 'Tena', 'therein': 'Tattha', 'together': 'saha'}
ORDER = {'attains': 'samāpajjatīti', 'numerical': 'gaṇanānupubbatā', 'order': 'ānupubbatā'}
UPASAMP = {'absorption': 'jhānassa', 'achievement': 'upasampadā', 'attainment': 'patti', 'enters': 'Upasampajjā',
           'full attainment': 'sampatti', 'gaining': 'lābho', 'meditative': 'jhānassa',
           'Meditative absorption': 'jhānassa', 'meditative absorption': 'jhānassa', 'obtaining': 'paṭilābho',
           'realisation': 'sacchikiriyā', 'touching': 'phusanā'}
JH = {'absorption': 'Jhāna', 'meditative': 'Jhāna', 'Meditative absorption': 'Jhāna', 'meditative absorption': 'Jhāna',
      'mind': 'cittassekaggatā', 'one-pointedness': 'ekaggatā', 'one-pointedness of mind': 'cittassekaggatā'}

M['2-531'] = {
 'designation': 'adhivacanaṃ', 'designation for dwelling': 'senāsanānaṃ adhivacanaṃ', 'distant': 'dūrānametaṃ',
 'distant dwelling places': 'dūrānametaṃ senāsanānaṃ', 'dwelling': 'senāsanānaṃ', 'dwelling places': 'senāsanānaṃ',
 'dwelling places hard': 'durabhisambhavānametaṃ senāsanānaṃ', 'endure': 'durabhisambhavānametaṃ',
 'forest': 'Vanapattha', 'frightening': 'bhīsanakānametaṃ',
 'frightening dwelling places': 'bhīsanakānametaṃ / senāsanānaṃ', 'hair-raising': 'salomahaṃsānametaṃ', 'hair-raising': 'salomahaṃsānametaṃ',
 'hair-raising dwelling places': 'salomahaṃsānametaṃ senāsanānaṃ', 'hard': 'durabhisambhavānametaṃ',
 'human': 'manussūpacārānametaṃ', 'outlying': 'pariyantānametaṃ',
 'outlying dwelling places': 'pariyantānametaṃ senāsanānaṃ', 'places': 'senāsanānaṃ', 'remote': 'pattha',
 'Remote forest': 'Vanapattha', 'thickets': 'vanasaṇḍānametaṃ', 'traffic': 'ūpacārānametaṃ',
}
M['2-532'] = dict(M['2-526'], **{'sound': 'saddaṃ'})
M['2-533'] = {'breath': 'vātaṃ', 'crowds': 'vijanavātaṃ', 'hidden': 'rāhasseyyakaṃ', 'noise': 'nigghosaṃ',
              'people': 'manussa', 'retreat': 'paṭisallāna', 'sound': 'saddaṃ', 'suitable': 'sāruppaṃ'}
M['2-534'] = {'empty': 'suññāgāragato', 'foot': 'mūla', 'forest': 'arañña', 'gone': 'gato', 'hut': 'āgāra',
              'tree': 'rukkha'}
M['2-535'] = {'crosswise': 'pallaṅkaṃ', 'folded': 'ābhujitvā', 'having': NDE, 'legs': 'pallaṅkaṃ',
              'seated': 'nisinno', 'sits': 'Nisīdati'}
M['2-536'] = {'body': 'kāyo', 'directed': 'paṇihito', 'having': NDE, 'placed': 'ṭhito', 'straight': 'Ujuṃ',
              'upright': 'ujuko'}
M['2-537'] = {'established': 'upaṭṭhapetvā', 'front': 'Parimukhaṃ', 'having': NDE, 'mindfulness': 'sati',
              'mouth': 'mukha', 'nose': 'nāsikagge', 'recollection': 'anussati', 'remembering': 'paṭissati',
              'right': 'sammā', 'sign': 'nimitte', 'therefore': 'Tena', 'therein': 'tattha', 'tip': 'agge'}
M['2-538'] = dict(STILL, **{
 'abandoned': 'pahāyā', 'aggregates': 'khandhā', 'clung': 'upādāna', 'covetousness': 'abhijjhā', 'lust': 'rāgo',
 'mind': 'cittassa', 'passion': 'sārāgo', 'regard': 'loke', 'therein': 'tattha'})
M['2-539'] = dict(CITTA, **{'covetousness': 'ābhijjhena', 'free': 'Vigatābhijjhena',
                            'mind free': 'Vigatābhijjhena cetasā', 'therein': 'tattha'})
M['2-540'] = dict(DWELLS)
M['2-541'] = dict(CITTA, **CLEANSE)
M['2-541'].update({'covetousness': 'abhijjhāya', 'lust': 'rāgo', 'passion': 'sārāgo', 'therein': 'tattha'})
M['2-542'] = dict(STILL, **{
 'abandoned': 'pahāyā', 'anger': 'kopo', 'angered': 'pakopo', 'dissatisfaction': 'anattamanatā',
 'fierceness': 'caṇḍikkaṃ', 'hate': 'doso', 'hating': 'dussanā', 'hatred': 'padoso', 'hostility': 'paṭivirodho',
 'ill': 'byāpādo', 'malice': 'byāpatti', 'malicious': 'byāpajjanā', 'mental': 'mano', 'mind': 'cittassa',
 'opposition': 'virodho', 'repugnance': 'paṭighāto', 'resentment': 'āghāto', 'resistance': 'paṭighaṃ',
 'rudeness': 'asuropo', 'therein': 'Tattha', 'wrath': 'kodho', 'wrathful': 'kujjhanā',
 'wrathfulness': 'kujjhitattaṃ'})
M['2-543'] = dict(CITTA, **{'free': 'abyāpannaṃ', 'ill': 'abyāpannaṃ', 'mind free': 'Abyāpannacitto',
                            'therein': 'tattha'})
M['2-544'] = dict(VIH)
M['2-545'] = dict(CITTA, **CLEANSE)
M['2-545'].update({'dissatisfaction': 'anattamanatā', 'fierceness': 'caṇḍikkaṃ', 'hatred': 'padoso',
                   'ill': 'byāpādo', 'resentment': 'āghāto', 'rudeness': 'asuropo'})
M['2-546'] = dict(STILL, **{
 'abandoned': 'pahāyā', 'abandoned dullness': 'Thinamiddhaṃ pahāyā', 'blocked': 'samorodho', 'body': 'kāyassa',
 'covered': 'onāho', 'drowsiness': 'middhaṃ', 'dull': 'thiyanā', 'dullness': 'thinaṃ',
 'dullness and drowsiness': 'Thinamiddhaṃ', 'enveloped': 'pariyonāho', 'inside': 'anto', 'lack': 'akalyatā',
 'mind': 'cittassa', 'nodding': 'pacalāyikā', 'readiness': 'akalyatā', 'sagging': 'olīyanā', 'sleep': 'suppaṃ',
 'sleeping': 'suppanā', 'sloth': 'līnaṃ', 'slothful': 'līyanā', 'slothfulness': 'līyitattaṃ',
 'slumping': 'sallīyanā', 'therein': 'Tattha', 'unworkableness': 'akammaññatā'})
M['2-547'] = dict(GIVEN, **{'drowsiness': 'middhassa', 'dullness': 'thina',
                            'dullness and drowsiness': 'thinamiddhassa', 'free': 'Vigata'})
M['2-548'] = dict(VIH)
M['2-549'] = {'cleansed': 'pariyodātā', 'having': NDE, 'light': 'āloka', 'luminous': 'ālokā',
              'perceived': 'sañjānitattaṃ', 'perceiving': 'sañjānanā', 'perception': 'saññā', 'percipient': 'saññī',
              'purified': 'parisuddhā', 'therefore': 'Tena', 'therein': 'Tattha'}
M['2-550'] = {
 'clear': 'sampajaññaṃ', 'clear comprehension': 'sampajaññaṃ', 'clearly': 'sampajāno', 'comprehending': 'sampajāno',
 'comprehension': 'sampajaññaṃ', 'endowed': 'upeto', 'furnished': 'samannāgato', 'investigation': 'vicayo',
 'investigation of things': 'dhammavicayo', 'mindful': 'Sato', 'mindfulness': 'sati', 'non-delusion': 'amoho',
 'recollection': 'anussati', 'right': 'sammā', 'therefore': 'Tena', 'therein': 'Tattha', 'things': 'dhamma',
 'understanding': 'pajānanā', 'view': 'diṭṭhi', 'wisdom': 'paññā'}
M['2-551'] = dict(CLEANSE, **{'drowsiness': 'middhaṃ', 'dullness': 'thinaṃ', 'dullness and drowsiness': 'thinamiddhā'})
M['2-552'] = dict(STILL, **{
 'abandoned': 'pahāyā', 'abandoned restlessness': 'Uddhaccakukkuccaṃ pahāyā', 'agitation': 'bhantattaṃ',
 'allowable': 'kappiye', 'blameless': 'avajje', 'blameworthy': 'vajje', 'calm': 'avūpasamo',
 'confusion': 'vilekhā', 'distraction': 'vikkhepo', 'kind': 'evarūpaṃ', 'lack': 'avūpasamo',
 'lack of calm': 'avūpasamo', 'mental': 'cetaso', 'mental distraction': 'cetaso vikkhepo', 'mind': 'cittassa',
 'perceiving': 'saññitā', 'regret': 'vippaṭisāro', 'remorse': 'kukkuccaṃ', 'remorseful': 'kukkuccāyanā',
 'restlessness': 'uddhaccaṃ', 'restlessness and remorse': 'Uddhaccakukkuccaṃ', 'therein': 'Tattha',
 'unallowable': 'Akappiye', 'whatever': 'yaṃ'})
M['2-553'] = dict(GIVEN, **{'remorse': 'kukkuccassa', 'restlessness': 'uddhacca',
                            'restlessness and remorse': 'uddhaccakukkuccassa', 'unagitated': 'Anuddhato'})
M['2-554'] = dict(VIH)
M['2-555'] = dict(CITTA, **{'calm': 'samitaṃ', 'inwardly': 'ajjhattaṃ', 'mind stilled': 'Vūpasantacitto',
                            'quieted': 'vūpasantaṃ', 'stilled': 'Vūpasanta'})
M['2-556'] = dict(CLEANSE, **{
 'agitation': 'bhantattaṃ', 'calm': 'avūpasamo', 'distraction': 'vikkhepo', 'lack': 'avūpasamo',
 'lack of calm': 'avūpasamo', 'mental': 'cetaso', 'mental distraction': 'cetaso vikkhepo', 'remorse': 'kukkuccaṃ',
 'restlessness': 'uddhaccaṃ', 'restlessness and remorse': 'uddhaccakukkuccā'})
M['2-557'] = dict(STILL, **{
 'abandoned': 'pahāyā', 'abandoned doubt': 'Vicikicchaṃ pahāyā', 'confusion': 'vilekho',
 'crossroads': 'dvidhāpatho', 'doubt': 'Vicikicchaṃ', 'doubting': 'kaṅkhāyanā', 'failure': 'apariyogāhaṇā',
 'grasping': 'gāho', 'hesitation': 'āsappanā', 'mental': 'mano', 'mind': 'cittassa', 'minds': 'dveḷhakaṃ',
 'perplexity': 'vimati', 'plunge': 'apariyogāhaṇā', 'rigidity': 'chambhitattaṃ', 'sides': 'anekaṃsa',
 'therein': 'tattha', 'uncertainty': 'vicikicchā', 'vacillation': 'parisappanā', 'wavering': 'saṃsayo'})
M['2-558'] = {'beyond': 'nittiṇṇo', 'crossed': 'tiṇṇo', 'doubt': 'vicikicchaṃ', 'gone': 'gato', 'having': NDE,
              'shore': 'pāra', 'therefore': 'Tena'}
M['2-559'] = {'doubt': 'vicikicchāya', 'free': 'nikkathaṃkathī', 'perplexed': 'vicikicchati',
              'perplexity': 'Akathaṃkathī', 'rid': 'vikathaṃkatho', 'therefore': 'Tena', 'things': 'dhammesu',
              'wholesome': 'kusalesu', 'wholesome things': 'kusalesu dhammesu'}
M['2-560'] = dict(CITTA, **CLEANSE)
M['2-560'].update({'confusion': 'vilekho', 'doubt': 'vicikicchā', 'doubting': 'kaṅkhāyanā',
                   'rigidity': 'chambhitattaṃ', 'therein': 'tattha'})
M['2-561'] = dict(STILL, **{'abandoned': 'pahāyā', 'hindrances': 'nīvaraṇe'})
M['2-562'] = {'corruptions': 'upakkilese', 'hindrances': 'nīvaraṇā', 'mind': 'Cetaso'}
M['2-563'] = {'arise': 'uppajjati', 'arisen': 'uppannā', 'ceases': 'nirujjhati', 'hindrances': 'nīvaraṇehi',
              'therefore': 'Tena', 'weaken': 'dubbalīkaraṇe', 'wisdom': 'Paññāya'}
M['2-564'] = {
 'desire': 'Chando', 'desire-and-lust': 'chandarāgo', 'doubt': 'vicikicchā', 'drowsiness': 'middhaṃ',
 'dullness': 'thinaṃ', 'ill': 'byāpādo', 'intention': 'saṅkappo', 'intention-and-lust': 'saṅkapparāgo',
 'lust': 'rāgo', 'pleasure': 'kāmo', 'pleasures': 'kāmehi', 'remorse': 'kukkuccaṃ', 'restlessness': 'uddhaccaṃ',
 'secluded': 'Vivicceva', 'secluded from sense': 'Vivicceva kāmehi', 'sense': 'kāmehi', 'sense desire': 'Kāmacchando',
 'sense pleasure': 'kāmo', 'sense pleasures': 'kāmehi', 'therefore': 'Tena', 'therein': 'tattha', 'things': 'dhammā',
 'unwholesome': 'akusalā', 'unwholesome things': 'akusalā dhammā'}
M['2-565'] = dict(VV, **{'absorption': 'appanā', 'application': 'abhiniropanā', 'called examination': 'vuccati vicāro',
                         'endowed': 'upeto', 'furnished': 'samannāgato', 'mind': 'cetaso'})
M['2-566'] = dict(BORN, **{'examination': 'vicāro', 'happiness': 'sukhaṃ', 'joy': 'pīti', 'mind': 'cittassekaggatā',
                           'one-pointedness': 'ekaggatā', 'one-pointedness of mind': 'cittassekaggatā',
                           'seclusion': 'viveke', 'thought': 'vitakko'})
M['2-567'] = dict(PITISUKHA, **{
 'born': 'cetosamphassajaṃ', 'born of mind-contact': 'cetosamphassajaṃ', 'comfort': 'sātaṃ', 'comfortable': 'sātaṃ',
 'comfortable happy': 'sātaṃ sukhaṃ', 'comfortable happy experience': 'sātaṃ sukhaṃ vedayitaṃ',
 'comfortable happy feeling': 'sātā sukhā vedanā', 'delight': 'pamodanā', 'elation': 'odagyaṃ',
 'experience': 'vedayitaṃ', 'experience born': 'cetosamphassajaṃ / vedayitaṃ', 'feeling': 'vedanā',
 'Feeling born': 'cetosamphassajā / vedanā', 'feeling born': 'cetosamphassajā / vedanā', 'felicity': 'vitti',
 'gladness': 'pāmojjaṃ', 'happy': 'sukhaṃ', 'happy experience': 'sukhaṃ vedayitaṃ',
 'happy experience born': 'cetosamphassajaṃ / sukhaṃ vedayitaṃ', 'happy feeling': 'sukhā vedanā',
 'happy feeling born': 'cetosamphassajā / sukhā vedanā', 'mental': 'cetasikaṃ', 'mental comfort': 'cetasikaṃ sātaṃ',
 'Mental comfort': 'cetasikaṃ sātaṃ', 'mental happiness': 'cetasikaṃ sukhaṃ', 'merriment': 'pahāso',
 'mind': 'cittassa', 'mind-contact': 'cetosamphassa', 'mirth': 'hāso', 'rejoicing': 'āmodanā',
 'satisfaction': 'attamanatā'})
M['2-568'] = dict(ORDER)
M['2-569'] = dict(JH, **{'examination': 'vicāro', 'happiness': 'sukhaṃ', 'joy': 'pīti', 'thought': 'vitakko'})
M['2-570'] = dict(UPASAMP)
M['2-571'] = dict(VIH)
M['2-572'] = dict(STILL, **VV)
M['2-572'].update({'stilling': 'vūpasamā', 'stilling of thought': 'Vitakkavicārānaṃ vūpasamā',
                   'thought and examination': 'Vitakkavicārānaṃ'})
M['2-573'] = {'inner': 'Ajjhatta', 'internal': 'ajjhattaṃ'}
M['2-574'] = {'confidence': 'Sampasādana', 'reliance': 'okappanā', 'trusting': 'saddahanā'}
M['2-575'] = {'concentration': 'samādhi', 'mind': 'Cetaso', 'right': 'sammā', 'steadiness': 'ṭhiti',
              'unification': 'ekodibhāva'}
M['2-576'] = dict(STILL, **VV)
M['2-576'].update({'along': 'anucāro'})
M['2-577'] = dict(BORN, **{'concentration': 'samādhimhi', 'confidence': 'sampasādo', 'happiness': 'sukhaṃ',
                           'joy': 'pīti'})
M['2-578'] = dict(PITISUKHA)
M['2-579'] = dict(ORDER)
M['2-580'] = dict(JH, **{'confidence': 'sampasādo', 'happiness': 'sukhaṃ', 'joy': 'pīti',
                         'Joy and happiness': 'pītisukhaṃ'})
def feel(contact, adj, adj_en):
    """comfortable/happy (and uncomfortable/painful) experience born of <contact>-contact"""
    c, ca = contact + 'samphassajaṃ', contact + 'samphassajā'
    return {
     'born': c, 'comfort': 'sātaṃ', 'comfortable': 'sātaṃ', 'comfortable happy': 'sātaṃ sukhaṃ',
     'comfortable happy experience': 'sātaṃ sukhaṃ vedayitaṃ', 'comfortable happy feeling': 'sātā sukhā vedanā',
     'experience': 'vedayitaṃ', 'experience born': c + ' / vedayitaṃ', 'feeling': 'vedanā',
     'Feeling born': ca + ' / vedanā', 'feeling born': ca + ' / vedanā', 'happiness': 'sukhaṃ', 'happy': 'sukhaṃ',
     'happy experience': 'sukhaṃ vedayitaṃ', 'happy experience born': c + ' / sukhaṃ vedayitaṃ',
     'happy feeling': 'sukhā vedanā', 'happy feeling born': ca + ' / sukhā vedanā',
     adj_en: adj, adj_en + ' comfort': adj + ' sātaṃ', adj_en.capitalize() + ' comfort': adj + ' sātaṃ',
     adj_en + ' happiness': adj + ' sukhaṃ', adj_en + ' discomfort': adj + ' asātaṃ', adj_en + ' pain': adj + ' dukkhaṃ',
     'discomfort': 'asātaṃ', 'pain': 'dukkhaṃ', 'painful': 'dukkhaṃ', 'painful experience': 'dukkhaṃ vedayitaṃ',
     'painful experience born': c + ' / dukkhaṃ vedayitaṃ', 'painful feeling': 'dukkhā vedanā',
     'painful feeling born': ca + ' / dukkhā vedanā', 'uncomfortable': 'asātaṃ',
     'uncomfortable painful': 'asātaṃ dukkhaṃ', 'uncomfortable painful experience': 'asātaṃ dukkhaṃ vedayitaṃ',
     'uncomfortable painful feeling': 'asātā dukkhā vedanā',
    }
CETO = feel('ceto', 'cetasikaṃ', 'mental')
CETO.update({'born of mind-contact': 'cetosamphassajaṃ', 'mind-contact': 'cetosamphassa'})
KAYA = feel('kāya', 'kāyikaṃ', 'bodily')
KAYA.update({'born of body-contact': 'kāyasamphassajaṃ', 'body-contact': 'kāyasamphassa'})
SATI = {'mindfulness': 'sati', 'recollection': 'anussati', 'right': 'sammā'}
UPEKKHA = {'equanimity': 'upekkhā', 'mind': 'cittassa', 'neutrality': 'majjhattatā', 'watching': 'ajjhupekkhanā'}
# mind and mental factors of one who has attained / been reborn / dwells happily in this life
CC = {'attained': 'samāpannassa', 'dwelling': 'vihārissa', 'factors': 'cetasikā', 'happily': 'sukhavihārissa',
      'life': 'diṭṭhadhamma', 'mental': 'cetasikā', 'mental factors': 'cetasikā', 'mind': 'citta',
      'reborn': 'upapannassa'}
PASS = {'beyond': 'samatikkammā', 'completely': 'Sabbaso', 'Completely passing': 'Sabbaso / samatikkammā',
        'completely passing': 'sabbaso / samatikkammā', 'gone': 'samatikkanto', 'passed': 'atikkanto',
        'passing': 'samatikkammā', 'therefore': 'Tena', 'transcended': 'vītikkanto'}
def field(form, keys):
    return {k: form for k in keys}

M['2-581'] = dict(UPASAMP)
M['2-582'] = dict(VIH)
M['2-583'] = dict(STILL, **{'away': 'virāgā', 'fading': 'virāgā', 'delight': 'pamodanā', 'elation': 'odagyaṃ',
                            'felicity': 'vitti', 'gladness': 'pāmojjaṃ', 'joy': 'pīti', 'merriment': 'pahāso',
                            'mind': 'cittassa', 'mirth': 'hāso', 'rejoicing': 'āmodanā',
                            'satisfaction': 'attamanatā', 'therein': 'tattha'})
M['2-584'] = dict(UPEKKHA, **{'endowed': 'upeto', 'equanimous': 'Upekkhako', 'furnished': 'samannāgato',
                              'therefore': 'Tena', 'therein': 'tattha'})
M['2-585'] = dict(VIH)
M['2-586'] = dict(M['2-550'], **{'therein': 'tattha'})
M['2-587'] = dict(CETO, **{
 'aggregate': 'khandho', 'aggregate of consciousness': 'viññāṇakkhandho',
 'Aggregate of Consciousness': 'viññāṇakkhandho', 'aggregate of mental': 'saṅkhārakkhandho',
 'Aggregate of Mental': 'saṅkhārakkhandho', 'Aggregate of Perception': 'Saññākkhandho',
 'aggregate of perception': 'Saññākkhandho', 'body': 'kāyo', 'consciousness': 'viññāṇa',
 'experiences': 'paṭisaṃvedeti', 'experiences happiness': 'Sukhañca / paṭisaṃvedetī', 'formations': 'saṅkhāra',
 'Mental Formations': 'saṅkhāra', 'mental formations': 'saṅkhāra', 'perception': 'Saññā', 'therefore': 'Tena',
 'therein': 'tattha'})
M['2-588'] = {'analyse': 'vibhajanti', 'buddhas': 'buddhā', 'declare': 'ācikkhanti', 'disciples': 'sāvakā',
              'disclose': 'vivaranti', 'establish': 'paṭṭhapenti', 'known': 'paññapenti', 'noble': 'ariyā',
              'ones': 'ariyā', 'plain': 'uttāniṃ', 'proclaim': 'pakāsenti', 'teach': 'desenti', 'therefore': 'Tena',
              'therein': 'tattha'}
M['2-589'] = dict(CETO, **DWELLS)
M['2-589'].update(UPEKKHA)
M['2-589'].update(SATI)
M['2-589'].update({'dwells happily': 'sukhavihārī', 'happily': 'sukhavihārī', 'equanimous': 'Upekkhako',
                   'furnished': 'samannāgato', 'mindful': 'satimā', 'therein': 'tattha'})
M['2-590'] = dict(ORDER)
M['2-591'] = dict(JH, **{'clear': 'sampajaññaṃ', 'clear comprehension': 'sampajaññaṃ',
                         'comprehension': 'sampajaññaṃ', 'equanimity': 'upekkhā', 'happiness': 'sukhaṃ',
                         'mindfulness': 'sati'})
M['2-592'] = dict(UPASAMP)
M['2-593'] = dict(VIH)
M['2-594'] = dict(STILL, **KAYA)
M['2-594'].update({'abandoning': 'pahānā', 'abandoning of happiness': 'Sukhassa ca pahānā', 'therein': 'Tattha'})
M['2-595'] = dict(STILL, **CETO)
M['2-595'].update({'disappearance': 'atthaṅgamā', 'grief': 'domanassaṃ', 'joy': 'somanassaṃ', 'therein': 'Tattha'})
M['2-596'] = {
 'born': 'cetosamphassajaṃ', 'born of mind-contact': 'cetosamphassajaṃ', 'comfortable': 'sātaṃ',
 'experience': 'vedayitaṃ', 'experience born': 'cetosamphassajaṃ / vedayitaṃ', 'feeling': 'vedanā',
 'Feeling born': 'cetosamphassajā / vedanā', 'feeling born': 'cetosamphassajā / vedanā', 'mental': 'cetasikaṃ',
 'mental experience': 'cetasikaṃ', 'mind-contact': 'cetosamphassa', 'neither-painful-nor-pleasant': 'adukkhamasukhaṃ',
 'painful': 'adukkhamasukhaṃ', 'painful nor pleasant': 'adukkhamasukhaṃ', 'pleasant': 'adukkhamasukhaṃ',
 'pleasant feeling': 'adukkhamasukhā vedanā', 'therefore': 'Tena', 'uncomfortable': 'nāsātaṃ'}
M['2-597'] = dict(UPEKKHA, **SATI)
M['2-597'].update({'cleansed': 'pariyodātā', 'equanimous': 'upekkhanā', 'opened': 'vivaṭā', 'purified': 'parisuddhā',
                   'purity': 'pārisuddhi', 'therefore': 'Tena', 'therein': 'tattha'})
M['2-598'] = dict(ORDER)
M['2-599'] = dict(JH, **{'equanimity': 'upekkhā', 'mindfulness': 'sati'})
M['2-600'] = dict(UPASAMP, **{'fourth meditative': 'catutthassa jhānassa',
                              'fourth meditative absorption': 'catutthassa jhānassa'})
M['2-601'] = dict(VIH)
M['2-602'] = dict(PASS, **{
 'beyond': 'samatikkamā', 'Completely passing': 'Sabbaso / samatikkamā', 'completely passing': 'sabbaso / samatikkamā',
 'passing': 'samatikkamā', 'attained': 'samāpannassa', 'attainment': 'samāpattiṃ', 'dwelling': 'vihārissa',
 'fine-material-sphere': 'Rūpāvacara', 'form': 'rūpa', 'happily': 'sukhavihārissa', 'having': NDE,
 'life': 'diṭṭhadhamma', 'material': 'rūpa', 'material form': 'rūpa', 'perceived': 'sañjānitattaṃ',
 'perceiving': 'sañjānanā', 'perception': 'saññā', 'perceptions': 'saññānaṃ',
 'perceptions of material': 'rūpasaññānaṃ', 'reborn': 'upapannassa', 'therein': 'tattha'})
M['2-603'] = dict(STILL, **{
 'called perceptions': 'vuccanti paṭighasaññāyo', 'disappearance': 'atthaṅgamā', 'perception': 'saññā',
 'perceptions': 'saññānaṃ', 'perceptions of resistance': 'Paṭighasaññānaṃ', 'resistance': 'Paṭigha',
 'sights': 'Rūpa', 'sounds': 'sadda', 'tangible': 'phoṭṭhabba', 'tangible things': 'phoṭṭhabba',
 'things': 'phoṭṭhabba', 'therein': 'tattha'})
M['2-604'] = {
 'attained': 'samāpannassa', 'attend': 'manasi karoti', 'attending': 'amanasikārā',
 'consciousness element': 'viññāṇadhātu', 'diversity': 'nānatta', 'element': 'dhātu', 'having': NDE, 'mind': 'mano',
 'mind element': 'manodhātu', 'mind-consciousness': 'manoviññāṇa', 'mind-consciousness element': 'manoviññāṇadhātu',
 'perceived': 'sañjānitattaṃ', 'perceiving': 'sañjānanā', 'perception': 'saññā', 'perceptions': 'saññānaṃ',
 'perceptions of diversity': 'nānattasaññānaṃ', 'possesses': 'samaṅgissa', 'therefore': 'Tena', 'therein': 'tattha'}
M['2-605'] = {'belongs': 'gataṃ', 'elements': 'bhūtehi', 'gap': 'vivaro', 'great elements': 'mahābhūtehi',
              'infinite': 'Ananto', 'mind': 'cittaṃ', 'pervades': 'pharati', 'places': 'ṭhapeti',
              'settles': 'saṇṭhapeti', 'space': 'ākāso', 'therefore': 'Tena', 'therein': 'tattha',
              'untouched': 'asamphuṭṭhaṃ', 'void': 'aghaṃ'}
AKASA = ['field of infinite', 'infinite', 'infinite space', 'space']
VINNANA = ['consciousness', 'field of infinite', 'infinite', 'infinite consciousness']
AKINCA = ['field of nothingness', 'nothingness']
M['2-606'] = dict(CC, field='āyatanaṃ', **field('ākāsānañcāyatanaṃ', AKASA))
M['2-607'] = dict(UPASAMP, field='āyatanassa', **field('ākāsānañcāyatanassa', AKASA))
M['2-608'] = dict(VIH)
M['2-609'] = dict(PASS, field='āyatanaṃ', **field('ākāsānañcāyatanaṃ', AKASA))
M['2-610'] = {'attends': 'manasi karoti', 'consciousness': 'viññāṇa', 'infinite': 'Anantaṃ', 'pervades': 'pharati',
              'space': 'ākāsaṃ', 'therefore': 'Tena', 'touched': 'phuṭṭhaṃ'}
M['2-611'] = dict(CC, field='āyatanaṃ', **field('viññāṇañcāyatanaṃ', VINNANA))
M['2-612'] = dict(UPASAMP, field='āyatanassa', **field('viññāṇañcāyatanassa', VINNANA))
M['2-613'] = dict(VIH)
M['2-614'] = dict(PASS, field='āyatanaṃ', **field('viññāṇañcāyatanaṃ', VINNANA))
M['2-615'] = {'consciousness': 'viññāṇaṃ', 'disappear': 'bhāveti', 'makes': 'bhāveti', 'nothing': 'Natthi kiñcī',
              'therefore': 'Tena', 'vanish': 'vibhāveti'}
M['2-616'] = dict(CC, field='āyatanaṃ', **field('ākiñcaññāyatanaṃ', AKINCA))
M['2-617'] = dict(UPASAMP, field='āyatanassa', **field('ākiñcaññāyatanassa', AKINCA))
M['2-618'] = dict(VIH)
M['2-619'] = dict(PASS, field='āyatanaṃ', **field('ākiñcaññāyatanaṃ', AKINCA))
M['2-619'].update({'attainment': 'samāpattiṃ', 'attends': 'manasi karoti', 'develops': 'bhāveti',
                   'formations': 'saṅkhārāvasesasamāpattiṃ', 'non-percipient': 'nāsaññī', 'peaceful': 'santato',
                   'percipient': 'saññī', 'percipient nor non-percipient': 'Nevasaññīnāsaññī',
                   'residue': 'āvasesa'})
M['2-620'] = dict(CC, field='āyatanaṃ', **{'neither-perception-nor-non-perception': 'nevasaññānāsaññāyatanaṃ'})
M['2-621'] = dict(UPASAMP, field='āyatanassa',
                  **{'neither-perception-nor-non-perception': 'nevasaññānāsaññāyatanassa'})
M['2-622'] = dict(DWELLS, **{'classification': 'bhājanīyaṃ', 'discourses': 'Suttanta', 'finished': NDE})
M['2-12-2-0'] = {'abhidhamma': 'Abhidhamma', 'classification': 'bhājanīyaṃ'}
M['2-12-2-1-0'] = {'fine-material-sphere': 'Rūpāvacara', 'wholesome': 'kusalaṃ'}
FOUR = {'absorption': 'jhānaṃ', 'absorptions': 'jhānāni', 'fourth meditative': 'catutthaṃ jhānaṃ',
        'fourth meditative absorption': 'catutthaṃ jhānaṃ', 'meditative': 'jhānaṃ',
        'Meditative absorption': 'jhānaṃ', 'meditative absorption': 'jhānaṃ', 'meditative absorptions': 'jhānāni'}
M['2-623'] = dict(FOUR)
# Abhidhamma jhāna occasions (shared frame)
ABH = dict(JH)
ABH.update({
 'absorption': 'jhānaṃ', 'meditative': 'jhānaṃ', 'Meditative absorption': 'jhānaṃ', 'meditative absorption': 'jhānaṃ',
 'abandoning': 'pahānā', 'abandoning of happiness': 'sukhassa ca pahānā', 'associated': 'sampayuttā',
 'away': 'virāgā', 'develops': 'bhāveti', 'dwells': 'viharati', 'enters': 'upasampajja',
 'enters and dwells': 'upasampajja viharati', 'equanimity': 'upekkhā', 'examination': 'vicāro', 'fading': 'virāgā',
 'five-factored': 'pañcaṅgikaṃ', 'five-factored meditative': 'pañcaṅgikaṃ jhānaṃ',
 'five-factored meditative absorption': 'pañcaṅgikaṃ jhānaṃ', 'fourth meditative': 'catutthaṃ jhānaṃ',
 'fourth meditative absorption': 'catutthaṃ jhānaṃ', 'happiness': 'sukhaṃ', 'joy': 'pīti', 'monk': 'bhikkhu',
 'occasion': 'samaye', 'pleasures': 'kāmehi', 'remaining': 'Avasesā', 'remaining things': 'Avasesā dhammā',
 'secluded': 'vivicceva', 'secluded from sense': 'vivicceva kāmehi', 'sense': 'kāmehi', 'sense pleasures': 'kāmehi',
 'stilling': 'vūpasamā', 'stilling of thought': 'vitakkavicārānaṃ vūpasamā', 'therein': 'Tattha', 'things': 'dhammā',
 'thought': 'vitakko', 'thought and examination': 'vitakkavicārānaṃ', 'three-factored': 'tivaṅgikaṃ',
 'three-factored meditative': 'tivaṅgikaṃ jhānaṃ', 'three-factored meditative absorption': 'tivaṅgikaṃ jhānaṃ',
 'two-factored': 'duvaṅgikaṃ', 'two-factored meditative': 'duvaṅgikaṃ jhānaṃ',
 'two-factored meditative absorption': 'duvaṅgikaṃ jhānaṃ'})
PANCAKA = {'born': 'vivekajaṃ', 'fifth': 'pañcamaṃ', 'four-factored': 'caturaṅgikaṃ',
           'four-factored meditative': 'caturaṅgikaṃ jhānaṃ', 'four-factored meditative absorption': 'caturaṅgikaṃ jhānaṃ',
           'Joy and happiness': 'pītisukhaṃ', 'seclusion': 'viveka', 'unwholesome': 'akusalehi',
           'unwholesome things': 'akusalehi dhammehi'}
RUPA = {'develops the path': 'maggaṃ bhāveti', 'device': 'kasiṇaṃ', 'earth': 'pathavī', 'earth device': 'pathavīkasiṇaṃ',
        'fine-material': 'rūpūpapattiyā', 'fine-material sphere': 'rūpūpapattiyā', 'path': 'maggaṃ',
        'path for rebirth': 'rūpūpapattiyā maggaṃ', 'rebirth': 'ūpapattiyā', 'sphere': NDE}
ARUPA = {'develops the path': 'maggaṃ bhāveti', 'immaterial': 'arūpūpapattiyā', 'immaterial sphere': 'arūpūpapattiyā',
         'path': 'maggaṃ', 'path for rebirth': 'arūpūpapattiyā maggaṃ', 'rebirth': 'ūpapattiyā', 'sphere': NDE,
         'accompanied': 'sahagataṃ', 'beyond': 'samatikkamma', 'completely': 'sabbaso',
         'Completely passing': 'sabbaso / samatikkamma', 'completely passing': 'sabbaso / samatikkamma',
         'field': 'āyatanaṃ', 'field of nothingness': 'ākiñcaññāyatanaṃ', 'nothingness': 'ākiñcaññāyatanaṃ',
         'neither-perception-nor-non-perception': 'nevasaññānāsaññāyatana', 'passing': 'samatikkamma',
         'perception': 'saññā', 'happiness': 'sukhassa'}
LOKUTTARA = {'abandoning': 'pahānāya', 'abandoning of views': 'diṭṭhigatānaṃ pahānāya', 'beyond': 'lokuttaraṃ',
             'develops the meditative': 'jhānaṃ bhāveti', 'difficult': 'dukkhapaṭipadaṃ',
             'difficult practice': 'dukkhapaṭipadaṃ', 'direct': 'ābhiññaṃ', 'direct knowledge': 'ābhiññaṃ',
             'dismantling': 'apacaya', 'knowledge': 'ābhiññaṃ', 'leading to dismantling': 'apacayagāmiṃ',
             'practice': 'paṭipadaṃ', 'practice and slow': 'dukkhapaṭipadaṃ dandhābhiññaṃ', 'reaching': 'pattiyā',
             'slow': 'dandhābhiññaṃ', 'slow direct': 'dandhābhiññaṃ', 'slow direct knowledge': 'dandhābhiññaṃ',
             'stage': 'bhūmiyā', 'views': 'diṭṭhigatānaṃ'}
VIPAKA = {'accumulated': 'upacitattā', 'contact': 'phasso', 'done': 'katattā', 'non-distraction': 'avikkhepo',
          'things are wholesome': 'dhammā kusalā', 'wholesome': 'kusalā', 'wholesome action': 'kusalassa kammassa'}
M['2-624'] = dict(ABH, **RUPA)
M['2-625'] = dict(ABH, **RUPA)
M['2-625'].update(PANCAKA)
M['2-12-2-2-0'] = {'immaterial-sphere': 'Arūpāvacara', 'wholesome': 'kusalaṃ'}
M['2-626'] = dict(ABH, **ARUPA)
M['2-12-2-3-0'] = {'beyond': 'Lokuttara', 'wholesome': 'kusalaṃ'}
M['2-627'] = dict(FOUR)
M['2-628'] = dict(ABH, **LOKUTTARA)
M['2-629'] = dict(ABH, **LOKUTTARA)
M['2-629'].update(PANCAKA)
M['2-12-2-4-0'] = {'fine-material-sphere': 'Rūpāvacara'}
M['2-630'] = dict(FOUR)
M['2-631'] = dict(ABH, **RUPA)
M['2-631'].update(VIPAKA)
M['2-631'].update({'fifth': 'pañcamaṃ', 'fine-material-sphere': 'rūpāvacarassa'})
M['2-12-2-5-0'] = {'immaterial-sphere': 'Arūpāvacara'}
M['2-632'] = dict(ABH, **ARUPA)
M['2-632'].update(VIPAKA)
M['2-632'].update({'immaterial-sphere': 'arūpāvacarassa'})
M['2-12-2-6-0'] = {'beyond': 'Lokuttara'}
M['2-633'] = dict(FOUR)
M['2-634'] = dict(ABH, **LOKUTTARA)
M['2-634'].update(VIPAKA)
M['2-634'].update({'developed': 'bhāvitattā', 'emptiness': 'suññataṃ', 'fifth': 'pañcamaṃ',
                   'wholesome meditative': 'kusalassa jhānassa', 'wholesome meditative absorption': 'kusalassa jhānassa'})
M['2-12-2-7-0'] = {'fine-material': 'Rūpārūpāvacarakiriyā', 'functional': 'kiriyā', 'immaterial': 'ārūpāvacara'}
M['2-635'] = dict(FOUR)
KIRIYA = {'dwelling': 'vihāraṃ', 'functional': 'kiriyaṃ', 'life': 'diṭṭhadhamma', 'pleasant': 'sukhavihāraṃ',
          'unwholesome': 'nākusalaṃ', 'wholesome': 'kusalaṃ', 'wholesome nor unwholesome': 'neva kusalaṃ nākusalaṃ'}
M['2-636'] = dict(ABH, **KIRIYA)
M['2-636'].update({'device': 'kasiṇaṃ', 'earth': 'pathavī', 'earth device': 'pathavīkasiṇaṃ', 'fifth': 'pañcamaṃ',
                   'fine-material-sphere': 'rūpāvacaraṃ'})
M['2-637'] = dict(ABH, **ARUPA)
M['2-637'].update(KIRIYA)
M['2-637'].update({'abhidhamma': 'Abhidhamma', 'classification': 'bhājanīyaṃ', 'finished': NDE,
                   'immaterial-sphere': 'arūpāvacaraṃ', 'immaterial-sphere meditative absorption': 'arūpāvacaraṃ jhānaṃ'})
QA = {'answers': NDE, 'questions': 'Pañhā', 'Questions and Answers': 'Pañhāpucchakaṃ', 'section': NDE,
      'Section of Questions': 'Pañhāpucchakaṃ'}
M['2-12-3-0'] = dict(QA)
M['2-638'] = dict(JHANA, **{'absorptions': 'jhānāni', 'meditative absorptions': 'jhānāni', 'body': 'kāyena',
                            'mind': 'cetaso', 'mindfulness': 'sati', 'monk': 'bhikkhu', 'things': 'dhammehi'})
M['2-639'] = {'absorptions': 'jhānānaṃ', 'conflict': 'saraṇā', 'free': 'araṇā', 'involve': 'saraṇā',
              'meditative': 'jhānānaṃ', 'meditative absorptions': 'jhānānaṃ', 'neutral': 'abyākatā',
              'unwholesome': 'akusalā', 'wholesome': 'kusalā'}
M['2-12-3-1-0'] = {'triads': 'Tikaṃ'}
M['2-640'] = dict(FOUR, **{
 'abandoned': 'pahātabbā', 'able': 'upādāniyā', 'accompanied': 'sahagatā',
 'accompanied by equanimity': 'upekkhāsahagataṃ', 'accompanied by happiness': 'sukhasahagatā',
 'accompanied by joy': 'pītisahagatā', 'accumulation': 'ācayagāmino', 'arise': 'uppādino', 'arisen': 'uppannā',
 'aside': 'ṭhapetvā', 'associated': 'sampayuttā', 'belong': NDE, 'beyond': 'asekkhā', 'birth': NDE,
 'cause': 'hetukā', 'causes': 'hetukā', 'clung': 'upādāniyā', 'connected': 'saṃkilesikā',
 'connected with defilement': 'saṃkilesikā', 'defilement': 'saṃkilesikā', 'describable': 'vattabbā',
 'dismantling': 'apacayagāmino', 'dominant': 'ādhipatino', 'dominant factor': 'ādhipatino', 'due to arise': 'uppādino',
 'equanimity': 'upekkhaṃ', 'equanimity arisen': 'etthuppannaṃ upekkhaṃ', 'examination': 'vicāre',
 'examination arisen': 'etthuppanne vitakkavicāre', 'expanded': 'mahaggatā', 'expanded object': 'mahaggatārammaṇaṃ',
 'external': 'bahiddhā', 'external object': 'bahiddhārammaṇaṃ', 'external objects': 'bahiddhārammaṇā',
 'factor': 'ādhipatino', 'feeling': 'vedanaṃ', 'fixed': 'niyatā', 'future object': 'anāgatārammaṇaṃ',
 'happiness': 'sukhaṃ', 'happiness arisen': 'etthuppannaṃ sukhaṃ', 'having': NDE, 'internal': 'ajjhattā',
 'internal and external': 'ajjhattabahiddhā', 'internal object': 'ajjhattārammaṇaṃ', 'invisible': 'Anidassana',
 'invisible and offer': 'Anidassanaappaṭighā', 'joy': 'pītiṃ', 'joy arisen': 'etthuppannaṃ pītiṃ',
 'leading to accumulation': 'ācayagāmino', 'leading to dismantling': 'apacayagāmino', 'limited': 'parittārammaṇaṃ',
 'limited object': 'parittārammaṇaṃ', 'measureless': 'appamāṇā', 'measureless object': 'appamāṇārammaṇaṃ',
 'measureless objects': 'appamāṇārammaṇā', 'meditative development': 'bhāvanāya', 'middling': 'majjhimā',
 'neither-painful-nor-pleasant': 'adukkhamasukhaṃ', 'neutral': 'abyākatā', 'object': 'ārammaṇaṃ',
 'objects': 'ārammaṇā', 'past object': 'atītārammaṇaṃ', 'path': 'magga', 'pleasant': 'sukhaṃ',
 'pleasant feeling': 'sukhaṃ vedanaṃ', 'present object': 'paccuppannārammaṇaṃ', 'refined': 'paṇītā',
 'resistance': 'appaṭighā', 'results nor things': 'nevavipākanavipākadhammadhammā', 'rightness': 'sammatta',
 'seeing': 'dassanena', 'setting': 'ṭhapetvā', 'subject to result': 'vipākadhammadhammā',
 'things': 'vipākadhammadhammā', 'things subject': 'vipākadhammadhammā', 'thought': 'vitakka',
 'thought and examination': 'vitakkavicāre', 'training': 'sekkhā', 'undefiled': 'asaṃkiliṭṭha',
 'unfixed': 'aniyatā', 'wholesome': 'kusalā'})
M['2-12-3-2-0'] = {'pairs': 'Dukaṃ'}
M['2-641'] = dict(FOUR, **QA)
M['2-641'].update({
 'abandoned': 'pahātabbā', 'accompanied': 'sahagatā', 'accompanied by equanimity': 'upekkhāsahagataṃ',
 'accompanied by happiness': 'sukhasahagatā', 'accompanied by joy': 'pītisahagatā', 'along': 'ānuparivattino',
 'analysis': 'vibhaṅgo', 'arise': 'sahabhuno', 'arisen': 'etthuppannaṃ', 'aside': 'ṭhapetvā',
 'associated': 'sampayuttā', 'belong': NDE, 'beyond': 'lokuttarā', 'birth': NDE, 'cannot': 'na',
 'causes': 'hetukā', 'clinging': 'upādānā', 'conditioned': 'saṅkhatā', 'conflict': 'araṇāti',
 'conjoined': 'saṃsaṭṭhā', 'defilements': 'kilesā', 'derived': 'upādā', 'describable': 'vattabbā',
 'dissociated': 'vippayuttā', 'equanimity': 'upekkhaṃ', 'equanimity arisen': 'etthuppannaṃ upekkhaṃ',
 'examination': 'vicāraṃ', 'examination arisen': 'etthuppannaṃ vicāraṃ', 'external': 'bāhirā',
 'factors': 'cetasikā', 'fetters': 'saṃyojanā', 'fine-material': 'rūpāvacarā', 'fine-material sphere': 'rūpāvacarā',
 'finished': 'niṭṭhito', 'fixed': 'niyatā', 'floods': 'oghā', 'follow': 'ānuparivattino', 'free': 'araṇāti',
 'grasping': 'parāmāsā', 'happiness': 'sukhaṃ', 'happiness arisen': 'etthuppannaṃ sukhaṃ', 'having': 'sahetukā',
 'hindrances': 'nīvaraṇā', 'immaterial': 'arūpā', 'immaterial sphere': 'arūpāvacarā', 'invisible': 'anidassanā',
 'joy': 'pītiṃ', 'joy arisen': 'etthuppannaṃ pītiṃ', 'known': 'viññeyyā', 'means': 'kenaci',
 'meditative development': 'bhāvanāya', 'mental': 'cetasikā', 'mental factors': 'cetasikā', 'mental taints': 'āsavā',
 'mind': 'citta', 'minds': 'cittā', 'objects': 'sārammaṇā', 'originated': 'samuṭṭhānā', 'resistance': 'appaṭighā',
 'roots': 'hetū', 'seeing': 'dassanena', 'sense': 'kāmāvacarā', 'sense sphere': 'kāmāvacarā', 'setting': 'ṭhapetvā',
 'sphere': 'āvacarā', 'subject to mental': 'sāsavā', 'surpassable': 'sauttarā', 'taints': 'āsavā',
 'thought': 'vitakkaṃ', 'ties': 'ganthā', 'together': 'saha', 'unfixed': 'aniyatā', 'unsurpassed': 'anuttarā',
 'worldly': 'lokiyā', 'wrong': 'parāmāsā', 'wrong grasping': 'parāmāsā', 'yokes': 'yogā'})

out, missing = [], []
for line in (d / f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines():
    sid, kws = line.split('] ', 1)
    sid = sid[1:]
    m = M.get(sid)
    if m is None:
        missing.append((sid, 'ALL')); continue
    pairs = []
    for k in kws.split(', '):
        k = k.strip()
        if k not in m:
            missing.append((sid, k)); pairs.append(f'???={k}')
        else:
            pairs.append(f'{m[k]}={k}')
    out.append(f'[{sid}] ' + ', '.join(pairs))
(d / f'{ch}.mapped.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
print('written', len(out), 'missing', [x for x in missing if x[1] != 'ALL'], 'unmapped segs', sum(1 for x in missing if x[1] == 'ALL'))
