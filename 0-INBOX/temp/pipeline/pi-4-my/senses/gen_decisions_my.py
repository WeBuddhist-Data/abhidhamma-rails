"""Write the Pāli→Burmese pi-4 decisions file for senses_my.py (brief: pi-4-my/burmese-senses-brief.md).
Adapted from pi-3-my/senses/gen_decisions_my.py (same MANUAL / LUMP_OK / TAG_CHANGED / NEW_SENSE mechanism); the
binding chain is now pi-3, then pi-2, then pi-1.

usage: python -I -X utf8 gen_decisions_my.py <agg.tsv> <decisions.txt>

For every headword of agg.tsv that has Burmese values (NDE-only headwords are skipped):
  1. a hand decision in MANUAL below wins;
  2. otherwise the approved Burmese senses are BINDING, pi-3 first, then pi-2, then pi-1 (each looked up exact, else
     the one case-insensitive match: the aggregation keeps the first spelling seen). The reference is the line of the
     first of pi-3 / pi-2 / pi-1 that has the headword. Every pi-4 value that the reference lists goes under the
     reference's sense with its English tag, in the reference's sense order (a sense with no pi-4 value is left out).
     A pi-4 value the reference does not list:
       - a later binding file (pi-2 / pi-1 after pi-3, pi-1 after pi-2) lists it: that file's sense (tag) is added
         after the reference's, or the value joins the reference sense with the same tag (REVIEW);
       - otherwise, the reference has one sense: the value joins it (REVIEW unless the headword is in LUMP_OK);
       - otherwise (the reference has several senses): UNRESOLVED (write MANUAL);
  3. otherwise, if the Marathi pi-4 senses file gives the headword ONE English tag, the line is that tag + every
     attested Burmese value (one sense; several values -> REVIEW unless LUMP_OK);
  4. otherwise (several Marathi senses, or no Marathi line) the headword is UNRESOLVED: write MANUAL.
Only the ENGLISH tags are read from the Marathi file; its Marathi values are dropped on parsing and never written.
A MANUAL entry for a pi-3 / pi-2 / pi-1 headword must keep the binding split: every value the binding senses list
(pi-3's sense for it, else pi-2's, else pi-1's) sits under a sense whose tag starts with that binding tag (an appended
«, …» is allowed) unless the headword is in TAG_CHANGED (logged reason); and a MANUAL sense that holds only values the
binding senses do not list, with a tag that starts with none of the binding tags, is a NEW sense and the headword must
be in NEW_SENSE (logged reason).
The script fails (exit 1) while anything is UNRESOLVED, a MANUAL value is not attested, a MANUAL entry omits an
attested value, a MANUAL entry breaks a binding sense, or a new sense is not logged in NEW_SENSE.
"""
import pathlib
import re
import sys
from collections import OrderedDict

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
BIND_FILES = OrderedDict([
    ('p3', ROOT / 'AI_translation/burmese/pi-3-pali-word-burmese-senses-plain.md'),
    ('p2', ROOT / 'AI_translation/burmese/pi-2-pali-word-burmese-senses-plain.md'),
    ('p1', ROOT / 'AI_translation/burmese/pi-1-pali-word-burmese-senses-plain.md'),
])
BOOK = {'p3': 'pi-3', 'p2': 'pi-2', 'p1': 'pi-1'}
MR_SENSES = ROOT / 'AI_translation/marathi/pi-4-pali-word-marathi-senses-plain.md'
VAL_RE = re.compile(r'^(.*)=(\d+)\[[^\]]*\]$')
NONLATIN = re.compile(r'[ऀ-ॿက-႟]')

