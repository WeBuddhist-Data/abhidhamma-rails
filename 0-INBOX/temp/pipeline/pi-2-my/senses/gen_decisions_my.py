"""Write the Pāli→Burmese pi-2 decisions file for senses_my.py (brief: pi-2-my/burmese-senses-brief.md).
Adapted from pi-1-my/senses/gen_decisions_my.py (same MANUAL / LUMP_OK mechanism).

usage: python -I -X utf8 gen_decisions_my.py <agg.tsv> <decisions.txt>

For every headword of agg.tsv that has Burmese values (NDE-only headwords are skipped):
  1. a hand decision in MANUAL below wins;
  2. otherwise, if the approved pi-1 Burmese senses file has the headword (exact, else the one
     case-insensitive match: the aggregation keeps the first spelling seen), its senses are BINDING:
     every pi-2 value that pi-1 lists goes under pi-1's sense with pi-1's English tag, in pi-1's
     sense order (a pi-1 sense with no pi-2 value is left out). A pi-2 value that pi-1 does not list
     is REVIEW (pi-1 has one sense: add the headword to LUMP_OK if the value is a variant / synonym
     of that sense, else MANUAL) or UNRESOLVED (pi-1 has several senses: MANUAL);
  3. otherwise, if the Marathi pi-2 senses file gives the headword ONE English tag, the line is that
     tag + every attested Burmese value (one sense; several values -> REVIEW unless LUMP_OK);
  4. otherwise (several Marathi senses, or no Marathi line) the headword is UNRESOLVED: write MANUAL.
Only the ENGLISH tags are read from the Marathi file; its Marathi values are dropped on parsing and
never written. A MANUAL entry for a pi-1 headword must keep pi-1's split: every value pi-1 lists sits
under a sense whose tag starts with pi-1's tag for it (an appended «, the same value also naming …»
is allowed) unless the headword is in P1_TAG_CHANGED (logged reason).
The script fails (exit 1) while anything is UNRESOLVED, a MANUAL value is not attested, a MANUAL entry
omits an attested value, or a MANUAL entry breaks a pi-1 sense.
"""
import pathlib
import re
import sys
from collections import OrderedDict

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
MY1_SENSES = ROOT / 'AI_translation/burmese/pi-1-pali-word-burmese-senses-plain.md'
MR_SENSES = ROOT / 'AI_translation/marathi/pi-2-pali-word-marathi-senses-plain.md'
VAL_RE = re.compile(r'^(.*)=(\d+)\[[^\]]*\]$')
NONLATIN = re.compile(r'[ऀ-ॿက-႟]')

