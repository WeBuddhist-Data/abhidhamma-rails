import pathlib
d = pathlib.Path(__file__).parent
ch = '1-khandhavibhango'
NDE = '(no direct equivalent)'
M = {}

import re
_root = pathlib.Path(__file__).resolve().parents[5]
PALI = {}
_buf = []
for _l in (_root / 'AI_translation' / 'pali' / 'pi-2_split_chapters' / f'{ch}.md').read_text(encoding='utf-8').splitlines():
    _buf.append(_l)
    _m = re.search(r'\^([\w-]+)\s*$', _l)
    if _m:
        PALI[_m.group(1)] = '\n'.join(_buf); _buf = []


def auto(sid, bases, over=None):
    """Union of the base dicts; for each key take the first candidate value present in this segment's Pali
    (NDE always counts as present). Keys with no present candidate are left out, so they show as missing."""
    text = PALI[sid]
    out = {}
    keys = []
    for b in bases:
        keys += [k for k in b if k not in keys]
    for k in keys:
        for b in bases:
            v = b.get(k)
            if v is None:
                continue
            if v == NDE or all(p in text for p in v.split(' / ')):
                out[k] = v
                break
    out.update(over or {})
    return out

M['2-1-0'] = {'aggregates': 'Khandha', 'analysis': 'vibhaṅgo'}
M['2-1-1-0'] = {'classification': 'bhājanīyaṃ', 'discourses': 'Suttanta'}
M['2-1'] = {
 'aggregate': 'khandho', 'aggregate of consciousness': 'viññāṇakkhandho',
 'Aggregate of Consciousness': 'viññāṇakkhandho', 'aggregate of feeling': 'vedanākkhandho',
 'aggregate of material': 'rūpakkhandho', 'aggregate of mental': 'saṅkhārakkhandho',
 'Aggregate of Mental': 'saṅkhārakkhandho', 'Aggregate of Perception': 'saññākkhandho',
 'aggregate of perception': 'saññākkhandho', 'aggregates': 'khandhā', 'consciousness': 'viññāṇa',
 'feeling': 'vedanā', 'form': 'rūpa', 'formations': 'saṅkhāra', 'material': 'rūpa', 'material form': 'rūpa',
 'mental': 'saṅkhāra', 'Mental Formations': 'saṅkhāra', 'mental formations': 'saṅkhāra', 'perception': 'saññā',
}
M['2-1-1-1-0'] = {'aggregate': 'khandho', 'aggregate of material': 'Rūpakkhandho', 'form': 'Rūpa',
                  'material': 'Rūpa', 'material form': 'Rūpa'}
M['2-2'] = {
 'aggregate': 'khandho', 'aggregate of material': 'rūpakkhandho', 'called the aggregate': 'vuccati rūpakkhandho',
 'coarse': 'oḷārikaṃ', 'form': 'rūpaṃ', 'gathered': 'abhisaññūhitvā', 'grouped': 'abhisaṅkhipitvā',
 'inferior': 'hīnaṃ', 'material': 'rūpaṃ', 'material form': 'rūpaṃ', 'subtle': 'sukhumaṃ', 'superior': 'paṇītaṃ',
 'therein': 'Tattha', 'together': 'tadekajjhaṃ', 'whatever': 'Yaṃ kiñci',
}
M['2-3'] = {
 'appeared': 'pātubhūtaṃ', 'arisen': 'uppannaṃ', 'arose': 'uppajjitvā', 'belonging': 'atītaṃsena', 'born': 'jātaṃ',
 'brought': 'abhinibbattaṃ', 'called future': 'vuccati / anāgataṃ', 'called past': 'vuccati / atītaṃ',
 'called present': 'vuccati / paccuppannaṃ', 'ceased': 'niruddhaṃ', 'changed': 'vipariṇataṃ',
 'completely': 'abbhatthaṅgataṃ', 'counted': 'saṅgahitaṃ', 'counted as belonging': 'atītaṃsena saṅgahitaṃ',
 'derived': 'upādāya', 'disappeared': 'vigataṃ', 'elements': 'bhūtā', 'emerged': 'uṭṭhitaṃ', 'form': 'rūpaṃ',
 'form derived': 'upādāyarūpaṃ', 'forth': 'abhinibbattaṃ', 'future material form': 'rūpaṃ anāgataṃ',
 'gone': 'vigataṃ', 'great elements': 'mahābhūtā', 'material': 'rūpaṃ', 'material form': 'rūpaṃ',
 'material form derived': 'upādāyarūpaṃ', 'past material': 'rūpaṃ atītaṃ', 'past material form': 'rūpaṃ atītaṃ',
 'present material form': 'rūpaṃ paccuppannaṃ', 'produced': 'nibbattaṃ', 'therein': 'Tattha', 'view': 'samuṭṭhitaṃ',
}
M['2-4'] = {
 'birth': NDE, 'derived': 'upādāya', 'elements': 'bhūtā', 'form': 'rūpaṃ', 'form derived': 'upādāyarūpaṃ',
 'great elements': 'mahābhūtā', 'individual': 'pāṭipuggalikaṃ', 'internal': 'ajjhattaṃ', 'material': 'rūpaṃ',
 'material form': 'rūpaṃ', 'material form derived': 'upādāyarūpaṃ', 'person': 'parapuggalānaṃ',
 'personal': 'paccattaṃ', 'therein': 'Tattha',
}
M['2-5'] = {
 'coarse': 'oḷārikaṃ', 'coarse material': 'rūpaṃ oḷārikaṃ', 'coarse material form': 'rūpaṃ oḷārikaṃ',
 'eye': 'Cakkhāyatanaṃ', 'eye faculty': 'Cakkhāyatanaṃ', 'faculty': 'indriyaṃ', 'faculty of femininity': 'Itthindriyaṃ',
 'femininity': 'Itthindriyaṃ', 'food': 'āhāro', 'form': 'rūpaṃ', 'material': 'rūpaṃ', 'material form': 'rūpaṃ',
 'physical': 'kabaḷīkāro', 'sense-field': 'āyatanaṃ', 'subtle': 'sukhumaṃ', 'subtle material': 'rūpaṃ sukhumaṃ',
 'subtle material form': 'rūpaṃ sukhumaṃ', 'therein': 'Tattha', 'touch': 'phoṭṭhabbāyatanaṃ',
}
M['2-6'] = {
 'agreeable': 'manāpaṃ', 'attractive': 'kantaṃ', 'considered': 'hīnaṃ', 'contempt': 'paribhūtaṃ',
 'despised': 'avaññātaṃ', 'disagreeable': 'amanāpaṃ', 'disregarded': 'acittīkataṃ', 'excellent': 'paṇītaṃ',
 'form': 'rūpaṃ', 'highly': 'cittīkataṃ', 'inferior': 'hīnaṃ', 'inferior material': 'rūpaṃ hīnaṃ',
 'inferior material form': 'rūpaṃ hīnaṃ', 'looked': 'uññātaṃ', 'material': 'rūpaṃ', 'material form': 'rūpaṃ',
 'regarded': 'cittīkataṃ', 'relative': 'upādāyupādāya', 'scorned': 'hīḷitaṃ', 'sights': 'rūpā', 'smells': 'gandhā',
 'sounds': 'saddā', 'superior': 'paṇītaṃ', 'superior material': 'rūpaṃ paṇītaṃ',
 'superior material form': 'rūpaṃ paṇītaṃ', 'tastes': 'rasā', 'therein': 'Tattha', 'things': 'phoṭṭhabbā',
 'things touched': 'phoṭṭhabbā', 'thought': 'hīnamataṃ', 'touched': 'phoṭṭhabbā', 'treated': 'paribhūtaṃ',
 'unattractive': 'akantaṃ', 'understood': 'daṭṭhabbaṃ', 'unwanted': 'aniṭṭhaṃ', 'wanted': 'iṭṭhaṃ',
}
M['2-7'] = {
 'called material': 'vuccati rūpaṃ', 'called material form': 'vuccati rūpaṃ', 'eye': 'Cakkhāyatanaṃ',
 'eye sense-field': 'Cakkhāyatanaṃ', 'faculty': 'indriyaṃ', 'faculty of femininity': 'Itthindriyaṃ',
 'femininity': 'Itthindriyaṃ', 'food': 'āhāro', 'form': 'rūpaṃ', 'material': 'rūpaṃ', 'material form': 'rūpaṃ',
 'nearby': 'upakaṭṭhe', 'physical': 'kabaḷīkāro', 'relative': 'upādāyupādāya', 'sense-field': 'āyatanaṃ',
 'therein': 'Tattha', 'touch': 'phoṭṭhabbāyatanaṃ', 'understood': 'daṭṭhabbaṃ', 'whatever': 'yaṃ vā panaññampi',
}
M['2-8'] = {
 'aggregate': 'khandho', 'aggregate of feeling': 'vedanākkhandho', 'called the aggregate': 'vuccati vedanākkhandho',
 'coarse': 'oḷārikā', 'feeling': 'vedanā', 'gathered': 'abhisaññūhitvā', 'grouped': 'abhisaṅkhipitvā',
 'inferior': 'hīnā', 'subtle': 'sukhumā', 'superior': 'paṇītā', 'therein': 'Tattha', 'together': 'tadekajjhaṃ',
 'whatever': 'Yā kāci',
}
M['2-9'] = {
 'appeared': 'pātubhūtā', 'arisen': 'uppannā', 'arose': 'uppajjitvā', 'belonging': 'atītaṃsena', 'born': 'jātā',
 'brought': 'abhinibbattā', 'called future': 'vuccati / anāgatā', 'called past': 'vuccati / atītā',
 'called past feeling': 'vuccati vedanā atītā', 'called present': 'vuccati / paccuppannā', 'ceased': 'niruddhā',
 'changed': 'vipariṇatā', 'completely': 'abbhatthaṅgatā', 'counted': 'saṅgahitā',
 'counted as belonging': 'atītaṃsena saṅgahitā', 'disappeared': 'vigatā', 'emerged': 'uṭṭhitā', 'feeling': 'vedanā',
 'forth': 'abhinibbattā', 'future feeling': 'vedanā anāgatā', 'gone': 'vigatā', 'painful': 'dukkhā',
 'painful feeling': 'dukkhā vedanā', 'painful nor pleasant': 'adukkhamasukhā', 'past feeling': 'vedanā atītā',
 'pleasant': 'sukhā', 'pleasant feeling': 'sukhā vedanā', 'present feeling': 'vedanā paccuppannā',
 'produced': 'nibbattā', 'therein': 'Tattha', 'view': 'samuṭṭhitā',
}
M['2-10'] = {
 'birth': NDE, 'feeling': 'vedanā', 'individual': 'pāṭipuggalikā', 'internal': 'ajjhattaṃ', 'painful': 'dukkhā',
 'painful feeling': 'dukkhā vedanā', 'painful nor pleasant': 'adukkhamasukhā', 'person': 'parapuggalānaṃ',
 'personal': 'paccattaṃ', 'pleasant': 'sukhā', 'pleasant feeling': 'sukhā vedanā', 'therein': 'Tattha',
}
# shared by the feeling coarse/subtle, inferior/superior, far/near segments 2-11..2-13
FEEL3 = {
 'absorption': 'samāpannassa', 'connected': 'Sāsavā', 'defilements': 'āsavā', 'feeling': 'vedanā',
 'feeling and feeling': 'vedanā', 'Feeling connected': 'Sāsavā vedanā', 'feeling free': 'anāsavā vedanā',
 'free': 'anāsavā', 'meditative': 'samāpannassa', 'meditative absorption': 'samāpannassa',
 'Meditative absorption': 'samāpannassa', 'neutral': 'abyākatā', 'neutral feeling': 'abyākatā vedanā',
 'painful': 'Dukkhā', 'painful feeling': 'Dukkhā vedanā', 'painful nor pleasant': 'adukkhamasukhā',
 'pleasant': 'sukhā', 'Pleasant and painful': 'Sukhadukkhā', 'pleasant and painful': 'Sukhadukkhā',
 'pleasant feeling': 'sukhā / vedanā', 'relative': 'upādāyupādāya', 'someone': NDE, 'therein': 'Tattha',
 'understood': 'daṭṭhabbā', 'unwholesome': 'Akusalā', 'Unwholesome feeling': 'Akusalā vedanā',
 'unwholesome feeling': 'Akusalā vedanā', 'wholesome': 'kusalābyākatā', 'wholesome and neutral': 'kusalābyākatā',
 'wholesome and unwholesome': 'Kusalākusalā', 'Wholesome and unwholesome': 'Kusalākusalā',
}
M['2-11'] = dict(FEEL3, **{'coarse': 'oḷārikā', 'feeling is coarse': 'vedanā oḷārikā', 'mental': 'Sāsavā',
                           'subtle': 'sukhumā'})