# Hand decisions: headword -> [(English tag, [Burmese values])]. Values must be attested.
# Binding senses first (pi-3, else pi-2, else pi-1 order and tag), then the senses new in pi-4.
MANUAL = OrderedDict([
    # ======== sample (agg-sample.tsv, the first 80 headwords) ========
    ('puggalapaññatti', [
        # new in pi-4; the Marathi tag 'title of the fourth Abhidhamma book' does not cover the chapter headings:
        # the title «…များကို သတ်မှတ်ဖော်ပြခြင်း» (^4-0, ^4-209) and «ပုဂ္ဂိုလ် သတ်မှတ်ချက်» of the headings: one meaning
        ('designation of persons, the title of the fourth Abhidhamma book and the member of the chapter headings '
         'such as Ekakapuggalapaññatti', ['ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း', 'ပုဂ္ဂိုလ် သတ်မှတ်ချက်']),
    ]),
    ('dhammo', [
        # one Burmese value «သဘော ရှိသော» in kuppa- / akuppa- / parihāna-dhammo and pāpa- / kalyāṇa-dhammo
        # (mapper P2): the Marathi split has no Burmese evidence, one sense
        ('having the nature of, of such a character (compound final), as in kuppadhammo and akuppadhammo and in '
         'pāpadhammo and kalyāṇadhammo', ['သဘော ရှိသော']),
    ]),
    ('rūpa', [
        # pi-3 senses (tags); «အဆင်း» (^4-176 sarūpavaccha) = the looks, colour: the visible-form sense
        ('the fine-material sphere, as in rūpāvacara and rūpūpapatti (compound member), rūpa in rūpasaññā of the '
         'immaterial-jhāna formula being given under matter', ['သိမ်မွေ့သော ရုပ်']),
        ('visible form, the object of the eye (compound member, as in rūpārammaṇa), the same meaning as outward '
         "looks in rūpappamāṇo and rūpappasanno and in sarūpavaccha 'with a calf of like colour'",
         ['အဆင်းအရောင်', 'အဆင်း']),
        ('matter, material form (heading and compound member, as in Rūpakaṇḍa and rūpakkhandha), also the '
         'material side of nāmarūpa (in nāmarūpapaccayā)', ['ရုပ်']),
    ]),
    ('puthu', [
        # new in pi-4; Marathi tags; two meanings (mapper: puthujjana / puthupañña)
        ('many, common, in puthujjana (compound member)', ['ပုထုဇဉ်']),
        ('broad, wide, in puthupañño (compound member)', ['ကျယ်ပြန့်သော']),
    ]),
    ('paṭipanno', [
        # new in pi-4; «ကျင့်ကြံသော» / «ကျင့်သော» (^4-189) are one verb, the text's own wording (map-harmonise item 5)
        ("practising, on the way, toward a fruit and in attahitāya paṭipanno 'practising for his own welfare' "
         '(participle)', ['ကျင့်ကြံသော', 'ကျင့်သော']),
    ]),
    # ======== full run (agg-part1.tsv): UNRESOLVED headwords ========
    ('phala', [
        # pi-2 senses (tags) + the result of effort or merit (^4-167, ^4-M-10 uṭṭhāna- / puññaphalūpajīvī)
        ("fruit, of plants in the smell and taste lists (compound member), also in phaladāna 'gift of fruit'",
         ['အသီး']),
        ('fruition of the path, in phalasamaṅgī (compound member)', ['ဖိုလ်']),
        ('result, the fruit of effort or of merit, in uṭṭhānaphalūpajīvī and puññaphalūpajīvī (compound member)',
         ['အကျိုး']),
    ]),
    ('sama', [
        ('simultaneous, at one and the same time, in samasīsī (compound member)', ['တပြိုင်နက်']),
        ('evenly, in due balance, in asamapekkhaṇā (compound member)', ['ညီညီညွတ်ညွတ်']),
    ]),
    ('vibha', [
        # no Marathi line: «vibha.» (^4-46, ^4-49) is the abbreviated reference to the second Abhidhamma book
        ('the Vibhaṅga, the second Abhidhamma book, abbreviated in a cross-reference note (vibha.)',
         ['ခွဲခြမ်းစိတ်ဖြာခြင်း']),
    ]),
    ('kammaṃ', [
        ("action-noun final '-making, -doing' in synonym lists, as in niṭṭhuriyakammaṃ and anāvikammaṃ",
         ['ပြုခြင်း']),
        ('morally significant deeds, kamma (accusative)', ['ကံ']),
    ]),
    ('ṭhānaṃ', [
        # pi-2 place / posture not attested; vivādaṭṭhānaṃ (^4-48, ^4-68) = ground of dispute
        ("ground, occasion, in vivādaṭṭhānaṃ 'ground for dispute' (compound final, nominative sg.)", ['အကြောင်း']),
    ]),
    ('āhāro', [
        ("food, what is eaten, in evamāhāro 'having such food' of the past-lives formula (compound final)",
         ['အစာ']),
        ("taking on, bringing along, in paḷāsāhāro 'the taking up of rivalry' (compound final)", ['ဆောင်ခြင်း']),
    ]),
    ('vaṇṇa', [
        # pi-2 senses (tags); «ချီးမွမ်း» (^4-M-10 avaṇṇaṃ vaṇṇaṃ) = praise; «အသားအရေ» (vaṇṇapokkharatā) = complexion
        ('praise, reputation, in vaṇṇamacchariya (compound member), also praise spoken, in avaṇṇaṃ vaṇṇaṃ',
         ['ဂုဏ်သတင်း', 'ချီးမွမ်း']),
        ("beauty, good looks, in vaṇṇamada 'pride of beauty' (compound member), here the complexion, in "
         'vaṇṇapokkharatā', ['အသားအရေ']),
    ]),
    ('hetu', [
        # pi-2 cause sense for attahetu / parahetu «အကြောင်း» (^4-98, ^4-99); purpose «အလို့ငှာ» (^4-52, ^4-72)
        ('cause, condition, in Hetucatukka of dependent origination and Hetuvāra of the analytical knowledges '
         "(heading member), also 'on account of', in attahetu and parahetu (compound final)", ['အကြောင်း']),
        ("for the purpose of, in paṭicchādanahetu 'in order to conceal' (compound final)", ['အလို့ငှာ']),
    ]),
    ('brahma', [
        # pi-1 'divine, sublime'; the one pi-4 value «မြင့်မြတ်သော» (brahmacariya, brahmacārī, brahmabhūta)
        ('divine, sublime, in brahmavihāra (compound member), also the sublime life, in brahmacariya and '
         'brahmacārī, and in brahmabhūta', ['မြင့်မြတ်သော']),
    ]),
    ('obhāso', [
        ('radiance, wisdom as brightness (nominative sg.)', ['အရောင်အဝါ']),
        ('seeming, outward look, in gambhīrobhāso and uttānobhāso (compound final)', ['ဟန် ထင်ရသော']),
    ]),
    ('cārī', [
        # one Burmese value in micchācārī and (a)brahmacārī: one sense
        ('one who practises, follows a conduct (agent noun), as in kāmesu micchācārī and abrahmacārī', ['ကျင့်သော']),
    ]),
    ('byāpajjati', [
        ('becomes malevolent, turns hostile (3rd sg. present)', ['ဖောက်ပြန်သည်']),
        ('is wounded, struck down in battle (3rd sg. present)', ['ဒဏ်ရာ ရသည်']),
    ]),
    ('assa', [
        ('his, of him (genitive pronoun)', ['ထိုသူ']),
    ]),
    ('diṭṭha', [
        # no Marathi line: diṭṭhānugatiṃ āpajjanti (^4-116, ^4-117, ^4-124, ^4-126)
        ("what is seen, an example, in diṭṭhānugatiṃ āpajjati 'follows the example' (compound member)", ['အမြင်']),
    ]),
    ('dhamme', [
        # pi-2 teaching / phenomena not attested; diṭṭheva dhamme (^4-131, ^4-202, ^4-209), kept sense difference
        ("this present life, in diṭṭhe ceva dhamme and diṭṭheva dhamme 'here and now' (locative)", ['ဘဝ']),
    ]),
    ('kattā', [
        ('one who acts, a doer rather than a talker (agent noun)', ['ပြုလုပ်သူ']),
        ('one who digs, maker of a burrow, with gādhaṃ (agent noun)', ['တူးသူ']),
    ]),
    ('patta', [
        ('the alms bowl, in pattacīvara and pattamaṇḍanā (compound member)', ['သပိတ်']),
        ("wings, the feathers of a bird, in pattabhāro 'with its wings as its only burden' (compound member)",
         ['အတောင်']),
    ]),
    ('pasādaṃ janeti', [
        # one Burmese value for the confidence of ^4-164 / ^4-165 and ^4-171 / ^4-172: one sense
        ('gives rise to confidence, becomes pleased, in a path (^4-164, ^4-165) and taking a measure (^4-171, '
         '^4-172) (phrase)', ['ကြည်ညိုမှုကို ဖြစ်စေသည်']),
    ]),
    ('go', [
        ('cow, bovine animal (compound member), as in gomaya and the cattle of the ascetic practices', ['နွား']),
    ]),
    ('mukhā', [
        ('the opening, the rim of a vessel, in kumbhimukhā (ablative)', ['နှုတ်ခမ်း']),
        ('face, in assumukhā with tears on the face (compound final)', ['မျက်ရည် စီးသော']),
    ]),
    ('eḷaka', [
        ('doorsill, threshold, in eḷakamantaraṃ (compound member)', ['တံခါးခုံ']),
        ('sheep, small livestock, in ajeḷaka (compound member)', ['သိုး']),
    ]),
    ('attha', [
        ('meaning, sense, in atthapaṭisambhidā (compound member), here in atthamaññāya', ['အနက်']),
        ("benefit, welfare, in atthajāpikā 'that brings about benefit' (compound member), here in atthavādī and "
         'atthasaṃhita', ['အကျိုး']),
    ]),
    ('bhūta', [
        # the other occurrences are (no direct equivalent), dropped (skill step 4)
        ('vegetation, plant life, in bhūtagāma (compound member)', ['အပင်']),
    ]),
    # ======== full run: REVIEW headwords with a genuinely new pi-4 meaning, or a tag fitted to pi-4 ========
    ('hoti', [
        ('is, comes to be, becomes (3rd sg. present)', ['ဖြစ်သည်']),
    ]),
    ('ṭhita', [
        ("holding in place, making last, in ṭhitakappī 'one who could make the aeon last' (compound member)",
         ['တည်နေစေသော']),
        ('steady, firm, in ṭhitatto (compound member)', ['တည်ငြိမ်သော']),
    ]),
    ('dhammesu', [
        ("teachings, truths, in pubbe ananussutesu dhammesu 'in things not heard before' (locative pl.)", ['တရား']),
    ]),
    ('bhāga', [
        ('side, part, in ubhatobhāgavimutto (compound member)', ['နှစ်ဖက်စလုံး']),
    ]),
    ('dhammā', [
        ("teachings, in tathāgatappaveditā dhammā 'the teachings made known by the Tathāgata' (nominative pl.)",
         ['တရား']),
    ]),
    ('ṭhito', [
        ("established in, abiding in, in phale ṭhito 'established in the fruit' (nominative sg. participle)",
         ['တည်သော', 'တည်နေသော']),
    ]),
    ('dhamma', [
        ('phenomena, states (as in the book title Dhammasaṅgaṇī), the same value also naming mind-objects, what '
         'the mind as sixth sense knows (as in dhammāyatana)', ['သဘောတရား']),
        ("the Buddha's teaching, in dhammamacchariya and dhammapaṭisanthāra", ['တရား']),
        ('moral nature, character, in pāpadhamma and kalyāṇadhamma (compound member)', ['သဘော']),
    ]),
    ('dukkhassa', [
        ('of suffering, the whole of what is unsatisfactory, in dukkhassantakaro and the noble truth '
         '(genitive sg.)', ['ဒုက္ခ']),
        ('of pain, of bodily pain (genitive sg.)', ['နာကျင်မှု']),
    ]),
    ('eka', [
        # kept sense difference (map-harmonise-notes): the numeral counted with the seed classifier
        ('one, as in the one-item section label Ekamūlaka, here one seed, one more birth, in ekabījī '
         '(compound member)', ['တစ်စေ့']),
    ]),
    ('antarā', [
        ("midway, before the middle of the life span, in antarāparinibbāyī (compound member)",
         ['သက်တမ်း၏ အလယ်သို့ မရောက်မီ']),
    ]),
    ('saṅkhāra', [
        ('mental formations, volitional activities (compound member, in saṅkhārakkhandha), the same value also '
         'naming the formation of striving, in padhānasaṅkhāra of the bases of power', ['ပြုပြင်ဖန်တီးမှု']),
        ('prompting, exertion, in sasaṅkhāraparinibbāyī and asaṅkhāraparinibbāyī (compound member)',
         ['တိုက်တွန်းမှု']),
    ]),
    ('kula', [
        ('families, supporting households, in kulamacchariya (compound member)', ['ကိုးကွယ်သော အိမ်']),
        ('the royal household, in rājakulamajjhagato (compound member)', ['မင်းမျိုးမင်းနွယ်']),
    ]),
    ('saha', [
        ("in accordance with, in sahadhammika 'reasonable, in accordance with the Dhamma' (compound member)",
         ['လျော်စွာ']),
    ]),
    ('āyatanaṃ', [
        ("abode, fold, in titthāyatanaṃ 'the sectarian fold' (compound final)", ['တည်ရာ']),
    ]),
    ('gataṃ', [
        # ^4-198 has araññagataṃ etc. only, mapped «မှား» there (probably a map slip; reported)
        ("resort to a view, in diṭṭhigataṃ 'a wrong view' (compound final)", ['မှား']),
        ('gone to, staying in, in araññagataṃ and suññāgāragataṃ (compound final)', ['ရောက်သော']),
    ]),
    ('pada', [
        ('rules, items, in sikkhāpada (compound final), here a grammatical item, in padasiddhi', ['ပုဒ်']),
        ("word, the letter of a text, in padaparamo 'one for whom the words are the most' (compound member)",
         ['စကားလုံး']),
    ]),
    ('kata', [
        ('what has been done for one, a kindness, in kataññū and katavedī (compound member)', ['ကျေးဇူး']),
    ]),
    ('bhajati', [
        ('resorts to a lodging, betakes oneself (3rd sg. present), the same value also naming associating with '
         'a person (^4-88, ^4-89)', ['ဆည်းကပ်သည်']),
    ]),
    ('vuṭṭhāti', [
        # kept sense difference (harmonise B5): attainment «ထမြောက်» vs illness «ပျောက်ကင်း»
        ('recovers, rises from an illness (3rd sg. present)', ['ပျောက်ကင်းသည်']),
    ]),
    ('sampajāna', [
        ('knowingly, deliberately, in sampajānamusā bhāsitā, the same value also in sampajānakārī '
         '(compound member)', ['သိလျက်']),
    ]),
    ('aṭṭhakathā', [
        ('the commentary chapter (heading), here the commentary cited as a source in variant notes',
         ['အဋ္ဌကထာ']),
    ]),
    ('manasi', [
        # word «နှလုံးသွင်းခြင်း» / fragment «နှလုံး» of manasi karoti (map-harmonise, word vs fragment)
        ("mental advertence, in the summary verse (manasi for manasikāra), also in manasi karoti 'attends to'",
         ['နှလုံး', 'နှလုံးသွင်းခြင်း']),
    ]),
    ('dukkhāya', [
        ("for the suffering, the misery of, in dīgharattaṃ ahitāya dukkhāya (dative sg.)", ['ဆင်းရဲခြင်း']),
    ]),
    ('sukhāya', [
        ("for the happiness, the well-being of, in dīgharattaṃ hitāya sukhāya (dative sg.)", ['ချမ်းသာခြင်း']),
    ]),
    ('gandha', [
        ('smell, odour as object (compound member)', ['အနံ့']),
        ('perfume, scents used as cosmetics, in mālāgandhavilepana (compound member)', ['နံ့သာ']),
    ]),
    ('attānaṃ', [
        ("a self, the soul as posited by a teacher's view, in attānaṃ saccato thetato paññapeti (accusative sg.)",
         ['အတ္တ']),
    ]),
    ('pāṇa', [
        # kept sense difference (map-harmonise-notes): pāṇātipāta «သူ့အသက်» vs living beings «သတ္တဝါ»
        ('living being, creature (compound member)', ['သတ္တဝါ']),
        ("life, the life of another, in pāṇātipātī 'one who takes life' (compound member)", ['သူ့အသက်']),
    ]),
    ('jātiyā', [
        ("existence, life-time, in tāya jātiyā 'in that same life' (instrumental)", ['ဘဝ']),
    ]),
    ('mutta', [
        ('free-flowing, quick, of speech, in muttapaṭibhāno (compound member)', ['လျင်မြန်သော']),
        ("discarding, free from, in muttācāro 'one who has discarded conventions' (compound member)",
         ['စွန့်လွှတ်သော']),
    ]),
    ('kusalā', [
        ('skilled, expert (nominative pl.)', ['ကျွမ်းကျင်သော']),
    ]),
    ('bhūtaṃ', [
        ('what is true, as it really is, in yathābhūtaṃ (adverbial)', ['အမှန်အတိုင်း']),
    ]),
    ('dassana', [
        ('seeing, vision, in vimuttiñāṇadassana (compound member)', ['သိမြင်သော']),
    ]),
    ('daṇḍa', [
        ('punishment, in daṇḍabhaya (compound member), here in daṇḍatajjita', ['ဒဏ်']),
        ('a stick, a rod, in daṇḍamantaraṃ (compound member)', ['တုတ်']),
    ]),
    ('atta', [
        ('oneself, one\'s own (reflexive compound member), as in attantapo and attahita', ['မိမိ']),
    ]),
    ('bhūmiyā', [
        ('the ground, the surface of the earth (locative)', ['မြေ']),
    ]),
    ('majjhima', [
        ('the Majjhima Nikāya, the middle-length collection, in a cross-reference note (title member)',
         ['မဇ္ဈိမ']),
    ]),
    ('sutte', [
        ('in the discourse, a sutta cited in a note (locative)', ['သုတ်']),
        ('in sleeping, in the clear-comprehension list (locative)', ['အိပ်ရာ']),
    ]),
    ('pharusaṃ', [
        ('harsh, rough speech, in pharusaṃ vācaṃ (accusative sg.)', ['ကြမ်းတမ်းသော စကား']),
    ]),
    ('nandī', [
        ('delight, enjoyment as craving (nominative sg. and compound member), also delighting in concord, in '
         'samagganandī (compound final)', ['နှစ်သက်သော']),
    ]),
    ('yogā', [
        ('crooked means, devious practices, in sāciyogā and the errand-running list (compound final, ablative)',
         ['နည်းလမ်း']),
    ]),
    ('khetta', [
        ('field, cultivated land, in khettavatthu (compound member)', ['လယ်']),
    ]),
    ('samādāya', [
        ('taking along, carrying with one, of the bowl and robe (absolutive)', ['ယူဆောင်၍']),
    ]),
    ('indriya', [
        # kept sense difference (map-harmonise-notes): indriyasaṃvara «အာရုံခံ အင်္ဂါ» vs indriyapaññatti «စွမ်းရည်»
        ("sense faculty, in indriyabaddha 'bound to the faculties' (compound member), here the faculties as a "
         'category, in indriyapaññatti', ['စွမ်းရည်']),
        ('the sense organs to be guarded, in indriyasaṃvara and indriyesu guttadvāro (compound member)',
         ['အာရုံခံ အင်္ဂါ']),
    ]),
    ('ṭhite', [
        ('in standing, in the clear-comprehension list (locative)', ['ရပ်ရာ']),
        ('steady, stable, of the concentrated mind, in ṭhite āneñjappatte (locative)', ['တည်တံ့သော']),
    ]),
    ('gate', [
        ('in walking, in the clear-comprehension list (locative)', ['သွားရာ']),
        ('gone to a destiny, in sugate duggate (locative or accusative pl.)', ['လားရာ ရှိသော']),
    ]),
    ('upapanno', [
        ('possessed of, provided with (nominative sg. participle)', ['ပြည့်စုံသော']),
        ('reborn, reappeared in a new existence (nominative sg. participle)', ['ဖြစ်ပေါ်လာသော']),
    ]),
    ('dukkhena', [
        ('bodily pain, in the grief series (instrumental sg.), also in sahāpi dukkhena sahāpi domanassena',
         ['နာကျင်မှု']),
    ]),
    ('sota', [
        ('the ear, the hearing organ (stem and compound member)', ['နား']),
        ('the current, the stream, in anusotagāmī and paṭisotagāmī (compound member)', ['ရေစီး']),
    ]),
    ('suto', [
        ('learning, what has been heard and studied, in appassuto and bahussuto (compound final)',
         ['အကြားအမြင်']),
    ]),
    ('ārabhati', [
        ('transgresses, commits an offence (3rd sg. present)', ['မှားယွင်းစွာ ပြုမူသည်']),
    ]),
    ('yathā', [
        ("in accordance with, in yathādiṭṭhissa 'of one whose effort accords with his view' (compound member), "
         "also 'as it comes', in yathāsanthatika", ['အတိုင်း']),
    ]),
    ('ṭhānesu', [
        ("places, in the editorial note 'evaṃ tīsu ṭhānesupi' 'likewise in the three places' (locative pl.)",
         ['နေရာ']),
    ]),
    ('puriso', [
        ("person, the member of sappuriso and asappuriso 'good person' (compound final)", ['သူတော်ကောင်း']),
    ]),
])

