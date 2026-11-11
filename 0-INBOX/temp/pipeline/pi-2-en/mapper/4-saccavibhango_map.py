import pathlib, re
d = pathlib.Path(__file__).parent
root = d.parents[4]
ch = '4-saccavibhango'
NDE = '(no direct equivalent)'

# ---- shared blocks -------------------------------------------------------
BIRTH_LOSS = {  # 2-194 / 2-195 / 2-198 common opening
 'illness': 'roga', 'meets': 'samannāgatassa', 'misfortune': 'byasanena', 'painful': 'dukkha',
 'relatives': 'Ñāti', 'someone': NDE, 'therein': 'Tattha', 'thing': 'dhammena', 'touched': 'phuṭṭhassa',
 'touched by loss': 'byasanena vā phuṭṭhassa', 'view': 'diṭṭhi', 'virtue': 'sīla', 'wealth': 'bhoga',
}
FOUR = {  # 2-189 / 2-215
 'ending of suffering': 'dukkhanirodhaṃ', 'noble': 'ariya', 'noble truth': 'ariyasaccaṃ',
 'noble truths': 'ariyasaccāni', 'origin': 'samudayaṃ', 'origin of suffering': 'dukkhasamudayaṃ',
 'suffering': 'dukkhaṃ', 'truth': 'saccaṃ', 'truth of suffering': 'dukkhaṃ ariyasaccaṃ', 'truths': 'saccāni',
}
# 2-203 / 2-204 common (craving arises / ceases in the world)
CRAVE = {
 'body': 'kāyo', 'body-consciousness': 'kāyaviññāṇaṃ', 'body-contact': 'kāyasamphasso',
 'born': 'Cakkhusamphassajā', 'born of body-contact': 'kāyasamphassajā',
 'born of ear-contact': 'Sotasamphassajā', 'born of eye-contact': 'Cakkhusamphassajā',
 'born of mind-contact': 'manosamphassajā', 'born of nose-contact': 'ghānasamphassajā',
 'born of tongue-contact': 'jivhāsamphassajā', 'craving': 'taṇhā', 'craving for things': 'phoṭṭhabbataṇhā',
 'ear': 'Sotaṃ', 'ear-consciousness': 'Sotaviññāṇaṃ', 'ear-contact': 'Sotasamphasso', 'examination': 'vicāro',
 'eye': 'Cakkhuṃ', 'eye-consciousness': 'Cakkhuviññāṇaṃ', 'eye-contact': 'Cakkhusamphasso', 'feeling': 'vedanā',
 'feeling born': 'Cakkhusamphassajā vedanā', 'Feeling born': 'Cakkhusamphassajā vedanā',
 'intention': 'sañcetanā', 'lovely': 'piyarūpaṃ', 'lovely thing': 'piyarūpaṃ', 'mental': 'dhammā',
 'mental objects': 'dhammā', 'mind': 'mano', 'mind-consciousness': 'manoviññāṇaṃ', 'mind-contact': 'manosamphasso',
 'noble': 'ariya', 'noble truth': 'ariyasaccaṃ', 'nose': 'ghānaṃ', 'nose-consciousness': 'ghānaviññāṇaṃ',
 'nose-contact': 'ghānasamphasso', 'objects': 'dhammā', 'perception': 'saññā', 'pleasing': 'sātarūpaṃ',
 'pleasing thing': 'sātarūpaṃ', 'regarding': NDE, 'sights': 'Rūpā', 'smells': 'gandhā', 'sounds': 'Saddā',
 'suffering': 'dukkha', 'tastes': 'rasā', 'therein': 'Tattha', 'thing': 'rūpaṃ', 'things': 'phoṭṭhabbā',
 'things touched': 'phoṭṭhabbā', 'thought': 'vitakko', 'tongue': 'jivhā', 'tongue-consciousness': 'jivhāviññāṇaṃ',
 'tongue-contact': 'jivhāsamphasso', 'touched': 'phoṭṭhabbā', 'truth': 'saccaṃ', 'whatever': 'Yaṃ',
}
# Abhidhamma classification 2-206 .. 2-214 (alternatives: first one present in the segment is used)
ABH = {
 'abandoning': 'pahānaṃ', 'abandoning of craving': ['Taṇhāya pahānaṃ', 'Taṇhāya / pahānaṃ'],
 'abandoning of wrong': 'diṭṭhigatānaṃ pahānāya', 'absorption': 'jhānaṃ', 'associated': 'sampayuttā',
 'beyond': 'uttaraṃ', 'concentration': 'samādhi', 'contact': 'phasso', 'craving': 'Taṇhā', 'defilements': 'kilesā',
 'develops': 'bhāveti', 'develops the meditative': 'jhānaṃ bhāveti', 'difficult': 'dukkhapaṭipadaṃ',
 'difficult and direct': 'dukkhapaṭipadaṃ dandhābhiññaṃ', 'direct': 'ābhiññaṃ', 'direct knowledge': 'ābhiññaṃ',
 'dismantling': 'apacaya', 'dwells': 'viharati', 'eightfold': 'aṭṭhaṅgiko', 'eightfold path': 'aṭṭhaṅgiko maggo',
 'fivefold': 'pañcaṅgiko', 'fivefold path': 'pañcaṅgiko maggo',
 'ending of suffering': 'dukkhanirodho', 'enters': 'upasampajja', 'enters and dwells': 'upasampajja viharati',
 'form': 'rūpaṃ', 'functioning': 'kiriyā', 'knowledge': 'ābhiññaṃ', 'knowledge slow': 'dandhābhiññaṃ',
 'leading to dismantling': 'apacayagāmiṃ', 'material': 'rūpaṃ', 'material form': 'rūpaṃ', 'meditative': 'jhānaṃ',
 'Meditative absorption': 'jhānaṃ', 'meditative absorption': 'jhānaṃ', 'mental': 'sāsavāni',
 'mental taints': 'sāsavāni', 'mere': 'kiriyā', 'mere functioning': 'kiriyā', 'monk': 'bhikkhu',
 'monk develops': 'bhikkhu / bhāveti', 'non-distraction': 'avikkhepo', 'occasion': 'samaye', 'origin': 'samudayo',
 'origin of suffering': 'dukkhasamudayo', 'path': 'maggo', 'pleasures': 'kāmehi', 'reaching': 'pattiyā',
 'remaining': 'avasesā', 'remaining defilements': 'avasesā ca kilesā', 'remaining states': 'avasesā dhammā',
 'remaining unwholesome': 'avasesā ca akusalā', 'remaining unwholesome states': 'avasesā ca akusalā dhammā',
 'remaining wholesome': 'avasesā ca sāsavā kusalā', 'remaining wholesome states': 'avasesā ca sāsavā kusalā dhammā',
 'results of action': 'kammavipākā', 'results of wholesome': 'kusalākusalānaṃ dhammānaṃ vipākā', 'right': 'sammā',
 'roots': 'mūlāni', 'roots subject': 'mūlāni sāsavāni', 'round': NDE, 'secluded': 'vivicceva',
 'secluded from sense': 'vivicceva kāmehi', 'sense': 'kāmehi', 'sense pleasures': 'kāmehi', 'slow': 'dandhābhiññaṃ',
 'stage': 'bhūmiyā', 'states subject': 'sāsavā / dhammā', 'suffering': 'dukkhaṃ', 'taints': 'sāsavā',
 'therein': 'Tattha', 'truths': 'saccāni', 'unwholesome': 'akusalā', 'unwholesome states': 'akusalā dhammā',
 'unwholesome states subject': ['sāsavā ca kusalākusalānaṃ dhammānaṃ', 'sāsavā kusalākusalānaṃ dhammānaṃ'],
 'view': 'diṭṭhi', 'views': 'diṭṭhigatānaṃ', 'wholesome': 'kusalā', 'wholesome and unwholesome': 'kusalākusalānaṃ',
 'Wholesome and unwholesome': 'kusalākusalānaṃ', 'wholesome nor unwholesome': 'neva kusalā nākusalā',
 'wholesome roots': 'kusalamūlāni', 'wholesome roots subject': 'kusalamūlāni sāsavāni',
 'wholesome states': 'kusalā dhammā', 'wholesome states subject': 'sāsavā kusalā dhammā',
 'wrong': 'diṭṭhigatānaṃ', 'wrong views': 'diṭṭhigatānaṃ',
}
# the full path-factor definitions (2-206 eightfold, 2-211 fivefold)
FACTORS = {
 'arousing': 'ārambho', 'awakening': 'sambojjhaṅgo', 'awakening factor': 'sambojjhaṅgo', 'effort': 'vāyāmo',
 'factor': 'sambojjhaṅgo', 'factor of concentration': 'samādhisambojjhaṅgo',
 'factor of energy': 'vīriyasambojjhaṅgo', 'factor of investigation': 'dhammavicayasambojjhaṅgo',
 'factor of mindfulness': 'satisambojjhaṅgo', 'intention': 'saṅkappo', 'investigation': 'vicayo',
 'investigation of states': 'dhammavicayo', 'mind': 'cittassa', 'mindfulness': 'sati', 'non-delusion': 'amoho',
 'path factor': 'maggaṅgaṃ', 'remembering': 'anussati', 'stability': 'saṇṭhiti', 'steadiness': 'ṭhiti',
 'thinking': 'takko', 'thought': 'vitakko', 'understanding': 'pajānanā', 'wisdom': 'paññā',
}
QA = {'answers': NDE, 'questions': 'Pañhā', 'Questions and Answers': 'Pañhāpucchakaṃ', 'section': NDE,
      'Section of Questions': 'Pañhāpucchakaṃ'}