M['2-12'] = dict(FEEL3, **{'feeling is inferior': 'vedanā hīnā', 'inferior': 'hīnā', 'inferior feeling': 'vedanā hīnā',
                           'superior': 'paṇītā', 'superior feeling': 'vedanā paṇītā'})
M['2-13'] = dict(FEEL3, **{
 'called feeling': 'vuccati vedanā', 'feelings': 'vedanāhi', 'neutral feelings': 'ābyākatāhi vedanāhi',
 'painful feelings': 'dukkhāhi vedanāhi', 'Pleasant and painful': 'sukhadukkhā', 'pleasant and painful': 'sukhadukkhā',
 'pleasant feeling': 'sukhā vedanā', 'wholesome': 'kusalā', 'wholesome and unwholesome': 'kusalākusalā',
 'Wholesome and unwholesome': 'kusalākusalā', 'wholesome feeling': 'kusalā vedanā'})
M['2-1-1-3-0'] = {'aggregate': 'khandho', 'aggregate of perception': 'Saññākkhandho',
                  'Aggregate of Perception': 'Saññākkhandho', 'perception': 'Saññā'}
M['2-14'] = {
 'aggregate': 'khandho', 'Aggregate of Perception': 'saññākkhandho', 'aggregate of perception': 'saññākkhandho',
 'called the aggregate': 'vuccati saññākkhandho', 'coarse': 'oḷārikā', 'gathered': 'abhisaññūhitvā',
 'grouped': 'abhisaṅkhipitvā', 'inferior': 'hīnā', 'perception': 'saññā', 'subtle': 'sukhumā', 'superior': 'paṇītā',
 'therein': 'Tattha', 'together': 'tadekajjhaṃ', 'whatever': 'Yā kāci',
}
CONTACT6 = {
 'body-contact': 'kāyasamphassa', 'born': 'cakkhusamphassajā', 'born of body-contact': 'kāyasamphassajā',
 'born of ear-contact': 'sotasamphassajā', 'born of eye-contact': 'cakkhusamphassajā',
 'born of mind-contact': 'manosamphassajā', 'born of nose-contact': 'ghānasamphassajā',
 'born of tongue-contact': 'jivhāsamphassajā', 'ear-contact': 'sotasamphassa', 'eye-contact': 'cakkhusamphassa',
 'mind-contact': 'manosamphassa', 'nose-contact': 'ghānasamphassa', 'tongue-contact': 'jivhāsamphassa',
}
TIME_F = {  # feminine past/future/present formula
 'appeared': 'pātubhūtā', 'arisen': 'uppannā', 'arose': 'uppajjitvā', 'belonging': 'atītaṃsena', 'born': 'jātā',
 'brought': 'abhinibbattā', 'called future': 'vuccati / anāgatā', 'called past': 'vuccati / atītā',
 'called present': 'vuccati / paccuppannā', 'ceased': 'niruddhā', 'changed': 'vipariṇatā',
 'completely': 'abbhatthaṅgatā', 'counted': 'saṅgahitā', 'counted as belonging': 'atītaṃsena saṅgahitā',
 'disappeared': 'vigatā', 'emerged': 'uṭṭhitā', 'forth': 'abhinibbattā', 'gone': 'vigatā', 'produced': 'nibbattā',
 'therein': 'Tattha', 'view': 'samuṭṭhitā',
}
M['2-15'] = dict(TIME_F, **CONTACT6)
M['2-15'].update({
 'future perception': 'saññā anāgatā', 'past perception': 'saññā atītā', 'perception': 'saññā',
 'perception born': 'cakkhusamphassajā saññā', 'Perception born': 'cakkhusamphassajā saññā',
 'present perception': 'saññā paccuppannā'})
M['2-16'] = dict(CONTACT6, **{
 'birth': NDE, 'individual': 'pāṭipuggalikā', 'internal': 'ajjhattaṃ', 'perception': 'saññā',
 'perception born': 'cakkhusamphassajā saññā', 'Perception born': 'cakkhusamphassajā saññā',
 'person': 'parapuggalānaṃ', 'personal': 'paccattaṃ', 'therein': 'Tattha'})
# shared by the perception coarse/subtle, inferior/superior, far/near segments 2-17..2-19
PERC3 = {
 'absorption': 'samāpannassa', 'connected': 'Sāsavā', 'defilements': 'āsavā', 'feeling': 'vedanāya',
 'feelings': 'vedanāhi', 'free': 'anāsavā', 'joined': 'sampayuttā', 'joined with feeling': 'vedanāya sampayuttā',
 'joined with painful': 'Dukkhāya vedanāya sampayuttā',
 'joined with pleasant': 'sukhāya ca adukkhamasukhāya ca vedanāhi sampayuttā', 'meditative': 'samāpannassa',
 'meditative absorption': 'samāpannassa', 'Meditative absorption': 'samāpannassa', 'neutral': 'abyākatā',
 'neutral perception': 'abyākatā saññā', 'painful': 'Dukkhāya', 'painful feeling': 'Dukkhāya vedanāya',
 'painful feelings': 'dukkhāhi vedanāhi', 'painful nor pleasant': 'adukkhamasukhāya', 'perception': 'saññā',
 'Perception connected': 'Sāsavā saññā', 'perception free': 'anāsavā saññā',
 'perception joined': 'sampayuttā saññā', 'Perception joined': 'sampayuttā saññā', 'pleasant': 'sukhāya',
 'Pleasant and painful': 'Sukhadukkhāhi', 'pleasant and painful': 'Sukhadukkhāhi',
 'pleasant feeling': 'sukhāya / vedanāhi', 'relative': 'upādāyupādāya', 'someone': NDE, 'therein': 'Tattha',
 'understood': 'daṭṭhabbā', 'unwholesome': 'Akusalā', 'Unwholesome perception': 'Akusalā saññā',
 'unwholesome perception': 'Akusalā saññā', 'wholesome': 'kusalābyākatā', 'wholesome and neutral': 'kusalābyākatā',
 'wholesome and unwholesome': 'Kusalākusalā', 'Wholesome and unwholesome': 'Kusalākusalā',
}
M['2-17'] = dict(PERC3, **{
 'born': 'Paṭighasamphassajā', 'coarse': 'oḷārikā', 'feeling is coarse': 'vedanāya / oḷārikā',
 'naming': 'adhivacanasamphassa', 'perception born': 'adhivacanasamphassajā saññā',
 'Perception born': 'Paṭighasamphassajā saññā', 'sense-impact': 'Paṭighasamphassa', 'subtle': 'sukhumā'})
M['2-18'] = dict(PERC3, **{'feeling is inferior': 'vedanāya / hīnā', 'inferior': 'hīnā', 'superior': 'paṇītā'})
M['2-19'] = dict(PERC3, **{
 'called perception': 'vuccati saññā', 'joined with pleasant': 'sukhāya vedanāya sampayuttā',
 'neutral perceptions': 'ābyākatāhi saññāhi', 'Pleasant and painful': 'sukhadukkhāhi',
 'pleasant and painful': 'sukhadukkhāhi', 'pleasant feeling': 'sukhāya vedanāya', 'perceptions': 'saññāhi',
 'perceptions joined': 'sampayuttāhi saññāhi', 'unwholesome perceptions': 'akusalābyākatāhi saññāhi',
 'wholesome': 'kusalā', 'wholesome and unwholesome': 'kusalākusalā', 'Wholesome and unwholesome': 'kusalākusalā',
 'wholesome perception': 'kusalā saññā'})
SK = {'formations': 'saṅkhārā', 'mental': 'saṅkhārā', 'Mental Formations': 'saṅkhārā', 'mental formations': 'saṅkhārā'}
M['2-1-1-4-0'] = {'aggregate': 'khandho', 'Aggregate of Mental': 'Saṅkhārakkhandho',
                  'aggregate of mental': 'Saṅkhārakkhandho', 'formations': 'Saṅkhāra', 'mental': 'Saṅkhāra',
                  'Mental Formations': 'Saṅkhāra', 'mental formations': 'Saṅkhāra'}
