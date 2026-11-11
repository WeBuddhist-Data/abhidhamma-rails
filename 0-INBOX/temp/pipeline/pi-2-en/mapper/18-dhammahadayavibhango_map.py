import pathlib
d = pathlib.Path(__file__).parent
ch = '18-dhammahadayavibhango'
NDE = '(no direct equivalent)'

def layer(*ds):
    """earlier dicts win (= the list that comes first in the English)"""
    out = {}
    for x in reversed(ds):
        out.update(x)
    return out

def over(base, extra):
    """segment-specific values win over the shared lists"""
    return dict(base, **extra)

def cap(s):
    return s[0].upper() + s[1:]

# ---- definitional lists (section comprising everything) ----
KHANDHA = {
 'aggregate': 'khandho', 'aggregate of consciousness': 'viññāṇakkhandho',
 'Aggregate of Consciousness': 'viññāṇakkhandho', 'aggregate of feeling': 'vedanākkhandho',
 'aggregate of material': 'Rūpakkhandho', 'aggregate of mental': 'saṅkhārakkhandho',
 'Aggregate of Mental': 'saṅkhārakkhandho', 'Aggregate of Perception': 'saññākkhandho',
 'aggregate of perception': 'saññākkhandho', 'aggregates': 'khandhā', 'consciousness': 'viññāṇa',
 'feeling': 'vedanā', 'form': 'Rūpa', 'formations': 'saṅkhāra', 'material': 'Rūpa', 'material form': 'Rūpa',
 'mental': 'saṅkhāra', 'Mental Formations': 'saṅkhāra', 'mental formations': 'saṅkhāra', 'perception': 'saññā',
 'therein': 'Tattha'}
AYATANA = {
 'body': 'kāyāyatanaṃ', 'body sense-field': 'kāyāyatanaṃ', 'ear': 'sotāyatanaṃ', 'ear sense-field': 'sotāyatanaṃ',
 'eye': 'Cakkhāyatanaṃ', 'eye sense-field': 'Cakkhāyatanaṃ', 'mental-object': 'dhammāyatanaṃ',
 'mental-object sense-field': 'dhammāyatanaṃ', 'mind': 'manāyatanaṃ', 'mind sense-field': 'manāyatanaṃ',
 'nose': 'ghānāyatanaṃ', 'nose sense-field': 'ghānāyatanaṃ', 'sense-field': 'āyatanaṃ', 'sense-fields': 'āyatanāni',
 'sight': 'rūpāyatanaṃ', 'sight sense-field': 'rūpāyatanaṃ', 'smell': 'gandhāyatanaṃ',
 'smell sense-field': 'gandhāyatanaṃ', 'sound': 'saddāyatanaṃ', 'tangible': 'phoṭṭhabbāyatanaṃ',
 'tangible sense-field': 'phoṭṭhabbāyatanaṃ', 'taste': 'rasāyatanaṃ', 'taste sense-field': 'rasāyatanaṃ',
 'tongue': 'jivhāyatanaṃ', 'tongue sense-field': 'jivhāyatanaṃ', 'twelve': 'dvādasāyatanāni',
 'twelve sense-fields': 'dvādasāyatanāni', 'therein': 'Tattha'}
DHATU = {
 'body': 'kāya', 'body element': 'kāyadhātu', 'body-consciousness': 'kāyaviññāṇa',
 'body-consciousness element': 'kāyaviññāṇadhātu', 'consciousness element': 'viññāṇadhātu', 'ear': 'sota',
 'ear element': 'sotadhātu', 'ear-consciousness': 'sotaviññāṇa', 'ear-consciousness element': 'sotaviññāṇadhātu',
 'eighteen': 'aṭṭhārasa', 'eighteen elements': 'aṭṭhārasa dhātuyo', 'element': 'dhātu', 'elements': 'dhātuyo',
 'eye': 'Cakkhu', 'eye element': 'Cakkhudhātu', 'eye-consciousness': 'cakkhuviññāṇa',
 'eye-consciousness element': 'cakkhuviññāṇadhātu', 'mental-object': 'dhamma', 'mental-object element': 'dhammadhātu',
 'mind': 'mano', 'mind element': 'manodhātu', 'mind-consciousness': 'manoviññāṇa',
 'mind-consciousness element': 'manoviññāṇadhātu', 'nose': 'ghāna', 'nose element': 'ghānadhātu',
 'nose-consciousness': 'ghānaviññāṇa', 'nose-consciousness element': 'ghānaviññāṇadhātu', 'sight': 'rūpa',
 'sight element': 'rūpadhātu', 'smell': 'gandha', 'smell element': 'gandhadhātu', 'sound': 'sadda',
 'sound element': 'saddadhātu', 'tangible': 'phoṭṭhabba', 'tangible element': 'phoṭṭhabbadhātu', 'taste': 'rasa',
 'taste element': 'rasadhātu', 'tongue': 'jivhā', 'tongue element': 'jivhādhātu',
 'tongue-consciousness': 'jivhāviññāṇa', 'tongue-consciousness element': 'jivhāviññāṇadhātu', 'therein': 'Tattha'}
SACCA = {'cessation': 'nirodha', 'origin': 'samudaya', 'path': 'magga', 'suffering': 'Dukkha', 'truth': 'saccaṃ',
         'truth of suffering': 'Dukkhasaccaṃ', 'truths': 'saccāni', 'therein': 'Tattha'}
INDRIYA = {
 'body': 'kāyindriyaṃ', 'body faculty': 'kāyindriyaṃ', 'concentration': 'samādhindriyaṃ', 'confidence': 'saddhindriyaṃ',
 'ear': 'sotindriyaṃ', 'ear faculty': 'sotindriyaṃ', 'equanimity': 'upekkhindriyaṃ',
 'equanimity faculty': 'upekkhindriyaṃ', 'eye': 'Cakkhundriyaṃ', 'eye faculty': 'Cakkhundriyaṃ',
 'faculties': 'indriyāni', 'faculty': 'indriyaṃ', 'faculty of concentration': 'samādhindriyaṃ',
 'faculty of confidence': 'saddhindriyaṃ', 'faculty of energy': 'vīriyindriyaṃ',
 'faculty of femininity': 'itthindriyaṃ', 'faculty of final': 'aññindriyaṃ', 'faculty of masculinity': 'purisindriyaṃ',
 'faculty of mindfulness': 'satindriyaṃ', 'faculty of wisdom': 'paññindriyaṃ', 'femininity': 'itthindriyaṃ',
 'fully': 'aññātāvindriyaṃ', 'grief': 'domanassindriyaṃ', 'happiness': 'sukhindriyaṃ', 'joy': 'somanassindriyaṃ',
 'joy faculty': 'somanassindriyaṃ', 'know': 'anaññātaññassāmītindriyaṃ', 'knowledge': 'aññindriyaṃ',
 'known': 'anaññātaññassāmītindriyaṃ', 'life': 'jīvitindriyaṃ', 'life faculty': 'jīvitindriyaṃ',
 'masculinity': 'purisindriyaṃ', 'mind': 'manindriyaṃ', 'mind faculty': 'manindriyaṃ', 'mindfulness': 'satindriyaṃ',
 'nose': 'ghānindriyaṃ', 'nose faculty': 'ghānindriyaṃ', 'pain': 'dukkhindriyaṃ', 'tongue': 'jivhindriyaṃ',
 'tongue faculty': 'jivhindriyaṃ', 'twenty-two': 'bāvīsatindriyāni', 'twenty-two faculties': 'bāvīsatindriyāni',
 'wisdom': 'paññindriyaṃ', 'therein': 'Tattha'}
HETU = {
 'delusion': 'moho', 'functional': 'kiriyābyākatesu', 'functional neutral': 'kiriyābyākatesu', 'greed': 'Lobho',
 'hate': 'doso', 'neutral': 'abyākata', 'neutral roots': 'abyākatahetū', 'non-delusion': 'amoho',
 'non-greed': 'Alobho', 'non-hate': 'adoso', 'results of wholesome': 'Kusalānaṃ / vipākato', 'root': 'hetu',
 'roots': 'hetū', 'things': 'dhammānaṃ', 'unwholesome': 'akusala', 'unwholesome root': 'akusalahetu',
 'unwholesome roots': 'akusalahetū', 'wholesome': 'kusala', 'wholesome root': 'kusalahetu',
 'wholesome roots': 'kusalahetū', 'wholesome things': 'Kusalānaṃ vā dhammānaṃ', 'therein': 'Tattha'}