# Binding headwords whose MANUAL entry deliberately departs from a binding tag (headword: reason).
TAG_CHANGED = {}

# Binding headwords whose MANUAL entry adds a sense with values the binding senses do not list (headword: reason).
NEW_SENSE = {
    # ---- UNRESOLVED headwords ----
    'phala': "pi-2 fruit «အသီး» / fruition «ဖိုလ်»; pi-4 «အကျိုး» is the result of effort or merit "
             "(^4-167, ^4-M-10 uṭṭhānaphalūpajīvī, puññaphalūpajīvī; mapper: phala sense by context)",
    'ṭhānaṃ': "pi-2 place «နေရာ» / posture «ရပ်ခြင်း» (not attested in pi-4); pi-4 «အကြောင်း» is the ground of "
              "vivādaṭṭhānaṃ (^4-48, ^4-68)",
    'āhāro': "pi-2 food «အစာ» kept (^4-183); pi-4 «ဆောင်ခြင်း» is the taking up of rivalry, paḷāsāhāro "
             "(^4-48, ^4-68), not nutriment",
    'hetu': "pi-2 roots / cause; pi-4 «အလို့ငှာ» is the final sense 'for the purpose of', paṭicchādanahetu "
            "(^4-52, ^4-72), against the causal attahetu «အကြောင်း» (^4-98, ^4-99)",
    'obhāso': "pi-2 radiance «အရောင်အဝါ» kept (^4-80); pi-4 «ဟန် ထင်ရသော» is the outward look, gambhīrobhāso / "
              "uttānobhāso of the water-pot simile (^4-161)",
    'dhamme': "pi-2 teaching / phenomena (not attested in pi-4); «ဘဝ» is this present life, diṭṭheva dhamme "
              "(^4-131, ^4-202, ^4-209; kept sense difference, brief)",
    'patta': "pi-2 bowl «သပိတ်» kept; pi-4 «အတောင်» is the bird's wings, pattabhāro (^4-180)",
    # ---- REVIEW headwords ----
    'hoti': "pi-2 / pi-1 «ရှိသည်» is 'exists' in the speculative views (not attested in pi-4); pi-4 «ဖြစ်သည်» is "
            "the copula 'is, comes to be' (^4-16, ^4-91 …)",
    'ṭhita': "pi-1 «ရပ်တန့်ခြင်း» is stopping, aṭṭhitakiriyatā (not attested in pi-4); pi-4 ṭhitakappī "
             "«တည်နေစေသော» (^4-17) and ṭhitatto «တည်ငြိမ်သော» (^4-188) are two further meanings",
    'dhammesu': "pi-2 «သဘောတရား» phenomena (not attested in pi-4); pi-4 «တရား» is the teachings, pubbe "
                "ananussutesu dhammesu (^4-22 …)",
    'bhāga': "pi-3 «သဘော» is kind, sabhāga (not attested in pi-4); pi-4 «နှစ်ဖက်စလုံး» is side, ubhatobhāga (^4-24 …)",
    'dhammā': "pi-2 / pi-1 «သဘောတရား» phenomena (not attested in pi-4); pi-4 «တရား» is the teachings, "
              "tathāgatappaveditā dhammā (^4-27, ^4-28, ^4-96, ^4-97)",
    'ṭhito': "pi-2 «တည်ငြိမ်သော» is the steady body (not attested in pi-4); pi-4 «တည်သော» / «တည်နေသော» is "
             "'established in', phale ṭhito (^4-29 …)",
    'dhamma': "pi-3 phenomena and pi-2 teaching kept; pi-4 «သဘော» is moral nature, pāpadhamma / kalyāṇadhamma "
              "(^4-141, ^4-143; mapper: dhamma sense by context)",
    'dukkhassa': "pi-2 «နာကျင်မှု» bodily pain kept (^4-183); pi-4 «ဒုက္ခ» is suffering, dukkhassantakaro and the "
                 "truth (^4-31 …), the pi-3 dukkha suffering sense",
    'antarā': "pi-3 «ကြားညှပ်» is the intermediate sections of the Mātikā (not attested in pi-4); pi-4 is midway "
              "in the life span, antarāparinibbāyī (^4-36)",
    'saṅkhāra': "pi-3 formations kept (^4-M-2); pi-4 «တိုက်တွန်းမှု» is prompting, sa- / asaṅkhāraparinibbāyī "
                "(^4-38, ^4-39; mapper: asaṅkhāra), as pi-1 saṅkhārena",
    'kula': "pi-2 supporting households kept; pi-4 «မင်းမျိုးမင်းနွယ်» is the royal household, rājakula (^4-98, ^4-99)",
    'saha': "pi-2 «အတူ» is 'together with' (not attested in pi-4); pi-4 «လျော်စွာ» is 'in accordance with', "
            "sahadhammika (^4-55, ^4-75)",
    'āyatanaṃ': "pi-3 sense base (not attested in pi-4); pi-4 «တည်ရာ» is the sectarian fold, titthāyatanaṃ (^4-62)",
    'gataṃ': "pi-2 / pi-1 «သဘော ရှိသော» 'having the nature of' (not attested in pi-4); pi-4 diṭṭhigataṃ «မှား» "
             "(^4-62) and araññagataṃ «ရောက်သော» (^4-196, ^4-197) are two meanings",
    'pada': "pi-2 «ပုဒ်» kept (^4-62 padasiddhi); pi-4 «စကားလုံး» is the word, padaparamo (^4-151, ^4-M-10)",
    'kata': "pi-2 «ပြုပြီးသော» is 'done' (not attested in pi-4); pi-4 «ကျေးဇူး» is a kindness done, kataññū (^4-83)",
    'vuṭṭhāti': "pi-2 «ထမြောက်သည်» emerges from an attainment (not attested in pi-4); pi-4 «ပျောက်ကင်းသည်» "
                "recovers from illness (^4-94; kept sense difference, brief and harmonise B5)",
    'sampajāna': "pi-2 «ကောင်းစွာ ဆင်ခြင်သိမြင်သော» clear comprehension (not attested in pi-4); pi-4 «သိလျက်» "
                 "is 'knowingly', sampajānamusā (^4-98, ^4-99, also ^4-182)",
    'dukkhāya': "pi-3 «နာကျင်သော» painful feeling (not attested in pi-4); pi-4 «ဆင်းရဲခြင်း» is 'for the misery', "
                "ahitāya dukkhāya (^4-116)",
    'sukhāya': "pi-3 «သာယာသော» pleasant feeling (not attested in pi-4); pi-4 «ချမ်းသာခြင်း» is 'for the "
               "well-being', hitāya sukhāya (^4-117)",
    'gandha': "pi-3 smell «အနံ့» kept (^4-M-3, ^4-M-4); pi-4 «နံ့သာ» is perfume, mālāgandhavilepana "
              "(^4-117, ^4-168, ^4-179; mapper: gandha sense by context)",
    'attānaṃ': "pi-2 «မိမိကိုယ်» oneself (not attested in pi-4); pi-4 «အတ္တ» is the self declared real by a "
               "teacher (^4-131)",
    'pāṇa': "pi-2 living being «သတ္တဝါ» kept (^4-182, ^4-198); pi-4 «သူ့အသက်» is life, pāṇātipāta (^4-132 …; "
            "kept sense difference, brief)",
    'jātiyā': "pi-3 / pi-2 birth (not attested in pi-4); pi-4 «ဘဝ» is the life-time, tāya jātiyā (^4-151)",
    'mutta': "pi-2 «ပုလဲ» is pearl (not attested in pi-4); pi-4 muttapaṭibhāno «လျင်မြန်သော» (^4-152 …) and "
             "muttācāro «စွန့်လွှတ်သော» (^4-174) are two meanings",
    'kusalā': "pi-3 «ကုသိုလ်» wholesome (not attested in pi-4); pi-4 «ကျွမ်းကျင်သော» is skilled (^4-156)",
    'bhūtaṃ': "pi-1 «မူလဓာတ်» great element (not attested in pi-4); pi-4 «အမှန်အတိုင်း» is yathābhūtaṃ "
              "(^4-166, ^4-M-10)",
    'dassana': "pi-2 «ပြသသော» showing (not attested in pi-4); pi-4 «သိမြင်သော» is vision, "
               "vimuttiñāṇadassana (^4-173)",
    'daṇḍa': "pi-2 punishment kept (^4-176 «ဒဏ်»); pi-4 «တုတ်» is the stick, daṇḍamantaraṃ (^4-174)",
    'atta': "pi-2 / pi-1 «အတ္တ» self, soul (not attested in pi-4); pi-4 «မိမိ» is the reflexive 'oneself', "
            "attantapo, attahita (^4-174 …)",
    'bhūmiyā': "pi-2 / pi-1 «အဆင့်» stage (not attested in pi-4); pi-4 «မြေ» is the ground (^4-176)",
    'majjhima': "pi-2 «သန်းခေါင်» middle watch (not attested in pi-4); pi-4 «မဇ္ဈိမ» is the Majjhima Nikāya in a "
                "note (^4-176)",
    'sutte': "pi-2 «အိပ်ရာ» in sleeping kept (^4-182); pi-4 «သုတ်» is a sutta cited in a note (^4-176)",
    'pharusaṃ': "pi-2 / pi-1 «ဖုထစ်သော» rough to the touch (not attested in pi-4); pi-4 «ကြမ်းတမ်းသော စကား» is "
                "harsh speech (^4-178)",
    'yogā': "pi-3 «ထမ်းပိုး» yokes (not attested in pi-4); pi-4 «နည်းလမ်း» is devious means, sāciyogā (^4-179)",
    'khetta': "pi-2 «လယ်ကွင်း» is the sense organ called a field (not attested in pi-4); pi-4 «လယ်» is cultivated "
              "land, khettavatthu (^4-179)",
    'samādāya': "pi-2 «ဆောက်တည်၍» undertaking (not attested in pi-4); pi-4 «ယူဆောင်၍» is taking the bowl and robe "
                "along (^4-180)",
    'indriya': "pi-2 «စွမ်းရည်» kept (^4-M-1); pi-4 «အာရုံခံ အင်္ဂါ» is the sense organs of indriyasaṃvara "
               "(^4-181, ^4-182; kept sense difference, brief)",
    'ṭhite': "pi-2 «ရပ်ရာ» in standing kept (^4-182); pi-4 «တည်တံ့သော» is the stable mind, ṭhite āneñjappatte "
             "(^4-183 …)",
    'gate': "pi-2 «သွားရာ» in walking kept (^4-182); pi-4 «လားရာ ရှိသော» is gone to a destiny, sugate duggate "
            "(^4-184)",
    'upapanno': "pi-2 'possessed of' kept for «ပြည့်စုံသော» (^4-189, ^4-M-10); pi-4 «ဖြစ်ပေါ်လာသော» is reborn "
                "(^4-183)",
    'sota': "pi-3 ear «နား» kept; pi-4 «ရေစီး» is the current, anusota / paṭisota (^4-188, ^4-M-10; mapper)",
    'suto': "pi-2 «ကြားရသော» heard (not attested in pi-4); pi-4 «အကြားအမြင်» is learning, appassuto / bahussuto "
            "(^4-189, ^4-M-10), the pi-1 sutā sense",
    'ārabhati': "pi-2 / pi-1 'arouses energy' (not attested in pi-4); pi-4 «မှားယွင်းစွာ ပြုမူသည်» is "
                "'transgresses' (^4-191, ^4-M-11)",
    'ṭhānesu': "pi-1 «အခြေအနေ» grounds that stir the mind (not attested in pi-4); pi-4 «နေရာ» is the places of an "
               "editorial note (^4-203)",
    'puriso': "pi-2 «အမျိုးသား» a man (not attested in pi-4); pi-4 «သူတော်ကောင်း» is the member of the NAME "
              "sappuriso (^4-M-10, mapper P2)",
}