M['2-20'] = dict(SK, **{
 'aggregate': 'khandho', 'Aggregate of Mental': 'saṅkhārakkhandho', 'aggregate of mental': 'saṅkhārakkhandho',
 'called the aggregate': 'vuccati saṅkhārakkhandho', 'coarse': 'oḷārikā', 'gathered': 'abhisaññūhitvā',
 'grouped': 'abhisaṅkhipitvā', 'inferior': 'hīnā', 'subtle': 'sukhumā', 'superior': 'paṇītā', 'therein': 'Tattha',
 'together': 'tadekajjhaṃ', 'whatever': 'Ye keci'})
INTENT = {'intention': 'cetanā', 'intention born': 'cakkhusamphassajā cetanā',
          'Intention born': 'cakkhusamphassajā cetanā'}
M['2-21'] = dict(TIME_F, **CONTACT6)
M['2-21'].update(SK)
M['2-21'].update(INTENT)
M['2-21'].update({'called future': 'vuccanti / anāgatā', 'called past': 'vuccanti / atītā',
                  'called present': 'vuccanti / paccuppannā'})
M['2-22'] = dict(CONTACT6, **SK)
M['2-22'].update(INTENT)
M['2-22'].update({'birth': NDE, 'individual': 'pāṭipuggalikā', 'internal': 'ajjhattaṃ', 'person': 'parapuggalānaṃ',
                  'personal': 'paccattaṃ', 'therein': 'Tattha'})
FORM3 = dict(SK, **{
 'absorption': 'samāpannassa', 'connected': 'Sāsavā', 'defilements': 'āsavā', 'feeling': 'vedanāya',
 'feelings': 'vedanāhi', 'Formations connected': 'Sāsavā saṅkhārā', 'formations free': 'anāsavā saṅkhārā',
 'formations joined': 'sampayuttā saṅkhārā', 'Formations joined': 'sampayuttā saṅkhārā', 'free': 'anāsavā',
 'joined': 'sampayuttā', 'joined with feeling': 'vedanāya sampayuttā',
 'joined with painful': 'Dukkhāya vedanāya sampayuttā',
 'joined with pleasant': 'sukhāya ca adukkhamasukhāya ca vedanāhi sampayuttā', 'meditative': 'samāpannassa',
 'meditative absorption': 'samāpannassa', 'Meditative absorption': 'samāpannassa', 'neutral': 'abyākatā',
 'neutral formations': 'abyākatā saṅkhārā', 'ones': NDE, 'painful': 'Dukkhāya', 'painful feeling': 'Dukkhāya vedanāya',
 'painful feelings': 'dukkhāhi vedanāhi', 'painful nor pleasant': 'adukkhamasukhāya', 'pleasant': 'sukhāya',
 'Pleasant and painful': 'Sukhadukkhāhi', 'pleasant and painful': 'Sukhadukkhāhi',
 'pleasant feeling': 'sukhāya / vedanāhi', 'relative': 'upādāyupādāya', 'someone': NDE, 'therein': 'Tattha',
 'understood': 'daṭṭhabbā', 'unwholesome': 'Akusalā', 'unwholesome formations': 'Akusalā saṅkhārā',
 'Unwholesome formations': 'Akusalā saṅkhārā', 'wholesome': 'kusalābyākatā', 'wholesome and neutral': 'kusalābyākatā',
 'wholesome and unwholesome': 'Kusalākusalā', 'Wholesome and unwholesome': 'Kusalākusalā'})
M['2-23'] = dict(FORM3, **{'coarse': 'oḷārikā', 'coarse mental formations': 'saṅkhārā oḷārikā', 'subtle': 'sukhumā'})
M['2-24'] = dict(FORM3, **{'inferior': 'hīnā', 'superior': 'paṇītā'})
M['2-25'] = dict(FORM3, **{
 'called mental formations': 'vuccanti saṅkhārā', 'joined with pleasant': 'sukhāya vedanāya sampayuttā',
 'Pleasant and painful': 'sukhadukkhāhi', 'pleasant and painful': 'sukhadukkhāhi', 'pleasant feeling': 'sukhāya vedanāya',
 'wholesome': 'kusalā', 'wholesome and unwholesome': 'kusalākusalā', 'Wholesome and unwholesome': 'kusalākusalā',
 'wholesome formations': 'kusalā saṅkhārā'})
del M['2-25']['ones']
M['2-1-1-5-0'] = {'aggregate': 'khandho', 'aggregate of consciousness': 'Viññāṇakkhandho',
                  'Aggregate of Consciousness': 'Viññāṇakkhandho', 'consciousness': 'Viññāṇa'}
M['2-26'] = {
 'aggregate': 'khandho', 'aggregate of consciousness': 'viññāṇakkhandho',
 'Aggregate of Consciousness': 'viññāṇakkhandho', 'called the aggregate': 'vuccati viññāṇakkhandho',
 'coarse': 'oḷārikaṃ', 'consciousness': 'viññāṇaṃ', 'gathered': 'abhisaññūhitvā', 'grouped': 'abhisaṅkhipitvā',
 'inferior': 'hīnaṃ', 'subtle': 'sukhumaṃ', 'superior': 'paṇītaṃ', 'therein': 'Tattha', 'together': 'tadekajjhaṃ',
 'whatever': 'Yaṃ kiñci',
}
VI6 = {'body-consciousness': 'kāyaviññāṇaṃ', 'consciousness': 'viññāṇaṃ', 'ear-consciousness': 'sotaviññāṇaṃ',
       'eye-consciousness': 'cakkhuviññāṇaṃ', 'mind-consciousness': 'manoviññāṇaṃ',
       'nose-consciousness': 'ghānaviññāṇaṃ', 'tongue-consciousness': 'jivhāviññāṇaṃ'}
TIME_N = {k: M['2-3'][k] for k in TIME_F}
M['2-27'] = dict(TIME_N, **VI6)
M['2-27'].update({'future consciousness': 'viññāṇaṃ anāgataṃ', 'past consciousness': 'viññāṇaṃ atītaṃ',
                  'present consciousness': 'viññāṇaṃ paccuppannaṃ'})
M['2-28'] = dict(VI6, **{'birth': NDE, 'individual': 'pāṭipuggalikaṃ', 'internal': 'ajjhattaṃ',
                         'person': 'parapuggalānaṃ', 'personal': 'paccattaṃ', 'therein': 'Tattha'})
CONS3 = {
 'absorption': 'samāpannassa', 'connected': 'Sāsavaṃ', 'consciousness': 'viññāṇaṃ',
 'Consciousness connected': 'Sāsavaṃ viññāṇaṃ', 'consciousness free': 'anāsavaṃ viññāṇaṃ',
 'Consciousness joined': 'sampayuttaṃ viññāṇaṃ', 'consciousness joined': 'sampayuttaṃ viññāṇaṃ',
 'defilements': 'āsavaṃ', 'feeling': 'vedanāya', 'feelings': 'vedanāhi', 'free': 'anāsavaṃ', 'joined': 'sampayuttaṃ',
 'joined with feeling': 'vedanāya sampayuttaṃ', 'joined with painful': 'Dukkhāya vedanāya sampayuttaṃ',
 'joined with pleasant': 'sukhāya ca adukkhamasukhāya ca vedanāhi sampayuttā', 'meditative': 'samāpannassa',
 'meditative absorption': 'samāpannassa', 'Meditative absorption': 'samāpannassa', 'neutral': 'abyākataṃ',
 'neutral consciousness': 'abyākataṃ viññāṇaṃ', 'painful': 'Dukkhāya', 'painful feeling': 'Dukkhāya vedanāya',
 'painful feelings': 'dukkhāhi vedanāhi', 'painful nor pleasant': 'adukkhamasukhāya', 'pleasant': 'sukhāya',
 'Pleasant and painful': 'Sukhadukkhāhi', 'pleasant and painful': 'Sukhadukkhāhi',
 'pleasant feeling': 'sukhāya / vedanāhi', 'relative': 'upādāyupādāya', 'someone': NDE, 'therein': 'Tattha',
 'understood': 'daṭṭhabbaṃ', 'unwholesome': 'Akusalaṃ', 'Unwholesome consciousness': 'Akusalaṃ viññāṇaṃ',
 'unwholesome consciousness': 'Akusalaṃ viññāṇaṃ', 'wholesome': 'kusalābyākatā',
 'wholesome and neutral': 'kusalābyākatā', 'wholesome and unwholesome': 'Kusalākusalā',
 'Wholesome and unwholesome': 'Kusalākusalā',
}
M['2-29'] = dict(CONS3, **{'coarse': 'oḷārikaṃ', 'coarse consciousness': 'viññāṇaṃ oḷārikaṃ',
                           'feeling is coarse': 'vedanāya / oḷārikaṃ', 'subtle': 'sukhumaṃ',
                           'subtle consciousness': 'viññāṇaṃ sukhumaṃ'})
M['2-30'] = dict(CONS3, **{'feeling is inferior': 'vedanāya / hīnaṃ', 'inferior': 'hīnaṃ', 'superior': 'paṇītaṃ'})
M['2-31'] = dict(CONS3, **{
 'called consciousness': 'vuccati viññāṇaṃ', 'classification': 'bhājanīyaṃ', 'discourses': 'Suttanta',
 'finished': NDE, 'joined with pleasant': 'sukhāya vedanāya sampayuttaṃ', 'Pleasant and painful': 'sukhadukkhāhi',
 'pleasant and painful': 'sukhadukkhāhi', 'pleasant feeling': 'sukhāya vedanāya', 'wholesome': 'kusalaṃ',
 'wholesome and unwholesome': 'kusalākusalā', 'Wholesome and unwholesome': 'kusalākusalā',
 'wholesome consciousness': 'kusalaṃ viññāṇaṃ'})
