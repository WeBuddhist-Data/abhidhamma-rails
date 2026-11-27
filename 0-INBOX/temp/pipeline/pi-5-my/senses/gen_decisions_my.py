"""Write the Pāli→Burmese pi-5 decisions file for senses_my.py (brief: pi-5-my/burmese-senses-brief.md).
Adapted from pi-4-my/senses/gen_decisions_my.py (same MANUAL / LUMP_OK / TAG_CHANGED / NEW_SENSE mechanism); the
binding chain is now pi-4, then pi-3, then pi-2, then pi-1.

usage: python -I -X utf8 gen_decisions_my.py <agg.tsv> <decisions.txt>

For every headword of agg.tsv that has Burmese values (NDE-only headwords are skipped):
  1. a hand decision in MANUAL below wins;
  2. otherwise the approved Burmese senses are BINDING, pi-4 first, then pi-3, then pi-2, then pi-1 (each looked up
     exact, else the one case-insensitive match: the aggregation keeps the first spelling seen). The reference is the
     line of the first of pi-4 / pi-3 / pi-2 / pi-1 that has the headword. Every pi-5 value that the reference lists
     goes under the reference's sense with its English tag, in the reference's sense order (a sense with no pi-5 value
     is left out). A pi-5 value the reference does not list:
       - a later binding file lists it: that file's sense (tag) is added after the reference's, or the value joins the
         reference sense with the same tag (REVIEW);
       - otherwise, the reference has one sense: the value joins it (REVIEW unless the headword is in LUMP_OK);
       - otherwise (the reference has several senses): UNRESOLVED (write MANUAL);
  3. otherwise, if the Marathi pi-5 senses file gives the headword ONE English tag, the line is that tag + every
     attested Burmese value (one sense; several values -> REVIEW unless LUMP_OK);
  4. otherwise (several Marathi senses, or no Marathi line) the headword is UNRESOLVED: write MANUAL.
Only the ENGLISH tags are read from the Marathi file; its Marathi values are dropped on parsing and never written.
A MANUAL entry for a pi-4 / pi-3 / pi-2 / pi-1 headword must keep the binding split: every value the binding senses
list (pi-4's sense for it, else pi-3's, else pi-2's, else pi-1's) sits under a sense whose tag starts with that binding
tag (an appended «, …» is allowed) unless the headword is in TAG_CHANGED (logged reason); and a MANUAL sense that holds
only values the binding senses do not list, with a tag that starts with none of the binding tags, is a NEW sense and
the headword must be in NEW_SENSE (logged reason).
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
    ('p4', ROOT / 'AI_translation/burmese/pi-4-pali-word-burmese-senses-plain.md'),
    ('p3', ROOT / 'AI_translation/burmese/pi-3-pali-word-burmese-senses-plain.md'),
    ('p2', ROOT / 'AI_translation/burmese/pi-2-pali-word-burmese-senses-plain.md'),
    ('p1', ROOT / 'AI_translation/burmese/pi-1-pali-word-burmese-senses-plain.md'),
])
BOOK = {'p4': 'pi-4', 'p3': 'pi-3', 'p2': 'pi-2', 'p1': 'pi-1'}
MR_SENSES = ROOT / 'AI_translation/marathi/pi-5-pali-word-marathi-senses-plain.md'
VAL_RE = re.compile(r'^(.*)=(\d+)\[[^\]]*\]$')
NONLATIN = re.compile(r'[\u0900-\u097f\u1000-\u109f]')

# Hand decisions: headword -> [(English tag, [Burmese values])]. Values must be attested.
# Binding senses first (pi-4, else pi-3, pi-2, pi-1 order and tag), then the senses new in pi-5.
MANUAL = OrderedDict([
    # ======== sample (agg-sample.tsv, the first 80 headwords) ========
    ('vatthu', [
        # pi-4 basis «အကြောင်း» not attested; pi-2 topics sense for the book title (^5-0) and its closing line (^5-918)
        ("topics, in Khuddakavatthu 'minor topics' (heading member), here the points of controversy, in the book "
         'title Kathāvatthu and its closing line', ['အငြင်းပွားရာ အကြောင်းအရာ', 'အကြောင်းအရာ']),
        ("stump, in tālāvatthukata 'made like a palm stump' of the arahant formula (compound member)", ['ငုတ်တို']),
    ]),
    ('vādī', [
        # pi-4 musāvādī «ပြောသော» (^5-857); the Tathāgata's epithets saccavādī, tathavādī … «ဆိုတော်မူသော» (^5-229 …)
        ('one who speaks, compound final in musāvādī, also in the epithets of the Tathāgata, saccavādī, tathavādī '
         'and the like', ['ဆိုတော်မူသော', 'ပြောသော']),
        ('party to the debate, in sakavādī (own side) and paravādī (the opponent) of the question notes',
         ['တစ်ဖက်သား', 'မိမိဘက်']),
    ]),
    ('vata', [
        ('vows, religious observances (compound member)', ['အကျင့်ဝတ်']),
        ("emphatic particle 'surely, indeed', in 'tena vata re vattabbe' of the rebuttal formula", ['အမှန်ပင်']),
    ]),
    ('parama', [
        # «အဆုံးစွန်» of paramattha (^5-1 …): the highest, the ultimate, the binding meaning
        ("highest, supreme (compound member), here the ultimate, in paramattha 'the ultimate sense'", ['အဆုံးစွန်']),
    ]),
    ('micchā', [
        # verdict «မှားသည်» / compound «မှားယွင်းသော» (map-harmonise §E): one lemma, one sense
        ("wrong, false (compound member), also the verdict 'that is wrong' of the rebuttal formula (predicate)",
         ['မှားသည်', 'မှားယွင်းသော']),
    ]),
    ('gati', [
        ('destination, rebirth realm (compound member), here also in the debate headings and the lists of realms',
         ['လားရာ']),
        ("access, the coming and going of monks, nuns and lay followers to a region, in 'yattha natthi gati "
         "bhikkhūnaṃ' (nominative)", ['သွားလာခြင်း']),
    ]),
    ('upādā', [
        ("derived from the great elements, of matter, here 'depending on', in upādāpaññatti 'designation by "
         "dependence' (compound member)", ['မှီ၍']),
        ('clinging, grasping, in anupādāparinibbāna (compound member, the positive part, mapper rule 8)',
         ['စွဲလမ်းမှု']),
    ]),
    ('purisa', [
        ("man, in purisaliṅga 'feature of a man', also masculinity, in purisindriya (compound member)", ['ယောက်ျား']),
        ("person, individual, in purisadosā 'faults of a person' (compound member), here in purisapuggala, "
         'purisayuga, purisuttama and the purisakāra headings', ['လူ']),
        ('good person, the member of sappurisa (compound member)', ['သူတော်ကောင်း']),
    ]),
    ('abhiññā', [
        ('by direct knowledge, higher knowing (instrumental), here the higher knowledges as a noun, in the '
         'headings and at ^5-196', ['ထူးကဲစွာ သိခြင်း']),
    ]),
    ('vāda', [
        ('doctrine, theory, in attavāda (compound member), here the position examined, in vādayutti (heading '
         'member)', ['ဝါဒ']),
        ('speaking, in musāvāda false speech (compound member)', ['ပြောခြင်း']),
    ]),
    ('paṭiññāya', [
        ("by self-declaration, claiming to be a monk (instrumental), here by one's own admission in the debate",
         ['ဝန်ခံချက်']),
    ]),
    ('aṭṭho', [
        # new in pi-5; one Burmese value «အရာ» (saccikaṭṭho, atthaṭṭho): the first Marathi sense only
        ('a reality, a thing that truly is, in saccikaṭṭho of the debate headings, also in atthaṭṭho and natthaṭṭho',
         ['အရာ']),
    ]),
    ('anuyogo', [
        ('an examination, a line of questioning (in the debate headings)', ['စစ်ဆေးမေးမြန်းခြင်း']),
        ('application to a practice, as in jāgariyānuyoga', ['နိုးကြားစွာ အားထုတ်ခြင်း']),
    ]),
    ('sutta', [
        # one Burmese value «သုတ္တန်» for the discourse and the book name: one sense
        ("a discourse of the Buddha, in the suttasādhana headings and 'Attheva suttanto', also in the book name "
         'Suttanipāta and in suttamūla', ['သုတ္တန်']),
    ]),
    ('niggaha', [
        ('rebuttal in debate', ['ချေပချက်']),
        ('holding back, restraining the mind', ['ချုပ်ကိုင်ခြင်း']),
    ]),
    # @@MANUAL-SAMPLE
    # ======== Marathi tags adjusted to the Burmese evidence (the Marathi tag described the Marathi wording) ========
    ('paramattho', [('the highest reality, the ultimate thing (nominative)', ['အဆုံးစွန် အရာ'])]),
    ('parihāni', [('decline, falling away (noun)', ['ဆုတ်ယုတ်ခြင်း'])]),
    ('Suniggahito', [('well rebutted (participle)', ['ကောင်းစွာ ချေပခြင်း ခံရသော'])]),
    ('hevameva', [("just so, in just this way (adverb, with the particle eva)", ['ဤနည်းအတိုင်းပင်'])]),
    ('niggaṇhāsi', [('you rebut (aorist)', ['ချေပသည်'])]),
    ('Dunniggahitā', [('improperly rebutted (participle)', ['မကောင်းစွာ ချေပခြင်း ခံရသော'])]),
    ('dukkaṭe', [('badly done (locative participle)', ['မကောင်းစွာ ပြုခဲ့သော'])]),
    ('vitāraṇa', [('crossing over doubt, clearing it up', ['ရှင်းပြပေးခြင်း'])]),
    ('Sabbesu', [('in all, among all things (locative pl.)', ['အရာအားလုံး'])]),
    ('dhammāyatanaṃ upalabbhati', [("'the mind-object base is apprehended' (thesis phrase)",
                                    ['သဘောတရား အာရုံခံ နယ်ပယ် … တွေ့ရသည်'])]),
    ('dhammadhātu upalabbhati', [("'the mind-object element is apprehended' (thesis phrase)",
                                  ['သဘောတရား ဓာတ် … တွေ့ရသည်'])]),
    ('adhigayha', [('taking all together, all at once (absolutive)', ['အလုံးစုံကို စုပေါင်း၍'])]),
    ('dhammāyatanaṃ puggalo', [("thesis phrase 'the mind-object base is the individual'",
                                ['သဘောတရား အာရုံခံ နယ်ပယ်သည် ပုဂ္ဂိုလ်'])]),
    ('anamataggo', [('without known beginning (predicate)', ['အစကို ရှာ၍ မတွေ့နိုင်'])]),
    ('nīvaraṇānaṃ', [('of the obstructions, the hindrances (genitive pl.)', ['အတားအဆီး'])]),
    ('lokā upapanno', [("'reborn from the world' (phrase)", ['လောက … ပြန်လည် ဖြစ်ပေါ်သော'])]),
    ('jīyati', [('ages, grows old (3rd sg.)', ['အိုသည်'])]),
    ('Tassa tasseva', [("'of each one in turn' (repeated pronoun with eva)", ['ထိုထိုသူ၏ပင်'])]),
    ('adukkhamasukhaṃ vedanaṃ', [('the feeling that is neither painful nor pleasant (accusative phrase)',
                                  ['မနာကျင် မသာယာသော ခံစားမှု'])]),
    ('bhavarāgānusayo', [('latent lust for becoming (nominative)', ['ဘဝရာဂ ကိန်းအောင်းခြင်း'])]),
    ('passāvo', [('bladder discharge, urine, also in the pair uccārapassāvo (nominative)', ['ကျင်ငယ်'])]),
    ('avitathāni', [('not untrue, not false, in avitathāni (nominative pl.)', ['မဖောက်ပြန်သော'])]),
    # ======== full run (agg-part1.tsv): UNRESOLVED headwords ========
    ('pada', [
        ('rules, items, in sikkhāpada (compound final), here a grammatical item, in padasiddhi, also a term '
         'examined, in Padasodhanakathā', ['ပုဒ်']),
        ("step, stride, in sattapadavītihāra 'walking seven steps' (compound member)", ['လှမ်း']),
    ]),
    ('bheda', [
        ('breaking into speech, in vacībheda', ['စကား ထွက်ခြင်း']),
        ('schism, in saṅghabheda', ['သင်းခွဲခြင်း']),
    ]),
    ('bodhiyā', [
        ('enlightenment as a state (instrumental), in the Bodhi headings and bodhiyā buddho', ['ဗောဓိ']),
        ('the Bodhi tree, in bodhiyā mūle (genitive)', ['ဗောဓိပင်']),
    ]),
    ('niyāma', [
        ('fixed course of rightness, the path that is certain', ['သေချာသော လမ်း', 'သေချာသော လမ်းကြောင်း']),
        ('fixed destiny of an ordinary person, in accantaniyāmatā', ['ကျိန်းသေခြင်း']),
    ]),
    ('sacca', [
        # pi-4 senses (tags); «မှန်သော» of the epithet saccavādī (^5-229 …) = what is true
        ("the truths, in saccānulomikañāṇa 'knowledge in conformity with the truths' (compound member)", ['သစ္စာ']),
        ('truth, what is true, as in idaṃsaccābhinivesa (compound member), here true, in the epithet saccavādī',
         ['မှန်သော']),
    ]),
    ('dhamma', [
        # pi-4 senses (tags); «ဓမ္မ» the loan in dhammacakka / dhammacakkhu / dhammavinaya = the teaching
        # (map-harmonise §A 12, kept difference dhamma «အရာ / ဓမ္မ / တရား»)
        ('phenomena, states (as in the book title Dhammasaṅgaṇī), the same value also naming mind-objects, what '
         'the mind as sixth sense knows (as in dhammāyatana)', ['သဘောတရား']),
        ("the Buddha's teaching, in dhammamacchariya and dhammapaṭisanthāra, here also in dhammadesanā and the "
         'fixed names dhammacakka, dhammacakkhu and dhammavinaya, and the truth in dhammaṭṭha and dhammaniyāmatā',
         ['တရား', 'ဓမ္မ']),
        ("field, domain, in sadhammakusala and paradhammakusala 'skilled in one's own or in another's field' "
         '(compound member)', ['အရာ']),
    ]),
    ('anantarā', [
        # three wordings of 'immediately (after)', the same meaning: one sense
        ('without interval, directly after, also in anantarāpayutta (compound member)',
         ['ချက်ချင်း နောက်', 'ချက်ချင်း', 'နောက်တွင် ချက်ချင်း']),
    ]),
    ('samāpanno', [
        ('having entered a meditative attainment', ['ဝင်စားနေသော']),
        ("involved in, in 'caught up in favouring and opposing' (anurodhavirodhaṃ samāpanno)", ['ရောက်သော']),
    ]),
    ('anantara', [
        ('contiguity, the proximity relation, in anantarapaccaya (compound member)',
         ['ချက်ချင်း နောက်၌ ဖြစ်စေသော', 'ကြားမလပ်']),
        ('next in sequence, in anantaravāra (compound member)', ['နောက်ဆက်တွဲ']),
    ]),
    ('vaṇṇa', [
        ('guise, outward look, in Arahantavaṇṇakathā (heading member)', ['အသွင်']),
    ]),
    ('Rūpaṃ puggalo', [
        # one Burmese value «ရုပ်» in all three segments: one sense
        ("thesis phrase 'matter is the individual'", ['ရုပ်သည် ပုဂ္ဂိုလ်', 'ရုပ် … ပုဂ္ဂိုလ်']),
    ]),
    ('sama', [
        ("evenly, in due balance, in asamapekkhaṇā (compound member), here equal, in samabhāga 'an equal share'",
         ['တူသော']),
    ]),
    ('kāyo', [
        ('the physical body, or bodily (nominative sg.)', ['ကိုယ်']),
        ('troop, multitude, in asurakāyo (compound final)', ['အပေါင်း']),
    ]),
    ('mahiso', [
        # no Marathi line
        ('buffalo (nominative sg.)', ['ကျွဲ']),
    ]),
    ('hatthako', [
        ('little hand, in kuṇihatthaka', ['လက်']),
        ('proper name, Hatthaka of Āḷavī', ['ဟတ္ထက']),
    ]),
    ('upapanno', [
        ('reborn, reappeared in a new existence (nominative sg. participle)', ['ပြန်လည် ဖြစ်ပေါ်သော']),
    ]),
    ('vigato', [
        # no Marathi line
        ('gone, vanished (nominative sg. participle)', ['ကွယ်ပျောက်သော']),
    ]),
    ('karonti', [
        ('do, perform (3rd pl.)', ['ပြုသည်']),
        ('construct, of houses and storerooms', ['ဆောက်သည်']),
    ]),
    ('dukkhā', [
        ('painful, of feeling (feminine adjective)', ['နာကျင်သော']),
        ('suffering, said of the five aggregates of clinging (nominative pl.)', ['ဒုက္ခ']),
        ("miserable, painful in the everyday sense, in 'kāmā aniccā dukkhā' of the views (nominative pl.)",
         ['ဆင်းရဲ']),
    ]),
    ('dha', [
        ('abbreviated citation of the Dhammapada', ['“ဓမ္မပဒ”']),
        ('abbreviated citation of the Dhammasaṅgaṇī', ['သဘောတရားများကို စုစည်းရေတွက်ခြင်း']),
    ]),
    ('saṅkiṇṇa', [
        ('filled in, of a moat, in saṅkiṇṇaparikha (compound member)', ['ဖို့ပြီးသော']),
        ('mingled, adulterated, in asaṅkiṇṇa (compound member)', ['ရောနှောခြင်း', 'ရောယှက်သော']),
    ]),
    ('ghano', [
        ('compact, solid, in ekagghano (masculine)', ['ခဲနက်']),
        ('the solid mass, an embryonic stage', ['အခဲ']),
    ]),
    ('viññātāresu', [
        # no Marathi line: aviññātāresu of the border peoples (^5-271), the positive part (mapper rule 8)
        ('those who understand, in aviññātāresu of the border peoples (locative pl.)', ['နားလည်သော']),
    ]),
    ('ekaṭṭhe', [
        ('co-existing, standing in one place, in tadekaṭṭhe (locative)', ['တစ်နေရာတည်း တည်ရှိသော']),
        ('identical in sense, eka-attha (locative)', ['အနက် တူသော']),
    ]),
    ('Anāgataṃ rūpaṃ', [
        ('matter yet to come (phrase)', ['အနာဂတ် ရုပ်']),
        ('visible object yet to come (phrase)', ['အနာဂတ် အဆင်းအရောင်']),
    ]),
    ('Atītaṃ rūpaṃ', [
        ('bygone matter (phrase)', ['အတိတ် ရုပ်']),
        ('bygone visible object (phrase)', ['အတိတ် အဆင်းအရောင်']),
    ]),
    ('Paccuppannaṃ rūpaṃ', [
        ('matter arisen now (phrase)', ['ပစ္စုပ္ပန် ရုပ်']),
        ('visible object arisen now (phrase)', ['ပစ္စုပ္ပန် အဆင်းအရောင်']),
    ]),
    ('rajjamānaṃ', [
        ('being coloured, of cloth in the dye (present participle)', ['ဆိုးဆေး ဆိုးနေသော']),
        ('becoming lustful, of the mind (present participle)', ['တပ်မက်ဆဲ']),
    ]),
    ('niccaṃ', [
        ('lasting, permanent (nominative or accusative)', ['မြဲသော', 'မြဲ']),
        ('constantly, always (adverb), in wishes for ever-leafy trees', ['အမြဲ']),
    ]),
    ('dhammaṃ', [
        ('mind-objects, what the mind as sixth sense knows (accusative sg.), the same value also naming a '
         'phenomenon, any state, as in na kañci dhammaṃ', ['သဘောတရား']),
        ("the teaching, the doctrine heard and remembered, in 'dhammaṃ jānāti – suttaṃ geyyaṃ' (accusative sg.)",
         ['တရား']),
        ("practice, in methunaṃ dhammaṃ 'sexual intercourse' (accusative sg.)", ['အကျင့်']),
    ]),
    ('bhedana', [
        ('smashing, physical destruction, in chedanabhedana (compound member)', ['ခွဲခြင်း']),
        ('estrangement from friends, in bhedanasaṃvattanika (compound member)', ['ကွဲပြားခြင်း']),
    ]),
    ('tiṭṭheyya', [
        ('would endure, remain in existence (optative)', ['တည်နေသည်']),
        ('would take up position, of an ambush, in paripanthe tiṭṭheyya (optative)',
         ['ဓားပြ တိုက်သည်', 'စောင့်ဆိုင်းလုယက်သည်']),
    ]),
    ('suriyova', [
        # no Marathi line
        ("the sun, in suriyova 'like the sun' (nominative with the particle va)", ['နေမင်း']),
    ]),
    ('paccayo', [
        ('support, conditioning factor (nominative)', ['အကြောင်း']),
        ('reliance on others, in parapaccayo (compound final)', ['အားကိုးရသော']),
    ]),
    ('viharissati', [
        # no Marathi line
        ('will dwell, will live on (3rd sg. future)', ['နေသည်']),
    ]),
    ('vihessati', [
        # no Marathi line: the variant reading of viharissati (^5-333)
        ('will dwell, the variant reading of viharissati (3rd sg. future)', ['နေသည်']),
    ]),
    ('āhāro', [
        # pi-4 food «အစာ» and pi-2 nutriment «အာဟာရ»; «ဆိုခြင်း» the uttering of dukkhāhāro (^5-334, ^5-353)
        ("food, what is eaten, in evamāhāro 'having such food' of the past-lives formula (compound final), here "
         'also the food of happiness, in sukhassāhāro', ['အစာ']),
        ('nutriment, a sustaining condition of mind (contact, volition, consciousness), also edible food as '
         'nutriment, in kabaḷīkāro āhāro and the four nutriments', ['အာဟာရ']),
        ("bringing out, utterance, in dukkhāhāro 'the uttering of pain' (compound final)", ['ဆိုခြင်း']),
    ]),
    ('muhuttaṃ', [
        ('a short span of time, as a unit beside khaṇa and laya (accusative)', ['မုဟုတ်ကာလ']),
        ('moment by moment, in the repeated muhuttaṃ muhuttaṃ (adverbial accusative)', ['ခဏခဏ']),
    ]),
    ('cetasikaṃ', [
        ('mental, of the mind as opposed to the body (neuter sg. adjective), here of pleasure and pain', ['စိတ်']),
        ('a mental factor, what accompanies the mind, in the cetasika dyad (acetasikaṃ, neuter sg.)',
         ['စိတ်၏ အဖော်']),
    ]),
    ('sutaṃ', [
        ('heard, what is heard (neuter sg. participle)', ['ကြားခဲ့ရသော']),
    ]),
    ('nirodhā', [
        # one Burmese value: one sense
        ('stoppings, endings, also ceasing together in ekanirodhā (nominative pl. or ablative)', ['ချုပ်ငြိမ်းသော']),
    ]),
    ('antarikā', [
        ('dividing gap, in the list uccanīcatā … antarikā (nominative)', ['ကြားအပိုင်း']),
        ('intermediate state between two jhānas, contacts etc., in jhānantarikā (nominative)', ['အကြား ကာလ']),
    ]),
    ('bhonto', [
        # no Marathi line: 'Ime vata bhonto sattā' (^5-377)
        ('good sirs, the respectful address (nominative pl.)', ['အချင်း']),
    ]),
    ('kula', [
        ("good family, in kulaputta 'a son of good family' (compound member)", ['အမျိုးကောင်း']),
    ]),
    ('gacchati', [
        # pi-2 senses (tags): «ရသည်» is pi-2's reckoning value; «သွားသည်» goes; «ရောက်သည်» reaches (^5-874)
        ("goes, takes a course, in 'agatiṃ gacchati' 'goes a wrong course' (3rd sg. present), here also of walking "
         'and travelling', ['သွားသည်']),
        ("comes under, is reckoned, in 'saṅkhyaṃ gacchati' (3rd sg. present), here also reaches a state, in "
         'bhāvanāpāripūriṃ gacchati', ['ရသည်', 'ရောက်သည်']),
    ]),
    ('niyāmo', [
        ('certainty, the fixed course of rightness (nominative sg.)', ['သေချာသော လမ်း', 'သေချာသော လမ်းကြောင်း']),
        ('a binding rule or law by which something is determined (nominative sg.)', ['စည်းမျဉ်း']),
    ]),
    ('niyatassa', [
        # one Burmese value: one sense
        ('of one certain of destiny (genitive sg.)', ['ကျိန်းသေသော']),
    ]),
    ('pariyāye', [
        ('comprehending, going round, in cetopariyāye (locative sg.)', ['ပိုင်းခြား၍ သိသော']),
        # «အလှည့်» (^5-635) / «ဘဝအဆက်ဆက်» (^5-782): the same sutta phrase in two wordings (map-harmonise §A 26)
        ('another time or turn, in apare vā pariyāye (locative sg.)', ['အလှည့်', 'ဘဝအဆက်ဆက်']),
    ]),
    ('niyāmatā', [
        ("certainty of one's destiny, the absolutely fixed course (nominative sg.)", ['ကျိန်းသေခြင်း']),
        ('fixed regularity of the way things are, in dhammaniyāmatā (nominative sg.)', ['သေချာခြင်း']),
    ]),
    ('jāyanti', [
        ('come to birth, of beings (3rd pl. present)', ['မွေးဖွားသည်']),
        ('develop, of limbs in the womb (3rd pl. present)', ['ဖြစ်ပေါ်သည်']),
    ]),
    ('passasi', [
        # no Marathi line
        ('you see (2nd sg. present)', ['မြင်သည်']),
    ]),
    ('byāyiko', [
        # no Marathi line: abyāyiko 'unfailing' (^5-485), the positive part (mapper rule 8)
        ("perishing, failing, in abyāyiko 'unfailing' (adjective)", ['ပျက်စီးတတ်သော']),
    ]),
    ('Ratto', [
        ('dyed with lust, inflamed (nominative sg. participle)', ['တပ်မက်နေသော']),
        ('by night, in divā ca ratto ca (adverbial)', ['ည']),
    ]),
    ('pavattati', [
        ('goes on, comes about, of mental states (3rd sg. present)', ['ဖြစ်ပွားသည်']),
        ('runs down, of water (3rd sg. present)', ['စီးဆင်းသည်']),
    ]),
    ('hāpayaṃ', [
        # no Marathi line: kulavaṃsaṃ ahāpayaṃ (^5-491), the positive part (mapper rule 8)
        ("letting decline, in kulavaṃsaṃ ahāpayaṃ 'not letting the family line decline' (present participle)",
         ['ဆုတ်ယုတ်စေသော']),
    ]),
    ('tiṭṭhanti', [
        ('remain, abide in a place (3rd pl. present)', ['တည်ရှိသည်', 'တည်သည်']),
        ('lie in wait, waylay and rob, in paripanthe tiṭṭhanti (3rd pl. present)', ['ဓားပြ တိုက်သည်']),
    ]),
    ('kammaṃ', [
        ("action-noun final '-making, -doing' in synonym lists, as in niṭṭhuriyakammaṃ and anāvikammaṃ, here in "
         'añjalikammaṃ and sāmīcikammaṃ', ['ပြုမူခြင်း']),
    ]),
    ('ṭhita', [
        ('steady, firm, in ṭhitatto (compound member), here in ṭhitadhamma', ['တည်မြဲသော']),
    ]),
    ('dissanti', [
        ('appear to be, with viya (3rd pl. passive)', ['ထင်ရသည်']),
        ('are seen, are met with (3rd pl. passive)', ['မြင်ရသည်']),
    ]),
    ('kaṇṇo', [
        ('organ of hearing (nominative)', ['နား']),
        ("angle or side, in catukkaṇṇo 'four-sided' (compound end)", ['ထောင့်']),
    ]),
    ('vattate', [
        # no Marathi line: the variant reading «vattate (?)» of vattati (^5-785)
        ('goes on, the variant reading of vattati in kammunā vattati loko (3rd sg. middle)', ['ဖြစ်သည်']),
    ]),
    ('vattati', [
        ('occurs, functions, of the mind-consciousness element depending on matter (3rd sg. present), here the '
         'world goes on by kamma, in kammunā vattati loko', ['ဖြစ်သည်']),
    ]),
    ('karaṇīyo', [
        ("worthy of, in añjalikaraṇīyo 'deserving joined palms' (compound end)", ['ရှိခိုးထိုက်သော']),
        ('fitting, ought to be done (gerundive)', ['လိုက်နာသင့်သော']),
    ]),
    ('kāraṇikā', [
        ('those who inflict punishment or torture, beside kammakāraṇā (nominative pl.)', ['ညှဉ်းပန်း နှိပ်စက်သူ']),
        ('animal trainers, in a list of stable hands (nominative pl.)', ['လေ့ကျင့်ပေးသူ']),
    ]),
    # @@MANUAL-UNRES
    # ======== full run: REVIEW headwords with a genuinely new pi-5 meaning, or a tag fitted to pi-5 ========
    # ---- REVIEW batch 1 ----
    ('para', [
        ('others, another person (compound member, as in paralābha and paranimmita), here also in paracitta and '
         'parappavāda', ['သူတစ်ပါး', 'ပရ', 'အခြားသူ', 'အခြား']),
        ("more than, beyond, in parosahassa 'over a thousand' (compound member)", ['ကျော်']),
    ]),
    ('citta', [
        ('mind, consciousness (stem and compound member), also in cittiddhipāda', ['စိတ်', 'စိတ္တ']),
        ('variegated, colourful, in cittavaṇḍa (compound member)', ['အရောင်စုံ']),
    ]),
    ('Sabbattha', [
        ("everywhere, in sabbatthagāminī 'leading to all destinations' (compound member), here also the adverb "
         "'in every place'", ['နေရာတိုင်း', 'ဘုံ အားလုံး']),
    ]),
    ('paṭicca', [
        ('dependent on conditions, first member of paṭiccasamuppanna, and of paṭiccasamuppāda (dependent '
         "origination) in the Mātikā and its definition, here also the absolutive 'depending on'",
         ['အကြောင်းတို့ကို မှီ၍', 'မှီ၍']),
    ]),
    ('rūpadhātu', [
        ('the visible-form element, the object of the eye (nominative sg.)', ['အဆင်းအရောင် ဓာတ်']),
        ('the fine-material realm of existence, among the planes (nominative sg.), also as the fine-material '
         'element', ['သိမ်မွေ့သော ရုပ်ဘုံ', 'သိမ်မွေ့သော ရုပ် ဓာတ်']),
    ]),
    ('dukkhaṃ', [
        ('suffering in the sense of the noble truth, the unsatisfactoriness of what is conditioned (nominative sg.)',
         ['ဒုက္ခ']),
        ('pain, suffering (nominative/accusative sg.), here painful feeling, also attributive in dukkhaṃ vedanaṃ',
         ['နာကျင်သော']),
        ("misery, pain in the everyday sense, in āpāyikaṃ dukkhaṃ 'the misery of the states of loss' and in "
         'sukhaṃ dukkhaṃ (nominative or accusative sg.)', ['ဆင်းရဲ']),
    ]),
    ('eka', [
        ('one, as in the one-item section label Ekamūlaka, here one seed, one more birth, in ekabījī (compound '
         'member), also one path, one mind-moment, in ekamagga and ekacittakkhaṇika', ['တစ်စေ့', 'တစ်ပါး', 'တစ်',
                                                                                     'တစ်ခု']),
        ("one and the same, in Ekādhippāyakathā 'on a shared intention' (compound member)", ['တူညီသော']),
    ]),
    ('aññā', [
        ('final knowledge, the knowing of one on the higher paths (compound member), here also in '
         'sammadaññāvimutta and aññāpaṭivedha', ['သိ၍', 'အပြည့်အဝ သိမြင်ခြင်း', 'ရဟန္တာ ဖိုလ်']),
        ('other, different (feminine pronoun)', ['တခြားစီ']),
    ]),
    ('sukha', [
        ('pleasure, happiness, or pleasant (compound member, as in sukhasahagata, sukhavihāra and sukhasamphassa)',
         ['သာယာမှု', 'သာယာသော']),
        ("happiness, well-being in the everyday sense, in sukhadukkha 'pleasure and pain' of the views and the "
         "perversion 'dukkhe sukhan'ti' (compound member and quoted word), also in Sukhānuppadānakathā",
         ['ချမ်းသာ', 'သုခ']),
    ]),
    ('paccaya', [
        ('condition, cause, requisite (compound member), here in the paccaya headings', ['အကြောင်း']),
        ("reliance on others, in aparappaccaya 'not dependent on others' (compound final)", ['မှီသော']),
    ]),
    ('paccayatā', [
        ('conditionality, in idappaccayatā (compound final), also being a condition, in the paccayatā debates',
         ['ဤအကြောင်းကြောင့် ဤအကျိုး ဖြစ်ပုံ', 'အကြောင်းဖြစ်ပုံ', 'အကြောင်းဖြစ်ခြင်း']),
    ]),
    ('jāti', [
        ('birth, being born (nominative sg.), also rebirth, in jātisaṃsāra, the last birth and the jāti of '
         'dependent origination', ['မွေးဖွားခြင်း', 'ဖြစ်ခြင်း', 'ပဋိသန္ဓေ နေခြင်း', 'ဘဝ']),
        ("kind, sort, in gandhajāti 'kinds of scent' (compound member)", ['မျိုး']),
    ]),
    ('āneñja', [
        ('imperturbable (compound member)', ['မတုန်မလှုပ်သော', 'မတုန်လှုပ်သော', 'မတုန်လှုပ်ခြင်း']),
        ('the cited sutta title Āneñjasappāya (name)', ['အာနေဉ္ဇသပ္ပာယ']),
    ]),
    ('Saṃkhittaṃ', [
        ('contracted, shrunken, of a sluggish mind (neuter sg. participle)', ['တွန့်ဆုတ်နေသော']),
        ('shortened text, in the editorial notes (Saṃkhittaṃ)', ['အကျဉ်းချုပ်']),
    ]),
    ('lohitaṃ', [
        ('blood, the fluid in the veins (nominative sg.)', ['သွေး']),
        ('red, the colour of blood (nominative sg.)', ['အနီ']),
    ]),
    ('phalā', [
        # new in pi-5; «ဖိုလ်» fruition vs «အသီးအပွင့်» the fruits of deeds (^5-98, ^5-99): kept sense difference
        ('fruitions of the path, in the paths and fruits (nominative pl.)', ['ဖိုလ်']),
        ('fruits, results of deeds, in iṭṭhaphalā and kantaphalā (compound final)', ['အသီးအပွင့်']),
    ]),
    ('kamma', [
        ('deeds, as compound member', ['ကံ']),
        ('work, busy activity, in kammārāmatā (compound member)', ['အလုပ်']),
    ]),
    ('sukhaṃ', [
        ('pleasure, happiness, or pleasant (neuter sg.)', ['သာယာသော']),
        ('comfort, ease, in seyyasukhaṃ, passasukhaṃ and middhasukhaṃ (compound final), here happiness, well-being, '
         'as in dibbaṃ sukhaṃ and sukhaṃ dukkhaṃ', ['ချမ်းသာ', 'သုခ']),
    ]),
    ('sukhadukkhaṃ', [
        # new in pi-5; three wordings of weal and woe (map-harmonise §A 19); ^5-742 the feelings
        ('pleasure-and-pain, weal and woe, in the views on who makes them', ['ချမ်းသာနှင့် ဆင်းရဲ', 'ချမ်းသာ ဆင်းရဲ',
                                                                            'သုခ ဒုက္ခ']),
        ('pleasant and painful feeling, as feelings (^5-742)', ['သာယာမှု နာကျင်မှု']),
    ]),
    ('dhammānaṃ', [
        ('of phenomena, states (genitive pl.)', ['သဘောတရား']),
        ("of the qualities to be understood, in catunnaṃ dhammānaṃ ananubodhā 'not understanding four things' "
         '(genitive pl.)', ['တရား']),
    ]),
    ('atta', [
        ('self, soul, in attavāda (compound member)', ['အတ္တ']),
        ("one's own being, individual existence, in attabhāva (compound member)", ['ကိုယ်']),
    ]),
    ('saha', [
        # pi-2 tag covers both «အတူ» and «တစ်ပြိုင်နက်» (saha upapattiyā): one sense
        ('together with, at the same time as (compound member and preposition)', ['အတူ', 'တစ်ပြိုင်နက်']),
    ]),
    ('bahiddhā', [
        ("external, belonging to others, in 'ajjhattaṃ vā bahiddhā vā' and the internal and external triad (adverb)",
         ['မိမိ၏ ပြင်ပ၌']),
        ("outside, in 'ito bahiddhā' 'outside this teaching' (adverb), here going outside the body, in bahiddhā "
         'nikkhamitvā', ['အပြင်']),
    ]),
    ('sukhāya', [
        ('for the happiness, the well-being of, in dīgharattaṃ hitāya sukhāya (dative sg.)', ['ချမ်းသာ']),
        ('pleasant, of feeling (feminine genitive sg.)', ['သာယာသော']),
    ]),
    # ---- REVIEW batch 2 ----
    ('gandhā', [
        ('odours, objects of the nose (nominative pl.)', ['အနံ့']),
        ("stench of corruption, in nirāmagandhā 'free from the stench of corruption' (compound final)",
         ['အပုပ်နံ့']),
    ]),
    ('ṭhānaṃ', [
        ("ground, occasion, in vivādaṭṭhānaṃ 'ground for dispute' (compound final, nominative sg.), here in "
         "diṭṭhiṭṭhānaṃ 'a basis of views'", ['တည်ရာ']),
        ("place, position, in 'āsabhaṃ ṭhānaṃ' 'the place of the leader' (accusative sg.), here the heavenly "
         "abode, in 'saggamupenti ṭhānaṃ'", ['ဌာန']),
    ]),
    ('dhammo', [
        ('having the nature of, of such a character (compound final), as in kuppadhammo and akuppadhammo and in '
         'pāpadhammo and kalyāṇadhammo', ['သဘော ရှိသော']),
        ("the teaching, the Dhamma of the good, in 'sataṃ dhammo' and 'buddhena dhammo desito' (nominative sg.)",
         ['တရား']),
        ('a phenomenon, a state (nominative sg.)', ['သဘောတရား']),
        ("practice, in methuno dhammo 'sexual intercourse' (nominative sg.)", ['အကျင့်']),
    ]),
    ('uppāda', [
        ('arising, origination (compound member), also in anuppādadhamma and uppādakkhaṇa',
         ['ဖြစ်ပေါ်တော့သော', 'ဖြစ်ခြင်း']),
        ("causing to flow, in ruhiruppāda 'the shedding of blood' (compound member)", ['ထွက်စေခြင်း']),
    ]),
    ('pādā', [
        ("bases, in iddhipādā 'bases of power' (nominative pl., compound final)", ['ပါဒ်']),
        ('the feet, the body part (nominative pl.)', ['ခြေ']),
    ]),
    ('su', [
        ('"well", intensifying prefix in subuddho, also good, in sugandha \'fragrant\'', ['ကောင်းစွာ', 'မွှေးသော']),
    ]),
    ('yogo', [
        ('yoke, bond binding to existence (nominative sg.)', ['ထမ်းပိုး']),
        ("effort, application, in pubbayogo 'former effort' (compound final)", ['အားထုတ်မှု']),
    ]),
    ('dhāreti', [
        ('puts on (3rd sg. present), also bears, carries', ['ဝတ်သည်', 'ဆောင်သည်']),
    ]),
    ('khu', [
        # new in pi-5: the citation khu. pā. and the extractor fragment of dhammacakkhuṃ (^5-278)
        ('abbreviated citation of the Khuddakapāṭha (khu. pā.)', ['“ခုဒ္ဒကပါဌ”']),
        ("eye, the fragment of dhammacakkhu 'the eye of the Dhamma' (compound final)", ['မျက်စိ']),
    ]),
    ('jātiyā', [
        ("existence, life-time, in tāya jātiyā 'in that same life' (instrumental)", ['ဘဝ']),
        ('birth, being born, as a link of dependent origination, in jātiyā ñāṇaṃ (locative), here also rebirth',
         ['မွေးဖွားခြင်း', 'ပဋိသန္ဓေ နေခြင်း']),
    ]),
    ('āma', [
        ("uncooked flesh, in āmagandha 'smell of raw flesh' (compound member)", ['အစိမ်း']),
        ("yes, the assent 'āma' (indeclinable)", ['ဟုတ်ပါသည်']),
    ]),
    ('katvā', [
        ('having performed, in uposathakammaṃ katvā (absolutive), here in kammaṃ katvā', ['ပြု၍']),
        ('treating as, on the ground that, in the idiom iti katvā (absolutive)', ['အကြောင်းပြု၍', 'မှတ်ယူ၍']),
    ]),
    ('gatā', [
        ('gone, arrived (rightly), in sammaggatā (nominative pl. participle), here in saṅghagatā', ['ရောက်သော']),
        ('directed to, concerned with, in kāyagatāsati (compound member)', ['အာရုံပြုသော']),
    ]),
    ('assa', [
        ('his, of him (genitive pronoun)', ['ထိုသူ']),
        ('horse, the steed, in assaratana and hatthigavassa (compound member)', ['မြင်း']),
    ]),
    ('vādo', [
        ("speaking, in musāvādo 'false speech' (compound final)", ['ပြောခြင်း']),
        ('a doctrine, a school, in sabbatthivādo (compound final)', ['ဝါဒ']),
    ]),
    ('sukka', [
        ('white, pure (compound member)', ['ဖြူစင်သော']),
        ('seminal fluid, in sukkavissaṭṭhi (compound member)', ['သုက်']),
    ]),
    ('pīta', [
        ('drunk, what has been drunk, in asitapītakhāyitasāyita (compound member)', ['သောက်']),
        ('yellow, the yellow meditation device (compound member)', ['အဝါ']),
    ]),
    ('uppādeyya', [
        ("would cause, as in shedding the Buddha's blood (optative), also would bring about, in methunaṃ uppādeyya",
         ['ထွက်စေသည်', 'ဖြစ်စေသည်']),
    ]),
    ('bhedo', [
        ('breaking up, dissolution, in the impermanence list (nominative sg.)', ['ပြိုပျက်ခြင်း']),
        ("breaking forth, in vacībhedo 'utterance of speech' (nominative sg.)", ['စကား ထွက်ခြင်း']),
    ]),
    ('ghātako', [
        ('one who kills, executes (nominative)', ['သတ်သူ']),
        ('raider, destroyer, in gāmaghātako and nigamaghātako (compound final)', ['ဖျက်ဆီးရမည့်']),
    ]),
    # ---- REVIEW batch 3 ----
    ('gandhaṃ', [
        ('smell, odour as object (accusative sg.)', ['အနံ့']),
        ('perfume, scent given as a gift, in the list annaṃ pānaṃ vatthaṃ … gandhaṃ (accusative sg.)', ['နံ့သာ']),
    ]),
    ('tena', [
        ("therefore, for that reason, in tena vuccati (instrumental pronoun), also 'if so, then', in tena hi",
         ['ထို့ကြောင့်', 'သို့ဖြစ်လျှင်']),
    ]),
    ('setu', [
        ('causeway, bridge, in setughāto (compound member)', ['တံတား']),
        ('proper name, Setu the young brahmin, in setu māṇavo', ['သေတု']),
    ]),
    ('bhūtā', [
        ('the great elements, primary matter, in mahābhūtā (nominative pl.)', ['မဟာဘုတ်', 'ဓာတ်ကြီး']),
        ("become, in vasībhūtā 'having become masters' (compound final)", ['ဖြစ်စေနိုင်သော']),
    ]),
    ('pānaṃ', [
        # new in pi-5: the drink (gift lists) and the drinking of surāmerayapāna (^5-903): two meanings
        ('beverage, drink (nominative or accusative sg.)', ['သောက်ဖွယ်', 'အဖျော်']),
        ('drinking, in surāmerayapānaṃ (compound final)', ['သောက်ခြင်း']),
    ]),
    ('karaṇaṃ', [
        ("doing, taking up, in akaraṇaṃ 'not doing' (nominative sg.), here making, causing, in aññāṇakaraṇa and "
         'nānākaraṇa', ['ပြုတတ်သော', 'ကွဲပြားစေတတ်သော']),
    ]),
    ('vihāra', [
        ('abiding, dwelling, in brahmavihāra (compound member)', ['နေထိုင်ရာ']),
        ('monastery, a dwelling of monks, in ārāmavihāra (compound member)', ['ကျောင်း']),
    ]),
    ('uppāditaṃ', [
        ("made to flow, of the Tathāgata's blood (neuter sg. participle)", ['ထွက်စေအပ်သော']),
        ('produced, aroused, of remorse, in kukkuccaṃ uppāditaṃ (neuter sg. participle)', ['ဖြစ်ပေါ်စေခဲ့ပြီးသော']),
    ]),
    ('kareyya', [
        ('would exercise or wield rule (optative), also would commit, of a robbery (^5-901)', ['ပြုသည်', 'လုယက်သည်']),
    ]),
    ('dukkhāya', [
        ('for the suffering, the misery of, in dīgharattaṃ ahitāya dukkhāya (dative sg.)', ['ဆင်းရဲဖွယ်ရာ']),
        ('painful, of feeling (feminine genitive sg.)', ['နာကျင်သော']),
    ]),
    # ---- REVIEW batch 4 (one-stem groups checked by hand) ----
    ('buddho', [
        ('the Buddha, the Awakened One (nominative sg.)', ['ဘုရား', 'ဘုရားရှင်']),
    ]),
    ('maya', [
        ("consisting in, made of, the suffix -maya (compound end)", ['ဖြစ်သော']),
    ]),
    ('dakkhiṇaṃ', [
        ('religious gift, offering (accusative sg.)', ['အလှူ']),
    ]),
    ('aññatra', [
        ('except, apart from (adverb), also elsewhere, in natthaññatra and aññatra gacchati', ['အခြား']),
    ]),
    ('iddhiṃ', [
        ("supernormal power, in iddhiṃ vikubbati 'works a wonder' (accusative sg.)", ['ဣဒ္ဓိ']),
    ]),
    ('antarā', [
        ("between, intermediate, in antarābhava 'the intermediate existence' (compound member), also 'in the "
         "meantime' (adverb)", ['ကြား']),
    ]),
    ('puriso', [
        ('a man, male person (nominative sg.)', ['ယောက်ျား', 'ယောကျ်ား']),
    ]),
    ('atthato', [
        ('in terms of meaning, as to import (adverb in -to)', ['အဓိပ္ပာယ်']),
    ]),
    ('kusalassa', [
        ("skilled, expert, in sadhammakusalassa 'of one skilled in his own field' (genitive sg.)", ['ကျွမ်းကျင်သော']),
    ]),
    ('hetuka', [
        ("caused, having a cause, in ahetukavāda 'the doctrine of no cause' (compound member)", ['အကြောင်း']),
    ]),
    ('asuci', [
        ('unclean (compound member), here the bodily impurity, semen, in asuci sukkavissaṭṭhi',
         ['မစင်ကြယ်သော', 'မစင်ကြယ်သော သုက်ထွက်ခြင်း', 'မစင်ကြယ်သော သုက်']),
    ]),
    ('āsayo', [
        ('receptacle, store, of food and drink in the body (nominative sg.)', ['သိုလှောင်ရာ']),
    ]),
    ('nāma', [
        ('name, in nāmagotta (compound member)', ['အမည်']),
    ]),
    ('maṃsa', [
        ("flesh (compound member), here fleshly, physical, in maṃsacakkhu 'the physical eye'", ['ပကတိ']),
    ]),
    ('samitaṃ', [
        ('continually, without a break (adverb)', ['အစဉ်တစိုက်']),
    ]),
    ('vivaṭṭa', [
        ("drawn back, removed, in vivaṭṭacchada 'with the veil drawn back' (compound member)", ['ဖွင့်လှစ်ပြီးသော']),
    ]),
    ('anto', [
        ("end, boundary, in cāturanto 'ruling to the four ends of the earth' (compound final)", ['အဆုံး']),
    ]),
    ('dhammena', [
        ('by righteousness, lawfully, in adaṇḍena asatthena dhammena (instrumental)', ['တရား']),
    ]),
    ('daṇḍena', [
        ('with a stick, a staff (instrumental), here force, punishment, in adaṇḍena', ['ဒဏ်']),
    ]),
    ('saraṇaṃ', [
        ('refuge, a place of safety to go to (nominative or accusative sg.)', ['ကိုးကွယ်ရာ']),
    ]),
    ('citto', [
        ('of mind, compound final (nominative sg.)', ['စိတ် ရှိသော']),
        ('proper name, Citta the householder (citto gahapati)', ['စိတ္တ']),
    ]),
    ('pariyāya', [
        ('comprehending, encompassing, in cetopariyāya (compound member)', ['ပိုင်းခြား သိခြင်း']),
    ]),
    ('upamā', [
        ('simile, comparison (nominative)', ['ဥပမာ']),
    ]),
    ('āruppā', [
        ('the immaterial attainments, absorptions of the formless (nominative pl.), here the immaterial realms',
         ['ရုပ်မရှိသော ဘုံ']),
    ]),
    ('sā', [
        ('that, she (feminine pronoun)', ['ထို']),
    ]),
    ('cetasiko', [
        ('a mental factor, what accompanies the mind, in cetasiko dhammo (masculine sg.)', ['စိတ်၏ အဖော်']),
    ]),
    ('dahati', [
        ('burns, consumes with fire (3rd sg. present)', ['လောင်သည်']),
    ]),
    ('santo', [
        ('the good, virtuous people (nominative pl.)', ['သူတော်ကောင်း']),
    ]),
    ('samiddhi', [
        ('proper name, the monk Samiddhi', ['သမိဒ္ဓိ']),
    ]),
    ('kāmo', [
        ('desirous of, wishing to, in bhaṇitukāmo and abhikkamitukāmo (compound final)', ['လို']),
    ]),
    ('Rūpataṇhā', [
        ('craving for visible forms (nominative sg.)', ['အဆင်းအရောင်ကို တပ်မက်မှု']),
    ]),
    ('kappo', [
        ('a world-age, an aeon (nominative sg.)', ['ကမ္ဘာ']),
    ]),
    ('samāhito', [
        ('furnished with, in paññāsīlasamāhito (compound final)', ['ပြည့်စုံသော']),
    ]),
    ('veḷu', [
        ('the Bamboo Grove, in the name Veḷuvana (compound member)', ['ဝေဠုဝန်']),
    ]),
    ('yuttaṃ', [
        ('harnessed, yoked (participle)', ['ကပ်ထားသော']),
    ]),
    ('pattaṃ', [
        ('alms bowl (accusative sg.)', ['သပိတ်']),
    ]),
    ('samaye', [
        ("in the system of thought, the doctrine, in satthusamaye (locative)", ['အယူဝါဒ']),
    ]),
    ('seyyaṃ', [
        ('bed, a sleeping place, in the gift lists (accusative sg.)', ['အိပ်ရာ']),
    ]),
    # @@MANUAL-REVIEW
])

# Binding headwords whose MANUAL entry deliberately departs from a binding tag (headword: reason).
TAG_CHANGED = {}

# Binding headwords whose MANUAL entry adds a sense with values the binding senses do not list (headword: reason).
NEW_SENSE = {
    # ---- sample ----
    'vatthu': "pi-4 basis «အကြောင်း» (not attested in pi-5); «ငုတ်တို» is the palm stump of tālāvatthukata in the "
              "arahant formula (^5-260, ^5-310 …), not a topic",
    'vādī': "pi-4 one who speaks «ပြောသော» kept; «မိမိဘက် / တစ်ဖက်သား» are the parties sakavādī / paravādī of the "
            "question notes (^5-1, ^5-2, ^5-344 …; map-harmonise §E)",
    'vata': "pi-1 vows «အကျင့်ဝတ်» kept (sīlabbata); «အမှန်ပင်» is the emphatic particle of 'vata re' (^5-1 …; "
            "kept sense difference, brief)",
    'gati': "pi-2 rebirth realm «လားရာ (ဘဝ)» kept; «သွားလာခြင်း» is the access of monks to a border region, 'yattha "
            "natthi gati bhikkhūnaṃ' (^5-271)",
    'upādā': "pi-3 derived «မှီ၍» kept (upādāpaññatti); «စွဲလမ်းမှု» is the grasping of anupādāparinibbāna (^5-125 …, "
             "mapper rule 8)",
    'purisa': "pi-4 man «ယောက်ျား» and pi-2 person «လူ» kept; «သူတော်ကောင်း» is the member of sappurisa (^5-480), as "
              "pi-4 puriso",
    'vāda': "pi-1 doctrine «ဝါဒ» kept (vādayutti); «ပြောခြင်း» is the speaking of musāvāda (^5-546)",
    # @@NEW-SAMPLE
    # ---- full run ----
    # ---- UNRESOLVED headwords ----
    'pada': "pi-4 items «ပုဒ်» kept (Padasodhanakathā); «လှမ်း» is the step of sattapadavītihāra, the seven steps of "
            "the newborn bodhisatta (^5-401)",
    'dhamma': "pi-4 phenomena «သဘောတရား» and teaching «တရား» kept («ဓမ္မ» the loan of dhammacakka, dhammavinaya); "
              "«အရာ» is the field of sadhammakusala / paradhammakusala (^5-312, ^5-316, ^5-320 …)",
    'vaṇṇa': "pi-4 praise / beauty (not attested in pi-5); «အသွင်» is the guise of Arahantavaṇṇakathā (^5-31-2-1-0), "
             "an outward look assumed",
    'kāyo': "pi-2 physical body «ကိုယ်» kept; «အပေါင်း» is the troop of asurakāyo (^5-504)",
    'dhammaṃ': "pi-4 mind-object «သဘောတရား» and teaching «တရား» kept; «အကျင့်» is methunaṃ dhammaṃ, sexual intercourse "
               "(^5-901, ^5-909; map-harmonise §B one sense per segment)",
    'āhāro': "pi-4 food «အစာ» and pi-2 nutriment «အာဟာရ» kept; «ဆိုခြင်း» is the uttering of dukkhāhāro (^5-334, "
             "^5-353), not pi-4's taking up of rivalry «ဆောင်ခြင်း»",
    'kula': "pi-4 supporting households / royal household (not attested in pi-5); «အမျိုးကောင်း» is the good family of "
            "kulaputto (^5-387)",
    # ---- REVIEW batch 1 ----
    'para': "pi-4 others «သူတစ်ပါး» kept; «ကျော်» is the 'more than' of parosahassa (^5-402)",
    'citta': "pi-4 mind «စိတ်» kept; «အရောင်စုံ» is the variegated of cittavaṇḍa (^5-387)",
    'dukkhaṃ': "pi-4 noble truth «ဒုက္ခ» and pi-2 painful feeling «နာကျင်သော» kept; «ဆင်းရဲ» is the misery of "
               "āpāyikaṃ dukkhaṃ (^5-157 …), as pi-2 dukkha 'misery'",
    'eka': "pi-4 one «တစ်စေ့» kept; «တူညီသော» is 'one and the same', Ekādhippāyakathā (^5-31-1-0)",
    'aññā': "pi-4 final knowledge kept; «တခြားစီ» is the feminine pronoun 'other' (^5-221; map-harmonise §E)",
    'paccaya': "pi-2 condition kept; «မှီသော» is the reliance of aparappaccaya (^5-232), as paccayo",
    'jāti': "pi-4 birth kept (also rebirth); «မျိုး» is the kind of Gandhajātikathā (^5-26-4-1-0)",
    'āneñja': "pi-4 imperturbable kept; «အာနေဉ္ဇသပ္ပာယ» is the cited sutta title (^5-834)",
    'Saṃkhittaṃ': "pi-2 shrunken mind kept; «အကျဉ်းချုပ်» is the editorial 'shortened text' note (^5-53 …; "
                  "map-harmonise §A 1)",
    'lohitaṃ': "pi-2 blood «သွေး» kept; «အနီ» is the colour red (^5-97)",
    'kamma': "pi-4 deeds «ကံ» kept; «အလုပ်» is the busy work of kammārāmatā (^5-267)",
    'dhammānaṃ': "pi-2 phenomena kept; «တရား» is the four qualities of catunnaṃ dhammānaṃ (^5-281)",
    'atta': "pi-2 self «အတ္တ» kept; «ကိုယ်» is the individual existence of attabhāva (^5-381 …; map-harmonise §B)",
    # ---- REVIEW batch 2 ----
    'gandhā': "pi-2 odours «အနံ့» kept; «အပုပ်နံ့» is the figurative stench of nirāmagandhā (^5-281)",
    'dhammo': "pi-4 'having the nature of' kept; pi-5 adds the teaching «တရား» (sataṃ dhammo, dhammo desito ^5-485, "
              "^5-804 …), a phenomenon «သဘောတရား» (^5-666 …) and methuno dhammo «အကျင့်» (^5-908)",
    'uppāda': "pi-2 arising kept; «ထွက်စေခြင်း» is the shedding of blood, ruhiruppāda (^5-546)",
    'pādā': "pi-2 bases «ပါဒ်» kept; «ခြေ» is the feet (^5-293, ^5-691)",
    'yogo': "pi-4 yoke «ထမ်းပိုး» kept; «အားထုတ်မှု» is the effort of pubbayogo (^5-354, ^5-400)",
    'āma': "pi-2 raw flesh «အစိမ်း» kept; «ဟုတ်ပါသည်» is the assent āma (^5-281)",
    'katvā': "pi-2 having performed kept (kammaṃ katvā); «အကြောင်းပြု၍ / မှတ်ယူ၍» is the idiom iti katvā 'on the "
             "ground that' (^5-299, ^5-282 …)",
    'gatā': "pi-4 gone kept; «အာရုံပြုသော» is the 'directed to' of kāyagatāsati (^5-301, ^5-303)",
    'assa': "pi-4 his «ထိုသူ» kept; «မြင်း» is the horse (assaratana ^5-303 …; kept sense difference, brief)",
    'vādo': "pi-2 speaking kept; «ဝါဒ» is the school of sabbatthivādo (^5-306)",
    'sukka': "pi-4 white «ဖြူစင်သော» kept; «သုက်» is the semen of sukkavissaṭṭhi (^5-307 …; kept sense difference, "
             "brief)",
    'ghātako': "pi-4 killer «သတ်သူ» kept; «ဖျက်ဆီးရမည့်» is the raider of gāmaghātako (^5-908)",
    # ---- REVIEW batch 3 ----
    'gandhaṃ': "pi-4 smell «အနံ့» kept; «နံ့သာ» is the perfume of the gift lists (^5-481, ^5-658, ^5-779, ^5-901)",
    'setu': "pi-2 bridge «တံတား» kept; «သေတု» is the name Setu māṇavo (^5-387)",
    'bhūtā': "pi-2 great elements kept; «ဖြစ်စေနိုင်သော» is the 'become' of vasībhūtā (^5-744, ^5-746)",
    'vihāra': "pi-2 abiding «နေထိုင်ရာ» kept; «ကျောင်း» is the monastery of ārāmavihāra (^5-802)",
    'uppāditaṃ': "pi-2 made to flow (blood) kept; «ဖြစ်ပေါ်စေခဲ့ပြီးသော» is remorse produced, kukkuccaṃ uppāditaṃ "
                 "(^5-660)",
    # ---- REVIEW batch 4 (each: binding sense not attested in pi-5 unless said; the pi-5 meaning differs) ----
    'buddho': "pi-3 'grasped' (subuddho) not attested; «ဘုရား / ဘုရားရှင်» is the Buddha (^5-398 …)",
    'maya': "pi-4 excrement (gomaya) not attested; «ဖြစ်သော» is the suffix -maya 'consisting in' (^5-15-5-1-0)",
    'dakkhiṇaṃ': "pi-2 southern not attested; «အလှူ» is the religious gift (^5-25-6-1-0 …)",
    'iddhiṃ': "pi-2 success «တန်ခိုး» not attested; «ဣဒ္ဓိ» is supernormal power, iddhiṃ vikubbati (^5-193 …)",
    'antarā': "pi-4 midway / pi-3 intermediate sections not attested; «ကြား» is the 'between' of antarābhava "
              "(^5-505 …)",
    'atthato': "pi-2 'as having essence' not attested; «အဓိပ္ပာယ်» is 'in terms of meaning' (^5-236, ^5-313)",
    'kusalassa': "pi-2 wholesome not attested; «ကျွမ်းကျင်သော» is skilled, sadhammakusalassa (^5-312 …)",
    'hetuka': "pi-1 rooted not attested; «အကြောင်း» is the cause of ahetukavāda (^5-296)",
    'āsayo': "pi-2 disposition not attested; «သိုလှောင်ရာ» is the bodily receptacle (^5-309)",
    'nāma': "pi-4 particle / pi-2 mentality not attested; «အမည်» is the name of nāmagotta (^5-317 …)",
    'samitaṃ': "pi-2 calmed not attested; «အစဉ်တစိုက်» is the adverb 'continually' (^5-397 …)",
    'vivaṭṭa': "pi-4 world-expansion not attested; «ဖွင့်လှစ်ပြီးသော» is vivaṭṭacchada (^5-402)",
    'anto': "pi-4 within not attested; «အဆုံး» is the end of cāturanto (^5-402)",
    'dhammena': "pi-2 'by a painful thing' not attested; «တရား» is 'righteously' (^5-402)",
    'saraṇaṃ': "pi-2 'involving strife' not attested; «ကိုးကွယ်ရာ» is the refuge (^5-445 …)",
    'citto': "pi-4 'of mind' kept; «စိတ္တ» is the name Citta the householder (^5-404)",
    'pariyāya': "pi-4 set turn not attested; «ပိုင်းခြား သိခြင်း» is the comprehending of cetopariyāya (^5-378)",
    'upamā': "pi-4 'like' (compound final) not attested; «ဥပမာ» is the noun simile (^5-335)",
    'sā': "pi-4 canine not attested; «ထို» is the feminine pronoun (^5-472)",
    'cetasiko': "pi-2 'belonging to the mind' not attested; «စိတ်၏ အဖော်» is the mental factor, cetasiko dhammo "
                "(^5-475 …), as pi-2 cetasikaṃ",
    'dahati': "pi-2 'regards oneself' not attested; «လောင်သည်» is 'burns' (^5-487)",
    'santo': "pi-2 calm not attested; «သူတော်ကောင်း» is the good people (^5-491)",
    'samiddhi': "pi-2 success not attested; «သမိဒ္ဓိ» is the monk's name (^5-539)",
    'kāmo': "pi-2 sensual pleasure not attested; «လို» is the compound final 'desirous of' (^5-564, ^5-566)",
    'Rūpataṇhā': "pi-2 craving for the fine-material sphere not attested; «အဆင်းအရောင်ကို တပ်မက်မှု» is craving for "
                 "visible forms (^5-676 …)",
    'kappo': "pi-2 fitting not attested; «ကမ္ဘာ» is the aeon (^5-742)",
    'samāhito': "pi-4 composed not attested; «ပြည့်စုံသော» is 'furnished with', paññāsīlasamāhito (^5-798)",
    'veḷu': "pi-2 bamboo not attested; «ဝေဠုဝန်» is the name Veḷuvana (^5-802)",
    'yuttaṃ': "pi-4 fittingly not attested; «ကပ်ထားသော» is 'harnessed' (^5-870)",
    'pattaṃ': "pi-4 'having reached' not attested; «သပိတ်» is the bowl (^5-886)",
    'samaye': "pi-2 'at that time' not attested; «အယူဝါဒ» is the doctrine of satthusamaye (^5-918)",
    'seyyaṃ': "pi-2 lying down not attested; «အိပ်ရာ» is the bed of the gift lists (^5-481)",
    # @@NEW-FULL
}

# Several Burmese values under one sense, or a value the binding sense does not list, checked by hand
# (variants or synonyms of one meaning, or the pi-5 text's own word for the binding meaning).
LUMP_OK = {
    # ---- sample ----
    'kathā',         # «ဆွေးနွေးချက်» (headings) / «ဆွေးနွေးခြင်း» (title ^5-0): one lemma = pi-4 'talk or treatise'
    'puggalo upalabbhati',   # «ပုဂ္ဂိုလ် … တွေ့ရသည်» / «ပုဂ္ဂိုလ်ကို တွေ့ရသည်»: one phrase, gapped or glued (rule 10)
    'suddha',        # «ရိုးရိုး» (Suddhasaccikaṭṭho) / «သက်သက်» (^5-233): plain, nothing but (map-harmonise §A 6)
    'suddhika',      # «ရိုးရိုး» = pi-1 «သက်သက်»: plain, unmixed version
    'catukka',       # «လေးပါး» = pi-4 «လေးမျိုးတွဲ»: the fourfold
    'naya',          # «နည်း» = pi-3 «ခွဲနည်း»: mode, method
    'niggahetabbe',  # «ချေပရမည့်» / «ချေပရသည်»: one gerundive, attributive vs predicate
    'brahma',        # «မြတ်သော» (ch10) = «မြင့်မြတ်သော»: the text's variant (map-harmonise §A 31)
    'brahmacariya',  # «မြတ်သော အကျင့်» (ch10) = «မြင့်မြတ်သော အကျင့်» (map-harmonise §A 31)
    'odhiso',        # «အပိုင်းအပိုင်း» = pi-2 «အပိုင်းအခြားဖြင့်»: piecemeal, partially
    # @@LUMP-SAMPLE
    # ---- full run: REVIEW headwords checked by hand ----
    # batch 1
    'ñāṇa',          # «သိခြင်း» of aññāṇa (positive part) = pi-4 knowledge «ဉာဏ်»
    'khandha',       # pi-2 stem «ပင်စည်» added after pi-4 aggregate (binding pi-2 sense)
    'dukkha',        # pi-2 misery «ဆင်းရဲ» added after the pi-4 senses (binding pi-2 sense)
    'Sabbadā',       # «အချိန်တိုင်း» / «အမြဲ»: at all times, synonyms
    'samāpatti',     # «သမာပတ်» / «ဈာန် ဝင်စားခြင်း» = pi-2 «ဈာန် ဝင်စားရာ»: meditative attainment
    'dhātu',         # pi-2 realm «ဘုံ» added after pi-4 element (binding pi-2 sense)
    'sattama',       # «ခုနစ်ကြိမ်မြောက်» = pi-3 «သတ္တမ»: the ordinal seventh
    'dhātuyā',       # pi-2 realm «ဘုံ» / pi-3 element «ဓာတ်» (binding senses)
    'rūpaṃ',         # pi-4 visible form / pi-3 matter (binding senses)
    'Aññaṃ',         # «တခြားစီ» / «အခြား» = pi-2 «တခြား» (map-harmonise §A 5)
    'ñāṇaṃ',         # pi-4 «သိခြင်း» / pi-2 «ဉာဏ်» under the same tag
    'maggo',         # pi-4 way «လမ်း» / pi-3 path «မဂ်» (binding senses)
    'magga',         # pi-4 path «မဂ်» / pi-2 way «လမ်း» (binding senses)
    'samaṅgissa',    # «ရရှိထားသော» = «ပြည့်စုံသော»: possessing
    'hetu',          # pi-2 roots «အမြစ်» added after pi-4 cause (binding pi-2 sense)
    'dhammaṭṭhitatā',   # «သဘောတရားတို့၏ တည်နေခြင်း သဘော» / «တရား၏ တည်ရှိခြင်း»: one fixity, the text's two wordings
    'mano',          # «စိတ်» of manosaṅkhāra (^5-742) = mind
    'du',            # «ဆိုးသော» (duggati) / «နံစော်သော» (duggandha): the prefix 'bad, ill-'
    'rāga',          # «တပ်မက်မှု» (asātarāga ^5-21-8-1-0) = «ရာဂ» (map-harmonise §A 3)
    'taṇhā',         # «တဏှာ» (^5-75) = «တပ်မက်မှု» (map-harmonise §A 3)
    'añño',          # «တခြားစီ» / «အခြား» / «တခြား»: other (map-harmonise §A 5)
    'satta',         # «အသညသတ်» of asaññasatta: the beings, one Burmese word for the compound (map-harmonise §F 10)
    'maggaṃ',        # pi-4 path «မဂ်» / pi-2 way «လမ်း» (binding senses)
    'bhuñjati',      # «ဘုဉ်းပေးတော်မူသည်» = «စားသည်», the honorific of the Buddha's eating
    'phalaṃ',        # pi-4 fruit / pi-2 fruition «ဖိုလ်» (binding senses)
    'mahapphalaṃ',   # «အကျိုး ကြီးမားသော» / «ကြီးမားသော အကျိုး»: one phrase, two orders
    'accanta',       # «အပြီးအပိုင်» / «အဆုံးစွန်» / «လုံးဝ»: completely, to the very end
    'adhippāya',     # «အလိုအတိုင်း» / «ရည်ရွယ်ချက်»: will, purpose
    'issariya',      # «မိမိ၏ အစွမ်း» / «အစိုးရခြင်း»: lordship, power
    'jāto',          # «ပေါ်ပေါက်သော» / «မွေးဖွားလာသော» / «ဖွားမြင်တော်မူ(ခဲ့)သော» = pi-2 born, come into being
    'jāte',          # «တစ်မျိုးတည်းမှ ဖြစ်သော» / «မျိုး»: of a kind
    'sattānaṃ',      # «အသညသတ်» of asaññasattānaṃ (as satta)
    'hoti',          # pi-2 exists «ရှိသည်» added after pi-4 is (binding pi-2 sense)
    'bhijjati',      # «ပျက်သည်» / «ပြိုကွဲသည်»: breaks up
    'samādhiṃ',      # «တည်ကြည်ခြင်း» = «သမာဓိ»: concentration
    'sammā',         # binding senses (pi-4 / pi-3)
    'upacchedo',     # «ပြတ်ခြင်း» / «ဖြတ်တောက်ခြင်း» = pi-2 «ပြတ်စဲခြင်း»: severance
    'vaṭṭa',         # «သံသရာ စက်ဝန်း» / «ဝဋ်»: the round
    'sayaṃ',         # «မိမိ» (sayaṃkataṃ) = «ကိုယ်တိုင်»: by oneself
    'mātā',          # «မိဘ» of mātāpitaro (^5-491): one Burmese word for both members = mother
    'yugā',          # «အစုံ» / «အတွဲ»: pairs (map-harmonise §A 28)
    'pātubhavanti',  # «ပေါ်ပေါက်သည်» / «ထင်ရှား ပေါ်လာသည်» = pi-2 «ထင်ရှားလာသည်»
    'pātubhāvā',     # «ပွင့်ပေါ်ခြင်း» / «ထင်ရှား လာခြင်း»: manifestation
    'pajānāti',      # «သိသည်» = «ကွဲပြားစွာ သိသည်»: knows
    'dhammesu',      # pi-4 teachings / pi-2 phenomena (binding senses)
    'uppajjati',     # «ပေါ်ပေါက်(လာ)သည်» = pi-2 «ဖြစ်ပေါ်သည်»: arises
    # batch 2
    'puñjo',         # «အစုအပုံ» = pi-2 «ပုံ»: a heap
    'tasmā',         # «သောကြောင့်» = «ထို့ကြောင့်»: therefore
    'bāla',          # «မိုက်မဲသော» / «လူမိုက်»: foolish, a fool
    'paññāpeti',     # «သတ်မှတ်ဖော်ပြသည်» / ch1's «ပညတ်သည်» (map-harmonise §B): declares
    'dhamme',        # pi-4 life / pi-2 teaching and phenomena (binding senses)
    'rāgo',          # «တပ်မက်မှု» of asātarāgo = «ရာဂ» (map-harmonise §A 3)
    'arahato bhāvito',   # the members in either order across «…» (map-harmonise §B construction)
    'thero',         # «မထေရ်» = pi-4 «ထေရ်» (map-harmonise §A 16)
    'iṭṭhā',         # spacing / «နှစ်သက်ဖွယ်» = «လိုလားဖွယ်ကောင်းသော» (map-harmonise §A 10, 23)
    'phassā',        # «အတွေ့» = «တွေ့ထိမှု»: contacts
    'apacinitvā',    # «ဖြိုဖျက်၍» / «ဖျက်ဆီး၍»: the same passage in two wordings (map-harmonise §A 26)
    'okkamituṃ',     # «သက်ဆင်းသည်» / «မသက်ဆင်းနိုင်» = pi-4 «သက်ဆင်းရန်» (map-harmonise §F 4)
    'mātu',          # «မယ်တော်» = «အမိ», the honorific of the Buddha's mother (^5-401)
    'attamanā',      # «နှစ်သက်သော» / «ဝမ်းမြောက်သည်» = pi-2 «စိတ်ကျေနပ်သည်»: glad
    'patta',         # binding senses (pi-4 bowl / a later binding sense)
    'uppajjanti',    # «ပေါ်ပေါက်သည်» = «ဖြစ်ပေါ်သည်»: arise
    'uppannaṃ',      # «ပေါ်ပေါက်ခဲ့သော» = «ဖြစ်ပေါ်ပြီးသော»: arisen
    'sāvaka',        # «သာဝက» (sāvakayuga) = «တပည့်»: disciple
    'abhisambuddho', # «ဘုရား ဖြစ်တော်မူသော» / «… အပြည့်အဝ သိမြင်တော်မူခဲ့သော»: fully awakened
    'yugaṃ',         # «အစုံ» / «နှစ်ပါး»: a pair
    'sāvakayugaṃ',   # «တပည့် အစုံ» / «အဂ္ဂသာဝက နှစ်ပါး»: the pair of chief disciples
    'cakkaṃ',        # «စကြာ» (dhammacakka) = pi-2 «တရားစက်» (map-harmonise §A 12)
    'aṭṭhena',       # «အနက်» / «အကြောင်း» (kenaṭṭhena): in the sense of
    'upasampajja',   # «ပြည့်စုံစွာ ဝင်ရောက်၍» / «ပြည့်စုံစေ၍» = pi-4 «ဝင်စား၍»: having entered upon
    'paṭiladdho',    # «ရရှိပြီးသော» / «ရသော»: acquired
    'abhabbo',       # «မထိုက်တန်» / «မစွမ်းနိုင်»: unfit, unable (map-harmonise §F 4)
    'dassana',       # «အမြင်» (dassanasampadā) = pi-4 «သိမြင်သော»: seeing, vision
    'kiñci',         # «တစ်စုံတစ်ရာ» / «မှန်သမျှ»: anything at all
    'sañjātaṃ',      # the text's wordings of the jāta series (map-harmonise §A 14)
    'jātaṃ',         # «ပေါ်ပေါက်သော» (sahajātaṃ) = pi-2 «ဖြစ်ပေါ်သော»
    'nibbattaṃ',     # the text's wordings of the jāta series (map-harmonise §A 14)
    'ajātaṃ',        # «မမွေးဖွားသေးသော» = «မဖြစ်သေးသော» (map-harmonise §A 14)
    'nandī',         # «နှစ်သက်မှု» / «ပျော်မွေ့မှု» = pi-4 «နှစ်သက်သော»: delight
    'paṇītaṃ',       # «မြတ်ခြင်း» (hīnappaṇītaṃ) = «မွန်မြတ်သော»: refined
    'vādā',          # pi-4 speaking / pi-2 doctrines (binding senses)
    'Yaṃ kiñci',     # «မှန်သမျှ» / «အကြင်» / «ဟူသမျှ» = pi-2 «မည်သည့် … မဆို»: whatever
    'paṭilabhanti',  # «ရရှိသည်» / «ရသည်»: acquire
    'sikkhāya',      # «သိက္ခာ» (^5-648) = «ကျင့်စဉ်»: the training
    'Aṭṭhānaṃ',      # «အကြောင်း မဟုတ်» = pi-4 «မဖြစ်နိုင်သော အကြောင်း»: no possibility
    'pāṇaṃ',         # «သတ္တဝါ» / «သူ့အသက်» (pāṇaṃ hane): a living being, its life
    'hareyya',       # «လုယူသည်» / «တိုက်သည်»: would carry off (map-harmonise §A 27)
    'pharusaṃ',      # pi-4 harsh speech / pi-2 rough (binding senses)
    'nillopaṃ',      # «လုယက်» / «ဥစ္စာ» / «ဓားပြ»: plunder, the same list (map-harmonise §A 27)
    'bhabbo',        # «ထိုက်တန်သော» / «သိနိုင်သော»: capable
    'ñāṇa niṭṭhitā', # «သိခြင်း … / ဉာဏ် … ပြီးဆုံးသော»: the heading phrase with the segment's word
    'cariyaṃ',       # «ကျင့်ဝတ်» (brahmacariyaṃ) = «အကျင့်»
    'samāpannassa',  # «(သမာပတ်ကို) ဝင်စား(နေ)သော» = pi-2: of one who has entered
    'samāpattiṃ samāpannassa',  # the members glued or gapped (rule 10)
    'nevasaññānāsaññāyatanaṃ samāpannassa',  # the members in either order (rule 10, G2)
    'catutthaṃ samāpannassa',   # the members in either order (rule 10, G2)
    # batch 3
    'khaṇo',         # «ခဏ» / «အခါ» (^5-338): the moment, the occasion
    'soḷasa sahassāni',  # the members in either order across «…» (rule 10)
    'viloketi',      # «ဘေးသို့ / ဝေ့ဝဲ ကြည့်သည်», «ကြည့်သည်» = pi-4 'looks around'
    'phoṭṭhabbaṃ',   # «အတွေ့အထိ» = «အထိအတွေ့»: the tangible
    'manāpā',        # «နှစ်သက်ဖွယ် ကောင်းသော» / «စိတ်နှင့် တွေ့သော» = pi-4 «စိတ်တွေ့သော»: pleasing
    'amanāpa',       # «စိတ်နှင့် မတွေ့ဖွယ်» / «မနှစ်သက်ဖွယ်»: unpleasing
    'dānaṃ',         # «ဒါန» = «အလှူ / ပေးလှူခြင်း»: the gift, giving
    'viveka',        # «ဆိတ်ငြိမ်ခြင်း» = pi-4 «ကင်းဆိတ်ခြင်း»: seclusion
    'sikkhā',        # «ကျင့်ခြင်း» (anupubbasikkhā) = «သိက္ခာ»: the training
    'voharati',      # «ပြောဆို သုံးနှုန်းသည်» / «သုံးနှုန်းပြောသည်»: expresses
    'hīna',          # «ယုတ်ခြင်း» / «ယုတ်လျော့သော» / «ချို့ယွင်းသော» = pi-4 «ယုတ်ညံ့သော»: low, deficient
    'akkhātā',       # «ဟောကြားသူ» = «ပြောကြားသော»: one who announces
    'vidū',          # «နားလည်သော» / «သိသော» = pi-4 «သိတော်မူသော»: one who knows
    'cuti',          # «စုတေ» / «စုတိ» = «သေခြင်း»: passing away
    'vadāmi',        # «ဆိုသည်» / «ဟောသည်»: I say (by speaker, map-harmonise §A 9)
    'uttamo',        # «အမြတ်ဆုံး» = pi-4 «အထွတ်အထိပ်»: supreme
    'anuttaraṃ',     # «အမြတ်ဆုံး» = pi-2 «ထိုထက် သာလွန်သည် မရှိသော»: unsurpassed
    'upapattiyā',    # «ပြန်လည် ဖြစ်ပေါ်သော / ခြင်း» = pi-1 «ဖြစ်ပေါ်ရန်»: rebirth (map-harmonise §F 14)
    'uppādā',        # «ဖြစ်ပေါ်သော / ခြင်း», «ပွင့်ပေါ်သည်» = pi-2 «ဖြစ်ပေါ်ရာ»: arising
    'seṭṭho',        # «အမြတ်ဆုံး» / «မြတ်သော» = pi-4 «အကောင်းဆုံး»: best
    'uddisi',        # «ကိုးကွယ်ခဲ့သည်» / «ညွှန်ပြခဲ့သည်»: named (another teacher), the same phrase
    'tapaṃ',         # «ပြင်းထန်သော / ခြိုးခြံသော အကျင့်»: austerity
    'akāsi',         # «ကျင့်ခဲ့သည်» / «ပြုခဲ့သည်»: did, performed (map-harmonise §B)
    'phusanti',      # «ထိသည်» / «တွေ့ထိသည်»: touch
    'niyamo',        # «ကျိန်းသေမှု» / «သေချာသော လမ်းကြောင်း»: certainty
    'mahābhūtā',     # «မဟာဘုတ်» = pi-2 «မူလဓာတ်ကြီး»: the great elements
    'abyābajjhaṃ',   # «ညှဉ်းဆဲမှု ကင်းခြင်း» / «မဆင်းရဲစေတတ်သော»: non-affliction
    'annaṃ',         # «ထမင်း» / «အစာ»: food
    'ārāma',         # «ကျောင်း» / «ဥယျာဉ်» / «အရံ»: park, monastery park
    'bhojanīyaṃ',    # «ဘောဇဉ်» / «စားဖွယ်» (map-harmonise §A 27)
    'parakataṃ sukhadukkhaṃ',   # the phrase glued or gapped (rule 10)
    'atthāya',       # «အကျိုး» / «အတွက်»: for the sake of (attano / parassa atthāya)
    'saṃvattaniyaṃ', # «ပို့ဆောင် / ဖြစ်စေ / ရောက်စေတတ်သော»: conducive (map-harmonise §A 26)
    'adhipacca',     # «အကြီးအကဲ ဖြစ်ခြင်း» / «အုပ်ချုပ်ခြင်း»: sovereignty
    'paccati',       # «ကျက်သည်» / «ပူလောင်ရသည်»: is tormented in hell (^5-501, ^5-657)
    'āyu',           # «အသက်» = pi-2 under the same tag
    'jātā',          # «ပေါ်ပေါက်သော» / «ဖြစ်ပေါ်သော» = pi-2 born, come to be
    'jāyiṃsu',       # «ဖြစ်သည်» / «မွေးဖွားသည်»: came to birth
    'bhāvitā bahulīkatā',   # the members in either order across «…» (rule 10)
    'ekanta',        # «တစ်ထစ်ချ» = pi-4 «လုံးဝ»: wholly
    'parinipphannaṃ',   # the text's three wordings (map-harmonise §A 24)
    'sañcetanikānaṃ',   # «ရည်ရွယ်၍» / «စေ့ဆော်၍»: the same passage in two wordings (map-harmonise §A 26)
    'voropitā',      # «သတ်ခဲ့ပြီးသော» = pi-2 «ချခံရသော»: deprived of life (map-harmonise §A 29)
    'niyato',        # pi-4 NAME / adjective under the same tag (mapper P1)
    'yoniṃ',         # «ဘဝ» / «ဘုံ» / «မွေးဖွားရာ အမျိုးအစား» of tiracchānayoniṃ: one mode of generation
    'upapajjeyya',   # «ပြန်လည် ဖြစ်ပေါ်သည်» = pi-2 «ရောက်သည်»: would be reborn
    'seyyathidaṃ',   # «ယင်းမှာ» = «ဆိုလိုသည်မှာ»: namely
    'diṭṭhadhamma',  # «ယခုဘဝ» = pi-2 «မျက်မှောက်ဘဝ»: this present life
    'rūpaṃ rūpāvacaraṃ',    # the members glued or separated (rule 10)
    'saṃvattaniyaṃ kammaṃ', # the same sutta phrase in two wordings (map-harmonise §A 26)
    'apacināti',     # «ဖြိုဖျက်သည်» / «ဖျက်ဆီးသည်» (map-harmonise §A 26)
    'ariyo aṭṭhaṅgiko',         # the members in either order (rule 10, G2)
    'ariyo aṭṭhaṅgiko maggo',   # the members in either order (rule 10, G2)
    # batch 5: one-stem groups and binding values checked by hand (rv-compact.txt)
    'Tena hi',  # «သို့ဖြစ်လျှင်» / «သို့ဖြစ်၍»: one lemma, the text's form / spacing (kept: form)
    'ṭhiti',  # «တည်ရာ» / «တည်ခြင်း» / «တည်နေသော» / «တည်တံ့ခြင်း»: one lemma, the text's form / spacing (kept: form), = the pi-2 sense
    'vimutti',  # «လွတ်မြောက်ခြင်း»: one meaning, = the pi-4 sense
    'upagata',  # «ရောက်သွားသော» / «ရောက်သော»: one lemma, the text's form / spacing (kept: form)
    'samannāgata',  # «ပြည့်စုံသော» / «ပြည့်စုံခြင်း»: one lemma, the text's form / spacing (kept: form)
    'cetasika',  # «စိတ်၏ အဖော် ဖြစ်သော သဘောတရား» / «စိတ်၏ အဖော်»: one lemma, the text's form / spacing (kept: form)
    'aṭṭhaka',  # «ရှစ်ပါးအစု»: one meaning, = the pi-4 sense
    'arūpa',  # «ရုပ်မရှိသော» / «ရုပ် မဟုတ်သော»: binding senses of pi-4 and a later binding file
    'arūpadhātu',  # «ရုပ်မရှိသော ဘုံ» / «ရုပ်မရှိသော ဓာတ်»: one lemma, the text's form / spacing (kept: form), = the pi-2 sense
    'dassāvī',  # «ရှုမြင်သော»: one meaning, = the pi-2 sense
    'Aññaṃ viññāṇaṃ',  # «သိစိတ် … တခြားစီ» / «သိစိတ်သည် တခြားစီ»: one phrase, glued or gapped (kept: construction)
    'kusalā',  # «ကုသိုလ်»: binding senses of pi-4 and a later binding file
    'ṭhitatā',  # «တည်နေခြင်း သဘော» / «တည်ရှိခြင်း»: one lemma, the text's form / spacing (kept: form)
    'aniccatā',  # «မမြဲခြင်း သဘော»: one meaning, = the pi-2 sense
    'sotindriyaṃ upalabbhati',  # «နား၏ စွမ်းရည်ကို တွေ့ရသည်» / «နား၏ စွမ်းရည် … တွေ့ရသည်»: one phrase, glued or gapped (kept: construction)
    'hitāya',  # «အကျိုး» / «အကျိုးစီးပွား»: one lemma, the text's form / spacing (kept: form), = the pi-4 sense
    'aññamañña',  # «အချင်းချင်း»: one meaning, = the pi-2 sense
    'vedayita',  # «ခံစားရခြင်း» / «ခံစားမှု»: one lemma, the text's form / spacing (kept: form), = the pi-2 sense
    'saññāvedayita',  # «မှတ်သိမှုနှင့် ခံစားရခြင်း» / «မှတ်သိမှုနှင့် ခံစားမှု»: one lemma, the text's form / spacing (kept: form)
    'upacaya',  # «စုဆောင်းမှု» / «စုဆောင်းခြင်း»: one lemma, the text's form / spacing (kept: form)
    'maccu',  # «သေခြင်း» / «သေမင်း»: binding senses of pi-3 and a later binding file
    'saṅgho dakkhiṇaṃ paṭiggaṇhāti',  # «သံဃာသည် အလှူကို ခံယူသည်» / «သံဃာသည် အလှူ … ခံယူသည်»: one phrase, glued or gapped (kept: construction)
    'paṭiggaṇhāti',  # «ခံယူသည်»: one meaning, = the pi-4 sense
    'dakkhiṇaṃ paṭiggaṇhāti',  # «အလှူကို ခံယူသည်» / «အလှူ … ခံယူသည်»: one phrase, glued or gapped (kept: construction)
    'saṅgho dakkhiṇaṃ visodheti',  # «သံဃာသည် အလှူကို စင်ကြယ်စေသည်» / «သံဃာသည် အလှူ … စင်ကြယ်စေသည်»: one phrase, glued or gapped (kept: construction)
    'dakkhiṇaṃ visodheti',  # «အလှူကို စင်ကြယ်စေသည်» / «အလှူ … စင်ကြယ်စေသည်»: one phrase, glued or gapped (kept: construction)
    'Buddhassa',  # «ဘုရား» / «ဘုရားရှင်»: one lemma, the text's form / spacing (kept: form)
    'sāmañña',  # «ရဟန်းအဖြစ်» / «ရဟန်း»: one lemma, the text's form / spacing (kept: form), = the pi-1 sense
    'tathatā',  # «ဟုတ်တိုင်းမှန်သော သဘော» / «ဟုတ်မှန်ခြင်း»: one lemma, the text's form / spacing (kept: form)
    'buddha',  # «ဘုရား»: one meaning, = the pi-2 sense
    'sassato',  # «ထာဝရ တည်မြဲသော»: one meaning, = the pi-2 sense
    'saṃvijjamāno',  # «ထင်ရှား ရှိနေသော»: one meaning, = the pi-4 sense
    'upapajjati',  # «ပြန်လည် ဖြစ်ပေါ်သည်»: one meaning, = the pi-2 sense
    'koci',  # «တစ်စုံတစ်ယောက်»: one meaning, = the pi-2 sense
    'puggalo sandhāvati',  # «ပုဂ္ဂိုလ် … ကူးသွားသည်» / «ပုဂ္ဂိုလ်သည် ကူးသွားသည်»: one phrase, glued or gapped (kept: construction)
    'karo',  # «ပြုသော» / «ပြုတော်မူသော»: one lemma, the text's form / spacing (kept: form), = the pi-4 sense
    'katānaṃ',  # «ပြုခဲ့သော» / «ပြုခဲ့»: one lemma, the text's form / spacing (kept: form)
    'nerayiko',  # «ငရဲ၌ ကျသော» / «ငရဲသား» / «ငရဲ၌ ကျမည့်»: one lemma, the text's form / spacing (kept: form)
    'samasamo',  # «အလွန် တူညီစွာ»: one meaning, = the pi-4 sense
    'vaya',  # «ပျက်စီး» / «ပျက်ခြင်း»: one lemma, the text's form / spacing (kept: form), = the pi-2 sense
    'virāga',  # «ပြယ်ပျောက်»: one meaning, = the pi-2 sense
    'rūpaṃ aniccaṃ',  # «ရုပ်သည် မမြဲသော» / «ရုပ် … မမြဲသော»: one phrase, glued or gapped (kept: construction)
    'puggalassa paññatti',  # «ပုဂ္ဂိုလ်၏ သတ်မှတ်ချက်» / «ပုဂ္ဂိုလ် … သတ်မှတ်ချက်»: one phrase, glued or gapped (kept: construction)
    'nirodhadhammaṃ',  # «ချုပ်ငြိမ်းတတ်သော သဘော … ရှိသော» / «ချုပ်ငြိမ်းခြင်း သဘော ရှိသော»: one lemma, the text's form / spacing (kept: form)
    'iṭṭha',  # «လိုလားဖွယ်» / «လိုလားအပ်သော»: one lemma, the text's form / spacing (kept: form)
    'aniṭṭha',  # «မလိုလားဖွယ်» / «မလိုလားအပ်သော»: one lemma, the text's form / spacing (kept: form)
    'vipariṇāmadhammā',  # «ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော ရှိသော» / «ဖောက်ပြန်ပြောင်းလဲခြင်း … သဘော ရှိသော»: one lemma, the text's form / spacing (kept: form), = the pi-2 sense
    'niruddhe',  # «ချုပ်ငြိမ်းသွားသော» / «ချုပ်ငြိမ်းသော» / «ချုပ်ငြိမ်းပြီးသော»: one lemma, the text's form / spacing (kept: form)
    'cakkhumā',  # «မျက်စိ ရှိသော»: one meaning, = the pi-4 sense
    'niruddhāya',  # «ချုပ်ငြိမ်းသွားသော» / «ချုပ်ငြိမ်းသော»: one lemma, the text's form / spacing (kept: form)
    'puggalānaṃ paññatti',  # «ပုဂ္ဂိုလ်၏ သတ်မှတ်ချက်» / «ပုဂ္ဂိုလ် … သတ်မှတ်ချက်»: one phrase, glued or gapped (kept: construction)
    'cavati',  # «စုတေသည်»: one meaning, = the pi-2 sense
    'jāyati',  # «မွေးဖွားသည်»: one meaning, = the pi-2 sense
    'kumārikā',  # «သူငယ်မ»: one meaning, = the pi-4 sense
    'yaṃ',  # «အကြင်အရာ»: one meaning (kept: none), = the pi-1 sense
    'Yo',  # «အကြင်သူ»: one meaning (kept: none), = the pi-1 sense
    'sāyati',  # «လျက်သည်»: one meaning, = the pi-2 sense
    'Mānusakaṃ',  # «လူ»: one meaning, = the pi-4 sense
    'karoti',  # «ပြုသည်» / «ပြုလုပ်သည်»: one lemma, the text's form / spacing (kept: form)
    'pathavī atthi',  # «မြေ … ရှိသည်» / «မြေ ရှိသည်»: one phrase, glued or gapped (kept: construction)
    'purisayugā',  # «လူ အစုံ» / «လူ အတွဲ»: one lemma, the text's form / spacing (kept: form)
    'parinibbute',  # «ပရိနိဗ္ဗာန် ပြုတော်မူပြီးသော» / «ပရိနိဗ္ဗာန် စံဝင်တော်မူပြီးသော»: one lemma, the text's form / spacing (kept: form)
    'uppādo',  # «ဖြစ်ပေါ်ခြင်း» / «ဖြစ်ခြင်း»: one lemma, the text's form / spacing (kept: form), = the pi-2 sense
    'parinibbuto',  # «ပရိနိဗ္ဗာန် ပြုတော်မူခဲ့သော» / «ပရိနိဗ္ဗာန် ပြုပြီးသော» / «ပရိနိဗ္ဗာန် ပြုတော်မူသော»: one lemma, the text's form / spacing (kept: form)
    'tiṭṭhati',  # «တည်သည်» / «တည်နေသည်»: one lemma, the text's form / spacing (kept: form), = the pi-4 sense
    'viharati',  # «နေသည်» / «နေတော်မူသည်»: the text's own word for the one meaning (kept: sense), = the pi-4 sense
    'dhammā',  # «သဘောတရား»: binding senses of pi-4 and a later binding file
    'nikkhamitvā',  # «ထွက်၍»: one meaning, = the pi-2 sense
    'bhagavā',  # «မြတ်စွာဘုရား»: one meaning, = the pi-4 sense
    'nirujjhamānaṃ',  # «ချုပ်ငြိမ်းသော» / «ချုပ်ငြိမ်းနေသော»: one lemma, the text's form / spacing (kept: form)
    'Ettāvatā',  # «ဤမျှဖြင့်»: binding senses of pi-4 and a later binding file
    'veti',  # «ပျက်ကွယ်သည်» / «ပျက်စီးသည်»: one lemma, the text's form / spacing (kept: form)
    'cakkhusamphasso',  # «မျက်စိ တွေ့ထိမှု»: one meaning, = the pi-2 sense
    'vedayitaṃ',  # «ခံစားရမှု»: one meaning, = the pi-2 sense
    'manosamphasso',  # «မနော တွေ့ထိမှု»: one meaning, = the pi-2 sense
    'dhuvo',  # «ခိုင်ခံ့သော»: one meaning, = the pi-2 sense
    'sammāsambuddho',  # «အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရား»: binding senses of pi-4 and a later binding file
    'bhattaṃ',  # «ထမင်း»: one meaning, = the pi-4 sense
    'nicca',  # «အမြဲ»: one meaning, = the pi-2 sense
    'anāgāmi',  # «အနာဂါမိ» / «အနာဂါမ်»: one lemma, the text's form / spacing (kept: form), = the pi-4 sense
    'sakadāgāmi',  # «သကဒါဂါမိ» / «သကဒါဂါမ်»: one lemma, the text's form / spacing (kept: form), = the pi-4 sense
    'saṇṭhāti',  # «တည်သည်»: one meaning, = the pi-4 sense
    'padhāna',  # «ကြိုးပမ်းအားထုတ်ခြင်း»: binding senses of pi-4 and a later binding file
    'nirodho',  # «ချုပ်ငြိမ်းခြင်း» / «ချုပ်သော»: one lemma, the text's form / spacing (kept: form), = the pi-4 sense
    'bhāvito',  # «ပွားများပြီးသော» / «ပွားများထားသော»: one lemma, the text's form / spacing (kept: form)
    'bojjhaṅgā bhāvitā',  # «ဗောဇ္ဈင်ကို ပွားများပြီးသော» / «ဗောဇ္ဈင်တို့ကို ပွားများပြီးသော»: one lemma, the text's form / spacing (kept: form)
    'kata',  # «ပြုပြီးသော» / «ပြုခဲ့သော»: binding senses of pi-4 and a later binding file
    'saṃyojano',  # «နှောင်ကြိုး»: one meaning, = the pi-4 sense
    'pariññātaṃ',  # «ပိုင်းခြား သိပြီးသော» / «ပိုင်းခြား သိခြင်း»: one lemma, the text's form / spacing (kept: form)
    'sacchikato',  # «မျက်မှောက်ပြုပြီးသော» / «မျက်မှောက် ပြုရသေးသော»: one lemma, the text's form / spacing (kept: form)
    'mutaṃ',  # «မှတ်ယူအပ်»: one meaning, = the pi-2 sense
    'aniṭṭhā',  # «မနှစ်သက်ဖွယ်»: one meaning, = the pi-2 sense
    'paṭicca uppajjati',  # «မှီ၍ … ဖြစ်ပေါ်သည်» / «မှီ၍ ဖြစ်ပေါ်သည်»: one phrase, glued or gapped (kept: construction)
    'ussineti',  # «စုပုံသည်» / «စုစည်းသည်»: the text's own word for the one meaning (kept: sense)
    'pariyuṭṭhito',  # «ထကြွခြင်းကို ခံရသော» / «ထကြွခြင်း ရှိသော»: one lemma, the text's form / spacing (kept: form)
    'visineti',  # «ဖြန့်ကြဲသည်» / «ဖြန့်ကျက်သည်»: one lemma, the text's form / spacing (kept: form)
    'payirupāsanti',  # «ဆည်းကပ်သည်»: binding senses of pi-4 and a later binding file
    'bhabbā',  # «သက်ဆင်းနိုင်သော»: one meaning, = the pi-2 sense
    'niyāmaṃ',  # «သေချာသော လမ်းကြောင်း» / «သေချာသော လမ်း»: one lemma, the text's form / spacing (kept: form), = the pi-4 sense
    'niyāmaṃ okkamituṃ',  # «သေချာသော လမ်းသို့ သက်ဆင်းသည်» / «သေချာသော လမ်းကြောင်းသို့ မသက်ဆင်းနိုင်»: one lemma, the text's form / spacing (kept: form)
    'abhabbā',  # «မသက်ဆင်းနိုင်»: one meaning, = the pi-2 sense
    'duppaññā',  # «ပညာ ညံ့သော»: one meaning, = the pi-4 sense
    'sammattaṃ',  # «မှန်ကန်ခြင်း»: one meaning, = the pi-4 sense
    'sambuddhā uppajjanti',  # «အမှန်ကို ကိုယ်တိုင် … သိမြင်တော်မူသော ဘုရားရှင်တို့ ပေါ်ပေါက်သည်» / «အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင် … ပွင့်သည်»: one lemma, the text's form / spacing (kept: form)
    'sammāsambuddhā',  # «အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင်» / «အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရား»: one lemma, the text's form / spacing (kept: form), = the pi-2 sense
    'pabbajati',  # «ရဟန်းပြုသည်» / «ရဟန်း ပြုသည်»: one lemma, the text's form / spacing (kept: form)
    'pavattitaṃ',  # «လည်စေတော်မူသော» / «လည်စေတော်မူခဲ့သော»: one lemma, the text's form / spacing (kept: form)
    'kāsāva',  # «သင်္ကန်း»: one meaning, = the pi-2 sense
    'paccekasambuddhā uppajjanti',  # «ပစ္စေကဗုဒ္ဓါတို့ ပေါ်ပေါက်သည်» / «ပစ္စေကဗုဒ္ဓါ … ပွင့်သည်»: one lemma, the text's form / spacing (kept: form)
    'paṭivedho',  # «ထိုးထွင်း သိမြင်ခြင်း» / «ထိုးထွင်း သိခြင်း»: one lemma, the text's form / spacing (kept: form), = the pi-4 sense
    'upapannassa',  # «ပြန်လည် ဖြစ်ပေါ်သော»: one meaning, = the pi-2 sense
    'pahīyanti',  # «ပယ်သည်» / «ပယ်ခံရသည်»: one lemma, the text's form / spacing (kept: form), = the pi-2 sense
    'arahatta',  # «ရဟန္တာ» / «ရဟန္တာ အဖြစ်»: one lemma, the text's form / spacing (kept: form), = the pi-4 sense
    'maggaṃ bhāveti',  # «မဂ်ကို ပွားများသည်» / «မဂ် … ပွားများသည်»: one phrase, glued or gapped (kept: construction), = the pi-2 sense
    'paṭivedhāya',  # «ထိုးထွင်း သိမြင်ရန်»: one meaning, = the pi-2 sense
    'sacchikiriyāya',  # «မျက်မှောက်ပြု»: one meaning, = the pi-4 sense
    'Arahattasacchikiriyāya',  # «ရဟန္တာ ဖိုလ်ကို မျက်မှောက်ပြုရန်» / «ရဟန္တာ အဖြစ်ကို မျက်မှောက်ပြုရန်»: one lemma, the text's form / spacing (kept: form)
    'sacchikata',  # «မျက်မှောက် ပြုရသေးသော»: one meaning, = the pi-2 sense
    'sakkāyadiṭṭhiṃ jahati',  # «ကိုယ်ကို အတ္တဟု ယူဆသော အယူ … စွန့်ပယ်သည်» / «ကိုယ်ကို အတ္တဟု ယူဆသော အယူကို စွန့်ပယ်သည်»: one phrase, glued or gapped (kept: construction)
    'kilese jahati',  # «ကိလေသာ … စွန့်ပယ်သည်» / «ကိလေသာတို့ကို စွန့်ပယ်သည်»: one lemma, the text's form / spacing (kept: form)
    'phusitvā viharati',  # «ထိ၍ နေသည်» / «ထိ၍ … နေသည်»: one phrase, glued or gapped (kept: construction)
    'upasampajja viharati',  # «ပြည့်စုံစွာ ဝင်ရောက်၍ နေသည်»: one meaning, = the pi-2 sense
    'samannāgato',  # «ပြည့်စုံသော»: binding senses of pi-4 and a later binding file
    'samudaya',  # «ဖြစ်ပေါ်ခြင်း» / «ဖြစ်ပေါ်တတ်သော»: one lemma, the text's form / spacing (kept: form), = the pi-4 sense
    'dassanena',  # «မြင်ခြင်း»: one meaning, = the pi-3 sense
    'oḷārikaṃ kāmarāgaṃ jahati',  # «ရုန့်ရင်းသော ကာမရာဂ … စွန့်ပယ်သည်» / «ရုန့်ရင်းသော ကာမရာဂကို စွန့်ပယ်သည်»: one phrase, glued or gapped (kept: construction)
    'virajaṃ',  # «မြူမှုန် ကင်းသော» / «မြူ ကင်းသော»: one lemma, the text's form / spacing (kept: form)
    'abhabba',  # «မစွမ်းနိုင်»: one meaning, = the pi-4 sense
    'diṭṭhī',  # «အယူ»: one meaning, = the pi-2 sense
    'avasesaṃ',  # «အကြွင်း»: one meaning, = the pi-1 sense
    'Arahatte',  # «ရဟန္တာ အဖြစ်» / «ရဟန္တာ ဖိုလ်»: one lemma, the text's form / spacing (kept: form)
    'samodhānaṃ',  # «ပေါင်းဆုံခြင်း»: one meaning, = the pi-2 sense
    'khīṇā',  # «ကုန်သော» / «ကုန်ခန်းပြီးသော»: one lemma, the text's form / spacing (kept: form)
    'abhiññāya',  # «ထူးကဲစွာ သိခြင်း» / «ထူးကဲစွာ သိ၍»: one lemma, the text's form / spacing (kept: form), = the pi-2 sense
    'satāni',  # «ရာပေါင်း»: one meaning, = the pi-2 sense
    'netti',  # «ကြိုး»: one meaning, = the pi-2 sense
    'vimuttiyā',  # «လွတ်မြောက်မှု» / «လွတ်မြောက်ခြင်း»: one lemma, the text's form / spacing (kept: form)
    'akkhāsi',  # «ဟောကြားတော်မူသည်» / «ဟောကြားတော်မူခဲ့သည်»: one lemma, the text's form / spacing (kept: form)
    'anuttarā',  # «အမြတ်ဆုံး»: one meaning, = the pi-3 sense
    'niruddhaṃ',  # «ချုပ်ငြိမ်းပြီးသော» / «ချုပ်ငြိမ်းပြီး»: one lemma, the text's form / spacing (kept: form), = the pi-2 sense
    'vipariṇataṃ',  # «ဖောက်ပြန်ပြောင်းလဲပြီးသော»: one meaning, = the pi-2 sense
    'abbhatthaṅgataṃ',  # «လုံးဝ ကွယ်ပြီးသော» / «လုံးဝ ကွယ်ပျောက်ပြီးသော»: one lemma, the text's form / spacing (kept: form), = the pi-2 sense
    'abhinibbattaṃ',  # «ထင်ရှားစွာ ဖြစ်မြောက်သော»: one meaning, = the pi-2 sense
    'vigataṃ',  # «ကင်းကွာပြီးသော» / «ကင်းပျောက်ပြီးသော»: one lemma, the text's form / spacing (kept: form), = the pi-2 sense
    'pātubhūtaṃ',  # «ထင်ရှား ပေါ်ပေါက်သော» / «ထင်ရှားလာပြီးသော»: one lemma, the text's form / spacing (kept: form), = the pi-2 sense
    'atītaṃ niruddhaṃ',  # «အတိတ်သည် ချုပ်ငြိမ်းပြီးသော» / «အတိတ် ချုပ်ငြိမ်းပြီးသော»: one phrase, glued or gapped (kept: construction)
    'atthaṅgataṃ',  # «ကွယ်ပြီးသော» / «ကွယ်ပျောက်ပြီးသော»: one lemma, the text's form / spacing (kept: form)
    'nirodhaṃ',  # «ချုပ်ငြိမ်းခြင်း» / «ချုပ်ငြိမ်းရာ ဈာန်» / «ချုပ်သော»: one lemma, the text's form / spacing (kept: form), = the pi-2 sense
    'anottappī',  # «ဒုစရိုက်ကို မကြောက်ရွံ့မှု ရှိသော»: one meaning, = the pi-2 sense
    'atīto moho',  # «အတိတ် မောဟ» / «အတိတ် … မောဟ»: one phrase, glued or gapped (kept: construction)
    'ādāna',  # «ယူခြင်း»: one meaning, = the pi-2 sense
    'sādhāraṇo',  # «ဆက်ဆံရသော» / «ဆက်ဆံသော»: one lemma, the text's form / spacing (kept: form)
    'gāma',  # «ရွာ»: one meaning, = the pi-4 sense
    'satthaṃ',  # «လက်နက်»: one meaning, = the pi-4 sense
    'upārambha',  # «အပြစ်တင် စွပ်စွဲခြင်း»: one meaning, = the pi-2 sense
    'pubbe',  # «ရှေး» / «ရှေးဦးစွာ»: one lemma, the text's form / spacing (kept: form)
    'saṅkhā',  # «ရေတွက်ခေါ်ဆိုချက်»: one meaning, = the pi-1 sense
    'āyatanaṃ',  # «အာရုံခံ နယ်ပယ်»: binding senses of pi-4 and a later binding file
    'cetanā',  # «စေ့ဆော်မှု»: binding senses of pi-4 and a later binding file
    'pātubhāvo',  # «ထင်ရှား လာခြင်း» / «ထင်ရှား ဖြစ်ပေါ်ခြင်း»: one lemma, the text's form / spacing (kept: form), = the pi-2 sense
    'visuddhiyā',  # «စင်ကြယ်သော» / «စင်ကြယ်ရန်»: one lemma, the text's form / spacing (kept: form), = the pi-2 sense
    'khāyita',  # «ခဲ»: one meaning, = the pi-2 sense
    'asita',  # «စား»: one meaning, = the pi-2 sense
    'vilepanaṃ',  # «နံ့သာပျောင်း» / «နံ့သာ လိမ်းဖွယ်»: one lemma, the text's form / spacing (kept: form)
    'sacchikataṃ',  # «မျက်မှောက်ပြုပြီးသော» / «မျက်မှောက် ပြုဖူးသော»: one lemma, the text's form / spacing (kept: form)
    'arahattaṃ',  # «ရဟန္တာ အဖြစ်» / «ရဟန္တာ ဖိုလ်»: one lemma, the text's form / spacing (kept: form)
    'anavakāso',  # «အခွင့် မဟုတ်»: one meaning, = the pi-2 sense
    'paripanthe',  # «လမ်း» / «လမ်းခရီး»: one lemma, the text's form / spacing (kept: form)
    'chindeyya',  # «ဖောက်ထွင်းသည်» / «ဖောက်သည်»: one lemma, the text's form / spacing (kept: form)
    'pisuṇaṃ',  # «ကုန်းချောစကား» / «ကုန်းတိုက်သော စကား»: one lemma, the text's form / spacing (kept: form), = the pi-4 sense
    'samphaṃ',  # «အကျိုးမဲ့ စကား» / «အကျိုးမဲ့» / «အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား»: one lemma, the text's form / spacing (kept: form)
    'pakato',  # «လွှမ်းမိုးခံရသော»: one meaning, = the pi-4 sense
    'gottaṃ',  # «အနွယ်»: one meaning, = the pi-2 sense
    'purisānaṃ',  # «ယောက်ျား»: one meaning, = the pi-2 sense
    'brahmacariyaṃ',  # «မြတ်သော အကျင့်»: binding senses of pi-4 and a later binding file
    'jānāti',  # «သိသည်» / «သိတော်မူသည်»: the text's own word for the one meaning (kept: sense), = the pi-4 sense
    'samāpattīsu',  # «သမာပတ်»: one meaning, = the pi-2 sense
    'Lokuttaraṃ jhānaṃ',  # «လောကကို ကျော်လွန်သော … ဈာန်»: one meaning, = the pi-1 sense
    'samuṭṭhānā',  # «ဖြစ်ပေါ်သော» / «ဖြစ်ပေါ်လာသော»: one lemma, the text's form / spacing (kept: form), = the pi-3 sense
    'niruddhā',  # «ချုပ်ငြိမ်းသွားသော»: one meaning, = the pi-2 sense
    'saññāvedayitanirodhaṃ',  # «မှတ်သိမှုနှင့် ခံစားရခြင်း ချုပ်ငြိမ်းရာ ဈာန်» / «မှတ်သိမှုနှင့် ခံစားမှု ချုပ်ငြိမ်းခြင်း»: one lemma, the text's form / spacing (kept: form)
    'ākāsānañcāyatanaṃ samāpannassa',  # «အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ် … သမာပတ်ကို ဝင်စားနေသော» / «အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်ကို ဝင်စားနေသော»: one lemma, the text's form / spacing (kept: form)
    'saññāvedayitanirodhaṃ samāpannassa',  # «မှတ်သိမှုနှင့် ခံစားမှု ချုပ်ငြိမ်းခြင်း သမာပတ်ကို ဝင်စားနေသော» / «မှတ်သိမှုနှင့် ခံစားရခြင်း ချုပ်ငြိမ်းရာ ဈာန်ကို ဝင်စားနေသော»: one lemma, the text's form / spacing (kept: form)
    'āgāraṃ',  # «အိမ်»: one meaning, = the pi-4 sense
    'sāsane',  # «သာသနာ»: one meaning, = the pi-2 sense
    'uppajjitvā',  # «ဖြစ်ပေါ်ပြီး» / «ဖြစ်ပေါ်၍»: one lemma, the text's form / spacing (kept: form), = the pi-2 sense
    'paññāsa',  # «ငါးဆယ်»: binding senses of pi-3 and a later binding file
    'soḷasa',  # «ဆယ့်ခြောက်»: binding senses of pi-3 and a later binding file
    'kappasahassāni',  # «ကမ္ဘာ»: one meaning, = the pi-2 sense
    'akusalaṃ cittaṃ',  # «အကုသိုလ် စိတ်»: one meaning, = the pi-2 sense
    'appamāṇa',  # «အပ္ပမာဏ»: binding senses of pi-3 and a later binding file
    'paritta',  # «ပရိတ္တာဘ»: one meaning, = the pi-3 sense
    'upadhi',  # «ဥပဓိ»: one meaning, = the pi-2 sense
    'kāyikaṃ',  # «ကိုယ်»: one meaning, = the pi-2 sense
    'rajanīyā',  # «တပ်မက်ဖွယ် ကောင်းသော» / «တပ်မက်ဖွယ်ကောင်းသော»: one lemma, the text's form / spacing (kept: form)
    'sakkāra',  # «အရိုအသေ ပြုခံရခြင်း»: one meaning, = the pi-4 sense
    'pītikaṃ',  # «ပီတိ» / «ပီတိ ရှိသော»: one lemma, the text's form / spacing (kept: form)
    'kantā',  # «ချစ်ခင်ဖွယ် ကောင်းသော» / «ချစ်ခင်ဖွယ်ကောင်းသော»: one lemma, the text's form / spacing (kept: form), = the pi-4 sense
    'nirāmisaṃ',  # «ကာမဂုဏ် ကင်းသော»: one meaning, = the pi-2 sense
    'saṃyamo',  # «စောင့်စည်းခြင်း»: one meaning, = the pi-2 sense
    'paṭisaṅkhā',  # «ပြန်လည် ဆင်ခြင်၍»: one meaning, = the pi-4 sense
    'paṇīta',  # «မြတ်ခြင်း»: one meaning, = the pi-4 sense
    'uppannassa',  # «ဖြစ်ပေါ်သော»: one meaning, = the pi-2 sense
    'cariyā',  # «ကျင့်ကြံမှု»: one meaning, = the pi-2 sense
    'vuṭṭhānaṃ',  # «ထမြောက်ခြင်း» / «ထမြောက်ရန်»: one lemma, the text's form / spacing (kept: form), = the pi-2 sense
    'aṭṭhāne',  # «မဖြစ်နိုင်သော အကြောင်း»: one meaning, = the pi-2 sense
    'manasi karoti',  # «နှလုံး သွင်းသည်» / «နှလုံး … ပြုသည်»: one lemma, the text's form / spacing (kept: form), = the pi-4 sense
    'cittaṃ vimuccati',  # «စိတ်သည် လွတ်မြောက်သည်» / «စိတ် … လွတ်မြောက်သည်»: one phrase, glued or gapped (kept: construction)
    'sarāgaṃ cittaṃ',  # «ရာဂ ရှိသော စိတ်» / «ရာဂ ရှိသော … စိတ်»: one phrase, glued or gapped (kept: construction)
    'vimuttaṃ',  # «လွတ်မြောက်ပြီးသော» / «လွတ်မြောက်သော»: one lemma, the text's form / spacing (kept: form), = the pi-2 sense
    'kataṃ',  # «ပြုသော» / «ပြုလုပ်ချက်»: one lemma, the text's form / spacing (kept: form), = the pi-4 sense
    'puggalassa saddhā',  # «ပုဂ္ဂိုလ်သည် ယုံကြည်မှု» / «ပုဂ္ဂိုလ်၌ ယုံကြည်မှု»: one phrase, glued or gapped (kept: construction)
    'puggalassa paññā',  # «ပုဂ္ဂိုလ်သည် ပညာ» / «ပုဂ္ဂိုလ်၌ ပညာ»: one phrase, glued or gapped (kept: construction)
    'muṭṭhassati',  # «သတိ လစ်သော»: one meaning, = the pi-4 sense
    'sabbena sabbaṃ',  # «လုံးဝ»: one meaning, = the pi-2 sense
    'sabbathā',  # «လုံးဝ»: one meaning, = the pi-2 sense
    'vuttāni bhagavatā',  # «မြတ်စွာဘုရား ဟောတော်မူသည်» / «မြတ်စွာဘုရား … ဟောတော်မူသည်»: one phrase, glued or gapped (kept: construction)
    'vuttāni',  # «ဟောတော်မူသည်»: one meaning, = the pi-2 sense
    'duggatiṃ',  # «လားရာ»: one meaning, = the pi-4 sense
    'upagataṃ',  # «ရောက်သော» / «ရောက်သွားသော»: one lemma, the text's form / spacing (kept: form)
    'paṇidhi',  # «ဆုတောင်းခြင်း» / «ဆုတောင်းမှု»: one lemma, the text's form / spacing (kept: form), = the pi-2 sense
    'asaṃvaro',  # «မစောင့်စည်းမှု»: one meaning, = the pi-2 sense
    'yoni',  # «မွေးဖွားရာ အမျိုးအစား» / «မွေးဖွားရာ»: one lemma, the text's form / spacing (kept: form), = the pi-2 sense
    'attabhāva',  # «ကိုယ်ခန္ဓာ»: one meaning, = the pi-2 sense
    'tittiravaṭṭakamorakapiñjaraṃ paṭiggaṇheyya',  # «ခါ … ငှက်ကြီးတို့ကို ခံယူသည်» / «ခါ … ငှက်ကြီး … ခံယူသည်»: one lemma, the text's form / spacing (kept: form)
    'vatthāni',  # «အဝတ်»: one meaning, = the pi-4 sense
    'bho',  # «အသျှင်»: one meaning, = the pi-4 sense
    'odātāni',  # «အဖြူ»: one meaning, = the pi-1 sense
    'anāsavaṃ',  # «စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော»: binding senses of pi-4 and a later binding file
    'agāraṃ',  # «လူ့ဘောင်»: one meaning, = the pi-4 sense
    'ajjhāvasati',  # «နေသည်»: one meaning, = the pi-4 sense
    'purisassa',  # «ယောကျ်ား»: one meaning, = the pi-4 sense
    'sattamaṃ',  # «ခုနစ်ခုမြောက်»: one meaning, = the pi-2 sense
    'Bodhisatto okkantaniyāmo',  # «ဘုရားလောင်း … သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းပြီးသော» / «ဘုရားလောင်းသည် သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းသော»: one lemma, the text's form / spacing (kept: form)
    'okkanta',  # «သက်ဆင်းပြီးသော» / «သက်ဆင်းသော»: one lemma, the text's form / spacing (kept: form)
    'okkantaniyāmo',  # «သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းပြီးသော» / «သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းသော»: one lemma, the text's form / spacing (kept: form)
    'pāvacane',  # «သာသနာ»: one meaning, = the pi-2 sense
    'Bodhisatto akāsi',  # «ဘုရားလောင်း … ပြုခဲ့သည်» / «ဘုရားလောင်း … ကျင့်ခဲ့သည်»: one lemma, the text's form / spacing (kept: form)
    'sambodhāya',  # «အမှန်ကို သိခြင်း»: one meaning, = the pi-2 sense
    'sadiso',  # «တူသော»: one meaning, = the pi-4 sense
    'nibbuto',  # «ငြိမ်းချမ်းသော»: one meaning, = the pi-4 sense
    'paṭipuggalo',  # «ပြိုင်ဘက် ပုဂ္ဂိုလ်» / «ပြိုင်ဘက် ပုဂ္ဂိုလ် ရှိသော»: one lemma, the text's form / spacing (kept: form)
    'anuttaro',  # «အမြတ်ဆုံး»: one meaning, = the pi-4 sense
    'saṃyojanā pahīyanti',  # «နှောင်ကြိုး … ပယ်သည်» / «နှောင်ကြိုးတို့ ပယ်ခံရသည်»: one lemma, the text's form / spacing (kept: form)
    'samāpattiṃ',  # «သမာပတ်»: one meaning, = the pi-2 sense
    'samāpajjeyya',  # «ဝင်စားနေသည်» / «ဝင်စားသည်»: one lemma, the text's form / spacing (kept: form)
    'samāpajjantassa',  # «ဝင်စားသူ» / «ဝင်စားနေသော»: one lemma, the text's form / spacing (kept: form), = the pi-2 sense
    'abhisametuṃ',  # «ထိုးထွင်း သိနိုင်သော» / «ထိုးထွင်း သိမြင်ရန်» / «ထိုးထွင်း သိ၍»: one lemma, the text's form / spacing (kept: form)
    'pattā',  # «ရောက်ပြီးသော» / «ရောက်သော»: one lemma, the text's form / spacing (kept: form)
    'dadantassa',  # «ပေးနေသော» / «ပေးလှူနေသော» / «ပေးသော»: one lemma, the text's form / spacing (kept: form)
    'ñāṇaṃ paṭisambhidā',  # «ဉာဏ် … ပိုင်းခြားသိသော ဉာဏ်» / «ဉာဏ်သည် ပိုင်းခြားသိသော ဉာဏ်»: one phrase, glued or gapped (kept: construction)
    'samanantara',  # «ကောင်းစွာ ကြားမလပ်» / «ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း»: one lemma, the text's form / spacing (kept: form)
    'vedeti',  # «ခံစားသည်» / «ခံစားရသည်»: one lemma, the text's form / spacing (kept: form)
    'asaṅkhatāni',  # «ပြုပြင်ဖန်တီးထားခြင်း မရှိသော» / «ပြုပြင်ဖန်တီးထားခြင်း မရှိသော အရာ»: one lemma, the text's form / spacing (kept: form)
    'abhisambujjhati',  # «ထိုးထွင်း သိတော်မူသည်»: one meaning, = the pi-4 sense
    'uttāniṃ',  # «ထင်ရှားအောင်»: one meaning, = the pi-2 sense
    'ṭhitā',  # «တည်သော» / «တည်ပြီးသော»: one lemma, the text's form / spacing (kept: form), = the pi-4 sense
    'saccāni asaṅkhatāni',  # «သစ္စာ … ပြုပြင်ဖန်တီးထားခြင်း မရှိသော» / «သစ္စာသည် ပြုပြင်ဖန်တီးထားခြင်း မရှိသော»: one phrase, glued or gapped (kept: construction)
    'upagaṃ',  # «ရောက်စေသော» / «ရောက်သော»: one lemma, the text's form / spacing (kept: form)
    'vuttā bhagavatā',  # «မြတ်စွာဘုရား ဟောတော်မူသည်» / «မြတ်စွာဘုရား … ဟောတော်မူသည်»: one phrase, glued or gapped (kept: construction)
    'appaṇihito',  # «တောင့်တမှု မရှိသော» / «တောင့်တမှု မရှိခြင်း»: one lemma, the text's form / spacing (kept: form)
    'antaraṃ',  # «ကြား»: one meaning, = the pi-4 sense
    'jā',  # «ဖြစ်ပေါ်သော»: one meaning, = the pi-4 sense
    'uddesaṃ',  # «ညွှန်ပြခြင်း»: one meaning, = the pi-4 sense
    'sahajātā',  # «အတူ ဖြစ်သော» / «အတူ ပေါ်ပေါက်သော»: one lemma, the text's form / spacing (kept: form)
    'vicāritaṃ',  # «သုံးသပ်ထားသော»: one meaning, = the pi-2 sense
    'attato',  # «အတ္တ»: one meaning, = the pi-2 sense
    'vitakkitaṃ',  # «ကြံစည်ထားသော»: one meaning, = the pi-2 sense
    'iṭṭhaphalaṃ',  # «လိုလားဖွယ် အသီးအပွင့် ရှိသော» / «လိုလားအပ်သော အကျိုး ရှိသော»: one lemma, the text's form / spacing (kept: form)
    'ekacco',  # «အချို့သူ» / «အချို့သော သူ»: one lemma, the text's form / spacing (kept: form), = the pi-4 sense
    'cittaṃ vaḍḍhati',  # «စိတ် တိုးပွားသည်» / «စိတ်သည် တိုးပွားသည်»: one phrase, glued or gapped (kept: construction)
    'paṇidahantassa',  # «ဆု တောင်းသော» / «ဆုတောင်းသော»: one phrase, glued or gapped (kept: construction)
    'manasikarontassa',  # «နှလုံးသွင်းသော»: one meaning, = the pi-2 sense
    'samannāharantassa',  # «စိတ်ကို ဆောင်သော»: one meaning, = the pi-2 sense
    'ābhogassa',  # «စိတ်ညွတ်သော» / «စိတ် ညွတ်သော»: one phrase, glued or gapped (kept: construction)
    'vidūrāni',  # «ဝေးကွာသော အရာ» / «ဝေးကွာသော»: one lemma, the text's form / spacing (kept: form)
    'gāmino',  # «သွားသော»: one meaning, = the pi-4 sense
    'sukhassa',  # «ချမ်းသာ»: one meaning, = the pi-4 sense
    'saṃvattati',  # «ဖြစ်စေသည်»: one meaning, = the pi-2 sense
    'āhārā',  # «အစာ»: one meaning, = the pi-2 sense
    'vipākā',  # «အကျိုး»: one meaning, = the pi-2 sense
    'pānīyaṃ',  # «သောက်ရေ» / «သောက်ဖွယ်»: one lemma, the text's form / spacing (kept: form)
    'yāpenti',  # «အသက်မွေးသည်»: one meaning, = the pi-1 sense
    'paṇḍitā',  # «ပညာရှိ»: one meaning, = the pi-1 sense
    'samannāhāro',  # «နှလုံးသွင်းခြင်း» / «နှလုံးသွင်းမှု»: one lemma, the text's form / spacing (kept: form), = the pi-2 sense
    'caritaṃ',  # «အကျင့်»: one meaning, = the pi-2 sense
    'cora',  # «ခိုးသူ»: binding senses of pi-4 and a later binding file
    'bhāvanā',  # «ပွားများခြင်း»: one meaning, = the pi-2 sense
    'dhīrā',  # «ပညာရှိ»: one meaning, = the pi-2 sense
    'Rūpino dhammā',  # «ရုပ် ဖြစ်သော သဘောတရား» / «ရုပ် … သဘောတရား»: one lemma, the text's form / spacing (kept: form), = the pi-3 sense
    'samuṭṭhitaṃ',  # «ဖြစ်ပေါ်သော»: one meaning, = the pi-2 sense
    'vedayati',  # «ခံစားသည်» / «ခံစားရသည်»: one lemma, the text's form / spacing (kept: form)
    'Nirodhaṃ samāpannassa',  # «ချုပ်ငြိမ်းခြင်း သမာပတ်ကို ဝင်စားနေသော» / «ချုပ်ငြိမ်းရာ ဈာန်ကို ဝင်စားနေသော»: one lemma, the text's form / spacing (kept: form)
    'avaseso',  # «အကြွင်း»: one meaning, = the pi-1 sense
    'saññī',  # «မှတ်ထင်သော» / «မှတ်သိသော»: one lemma, the text's form / spacing (kept: form), = the pi-4 sense
    'ārabbha uppajjati',  # «အာရုံပြု၍ ဖြစ်ပေါ်သည်» / «အာရုံပြု၍ … ဖြစ်ပေါ်သည်»: one phrase, glued or gapped (kept: construction)
    'samaṅgī',  # «ပြည့်စုံသော» / «ပြည့်စုံနေသော»: one lemma, the text's form / spacing (kept: form)
    'cakkhuviññāṇasamaṅgī',  # «မျက်စိ သိစိတ်နှင့် ပြည့်စုံသော» / «မျက်စိ သိစိတ်နှင့် ပြည့်စုံနေသော»: one lemma, the text's form / spacing (kept: form)
    'Sabbaso',  # «အခါခပ်သိမ်း»: one meaning, = the pi-2 sense
    'jhāyī',  # «ဈာန်ဝင်သော»: one meaning, = the pi-2 sense
    'lābhī',  # «ရသော»: one meaning, = the pi-4 sense
    'Mato',  # «သေပြီးသော» / «သေ၍»: the text's own word for the one meaning (kept: sense)
    'samanantarā uppajjanti',  # «ချက်ချင်း နောက်၌ ဖြစ်ပေါ်သည်» / «ချက်ချင်း နောက်၌ … ဖြစ်ပေါ်သည်»: one phrase, glued or gapped (kept: construction)
    'manasikārā',  # «နှလုံး သွင်း»: one meaning, = the pi-2 sense
    'samanantarā',  # «ချက်ချင်း နောက်၌» / «ချက်ချင်း»: one lemma, the text's form / spacing (kept: form), = the pi-4 sense
    'Cakkhuviññāṇaṃ uppajjati',  # «မျက်စိ သိစိတ် ဖြစ်ပေါ်သည်» / «မျက်စိ သိစိတ် … ဖြစ်ပေါ်သည်»: one phrase, glued or gapped (kept: construction)
    'suññataṃ',  # «ဆိတ်သုဉ်းခြင်း»: binding senses of pi-2 and a later binding file
    'Tena hi sīlaṃ',  # «သို့ဖြစ်လျှင် သီလ» / «သို့ဖြစ်လျှင် … သီလ»: one phrase, glued or gapped (kept: construction)
    'āsana',  # «နေရာ»: one meaning, = the pi-4 sense
    'dussilyaṃ',  # «သီလ ပျက်ခြင်း»: one meaning, = the pi-4 sense
    'saṅgaha',  # «အကျဉ်းချုပ်»: binding senses of pi-3 and a later binding file
    'jīvitāvasese',  # «အသက်၏ အကြွင်း» / «အသက် အကြွင်းအကျန်»: one lemma, the text's form / spacing (kept: form)
    'santati',  # «အစဉ်»: one meaning, = the pi-1 sense
    'bhāṇī',  # «ပြောဆိုသော»: one meaning, = the pi-4 sense
    'mātaraṃ jīvitā',  # «အမိ» / «အမိကို အသက်»: one lemma, the text's form / spacing (kept: form)
    'amanussa',  # «လူ မဟုတ်သော»: one meaning, = the pi-2 sense
    'tiracchānayoniṃ',  # «တိရစ္ဆာန် ဘဝ» / «တိရစ္ဆာန် ဘုံ» / «တိရစ္ဆာန် မွေးဖွားရာ အမျိုးအစား»: one lemma, the text's form / spacing (kept: form)
    'Āpāyiko',  # «အပါယ်သို့ ရောက်သော» / «အပါယ်သို့ ရောက်မည့်»: one lemma, the text's form / spacing (kept: form)
    'rato',  # «မွေ့လျော်သော»: one meaning, = the pi-4 sense
    'vagga',  # «ဝဂ်»: one meaning, = the pi-2 sense
    'kusalaṃ cittaṃ',  # «ကုသိုလ် စိတ်»: one meaning, = the pi-2 sense
    'niyāmaṃ okkameyya',  # «သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းသည်» / «သေချာသော လမ်းကြောင်း … သက်ဆင်းသည်»: one phrase, glued or gapped (kept: construction)
    'paṭivinodetvā',  # «ပယ်ဖျောက်၍»: one meaning, = the pi-4 sense
    'niyāmaṃ okkamati',  # «သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းသည်» / «သေချာသော လမ်းကြောင်း … သက်ဆင်းသည်»: one phrase, glued or gapped (kept: construction)
    'Micchattaniyato',  # «မှားယွင်းမှု၌ လမ်းကြောင်း သေချာပြီးသော»: one meaning, = the pi-2 sense
    'mahā',  # «မဟာ»: one meaning, = the pi-4 sense
    'Akusalamūlaṃ paṭisandahati',  # «အကုသိုလ်၏ အမြစ် … ဆက်စပ်သည်» / «အကုသိုလ်၏ အမြစ်နှင့် ဆက်စပ်သည်»: one phrase, glued or gapped (kept: construction)
    'Kusalaṃ uppajjati',  # «ကုသိုလ် … ဖြစ်ပေါ်သည်» / «ကုသိုလ် ဖြစ်ပေါ်သည်»: one phrase, glued or gapped (kept: construction)
    'avihiṃsā',  # «မညှဉ်းပန်းခြင်း»: one meaning, = the pi-2 sense
    'abyāpāda',  # «မဖျက်ဆီးလိုခြင်း»: one meaning, = the pi-2 sense
    'Kusalamūlaṃ paṭisandahati',  # «ကုသိုလ်၏ အမြစ်နှင့် ဆက်စပ်သည်» / «ကုသိုလ်၏ အမြစ် … ဆက်စပ်သည်»: one phrase, glued or gapped (kept: construction)
    'Akusalaṃ uppajjati',  # «အကုသိုလ် ဖြစ်ပေါ်သည်» / «အကုသိုလ် … ဖြစ်ပေါ်သည်»: one phrase, glued or gapped (kept: construction)
    'sīsaṃ',  # «ဦးခေါင်း»: one meaning, = the pi-4 sense
    'yāpeti',  # «အသက် မွေးသည်»: one meaning, = the pi-4 sense
    'vihāro',  # «နေခြင်း»: one meaning, = the pi-2 sense
    'ahitāya',  # «အစီးအပွား မဖြစ်ဖွယ်ရာ»: one meaning, = the pi-4 sense
    'abyākatā dhammā',  # «ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော … သဘောတရား»: one meaning, = the pi-1 sense
    'upacayo',  # «စုဆောင်းမှု» / «စုဆောင်းခြင်း»: one lemma, the text's form / spacing (kept: form)
    'pāpaṃ',  # «ယုတ်မာမှု»: one meaning, = the pi-4 sense
    'vihāraṃ',  # «နေခြင်း»: one meaning, = the pi-2 sense
    'sukhavihāraṃ',  # «ချမ်းသာစွာ နေခြင်း»: one meaning, = the pi-2 sense
    'sobhagya',  # «ကောင်းသော ကံကြမ္မာ» / «ကောင်းကျိုး ချမ်းသာ»: one lemma, the text's form / spacing (kept: form)
    'visinetvā',  # «ဖြန့်ကြဲ၍» / «ဖြန့်ကျက်၍»: one lemma, the text's form / spacing (kept: form)
    'ekāgārikaṃ kareyya',  # «အိမ်တစ်အိမ်တည်းကို ဝိုင်းဝန်း၍ လုယက်သည်» / «အိမ်တစ်လုံးကို ဝိုင်းဝန်း လုယက်သည်»: one lemma, the text's form / spacing (kept: form)
    'indriyabaddhaṃ dukkhaṃ',  # «စွမ်းရည်တို့နှင့် ဆက်စပ်သော … ဒုက္ခ» / «စွမ်းရည်တို့နှင့် ဆက်စပ်သော ဒုက္ခ»: one phrase, glued or gapped (kept: construction)
    'pariññāya',  # «ပိုင်းခြား သိရန်»: one meaning, = the pi-2 sense
    'avasesā',  # «ကြွင်းသော»: binding senses of pi-4 and a later binding file
    'khettaṃ',  # «လယ်မြေ»: one meaning, = the pi-1 sense
    'appameyyo',  # «အတိုင်းအဆ မရှိသော»: one meaning, = the pi-4 sense
    'uddissa',  # «ရည်စူး၍»: one meaning, = the pi-4 sense
    'paṭipannā',  # «ကျင့်ကြံဆဲသော»: one meaning, = the pi-4 sense
    'Vineyya',  # «ဖယ်ရှား၍»: one meaning, = the pi-2 sense
    'dvipadānaṃ',  # «ခြေနှစ်ချောင်း ရှိသော» / «ခြေ နှစ်ချောင်း ရှိသော»: one phrase, glued or gapped (kept: construction)
    'pavaro',  # «အထူးမြတ်ဆုံး»: one meaning, = the pi-4 sense
    'bhagavā jāto',  # «မြတ်စွာဘုရား … ဖွားမြင်တော်မူခဲ့သော» / «မြတ်စွာဘုရား … ဖွားမြင်တော်မူသော»: one lemma, the text's form / spacing (kept: form)
    'dullabhā',  # «ရှားပါးသော»: one meaning, = the pi-4 sense
    'paṭivijānāti',  # «ခွဲခြား သိသည်»: one meaning, = the pi-2 sense
    'nimuggo',  # «နစ်မြုပ်သော»: one meaning, = the pi-4 sense
    'patigādha',  # «ခြေကုတ်ရာ မြေ»: one meaning, = the pi-4 sense
    'raja',  # «မြူ»: one meaning, = the pi-4 sense
    'suviññāpaye',  # «သိအောင် ပြရ လွယ်ကူသော»: one meaning, = the pi-2 sense
    'viññāpaye',  # «သိအောင် ပြရ»: one meaning, = the pi-2 sense
    'tiriyaṃ',  # «ဘေး»: one meaning, = the pi-2 sense
    'bandhanaṃ',  # «အနှောင်»: one meaning, = the pi-2 sense
    'pāde',  # «ခြေ»: one meaning, = the pi-2 sense
    'kaṭukā',  # «ခါးသက်သော»: one meaning, = the pi-2 sense
    'pharitvā',  # «ပျံ့နှံ့၍»: one meaning, = the pi-2 sense
    'makkhikā',  # «ယင်»: one meaning, = the pi-4 sense
    'pañcaṅgiko maggo',  # «မဂ်သည် အင်္ဂါ ငါးပါး ရှိသော»: one meaning, = the pi-2 sense
    'pāripūriṃ',  # «ပြည့်စုံခြင်း»: one meaning, = the pi-4 sense
    'buddhānaṃ',  # «ဘုရား»: one meaning, = the pi-4 sense
    'upaṭṭhāko',  # «အလုပ်အကျွေး»: one meaning, = the pi-4 sense
    'buddhā',  # «ဘုရား»: one meaning, = the pi-2 sense
    'buddhā tiṭṭhanti',  # «ဘုရား တည်ရှိသည်» / «ဘုရားတို့ တည်ရှိသည်»: one phrase, glued or gapped (kept: construction)
    'dhammā niyatā',  # «သဘောတရား … ကျိန်းသေသော»: one meaning, = the pi-1 sense
    'upaṭṭhita',  # «ထင်ရှား တည်သော»: one meaning, = the pi-4 sense
    'kiriyābyākate',  # «ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော ကြိယာ»: one meaning, = the pi-2 sense
    'ratta',  # «ညဉ့်ဦးယံ ညဉ့်နောက်ယံ»: one meaning, = the pi-4 sense
    'ghoso',  # «အသံ»: one meaning, = the pi-1 sense
    'pisuṇāya',  # «ကုန်းချောစကား»: one meaning, = the pi-4 sense
    'saṃvattanikā',  # «ပို့ဆောင်တတ်သော»: one meaning, = the pi-2 sense
    'ajjhattikaṃ',  # «မိမိ၏»: one meaning, = the pi-2 sense
    # @@LUMP-FULL
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
        for k in reversed(list(found)):                         # pi-4 first where several list a value
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
        f.write(f'# Pāli→Burmese pi-5 sense decisions, written by gen_decisions_my.py from {pathlib.Path(aggp).name}\n')
        f.write('# English tags: pi-4, then pi-3, then pi-2, then pi-1 Burmese senses (binding), else Marathi pi-5 senses '
                '(tags only), or MANUAL;\n')
        f.write('# values: pi-5 Burmese keyword map only.\n')
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