# Hand decisions: headword -> [(English tag, [Burmese values])]. Values must be attested.
# pi-1 senses first (pi-1 order, pi-1 tag), then the senses new in pi-2.
MANUAL = OrderedDict([
    # ---- sample: pi-1 senses, a value pi-1 lacks placed in its pi-1 sense ----
    ('rūpa', [
        ('the fine-material sphere, as in rūpāvacara and rūpūpapatti (compound member), rūpa in '
         'rūpasaññā of the immaterial-jhāna formula being given under matter',
         ['သိမ်မွေ့သော ရုပ်']),
        ('visible form, the object of the eye (compound member, as in rūpārammaṇa)', ['အဆင်းအရောင်']),
        ('matter, material form (heading and compound member, as in Rūpakaṇḍa and rūpakkhandha), also '
         'the material side of nāmarūpa (in nāmarūpapaccayā)',
         ['ရုပ်', 'ရုပ်ပိုင်း']),
    ]),
    # ---- sample: pi-1 senses + a genuinely new pi-2 meaning ----
    ('rūpaṃ', [
        ('matter, material form (nominative/accusative sg.), also the material side of nāmarūpa',
         ['ရုပ်', 'ရုပ်ပိုင်း']),
        ('visible form, the object of the eye, in the restraint passage (accusative sg.)',
         ['အဆင်းအရောင်']),
        ("of such a nature, in piyarūpaṃ sātarūpaṃ 'what is dear and pleasing' (compound final)",
         ['သဘော ရှိသော', 'သဘော']),
    ]),
    ('Āyatana', [
        ('sense bases, the sense fields (compound member)', ['အာရုံခံ နယ်ပယ်']),
        ('sphere, in the names of the immaterial attainments such as ākāsānañcāyatana (compound final)',
         ['နယ်ပယ်']),
    ]),
    ('āyatanaṃ', [
        ('sense base, the sense field (nominative/accusative sg.)', ['အာရုံခံ နယ်ပယ်']),
        ('sphere, in the names of the immaterial attainments such as ākāsānañcāyatanaṃ (compound final)',
         ['နယ်ပယ်']),
    ]),
    ('Dhātu', [
        ('element, irreducible constituent (stem and compound final)', ['ဓာတ်']),
        ('realm, plane of existence, in kāmadhātu, rūpadhātu and arūpadhātu (compound final)', ['ဘုံ']),
    ]),
    ('Magga', [
        ('the path (stem and heading)', ['မဂ်']),
        ("way, road, in kummagga 'wrong way' (compound member)", ['လမ်း']),
    ]),
    ('āhāro', [
        ('nutriment, a sustaining condition of mind (contact, volition, consciousness), also edible '
         'food as nutriment, in kabaḷīkāro āhāro and the four nutriments',
         ['အာဟာရ']),
        ("food, what is eaten, in evamāhāro 'having such food' of the past-lives formula (compound final)",
         ['အစာ']),
    ]),
    ('Tattha', [
        ('therein, in that connection, opening a definition (locative)', ['ထိုတို့အနက်']),
        ("in that, in the case just described, in 'yā tattha paññā' 'the understanding therein' (locative)",
         ['ထို၌']),
    ]),
    ('ajjhattaṃ', [
        ("internally, within oneself, as in 'ajjhattaṃ arūpasaññī' and 'ajjhattaṃ sampasādanaṃ' (adverb)",
         ['မိမိ၌', 'မိမိ၏ အတွင်း၌ ဖြစ်သော']),
        ("internal, one's own as opposed to others' (internal and external pair)", ['မိမိ၌ ရှိသော']),
    ]),
    ('Dukkha', [
        ("painful, hard, as in dukkhapaṭipadā 'painful practice' (compound member)", ['ခက်ခဲသော']),
        ('pain, painful feeling or painful to the touch (compound member, as in dukkhasahagata and '
         'dukkhasamphassa)',
         ['နာကျင်သော', 'နာကျင်မှု', 'ကိုယ်ဆင်းရဲခြင်း']),
        ('suffering, the whole of what is unsatisfactory, in dukkhamūla and dukkhakkhandha (compound '
         'member)',
         ['ဒုက္ခ']),
        ("misery, affliction in the everyday sense, in dukkhadhammena phuṭṭhassa 'touched by some "
         "painful thing' and sukhadukkha 'pleasure and pain' of the views (compound member)",
         ['ဆင်းရဲ']),
    ]),
    # ---- sample: one pi-1 sense, the same value also carrying a second meaning in pi-2 ----
    ('saṅkhāra', [
        ('mental formations, volitional activities (compound member, in saṅkhārakkhandha), the same '
         'value also naming the formation of striving, in padhānasaṅkhāra of the bases of power',
         ['ပြုပြင်ဖန်တီးမှု']),
    ]),
    ('upādāya', [
        ('derived from, depending on the great elements, as in upādāya rūpaṃ (absolutive), the same '
         "value also naming 'with reference to', in ajjhattikassa upādāya and 'hetū paccayā upādāya'",
         ['မှီ၍']),
    ]),
    # ======== full run (agg-part1.tsv): REVIEW headwords split by hand ========
    # ---- pi-1 senses kept, a genuinely new pi-2 meaning added ----
    ('Hetu', [
        ('roots, the wholesome and unwholesome root conditions (stem and heading)', ['အမြစ်']),
        ('cause, condition, in Hetucatukka of dependent origination and Hetuvāra of the analytical '
         'knowledges (heading member)', ['အကြောင်းပြုခြင်း', 'အကြောင်းရင်း']),
    ]),
    ('Jāti', [
        ('birth, being born (nominative sg.)', ['မွေးဖွားခြင်း']),
        ("birth as social standing, descent, in jātimada 'pride of birth' (compound member)", ['ဇာတိ']),
    ]),
    ('paṭighāto', [
        ('resentment, striking back (nominative sg.)', ['ပြန်လည် ရန်ငြိုးဖွဲ့ခြင်း']),
        ("impingement, the mind's being struck, in 'lokadhammesu cittassa paṭighāto' (nominative sg.)",
         ['ထိခိုက်မှု']),
    ]),
    ('purisa', [
        ("man, in purisaliṅga 'feature of a man', also masculinity, in purisindriya (compound member)",
         ['ယောက်ျား']),
        ("person, individual, in purisadosā 'faults of a person' (compound member)", ['လူ']),
    ]),
    ('Rūpadhātu', [
        ('the visible-form element, the object of the eye (nominative sg.)', ['အဆင်းအရောင် ဓာတ်']),
        ('the fine-material realm of existence, among the planes (nominative sg.)', ['သိမ်မွေ့သော ရုပ်ဘုံ']),
    ]),
    ('hetukaṃ', [
        ('having roots, rooted, in pahātabbahetukaṃ (compound final)', ['အမြစ်']),
        ('caused by, having X as its cause, as in cittahetukaṃ (compound final)', ['အကြောင်းပြုသော']),
    ]),
    ('sutaṃ', [
        ('heard, what is heard (neuter sg. participle)', ['ကြားရသော']),
        ("learning, what one has heard and studied, in sutamada 'pride of learning' (compound member)",
         ['အကြားအမြင်']),
    ]),
    ('paccayā', [
        ('with X as condition, in the dependent origination formula', ['ကြောင့်']),
        ('born of, arising with X as condition, of feeling and the like in cakkhusamphassapaccayā and '
         'similar (compound final)', ['အကြောင်းပြု၍']),
    ]),
    ('yoga', [
        ('the yokes, bonds (heading member)', ['ထမ်းပိုး']),
        ("skill, application, in yogavihita 'made with skill' (compound member)", ['ပညာရှိ']),
    ]),
    ('Kāyo', [
        ('the physical body, or bodily (nominative sg.)', ['ကိုယ်']),
        ("the mental body, the group of mental factors, in 'katamo kāyo? saññākkhandho …' (nominative sg.)",
         ['စိတ်၏ အဖော်တို့']),
    ]),
    ('Sotaṃ', [
        ('the ear, the hearing organ (accusative sg.)', ['နား']),
        ('stream, current, an epithet of craving (nominative sg.)', ['ရေစီးကြောင်း']),
    ]),
    ('dukkhaṃ', [
        ('pain, suffering (nominative/accusative sg.), here painful feeling, also attributive in '
         'dukkhaṃ vedanaṃ', ['နာကျင်မှု', 'နာကျင်သော']),
        ('suffering in the sense of the noble truth, the unsatisfactoriness of what is conditioned '
         '(nominative sg.)', ['ဒုက္ခ']),
    ]),
    ('pasādo', [
        ('sensitivity, the sensitive matter of a sense organ (nominative sg.)', ['အာရုံခံ ကြည်လင်မှု']),
        ('confidence, serene trust, in the faith-based chain of conditions (nominative sg.)', ['ကြည်ညိုမှု']),
    ]),
    ('taca', [
        ('bark of a tree (compound member)', ['အခေါက်']),
        ("skin, in valittacatā 'wrinkled skin' (compound member)", ['အရေ']),
    ]),
    ('patta', [
        ("leaf, foliage (compound member), also in pattadāna 'gift of leaves'", ['အရွက်', 'သစ်ရွက်']),
        ('the alms bowl, in pattacīvara and pattamaṇḍanā (compound member)', ['သပိတ်']),
    ]),
    ('mūla', [
        ('root of a plant (compound member), the same value also naming the root condition, in '
         'kusalamūla and akusalamūla', ['အမြစ်']),
        ('foot of a tree, in rukkhamūla (compound member)', ['ရင်း']),
    ]),
    ('mūlaṃ', [
        ('root, as in kusalamūla (nominative sg.)', ['အမြစ်']),
        ('foot of a tree, in rukkhamūlaṃ (nominative sg.)', ['ရင်း']),
    ]),
    ('kasāvo', [
        ('astringent in taste (nominative sg.)', ['အဖန်']),
        ('stain, corruption, in rāgakasāvo and the three stains (nominative sg.)', ['အမည်းအစက်']),
    ]),
    ('raso', [
        ('taste, flavour as object (nominative sg.)', ['အရသာ']),
        ('juice, sap, in mūlaraso and similar (compound final)', ['အရည်']),
    ]),
    ('parittā', [
        ('limited, small in scope (nominative pl.)', ['အကန့်အသတ် ရှိသော']),
        ("gentle, mild, of winds, in 'parittā vātā' (nominative pl.)", ['အားနည်းသော']),
    ]),
    ('hadayaṃ', [
        ('heart, as a synonym of mind (neuter sg.)', ['နှလုံးသား']),
        ('the heart, the bodily organ, in the list of body parts (neuter sg.)', ['နှလုံး']),
    ]),
    ('mukha', [
        ('the mouth, through which food is eaten (compound member)', ['ခံတွင်း']),
        ("the face area, in parimukhaṃ 'in front, before the face' (compound member)", ['နှုတ်ခမ်းအထက်']),
    ]),
    ('sukhaṃ', [
        ('pleasure, happiness, or pleasant (neuter sg.)', ['သာယာမှု', 'သာယာသော']),
        ('comfort, ease, in seyyasukhaṃ, passasukhaṃ and middhasukhaṃ (compound final)', ['ချမ်းသာ']),
    ]),
    ('doso', [
        ('hatred, hostility (nominative sg.)', ['ဒေါသ']),
        ("fault, danger, in 'natthi kāmesu doso' 'there is no fault in sense pleasures' (nominative sg.)",
         ['အပြစ်']),
    ]),
    ('pariyantaṃ', [
        ('boundary, the lower limit (accusative sg.)', ['အဆုံးအစွန်', 'အဆုံး']),
        ("bounded by, enclosed within, in tacapariyantaṃ 'enclosed by the skin' (compound final)",
         ['ဝန်းရံထားသော']),
    ]),
    ('sati', [
        ('mindfulness, alert presence of mind (nominative sg.)', ['သတိ']),
        ("'when that exists', locative of atthi in tasmiṃ sati (participle)", ['ရှိသော']),
    ]),
    ('nimittaṃ', [
        ('sign, characteristic mark (nominative sg.)', ['အမှတ်အသား']),
        ('hint, a sign given to obtain gifts, in the definition of hinting (nominative sg.)',
         ['အရိပ်အမြွက် ပြခြင်း']),
    ]),
    ('nāma', [
        ('mentality, the mental side of name-and-form (compound member)', ['စိတ်ပိုင်း']),
        ("even, indeed, emphatic particle, in 'tvampi nāma' (indeclinable)", ['ပင်လျှင်']),
    ]),
    ('Dukkhe', [
        ('about suffering, the first truth (locative)', ['ဒုက္ခ']),
        ("in the painful, misery in the everyday sense, in the perversion 'dukkhe sukhan'ti' and the "
         "worldly condition 'dukkhe paṭivirodho' (locative)", ['ဆင်းရဲသော', 'ဆင်းရဲ']),
    ]),
    ('āpajjati', [
        ('takes up, comes to practise (restraint) (3rd sg. present)', ['ပြုသည်']),
        ('sets about, applies oneself, as in parivīmaṃsaṃ āpajjati and yogaṃ āpajjati (3rd sg. present)',
         ['ရောက်သည်', 'ဝင်ရောက် ဆောင်ရွက်သည်']),
    ]),
    ('saritā', [
        ('stream, flowing current, of craving (feminine sg.)', ['စီးဆင်းတတ်သူ']),
        ('one who remembers (agent noun, masculine sg.)', ['အောက်မေ့သူ']),
    ]),
    ('dhammaṃ', [
        ('mind-objects, what the mind as sixth sense knows (accusative sg.), the same value also naming '
         'a phenomenon, any state, as in na kañci dhammaṃ', ['သဘောတရား']),
        ("the teaching, the doctrine heard and remembered, in 'dhammaṃ jānāti – suttaṃ geyyaṃ' "
         "(accusative sg.)", ['တရား']),
    ]),
    ('sato', [
        ('mindful, attentive (masculine sg.)', ['သတိ ရှိသော']),
        ("existing, actually present, in 'sato sattassa' 'of an existing being' (genitive sg. participle)",
         ['ရှိနေသော']),
    ]),
    ('paṭigha', [
        ('aversion, resentment (compound member)', ['မုန်းတီးမှု']),
        ('sensory impingement, in paṭighasaññā (compound member)', ['ထိခိုက်မှု']),
    ]),
    ('samāpattiyā', [
        ('by engaging in, entering upon (instrumental/genitive sg.), of bad and of good states',
         ['ကျူးလွန်ခြင်း', 'ရောက်ရှိရန်']),
        ('meditative attainment, in jhānasamāpattiyā (compound final)', ['ဈာန် ဝင်စားရာ']),
    ]),
    ('obhāso', [
        ('radiance, wisdom as brightness (nominative sg.)', ['အရောင်အဝါ']),
        ('hint, a suggestive remark, in the definition of hinting for gain (nominative sg.)',
         ['သွယ်ဝိုက် ပြောခြင်း']),
    ]),
    ('abhiññā', [
        ('by direct knowledge, higher knowing (instrumental)', ['ထူးကဲစွာ သိ၍']),
        ('direct knowing, what is to be directly known, a topic word in the summary verse (heading member)',
         ['ထူးကဲစွာ သိရမည့်']),
    ]),
    ('jappā', [
        ('hankering, yearning, in the greed list (nominative sg.)', ['တမ်းတခြင်း']),
        ("talk, in sāmantajappā 'roundabout talk' (compound final)", ['စကား ပြောခြင်း']),
    ]),
    # ---- pi-1 headword, no pi-1 value attested: the pi-2 value has another meaning ----
    ('hadaya', [
        ('heart, essence, core, in Dhammahadayavibhaṅga (heading member)', ['နှလုံးသား']),
    ]),
    ('antara', [
        ("different, the respective, in Bhūmantaradassanavāra 'the section showing the various planes' "
         "(heading member)", ['အသီးသီး']),
    ]),
    ('pīta', [
        ('drunk, what has been drunk, in asitapītakhāyitasāyita (compound member)', ['သောက်ထားသော']),
    ]),
    ('gamā', [
        ("going to, reaching, in hadayaṅgamā 'touching the heart' (compound final), here the winds "
         "going upward and downward, in uddhaṅgamā and adhogamā", ['တက်သော']),
    ]),
    ('suttaṃ', [
        ("a discourse, the sutta as a division of the teaching, in 'dhammaṃ jānāti – suttaṃ geyyaṃ' "
         "(nominative/accusative sg.)", ['သုတ်']),
    ]),
    ('sutā', [
        ("heard, what has been heard, in 'kati sutā' of the questions (nominative pl. participle)",
         ['ကြားရသော']),
    ]),
    ('khanti', [
        ('acceptance, approval of a view or of the truth, in anulomikā khanti and dhammanijjhānakkhanti '
         '(nominative sg.)', ['သည်းခံ လက်ခံမှု']),
    ]),
    ('adhimutti', [
        ("inclination, disposition of beings, in 'sattānaṃ adhimutti' (nominative sg.)", ['စိတ်ညွတ်ရာ']),
    ]),
    # ---- new in pi-2 (Marathi gives one tag), split on the Burmese evidence ----
    ('dukkhā', [
        ('painful, of feeling (feminine adjective)', ['နာကျင်သော']),
        ('suffering, said of the five aggregates of clinging (nominative pl.)', ['ဒုက္ခ']),
        ("miserable, painful in the everyday sense, in 'kāmā aniccā dukkhā' of the views (nominative pl.)",
         ['ဆင်းရဲသော']),
    ]),
    ('Jātiyā', [
        ("birth as social standing, descent, in 'jātiyā vā gottena vā' of the conceit formulas "
         "(instrumental)", ['ဇာတိ']),
        ('birth, being born, as a link of dependent origination, in jātiyā ñāṇaṃ (locative)',
         ['မွေးဖွားခြင်း']),
    ]),
    ('jātiṃ', [
        ("a birth, one life, in 'ekampi jātiṃ' of the recollection of past lives (accusative sg.)", ['ဘဝ']),
        ("birth as social standing, descent, in 'jātiṃ paṭicca' of jātimada (accusative sg.)", ['ဇာတိ']),
    ]),
    ('Jātiṃ paṭicca', [
        ("on account of birth as social standing, in jātimada 'pride of birth' (phrase)", ['ဇာတိကို စွဲ၍']),
        ("on account of being born, in jātibhaya 'fear of birth' (phrase)", ['မွေးဖွားခြင်းကို စွဲ၍']),
    ]),
    ('Ajjhatta', [
        ('internal, of the internal fetters, in ajjhattasaṃyojana (compound member)', ['အတွင်းပိုင်း']),
        ("internally, within oneself, the quoted word of the jhāna gloss, also in ajjhattabahiddhā "
         "'internal and external' (quoted word and compound member)", ['မိမိ၌']),
    ]),
    ('vatthukā', [
        ("having topics, grounds, in dasavatthukā 'with ten grounds' of the views (compound final)",
         ['အကြောင်းအရာ … ရှိသော']),
        ('having a base, a physical support, as in uppannavatthukā and nānāvatthukā (compound final)',
         ['မှီရာ ရှိသော']),
    ]),
    ('anāsavaṃ', [
        ('not an object of the taints, in the taint classification of the matrix (neuter sg.)',
         ['စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော']),
        ('free of taints, taintless, in anāsavaṃ cetovimuttiṃ (accusative sg.)', ['စိတ်အစွန်းအထင်း မရှိသော']),
    ]),
    ('āvacarā', [
        ('belonging to a sphere, compound final (nominative pl.)', ['ဘုံနှင့် ဆိုင်သော']),
        ("moving about, ranging, in etthāvacarā 'those that range here' (compound final)", ['ကျင်လည်သော']),
    ]),
    ('gacchati', [
        ("goes, takes a course, in 'agatiṃ gacchati' 'goes a wrong course' (3rd sg. present)", ['လိုက်သည်']),
        ("comes under, is reckoned, in 'saṅkhyaṃ gacchati' (3rd sg. present)", ['ရသည်']),
    ]),
    ('attha', [
        ('meaning, sense, in atthapaṭisambhidā (compound member)', ['အကျိုးအနက်']),
        ("benefit, welfare, in atthajāpikā 'that brings about benefit' (compound member)", ['အကျိုး']),
    ]),
    ('phale', [
        ('in the fruition, the fruit of the path (locative)', ['ဖိုလ်']),
        ("in the result, the effect, in hetuphale 'in cause and effect' (locative)", ['အကျိုး']),
    ]),
    ('suta', [
        ('heard, what has been heard, in sutavāditā (compound member)', ['ကြားသော']),
        ("learning, hearing the teaching, in sutamayā paññā and sutamada 'pride of learning' "
         "(compound member)", ['ကြားနာခြင်း', 'အကြားအမြင်']),
    ]),
    ('ṭhānaṃ', [
        ("place, position, in 'āsabhaṃ ṭhānaṃ' 'the place of the leader' (accusative sg.)", ['နေရာ']),
        ('standing, one of the four postures (accusative sg.)', ['ရပ်ခြင်း']),
    ]),
    # ======== full run: UNRESOLVED headwords ========
    ('rūpā', [
        ('visible forms, objects of the eye (nominative pl.)', ['အဆင်းအရောင်']),
        ('material, having material form, said of sense bases and elements (nominative pl. adjective)',
         ['ရုပ်']),
    ]),
    ('catukkaṃ', [
        ('set of four, the classification by fours, in Paccayacatukka and the matrix of fours '
         '(compound final and heading)', ['လေးမျိုးတွဲ']),
    ]),
    ('pāda', [
        ('base, basis, in iddhipāda (compound final)', ['ပါဒ်']),
        ('the foot, a part of the body, in pādatala (compound member)', ['ခြေ']),
    ]),
    ('vatthu', [
        ('basis, ground, in ñāṇavatthu and kusītavatthu (compound final)', ['အခြေခံ', 'အကြောင်း']),
        ("topics, in Khuddakavatthu 'minor topics' (heading member)", ['အကြောင်းအရာ']),
    ]),
    ('ādi', [
        ('and so on, closing a list in headings (compound final)', ['စသည်']),
        ('beginning, starting point, in the pātimokkha gloss (noun)', ['အစ']),
    ]),
    ('bahiddhā', [
        ("external, belonging to others, in 'ajjhattaṃ vā bahiddhā vā' and the internal and external "
         "triad (adverb)", ['မိမိ၏ ပြင်ပ၌']),
        ("outside, in 'ito bahiddhā' 'outside this teaching' (adverb)", ['အပြင်ဘက်']),
        ('external, of the external fetters, in bahiddhāsaṃyojana (compound member)', ['အပြင်ပိုင်း']),
    ]),
    ('āyatanāni', [
        ('sense bases, the sense fields (nominative pl.)', ['အာရုံခံ နယ်ပယ်']),
        ("grounds, bases, in titthāyatanāni 'grounds of sectarian doctrines' (compound final)", ['တည်ရာ']),
    ]),
    ('vādā', [
        ('doctrines, assertions, as in nibbānavādā (nominative pl.)', ['ဝါဒ']),
        ("speaking, as in musāvādā 'from false speech' (ablative)", ['ပြောခြင်း']),
    ]),
    ('Kāmadhātu', [
        ('the sense-sphere realm, the world of sensual pleasure (nominative sg.)', ['ကာမဘုံ']),
        ('the element of sensual thought, in the six elements of kāma, byāpāda and so on (nominative sg.)',
         ['ကာမ ဓာတ်']),
    ]),
    ('cakkhundriyaṃ', [
        ('the eye faculty, as one of the twenty-two controlling faculties and as the sense faculty to be '
         'guarded (nominative/accusative sg.)', ['မျက်စိ၏ စွမ်းရည်']),
    ]),
    ('sukha', [
        ("easy, as in sukhapaṭipadā 'easy practice' (compound member)", ['လွယ်ကူသော']),
        ('pleasure, happiness, or pleasant (compound member, as in sukhasahagata, sukhavihāra and '
         'sukhasamphassa)', ['သာယာမှု', 'သာယာစွာ', 'သာယာသော']),
        ("happiness, well-being in the everyday sense, in sukhadukkha 'pleasure and pain' of the views "
         "and the perversion 'dukkhe sukhan'ti' (compound member and quoted word)", ['ချမ်းသာသော', 'ချမ်းသာ']),
    ]),
    ('hetuko', [
        ('having roots, rooted, as in sahetuko (compound final)', ['အမြစ်']),
        ('caused by, having X as its cause, as in avijjāhetuko (compound final)', ['အကြောင်းပြုသော']),
    ]),
    ('kusalo', [
        ('wholesome (masculine sg.)', ['ကုသိုလ်']),
        ('skilled, expert, as in samādhikusalo (compound final)', ['ကျွမ်းကျင်သော']),
    ]),
    ('hetū', [
        ('roots, root conditions (nominative pl.)', ['အမြစ်']),
        ("causes, conditions, in 'hetū paccayā' of the skill-in-the-possible passage (nominative pl.), "
         "also in pubbekatahetū 'past deeds as the cause'", ['အကြောင်းရင်း', 'အကြောင်း']),
    ]),
    ('vaṇṇa', [
        ('colour, hue, as in vaṇṇanibhā (compound member)', ['အရောင်']),
        ('praise, reputation, in vaṇṇamacchariya (compound member)', ['ဂုဏ်သတင်း', 'ဂုဏ်ကျေးဇူး']),
        ("beauty, good looks, in vaṇṇamada 'pride of beauty' (compound member)", ['အဆင်းလှခြင်း']),
    ]),
    ('mutta', [
        ('pearl, in maṇisaṅkhamutta (compound member)', ['ပုလဲ']),
    ]),
    ('phala', [
        ("fruit, of plants in the smell and taste lists (compound member), also in phaladāna 'gift of fruit'",
         ['အသီး', 'သစ်သီး']),
        ('fruition of the path, in phalasamaṅgī (compound member)', ['ဖိုလ်']),
    ]),
    ('sammā', [
        ('right, correct, prefixed to path factors (compound member), also the adverb rightly '
         '(sammāpaṭipannā)', ['မှန်ကန်သော', 'မှန်ကန်စွာ']),
        ('perfectly, in sammāsambuddha (title line)', ['အပြည့်အဝ']),
        ("well, properly, thoroughly (adverb), in 'sammā pariṇāmaṃ gacchati' and 'sammā samucchinno'",
         ['ကောင်းစွာ']),
    ]),
    ('dhātuyā', [
        ('in the realm, the plane of existence, as in kāmadhātuyā (locative)', ['ဘုံ']),
        ('of or in the element, irreducible constituent, as in manodhātuyā (genitive/locative sg.)',
         ['ဓာတ်']),
    ]),
    ('dhamme', [
        ("the Buddha's teaching, in 'doubts about the Teacher, the teaching, the training' (locative), "
         "also in 'imasmiṃ dhamme' and in 'dhamme ñāṇaṃ' of the analytical knowledges",
         ['တရားတော်', 'တရား']),
        ('phenomena, states, in dhamme ārabbha (accusative pl.)', ['သဘောတရား']),
    ]),
    ('dhammesu', [
        ('among phenomena, states, also mind-objects, in dhammesu dhammānupassī (locative pl.)',
         ['သဘောတရား']),
    ]),
    ('rūpe', [
        ("matter, material form, as in nāmarūpe and 'rūpe avītarāgo' (locative sg.)", ['ရုပ်ပိုင်း', 'ရုပ်']),
        ('visible forms, the objects of the eye (accusative pl.)', ['အဆင်းအရောင်']),
    ]),
    ('kāmā', [
        ('wishing, desiring, in atthakāmā and ayogakkhemakāmā (compound final)', ['လိုလားသော']),
        ('sense pleasures (nominative pl.)', ['ကာမ']),
    ]),
    ('kappeti', [
        ("makes a living, in 'jīvikaṃ kappeti' (3rd sg. present)", ['မွေးသည်']),
        ("assumes a bodily posture, in 'iriyāpathaṃ kappeti' and 'sīhaseyyaṃ kappeti' (3rd sg. present)",
         ['ပြုလုပ်သည်', 'ပြုသည်']),
    ]),
    ('maggo', [
        ('the path, as a set of factors (nominative sg.)', ['မဂ်']),
        ("way, road, in kummaggo 'wrong way' (compound final, nominative sg.), also a road to travel, a "
         "journey, in the bases of laziness", ['လမ်း', 'ခရီး']),
    ]),
    ('uttaraṃ', [
        ('beyond the world, supramundane, in lokuttaraṃ (neuter sg. compound final)', ['ကျော်လွန်သော']),
        ("northern, in 'uttaraṃ disaṃ' (accusative sg.)", ['မြောက်']),
    ]),
    ('saṅkhāro', [
        ('a formation, a volitional formation in dependent origination (nominative sg.), the same value '
         'also naming the formation of striving, in padhānasaṅkhāro', ['ပြုပြင်ဖန်တီးမှု']),
    ]),
    ('vattati', [
        ('occurs, functions, of the mind-consciousness element depending on matter (3rd sg. present)',
         ['ဖြစ်ပေါ်သည်']),
        ("conducts oneself, behaves, as a gloss of viharati and in 'samādāya vattati' (3rd sg. present)",
         ['လည်ပတ်သည်', 'ကျင့်သည်']),
    ]),
    ('carati', [
        ('moves about, lives, as a gloss of viharati (3rd sg. present)', ['ကျင့်လည်သည်', 'ကျင်လည်သည်']),
        ("does, acts, in 'anatthaṃ carati' 'does harm' (3rd sg. present)", ['ပြုသည်']),
        ("leads a way of life, in 'brahmacariyaṃ carati' (3rd sg. present)", ['ကျင့်သည်']),
    ]),
    ('sampatti', [
        ('full attainment, in the definition of iddhi (nominative sg.)', ['ကောင်းစွာ ရောက်ခြင်း']),
        ('favourable circumstance, excellence, success in meditation, in gatisampatti and kālasampatti '
         '(compound final)', ['ပြည့်စုံမှု']),
    ]),
    ('amanasikārā', [
        ("non-attention, not attending (ablative), as in nānattasaññānaṃ amanasikārā and "
         "'na amanasikārā uppajjanti'", ['နှလုံး မသွင်းခြင်း', 'နှလုံး မသွင်းဘဲ']),
    ]),
    ('gocara', [
        ('resort, range, in ācāragocara and in gocaravisaya, the range of a sense faculty (compound member)',
         ['ကျက်စားရာ']),
    ]),
    ('pāripūriṃ', [
        ('completeness of limbs, physical perfection, a ground of intoxication (accusative sg.)',
         ['ကိုယ်အင်္ဂါ ပြည့်စုံခြင်း']),
        ("a full measure, enough food, in 'bhojanassa pāripūriṃ' (accusative sg.)", ['ပြည့်စုံမှု']),
    ]),
    ('rūpataṇhā', [
        ('craving for the fine-material sphere (nominative sg.)', ['သိမ်မွေ့သော ရုပ်ဘဝကို တပ်မက်မှု']),
    ]),
    ('vādo', [
        ("speaking, in musāvādo 'false speech' (compound final)", ['ပြောခြင်း']),
    ]),
    ('upanidhāya', [
        ('compared with, in relation to (absolutive)', ['နှိုင်းယှဉ်၍']),
    ]),
    ('Parapuggalaṃ', [
        ('another person, others (accusative sg.)', ['သူတစ်ပါး']),
    ]),
    ('aggi', [
        ('fire, the physical danger in aggibhaya, also the fires of lust, hatred and delusion '
         '(compound member)', ['မီး']),
    ]),
])