M['2-1-2-0'] = {'abhidhamma': 'Abhidhamma', 'classification': 'bhājanīyaṃ'}
M['2-32'] = dict(M['2-1'])
M['2-1-2-1-0'] = dict(M['2-1-1-1-0'])
M['2-33'] = {
 'abandoned': 'pahātabbaṃ', 'able': 'saṃyojaniyaṃ', 'accompanied': 'sahagataṃ',
 'accompanied by equanimity': 'upekkhāsahagataṃ', 'accompanied by happiness': 'sukhasahagataṃ',
 'accompanied by joy': 'pītisahagataṃ', 'accumulation': 'ācaya', 'aggregate': 'khandho',
 'aggregate of material': 'rūpakkhandho', 'aging': 'jarābhibhūtaṃ', 'air': 'vāyo', 'air element': 'vāyodhātu',
 'alone': 'mattaṃ', 'along': 'ānuparivatti', 'analysed': 'vibhattaṃ', 'arisen': 'uppannaṃ', 'arises': 'sahabhu',
 'away': 'oghaniyaṃ', 'belong': NDE, 'belongs': NDE, 'beyond': 'āsekkhaṃ', 'bind': 'saṃyojaniyaṃ', 'birth': NDE,
 'bodily': 'viññatti', 'body': 'kāyaviññeyyaṃ', 'body faculty': 'kāyindriyaṃ', 'body sense-field': 'kāyāyatanaṃ',
 'bring': NDE, 'called the aggregate': 'vuccati rūpakkhandho', 'cause': 'hetu', 'causes': 'hetukaṃ',
 'chapter': 'kaṇḍe', 'class': 'vidhena', 'clung': 'upādāniyaṃ', 'coarse': 'oḷārikaṃ', 'cognized': 'viññātaṃ',
 'compounded': 'saṅkhataṃ', 'consciousness': 'viññāṇehi', 'consciousness element': 'viññāṇadhātu',
 'contact': 'samphassaṃ', 'defilement': 'saṃkilesikaṃ', 'derived': 'upādā', 'dismantling': 'āpacaya',
 'dissociated': 'vippayuttaṃ', 'ear': 'sotaviññeyyaṃ', 'ear faculty': 'sotindriyaṃ', 'ear sense-field': 'sotāyatanaṃ',
 'earth': 'pathavī', 'earth element': 'pathavīdhātu', 'eightfold': 'Aṭṭhavidhena', 'eightfold class': 'Aṭṭhavidhena',
 'element': 'dhātu', 'elevenfold': 'Ekādasavidhena', 'equanimity': 'upekkhā', 'examination': 'vicāraṃ',
 'existence': NDE, 'exists': 'sappaccayaṃ', 'expression': 'viññatti', 'external': 'bāhiraṃ',
 'eye': 'cakkhuviññeyyaṃ', 'eye faculty': 'cakkhundriyaṃ', 'eye sense-field': 'cakkhāyatanaṃ', 'factor': 'cetasikaṃ',
 'faculty': 'indriyaṃ', 'faculty of femininity': 'itthindriyaṃ', 'faculty of masculinity': 'purisindriyaṃ',
 'femininity': 'itthindriyaṃ', 'fetters': 'saṃyojaniyaṃ', 'fine-material': 'rūpāvacaraṃ',
 'fine-material sphere': 'rūpāvacaraṃ', 'fire': 'tejo', 'fire element': 'tejodhātu', 'fivefold': 'Pañcavidhena',
 'fivefold class': 'Pañcavidhena', 'fixed': 'niyataṃ', 'floods': 'oghaniyaṃ', 'follows': 'ānuparivatti',
 'food': 'āhāro', 'form': 'rūpaṃ', 'form derived': 'rūpaṃ upādā', 'form knowable': 'viññeyyaṃ rūpaṃ',
 'fourfold': 'Catubbidhena', 'grasped': 'parāmaṭṭhaṃ', 'happiness': 'sukha', 'heard': 'sutaṃ',
 'hindrances': 'nīvaraṇiyaṃ', 'immaterial': 'arūpāvacaraṃ', 'immaterial sphere': 'arūpāvacaraṃ',
 'impermanent': 'aniccaṃ', 'internal': 'ajjhattikaṃ', 'invisible': 'anidassanaṃ', 'joy': 'pīti', 'kinds': NDE,
 'kinds of consciousness': 'viññāṇehi', 'knowable': 'viññeyyaṃ', 'known': 'viññeyyaṃ', 'leads': 'gāmī',
 'life': 'jīvitindriyaṃ', 'life faculty': 'jīvitindriyaṃ', 'limited': 'parittaṃ', 'masculinity': 'purisindriyaṃ',
 'material': 'rūpaṃ', 'material form': 'rūpaṃ', 'material form derived': 'rūpaṃ upādā',
 'material form knowable': 'viññeyyaṃ rūpaṃ', 'material form produced': 'rūpaṃ cittasamuṭṭhānaṃ',
 'meditative': 'bhāvanāya', 'meditative development': 'bhāvanāya', 'mental': 'āsavaṃ', 'mental factor': 'cetasikaṃ',
 'mental objects': 'dhammāyatana', 'mental taints': 'āsavaṃ', 'mind': 'citta', 'mind element': 'manodhātu',
 'mind-consciousness': 'manoviññāṇa', 'mind-consciousness element': 'manoviññāṇadhātu', 'neutral': 'abyākataṃ',
 'ninefold': 'Navavidhena', 'ninefold class': 'Navavidhena', 'nose': 'ghānaviññeyyaṃ', 'nose faculty': 'ghānindriyaṃ',
 'nose sense-field': 'ghānāyatanaṃ', 'object': 'ārammaṇaṃ', 'objects': 'dhammāyatana', 'obstruct': 'nīvaraṇiyaṃ',
 'offers': 'sappaṭighaṃ', 'offers resistance': 'sappaṭighaṃ', 'open to defilement': 'saṃkilesikaṃ', 'outcome': NDE,
 'outside': 'apariyāpannaṃ', 'overcome': 'ābhibhūtaṃ', 'painful': 'dukkha', 'physical': 'kabaḷīkāro',
 'pleasant': 'sukha', 'produced': 'samuṭṭhānaṃ', 'produces': 'vipākadhammadhammaṃ', 'resistance': 'sappaṭighaṃ',
 'root': 'hetu', 'round': NDE, 'seeing': 'dassanena', 'sense': 'kāmāvacaraṃ', 'sense sphere': 'kāmāvacaraṃ',
 'sense-field': 'āyatanaṃ', 'sense-field of mental': 'dhammāyatana', 'sense-field of sights': 'rūpāyatanaṃ',
 'sense-field of smells': 'gandhāyatanaṃ', 'sense-field of sounds': 'saddāyatanaṃ',
 'sense-field of tastes': 'rasāyatanaṃ', 'sense-field of things': 'phoṭṭhabbāyatanaṃ', 'sensed': 'mutaṃ',
 'sevenfold': 'Sattavidhena', 'sevenfold class': 'Sattavidhena', 'sights': 'rūpāyatanaṃ', 'single': 'Ekavidhena',
 'single class': 'Ekavidhena', 'sixfold': 'Chabbidhena', 'sixfold class': 'Chabbidhena', 'smells': 'gandhāyatanaṃ',
 'something': NDE, 'sounds': 'saddāyatanaṃ', 'sphere': 'āvacaraṃ', 'subtle': 'sukhumaṃ', 'sweep': 'oghaniyaṃ',
 'taints': 'āsavaṃ', 'tastes': 'rasāyatanaṃ', 'tenfold': 'Dasavidhena', 'tenfold class': 'Dasavidhena',
 'therein': 'Tattha', 'things': 'phoṭṭhabbāyatanaṃ', 'things touched': 'phoṭṭhabbāyatanaṃ', 'thought': 'vitakka',
 'thought and examination': 'savitakkasavicāraṃ', 'threefold': 'Tividhena', 'threefold class': 'Tividhena',
 'tie': 'ganthaniyaṃ', 'ties': 'ganthaniyaṃ', 'together': 'saha', 'tongue': 'jivhāviññeyyaṃ',
 'tongue faculty': 'jivhindriyaṃ', 'tongue sense-field': 'jivhāyatanaṃ', 'touched': 'phoṭṭhabbāyatanaṃ',
 'trainees': 'sekkha', 'training': 'āsekkhaṃ', 'twofold': 'Duvidhena', 'twofold class': 'Duvidhena',
 'undefiled': 'asaṃkiliṭṭha', 'verbal': 'viññatti', 'visible': 'sanidassanaṃ', 'water': 'āpo',
 'water element': 'āpodhātu', 'worldly': 'lokiyaṃ', 'wrongly': 'parāmaṭṭhaṃ', 'wrongly grasped': 'parāmaṭṭhaṃ',
 'yoke': 'yoganiyaṃ', 'yokes': 'yoganiyaṃ',
}
M['2-1-2-2-0'] = {'aggregate': 'khandho', 'aggregate of feeling': 'Vedanākkhandho', 'feeling': 'Vedanā'}
CLASSES = {
 'class': 'vidhena', 'eightfold': 'Aṭṭhavidhena', 'eightfold class': 'Aṭṭhavidhena', 'fivefold': 'Pañcavidhena',
 'fivefold class': 'Pañcavidhena', 'fourfold': 'Catubbidhena', 'ninefold': 'Navavidhena', 'ninefold class': 'Navavidhena',
 'sevenfold': 'Sattavidhena', 'sevenfold class': 'Sattavidhena', 'single': 'Ekavidhena', 'single class': 'Ekavidhena',
 'sixfold': 'Chabbidhena', 'sixfold class': 'Chabbidhena', 'tenfold': 'Dasavidhena', 'tenfold class': 'Dasavidhena',
 'threefold': 'Tividhena', 'threefold class': 'Tividhena', 'twofold': 'Duvidhena', 'twofold class': 'Duvidhena',
}
M['2-34'] = dict(CLASSES, **CONTACT6)
M['2-34'].update({
 'aggregate': 'khandho', 'aggregate of feeling': 'vedanākkhandho', 'belonging': NDE,
 'born of contact': 'samphassajā', 'cause': 'hetuko', 'consciousness element': 'viññāṇadhātu', 'contact': 'phassa',
 'element': 'dhātu', 'equanimity': 'upekkhindriyaṃ', 'faculty': 'indriyaṃ', 'faculty of equanimity': 'upekkhindriyaṃ',
 'faculty of gladness': 'somanassindriyaṃ', 'faculty of pain': 'dukkhindriyaṃ', 'faculty of pleasure': 'sukhindriyaṃ',
 'faculty of sadness': 'domanassindriyaṃ', 'feeling': 'vedanā', 'feeling belonging': NDE,
 'feeling born': 'cakkhusamphassajā vedanā', 'Feeling born': 'cakkhusamphassajā vedanā',
 'fine-material': 'rūpāvacaro', 'fine-material sphere': 'rūpāvacaro', 'gladness': 'somanassindriyaṃ',
 'immaterial': 'arūpāvacaro', 'immaterial sphere': 'arūpāvacaro', 'joined': 'sampayutto',
 'joined with contact': 'phassasampayutto', 'mind': 'mano', 'mind element': 'manodhātu',
 'mind-consciousness': 'manoviññāṇa', 'mind-consciousness element': 'manoviññāṇadhātu', 'neutral': 'abyākato',
 'neutral feeling': 'abyākato', 'pain': 'dukkhindriyaṃ', 'painful': 'dukkhā', 'pleasant': 'sukhā',
 'pleasure': 'sukhindriyaṃ', 'root': 'hetuko', 'sadness': 'domanassindriyaṃ', 'sense': 'kāmāvacaro',
 'sense sphere': 'kāmāvacaro', 'sphere': 'āvacaro', 'therein': 'Tattha', 'unwholesome': 'akusalo',
 'Unwholesome feeling': 'akusalo', 'unwholesome feeling': 'akusalo', 'wholesome': 'kusalo', 'wholesome feeling': 'kusalo'})