AHARA = {'consciousness': 'viññāṇāhāro', 'contact': 'phassāhāro', 'food': 'Kabaḷīkārāhāro',
         'intention': 'manosañcetanāhāro', 'mental': 'manosañcetanāhāro', 'nutriment': 'āhāro', 'nutriments': 'āhārā',
         'solid': 'Kabaḷīkārāhāro', 'therein': 'Tattha'}
PHASSA = {'body-contact': 'kāyasamphasso', 'contact': 'samphasso', 'contacts': 'phassā', 'ear-contact': 'sotasamphasso',
          'eye-contact': 'Cakkhusamphasso', 'mind-consciousness-element': 'manoviññāṇadhātu',
          'mind-element': 'manodhātu', 'mind-element contact': 'manodhātusamphasso', 'nose-contact': 'ghānasamphasso',
          'tongue-contact': 'jivhāsamphasso', 'therein': 'Tattha'}
def born(word, en, en_pl):
    return {'body-contact': 'kāyasamphassa', 'born': 'Cakkhusamphassajā',
            'born of body-contact': 'kāyasamphassajā', 'born of ear-contact': 'sotasamphassajā',
            'born of eye-contact': 'Cakkhusamphassajā', 'born of mind-element': 'manodhātusamphassajā',
            'born of nose-contact': 'ghānasamphassajā', 'born of tongue-contact': 'jivhāsamphassajā',
            'contact': 'samphassa', 'ear-contact': 'sotasamphassa', 'eye-contact': 'Cakkhusamphassa',
            en: word, en + ' born': 'Cakkhusamphassajā ' + word, cap(en) + ' born': 'Cakkhusamphassajā ' + word,
            en_pl: word, 'mind-consciousness-element': 'manoviññāṇadhātu', 'mind-element': 'manodhātu',
            'mind-element contact': 'manodhātusamphassa', 'nose-contact': 'ghānasamphassa',
            'tongue-contact': 'jivhāsamphassa', 'therein': 'Tattha'}
VEDANA = born('vedanā', 'feeling', 'feelings')
SANNA = born('saññā', 'perception', 'perceptions')
CETANA = born('cetanā', 'intention', 'intentions')
CITTA = {'body-consciousness': 'kāyaviññāṇaṃ', 'consciousness element': 'viññāṇadhātu', 'ear-consciousness': 'sotaviññāṇaṃ',
         'element': 'dhātu', 'eye-consciousness': 'Cakkhuviññāṇaṃ', 'mind': 'mano', 'mind element': 'manodhātu',
         'mind-consciousness': 'manoviññāṇa', 'mind-consciousness element': 'manoviññāṇadhātu', 'minds': 'cittāni',
         'nose-consciousness': 'ghānaviññāṇaṃ', 'tongue-consciousness': 'jivhāviññāṇaṃ', 'therein': 'Tattha'}
SUMMARY = {'aggregates': 'khandhā', 'contacts': 'phassā', 'eighteen': 'aṭṭhārasa',
           'eighteen elements': 'aṭṭhārasa dhātuyo', 'elements': 'dhātuyo', 'faculties': 'indriyāni',
           'feelings': 'vedanā', 'intentions': 'cetanā', 'minds': 'cittāni', 'nutriments': 'āhārā',
           'perceptions': 'saññā', 'roots': 'hetū', 'sense-fields': 'āyatanāni', 'truths': 'saccāni',
           'twelve': 'dvādasāyatanāni', 'twelve sense-fields': 'dvādasāyatanāni', 'twenty-two': 'bāvīsatindriyāni',
           'twenty-two faculties': 'bāvīsatindriyāni'}
def realm(word, en, cap_en):
    """word = the realm locative as it stands, e.g. 'kāmadhātuyā'"""
    stem = word[:-len('dhātuyā')] if word.endswith('dhātuyā') else word
    return {'element': 'dhātuyā', en + ' element': word, cap_en: word, en: stem}
KAMA = lambda w='Kāmadhātuyā': dict(realm(w, 'sense-pleasure', 'Sense-Pleasure Element'), **{'pleasure element': w})
RUPA = lambda w='Rūpadhātuyā': realm(w, 'material-form', 'Material-Form Element')
ARUPA = lambda w='Arūpadhātuyā': realm(w, 'immaterial', 'Immaterial Element')
QA_SEC = {'section': 'vāro'}

M = {}
M['2-18-0'] = {'analysis': 'vibhaṅgo', 'heart': 'hadaya', 'teaching': 'Dhamma'}
M['2-18-1-0'] = {'comprising': 'saṅgāhika', 'everything': 'Sabba', 'section': 'vāro'}
M['2-978'] = dict(SUMMARY)
M['2-979'] = dict(KHANDHA)
M['2-980'] = dict(AYATANA)
M['2-981'] = dict(DHATU)
M['2-982'] = dict(SACCA)
M['2-983'] = dict(INDRIYA)
M['2-984'] = dict(HETU)
M['2-985'] = dict(AHARA)
M['2-986'] = dict(PHASSA)
M['2-987'] = dict(VEDANA)
M['2-988'] = dict(SANNA)
M['2-989'] = dict(CETANA)
M['2-990'] = dict(CITTA)
M['2-18-2-0'] = {'non-occurrence': 'ānuppatti', 'occurrence': 'Uppattānuppattivāro', 'section': 'vāro'}
M['2-18-2-1-0'] = {'element': 'dhātu', 'pleasure element': 'Kāmadhātu', 'sense-pleasure': 'Kāma',
                   'sense-pleasure element': 'Kāmadhātu', 'Sense-Pleasure Element': 'Kāmadhātu'}
M['2-991'] = layer(KAMA(), SUMMARY)
FULL = (KHANDHA, AYATANA, DHATU, SACCA, INDRIYA, HETU, AHARA, PHASSA, VEDANA, SANNA, CETANA, CITTA)
M['2-992'] = layer(KAMA('kāmadhātuyā'), *FULL)
M['2-992'].update({'aggregates': 'khandhā', 'contacts': 'phassā', 'feelings': 'vedanā', 'perceptions': 'saññā',
                   'intentions': 'cetanā', 'known': 'aññātāvindriyaṃ', 'truths': 'saccāni', 'roots': 'hetū',
                   'faculties': 'indriyāni', 'minds': 'cittāni', 'sense-fields': 'āyatanāni', 'elements': 'dhātuyo'})
M['2-18-2-2-0'] = {'element': 'dhātu', 'material-form': 'Rūpa', 'Material-Form Element': 'Rūpadhātu',
                   'material-form element': 'Rūpadhātu'}
M['2-993'] = layer(RUPA(), SUMMARY, {'fourteen': 'cuddasindriyāni', 'Fourteen faculties': 'cuddasindriyāni',
                                     'sense-fields': 'āyatanā'})
M['2-993'].update({'sense-fields': 'āyatanā'})
M['2-994'] = layer(RUPA('rūpadhātuyā'), *FULL)
M['2-994'].update({'aggregates': 'khandhā', 'contacts': 'phassā', 'feelings': 'vedanā', 'perceptions': 'saññā',
                   'intentions': 'cetanā', 'feeling': 'vedanā', 'truths': 'saccāni', 'roots': 'hetū',
                   'faculties': 'indriyāni', 'minds': 'cittāni', 'sense-fields': 'āyatanāni', 'elements': 'dhātuyo',
                   'fourteen': 'cuddasindriyāni', 'Fourteen faculties': 'cuddasindriyāni', 'contact': 'Phassāhāro',
                   'food': NDE})
M['2-18-2-3-0'] = {'element': 'dhātu', 'immaterial': 'Arūpa', 'immaterial element': 'Arūpadhātu',
                   'Immaterial Element': 'Arūpadhātu'}