# pi-1 headwords whose MANUAL entry deliberately departs from a pi-1 tag (headword: reason).
P1_TAG_CHANGED = {}

# Several Burmese values under one sense, checked by hand (variants or synonyms of one meaning).
LUMP_OK = {
    # ---- sample ----
    'jātaṃ',   # time list «မွေးဖွားပြီးသော» (born) / sahajātaṃ «ဖြစ်ပေါ်သော» (co-arisen): one meaning, come to be
    # ---- full run: REVIEW headwords checked by hand (review-sheet.txt): grammatical variants of one
    # lemma, synonyms of one meaning, or the text's own wording of one meaning (map-harmonise-notes
    # «Text» / «Grammar» / «Rule»); a single pi-2 value that differs from pi-1's fits pi-1's sense ----
    'Paṭicca',   # «မှီ၍» (cakkhuñca paṭicca) = pi-1's 'dependent on': one meaning, as pi-1 (one sense)
    'niddeso',
    'vuccati rūpaṃ',
    'pātubhūtā',
    'abbhatthaṅgatā',
    'Iddhi',   # «ဣဒ္ဓိ» (iddhipāda) / «တန်ခိုး» (iddhividha): loan and native word for one meaning, power
    'samāpannassa',
    'ārūpāvacara',
    'Upekkhā',   # «လျစ်လျူရှုဖွယ်» (upekkhaṭṭhāniya): the same meaning in a «…ဖွယ်» construction
    'Catukka',
    'Pañcaka',
    'icchatā',
    'māno',   # «ထင်မှတ်မှု» in omāno: conceit as such
    'vibhava',
    'uccheda',
    'ucchedadiṭṭhi',
    'Sassata',
    'ānudiṭṭhi',
    'pāpa',
    'vipatti',   # sīlavipatti «ပျက်စီးခြင်း» / jhāna vipatti «ချို့ယွင်းမှု»: one meaning, failure
    'esanā',
    'adhamma',
    'nānatta',
    'kamyatā',
    'uppādā',
    'ānantarikāni',
    'vivāda',
    'vatthūni',   # virodha- / kilesa- / ñāṇavatthūni: synonyms for one meaning, grounds
    'ānusayā',
    'kilesavatthūni',
    'nevasaññīnāsaññī',
    'sattā',   # asaññasattā «(အသည)သတ်»: the loan for one meaning, beings
    'āyu',
    'gāmī',
    'uppanno',
    'asekkho',
    'sekkho',
    'hīno',   # «ယုတ်ညံ့သော» / «ယုတ်ညံ့သူ»: one lemma (quality / person), one meaning, inferior
    'na',
    'vipākadhammadhammā',
    'pihakaṃ',
    'santiṭṭhati',
    'somanassa',   # «ဝမ်းမြောက်ဖွယ်» (somanassaṭṭhāniya): one lemma, «…မှု» / «…ဖွယ်»
    'domanassa',   # «စိတ်ဆင်းရဲဖွယ်» (domanassaṭṭhāniya): one lemma, «…မှု» / «…ဖွယ်»
    'adukkhamasukhaṃ',
    'paṭivirodho',
    'uparito',
    'byāpajjanā',
    'uppajjati',   # «ဖြစ်ပေါ်လာသည်»: variant; the Marathi 'is reborn' sense has no Burmese of its own
    'samannāhāro',
    'samanantarā',
    'Soḷasa',   # numerals fuse the multiplier (rule): one meaning, sixteen
    'Dvādasa',   # numerals keep the text's classifier (rule): one meaning, twelve
    'paṭilābho',
    'cuti',
    'bhoga',
    'ahita',
    'manāpā',
    'kantā',
    'pitā',
    'mātā',
    'icchā',
    'sañcetanā',
    'piyarūpaṃ',
    'sātarūpaṃ',
    'virāga',
    'nirujjhati',
    'ātāpī',
    'ārabhati',
    'vineyya',
    'chandaṃ',   # «ဆန္ဒ» / kāmacchandaṃ «လိုလားမှု»: loan and native word for one meaning, desire
    'kāyānupassī viharati',
    'aṭṭhaṅgiko maggo',
    'paṭisaṃvedeti',
    'pītisukhaṃ',
    'anuppādāya',
    'avasesā',
    'Avasesā dhammā',
    'jīvitaṃ',   # jīvitindriya «အသက်» / jīvitamada «အသက်ရှင်ခြင်း»: one meaning, life
    'rūpajīvitindriyaṃ',
    'jarāmaraṇaṃ',
    'saṅkhārapaccayā',
    'apuññābhisaṅkhāro',
    'dāna',
    'āneñjābhisaṅkhāro',
    'bhāvanā',
    'Puññābhisaṅkhāro',
    'phusanā',
    'chambhitattaṃ',
    'abyāpajjo',
    'pahānā',
    'dhātu uppannā',
    'bahulīkaroti',
    'āsevati',
    'sampanno',
    'upeto',
    'samupeto',
    'samannāgato',
    'upapanno',
    'yāpeti',
    'yapeti',
    'Iriyati',
    'byantīkatā',
    'samitā',
    'visositā',
    'sositā',
    'appitā',
    'byappitā',
    'atthaṅgatā',
    'vūpasantā',
    'santā',
    'pajānāti',
    'uppādo',
    'vīriyaṃ ārabhati',
    'chando',   # «ဆန္ဒ» (chando kāmo, asmīti chando, chandiddhipāda) / kāmacchando «လိုလားမှု»: one meaning
    'dhuratā',
    'upasampadā',
    'sacchikiriyā',
    'bojjhaṅgā',
    'nirodha',
    'upekkhanā',
    'majjhattatā',
    'ajjhupekkhanā',
    'saññī',
    'saṃvara',
    'Kāyiko',
    'vācasiko',
    'rāja',
    'sevati',
    'vajja',
    'abhijjhādomanassā',
    'domanassā',
    'sutvā',
    'seyyaṃ',
    'bhūrī',
    'Viharatī',
    'chandarāgo',
    'paññapenti',
    'samāpattiṃ',   # «ဈာန်» / «ဈာန် ဝင်စားရာ»: one meaning, meditative attainment
    'nāsaññī',
    'ekaṃ disaṃ pharitvā',
    'vipulaṃ',
    'meraya',
    'kāmāvacare',
    'paṭibhāna',   # «ဉာဏ်ပေါ်မှု» / paṭibhānamada «လျင်မြန်သော ဉာဏ်»: one meaning, ready wit
    'Nānā',
    'mattā',
    'iriyāpathaṃ',
    'sammuti',
    'vihāra',
    'aññaṃ',
    'ābhogo',
    'āvaṭṭanā',
    'paṭilabhati',
    'vijjā',
    'ārabbha',
    'Dānaṃ',   # act «ပေးလှူခြင်း» / dānaṃ datvā «အလှူ»: one meaning, giving, gift
    'arahatta',
    'manasikārā',
    'paccavekkhaṇā',
    'jarāmaraṇa',
    'bhedā',
    'amanāpo',
    'aṭṭhamaṃ',
    'rājāno',
    'Sassato',
    'Vuṭṭhāna',
    'rūpāni',
    'sakkāra',
    'jīvita',
    'garukāra',
    'nikkhitta',
    'paccaya',   # gilānappaccaya «အထောက်အပံ့» / «ပစ္စည်း»: one meaning, requisite, support
    'pariḷāho',
    'kata',
    'sīlabbatena',
    'kula',
    'ajjhosānaṃ',
    'uppajjati diṭṭhi',
    'jimhatā',
    'vaṅkatā',
    'kuṭilatā',
    'kodha',
    'kaṭukā',
    'saṃvattanikā',
    'saṅgo',
    'piyassa',
    'anatthaṃ',
    'manāpassa',
    'nimmāna',   # nimmānaratī loan «နိမ္မာန» / «ဖန်ဆင်းခြင်း»: one meaning, creation
    'kusalahetu',
    'samphasso',
    'upapatti',
    'appamāṇa',
    'kappasahassāni',   # numerals fuse the count (rule): one meaning, thousands of aeons
    'Vīsati',   # «နှစ်သောင်း» (vīsati kappasahassāni, fused numeral): one meaning, twenty
    'gatā',
}