M['2-35'] = dict(CLASSES, **{
 'abandoned': 'pahātabbo', 'able': 'upādāniyo', 'accumulation': 'ācaya', 'aggregate': 'khandho',
 'aggregate of feeling': 'vedanākkhandho', 'arise': 'uppādī', 'arisen': 'uppanno', 'beyond': 'asekkho', 'birth': NDE,
 'bound': 'uppādī', 'cause': 'hetuko', 'causes': 'hetuko', 'classified': 'dasavidhena', 'clung': 'upādāniyo',
 'contact': 'phassa', 'defiled': 'saṃkiliṭṭha', 'defilement': 'saṃkilesiko', 'dismantling': 'apacaya',
 'dominant': 'ādhipati', 'dominant factor': 'ādhipati', 'examination': 'vicāro', 'expanded': 'mahaggato',
 'expanded feeling': 'mahaggato', 'expanded object': 'mahaggatārammaṇo', 'external': 'bahiddho',
 'external feeling': 'bahiddho', 'external object': 'bahiddhārammaṇo', 'factor': 'ādhipati', 'feeling': 'vedanā',
 'feeling both internal': 'ajjhattabahiddho', 'feeling bound': 'uppādī', 'feeling fixed': 'micchattaniyato',
 'feeling is classified': 'dasavidhena vedanākkhandho', 'feeling leading': 'ācayagāmī',
 'feeling neither defiled': 'asaṃkiliṭṭhaasaṃkilesiko', 'feeling not fixed': 'aniyato', 'feeling of trainees': 'sekkho',
 'feeling that produces': 'vipākadhammadhammo', 'feeling undefiled': 'asaṃkiliṭṭhasaṃkilesiko',
 'feeling whose root': 'pahātabbahetuko', 'feeling without thought': 'avitakkavicāramatto', 'fixed': 'niyato',
 'future feeling': 'anāgato', 'future object': 'anāgatārammaṇo', 'inferior': 'hīno', 'inferior feeling': 'hīno',
 'internal': 'ajjhatto', 'internal and external': 'ajjhattabahiddho', 'internal feeling': 'ajjhatto',
 'internal object': 'ajjhattārammaṇo', 'joined': 'sampayutto', 'joined with contact': 'phassasampayutto',
 'leading to dismantling': 'apacayagāmī', 'limited': 'paritto', 'limited feeling': 'paritto',
 'limited object': 'parittārammaṇo', 'measureless': 'appamāṇo', 'measureless feeling': 'appamāṇo',
 'measureless object': 'appamāṇārammaṇo', 'meditative': 'bhāvanāya', 'meditative development': 'bhāvanāya',
 'middling': 'majjhimo', 'middling feeling': 'majjhimo', 'object': 'ārammaṇo',
 'object both internal': 'ajjhattabahiddhārammaṇo', 'open to defilement': 'saṃkilesiko', 'past feeling': 'atīto',
 'past object': 'atītārammaṇo', 'path': 'magga', 'present feeling': 'paccuppanno',
 'present object': 'paccuppannārammaṇo', 'produces': 'vipākadhammadhammo', 'rightness': 'sammatta', 'root': 'hetuko',
 'seeing': 'dassanena', 'superior': 'paṇīto', 'superior feeling': 'paṇīto', 'ten': 'dasavidhena',
 'thought': 'vitakka', 'thought and examination': 'savitakkasavicāro', 'trainees': 'sekkho', 'training': 'asekkho',
 'undefiled': 'asaṃkiliṭṭha', 'ways': 'dasavidhena', 'wrongness': 'micchatta'})
M['2-36'] = dict(CLASSES, **{
 'abandoned': 'pahātabbo', 'able': 'saṃyojaniyo', 'accompanied': 'sahagato', 'accompanied by joy': 'pītisahagato',
 'aggregate': 'khandho', 'aggregate of feeling': 'vedanākkhandho', 'away': 'oghaniyo', 'belonging': NDE,
 'beyond': 'uttaro', 'bind': 'saṃyojaniyo', 'birth': NDE, 'bound': 'saṃyojaniyo', 'cannot': 'asaṃyojaniyo',
 'cause': 'hetu', 'causes': 'hetu', 'classified': 'dasavidhena', 'clinging': 'upādāna', 'clung': 'upādāniyo',
 'conflict': 'saraṇo', 'consciousness': NDE, 'contact': 'phassa', 'defiled': 'saṃkiliṭṭho',
 'defiled feeling': 'saṃkiliṭṭho', 'defilement': 'saṃkilesiko', 'defilements': 'kilesa', 'dissociated': 'vippayutto',
 'dissociated from clinging': 'upādānavippayutto', 'dissociated from wrong': 'parāmāsavippayutto',
 'examination': 'savicāro', 'existence': NDE, 'feeling': 'vedanā', 'feeling accompanied': 'pītisahagato',
 'feeling belonging': NDE, 'feeling dissociated': 'hetuvippayutto', 'feeling fixed': 'niyato',
 'feeling free': 'anāsavo', 'feeling included': 'pariyāpanno', 'feeling involving': 'saraṇo',
 'feeling is classified': 'dasavidhena vedanākkhandho', 'feeling joined': 'hetusampayutto',
 'feeling knowable': 'kenaci viññeyyo', 'feeling not belonging': 'na kāmāvacaro', 'feeling not fixed': 'aniyato',
 'feeling not knowable': 'kenaci na viññeyyo', 'feeling open': 'saṃkilesiko', 'feeling subject': 'sāsavo',
 'feeling whose root': 'pahātabbahetuko', 'feeling without thought': 'avitakko', 'fetters': 'saṃyojaniyo',
 'fine-material': 'rūpāvacaro', 'fine-material sphere': 'rūpāvacaro', 'fixed': 'niyato', 'floods': 'oghaniyo',
 'free': 'anāsavo', 'grasped': 'parāmaṭṭho', 'grasping': 'parāmāsa', 'hindrances': 'nīvaraṇiyo',
 'immaterial': 'arūpāvacaro', 'immaterial sphere': 'arūpāvacaro', 'involving': 'saraṇo', 'itself': NDE,
 'joined': 'sampayutto', 'joined with clinging': 'upādānasampayutto', 'joined with contact': 'phassasampayutto',
 'joined with root': 'hetusampayutto', 'joy': 'pīti', 'kinds': NDE, 'kinds of consciousness': 'kenaci',
 'knowable': 'viññeyyo', 'leads': 'niyyāniko', 'meditative': 'bhāvanāya', 'meditative development': 'bhāvanāya',
 'mental': 'āsavo', 'mental taints': 'āsavo', 'neutral': 'abyākato', 'neutral feeling': 'abyākato',
 'none': 'ahetuko', 'obstruct': 'nīvaraṇiyo', 'obstructed': 'nīvaraṇiyo', 'open to defilement': 'saṃkilesiko',
 'outcome': NDE, 'outside': 'apariyāpanno', 'root': 'hetu', 'round': NDE, 'seeing': 'dassanena',
 'sense': 'kāmāvacaro', 'sense sphere': 'kāmāvacaro', 'sphere': 'āvacaro', 'surpassed': 'sauttaro',
 'sweep': 'oghaniyo', 'swept': 'oghaniyo', 'taints': 'āsava', 'ten': 'dasavidhena', 'thought': 'vitakko',
 'tie': 'ganthaniyo', 'tied': 'ganthaniyo', 'ties': 'gantha', 'unable': 'asaṃyojaniyo', 'undefiled': 'asaṃkiliṭṭho',
 'undefiled feeling': 'asaṃkiliṭṭho', 'unwholesome': 'akusalo', 'Unwholesome feeling': 'akusalo',
 'unwholesome feeling': 'akusalo', 'ways': 'dasavidhena', 'wholesome': 'kusalo', 'wholesome feeling': 'kusalo',
 'worldly': 'lokiyo', 'worldly feeling': 'lokiyo', 'wrong': 'parāmāsa', 'wrong grasping': 'parāmāsa',
 'wrongly': 'parāmaṭṭho', 'wrongly grasped': 'parāmaṭṭho', 'yoked': 'yoganiyo', 'yokes': 'yoganiyo'})
FEEL_T, FEEL_D = M['2-35'], M['2-36']
M['2-37'] = dict(FEEL_D, **FEEL_T)
M['2-37'].update({'feeling free': 'araṇo', 'free': 'araṇo', 'pairs': 'Duka', 'rooted': 'mūlakaṃ'})
M['2-38'] = dict(FEEL_D, **FEEL_T)
M['2-39'] = dict(FEEL_T, **FEEL_D)
M['2-40'] = dict(FEEL_T, **FEEL_D)
M['2-40'].update({'feeling dissociated': 'āsavavippayutto', 'feeling joined': 'āsavasampayutto'})
M['2-41'] = dict(FEEL_T)
M['2-42'] = dict(FEEL_T, **FEEL_D)
M['2-42'].update({'rooted': 'mūlakaṃ', 'triads': 'Tika'})
for _s in ('2-37', '2-42'):
    M[_s].update({'external': 'bahiddhārammaṇo', 'internal': 'ajjhattārammaṇo',
                  'internal and external': 'ajjhattabahiddhārammaṇo'})