M = {}
M['2-4-0'] = {'analysis': 'vibhaṅgo', 'truths': 'Sacca'}
M['2-4-1-0'] = {'classification': 'bhājanīyaṃ', 'discourses': 'Suttanta'}
M['2-189'] = dict(FOUR)
M['2-4-1-1-0'] = {'suffering': 'Dukkha', 'truth': 'saccaṃ', 'truth of suffering': 'Dukkhasaccaṃ'}
SADNESS = 'sokaparidevadukkhadomanassupāyāsāpi'  # domanassa+upāyāsā sandhi: whole compound
M['2-190'] = {
 'aggregates': 'khandhā', 'aging': 'jarāpi', 'birth': 'Jātipi', 'brief': 'saṃkhittena', 'clung': 'upādāna',
 'death': 'maraṇampi', 'despair': 'upāyāsāpi', 'disliked': 'appiyehi', 'getting': 'labhati', 'lamentation': 'parideva',
 'loved': 'piyehi', 'noble': 'ariya', 'noble truth': 'ariyasaccaṃ', 'pain': 'dukkha', 'sadness': SADNESS,
 'separation': 'vippayogo', 'sorrow': 'soka', 'suffering': 'dukkhaṃ', 'therein': 'Tattha', 'truth': 'saccaṃ',
 'truth of suffering': 'dukkhaṃ ariyasaccaṃ', 'wants': 'picchaṃ',
}
M['2-191'] = {
 'acquiring': 'paṭilābho', 'aggregates': 'khandhānaṃ', 'appearance': 'pātubhāvo', 'beings': 'sattānaṃ',
 'birth': 'jāti', 'born': 'sañjāti', 'coming': 'abhinibbatti', 'descent': 'okkanti', 'forth': 'abhinibbatti',
 'order': 'nikāye', 'sense-fields': 'āyatanānaṃ', 'therein': 'Tattha',
}
M['2-192'] = {
 'aging': 'jarā', 'beings': 'sattānaṃ', 'brokenness': 'khaṇḍiccaṃ', 'faculties': 'indriyānaṃ', 'greyness': 'pāliccaṃ',
 'growing': 'jīraṇatā', 'hair': 'pāliccaṃ', 'life': 'āyuno', 'old': 'jīraṇatā', 'order': 'nikāye',
 'ripening': 'paripāko', 'skin': 'taca', 'span': 'āyuno', 'teeth': 'khaṇḍiccaṃ', 'therein': 'Tattha',
 'wrinkling': 'vali',
}
M['2-193'] = {
 'aggregates': 'khandhānaṃ', 'away': 'cavanatā', 'beings': 'sattānaṃ', 'body': 'kaḷevarassa', 'breaking': 'bhedo',
 'completion': 'kālakiriyā', 'cutting': 'upacchedo', 'death': 'maraṇaṃ', 'disappearance': 'antaradhānaṃ',
 'faculty': 'indriya', 'laying': 'nikkhepo', 'life': 'jīvitindriyassupacchedo', 'life faculty': 'jīvitindriya',
 'mortality': 'maccu', 'order': 'nikāyā', 'passing': 'cuti', 'therein': 'Tattha',
}
M['2-194'] = dict(BIRTH_LOSS, **{
 'burning': 'parijjhāyanā', 'dart': 'sallaṃ', 'deep': 'antoparisoko', 'inner': 'anto', 'mind': 'cetaso',
 'sadness': 'domanassaṃ', 'sorrow': 'soko', 'sorrowing': 'socanā'})