def parse_line(line):
    """'hw: {t: a / b; t2: c}' -> (hw, [(t, [a, b]), (t2, [c])])."""
    i = line.find(': {')
    if i < 0 or not line.endswith('}'):
        return None, None
    hw, body = line[:i], line[i + 3:-1]
    senses = []
    for s in body.split('; '):
        if ': ' not in s:
            return hw, None
        t, v = s.rsplit(': ', 1)
        senses.append((t.strip(), [x.strip() for x in v.split(' / ')]))
    return hw, senses


def read_senses(path, keep_values):
    d = {}
    for line in path.read_text(encoding='utf-8-sig').splitlines():
        line = line.strip()
        if not line:
            continue
        hw, s = parse_line(line)
        if hw is None or s is None:
            sys.exit(f'cannot parse senses line in {path.name}: {line[:80]!r}')
        d[hw] = s if keep_values else [t for t, _ in s]   # Marathi: values dropped here
    return d


def lookup(d, hw):
    if hw in d:
        return hw
    m = [k for k in d if k.lower() == hw.lower()]
    return m[0] if len(m) == 1 else None


def read_agg(path):
    rows = OrderedDict()
    for n, line in enumerate(open(path, encoding='utf-8-sig'), 1):
        line = line.rstrip('\n').rstrip('\r')
        if not line.strip():
            continue
        cols = line.split('\t')
        if len(cols) != 4:
            sys.exit(f'agg line {n}: expected 4 columns')
        vals = OrderedDict()
        for item in [x.strip() for x in cols[2].split(' | ') if x.strip()]:
            m = VAL_RE.match(item)
            if not m:
                sys.exit(f'agg line {n}: cannot parse {item!r}')
            vals[m.group(1)] = vals.get(m.group(1), 0) + int(m.group(2))
        rows[cols[0]] = vals
    return rows