# 2-43..2-60: one pair (dyad) plus one triad each; values picked from the two feeling templates by presence,
# with per-segment overrides where the dyad names a different set (fetters, ties, floods, yokes, taints)
DT = [FEEL_D, FEEL_T]
M['2-43'] = auto('2-43', [FEEL_T, FEEL_D])
M['2-44'] = auto('2-44', DT)
M['2-45'] = auto('2-45', DT)
M['2-46'] = auto('2-46', DT)
M['2-47'] = auto('2-47', DT)
M['2-48'] = auto('2-48', DT)
M['2-49'] = auto('2-49', DT, {'feeling dissociated': 'āsavavippayutto', 'feeling joined': 'āsavasampayutto'})
M['2-50'] = auto('2-50', DT, {'dissociated': 'vippayutta', 'feeling dissociated': 'āsavavippayuttasāsavo'})
M['2-51'] = auto('2-51', DT)
M['2-52'] = auto('2-52', DT, {'feeling dissociated': 'saṃyojanavippayutto', 'feeling joined': 'saṃyojanasampayutto',
                              'fetters': 'saṃyojana'})
M['2-53'] = auto('2-53', DT, {'dissociated': 'vippayutta', 'feeling dissociated': 'saṃyojanavippayuttasaṃyojaniyo',
                              'fetters': 'saṃyojana'})
M['2-54'] = auto('2-54', DT, {'cannot': 'aganthaniyo'})
M['2-55'] = auto('2-55', DT, {'feeling dissociated': 'ganthavippayutto', 'feeling joined': 'ganthasampayutto',
                              'feeling fixed': 'micchattaniyato'})
M['2-56'] = auto('2-56', DT, {'able': 'ganthaniyo', 'cause': 'hetuko', 'dissociated': 'vippayutta',
                              'feeling dissociated': 'ganthavippayuttaganthaniyo', 'unable': 'aganthaniyo'})
M['2-57'] = auto('2-57', DT, {'cannot': 'anoghaniyo'})
M['2-58'] = auto('2-58', DT, {'feeling dissociated': 'oghavippayutto', 'feeling joined': 'oghasampayutto',
                              'floods': 'ogha'})
M['2-59'] = auto('2-59', DT, {'able': 'oghaniyo', 'dissociated': 'vippayutta',
                              'feeling dissociated': 'oghavippayuttaoghaniyo', 'floods': 'ogha',
                              'unable': 'anoghaniyo'})
M['2-60'] = auto('2-60', DT, {'bind': 'yoganiyo', 'cannot': 'ayoganiyo'})
M['2-61'] = auto('2-61', [FEEL_D, FEEL_T, CONTACT6, CLASSES], {
 'belong': NDE, 'called the aggregate': 'vuccati vedanākkhandho', 'condition': 'paccayā',
 'expanding': 'vaḍḍhakaṃ', 'feeling born': 'cakkhusamphassajā vedanā', 'Feeling born': 'cakkhusamphassajā vedanā',
 'feeling dissociated': 'yogavippayutto', 'feeling joined': 'yogasampayutto', 'manifold': 'Bahuvidhena',
 'manifold class': 'Bahuvidhena', 'sides': 'Ubhato', 'thirtyfold': 'Tiṃsavidhena', 'thirtyfold class': 'Tiṃsavidhena',
 'twenty-fourfold': 'Catuvīsatividhena', 'twenty-fourfold class': 'Catuvīsatividhena', 'yokes': 'yoga'})
M['2-48']['taints'] = 'āsavo'
M['2-49']['abandoned'] = 'pahātabba'
M['2-53'].update({'expanded': 'mahaggatārammaṇo', 'limited': 'parittārammaṇo', 'measureless': 'appamāṇārammaṇo'})
M['2-61'].update({'external': 'bahiddhārammaṇo', 'internal': 'ajjhattārammaṇo',
                  'internal and external': 'ajjhattabahiddhārammaṇo'})

SETS = {'āsava': ('taints', 'sāsavo', 'anāsavo'), 'saṃyojana': ('fetters', 'saṃyojaniyo', 'asaṃyojaniyo'),
        'gantha': ('ties', 'ganthaniyo', 'aganthaniyo'), 'ogha': ('floods', 'oghaniyo', 'anoghaniyo'),
        'yoga': ('yokes', 'yoganiyo', 'ayoganiyo'), 'nīvaraṇa': ('hindrances', 'nīvaraṇiyo', 'anīvaraṇiyo'),
        'parāmāsa': ('wrong', 'parāmaṭṭho', 'aparāmaṭṭho'), 'upādāna': ('clinging', 'upādāniyo', 'anupādāniyo'),
        'kilesa': ('defilements', 'saṃkilesiko', 'asaṃkilesiko')}


def generic(sid, noun):
    """Overrides that follow from which pair (dyad) and triad the segment's Pali actually has."""
    text = PALI[sid]
    dy = ' '.join(l for l in text.splitlines() if l.startswith('Duvidhena'))
    o = {}
    for x, (setname, pos, neg) in SETS.items():
        if x + 'sampayutto' in dy:
            o.update({noun + ' dissociated': x + 'vippayutto', noun + ' joined': x + 'sampayutto', setname: x})
        elif x + 'vippayutta' in dy:
            o.update({'dissociated': 'vippayutta', noun + ' dissociated': x + 'vippayutta' + pos, setname: x,
                      'able': pos, 'unable': neg})
        elif x == 'āsava' and 'sāsavo' in dy:
            o.update({'taints': 'āsavo'})
        elif ' ' + pos in dy:
            o.update({'cannot': neg, 'able': pos, 'bind': pos, setname: pos})
    if 'hetu' not in dy:
        o.update({'cause': 'hetuko', 'causes': 'hetuko', 'root': 'hetuko'})
    if 'micchattaniyato' in text:
        o[noun + ' fixed'] = 'micchattaniyato'
    if 'araṇo' in dy and 'anāsavo' not in dy:
        o.update({'free': 'araṇo', noun + ' free': 'araṇo'})
    return o


OBJ_FB = {'external': 'bahiddhārammaṇo', 'internal': 'ajjhattārammaṇo',
          'internal and external': 'ajjhattabahiddhārammaṇo', 'expanded': 'mahaggatārammaṇo',
          'limited': 'parittārammaṇo', 'measureless': 'appamāṇārammaṇo', 'abandoned': 'pahātabba'}


def renoun(dct, noun, pali, Noun):
    """Feeling template -> perception/formations/consciousness template (keys and the vedanā values)."""
    out = {}
    for k, v in dct.items():
        k2 = re.sub(r'\bfeeling\b', noun, k).replace('Feeling', Noun)
        if v == 'vedanā':
            v = pali
        v = v.replace('vedanākkhandho', pali + 'kkhandho') if v.endswith('vedanākkhandho') else v
        out[k2] = v
    return out


TRI_V = {'feeling': 'vedanāya', 'joined with feeling': 'vedanāya sampayutto',
         'joined with painful': 'dukkhāya vedanāya sampayutto', 'joined with pleasant': 'sukhāya vedanāya sampayutto',
         'painful': 'dukkhāya', 'painful feeling': 'dukkhāya vedanāya', 'painful nor pleasant': 'adukkhamasukhāya',
         'pleasant': 'sukhāya', 'pleasant feeling': 'sukhāya vedanāya'}
TRI_A = {'accompanied': 'sahagato', 'accompanied by equanimity': 'upekkhāsahagato',
         'accompanied by happiness': 'sukhasahagato', 'accompanied by joy': 'pītisahagato', 'equanimity': 'upekkhā',
         'happiness': 'sukha', 'joy': 'pīti'}
PERC_T = renoun(FEEL_T, 'perception', 'saññā', 'Perception')
PERC_D = renoun(FEEL_D, 'perception', 'saññā', 'Perception')
PERC_T.update({'Aggregate of Perception': 'saññākkhandho'})
PERC_V = dict(TRI_V, **{'perception joined': 'sukhāya vedanāya sampayutto',
                        'Perception joined': 'sukhāya vedanāya sampayutto'})
PERC_A = dict(TRI_A, **{'perception accompanied': 'pītisahagato'})

M['2-1-2-3-0'] = dict(M['2-1-1-3-0'])
M['2-62'] = renoun(M['2-34'], 'perception', 'saññā', 'Perception')
M['2-62'].update({
 'accompanied': 'sahagatā', 'Aggregate of Perception': 'saññākkhandho', 'equanimity': 'upekkhindriya',
 'faculty': 'indriya', 'faculty of equanimity': 'upekkhindriya', 'faculty of gladness': 'somanassindriya',
 'faculty of pain': 'dukkhindriya', 'faculty of pleasure': 'sukhindriya', 'faculty of sadness': 'domanassindriya',
 'gladness': 'somanassindriya', 'pain': 'dukkhindriya', 'perception born': 'cakkhusamphassajā saññā',
 'Perception born': 'cakkhusamphassajā saññā', 'perception joined': 'sukhindriyasampayutto',
 'Perception joined': 'sukhindriyasampayutto', 'perception not included': 'apariyāpanno', 'pleasure': 'sukhindriya',
 'sadness': 'domanassindriya'})
for _i in range(63, 91):
    _sid = f'2-{_i}'
    _dy = ' '.join(l for l in PALI[_sid].splitlines() if l.startswith('Duvidhena'))
    _bases = [PERC_T, PERC_D] if 'sahetuko, atthi ahetuko' in _dy else [PERC_D, PERC_T]
    M[_sid] = auto(_sid, _bases + [PERC_V, PERC_A, CLASSES, OBJ_FB], generic(_sid, 'perception'))
    if 'Perception joined' not in M[_sid] and 'perception joined' in M[_sid]:
        M[_sid]['Perception joined'] = M[_sid]['perception joined']
for _i in range(43, 61):
    M[f'2-{_i}'].update(generic(f'2-{_i}', 'feeling'))
M['2-65']['perception not accompanied'] = 'na pītisahagato'
M['2-66'].update({'pairs': 'Duka', 'rooted': 'mūlakaṃ', 'treatment': 'vitthāro', 'triad': 'tike', 'triads': 'tikā',
                  'wholesome': 'kusala'})