# Several Burmese values under one sense, or a value the binding sense does not list, checked by hand
# (variants or synonyms of one meaning, or the pi-4 text's own word for the binding meaning).
LUMP_OK = {
    # ---- sample ----
    'paññatti',      # book title «သတ်မှတ်ဖော်ပြခြင်း» (^4-0) / «သတ်မှတ်ချက်»: designation, one meaning (approved terms)
    'kasira',        # «ပင်ပန်း» (akasiralābhī) / «ခက်ခဲသော» (^4-168): toil, difficulty, one meaning
    'cetanā',        # «စေတနာ» (cetanābhabbo, the pi-4 text's word) = pi-3 'intention, volition'
    'pahīnāni',      # word «ပယ်ပြီးသော» / fragment of appahīna «ပယ်ရသော» (map-harmonise, rule 8): one meaning
    'sekkhā',        # the NAME plural «ကျင့်ကြံဆဲသူ» (mapper P1) = pi-3 «ကျင့်ကြံဆဲသူ၏» (genitive): one lemma
    # ---- full run: REVIEW headwords checked by hand ----
    'bhabba',        # «ထိုက်တန်သော» (bhabbāgamano) / «ထိန်းနိုင်သော» (anurakkhaṇābhabbo): capable, one meaning
    'niyato',        # NAME «လမ်းကြောင်း ကျိန်းသေသူ» / adjective «ကျိန်းသေသော» (mapper P1): pi-2 'fixed in destiny'
    'sammā',         # pi-2 «မှန်ကန်စွာ» is under the same tag as pi-3 «မှန်ကန်သော»: one sense
    'sammāsambuddho',   # the approved NAME «…ဘုရားရှင်» (P1) = pi-2 «…ဘုရား»: one meaning
    'dukkha',        # pi-2 «နာကျင်သော» is under the same pain tag as pi-3 «နာကျင်မှု»
    'sañjaneti',     # «ဖြစ်ပေါ်စေသည်» = pi-2 «ကောင်းစွာ ဖြစ်စေသည်»: produces, one meaning
    'gāmī',          # «ရောက်သော» (akaniṭṭhagāmī) / «လိုက်သွားသော» (anu- / paṭisotagāmī): going to, one meaning
    'pahīnā', 'pahīno', 'pahīnaṃ',   # word / fragment, as pahīnāni
    'avasesa',       # «အကြွင်း» = pi-1 «အကြွင်းအကျန်»
    'arahatta',      # pi-1 «ရဟန္တာ» under the same tag as pi-2 «အရဟတ္တ»
    'para',          # pi-1 lists «ပရ» (Paranimmita) under the same 'others' tag
    'saṭho',         # NAME «စဉ်းလဲသူ» (P1) = pi-2 «စဉ်းလဲသော»
    'evaṃ',          # «ဤသို့» / «ဤနည်းတူ» (the notes «evaṃ …»): thus, in this way
    'nikati',        # «ကောက်ကျစ်ခြင်း» / «စဉ်းလဲခြင်း» (^4-179): the text's two words for dishonesty (map-harmonise 8)
    'vācāya',        # «နှုတ်» / «စကား»: by speech, one meaning
    'anādariyatā',   # «…အဖြစ်» = pi-2 «…သဘော»
    'sutā',          # only the pi-1 'learning' sense is attested (appassutā)
    'indriyaṃ asaṃvutaṃ',   # gapped «စွမ်းရည် … မစောင့်စည်းသော» = pi-2 contiguous (rule 10)
    'rūpaṃ',         # only the pi-2 'visible form' sense is attested (restraint passage)
    'bhojane mattaññū',     # NAME «…သိသူ» = pi-2 «…သိသော»
    'anussati',      # pi-1 lists «အောက်မေ့နိုင်သော» under the same tag
    'sampajāno',     # NAME «…ရှိသူ» / adjective «…သိမြင်သော» (map-harmonise, NAME vs adjective)
    'abhisamayo',    # «ထိုးဖောက် သိမြင်ခြင်း» / «ထင်ထင်ရှားရှား သိမြင်ခြင်း»: the text's two wordings (map-harmonise 7)
    'phalaṃ',        # «အကျိုး» (mahapphalaṃ) = pi-2 'fruit, the result of deeds'
    'gatā',          # pi-1 «ရောက်ရှိသော» under the same tag
    'sammāpaṭipannā',   # «…ကျင့်ကြံသော» / «…ကျင့်သော»: one verb (map-harmonise 5)
    'maggo',         # only pi-2 'way, road' sense attested (kummaggo)
    'paṭiggāho',     # «လက်ခံ စွဲကိုင်ခြင်း» = pi-1 'firm grasping'
    'bahiddhā',      # only pi-2 'external fetters' sense attested (bahiddhāsaṃyojano)
    'phāsu',         # word «ချမ်းသာ» / adverb «ချမ်းသာစွာ» (map-harmonise, word vs fragment)
    'bhūrī',         # pi-1 «ကျယ်ပြန့်ခြင်း» under the same tag
    'sevati', 'sevanti',   # «ပေါင်းသင်းသည်» = pi-2 'associates with'
    'sāvakā',        # «တပည့်» = pi-2 «တပည့်သာဝက»
    'suṇāti',        # «ကြားရ / ကြား / ကြားနာ»: the text's three wordings for hearing (map-harmonise 6)
    'nāmo',          # «မည်သော» (itthannāmo) = pi-2 'having such a name'
    'pūti',          # «ပုပ်သိုးသော» = pi-2 «ပုပ်စပ်သော»
    'vigata',        # «ကင်းပြီးသော» (NAME part) / «ကင်းသော» (map-harmonise, word vs fragment): one meaning
    'evameva',       # «ထို့အတူပင်» / «ဤနည်းတူ» (note): just so, likewise
    'gilāna',        # «လူနာ» / «သူနာ» (gilānapaccaya idiom, map-harmonise 11): sick, one meaning
    'gamā',          # pi-1 «ရောက်သော» under the same tag
    'manāpā',        # pi-1 «စိတ်တွေ့သော» under the same tag
    'maṇi',          # «ပတ္တမြား» = pi-2 «ကျောက်မျက်»: gem
    'natthi kiñci',  # «တစ်စုံတစ်ရာမျှ မရှိသည်» = pi-2 'there is nothing'
    'pāsāṇo',        # «ကျောက်» = pi-2 «ကျောက်တုံး»: rock
    'ādi',           # only pi-2 'beginning' sense attested (ādikalyāṇa)
    'brahmacariyaṃ', # «မြင့်မြတ်သော အကျင့်» = pi-2 «မြတ်သော အကျင့်»
    'cariyaṃ',       # «အကျင့်» = pi-2 «ကျင့်ဝတ်»: way of living
    'atthaṃ',        # «အနက်အဓိပ္ပာယ်» / «အနက်» (map-harmonise 1) = pi-2 'the meaning'
    'pakāsenti',     # «ထုတ်ဖော် ပြသည်» = pi-2 'make manifest'
    'desenti',       # «ဟောကြားသည်» = pi-2 «ဟောသည်»
    'byañjanaṃ',     # «စကားလုံး» / «သဒ္ဒါ» (^4-177): the text's two words for the phrasing (map-harmonise 1)
    'payirupāsanti', # «ချဉ်းကပ် ခစားသည်» = pi-2 'attend on'
    'anattamano',    # «စိတ်မနှစ်သိမ့်သော» = pi-2 «စိတ် မနှစ်သိမ့်သော» (spacing)
    'bhajanti',      # «ဆည်းကပ်သည်» = pi-2 'associate with'
    'senāsana',      # «ကျောင်းအိပ်ရာနေရာ» / «အိပ်ရာ နေရာ» (map-harmonise 2): lodging, one meaning
    'samphasso',     # pi-1 «ထိတွေ့ရ» under the same tag
    'dubbaṇṇo',      # «အဆင်း ညှိုးသော» (cloth) / «အဆင်း ဆိုးသော» (persons) (map-harmonise 9): ill-coloured
    'sukha',         # pi-2 «သာယာသော» under the same tag as pi-3 «သာယာမှု»
    'pameyyo',       # NAME «ချိန်ဆရ» / adjective «ချိန်ဆ၍ ရနိုင်သော» (map-harmonise): measurable
    'indriyo',       # «အာရုံခံ အင်္ဂါ» = pi-2 'having faculties' (ahīnindriyo-type compound final)
    'vāco',          # NAME part «ပြောတတ်သော» / «စကားကို ပြောသော» (map-harmonise): of speech
    'kathā',         # «စကား» (sīlakathā …) fits pi-3 'talk or treatise'
    'purisapuggalo', # «လူ ပုဂ္ဂိုလ်» = pi-2 «ပုဂ္ဂိုလ်»
    'anatthaṃ',      # pi-1 «မကောင်းမှု» under the same tag
    'duggandho',     # «အနံ့ ဆိုးသော» = pi-2 'foul smell'
    'kārī',          # «ကျင့်သော» (paripūrakārī) / «ပြုလေ့ရှိသော» (^4-182): one who does, one meaning
    'attanā',        # «မိမိကိုယ်တိုင်» / «မိမိကိုယ်» (map-harmonise, word vs fragment): by oneself
    'atthe',         # «အနက်» = pi-2 «အကျိုးအနက်»: the meaning
    'nirodha',       # pi-2 «ချုပ်ငြိမ်း» under the same tag as pi-3 «ချုပ်ငြိမ်းခြင်း» (map A3)
    'avaṇṇa',        # «ကဲ့ရဲ့» = pi-2 «ကဲ့ရဲ့ သတင်း»: dispraise
    'vaṇṇapokkharatāya',  # «လှပသော အဆင်း» = pi-2 «အဆင်းလှခြင်း»
    'kasirena',      # «ခက်ခဲစွာ» = pi-2 «ပင်ပန်းစွာ»
    'gahapati',      # «သူကြွယ်» / «သူကြွယ်မျိုး» (map-harmonise, word vs compound): householder
    'ābādho',        # «ရောဂါ» = pi-2 «အနာရောဂါ»
    'sāro',          # «အနှစ်» = pi-2 «အနှစ်သာရ»: heartwood
    'pariṇāhaṃ', 'ārohaṃ', 'saṇṭhānaṃ',   # the body measures (^4-171) = pi-2's
    'dukkara',       # «ပြုရခက်သော» = pi-2 'hard to do'
    'ajinaṃ',        # «သမင်သားရေ» / «သားရေ»: antelope hide, one meaning
    'ācāro',         # «ကျင့်ဝတ်» (muttācāro) = pi-2 'conduct'
    'yāpeti',        # «မျှတသည်» = pi-2 «မျှတစေသည်»
    'padhāna',       # «ကြိုးစားခြင်း» = pi-2 'striving'
    'cora',          # «သူခိုး» = pi-2 «ခိုးသူ»
    'sappi',         # «ထောပတ်ကြည်» / «ထောပတ်» (^4-176) (map-harmonise 3): ghee, one meaning
    'khara',         # «ကြမ်းသော» = pi-1 «ခက်မာ»: harsh
    'uppajjati',     # «ပွင့်ထွန်းတော်မူသည်» (honorific, the Tathāgata) = pi-2 'arises'
    'raja',          # «ဖုန်လုံး» (the dust cloud) / «မြူမှုန်» (rajāpatha): dust, one meaning
    'paṭisaṃvedī',   # «ခံစားသော» = pi-2 «ခံစားခဲ့သော»
    'vijjā',         # pi-1 «အမှန်သိမြင်မှု» under the same tag
    'ekanta',        # «စင်စစ်» / «လုံးဝ»: wholly, synonyms
    'sacca',         # pi-1 truth «အမှန်» added after pi-3 «သစ္စာ» (binding pi-1 sense)
    'cittaṃ parisodheti',   # gapped «စိတ် … » = pi-2 contiguous (rule 10)
    'vūpasantacitto',       # «…ငြိမ်သက်ပြီးသော…» = pi-2 «…ငြိမ်သက်သော…»
    'anussarati',    # «အဖန်ဖန် အောက်မေ့သည်» = pi-2 (without «တော်မူ»)
    'dasa',          # pi-2 «ဆယ်» under the same tag as pi-3 «ဆယ်ပါး»
    'cuti',          # pi-1 «သေခြင်း» under the same tag
    'dukkhaṃ',       # only pi-2 noble-truth sense attested (^4-198, ^4-208)
    'itthī',         # «မိန်းမ» = pi-2 «အမျိုးသမီး»: a woman
    'viloketi',      # «ပတ်ဝန်းကျင်ကို ကြည့်သည်» = pi-2 'looks around'
    'Ettāvatā',      # «ဤမျှ» = pi-2 «ဤမျှဖြင့်»
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
    bind = OrderedDict((k, read_senses(p, True)) for k, p in BIND_FILES.items())
    mr = read_senses(MR_SENSES, False)
    out, unresolved, review, errs = [], [], [], []
    stats = OrderedDict([('manual', 0)])
    for k in bind:
        for s in ('same', 'subset', 'plus', 'lump'):
            stats[f'{k}_{s}'] = 0
    stats['mr'] = 0
    stats['case_only'] = 0
    for hw, vals in rows.items():
        if not vals:
            continue
        found = OrderedDict()                                   # src -> senses, in binding order
        for k, d in bind.items():
            kk = lookup(d, hw)
            if kk:
                found[k] = d[kk]
                if kk != hw and not [x for x in found if x != k]:
                    stats['case_only'] += 1
        of = {k: {v: t for t, vs in s for v in vs} for k, s in found.items()}
        bind_of = {}
        for k in reversed(list(found)):                         # pi-3 first where several list a value
            bind_of.update(of[k])
        bind_tags = [t for s in found.values() for t, _ in s]
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
            if found and hw not in TAG_CHANGED:
                for t, vs in senses:
                    for v in vs:
                        if v in bind_of and not t.startswith(bind_of[v]):
                            errs.append(f'{hw}: {v!r} leaves its binding sense {bind_of[v]!r}')
            if found:
                for t, vs in senses:
                    if all(v not in bind_of for v in vs) and not any(t.startswith(b) for b in bind_tags) \
                            and hw not in NEW_SENSE:
                        errs.append(f'{hw}: new sense {t!r} not logged in NEW_SENSE')
        elif found:
            src = next(iter(found))
            ref, ref_of = found[src], of[src]
            later = [k for k in found if k != src]
            new = [v for v in vals if v not in ref_of]
            senses = [(t, [v for v in vs if v in vals]) for t, vs in ref]
            senses = [(t, list(vs)) for t, vs in senses if vs]
            if not new:
                full = len(senses) == len(ref) and len(vals) == len(ref_of)
                stats[f'{src}_{"same" if full else "subset"}'] += 1
            elif all(any(v in of[k] for k in later) for v in new):
                for v in new:
                    k = next(k for k in later if v in of[k])
                    t1 = of[k][v]
                    hit = [s for s in senses if s[0] == t1]
                    if hit:
                        hit[0][1].append(v)
                    else:
                        senses.append((t1, [v]))
                stats[f'{src}_plus'] += 1
                if hw not in LUMP_OK:
                    review.append((hw, f'{BOOK[src]} senses + later binding sense for ' + ' / '.join(new),
                                   list(vals)))
            elif len(ref) == 1:
                senses = [(ref[0][0], list(vals))]
                stats[f'{src}_lump'] += 1
                if hw not in LUMP_OK:
                    review.append((hw, f'{BOOK[src]} one sense, new values ' + ' / '.join(new), list(vals)))
            else:
                unresolved.append((hw, f'{BOOK[src]} senses ' + str([t for t, _ in ref]), list(vals)))
                continue
        else:
            k3 = lookup(mr, hw)
            tags = mr.get(k3) if k3 else None
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
    unused = [h for h in list(MANUAL) + list(LUMP_OK) if h not in rows]
    if unused:
        print(f'note: MANUAL / LUMP_OK entries not in this input (fine for a part run): {unused}')
    with open(outp, 'w', encoding='utf-8', newline='\n') as f:
        f.write(f'# Pāli→Burmese pi-4 sense decisions, written by gen_decisions_my.py from {pathlib.Path(aggp).name}\n')
        f.write('# English tags: pi-3, then pi-2, then pi-1 Burmese senses (binding), else Marathi pi-4 senses '
                '(tags only), or MANUAL;\n')
        f.write('# values: pi-4 Burmese keyword map only.\n')
        f.write('\n'.join(out) + '\n')
    print(f'wrote {len(out)} decision lines -> {outp}')
    print('  ' + ' | '.join(f'{k} {v}' for k, v in stats.items()))
    if review:
        print(f'REVIEW ({len(review)}): check, then add to LUMP_OK or MANUAL:')
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