M['2-195'] = dict(BIRTH_LOSS, **{
 'act': 'ādevanā', 'crying': 'ādevo', 'lamentation': 'paridevo', 'lamenting': 'paridevo', 'moaning': 'lālappo',
 'raving': 'palāpo', 'talk': 'vācā', 'wailing': 'vippalāpo'})
def PAINDEF(contact, born_n, born_f, extra):
    m = {
     'born': born_n, 'discomfort': 'asātaṃ', 'experience': 'vedayitaṃ', 'experience born': f'{born_n} / vedayitaṃ',
     'feeling': 'vedanā', 'Feeling born': f'{born_f} / vedanā', 'feeling born': f'{born_f} / vedanā',
     'pain': 'dukkhaṃ', 'painful': 'dukkhaṃ', 'painful experience': 'dukkhaṃ vedayitaṃ',
     'painful experience born': f'{born_n} asātaṃ dukkhaṃ vedayitaṃ', 'painful feeling': 'dukkhā vedanā',
     'painful feeling born': f'{born_f} asātā dukkhā vedanā', 'therein': 'Tattha', 'uncomfortable': 'asātaṃ',
    }
    m.update(extra); return m
M['2-196'] = PAINDEF('kāyasamphassa', 'kāyasamphassajaṃ', 'kāyasamphassajā', {
 'bodily': 'kāyikaṃ', 'body-contact': 'kāyasamphassa', 'born of body-contact': 'kāyasamphassajaṃ'})