M['2-70'].update({'rooted': 'mūlakaṃ', 'triads': 'Tika'})


def closing(sid, noun, Noun, pali, bases):
    """Last segment of each aggregate (2-61 pattern): extended classes conditioned by the six contacts."""
    text = PALI[sid]
    o = {
     'belong': NDE, 'belonging': NDE, noun + ' belonging': NDE,
     'called the aggregate': f'vuccati {pali}kkhandho', 'condition': 'paccayā', 'expanding': 'vaḍḍhakaṃ',
     noun + ' born': f'cakkhusamphassajā {pali}', Noun + ' born': f'cakkhusamphassajā {pali}',
     noun + ' not included': 'apariyāpanno', 'manifold': 'Bahuvidhena', 'manifold class': 'Bahuvidhena',
     'sides': 'Ubhato', 'twenty-fourfold': 'Catuvīsatividhena', 'twenty-fourfold class': 'Catuvīsatividhena',
     'thirtyfold': 'Tiṃsatividhena' if 'Tiṃsatividhena' in text else 'Tiṃsavidhena'}
    o['thirtyfold class'] = o['thirtyfold']
    o.update(generic(sid, noun))
    return auto(sid, bases + [CONTACT6, CLASSES, OBJ_FB], o)


M['2-91'] = closing('2-91', 'perception', 'Perception', 'saññā', [PERC_D, PERC_T, PERC_V])
M['2-91']['Perception joined'] = M['2-91']['perception joined']

# ---- aggregate of mental formations (Abhidhamma classification) ----
SKX = {'aggregate of mental': 'saṅkhārakkhandho', 'Aggregate of Mental': 'saṅkhārakkhandho', 'formations': 'saṅkhāra',
       'mental': 'saṅkhāra', 'Mental Formations': 'saṅkhāra', 'mental formations': 'saṅkhāra',
       'joined with mind': 'cittasampayutto', 'mind': 'citta', 'joined': 'sampayutto', 'themselves': NDE}
SK_T = renoun(FEEL_T, 'formations', 'saṅkhāra', 'Formations')
SK_D = renoun(FEEL_D, 'formations', 'saṅkhāra', 'Formations')
SK_V = dict(TRI_V, **{'formations joined': 'sukhāya vedanāya sampayutto',
                      'Formations joined': 'sukhāya vedanāya sampayutto'})
SK_A = dict(TRI_A, **{'formations accompanied': 'pītisahagato', 'formations not accompanied': 'na pītisahagato'})
for _d in (SK_T, SK_D):
    for _k in list(_d):
        if _k.startswith('formations that produce'):
            _d['formations that produce'] = _d[_k]
M['2-1-2-4-0'] = dict(M['2-1-1-4-0'])
M['2-92'] = renoun(M['2-34'], 'formations', 'saṅkhāra', 'Formations')
M['2-92'].update(SKX)
M['2-92'].update({
 'accompanied': 'sahagatā', 'causes': 'hetu', 'contact': 'samphassa', 'equanimity': 'upekkhindriya',
 'faculty': 'indriya', 'faculty of equanimity': 'upekkhindriya', 'faculty of gladness': 'somanassindriya',
 'faculty of pain': 'dukkhindriya', 'faculty of pleasure': 'sukhindriya', 'faculty of sadness': 'domanassindriya',
 'formations belonging': NDE, 'formations joined': 'sukhindriyasampayutto',
 'Formations joined': 'sukhindriyasampayutto', 'gladness': 'somanassindriya', 'intention': 'cetanā',
 'intention born': 'cakkhusamphassajā cetanā', 'Intention born': 'cakkhusamphassajā cetanā',
 'neutral formations': 'abyākato', 'pain': 'dukkhindriya', 'pleasure': 'sukhindriya', 'root': 'hetu',
 'sadness': 'domanassindriya', 'unwholesome formations': 'akusalo', 'Unwholesome formations': 'akusalo',
 'wholesome formations': 'kusalo'})
for _i in range(93, 120):
    _sid = f'2-{_i}'
    _dy = ' '.join(l for l in PALI[_sid].splitlines() if l.startswith('Duvidhena'))
    _bases = [SK_T, SK_D] if 'sahetuko, atthi ahetuko' in _dy else [SK_D, SK_T]
    M[_sid] = auto(_sid, [SKX] + _bases + [SK_V, SK_A, CLASSES, OBJ_FB], generic(_sid, 'formations'))
    if 'Formations joined' not in M[_sid] and 'formations joined' in M[_sid]:
        M[_sid]['Formations joined'] = M[_sid]['formations joined']
M['2-93']['produce'] = 'vipākadhammadhammo'
M['2-102']['produce'] = 'vipākadhammadhammo'
M['2-95'].update({'pairs': 'Duka', 'rooted': 'mūlakaṃ'})
M['2-99'].update({'rooted': 'mūlakaṃ', 'triads': 'Tika'})
M['2-108']['taints'] = 'āsavo'
M['2-114']['fetters'] = 'saṃyojanaṃ'
M['2-117']['fetters'] = 'saṃyojanaṃ'
M['2-118']['fetters'] = 'saṃyojanaṃ'
M['2-120'] = closing('2-120', 'formations', 'Formations', 'saṅkhāra', [SKX, SK_D, SK_T, SK_V])
M['2-120'].update({'called the aggregate': 'vuccati saṅkhārakkhandho', 'formations born': 'cakkhusamphassajā cetanā',
                   'Formations born': 'cakkhusamphassajā cetanā', 'intention': 'cetanā',
                   'intention born': 'cakkhusamphassajā cetanā', 'Intention born': 'cakkhusamphassajā cetanā',
                   'ties': 'gantho'})
if 'formations joined' in M['2-120']:
    M['2-120']['Formations joined'] = M['2-120']['formations joined']

# ---- aggregate of consciousness (Abhidhamma classification) ----
VI_T = renoun(FEEL_T, 'consciousness', 'viññāṇa', 'Consciousness')
VI_D = renoun(FEEL_D, 'consciousness', 'viññāṇa', 'Consciousness')
VIX = {'Aggregate of Consciousness': 'viññāṇakkhandho'}
VI_V = dict(TRI_V, **{'consciousness joined': 'sukhāya vedanāya sampayutto',
                      'Consciousness joined': 'sukhāya vedanāya sampayutto'})
VI_A = dict(TRI_A, **{'consciousness accompanied': 'pītisahagato', 'consciousness not accompanied': 'na pītisahagato'})
M['2-1-2-5-0'] = dict(M['2-1-1-5-0'])
M['2-121'] = renoun(M['2-34'], 'consciousness', 'viññāṇa', 'Consciousness')
M['2-121'].update(VI6)
M['2-121'].update(VIX)
M['2-121'].update({
 'accompanied': 'sahagataṃ', 'consciousness': 'viññāṇa', 'consciousness belonging': NDE,
 'consciousness joined': 'sukhindriyasampayutto', 'Consciousness joined': 'sukhindriyasampayutto',
 'consciousness not included': 'apariyāpanno', 'equanimity': 'upekkhindriya', 'faculty': 'indriya',
 'faculty of equanimity': 'upekkhindriya', 'faculty of gladness': 'somanassindriya', 'faculty of pain': 'dukkhindriya',
 'faculty of pleasure': 'sukhindriya', 'faculty of sadness': 'domanassindriya', 'gladness': 'somanassindriya',
 'pain': 'dukkhindriya', 'pleasure': 'sukhindriya', 'sadness': 'domanassindriya'})
for _i in range(122, 149):
    _sid = f'2-{_i}'
    _dy = ' '.join(l for l in PALI[_sid].splitlines() if l.startswith('Duvidhena'))
    _bases = [VI_T, VI_D] if 'sahetuko, atthi ahetuko' in _dy else [VI_D, VI_T]
    M[_sid] = auto(_sid, [VIX] + _bases + [VI_V, VI_A, CLASSES, OBJ_FB], generic(_sid, 'consciousness'))
    if 'Consciousness joined' not in M[_sid] and 'consciousness joined' in M[_sid]:
        M[_sid]['Consciousness joined'] = M[_sid]['consciousness joined']
M['2-124'].update({'pairs': 'Duka', 'rooted': 'mūlakaṃ', 'treatment': 'vitthāro', 'triad': 'tike', 'triads': 'tikā',
                   'wholesome': 'kusala'})
M['2-128'].update({'rooted': 'mūlakaṃ', 'triads': 'Tika'})
M['2-149'] = closing('2-149', 'consciousness', 'Consciousness', 'viññāṇa', [VIX, VI_D, VI_T, VI_V])
M['2-149'].update({'consciousness born': 'cakkhuviññāṇaṃ', 'Consciousness born': 'cakkhuviññāṇaṃ'})
M['2-149'].update({k: v for k, v in VI6.items() if k != 'consciousness'})
if 'consciousness joined' in M['2-149']:
    M['2-149']['Consciousness joined'] = M['2-149']['consciousness joined']
M['2-149'].update({'abhidhamma': 'Abhidhamma', 'classification': 'bhājanīyaṃ', 'finished': NDE})

# ---- section of questions and answers ----
QA = {'answers': NDE, 'questions': 'Pañhā', 'Questions and Answers': 'Pañhāpucchakaṃ', 'section': NDE,
      'Section of Questions': 'Pañhāpucchakaṃ'}
M['2-1-3-0'] = dict(QA)
M['2-150'] = dict(M['2-1'])
M['2-151'] = {'aggregates': 'khandhānaṃ', 'conflict': 'saraṇā', 'free': 'araṇā', 'involve': 'saraṇā',
              'neutral': 'abyākatā', 'unwholesome': 'akusalā', 'wholesome': 'kusalā'}