M['2-995'] = layer(ARUPA(), {'aggregates': 'khandhā', 'contact': 'phasso', 'elements': 'dhātuyo',
                             'eleven': 'ekādasindriyāni', 'Eleven faculties': 'ekādasindriyāni',
                             'faculties': 'indriyāni', 'feeling': 'vedanā', 'intention': 'cetanā', 'mind': 'cittaṃ',
                             'minds': 'cittāni', 'nutriments': 'āhārā', 'perception': 'saññā', 'roots': 'hetū',
                             'sense-fields': 'āyatanāni', 'truths': 'saccāni'})
# immaterial / not-included definitions: lists start with capitalised Mana-/Mano- words
ARUPA_LISTS = layer(
 {k: v for k, v in KHANDHA.items() if 'material' not in k and k != 'form'},
 {'mind': 'Manāyatanaṃ', 'mind sense-field': 'Manāyatanaṃ', 'mental-object': 'dhammāyatanaṃ',
  'mental-object sense-field': 'dhammāyatanaṃ', 'sense-field': 'āyatanaṃ', 'sense-fields': 'āyatanāni'},
 {'consciousness element': 'viññāṇadhātu', 'element': 'dhātu', 'elements': 'dhātuyo',
  'mental-object element': 'dhammadhātu', 'mind-consciousness': 'Manoviññāṇa',
  'mind-consciousness element': 'Manoviññāṇadhātu'},
 SACCA,
 {k: v for k, v in INDRIYA.items() if k in (
  'concentration', 'confidence', 'equanimity', 'equanimity faculty', 'faculties', 'faculty',
  'faculty of concentration', 'faculty of confidence', 'faculty of energy', 'faculty of final',
  'faculty of mindfulness', 'faculty of wisdom', 'fully', 'joy', 'joy faculty', 'know', 'knowledge', 'known', 'life',
  'life faculty', 'mindfulness', 'wisdom')},
 {'mind faculty': 'Manindriyaṃ'},
 HETU,
 {'consciousness': 'viññāṇāhāro', 'contact': 'Phassāhāro', 'intention': 'manosañcetanāhāro',
  'mental': 'manosañcetanāhāro', 'nutriment': 'āhāro', 'nutriments': 'āhārā'},
 {'mind-consciousness-element': 'Manoviññāṇadhātu'})
ARUPA_LISTS['aggregate of feeling'] = 'Vedanākkhandho'  # the four-aggregate list starts with it
M['2-996'] = layer(ARUPA('arūpadhātuyā'), ARUPA_LISTS)
M['2-996'].update({'eleven': 'ekādasindriyāni', 'Eleven faculties': 'ekādasindriyāni','known': 'aññātāvindriyaṃ', 'aggregates': 'khandhā', 'feeling': 'vedanā',
                   'mental': 'saṅkhāra'})
M['2-18-2-4-0'] = {'not-included': 'Apariyāpannaṃ'}
M['2-997'] = {'aggregates': 'khandhā', 'contact': 'phasso', 'elements': 'dhātuyo', 'faculties': 'indriyāni',
              'feeling': 'vedanā', 'intention': 'cetanā', 'mind': 'cittaṃ', 'minds': 'cittāni', 'nutriments': 'āhārā',
              'perception': 'saññā', 'roots': 'hetū', 'sense-fields': 'āyatanāni', 'sphere': NDE,
              'truths': 'saccāni', 'twelve': 'dvādasindriyāni', 'Twelve faculties': 'dvādasindriyāni'}
M['2-998'] = layer(ARUPA_LISTS, {'twelve': 'dvādasindriyāni', 'Twelve faculties': 'dvādasindriyāni'})
M['2-998'].update({'aggregates': 'khandhā', 'feeling': 'vedanā', 'mental': 'saṅkhāra', 'path': 'Magga',
                   'wholesome things': 'Kusalānaṃ dhammānaṃ', 'fully': 'aññātāvindriyaṃ'})
M['2-18-3-0'] = {'section': 'vāro'}
M['2-18-3-1-0'] = dict(M['2-18-2-1-0'])
M['2-999'] = {'aggregates': 'khandhānaṃ', 'element': 'dhātu', 'minds': 'cittānaṃ', 'pleasure element': 'kāmadhātu',
              'sense-pleasure': 'kāma', 'sense-pleasure element': 'kāmadhātu', 'Sense-Pleasure Element': 'kāmadhātu'}
# "included / not included" and later analytic sections: the 12 sets named by number
ANAL = {
 'aggregate': 'khandho', 'aggregate of material': 'Rūpakkhandho', 'aggregates': 'khandhā',
 'consciousness element': 'viññāṇadhātu', 'contact': 'samphasso', 'contacts': 'phassā', 'element': 'dhātu',
 'elements': 'dhātuyo', 'faculties': 'indriyā', 'faculty': 'indriyaṃ', 'feelings': 'vedanā',
 'food': 'Kabaḷīkāro', 'form': 'Rūpa', 'intentions': 'cetanā', 'material': 'Rūpa', 'material form': 'Rūpa',
 'mind-consciousness': 'manoviññāṇa', 'mind-consciousness element': 'manoviññāṇadhātu',
 'mind-consciousness-element': 'manoviññāṇadhātu', 'minds': 'cittā', 'nutriment': 'āhāro', 'nutriments': 'āhārā',
 'origin': 'Samudaya', 'cessation': 'Nirodha', 'path': 'Magga', 'perceptions': 'saññā', 'roots': 'hetū',
 'sense-fields': 'āyatanā', 'sixteen': 'Soḷasa', 'Sixteen elements': 'Soḷasa dhātuyo', 'solid': 'Kabaḷīkāro',
 'suffering': 'dukkha', 'ten': 'Dasāyatanā', 'Ten sense-fields': 'Dasāyatanā', 'ten sense-fields': 'Dasāyatanā',
 'ten faculties': 'Dasindriyā', 'Ten faculties': 'Dasindriyā', 'Ten elements': 'Dasa dhātuyo',
 'ten elements': 'Dasa dhātuyo', 'truth': 'saccaṃ', 'truth of suffering': 'dukkhasaccaṃ', 'truths': 'saccā',
 'unwholesome': 'akusala', 'unwholesome roots': 'akusalahetū', 'wholesome': 'kusala',
 'wholesome roots': 'kusalahetū', 'neutral': 'abyākata', 'neutral roots': 'abyākatahetū',
 'mental-object': 'Dhammāyatanaṃ', 'mental-object sense-field': 'Dhammāyatanaṃ',
 'mental-object element': 'Dhammadhātu', 'mind': 'Manāyatanaṃ', 'mind sense-field': 'Manāyatanaṃ',
 'sense-field': 'āyatanaṃ', 'life': 'Jīvitindriyaṃ', 'life faculty': 'Jīvitindriyaṃ',
 'fourteen': 'Cuddasindriyā', 'Fourteen faculties': 'Cuddasindriyā'}
def incl(word):
    r = {'element': 'dhātu'}
    return r
M['2-1000'] = dict(ANAL, **{'elements are included': 'dhātuyo kāmadhātupariyāpannā', 'pleasure element': 'kāmadhātu',
                            'sense-pleasure': 'kāma', 'Sense-Pleasure Element': 'kāmadhātu',
                            'sense-pleasure element': 'kāmadhātu', 'suffering': 'dukkha', 'truths': 'saccā'})
M['2-18-3-2-0'] = dict(M['2-18-2-2-0'])
M['2-1001'] = {'aggregates': 'khandhānaṃ', 'element': 'dhātu', 'material-form': 'rūpa',
               'material-form element': 'rūpadhātu', 'Material-Form Element': 'rūpadhātu', 'minds': 'cittānaṃ'}
M['2-1002'] = dict(ANAL, **{'material-form': 'rūpa', 'material-form element': 'rūpadhātu',
                            'Material-Form Element': 'rūpadhātu', 'thirteen': 'Terasindriyā',
                            'thirteen faculties': 'Terasindriyā', 'Thirteen faculties': 'Terasindriyā',
                            'truths': 'saccāni'})