M['2-197'] = PAINDEF('cetosamphassa', 'cetosamphassajaṃ', 'cetosamphassajā', {
 'born of mind-contact': 'cetosamphassajaṃ', 'mental': 'cetasikaṃ', 'mental discomfort': 'cetasikaṃ asātaṃ',
 'mental pain': 'cetasikaṃ dukkhaṃ', 'mind-contact': 'cetosamphassa', 'sadness': 'domanassaṃ'})
M['2-198'] = dict(BIRTH_LOSS, **{'despair': 'upāyāso', 'distress': 'āyāso'})
ASSOC = {
 'coming': 'samāgamo', 'joining': 'samodhānaṃ', 'mingling': 'missībhāvo', 'security': 'yogakkhema',
 'sights': 'rūpā', 'smells': 'gandhā', 'someone': 'yassa', 'sounds': 'saddā', 'suffering': 'dukkho', 'tastes': 'rasā',
 'therein': 'Tattha', 'things': 'phoṭṭhabbā', 'things touched': 'phoṭṭhabbā', 'together': 'samāgamo',
 'touched': 'phoṭṭhabbā', 'whatever': NDE, 'whoever': 'ye vā panassa', 'wishes': 'kāmā',
}
M['2-199'] = dict(ASSOC, **{
 'disagreeable': 'amanāpā', 'discomfort': 'aphāsuka', 'disliked': 'appiyehi', 'harm': 'ahita', 'ill': 'anattha',
 'unattractive': 'akantā', 'unwanted': 'aniṭṭhā'})
M['2-200'] = dict(ASSOC, **{
 'agreeable': 'manāpā', 'attractive': 'kantā', 'brother': 'bhātā', 'comfort': 'phāsuka', 'coming': 'asamāgamo',
 'companions': 'amaccā', 'father': 'pitā', 'friends': 'mittā', 'joining': 'asamodhānaṃ', 'kin': 'sālohitā',
 'loved': 'piyehi', 'mingling': 'amissībhāvo', 'mother': 'mātā', 'relatives': 'ñātī', 'separation': 'vippayogo',
 'sister': 'bhaginī', 'together': 'asamāgamo', 'wanted': 'iṭṭhā'})
M['2-201'] = {
 'aging': 'Jarā', 'arises': 'uppajjati', 'beings': 'sattānaṃ', 'birth': 'jāti', 'cannot': 'Na', 'death': 'maraṇa',
 'despair': 'upāyāsā', 'gained': 'pattabbaṃ', 'getting': 'labhati', 'illness': 'byādhi', 'lamentation': 'parideva',
 'pain': 'dukkha', 'sadness': 'sokaparidevadukkhadomanassupāyāsā', 'sorrow': 'soka', 'suffering': 'dukkhaṃ',
 'therein': 'Tattha', 'wants': 'picchaṃ', 'wish': 'icchā', 'wishing': 'icchāya',
}
M['2-202'] = {
 'aggregate': 'khandho', 'aggregate of consciousness': 'viññāṇupādānakkhandho',
 'Aggregate of Consciousness': 'viññāṇupādānakkhandho', 'aggregate of feeling': 'vedanupādānakkhandho',
 'aggregate of material': 'rūpupādānakkhandho', 'aggregate of mental': 'saṅkhārupādānakkhandho',
 'Aggregate of Mental': 'saṅkhārupādānakkhandho', 'Aggregate of Perception': 'saññupādānakkhandho',
 'aggregate of perception': 'saññupādānakkhandho', 'aggregates': 'khandhā', 'brief': 'saṃkhittena',
 'clung': 'upādāna', 'consciousness': 'viññāṇupādānakkhandho', 'feeling': 'vedanupādānakkhandho',
 'form': 'rūpupādānakkhandho', 'formations': 'saṅkhārupādānakkhandho', 'material': 'rūpupādānakkhandho',
 'material form': 'rūpupādānakkhandho', 'mental': 'saṅkhārupādānakkhandho',
 'Mental Formations': 'saṅkhārupādānakkhandho', 'mental formations': 'saṅkhārupādānakkhandho',
 'namely': 'Seyyathidaṃ', 'noble': 'ariya', 'noble truth': 'ariyasaccaṃ', 'perception': 'saññupādānakkhandho',
 'suffering': 'dukkhā', 'therein': 'Tattha', 'truth': 'saccaṃ', 'truth of suffering': 'dukkhaṃ ariyasaccaṃ',
}
M['2-4-1-2-0'] = {'origin': 'Samudaya', 'truth': 'saccaṃ'}
M['2-203'] = dict(CRAVE, **{
 'accompanied': 'sahagatā', 'arise': 'uppajjati', 'arises': 'uppajjati', 'craving arise': 'taṇhā / uppajjati',
 'craving arises': 'taṇhā uppajjamānā uppajjati', 'craving for existence': 'bhavataṇhā',
 'craving for non-existence': 'vibhavataṇhā', 'craving for sense': 'kāmataṇhā', 'delight': 'nandi',
 'delighting': 'ābhinandinī', 'desire': 'rāga', 'existence': 'bhava', 'leads': 'ponobhavikā', 'namely': 'seyyathidaṃ',
 'non-existence': 'vibhava', 'origin': 'samudayaṃ', 'origin of suffering': 'dukkhasamudayaṃ', 'pleasures': 'kāma',
 'renewed': 'ponobhavikā', 'sense': 'kāma', 'sense pleasures': 'kāma', 'settle': 'nivisati', 'settles': 'nivisati'})