def main(aggp, outp):
    rows = read_agg(aggp)
    my1 = read_senses(MY1_SENSES, True)
    mr = read_senses(MR_SENSES, False)
    out, unresolved, review, errs = [], [], [], []
    stats = {'manual': 0, 'p1_same': 0, 'p1_subset': 0, 'p1_lump': 0, 'mr': 0, 'p1_case': 0}
    for hw, vals in rows.items():
        if not vals:
            continue
        k1 = lookup(my1, hw)
        p1 = my1.get(k1) if k1 else None
        if k1 and k1 != hw:
            stats['p1_case'] += 1
        p1_of = {v: t for t, vs in (p1 or []) for v in vs}
        if hw in MANUAL:
            stats['manual'] += 1
            senses = MANUAL[hw]
            given = [v for _, vs in senses for v in vs]
            for v in given:
                if v not in vals:
                    errs.append(f'{hw}: MANUAL value not attested: {v!r}')
            for v in vals:
                if v not in given:
                    errs.append(f'{hw}: attested value missing from MANUAL: {v!r}')
            if len(given) != len(set(given)):
                errs.append(f'{hw}: a value is under two senses')
            if p1 and hw not in P1_TAG_CHANGED:
                for t, vs in senses:
                    for v in vs:
                        if v in p1_of and not t.startswith(p1_of[v]):
                            errs.append(f'{hw}: {v!r} leaves its pi-1 sense {p1_of[v]!r}')
        elif p1:
            new = [v for v in vals if v not in p1_of]
            if not new:
                senses = [(t, [v for v in vs if v in vals]) for t, vs in p1]
                senses = [(t, vs) for t, vs in senses if vs]
                stats['p1_same' if len(senses) == len(p1) and len(vals) == len(p1_of) else 'p1_subset'] += 1
            elif len(p1) == 1 and hw in LUMP_OK:
                senses = [(p1[0][0], list(vals))]
                stats['p1_lump'] += 1
            elif len(p1) == 1:
                senses = [(p1[0][0], list(vals))]
                review.append((hw, 'pi-1 one sense, new values ' + ' / '.join(new), list(vals)))
                stats['p1_lump'] += 1
            else:
                unresolved.append((hw, 'pi-1 senses ' + str([t for t, _ in p1]), list(vals)))
                continue
        else:
            k2 = lookup(mr, hw)
            tags = mr.get(k2) if k2 else None
            if tags and len(tags) == 1:
                senses = [(tags[0], list(vals))]
                stats['mr'] += 1
                if len(vals) > 1 and hw not in LUMP_OK:
                    review.append((hw, 'one Marathi tag', list(vals)))
            else:
                unresolved.append((hw, f'Marathi tags={tags}', list(vals)))
                continue
        for tag, _ in senses:
            if NONLATIN.search(tag) or '; ' in tag or not tag:
                errs.append(f'{hw}: bad tag {tag!r}')
        out.append(hw + ': {' + '; '.join(t + ': ' + ' / '.join(vs) for t, vs in senses) + '}')
    unused = [h for h in MANUAL if h not in rows]
    if unused:
        print(f'note: MANUAL entries not in this input (fine for a part run): {unused}')
    with open(outp, 'w', encoding='utf-8', newline='\n') as f:
        f.write(f'# Pāli→Burmese pi-2 sense decisions, written by gen_decisions_my.py from {pathlib.Path(aggp).name}\n')
        f.write('# English tags: pi-1 Burmese senses (binding), else Marathi pi-2 senses (tags only), or MANUAL;\n')
        f.write('# values: pi-2 Burmese keyword map only.\n')
        f.write('\n'.join(out) + '\n')
    print(f'wrote {len(out)} decision lines -> {outp}')
    print(f'  MANUAL {stats["manual"]} | pi-1 senses unchanged {stats["p1_same"]} | pi-1 senses, subset '
          f'attested {stats["p1_subset"]} | pi-1 one sense + new values {stats["p1_lump"]} | Marathi tag '
          f'{stats["mr"]} | pi-1 matched by case only {stats["p1_case"]}')
    if review:
        print(f'REVIEW ({len(review)}): several Burmese values lumped into one sense; check, then add to '
              f'LUMP_OK or MANUAL:')
        for hw, why, vs in review:
            print(f'  {hw} [{why}]: {" / ".join(vs)}')
    if unresolved:
        print(f'UNRESOLVED ({len(unresolved)}): write MANUAL:')
        for hw, why, vs in unresolved:
            print(f'  {hw}\t{why}\tburmese={vs}')
    if errs:
        print(f'ERRORS ({len(errs)}):')
        for e in errs:
            print('  ' + e)
    return 1 if (unresolved or errs) else 0


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sys.exit(main(*sys.argv[1:]))