M['2-1-3-1-0'] = {'triads': 'Tikaṃ'}
M['2-152'] = {
 'abandoned': 'pahātabbo', 'able': 'upādāniyo', 'accompanied': 'sahagato', 'accompanied by equanimity': 'upekkhāsahagato',
 'accompanied by happiness': 'sukhasahagato', 'accompanied by joy': 'pītisahagato', 'accumulation': 'ācaya',
 'aggregate': 'khandho', 'aggregate of feeling': 'Vedanākkhandho', 'aggregate of material': 'Rūpakkhandho',
 'aggregate of mental': 'Saṅkhārakkhandho', 'Aggregate of Mental': 'Saṅkhārakkhandho', 'aggregates': 'khandhā',
 'aggregates may belong': 'khandhā siyā', 'arise': 'uppādino', 'arisen': 'uppannā', 'belong': NDE, 'belongs': NDE,
 'beyond': 'asekkhā', 'birth': NDE, 'bound': 'uppādino', 'cannot': 'na', 'cause': 'hetukā', 'causes': 'hetukā',
 'clung': 'upādāniyo', 'defiled': 'saṃkiliṭṭha', 'defilement': 'saṃkilesiko', 'describable': 'vattabbo',
 'described': 'vattabbā', 'dismantling': 'apacaya', 'dominant': 'ādhipatino', 'dominant factor': 'ādhipatino',
 'equanimity': 'upekkhā', 'examination': 'vicāro', 'expanded': 'mahaggatā', 'expanded object': 'mahaggatārammaṇā',
 'external': 'bahiddhā', 'external object': 'bahiddhārammaṇā', 'factor': 'ādhipatino', 'feeling': 'vedanāya',
 'fixed': 'niyatā', 'form': 'Rūpa', 'formations': 'Saṅkhāra', 'future object': 'anāgatārammaṇā', 'happiness': 'sukha',
 'having': NDE, 'inferior': 'hīnā', 'internal': 'ajjhattā', 'internal and external': 'ajjhattabahiddhā',
 'internal object': 'ajjhattārammaṇā', 'invisible': 'anidassana', 'invisible and offer': 'anidassanasappaṭigho',
 'joined': 'sampayuttā', 'joined with feeling': 'vedanāya sampayuttā',
 'joined with painful': 'dukkhāya vedanāya sampayuttā', 'joined with pleasant': 'sukhāya vedanāya sampayuttā',
 'joy': 'pīti', 'leads': 'gāmī', 'limited': 'paritto', 'limited object': 'parittārammaṇā', 'material': 'Rūpa',
 'material form': 'Rūpa', 'measureless': 'appamāṇā', 'measureless object': 'appamāṇārammaṇā',
 'meditative': 'bhāvanāya', 'meditative development': 'bhāvanāya', 'mental': 'Saṅkhāra',
 'Mental Formations': 'Saṅkhāra', 'mental formations': 'Saṅkhāra', 'middling': 'majjhimo', 'neutral': 'abyākato',
 'object': 'ārammaṇo', 'object both internal': 'ajjhattabahiddhārammaṇā', 'open to defilement': 'saṃkilesiko',
 'outcome': NDE, 'painful': 'dukkhāya', 'painful feeling': 'dukkhāya vedanāya',
 'painful nor pleasant': 'adukkhamasukhāya', 'past object': 'atītārammaṇā', 'path': 'magga', 'pleasant': 'sukhāya',
 'pleasant feeling': 'sukhāya vedanāya', 'present object': 'paccuppannārammaṇā', 'produce': 'vipākadhammadhammā',
 'produces': 'vipākadhammadhammo', 'resistance': 'sappaṭigho', 'rightness': 'sammatta', 'root': 'hetuko',
 'seeing': 'dassanena', 'something': NDE, 'superior': 'paṇītā', 'thought': 'vitakka',
 'thought and examination': 'savitakkasavicārā', 'trainees': 'sekkhā', 'training': 'asekkhā',
 'undefiled': 'asaṃkiliṭṭha', 'unwholesome': 'akusalā', 'visible': 'sanidassana', 'wholesome': 'kusalā',
 'wrongness': 'micchatta',
}
M['2-1-3-2-0'] = {'pairs': 'Dukaṃ'}
M['2-153'] = dict(QA, **{
 'abandoned': 'pahātabbo', 'able': 'saṃyojaniyā', 'accompanied': 'sahagato',
 'accompanied by equanimity': 'upekkhāsahagatā', 'accompanied by happiness': 'sukhasahagatā',
 'accompanied by joy': 'pītisahagato', 'aggregate': 'khandho', 'aggregate of consciousness': 'Viññāṇakkhandho',
 'Aggregate of Consciousness': 'Viññāṇakkhandho', 'aggregate of material': 'Rūpakkhandho',
 'aggregate of mental': 'Saṅkhārakkhandho', 'Aggregate of Mental': 'Saṅkhārakkhandho', 'aggregates': 'khandhā',
 'aggregates are mingled': 'khandhā cittasaṃsaṭṭhā', 'aggregates may belong': 'khandhā siyā',
 'along': 'ānuparivattino', 'analysis': 'vibhaṅgo', 'arise': 'sahabhuno', 'belong': NDE, 'belongs': NDE,
 'beyond': 'uttarā', 'birth': NDE, 'bound': 'saṃyojaniyo', 'cannot': 'na', 'cause': 'hetu', 'causes': 'hetū',
 'clinging': 'upādānā', 'clinging joined': 'upādānā ceva upādānasampayuttā', 'clung': 'upādāniyo',
 'compounded': 'saṅkhatā', 'conflict': 'saraṇā', 'consciousness': NDE, 'defiled': 'saṃkiliṭṭhā',
 'defilement': 'saṃkilesiko', 'defilement joined': 'kileso ceva kilesasampayutto', 'defilements': 'kilesā',
 'defilements joined': 'kilesā ceva kilesasampayuttā', 'derived': 'upādā', 'describable': 'vattabbo',
 'described': 'vattabbā', 'dissociated': 'vippayutto', 'dissociated from clinging': 'upādānavippayutto',
 'dissociated from wrong': 'parāmāsavippayutto', 'equanimity': 'upekkhā', 'examination': 'vicāro',
 'existence': NDE, 'external': 'bāhirā', 'factors': 'cetasikā', 'fetter': 'saṃyojanaṃ',
 'fetter joined': 'saṃyojanañceva saṃyojanasampayutto', 'fetters': 'saṃyojanā',
 'fetters joined': 'saṃyojanā ceva saṃyojanasampayuttā', 'fine-material': 'rūpāvacaro',
 'fine-material sphere': 'rūpāvacaro', 'finished': 'niṭṭhito', 'fixed': 'niyatā', 'floods': 'oghā',
 'follow': 'ānuparivattino', 'form': 'Rūpa', 'form is dissociated': 'Rūpakkhandho hetuvippayutto',
 'formations': 'Saṅkhāra', 'free': 'anāsavā', 'grasped': 'parāmaṭṭho', 'grasping': 'parāmāso', 'happiness': 'sukha',
 'having': 'sahetuko', 'hindrance': 'nīvaraṇaṃ', 'hindrance joined': 'nīvaraṇañceva nīvaraṇasampayutto',
 'hindrances': 'nīvaraṇā', 'hindrances joined': 'nīvaraṇā ceva nīvaraṇasampayuttā', 'immaterial': 'arūpā',
 'immaterial sphere': 'arūpāvacaro', 'internal': 'ajjhattiko', 'invisible': 'anidassanā', 'involve': 'saraṇā',
 'joined': 'sampayuttā', 'joined with clinging': 'upādānasampayuttā', 'joined with mind': 'cittasampayuttā',
 'joined with root': 'hetusampayuttā', 'joy': 'pīti', 'kinds': NDE, 'kinds of consciousness': 'kenaci',
 'knowable': 'viññeyyā', 'material': 'Rūpa', 'material form': 'Rūpa', 'meditative': 'bhāvanāya',
 'meditative development': 'bhāvanāya', 'mental': 'Saṅkhāra', 'mental factors': 'cetasikā',
 'Mental Formations': 'Saṅkhāra', 'mental formations': 'Saṅkhāra', 'mental taints': 'āsavā', 'mind': 'cittaṃ',
 'mingled': 'saṃsaṭṭhā', 'mingled with mind': 'cittasaṃsaṭṭhā', 'object': 'ārammaṇo', 'objects': 'sārammaṇā',
 'obstructed': 'nīvaraṇiyo', 'open to defilement': 'saṃkilesiko', 'others': 'kenaci', 'outcome': NDE,
 'outside': 'apariyāpannā', 'produced': 'samuṭṭhānā', 'resistance': 'sappaṭigho', 'root': 'hetu',
 'root cause joined': 'hetu ceva hetusampayutto', 'root causes joined': 'hetū ceva hetusampayuttā', 'round': NDE,
 'seeing': 'dassanena', 'sense': 'kāmāvacaro', 'sense sphere': 'kāmāvacaro', 'sphere': 'āvacaro',
 'surpassable': 'sauttarā', 'surpassed': 'sauttaro', 'taint': 'āsavo', 'taint joined': 'āsavo ceva āsavasampayutto',
 'taints': 'āsavā', 'taints joined': 'āsavā ceva āsavasampayuttā', 'thought': 'vitakko', 'tie': 'gantho',
 'tie joined': 'gantho ceva ganthasampayutto', 'tied': 'ganthaniyo', 'ties': 'ganthā',
 'ties joined': 'ganthā ceva ganthasampayuttā', 'together': 'saha', 'unable': 'asaṃyojaniyā',
 'undefiled': 'asaṃkiliṭṭho', 'unsurpassable': 'anuttarā', 'visible': 'sanidassano', 'worldly': 'lokiyo',
 'wrong': 'parāmāsā', 'wrong grasping': 'parāmāsā', 'wrongly': 'parāmaṭṭho', 'wrongly grasped': 'parāmaṭṭho',
 'yokes': 'yogā'})
M['2-1-1-2-0'] = dict(M['2-1-2-2-0'])
# @@END@@

if __name__ == '__main__':
    out, missing, unused = [], [], []
    for line in (d / f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines():
        sid, kws = line.split('] ', 1)
        sid = sid[1:]
        if sid not in M:
            missing.append((sid, '*')); continue
        m = M[sid]
        pairs = []
        ks = [k.strip() for k in kws.split(', ')]
        for k in ks:
            if k not in m:
                missing.append((sid, k)); pairs.append(f'???={k}')
            else:
                pairs.append(f'{m[k]}={k}')
        unused += [(sid, k) for k in m if k not in ks]
        out.append(f'[{sid}] ' + ', '.join(pairs))
    (d / f'{ch}.mapped.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('written', len(out))
    print('missing', [x for x in missing if x[1] != '*'])
    print('segments not yet mapped', len([x for x in missing if x[1] == '*']))
    print('unused count', len(unused))