M['2-4-1-3-0'] = {'truth': 'saccaṃ'}
M['2-204'] = dict(CRAVE, **{
 'abandoned': 'pahīyati', 'away': 'virāga', 'cease': 'nirujjhati', 'ceases': 'nirujjhati', 'complete': 'asesa',
 'craving abandoned': 'taṇhā / pahīyati', 'craving is abandoned': 'taṇhā pahīyamānā pahīyati',
 'ending of suffering': 'dukkhanirodhaṃ', 'fading': 'virāga', 'giving': 'cāgo', 'letting': 'paṭinissaggo',
 'release': 'mutti', 'relying': 'anālayo'})
M['2-4-1-4-0'] = {'path': 'Magga', 'truth': 'saccaṃ'}
M['2-205'] = {
 'abandoned': 'pahāya', 'abandoning': 'pahānāya', 'absorption': 'jhānaṃ', 'applies': 'paggaṇhāti', 'ardent': 'ātāpī',
 'arisen': 'Uppannānaṃ', 'arising': 'uppādāya', 'arouses': 'ārabhati', 'away': 'vineyya', 'bad': 'pāpakānaṃ',
 'beings': 'Pāṇātipātā', 'body': 'kāye', 'born': 'vivekajaṃ', 'chatter': 'samphappalāpā',
 'classification': 'bhājanīyaṃ', 'clearly': 'sampajāno', 'concentration': 'samādhi', 'confidence': 'sampasādanaṃ',
 'contemplating': 'ānupassī', 'contemplating feelings': 'Vedanāsu', 'contemplating the body': 'kāye kāyānupassī',
 'covetousness': 'abhijjhā', 'declare': 'ācikkhanti', 'desire': 'chandaṃ', 'disappearance': 'atthaṅgamā',
 'disciple': 'sāvako', 'discourses': 'Suttanta', 'divisive': 'pisuṇāya', 'dwells': 'viharati',
 'dwells contemplating': 'kāyānupassī viharati', 'dwells contemplating feelings': 'Vedanāsu',
 'dwells happily': 'sukhavihārī', 'effort': 'vāyāmo', 'eightfold': 'aṭṭhaṅgiko', 'eightfold path': 'aṭṭhaṅgiko maggo',
 'endeavours': 'padahati', 'ending of suffering': 'dukkhanirodha', 'enters': 'upasampajja',
 'enters and dwells': 'upasampajja viharati', 'equanimity': 'upekkhako', 'equanimous': 'upekkhako',
 'examination': 'vicāraṃ', 'expansion': 'vepullāya', 'experiences': 'paṭisaṃvedeti',
 'experiences happiness': 'sukhañca / paṭisaṃvedeti', 'fading': 'virāgā', 'false': 'Musā',
 'false speech': 'Musāvādā', 'feelings': 'Vedanāsu', 'feelings in feelings': 'Vedanāsu', 'finished': NDE,
 'fourth meditative': 'catutthaṃ jhānaṃ', 'fourth meditative absorption': 'catutthaṃ jhānaṃ',
 'fulfilment': 'pāripūriyā', 'generates': 'janeti', 'generates desire': 'chandaṃ janeti', 'gladness': 'somanassa',
 'goodwill': 'abyāpāda', 'happily': 'sukhavihārī', 'happiness': 'sukhaṃ', 'harmlessness': 'avihiṃsā',
 'harsh': 'pharusāya', 'having': NDE, 'idle': 'samphappalāpā', 'inner': 'ajjhattaṃ', 'intention': 'saṅkappo',
 'joy': 'pīti', 'Joy and happiness': 'pītisukhaṃ', 'killing': 'ātipātā', 'killing living': 'Pāṇātipātā',
 'knowledge': 'ñāṇaṃ', 'livelihood': 'ājīvo', 'living': 'Pāṇātipātā', 'maintaining': 'ṭhitiyā', 'makes': 'kappeti',
 'meditative': 'jhānaṃ', 'Meditative absorption': 'jhānaṃ', 'meditative absorption': 'jhānaṃ',
 'mental': 'dhammesu', 'mental objects': 'dhammesu', 'mind': 'cittaṃ', 'mindful': 'satimā', 'mindfulness': 'sati',
 'misconduct': 'micchācārā', 'monk': 'bhikkhu', 'monk dwells': 'bhikkhu / viharati',
 'monk dwells contemplating': 'bhikkhu / kāyānupassī viharati', 'monk generates': 'bhikkhu / janeti',
 'monk generates desire': 'bhikkhu / chandaṃ janeti', 'namely': 'seyyathidaṃ', 'noble': 'ariya',
 'noble truth': 'ariyasaccaṃ', 'non-arising': 'anuppādāya', 'non-confusion': 'asammosāya', 'objects': 'dhammesu',
 'objects in mental': 'dhammesu', 'ones': 'ariyā', 'origin': 'samudaye', 'origin of suffering': 'dukkhasamudaye',
 'pain': 'dukkhassa', 'painful': 'adukkhamasukhaṃ', 'painful nor pleasant': 'adukkhamasukhaṃ',
 'path': 'maggo', 'pleasant': 'adukkhamasukhaṃ', 'pleasure': 'Sukhassa', 'pleasures': 'kāmehi',
 'purity': 'pārisuddhiṃ', 'refraining': 'veramaṇī', 'renunciation': 'Nekkhamma', 'right': 'sammā',
 'sadness': 'domanassaṃ', 'secluded': 'vivicca', 'secluded from sense': 'vivicceva kāmehi', 'seclusion': 'viveka',
 'sense': 'kāmehi', 'sense pleasures': 'kāmehi', 'sexual': 'kāmesu', 'speech': 'vācā', 'stilling': 'vūpasamā',
 'stilling of thought': 'Vitakkavicārānaṃ vūpasamā', 'strives': 'vāyamati', 'suffering': 'dukkha',
 'taking': 'ādānā', 'therein': 'Tattha', 'thought': 'vitakkaṃ', 'thought and examination': 'savitakkaṃ savicāraṃ',
 'towards': NDE, 'truth': 'saccaṃ', 'understanding': 'sampajāno', 'unification': 'ekodibhāvaṃ',
 'unwholesome': 'akusalānaṃ', 'unwholesome states': 'akusalānaṃ dhammānaṃ', 'view': 'diṭṭhi',
 'wholesome': 'kusalānaṃ', 'wholesome states': 'kusalānaṃ dhammānaṃ', 'wrong': 'micchā',
}
M['2-4-2-0'] = {'abhidhamma': 'Abhidhamma', 'classification': 'bhājanīyaṃ'}
M['2-206'] = dict(ABH, **FACTORS)
M['2-206'].update({
 'abstaining': 'paṭivirati', 'away': 'veramaṇī', 'bodily': 'kāya', 'Bodily misconduct': 'kāyaduccaritehi',
 'bodily misconduct': 'kāyaduccaritehi', 'causeway': 'setu', 'committing': 'akaraṇaṃ', 'desisting': 'ārati',
 'destroying': 'ghāto', 'doing': 'akiriyā', 'keeping': 'veramaṇī', 'kinds': NDE, 'limit': 'velā',
 'livelihood': 'ājīvo', 'misconduct': 'duccaritehi', 'overstepping': 'anatikkamo', 'refraining': 'virati',
 'speech': 'vācā', 'transgressing': 'anajjhāpatti', 'verbal': 'vacī', 'verbal misconduct': 'vacīduccaritehi'})