M['2-18-3-3-0'] = dict(M['2-18-2-3-0'])
M['2-1003'] = {'aggregates': 'khandhānaṃ', 'element': 'dhātu', 'immaterial': 'arūpa',
               'immaterial element': 'arūpadhātu', 'Immaterial Element': 'arūpadhātu', 'minds': 'cittānaṃ'}
M['2-1004'] = dict(ANAL, **{'immaterial': 'arūpa', 'immaterial element': 'arūpadhātu',
                            'Immaterial Element': 'arūpadhātu', 'truths': 'saccāni', 'suffering': 'Dukkha',
                            'truth of suffering': 'Dukkhasaccaṃ'})
M['2-1005'] = {'aggregates': 'khandhānaṃ', 'minds': 'cittānaṃ'}
M['2-1006'] = dict(ANAL, **{'elements are included': 'dhātuyo pariyāpannā'})
M['2-18-4-0'] = {'appear': NDE, 'section': 'vāro', 'Section Showing': 'dassanavāro', 'showing': 'dassana',
                 'things': 'Dhamma'}
M['2-18-4-1-0'] = dict(M['2-18-2-1-0'])
REBIRTH = {'appear': 'pātubhavanti', 'appears': 'pātubhavati', 'moment': 'khaṇe',
           'moment of rebirth': 'upapattikkhaṇe', 'rebirth': 'upapatti'}
M['2-1007'] = over(layer(KAMA(), REBIRTH), {
 'aggregates': 'khandhā', 'beings': NDE, 'contact': 'phasso', 'elements': 'dhātuyo', 'eleven': 'ekādasāyatanāni',
 'Eleven elements': 'ekādasa dhātuyo', 'eleven elements': 'ekādasa dhātuyo',
 'Eleven sense-fields': 'ekādasāyatanāni', 'eleven sense-fields': 'ekādasāyatanāni', 'faculties': 'indriyāni',
 'feeling': 'vedanā', 'fourteen': 'cuddasindriyāni', 'Fourteen faculties': 'cuddasindriyāni', 'intention': 'cetanā',
 'mind': 'cittaṃ', 'minds': 'cittāni', 'nutriments': 'āhārā', 'perception': 'saññā', 'roots': 'hetū',
 'sense-fields': 'āyatanāni', 'ten': 'dasāyatanāni', 'Ten elements': 'dasa dhātuyo', 'ten elements': 'dasa dhātuyo',
 'ten faculties': 'dasindriyāni', 'Ten faculties': 'dasindriyāni', 'Ten sense-fields': 'dasāyatanāni',
 'ten sense-fields': 'dasāyatanāni', 'thirteen': 'terasindriyāni', 'thirteen faculties': 'terasindriyāni',
 'Thirteen faculties': 'terasindriyāni', 'truth': 'saccaṃ', 'twelve': 'dvādasindriyāni',
 'Twelve faculties': 'dvādasindriyāni'})
M['2-1008'] = layer(KAMA(), REBIRTH, KHANDHA)
M['2-1008'].update({'aggregates': 'khandhā'})
BEINGS = {
 'animals': 'tiracchānagatānaṃ', 'beings': 'sattānaṃ', 'birth': 'jaccandhānaṃ', 'blind': 'jaccandhānaṃ',
 'complete': 'paripuṇṇāyatanānaṃ', 'deaf': 'badhirānaṃ', 'demons': 'asurānaṃ', 'eon': 'kappikānaṃ',
 'ghosts': 'petānaṃ', 'gods': 'devānaṃ', 'hell': 'nerayikānaṃ', 'humans': 'manussānaṃ', 'reborn': 'opapātikānaṃ',
 'reborn animals': 'opapātikānaṃ tiracchānagatānaṃ', 'reborn demons': 'opapātikānaṃ asurānaṃ',
 'reborn ghosts': 'opapātikānaṃ petānaṃ', 'sense': 'Kāmāvacarānaṃ', 'sense sphere': 'Kāmāvacarānaṃ',
 'sphere': 'āvacarānaṃ', 'spontaneously': 'opapātikānaṃ', 'spontaneously reborn': 'opapātikānaṃ',
 'spontaneously reborn animals': 'opapātikānaṃ tiracchānagatānaṃ',
 'spontaneously reborn demons': 'opapātikānaṃ asurānaṃ', 'spontaneously reborn ghosts': 'opapātikānaṃ petānaṃ',
 'womb-born': 'Gabbhaseyyakānaṃ'}
AY_LOWER = dict(AYATANA, eye='cakkhāyatanaṃ', **{'eye sense-field': 'cakkhāyatanaṃ'})
M['2-1009'] = over(layer(KAMA(), REBIRTH, BEINGS, AY_LOWER), {
 'eleven': 'ekādasāyatanāni', 'Eleven sense-fields': 'ekādasāyatanāni', 'eleven sense-fields': 'ekādasāyatanāni',
 'rebirth eleven': 'upapattikkhaṇe ekādasāyatanāni', 'rebirth eleven sense-fields': 'upapattikkhaṇe ekādasāyatanāni',
 'rebirth ten': 'upapattikkhaṇe dasāyatanāni', 'rebirth ten sense-fields': 'upapattikkhaṇe dasāyatanāni',
 'ten': 'dasāyatanāni', 'Ten sense-fields': 'dasāyatanāni', 'ten sense-fields': 'dasāyatanāni'})
M['2-1009'].update({'sense-fields': 'āyatanāni'})
DH_LOWER = dict(DHATU, eye='cakkhu', **{'eye element': 'cakkhudhātu'})
M['2-1010'] = over(layer(KAMA(), REBIRTH, BEINGS, DH_LOWER), {
 'elements': 'dhātuyo', 'eleven': 'ekādasa', 'Eleven elements': 'ekādasa dhātuyo', 'eleven elements': 'ekādasa dhātuyo',
 'rebirth eleven': 'upapattikkhaṇe ekādasa', 'rebirth eleven elements': 'upapattikkhaṇe ekādasa dhātuyo',
 'rebirth ten': 'upapattikkhaṇe dasa', 'rebirth ten elements': 'upapattikkhaṇe dasa dhātuyo', 'ten': 'dasa',
 'Ten elements': 'dasa dhātuyo', 'ten elements': 'dasa dhātuyo', 'sense-fields': 'āyatanānaṃ'})
M['2-1011'] = layer(KAMA(), REBIRTH, {'suffering': 'Dukkha', 'truth': 'saccaṃ', 'truth of suffering': 'Dukkhasaccaṃ'})
IN_LOWER = dict(INDRIYA, eye='cakkhundriyaṃ', **{'eye faculty': 'cakkhundriyaṃ'})
M['2-1012'] = over(layer(KAMA(), REBIRTH, BEINGS, IN_LOWER), {
 'reborn ghosts': 'Opapātikānaṃ petānaṃ', 'spontaneously reborn ghosts': 'Opapātikānaṃ petānaṃ',
 'aside': 'ṭhapetvā', 'associated': 'sampayuttānaṃ', 'dissociated': 'vippayuttānaṃ',
 'dissociated from knowledge': 'ñāṇavippayuttānaṃ', 'faculties': 'indriyāni', 'fourteen': 'cuddasindriyāni',
 'Fourteen faculties': 'cuddasindriyāni', 'knowledge': 'ñāṇa', 'rebirth ten': 'upapattikkhaṇe dasindriyāni',
 'rebirth thirteen': 'upapattikkhaṇe terasindriyāni', 'rebirth thirteen faculties': 'upapattikkhaṇe terasindriyāni',
 'roots': 'sahetukānaṃ', 'sense-fields': 'āyatanānaṃ', 'setting': 'ṭhapetvā', 'sex': 'napuṃsakānaṃ',
 'ten': 'dasindriyāni', 'ten faculties': 'dasindriyāni', 'Ten faculties': 'dasindriyāni',
 'thirteen': 'terasindriyāni', 'thirteen faculties': 'terasindriyāni', 'Thirteen faculties': 'terasindriyāni',
 'twelve': 'dvādasindriyāni', 'Twelve faculties': 'dvādasindriyāni'})
VIPAKAHETU = {'non-delusion': 'amoho', 'non-greed': 'alobho', 'non-hate': 'adoso', 'resultant': 'vipāka',
              'resultant root': 'vipākahetu', 'root': 'hetu', 'roots': 'hetū'}
M['2-1013'] = over(layer(KAMA(), REBIRTH, BEINGS, VIPAKAHETU), {
 'associated': 'sampayuttānaṃ', 'dissociated': 'vippayuttānaṃ', 'dissociated from knowledge': 'ñāṇavippayuttānaṃ',
 'knowledge': 'ñāṇa', 'remaining': 'Avasesānaṃ', 'womb-born': 'gabbhaseyyakānaṃ'})
M['2-1014'] = over(layer(KAMA(), REBIRTH, AHARA), {
 'consciousness element': 'viññāṇadhātu', 'feeling': 'vedanā', 'food': 'Kabaḷīkāro', 'solid': 'Kabaḷīkāro',
 'mind': 'cittaṃ', 'mind-consciousness': 'Manoviññāṇa', 'mind-consciousness element': 'Manoviññāṇadhātu',
 'mind-consciousness-element': 'Manoviññāṇadhātu', 'perception': 'saññā'})
M['2-18-4-2-0'] = dict(M['2-18-2-2-0'])
M['2-1015'] = over(layer(RUPA(), REBIRTH), {
 'aggregates': 'khandhā', 'aside': 'ṭhapetvā', 'contact': 'phasso', 'elements': 'dhātuyo', 'faculties': 'indriyāni',
 'feeling': 'vedanā', 'gods': 'devānaṃ', 'intention': 'cetanā', 'mind': 'cittaṃ', 'minds': 'cittāni',
 'non-percipient': 'asaññasattānaṃ', 'non-percipient gods': 'asaññasattānaṃ devānaṃ', 'nutriments': 'āhārā',
 'perception': 'saññā', 'roots': 'hetū', 'sense-fields': 'āyatanāni', 'setting': 'ṭhapetvā',
 'ten': 'dasindriyāni', 'ten faculties': 'dasindriyāni', 'Ten faculties': 'dasindriyāni', 'truth': 'saccaṃ'})
RUPA_LISTS = layer(
 KHANDHA,
 {'eye': 'Cakkhāyatanaṃ', 'eye sense-field': 'Cakkhāyatanaṃ', 'sight': 'rūpāyatanaṃ', 'sight sense-field': 'rūpāyatanaṃ',
  'ear': 'sotāyatanaṃ', 'ear sense-field': 'sotāyatanaṃ', 'mind': 'manāyatanaṃ', 'mind sense-field': 'manāyatanaṃ',
  'mental-object': 'dhammāyatanaṃ', 'mental-object sense-field': 'dhammāyatanaṃ', 'sense-field': 'āyatanaṃ',
  'sense-fields': 'āyatanāni'},
 {'eye element': 'Cakkhudhātu', 'sight element': 'rūpadhātu', 'ear element': 'sotadhātu',
  'mind-consciousness': 'manoviññāṇa', 'mind-consciousness element': 'manoviññāṇadhātu',
  'mental-object element': 'dhammadhātu', 'element': 'dhātu', 'elements': 'dhātuyo',
  'consciousness element': 'viññāṇadhātu'},
 {'suffering': 'Dukkha', 'truth': 'saccaṃ', 'truth of suffering': 'Dukkhasaccaṃ'},
 {k: v for k, v in INDRIYA.items() if k in (
  'concentration', 'confidence', 'equanimity', 'equanimity faculty', 'faculties', 'faculty',
  'faculty of concentration', 'faculty of confidence', 'faculty of energy', 'faculty of mindfulness',
  'faculty of wisdom', 'joy', 'joy faculty', 'life', 'life faculty', 'mind faculty', 'mindfulness', 'wisdom',
  'ear faculty', 'eye faculty')},
 {'non-delusion': 'amoho', 'non-greed': 'Alobho', 'non-hate': 'adoso', 'resultant': 'vipāka',
  'resultant root': 'vipākahetu', 'root': 'hetu', 'roots': 'hetū'},
 {'contact': 'Phassāhāro', 'intention': 'manosañcetanāhāro', 'nutriment': 'āhāro', 'nutriments': 'āhārā'},
 {'mind-consciousness-element': 'Manoviññāṇadhātu'})
M['2-1016'] = over(layer(RUPA(), REBIRTH, RUPA_LISTS), {'ten': 'dasindriyāni', 'ten faculties': 'dasindriyāni',
                                                  'Ten faculties': 'dasindriyāni'})
M['2-1016'].update({'faculties': 'indriyāni', 'aggregates': 'khandhā', 'sense-fields': 'āyatanāni'})
M['2-18-4-3-0'] = {'beings': 'sattā', 'non-percipient': 'Asañña'}
M['2-1017'] = over(REBIRTH, {
 'aggregate': 'khandho', 'aggregate of material': 'rūpakkhandho', 'aggregates': 'khandhā', 'contact': 'aphassakā',
 'element': 'dhātu', 'elements': 'dhātuyo', 'faculty': 'indriyaṃ', 'feeling': 'avedanakā', 'form': 'rūpa',
 'gods': 'devānaṃ', 'intention': 'acetanakā', 'life': 'jīvitindriyaṃ', 'life faculty': 'jīvitindriyaṃ',
 'material': 'rūpa', 'material form': 'rūpa', 'material life faculty': 'rūpajīvitindriyaṃ',
 'mental-object': 'dhammāyatanaṃ', 'mental-object element': 'dhammadhātu',
 'mental-object sense-field': 'dhammāyatanaṃ', 'mind': 'acittakā', 'minds': 'cittāni',
 'non-percipient': 'Asaññasattānaṃ', 'non-percipient gods': 'Asaññasattānaṃ devānaṃ', 'nutriment': 'anāhārā',
 'perception': 'asaññakā', 'roots': 'ahetukā', 'sense-field': 'āyatanaṃ', 'sense-fields': 'āyatanāni',
 'sight': 'rūpāyatanaṃ', 'sight element': 'rūpadhātu', 'sight sense-field': 'rūpāyatanaṃ', 'suffering': 'dukkha',
 'truth': 'saccaṃ', 'truth of suffering': 'dukkhasaccaṃ'})
M['2-18-4-4-0'] = dict(M['2-18-2-3-0'])
M['2-1018'] = over(layer(ARUPA(), REBIRTH), {
 'aggregates': 'khandhā', 'contact': 'phasso', 'elements': 'dhātuyo', 'faculties': 'indriyāni', 'feeling': 'vedanā',
 'intention': 'cetanā', 'mind': 'cittaṃ', 'minds': 'cittāni', 'nutriments': 'āhārā', 'perception': 'saññā',
 'roots': 'hetū', 'sense-fields': 'āyatanāni', 'truth': 'saccaṃ'})
M['2-1019'] = layer(ARUPA(), REBIRTH, ARUPA_LISTS, VIPAKAHETU)
M['2-1019'].update({'aggregates': 'khandhā', 'feeling': 'vedanā', 'mental': 'saṅkhāra', 'non-greed': 'Alobho',
                    'faculties': 'indriyāni'})
M['2-18-5-0'] = {'different': 'antara', 'planes': 'Bhūmantaradassanavāro', 'section': 'vāro',
                 'Section Showing': 'dassanavāro', 'showing': 'dassana'}