for s in ['2-207', '2-208', '2-209', '2-210', '2-212', '2-213']:
    M[s] = dict(ABH)
M['2-211'] = dict(ABH, **FACTORS)
M['2-212'].update({'effort': 'vāyāmo', 'intention': 'saṅkappo', 'mindfulness': 'sati'})
M['2-214'] = dict(ABH, **{'abhidhamma': 'Abhidhamma', 'classification': 'bhājanīyaṃ', 'finished': NDE})
M['2-4-3-0'] = dict(QA)
M['2-215'] = dict(FOUR)
M['2-216'] = {
 'conflict': 'saraṇā', 'free': 'araṇā', 'involve': 'saraṇā', 'neutral': 'abyākatā', 'noble': 'ariya',
 'noble truths': 'ariyasaccānaṃ', 'truths': 'saccānaṃ', 'unwholesome': 'akusalā', 'wholesome': 'kusalā',
}
M['2-4-3-1-0'] = {'triads': 'Tikaṃ'}
M['2-217'] = {
 'abandoned': 'pahātabbā', 'able': 'upādāniyaṃ', 'accompanied': 'sahagatā', 'accompanied by joy': 'pītisahagatā',
 'accumulation': 'ācaya', 'arise': 'uppādino', 'arisen': 'uppannā', 'belong': NDE, 'belongs': NDE,
 'beyond': 'āsekkhā', 'bound': 'uppādino', 'cannot': 'na', 'cause': 'hetukaṃ', 'causes': 'hetukā',
 'clung': 'upādāniyaṃ', 'defiled': 'saṃkiliṭṭha', 'defilement': 'saṃkilesikaṃ', 'describable': 'vattabbaṃ',
 'described': 'vattabbaṃ', 'dismantling': 'apacaya', 'dominant': 'ādhipati', 'dominant factor': 'ādhipati',
 'equanimity': 'upekkhā', 'examination': 'vicāra', 'expanded': 'mahaggataṃ',
 'expanded object': 'mahaggatārammaṇaṃ', 'external': 'bahiddhā', 'external object': 'bahiddhārammaṇaṃ',
 'factor': 'ādhipati', 'feeling': 'vedanāya', 'fixed': 'niyataṃ', 'future object': 'anāgatārammaṇā',
 'happiness': 'sukha', 'having': NDE, 'inferior': 'hīnaṃ', 'internal': 'ajjhattā',
 'internal and external': 'ajjhattabahiddhā', 'internal object': 'ajjhattārammaṇaṃ', 'invisible': 'anidassana',
 'invisible and offer': 'anidassanaappaṭighā', 'joined': 'sampayuttā',
 'joined with pleasant': 'sukhāya vedanāya sampayuttā', 'joy': 'pīti', 'leads': 'gāmi', 'limited': 'parittaṃ',
 'limited object': 'parittārammaṇaṃ', 'measureless': 'appamāṇā', 'measureless object': 'appamāṇārammaṇaṃ',
 'meditative': 'bhāvanāya', 'meditative development': 'bhāvanāya', 'middling': 'majjhimaṃ',
 'neutral': 'abyākataṃ', 'object': 'ārammaṇaṃ', 'object both internal': 'ajjhattabahiddhārammaṇaṃ',
 'open to defilement': 'saṃkilesikaṃ', 'origin': 'Samudaya', 'outcome': NDE, 'painful': 'dukkhāya',
 'painful feeling': 'dukkhāya vedanāya', 'painful nor pleasant': 'adukkhamasukhāya',
 'past object': 'atītārammaṇā', 'path': 'Magga', 'pleasant': 'sukhāya', 'pleasant feeling': 'sukhāya vedanāya',
 'present object': 'paccuppannārammaṇā', 'produce': 'vipākadhammadhammā', 'produces': 'vipākadhammadhammaṃ',
 'resistance': 'appaṭighā', 'rightness': 'sammatta', 'root': 'hetukā', 'seeing': 'dassanena', 'something': NDE,
 'suffering': 'Dukkha', 'superior': 'paṇītā', 'things': 'dhammā', 'thought': 'vitakka',
 'thought and examination': 'savitakkasavicāraṃ', 'trainees': 'sekkhaṃ', 'training': 'āsekkhā', 'truth': 'saccaṃ',
 'truth of suffering': 'Dukkhasaccaṃ', 'truths': 'saccā', 'undefiled': 'asaṃkiliṭṭha', 'unwholesome': 'akusalaṃ',
 'visible': 'sanidassana', 'wholesome': 'kusalaṃ', 'wrongness': 'micchatta',
}
M['2-4-3-2-0'] = {'pairs': 'Dukaṃ'}
M['2-218'] = dict(QA, **{
 'abandoned': 'pahātabbā', 'able': 'saṃyojaniyā', 'accompanied': 'sahagatā',
 'accompanied by equanimity': 'upekkhāsahagatā', 'accompanied by happiness': 'sukhasahagatā',
 'accompanied by joy': 'pītisahagatā', 'along': 'ānuparivattino', 'analysis': 'vibhaṅgo', 'arise': 'sahabhuno',
 'arising': 'sahabhū', 'belong': NDE, 'belongs': NDE, 'beyond': 'uttarā', 'bound': 'saṃyojaniyā', 'cannot': 'na',
 'cause': 'hetu', 'causes': 'hetū', 'clinging': 'upādānaṃ',
 'clinging joined': 'upādānañceva upādānasampayuttañca', 'clung': 'upādāniyā', 'compounded': 'saṅkhatā',
 'conflict': 'saraṇaṃ', 'consciousness': NDE, 'defiled': 'saṃkiliṭṭhaṃ', 'defilement': 'kileso',
 'defilement joined': 'kileso ceva kilesasampayuttañca', 'defilements': 'kilesā',
 'defilements joined': 'kilesā ceva kilesasampayuttā', 'derived': 'upādā', 'describable': 'vattabbaṃ',
 'described': 'vattabbā', 'dissociated': 'vippayuttaṃ', 'dissociated from clinging': 'upādānavippayuttā',
 'dissociated from wrong': 'parāmāsavippayuttā', 'equanimity': 'upekkhā', 'examination': 'vicāraṃ',
 'existence': NDE, 'external': 'bāhirā', 'factor': 'cetasikaṃ', 'factors': 'cetasikā', 'fetter': 'saṃyojanaṃ',
 'fetter joined': 'saṃyojanañceva saṃyojanasampayuttañca', 'fetters': 'saṃyojanā',
 'fetters joined': 'saṃyojanā ceva saṃyojanasampayuttā', 'fine-material': 'rūpāvacaraṃ',
 'fine-material sphere': 'rūpāvacaraṃ', 'finished': 'niṭṭhito', 'fixed': 'niyataṃ', 'flood': 'ogho',
 'follow': 'ānuparivattino', 'free': 'araṇā', 'grasped': 'parāmaṭṭhā', 'grasping': 'parāmāsā',
 'happiness': 'sukha', 'having': 'sahetukā', 'hindrance': 'nīvaraṇaṃ',
 'hindrance joined': 'nīvaraṇañceva nīvaraṇasampayuttañca', 'hindrances': 'nīvaraṇā',
 'hindrances joined': 'nīvaraṇā ceva nīvaraṇasampayuttā', 'immaterial': 'arūpāni',
 'immaterial sphere': 'arūpāvacaraṃ', 'internal': 'ajjhattaṃ', 'invisible': 'anidassanā', 'involve': 'saraṇaṃ',
 'involves': 'saraṇaṃ', 'joined': 'sampayuttā', 'joined with clinging': 'upādānasampayuttā',
 'joined with mind': 'cittasampayuttā', 'joined with root': 'hetusampayuttā', 'joy': 'pīti', 'kinds': NDE,
 'kinds of consciousness': 'kenaci', 'knowable': 'viññeyyā', 'leads': 'niyyānikaṃ', 'material': 'rūpaṃ',
 'meditative': 'bhāvanāya', 'meditative development': 'bhāvanāya', 'mental': 'cetasikā',
 'mental factor': 'cetasikaṃ', 'mental factors': 'cetasikā', 'mental taint': 'āsavo', 'mind': 'cittaṃ',
 'mingled': 'saṃsaṭṭhā', 'mingled with mind': 'cittasaṃsaṭṭhā', 'object': 'ārammaṇaṃ', 'objects': 'ārammaṇā',
 'obstructed': 'nīvaraṇiyā', 'open to defilement': 'saṃkilesikā', 'origin': 'Samudaya', 'others': 'kenaci',
 'outcome': NDE, 'outside': 'apariyāpannā', 'path': 'Magga', 'produced': 'samuṭṭhānā', 'resistance': 'appaṭighā',
 'root': 'hetu', 'root cause joined': 'hetu ceva hetusampayuttañca', 'round': NDE, 'seeing': 'dassanena',
 'sense': 'kāmāvacaraṃ', 'sense sphere': 'kāmāvacaraṃ', 'sphere': 'āvacaraṃ', 'suffering': 'Dukkha',
 'surpassed': 'sauttarā', 'taint': 'āsavo', 'taint joined': 'āsavo ceva āsavasampayuttañca', 'taints': 'āsavā',
 'taints joined': 'āsavā ceva āsavasampayuttā', 'thought': 'vitakkaṃ', 'tie': 'gantho',
 'tie joined': 'gantho ceva ganthasampayuttañca', 'tied': 'ganthaniyā', 'ties': 'ganthā',
 'ties joined': 'ganthā ceva ganthasampayuttā', 'together': 'saha', 'truth': 'saccaṃ',
 'truth of suffering': 'Dukkhasaccaṃ', 'truths': 'saccā', 'truths are dissociated': 'saccā / vippayuttā',
 'truths are free': 'saccā araṇā', 'truths are joined': 'saccā / sampayuttā',
 'truths are mingled': 'saccā / saṃsaṭṭhā', 'truths arise': 'saccā / sahabhuno',
 'truths follow': 'saccā / ānuparivattino', 'truths offer': 'saccāni appaṭighā', 'unable': 'asaṃyojaniyā',
 'uncompounded': 'asaṅkhataṃ', 'undefiled': 'asaṃkiliṭṭhā', 'unsurpassable': 'anuttarā', 'visible': 'sanidassanaṃ',
 'worldly': 'lokiyā', 'wrong': 'parāmāsā', 'wrong grasping': 'parāmāsā', 'wrongly': 'parāmaṭṭhā',
 'wrongly grasped': 'parāmaṭṭhā', 'yoke': 'yogo',
})

# ---- build ---------------------------------------------------------------
def segments(path):
    segs, buf = {}, []
    for line in path.read_text(encoding='utf-8').splitlines():
        buf.append(line)
        m = re.search(r'\^([\w-]+)\s*$', line)
        if m:
            segs[m.group(1)] = '\n'.join(buf); buf = []
    return segs

def resolve(val, text):
    """Pick the first alternative whose parts all occur; fix first-letter case to match the segment."""
    alts = val if isinstance(val, list) else [val]
    for a in alts:
        if a == NDE:
            return a
        parts = []
        for p in a.split(' / '):
            for c in (p, p[0].upper() + p[1:], p[0].lower() + p[1:]):
                if c in text:
                    parts.append(c); break
            else:
                break
        else:
            return ' / '.join(parts)
    return alts[0]

if __name__ == '__main__':
    segs = segments(root / 'AI_translation' / 'pali' / 'pi-2_split_chapters' / f'{ch}.md')
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
                pairs.append(f'{resolve(m[k], segs[sid])}={k}')
        out.append(f'[{sid}] ' + ', '.join(pairs))
    (d / f'{ch}.mapped.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('written', len(out), 'missing', missing)