M['2-1020'] = dict(KHANDHA, **{
 'aggregate of material': 'rūpakkhandho', 'aggregates': 'khandha', 'Akaniṭṭha gods': 'akaniṭṭhe deve',
 'attained': 'samāpannassa', 'consciousness': 'viññāṇaṃ', 'creations': 'paranimmitavasavattī',
 'dwelling': 'vihārissa', 'element': 'dhātu', 'elements': 'dhātu', 'factors': 'cetasikā', 'feeling': 'vedanā',
 'field': 'āyatanūpage', 'field of infinite': 'ākāsānañcāyatanūpage', 'fine-material': 'rūpāvacarā',
 'fine-material sphere': 'rūpāvacarā', 'form': 'rūpaṃ', 'formations': 'saṅkhārā', 'fruits': 'phalāni', 'gods': 'deve',
 'gods who wield': 'paranimmitavasavattī deve', 'happily': 'sukhavihārissa', 'hell': 'nirayaṃ',
 'immaterial': 'arūpāvacarā', 'immaterial sphere': 'arūpāvacarā', 'infinite': 'ākāsānañcāyatanūpage',
 'infinite space': 'ākāsānañcāyatanūpage', 'interval': 'antare', 'life': 'diṭṭhadhamma', 'limit': 'pariyantaṃ',
 'limit the gods': 'deve antokaritvā', 'material': 'rūpaṃ', 'material form': 'rūpaṃ', 'mental': 'cetasikā',
 'mental factors': 'cetasikā', 'mental taints': 'Sāsavā', 'mind': 'citta',
 'neither-perception-nor-non-perception': 'nevasaññānāsaññāyatanūpage', 'neutral': 'kusalākusalabyākatā',
 'others': 'paranimmitavasavattī', 'paths': 'Maggā', 'perception': 'saññā', 'power': 'vasavattī',
 'reached the field': 'āyatanūpage', 'reborn': 'upapannassa', 'sense': 'Kāmāvacarā', 'sense sphere': 'Kāmāvacarā',
 'sense-fields': 'āyatanā', 'space': 'ākāsānañcāyatanūpage', 'sphere': 'āvacarā',
 'sphere and things': 'Kāmāvacarā dhammā', 'subject to mental': 'Sāsavā', 'taints': 'Sāsavā', 'taking': 'karitvā',
 'things': 'dhammā', 'things not included': 'apariyāpannā dhammā', 'things subject': 'Sāsavā / dhammā',
 'unconditioned': 'asaṅkhatā', 'unconditioned element': 'asaṅkhatā ca dhātu', 'unwholesome': 'kusalākusalabyākatā',
 'upper': 'uparito', 'wholesome': 'kusalākusalabyākatā', 'wield': 'vasavattī'})
M['2-18-6-0'] = {'generating': 'Uppādaka', 'Generating Action': 'Uppādakakamma', 'life': 'āyu', 'measure': 'pamāṇa',
                 'Measure of Life': 'āyuppamāṇa', 'section': 'vāro'}
M['2-18-6-1-0'] = {'generating': 'Uppādaka', 'Generating Action': 'Uppādakakammaṃ'}
M['2-1021'] = {
 'arahants': 'arahanto', 'beings': NDE, 'brahmins': 'brāhmaṇa', 'convention': 'sammuti', 'creating': 'nimmāna',
 'creations': 'paranimmitavasavattīnaṃ', 'delight': 'ratīnaṃ', 'gifts': 'Dānaṃ', 'gods': 'devā',
 'gods who delight': 'nimmānaratīnaṃ devānaṃ', 'gods who wield': 'paranimmitavasavattīnaṃ devānaṃ',
 'Great Kings': 'mahārājike', 'having': NDE, 'householders': 'gahapati', 'kept': 'katvā', 'kinds': NDE,
 'kings': 'rājāno', 'nobles': 'khattiya', 'observance': 'uposatha', 'others': 'paranimmitavasavattīnaṃ',
 'power': 'vasavattīnaṃ', 'princes': 'kumārā', 'purity': 'visuddhi', 'queens': 'deviyo', 'realm': NDE,
 'rebirth': 'upapatti', 'reborn': 'upapajjanti', 'thirty-three': 'tāvatiṃsānaṃ', 'tusita': 'tusitānaṃ',
 'Tusita gods': 'tusitānaṃ devānaṃ', 'undertaken': 'samādiyitvā', 'upwards': 'tadupari', 'virtue': 'sīlaṃ',
 'wealthy': 'mahāsālānaṃ', 'wield': 'vasavattīnaṃ', 'Yāma gods': 'yāmānaṃ devānaṃ'}
M['2-18-6-2-0'] = {'life': 'Āyu', 'measure': 'pamāṇaṃ', 'Measure of Life': 'Āyuppamāṇaṃ'}
LIFE = {'life': 'āyu', 'measure': 'pamāṇaṃ', 'Measure of Life': 'āyuppamāṇaṃ'}
M['2-1022'] = dict(LIFE, **{'beings': NDE, 'human': 'Manussānaṃ', 'hundred': 'sataṃ'})
M['2-1023'] = dict(LIFE, **{
 'abounding': 'samiddhino', 'counted': 'saṅkhāto', 'creating': 'nimmāna', 'creations': 'paranimmitavasavattīnaṃ',
 'crores': 'koṭiyo', 'delight': 'ratīnaṃ', 'divine': 'dibbāni', 'divine years': 'dibbāni / vassasatāni',
 'every': 'sabba', 'fifty': 'paññāsa', 'forty-four': NDE, 'gods': 'devānaṃ',
 'gods who delight': 'nimmānaratīnaṃ devānaṃ', 'gods who wield': 'paranimmitavasavattīnaṃ devānaṃ',
 'Great Kings': 'mahārājikānaṃ', 'human': 'mānusakāni', 'human reckoning': 'Manussānaṃ gaṇanāya',
 'human years': 'mānusakāni / vassāni', 'hundred': 'satāni', 'hundred human': 'mānusakaṃ vassasataṃ',
 'hundred human years': 'mānusakaṃ vassasataṃ', 'kings': 'mahārājikānaṃ', 'make a month': 'māso',
 'make a year': 'saṃvaccharo', 'million': NDE, 'million years': NDE, 'months make': 'dvādasamāsiyo saṃvaccharo',
 'night': 'rattindivo', 'nights': 'rattiyo', 'nights make': 'rattiyo māso', 'others': 'paranimmitavasavattīnaṃ',
 'pleasure': 'kāma', 'power': 'vasavattīnaṃ', 'proclaimed': 'pakāsitāti', 'realms': NDE, 'reckoning': 'gaṇanāya',
 'sense': 'kāma', 'sense pleasure': 'kāma', 'sense-sphere': 'kāmāvacarā', 'seventy-six': NDE, 'sixteen': 'soḷasa',
 'thirty': 'tiṃsa', 'thirty-six': NDE, 'thirty-three': 'tāvatiṃsānaṃ', 'thousand': 'sahassaṃ',
 'tusita': 'tusitānaṃ', 'Tusita gods': 'tusitānaṃ devānaṃ', 'twelve': 'dvādasa', 'twenty-eight': 'aṭṭhavīsañca',
 'wield': 'vasavattīnaṃ', 'Yāma gods': 'yāmānaṃ devānaṃ'})
JH = {'absorption': 'jhānaṃ', 'meditative': 'jhānaṃ', 'meditative absorption': 'jhānaṃ',
      'Meditative absorption': 'jhānaṃ', 'degree': NDE, 'developed': 'bhāvetvā', 'gods': 'devānaṃ', 'having': NDE,
      'limited': 'parittaṃ', 'limited degree': 'parittaṃ', 'middling': 'majjhimaṃ', 'middling degree': 'majjhimaṃ',
      'refined': 'paṇītaṃ', 'refined degree': 'paṇītaṃ', 'reborn': 'upapajjanti'}
M['2-1024'] = dict(LIFE, **JH)
M['2-1024'].update({'Brahmā gods': 'brahmānaṃ devānaṃ', 'eon': 'Kappassa', 'Great Brahmā': 'mahābrahmānaṃ',
                    'Great Brahmā gods': 'mahābrahmānaṃ devānaṃ', 'ministers': 'purohitānaṃ',
                    'retinue': 'pārisajjānaṃ'})
M['2-1025'] = dict(LIFE, **JH)
M['2-1025'].update({'eons': 'kappā', 'measureless': 'appamāṇābhānaṃ', 'radiance': 'ābhānaṃ',
                    'streaming': 'ābhassarānaṃ'})
M['2-1026'] = dict(LIFE, **JH)
M['2-1026'].update({'beauty': 'subhānaṃ', 'complete': 'kiṇhānaṃ', 'eons': 'kappā', 'measureless': 'appamāṇa',
                    'sixteen': 'Soḷasa', 'sixty-four': 'Catusaṭṭhi', 'thirty-two': 'Bāttiṃsa'})
M['2-1027'] = dict(LIFE, **JH)
M['2-1027'].update({
 'Akaniṭṭha gods': 'akaniṭṭhānaṃ devānaṃ', 'aspiration': 'paṇidhi', 'atappa': 'atappānaṃ',
 'Atappa gods': 'atappānaṃ devānaṃ', 'attention': 'manasikāra', 'aviha': 'avihānaṃ', 'Aviha gods': 'avihānaṃ devānaṃ',
 'consciousness': 'viññāṇañcāyatanūpagānaṃ', 'desire': 'chanda', 'difference': 'nānattatā',
 'eons': 'kappasahassāni', 'field': 'āyatanūpagānaṃ', 'field of infinite': 'ākāsānañcāyatanūpagānaṃ',
 'field of nothingness': 'ākiñcaññāyatanūpagānaṃ', 'fourth meditative': 'Catutthaṃ jhānaṃ',
 'fourth meditative absorption': 'Catutthaṃ jhānaṃ', 'hundred': 'satāni', 'infinite': 'ākāsānañcāyatanūpagānaṃ',
 'infinite consciousness': 'viññāṇañcāyatanūpagānaṃ', 'infinite space': 'ākāsānañcāyatanūpagānaṃ',
 'neither-perception-nor-non-perception': 'nevasaññānāsaññāyatanūpagānaṃ', 'non-percipient': 'asaññasattānaṃ',
 'non-percipient gods': 'asaññasattānaṃ devānaṃ', 'nothingness': 'ākiñcaññāyatanūpagānaṃ', 'object': 'ārammaṇa',
 'reached the field': 'āyatanūpagānaṃ', 'resolve': 'abhinīhāra', 'sixteen': 'Soḷasa',
 'space': 'ākāsānañcāyatanūpagānaṃ', 'sudassa': 'sudassānaṃ', 'Sudassa gods': 'sudassānaṃ devānaṃ',
 'Sudassī gods': 'sudassīnaṃ devānaṃ', 'thousand': 'sahassaṃ', 'thousand eons': 'Kappasahassaṃ',
 'vehapphala': 'vehapphalānaṃ', 'Vehapphala gods': 'vehapphalānaṃ devānaṃ', 'wisdom': 'paññā'})
M['2-1028'] = dict(LIFE, **{
 'consciousness': 'Viññāṇañcāyatanūpagānaṃ', 'eighty-four': 'Caturāsīti', 'eons': 'kappasahassāni', 'forty': 'Cattārīsa',
 'field': 'āyatanūpagānaṃ', 'field of infinite': 'Ākāsānañcāyatanūpagānaṃ',
 'field of nothingness': 'Ākiñcaññāyatanūpagānaṃ', 'gods': 'devānaṃ', 'infinite': 'Ākāsānañcāyatanūpagānaṃ',
 'infinite consciousness': 'Viññāṇañcāyatanūpagānaṃ', 'infinite space': 'Ākāsānañcāyatanūpagānaṃ',
 'neither-perception-nor-non-perception': 'Nevasaññānāsaññāyatanūpagānaṃ',
 'nothingness': 'Ākiñcaññāyatanūpagānaṃ', 'reached the field': 'āyatanūpagānaṃ', 'sixty': 'Saṭṭhi',
 'space': 'Ākāsānañcāyatanūpagānaṃ', 'thousand': 'sahassāni', 'thousand eons': 'kappasahassāni', 'twenty': 'Vīsati'})
M['2-1029'] = {
 'again': 'punāgacchanti', 'aging': 'Jarā', 'aging and death': 'Jarāmaraṇa', 'attain': 'parinibbanti',
 'away': 'cavanti', 'bad': 'duggatiṃ', 'bad destination': 'duggatiṃ', 'beings': 'sattā', 'careful': 'nipakā',
 'death': 'maraṇa', 'destination': 'gatiṃ', 'develop': 'bhāventi', 'developed': 'Bhāvayitvā',
 'exhausted': 'saṅkhayā', 'existence': 'bhavo', 'form': 'rūpa', 'fully': 'pariññāya', 'fully understood': 'pariññāya',
 'gone': 'gatā', 'having': NDE, 'highest': 'uttamaṃ', 'life': 'dīghāyukā', 'lifted': 'Ukkhittā', 'material': 'rūpa',
 'material form': 'rūpa', 'mental': 'āsave', 'mental taints': 'āsave', 'merit': 'puñña', 'ones': NDE,
 'pass': 'cavanti', 'path': 'maggaṃ', 'peak': 'Bhavaggatampi', 'permanent': 'nicco', 'pleasure': 'kāma',
 'plunges': 'nibbānogadhagāminaṃ', 'power': 'tejena', 'pure': 'suciṃ', 'release': 'mokkhāya', 'sage': 'mahesinā',
 'sense': 'kāma', 'sense pleasure': 'kāma', 'span': 'āyusaṅkhayā', 'subtle': 'nipuṇā', 'taints': 'anāsavāti',
 'therefore': 'Tasmā', 'thinkers': 'cintakā', 'understood': 'pariññāya', 'whatever': 'koci', 'wise': 'dhīrā'}
M['2-18-7-0'] = {'directly': 'Abhiññeyyādivāro', 'known': 'Abhiññeyyādivāro', 'rest': 'ādi', 'section': 'vāro'}
M['2-1030'] = {'abandoned': 'pahātabbā', 'aggregates': 'khandhānaṃ', 'developed': 'bhāvetabbā',
               'directly': 'abhiññeyyā', 'fully': 'pariññeyyā', 'fully understood': 'pariññeyyā',
               'known': 'abhiññeyyā', 'minds': 'cittānaṃ', 'realised': 'sacchikātabbā', 'understood': 'pariññeyyā'}
CAPS = {'mind-consciousness': 'Manoviññāṇa', 'mind-consciousness element': 'Manoviññāṇadhātu',
        'mind-consciousness-element': 'Manoviññāṇadhātu', 'suffering': 'Dukkha', 'truth of suffering': 'Dukkhasaccaṃ'}
M['2-1031'] = dict(ANAL, **CAPS)
M['2-1031'].update({
 'abandoned': 'pahātabbo', 'developed': 'bhāvetabbo', 'directly': 'abhiññeyyo', 'fully': 'pariññeyyo',
 'fully understood': 'pariññeyyo', 'known': 'abhiññeyyo', 'realised': 'sacchikātabbo', 'understood': 'pariññeyyo',
 'faculty': 'indriyaṃ', 'faculty of final': 'Aññindriyaṃ', 'grief': 'Domanassindriyaṃ',
 'know': 'Anaññātaññassāmītindriyaṃ', 'knowledge': 'Aññindriyaṃ'})
M['2-18-8-0'] = {'having': 'Sārammaṇānārammaṇavāro', 'objects': 'ārammaṇa', 'section': 'vāro'}
M['2-1032'] = {'aggregates': 'khandhānaṃ', 'minds': 'cittānaṃ', 'objects': 'sārammaṇā'}
M['2-1033'] = dict(ANAL, **{'Ten elements': 'Dasa dhātuyo', 'object': 'ārammaṇo', 'objects': 'sārammaṇā',
                            'suffering': 'Dukkha', 'truth of suffering': 'Dukkhasaccaṃ'})
M['2-1034'] = {'aggregates': 'khandhānaṃ', 'minds': 'cittānaṃ', 'objects': 'ārammaṇā',
               'things-with-objects': 'sārammaṇārammaṇā', 'things-without-objects': 'anārammaṇārammaṇā'}
M['2-1035'] = dict(ANAL, **CAPS)
M['2-1035'].update({'object': 'ārammaṇo', 'objects': 'ārammaṇā', 'things-with-objects': 'sārammaṇārammaṇā',
                    'things-without-objects': 'anārammaṇārammaṇā'})
M['2-18-9-0'] = {'heard': 'Diṭṭhasutādidassanavāro', 'rest': 'ādi', 'section': 'vāro', 'Section Showing': 'dassanavāro',
                 'showing': 'dassana'}
M['2-1036'] = {'aggregates': 'khandhānaṃ', 'heard': 'sutā', 'known': 'viññātā', 'minds': 'cittānaṃ', 'sensed': 'mutā'}
M['2-1037'] = dict(ANAL, **CAPS)
M['2-1037'].update({
 'heard': 'suto', 'known': 'viññāto', 'sensed': 'muto', 'sense-fields': 'āyatanā', 'sight': 'Rūpāyatanaṃ',
 'sight element': 'Rūpadhātu', 'sight sense-field': 'Rūpāyatanaṃ', 'smell': 'Gandhāyatanaṃ',
 'smell element': 'Gandhadhātu', 'smell sense-field': 'Gandhāyatanaṃ', 'sound': 'Saddāyatanaṃ',
 'sound element': 'Saddadhātu', 'tangible': 'phoṭṭhabbāyatanaṃ', 'tangible element': 'phoṭṭhabbadhātu',
 'tangible sense-field': 'phoṭṭhabbāyatanaṃ', 'taste': 'rasāyatanaṃ', 'taste element': 'rasadhātu',
 'taste sense-field': 'rasāyatanaṃ', 'thirteen': 'Terasa', 'truths': 'saccāni', 'twenty-two': 'Bāvīsatindriyā',
 'twenty-two faculties': 'Bāvīsatindriyā'})
M['2-18-10-0'] = {'rest': 'ādi', 'section': 'vāro', 'Section Showing': 'dassanavāro', 'showing': 'dassana',
                  'triads': 'Tikādidassanavāro'}
M['2-18-10-1-0'] = {'triad': 'tikaṃ', 'wholesome': 'Kusala'}
M['2-1038'] = dict(ANAL, **CAPS)
M['2-1038'].update({'grief': 'Domanassindriyaṃ', 'know': 'Anaññātaññassāmītindriyaṃ',
                    'known': 'Anaññātaññassāmītindriyaṃ', 'neutral': 'abyākato', 'wholesome': 'kusalā',
                    'unwholesome': 'akusalā'})
M['2-18-10-2-0'] = {'feeling': 'Vedanā', 'triad': 'tikaṃ'}
M['2-1039'] = dict(ANAL, **CAPS)
M['2-1039'].update({
 'aggregates': 'khandhānaṃ', 'associated': 'sampayuttā', 'body-consciousness': 'kāyaviññāṇa',
 'body-consciousness element': 'kāyaviññāṇadhātu', 'body-consciousness-element': 'Kāyaviññāṇadhātu',
 'delusion': 'Moho', 'describable': 'vattabbā', 'feeling': 'vedanāya', 'hate': 'Doso', 'minds': 'cittānaṃ',
 'neither-painful-nor-pleasant': 'adukkhamasukhāya', 'painful': 'dukkhāya', 'painful feeling': 'dukkhāya vedanāya',
 'pleasant': 'sukhāya', 'pleasant feeling': 'sukhāya vedanāya', 'root': 'hetu', 'twelve': 'Dvādasindriyā',
 'Twelve faculties': 'Dvādasindriyā', 'unwholesome root': 'akusalahetu'})
M['2-18-10-3-0'] = {'Result Triad': 'Vipākattikaṃ', 'triad': 'tikaṃ'}
MANO = {'mind': 'Mano', 'mind element': 'Manodhātu', 'mind-element': 'Manodhātu',
        'mind-element contact': 'Manodhātusamphasso'}
M['2-1040'] = dict(ANAL, **CAPS)
M['2-1040'].update(MANO)
M['2-1040'].update({
 'aggregates': 'khandhānaṃ', 'faculty of final': 'Aññindriyaṃ', 'knowledge': 'Aññindriyaṃ', 'minds': 'cittānaṃ',
 'results nor things': 'nevavipākanavipākadhammadhammā', 'subject to result': 'vipākadhammadhammā',
 'thing': 'nevavipākanavipākadhammadhammo', 'thing subject': 'nevavipākanavipākadhammadhammo',
 'things': 'vipākadhammadhammā', 'things subject': 'vipākadhammadhammā'})
M['2-18-10-4-0'] = {'taken-up': 'Upādinna', 'triad': 'tikaṃ'}
M['2-1041'] = dict(ANAL, **CAPS)
M['2-1041'].update(MANO)
M['2-1041'].update({
 'able': 'upādāniyā', 'aggregates': 'khandhānaṃ', 'birth': NDE, 'clung': 'upādāniyā', 'grief': 'Domanassindriyaṃ',
 'minds': 'cittānaṃ', 'sense-field': 'āyatanaṃ', 'sound': 'Saddāyatanaṃ', 'sound element': 'Saddadhātu',
 'ten': 'Dasa'})
M['2-18-10-5-0'] = {'thought': 'Vitakka', 'triad': 'tikaṃ'}
M['2-1042'] = dict(ANAL, **CAPS)
M['2-1042'].update(MANO)
M['2-1042'].update({
 'aggregate of mental': 'Saṅkhārakkhandho', 'Aggregate of Mental': 'Saṅkhārakkhandho', 'aggregates': 'khandhānaṃ',
 'describable': 'vattabbo', 'eleven': 'Ekādasindriyā', 'Eleven faculties': 'Ekādasindriyā',
 'equanimity': 'Upekkhindriyaṃ', 'equanimity faculty': 'Upekkhindriyaṃ', 'examination': 'vicārā',
 'fifteen': 'Pannarasa', 'Fifteen elements': 'Pannarasa dhātuyo', 'formations': 'Saṅkhāra',
 'grief': 'Domanassindriyaṃ', 'mental': 'Saṅkhāra', 'Mental Formations': 'Saṅkhāra', 'mental formations': 'Saṅkhāra',
 'mind': 'Manāyatanaṃ', 'minds': 'cittānaṃ', 'thought': 'vitakka'})
M['2-18-10-6-0'] = {'material-form': 'Rūpa', 'pair': 'dukaṃ'}
M['2-1043'] = dict(ANAL, **CAPS)
M['2-1043'].update({'aggregates': 'khandhānaṃ', 'immaterial': 'arūpā', 'material': 'rūpā', 'minds': 'cittānaṃ',
                    'truths': 'saccāni'})
M['2-18-10-7-0'] = {'pair': 'dukaṃ', 'worldly': 'Lokiya'}
M['2-1044'] = dict(ANAL, **CAPS)
M['2-1044'].update({
 'aggregates': 'khandhānaṃ', 'analysis': 'vibhaṅgo', 'beyond': 'lokuttarā', 'book': 'pakaraṇaṃ',
 'Book of Analysis': 'Vibhaṅgapakaraṇaṃ', 'born': 'Manoviññāṇadhātusamphassajā', 'direct': 'Abhiññā',
 'direct knowledges': 'Abhiññā', 'eighteen': 'Aṭṭhārasannaṃ', 'eighteen elements': 'Aṭṭhārasannaṃ dhātūnaṃ',
 'elements': 'dhātūnaṃ', 'feeling': 'vedanā', 'Feeling born': 'Manoviññāṇadhātusamphassajā vedanā',
 'feeling born': 'Manoviññāṇadhātusamphassajā vedanā', 'finished': 'niṭṭhito', 'heart': 'hadaya',
 'intention': 'cetanā', 'intention born': 'Manoviññāṇadhātusamphassajā cetanā',
 'Intention born': 'Manoviññāṇadhātusamphassajā cetanā', 'knowledges': 'Abhiññā', 'minds': 'cittānaṃ',
 'objects': 'sārammaṇā', 'perception': 'saññā', 'perception born': 'Manoviññāṇadhātusamphassajā saññā',
 'Perception born': 'Manoviññāṇadhātusamphassajā saññā', 'sense-fields': 'āyatanānaṃ', 'taken-up': 'upādinnā',
 'teaching': 'Dhamma', 'thought': 'vitakkaṃ', 'truths': 'saccānaṃ', 'twelve': 'Dvādasannaṃ',
 'twelve sense-fields': 'Dvādasannaṃ āyatanānaṃ', 'wholesome': 'kusala', 'worldly': 'lokiyā'})

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
print('written', len(out), 'missing', missing)
