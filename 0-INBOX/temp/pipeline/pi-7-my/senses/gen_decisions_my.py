"""Write the Pāli→Burmese pi-7 decisions file for senses_my.py (brief: pi-7-my/burmese-senses-brief.md).
Adapted from pi-6-my/senses/gen_decisions_my.py (same engine and MANUAL / LUMP_OK / TAG_CHANGED / NEW_SENSE / MR_ADJUST
mechanism); the binding chain is now pi-6, then pi-5, pi-4, pi-3, pi-2, pi-1; the tags for headwords new in pi-7 come
from the Marathi pi-7 senses (tags only).

usage: python -I -X utf8 gen_decisions_my.py <agg.tsv> <decisions.txt>

For every headword of agg.tsv that has Burmese values (NDE-only headwords are skipped):
  1. a hand decision in MANUAL below wins;
  2. otherwise the approved Burmese senses are BINDING, pi-6 first, then pi-5, pi-4, pi-3, pi-2, pi-1 (each looked up
     exact, else the one case-insensitive match: the aggregation keeps the first spelling seen). The reference is the
     line of the first of pi-6 / pi-5 / pi-4 / pi-3 / pi-2 / pi-1 that has the headword. Every pi-7 value that the
     reference lists goes under the reference's sense with its English tag, in the reference's sense order (a sense
     with no pi-7 value is left out). A pi-7 value the reference does not list:
       - a later binding file lists it: that file's sense (tag) is added after the reference's, or the value joins the
         reference sense with the same tag (REVIEW);
       - otherwise, the reference has one sense: the value joins it (REVIEW unless the headword is in LUMP_OK);
       - otherwise (the reference has several senses): UNRESOLVED (write MANUAL);
  3. otherwise, if the Marathi pi-7 senses file gives the headword ONE English tag, the line is that tag + every
     attested Burmese value (one sense; several values -> REVIEW unless LUMP_OK); where that Marathi tag does not
     describe the headword the Burmese values show (e.g. the tag of a compound member, or a positive tag on a negated
     form), MR_ADJUST gives the adjusted English tag with its logged reason (only for such headwords);
  4. otherwise (several Marathi senses, or no Marathi line) the headword is UNRESOLVED: write MANUAL.
Only the ENGLISH tags are read from the Marathi file; its Marathi values are dropped on parsing and never written.
A MANUAL entry for a pi-6 / pi-5 / pi-4 / pi-3 / pi-2 / pi-1 headword must keep the binding split: every value the
binding senses list (pi-6's sense for it, else pi-5's, pi-4's, pi-3's, pi-2's, pi-1's) sits under a sense whose tag
starts with that binding tag (an appended «, …» is allowed) unless the headword is in TAG_CHANGED (logged reason); and a
MANUAL sense that holds only values the binding senses do not list, with a tag that starts with none of the binding
tags, is a NEW sense and the headword must be in NEW_SENSE (logged reason).
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
    ('p6', ROOT / 'AI_translation/burmese/pi-6-pali-word-burmese-senses-plain.md'),
    ('p5', ROOT / 'AI_translation/burmese/pi-5-pali-word-burmese-senses-plain.md'),
    ('p4', ROOT / 'AI_translation/burmese/pi-4-pali-word-burmese-senses-plain.md'),
    ('p3', ROOT / 'AI_translation/burmese/pi-3-pali-word-burmese-senses-plain.md'),
    ('p2', ROOT / 'AI_translation/burmese/pi-2-pali-word-burmese-senses-plain.md'),
    ('p1', ROOT / 'AI_translation/burmese/pi-1-pali-word-burmese-senses-plain.md'),
])
BOOK = {'p6': 'pi-6', 'p5': 'pi-5', 'p4': 'pi-4', 'p3': 'pi-3', 'p2': 'pi-2', 'p1': 'pi-1'}
MR_SENSES = ROOT / 'AI_translation/marathi/pi-7-pali-word-marathi-senses-plain.md'
VAL_RE = re.compile(r'^(.*)=(\d+)\[[^\]]*\]$')
NONLATIN = re.compile(r'[\u0900-\u097f\u1000-\u109f]')

# Hand decisions: headword -> [(English tag, [Burmese values])]. Values must be attested.
# Binding senses first (pi-6, else pi-5, pi-4, pi-3, pi-2, pi-1 order and tag), then the senses new in pi-7.
MANUAL = OrderedDict([
    # ======== sample (agg-sample.tsv, the first 80 headwords) ========
    ('Ekamūlakaṃ', [
        # pi-6 'based on one root in common' and pi-3 'section label …' not attested; the counted mūlaka (T6)
        ('the one-condition series, the counts that start from a single condition (heading)',
         ['အကြောင်း တစ်ခုကို အခြေခံခြင်း']),
    ]),
    ('Anulomaṃ', [
        # pi-6 sense kept for the order; the mind moment is new (brief; map-harmonise §B kept: sense, harmonise H1)
        ('the affirmative form of the paired questions, in the headings of each section (heading member), here the '
         'positive method of the Paṭṭhāna counts', ['အဟုတ်ပြ ပုံစံ']),
        ('conformity, the cognitive moment before change-of-lineage (nominative sg.)', ['လျော်ညီခြင်း စိတ်']),
    ]),
    ('Anantara', [
        # pi-5 sense 1 is the proximity relation itself (Kathāvatthu 5-22-3-1-0 Anantarapaccayakathā): both pi-7
        # values are the text's word for it, bare name (ghaṭanā lists) and «…ဟူသော အကြောင်း» name (T1-T4 grammar)
        ('contiguity, the proximity relation, in anantarapaccaya (compound member), here the proximity condition, by '
         'its bare name in the combination lists and as the named condition in the headings',
         ['ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း', 'ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း']),
    ]),
    ('Jhāna', [
        # pi-5 value «ဈာန်» stays in its sense (^7-8-4, the bare name in a cut chain); the condition name is new
        ('meditative absorption, chapter subject (stem and heading), here also the jhāna condition by its bare name '
         'in an abbreviated chain', ['ဈာန်']),
        ('jhāna condition, the named condition in the headings (stem)', ['ဈာန်ဟူသော အကြောင်း']),
    ]),
    ('Natthi', [
        # the verb of the notes keeps the pi-6 sense (one lemma, «မရှိ» / «မရှိသည်», f_natthi); the condition is new
        ("there is not, the denial in the nihilist view 'there is no gift' (3rd sg. present), here 'there is not' in "
         "the editorial notes", ['မရှိ', 'မရှိသည်']),
        ('absence condition, by its bare name in the combination lists and as the named condition in the headings '
         '(stem)', ['မရှိခြင်း', 'မရှိခြင်းဟူသော အကြောင်း']),
    ]),
    ('Hetudukaṃ', [
        # new in pi-7: the two Marathi pi-7 senses; map-harmonise §B kept: sense
        ('the root dyad, first dyad of the matrix (heading)', ['အမြစ် နှစ်မျိုးတွဲ']),
        ('pairs with the root condition, combinations in the counts (heading)', ['အမြစ်ဟူသော အကြောင်း၏ နှစ်မျိုးတွဲ']),
    ]),
    # @@MANUAL-SAMPLE
    # ======== full run (agg-part1.tsv) ========
    # ---- condition names: the binding value stays in its sense, the «…ဟူသော အကြောင်း» name is the condition ----
    ('Atthi', [
        ('there is, exists (3rd sg. present), here in an editorial note', ['ရှိသည်']),
        ('presence condition, by its bare name in the combination lists and as the named condition in a heading '
         '(stem)', ['ရှိခြင်း', 'ရှိခြင်းဟူသော အကြောင်း']),
    ]),
    ('indriya', [
        ("sense faculty, in indriyabaddha 'bound to the faculties' (compound member), here the faculties as a "
         "category, in indriyapaññatti, here also the faculty condition by its bare name in the combination lists",
         ['စွမ်းရည်']),
        ('faculty condition, the named condition in the headings (stem)', ['စွမ်းရည်ဟူသော အကြောင်း']),
    ]),
    ('Sahajāta', [
        ('born together (compound member), here also the co-arising condition by its bare name in the combination '
         'lists and section names, and the adjective in a heading', ['အတူ ပေါ်ပေါက်ခြင်း', 'အတူ ပေါ်ပေါက်သော']),
        ('co-arising condition, the named condition in a heading (stem)', ['အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်း']),
    ]),
    ('adhipati', [
        ('predominance, dominant factor (heading), here also the predominance condition by its bare name in the '
         'combination lists', ['အကြီးအမှူး']),
        ('predominance condition, the named condition in the headings (stem)', ['အကြီးအမှူးဟူသော အကြောင်း']),
    ]),
    ('Aññamañña', [
        # pi-5 / pi-2 sense is the reciprocity relation itself (5-23-2-1-0 Aññamaññapaccayakathā): both pi-7 values
        ('mutuality, reciprocity (heading member), here the mutuality condition, by its bare name in the '
         'combination lists and as the named condition in the headings',
         ['အချင်းချင်း ထောက်ပံ့ခြင်း', 'အချင်းချင်း ထောက်ပံ့ခြင်းဟူသော အကြောင်း']),
    ]),
    ('Ārammaṇa', [
        ('object of the mind, what the mind takes up (compound member), here also the object condition by its bare '
         'name in the combination lists', ['အာရုံ']),
        ('object condition, the named condition in the headings (stem)', ['အာရုံဟူသော အကြောင်း']),
    ]),
    ('vipāka', [
        ('resultant, born as the result of action (compound member), here also the result condition by its bare name '
         'in the combination lists', ['ကံ၏ အကျိုး']),
        ('result condition, the named condition in a heading (stem)', ['ကံ၏ အကျိုးဟူသော အကြောင်း']),
    ]),
    ('Kamma', [
        ('deeds, as compound member, here also the kamma condition by its bare name in the combination lists', ['ကံ']),
        ('kamma condition, the named condition in the headings (stem)', ['ကံဟူသော အကြောင်း']),
    ]),
    ('āsevana', [
        # pi-5 sense is the repetition relation (5-30-7-1-0 Āsevanapaccayakathā): the text's word for it
        ('repeated practice, frequency, here the repetition condition by its bare name in the combination lists',
         ['အလေ့အကျင့် ပြုခြင်း']),
    ]),
    # ---- bare condition names whose binding (ordinary) value is not attested ----
    ('vippayutta', [('dissociation condition, by its bare name in the combination lists (stem)', ['ကင်းကွာခြင်း'])]),
    ('sampayutta', [('association condition, by its bare name in the combination lists (stem)', ['ယှဉ်တွဲခြင်း'])]),
    ('purejāta', [
        ('pre-arising condition, by its bare name in the combination lists, also the label of the object and base '
         'kinds of pre-arising (stem)', ['ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း']),
    ]),
    ('āhāra', [('nutriment condition, by its bare name in the combination lists (stem)', ['အာဟာရ'])]),
    ('Vigata', [('disappearance condition, by its bare name in the combination lists (stem)', ['ပျောက်ကွယ်ခြင်း'])]),
    ('vigataṃ', [('disappearance condition, named in an editorial note (nominative sg.)', ['ပျောက်ကွယ်ခြင်း'])]),
    # ---- counting locatives of the conditions (T2) ----
    ('ārammaṇe', [('in the object condition, the count locative (locative)', ['အာရုံဟူသော အကြောင်း'])]),
    ('āhāre', [('in the nutriment condition, the count locative (locative)', ['အာဟာရဟူသော အကြောင်း'])]),
    ('indriye', [('in the faculty condition, the count locative (locative)', ['စွမ်းရည်ဟူသော အကြောင်း'])]),
    ('magge', [('in the path condition, the count locative (locative)', ['မဂ်ဟူသော အကြောင်း'])]),
    ('vippayutte', [('in the dissociation condition, the count locative (locative)', ['ကင်းကွာခြင်းဟူသော အကြောင်း'])]),
    ('vigate', [('in the disappearance condition, the count locative (locative)', ['ပျောက်ကွယ်ခြင်းဟူသော အကြောင်း'])]),
    ('jhāne', [('in the jhāna condition, the count locative (locative)', ['ဈာန်ဟူသော အကြောင်း'])]),
    ('sampayutte', [('in the association condition, the count locative (locative)', ['ယှဉ်တွဲခြင်းဟူသော အကြောင်း'])]),
    ('vipāke', [
        # new in pi-7 (two Marathi pi-7 senses); the noun and the adjective of 'vipāke khandhe' are one lemma
        ('in the result condition, the count locative (locative)', ['ကံ၏ အကျိုးဟူသော အကြောင်း']),
        ("resultant, born as the result of action, in 'vipāke khandhe' (accusative pl.), also the result as a noun",
         ['ကံ၏ အကျိုး', 'ကံ၏ အကျိုး ဖြစ်သော']),
    ]),
    ('vipākaṃ', [
        ('resultant, born as the result of action (neuter sg.)', ['ကံ၏ အကျိုး ဖြစ်သော']),
        ("the result condition, named in the count notes, as in 'āsevane vipākaṃ natthi' (neuter sg.)",
         ['ကံ၏ အကျိုး']),
    ]),
    # ---- other binding headwords with a new pi-7 sense ----
    ('nirodhā', [("from cessation, the attainment of cessation, in 'nirodhā vuṭṭhahantassa' (ablative)",
                  ['ချုပ်ငြိမ်းခြင်း သမာပတ်'])]),
    ('parikammaṃ', [('preliminary work, the preparation for jhāna or path (nominative sg.)', ['ကြိုတင် ပြင်ဆင်မှု'])]),
    ('tiṭṭhati', [("lies in wait, in 'paripanthe tiṭṭhati' 'commits highway robbery' (3rd sg. present)",
                   ['ဓားပြ တိုက်သည်'])]),
    ('dhammassa', [('of a phenomenon, a state (genitive sg.)', ['သဘောတရား'])]),
    ('gamanāni', [('courses, the ways the answers run, in an editorial note (nominative pl.)', ['သွားပုံ'])]),
    ('byañjanena', [('by the wording, the letter of the text (instrumental)', ['စကားလုံး'])]),
    ('kāraṇena', [("in this way, by this method, in 'iminā kāraṇena' (instrumental)", ['နည်းလမ်း'])]),
    ('ante', [("at the end, in 'ante ante' 'at the end of each' (locative)", ['အဆုံးတိုင်း'])]),
    ('agge', [('at the front, first, in an editorial note (locative)', ['ရှေ့ဆုံး'])]),
    ('Yogaṃ', [('a bond, yoke, item of the bond dyad (accusative sg.)', ['ထမ်းပိုး'])]),
    ('bāhiro', [('external, outside oneself, the triad item (masculine sg.)', ['ပြင်ပ'])]),
    ('likhitaṃ', [("written, set down above, in 'heṭṭhā likhitaṃ' (neuter sg. participle)", ['ရေးထားသော'])]),
    ('anuloma', [("positive, the positive method, the first member of a detached 'anuloma paccanīyaṃ' "
                  "(compound member)", ['အဟုတ်ပြ ပုံစံ'])]),
    ('Abyākatamūlaṃ', [('the series starting from the indeterminate item, in the count notes (nominative sg.)',
                        ['ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော … အခြေခံခြင်း'])]),
    ('kiñci', [("some, in 'kiñci kāle' 'at some times' (indefinite pronoun)", ['အချို့သော'])]),
    ('paccaya', [('arising by way of condition, the Paccayavāra as a member of the combined section name with '
                  'sahajāta, nissaya, saṃsaṭṭha and sampayutta (heading member)', ['အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်း'])]),
    ('vatthu', [('the physical base, the material support of mind (nominative sg.)', ['မှီရာ ဝတ္ထု'])]),
    ('citto', [("mind, the item of the mind dyad, in 'citto dhammo' (masculine sg.)", ['စိတ်'])]),
    # ---- binding headwords whose pi-7 value is another grammatical form of the binding meaning (tag extended) ----
    ('kusale', [("in the wholesome mind (locative sg.), here wholesome, said of the aggregates, in 'kusale khandhe' "
                 "(accusative pl.)", ['ကုသိုလ်'])]),
    ('vodānaṃ', [('cleansing, purification (accusative sg.), here the cleansing moment of mind before a higher path',
                  ['စင်ကြယ်ခြင်း စိတ်'])]),
    ('sahajātaṃ', [('born together with it, conascent (neuter sg. participle), here also co-arising as the label of '
                    'the co-arisen kind of a condition', ['အတူ ပေါ်ပေါက်ခြင်း', 'အတူ ပေါ်ပေါက်သော'])]),
    # ---- new in pi-7, several Marathi pi-7 senses but one Burmese value (or a Marathi-only artefact in the tag) ----
    ('Ārammaṇādhipati', [('object-predominance, the object kind of predominance (nominative), also as a member of '
                          'the combination lists', ['အာရုံ အကြီးအမှူး'])]),
    ('kātabbaṃ', [('to be done or made, of a basic sentence, a cycle or a list (gerundive)', ['ပြုရမည့်'])]),
    ('uppādetvā', [("having shed, of the Buddha's blood, in 'lohitaṃ uppādetvā' (absolutive)", ['ထွက်စေ၍'])]),
    ('kātabbā', [
        ('should be done, in general (gerundive)', ['ပြုရမည့်']),
        ('to be included, of items such as rebirth, the great elements or food (gerundive)', ['ထည့်ရမည့်']),
    ]),
    ('kātabbo', [('to be made or done, of a basic sentence, a cycle or a list (gerundive)', ['ပြုရမည့်'])]),
    ('Hetuṃ', [('root, item of the root dyad, a root phenomenon (accusative sg.)', ['အမြစ်'])]),
    ('Saññojanañca', [('and a fetter, item of the fetter dyad (accusative sg. with -ñca)', ['နှောင်ကြိုး'])]),
    ('parāmāsassa', [('of wrong grasping, item of the wrong-grasping dyad (genitive sg.)', ['မှားယွင်းသော ယူဆမှု'])]),
    # @@MANUAL-FULL
])

# Binding headwords whose MANUAL entry deliberately departs from a binding tag (headword: reason).
TAG_CHANGED = {
    # @@TAGCH
}

# Binding headwords whose MANUAL entry adds a sense with values the binding senses do not list (headword: reason).
NEW_SENSE = {
    # ---- sample ----
    'Ekamūlakaṃ': "pi-6 'based on one root in common' «တူညီသော အမြစ်ကို အခြေခံသော» and pi-3 'section label for items "
                  "taken one at a time' not attested; «အကြောင်း တစ်ခုကို အခြေခံခြင်း» is the counted mūlaka, the "
                  "one-condition series (^7-1-34 …; map-table T6, my7-zeroshot-terms §2)",
    'Anulomaṃ': "pi-6 sense kept for the positive method «အဟုတ်ပြ ပုံစံ»; «လျော်ညီခြင်း စိတ်» is the conformity mind "
                "moment before gotrabhū (^7-8-27 …; brief, map-harmonise §B kept: sense, harmonise H1)",
    'Jhāna': "pi-5 sense kept for «ဈာန်» (^7-8-4); «ဈာန်ဟူသော အကြောင်း» is the jhāna condition named in the headings "
             "(^7-1-1-1-4-2-16-0; map-table T1, brief: condition vs ordinary sense where the values differ)",
    'Natthi': "pi-6 sense kept for the verb «မရှိသည်» / «မရှိ» of the notes (^7-2-339, ^7-8-4 …); «မရှိခြင်း» / "
              "«မရှိခြင်းဟူသော အကြောင်း» are the absence condition (^7-2-454, ^7-1-1-1-4-2-20-0 …; map-table T1, T4, "
              "map-harmonise §B kept: grammar / sense)",
    # @@NEW-SAMPLE
    # ---- full run ----
    'Atthi': "pi-5 sense kept for the verb «ရှိသည်» of a note (^7-10-111); «ရှိခြင်း» / «ရှိခြင်းဟူသော အကြောင်း» are the "
             "presence condition (^7-2-441 …, ^7-2-1-1-1-3-4-0; map-table T1, T4)",
    'indriya': "pi-5 sense kept for «စွမ်းရည်» (bare name, ^7-2-442 …); «စွမ်းရည်ဟူသော အကြောင်း» is the faculty condition "
               "named in the headings (^7-1-1-1-4-54-5-0 …; map-table T1, brief)",
    'Sahajāta': "pi-5 sense kept for «အတူ ပေါ်ပေါက်ခြင်း» / «…သော»; «အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်း» is the co-arising "
                "condition named in a heading (^7-1-1-1-4-54-49-0; map-table T1)",
    'adhipati': "pi-5 sense kept for «အကြီးအမှူး»; «အကြီးအမှူးဟူသော အကြောင်း» is the predominance condition named in the "
                "headings (^7-1-1-1-4-54-57-0, ^7-4-3-1-69-5-0; map-table T1)",
    'Ārammaṇa': "pi-5 sense kept for «အာရုံ»; «အာရုံဟူသော အကြောင်း» is the object condition named in the headings "
                "(^7-4-3-1-21-2-0 …; map-table T1)",
    'vipāka': "pi-2 sense kept for «ကံ၏ အကျိုး»; «ကံ၏ အကျိုးဟူသော အကြောင်း» is the result condition named in a heading "
              "(^7-3-1-9-30-9-0; map-table T1, brief)",
    'Kamma': "pi-5 sense 'deeds' kept for «ကံ»; «ကံဟူသော အကြောင်း» is the kamma condition named in the headings "
             "(^7-1-1-1-4-16-13-0 …; map-table T1)",
    'vippayutta': "pi-5 'dissociated from, compound final' «ကင်းကွာသော» not attested; «ကင်းကွာခြင်း» is the bare name of "
                  "the dissociation condition (^7-2-441 …; map-table T1)",
    'sampayutta': "pi-3 / pi-1 'conjoined with, compound final' «ယှဉ်တွဲသော» not attested; «ယှဉ်တွဲခြင်း» is the bare "
                  "name of the association condition (^7-2-451 …; map-table T1)",
    'purejāta': "pi-5 'born beforehand' «ရှေးဦးစွာ ဖြစ်ပေါ်ပြီးသော» not attested; «ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း» is the bare "
                "name of the pre-arising condition (^7-2-445 …; map-table T1)",
    'āhāra': "pi-5 'bringing out in speech' «ဆိုခြင်း» not attested; «အာဟာရ» is the bare name of the nutriment condition "
             "(^7-2-450 …; map-table T1)",
    'Vigata': "pi-5 'gone, removed' «ကင်းသော» not attested; «ပျောက်ကွယ်ခြင်း» is the bare name of the disappearance "
              "condition (^7-2-522, ^7-8-4; map-table T1)",
    'vigataṃ': "pi-5 'departed' «ကင်းကွာပြီးသော» not attested; «ပျောက်ကွယ်ခြင်း» is the disappearance condition named "
               "in a note (^7-4-119; map-table T1)",
    'ārammaṇe': "pi-5 'in the object' «အာရုံ» not attested; «အာရုံဟူသော အကြောင်း» is the counting locative of the "
                "object condition (^7-2-73 …; map-table T2, phase-1 §E)",
    'āhāre': "pi-5 'in nutritive conditions' «အာဟာရ» not attested; «အာဟာရဟူသော အကြောင်း» is the counting locative of "
             "the nutriment condition (^7-2-73 …; map-table T2)",
    'indriye': "pi-6 'faculties' «စွမ်းရည်» not attested; «စွမ်းရည်ဟူသော အကြောင်း» is the counting locative of the "
               "faculty condition (^7-2-73 …; map-table T2)",
    'magge': "pi-5 'in the path' «မဂ်» not attested; «မဂ်ဟူသော အကြောင်း» is the counting locative of the path condition "
             "(^7-2-73 …; map-table T2)",
    'vippayutte': "pi-5 'dissociated from (locative)' «ကင်းကွာသော» not attested; «ကင်းကွာခြင်းဟူသော အကြောင်း» is the "
                  "counting locative of the dissociation condition (^7-2-73 …; map-table T2)",
    'vigate': "pi-5 'when departed' «ကင်းသွားသော» not attested; «ပျောက်ကွယ်ခြင်းဟူသော အကြောင်း» is the counting locative "
              "of the disappearance condition (^7-2-73 …; map-table T2)",
    'jhāne': "pi-1 'in the meditative absorption' «ဈာန်» not attested; «ဈာန်ဟူသော အကြောင်း» is the counting locative of "
             "the jhāna condition (^7-2-76 …; map-table T2)",
    'sampayutte': "pi-1 'conjoined with (locative)' «ယှဉ်တွဲသော» not attested; «ယှဉ်တွဲခြင်းဟူသော အကြောင်း» is the "
                  "counting locative of the association condition (^7-2-76; map-table T2)",
    'vipākaṃ': "pi-2 sense kept for the adjective «ကံ၏ အကျိုး ဖြစ်သော»; «ကံ၏ အကျိုး» is the result condition named in the "
               "count notes '(āsevane vipākaṃ natthi)' (^7-2-81, ^7-2-283, ^7-8-4; Marathi pi-7 tag, map-harmonise §B "
               "kept: sense)",
    'nirodhā': "pi-5 'stoppings, endings' «ချုပ်ငြိမ်းသော» not attested; «ချုပ်ငြိမ်းခြင်း သမာပတ်» is the attainment of "
               "cessation, 'nirodhā vuṭṭhahantassa' (^7-2-417 …; map-table, my7 LEX)",
    'parikammaṃ': "pi-5 'massaging the body' «ပွတ်တိုက်ပေးခြင်း» not attested; «ကြိုတင် ပြင်ဆင်မှု» is the jhāna / path "
                  "preliminary (^7-2-423 …; notes-g2 §D)",
    'tiṭṭhati': "pi-5 'stands upright' «တည်သည်» not attested; «ဓားပြ တိုက်သည်» is 'paripanthe tiṭṭhati', highway robbery "
                "(^7-2-423 …; map-table T11)",
    'dhammassa': "pi-5 'the Buddha's teaching' «တရား» not attested; «သဘောတရား» is dhamma as phenomenon (^7-4-93 …)",
    'gamanāni': "pi-2 'goings, in agatigamanāni' «လိုက်ခြင်း» not attested; «သွားပုံ» is the courses of the answers in a "
                "note (^7-8-28)",
    'byañjanena': "pi-5 'by outward mark' «အသွင်» not attested; «စကားလုံး» is the wording of the text, 'byañjanena na "
                  "samenti' (^7-10-112)",
    'kāraṇena': "pi-5 'by the reason' «အကြောင်း» not attested; «နည်းလမ်း» is 'iminā kāraṇena', by this method "
                "(^7-23-5 …; coordinator g2 decision kāraṇena)",
    'ante': "pi-2 'extremes' «အစွန်း» not attested; «အဆုံးတိုင်း» is 'ante ante', at the end of each (^7-23-46)",
    'agge': "pi-2 'at the tip' «ဖျား» not attested; «ရှေ့ဆုံး» is 'at the front, first' of a note (^7-25-80, ^7-25-81)",
    'Yogaṃ': "pi-5 'connection, in ayoganti' «ဆက်စပ်» not attested; «ထမ်းပိုး» is the bond, the item of the yoga dyad "
             "(^7-29-2 …; notes-g3, cluster names)",
    'bāhiro': "pi-5 'one outside the dispensation' «သာသနာပ» not attested; «ပြင်ပ» is the triad item 'external' "
              "(^7-32-318 …)",
    'likhitaṃ': "pi-4 'burnished' «ပွတ်ထားသော» not attested; «ရေးထားသော» is 'written', 'heṭṭhā likhitaṃ' (^7-35-124; "
                "notes-g4 §D)",
    'anuloma': "pi-5 'direct order' «အစဉ်အတိုင်း» not attested; «အဟုတ်ပြ ပုံစံ» is the positive method (^7-36-11; as "
               "pi-6 anulomaṃ, brief)",
    'Abyākatamūlaṃ': "pi-1 'a root that is neither wholesome nor unwholesome' «… အမြစ်» not attested; «… အခြေခံခြင်း» is "
                     "the series based on the indeterminate item (^7-65-50 …; map-table T6)",
    'kiñci': "pi-5 'anything at all' «တစ်စုံတစ်ရာ» not attested; «အချို့သော» is 'kiñci kāle', at some times (^7-1-6, "
             "^7-1-10; map-table)",
    'paccaya': "pi-5 / pi-2 'condition' «အကြောင်း / အထောက်အပံ့» not attested; «အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်း» is the "
               "Paccayavāra member of the combined vāra name (^7-1-1-1-8-7-0 …; map-harmonise §F 1)",
    'vatthu': "pi-5 / pi-4 / pi-2 'topics, stump, basis' not attested; «မှီရာ ဝတ္ထု» is the physical base (^7-2-57 …; "
              "notes-g2 §D: pi-3's «အခြေခံ» is another sense)",
    'citto': "pi-5 'of mind, compound final' «စိတ် ရှိသော» and 'Citta the householder' not attested; «စိတ်» is the item of "
             "the mind dyad, 'citto dhammo' (^7-70-23 …)",
    # @@NEW-FULL
}

# Several Burmese values under one sense, or a value the binding sense does not list, checked by hand
# (variants or synonyms of one meaning, or the pi-7 text's own word for the binding meaning).
LUMP_OK = {
    # ---- sample ----
    'paccayo',  # «အကြောင်း»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'vigatapaccayā',  # «ပျောက်ကွယ်ခြင်းဟူသော အကြောင်းကြောင့်» / «ပျောက်ကွယ်ခြင်းဟူသော အကြောင်း»: the condition by its frame: ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း», the bare name, negatives (map-table T1-T4; kept: grammar)
    'Naanantara',  # «ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း» / «ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်းကြောင့် မဟုတ်»: the condition by its frame: ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း», the bare name, negatives (map-table T1-T4; kept: grammar)
    'Napacchājāta',  # «နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း» / «နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်းကြောင့် မဟုတ်»: the condition by its frame: ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း», the bare name, negatives (map-table T1-T4; kept: grammar)
    'Nissaya',  # «အမှီ» / «အမှီဟူသော အကြောင်း»: the condition by its frame: ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း», the bare name, negatives (map-table T1-T4; kept: grammar)
    # @@LUMP-SAMPLE
    # ---- full run: REVIEW headwords checked by hand ----
    'Upanissaya',  # «အားကြီးသော အမှီ» / «အားကြီးသော အမှီဟူသော အကြောင်း»: the condition by its frame: ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း», the bare name, negatives (map-table T1-T4; kept: grammar)
    'purejātapaccayā',  # «ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်းကြောင့်» / «ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း»: the condition by its frame: ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း», the bare name, negatives (map-table T1-T4; kept: grammar)
    'upanissayapaccayā',  # «အားကြီးသော အမှီဟူသော အကြောင်းကြောင့်» / «အားကြီးသော အမှီဟူသော အကြောင်း»: the condition by its frame: ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း», the bare name, negatives (map-table T1-T4; kept: grammar)
    'saṃsaṭṭha',  # «ရောနှောခြင်း»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'samanantarā',  # «ကောင်းစွာ ချက်ချင်း နောက်»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'rūpaṃ',  # «ရုပ်» / «အဆင်းအရောင်»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'kusalākusalaṃ',  # «ကုသိုလ်နှင့် အကုသိုလ်»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'kammaṃ',  # «ကံ»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'vipākā',  # «ကံ၏ အကျိုး ဖြစ်သော»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'uppajjeyya',  # «ဖြစ်ပေါ်နိုင်သည်»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'hetupaccayā',  # «အမြစ်ဟူသော အကြောင်းကြောင့်» / «အမြစ်ဟူသော အကြောင်း»: the condition by its frame: ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း», the bare name, negatives (map-table T1-T4; kept: grammar)
    'uppajjeyyuṃ',  # «ဖြစ်ပေါ်နိုင်သည်»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'ārammaṇapaccayā',  # «အာရုံဟူသော အကြောင်းကြောင့်» / «အာရုံဟူသော အကြောင်း»: the condition by its frame: ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း», the bare name, negatives (map-table T1-T4; kept: grammar)
    'adhipatipaccayā',  # «အကြီးအမှူးဟူသော အကြောင်းကြောင့်» / «အကြီးအမှူးဟူသော အကြောင်း»: the condition by its frame: ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း», the bare name, negatives (map-table T1-T4; kept: grammar)
    'anantarapaccayā',  # «ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်းကြောင့်» / «ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း»: the condition by its frame: ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း», the bare name, negatives (map-table T1-T4; kept: grammar)
    'samanantarapaccayā',  # «ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်းကြောင့်» / «ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း»: the condition by its frame: ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း», the bare name, negatives (map-table T1-T4; kept: grammar)
    'sahajātapaccayā',  # «အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်းကြောင့်» / «အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်း»: the condition by its frame: ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း», the bare name, negatives (map-table T1-T4; kept: grammar)
    'āsevanapaccayā',  # «အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်းကြောင့်» / «အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း»: the condition by its frame: ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း», the bare name, negatives (map-table T1-T4; kept: grammar)
    'kammapaccayā',  # «ကံဟူသော အကြောင်းကြောင့်» / «ကံဟူသော အကြောင်း»: the condition by its frame: ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း», the bare name, negatives (map-table T1-T4; kept: grammar)
    'natthipaccayā',  # «မရှိခြင်းဟူသော အကြောင်းကြောင့်» / «မရှိခြင်းဟူသော အကြောင်း»: the condition by its frame: ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း», the bare name, negatives (map-table T1-T4; kept: grammar)
    'avigatapaccayā',  # «မပျောက်ကွယ်ခြင်းဟူသော အကြောင်းကြောင့်» / «မပျောက်ကွယ်ခြင်းဟူသော အကြောင်း»: the condition by its frame: ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း», the bare name, negatives (map-table T1-T4; kept: grammar)
    'naadhipatipaccayā',  # «အကြီးအမှူးဟူသော အကြောင်းကြောင့် မဟုတ်» / «အကြီးအမှူးဟူသော အကြောင်း မဟုတ်ခြင်း»: the condition by its frame: ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း», the bare name, negatives (map-table T1-T4; kept: grammar)
    'Naadhipati',  # «အကြီးအမှူးဟူသော အကြောင်း မဟုတ်ခြင်း» / «အကြီးအမှူးဟူသော အကြောင်းကြောင့် မဟုတ်»: the condition by its frame: ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း», the bare name, negatives (map-table T1-T4; kept: grammar)
    'kiriyābyākataṃ',  # «ပြုရုံမျှသာ ဖြစ်သော ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'vipākābyākate',  # «ကံ၏ အကျိုး ဖြစ်သော ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'kiriyābyākate',  # «ပြုရုံမျှသာ ဖြစ်သော ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'naārammaṇapaccayā',  # «အာရုံဟူသော အကြောင်းကြောင့် မဟုတ်» / «အာရုံဟူသော အကြောင်း မဟုတ်ခြင်း»: the condition by its frame: ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း», the bare name, negatives (map-table T1-T4; kept: grammar)
    'pañhā',  # «ပြဿနာ»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'Saṃkhittaṃ',  # «အကျဉ်းချုပ်»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'sahajāto',  # «အတူ ပေါ်ပေါက်သော»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'Paripuṇṇaṃ',  # «ပြည့်စုံသော» / «ပြည့်စုံစွာ»: grammatical forms of one lemma, one meaning (kept: grammar / construction)
    'sattarasa',  # «ဆယ့်ခုနစ်ခု»: the count with the text's classifier «ခု» (T6), the same number as the binding «ပါး»
    'datvā',  # «ပြု၍»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'uposathakammaṃ',  # «ဥပုသ်ကို စောင့်ထိန်းသည်» / «ဥပုသ် စောင့်ထိန်းခြင်း» / «ဥပုသ်»: the act compound: the whole act, the noun, or the bare noun before …pe… (U2; kept: construction)
    'paccavekkhati',  # «ပြန်လည် ဆင်ခြင်သည်»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'suciṇṇāni',  # «ကောင်းစွာ ကျင့်ခဲ့ဖူးသော» / «ကောင်းစွာ ပြုခဲ့ဖူးသော»: two text forms of one meaning (map-harmonise §A; kept: text)
    'assādeti',  # «သာယာ» / «သာယာသည်»: grammatical forms of one lemma, one meaning (kept: grammar / construction)
    'vipāko',  # «ကံ၏ အကျိုး ဖြစ်သော» / «ကံ၏ အကျိုး»: grammatical forms of one lemma, one meaning (kept: grammar / construction)
    'tadārammaṇatā',  # «ထိုအာရုံကိုပင် အာရုံပြုသော အဖြစ်» / «ထိုအာရုံကို အာရုံပြုသည့် အနေ»: two text forms of one meaning (map-harmonise §A; kept: text)
    'kusalassa',  # «ကုသိုလ်»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'vipassati',  # «ထိုးထွင်း၍ ရှုသည်»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'vuṭṭhahantassa',  # «ထမြောက်နေသူ»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'deti',  # «ပြုသည်»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'sutaṃ',  # «အကြားအမြင်»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'uppādenti',  # «ဖြစ်စေသည်»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'ṭhānāṭhānakosallassa',  # «ဖြစ်နိုင်ခြင်းနှင့် မဖြစ်နိုင်ခြင်း၌ ကျွမ်းကျင်ခြင်း» / «ဖြစ်နိုင်သော အကြောင်းနှင့် မဖြစ်နိုင်သော အကြောင်း၌ ကျွမ်းကျင်မှု»: two text forms of one meaning (map-harmonise §A; kept: text)
    'attānaṃ',  # «မိမိကိုယ်»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'vipākassa',  # «ကံ၏ အကျိုး» / «ကံ၏ အကျိုး ဖြစ်သော»: grammatical forms of one lemma, one meaning (kept: grammar / construction)
    'bhaṇati',  # «ပြောသည်»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'harati',  # «လုယူသည်»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'ekāgārikaṃ',  # «အိမ်တစ်လုံးတည်း» / «အိမ်တစ်လုံးတည်းကို ဝိုင်း၍ တိုက်သည်»: the act compound: the whole act, the noun, or the bare noun before …pe… (U2; kept: construction)
    'gāmaghātaṃ',  # «ရွာကို ဖျက်ဆီး၍ လုယက်သည်» / «ရွာ»: the act compound: the whole act, the noun, or the bare noun before …pe… (U2; kept: construction)
    'Cakkaṃ',  # «စက်ဝိုင်း»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'Bhojanaṃ',  # «အစားအစာ»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'āhārā',  # «အာဟာရ»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'āhāraṃ',  # «အာဟာရ»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'terasa',  # «ဆယ့်သုံးခု»: the count with the text's classifier «ခု» (T6), the same number as the binding «ပါး»
    'Pacchājāta',  # «နောက်မှ ဖြစ်ပေါ်ခြင်း» / «နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း»: the condition by its frame: ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း», the bare name, negatives (map-table T1-T4; kept: grammar)
    'pannarasa',  # «ဆယ့်ငါးခု»: the count with the text's classifier «ခု» (T6), the same number as the binding «ပါး»
    'ekādasa',  # «ဆယ့်တစ်ခု»: the count with the text's classifier «ခု» (T6), the same number as the binding «ပါး»
    'nevavipākanavipākadhammadhammo',  # «ကံ၏ အကျိုးလည်း မဟုတ် အကျိုး ပေးတတ်သည်လည်း မဟုတ်သော သဘောတရား» / «ကံ၏ အကျိုးလည်း မဟုတ် အကျိုး ပေးတတ်သည်လည်း မဟုတ်သော»: grammatical forms of one lemma, one meaning (kept: grammar / construction)
    'saññojanādidukāni',  # «နှောင်ကြိုး စသည်တို့၏ နှစ်မျိုးတွဲ» / «နှောင်ကြိုး နှစ်မျိုးတွဲ စသည်»: two text forms of one meaning (map-harmonise §A; kept: text)
    'dvādasa',  # «ဆယ့်နှစ်ခု»: the count with the text's classifier «ခု» (T6), the same number as the binding «ပါး»
    'kāyikaṃ',  # «ကိုယ်ပိုင်းဆိုင်ရာ»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'dukkhaṃ',  # «နာကျင်မှု» / «ဆင်းရဲ»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'soḷasa',  # «ဆယ့်ခြောက်ခု»: the count with the text's classifier «ခု» (T6), the same number as the binding «ပါး»
    'cuddasa',  # «ဆယ့်လေးခု»: the count with the text's classifier «ခု» (T6), the same number as the binding «ပါး»
    'dukkhassa',  # «နာကျင်မှု»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'tevīsa',  # «နှစ်ဆယ့်သုံးခု»: the count with the text's classifier «ခု» (T6), the same number as the binding «ပါး»
    'patthanā',  # «တောင့်တခြင်း»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'avasesā',  # «ကြွင်းသော»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'paṭiccavārasadisā',  # «မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူအောင်» / «မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်»: the -sadisa note in each segment's form «…နှင့် တူသည် / တူအောင်» (coordinator; kept: text shape)
    'naindriya',  # «စွမ်းရည်ဟူသော အကြောင်းကြောင့် မဟုတ်» / «စွမ်းရည်ဟူသော အကြောင်း မဟုတ်ခြင်း»: the condition by its frame: ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း», the bare name, negatives (map-table T1-T4; kept: grammar)
    'namagga',  # «မဂ်ဟူသော အကြောင်း မဟုတ်ခြင်း» / «မဂ်ဟူသော အကြောင်းကြောင့် မဟုတ်»: the condition by its frame: ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း», the bare name, negatives (map-table T1-T4; kept: grammar)
    'tiṃsa',  # «သုံးဆယ်ခု»: the count with the text's classifier «ခု» (T6), the same number as the binding «ပါး»
    'passitvā',  # «ကြည့်၍»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'Dassanena',  # «သစ္စာကို မြင်ခြင်း»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'paṭiccavārasadiso',  # «မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်» / «မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူအောင်»: the -sadisa note in each segment's form «…နှင့် တူသည် / တူအောင်» (coordinator; kept: text shape)
    'paṭiccavārasadisaṃ',  # «မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်» / «မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူအောင်»: the -sadisa note in each segment's form «…နှင့် တူသည် / တူအောင်» (coordinator; kept: text shape)
    'pavattipaṭisandhi',  # «ဘဝ ဖြစ်စဉ် … ပဋိသန္ဓေ» / «ဘဝ ဖြစ်ဆဲ ကာလ … ပဋိသန္ဓေ»: two text forms of one meaning (map-harmonise §A; kept: text)
    'Gaṇanāya',  # «ရေတွက်ချက်»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'sekkho',  # «ကျင့်ကြံဆဲသူ၏»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'asekkho',  # «ကျင့်ကြံမှု ပြီးဆုံးသူ၏»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'aññamaññapaccaya',  # «အချင်းချင်း ထောက်ပံ့ခြင်း»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'sukhassa',  # «သာယာမှု»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'micchattaniyato',  # «မှားယွင်းမှု၌ ကျိန်းသေသော»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'sammattaniyato',  # «မှန်ကန်မှု၌ ကျိန်းသေသော»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'voropeti',  # «သတ်သည်»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'uppannassa',  # «ဖြစ်ပေါ်ပြီးသော»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'Ajjhattaṃ',  # «မိမိ၌ ရှိသော»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'paro',  # «သူတစ်ပါး»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'asaññasattā',  # «အသညသတ်»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'dutiyagamanasadisaṃ',  # «ဒုတိယ သွားပုံနှင့် တူသည်» / «ဒုတိယ သွားပုံနှင့် တူအောင်»: the -sadisa note in each segment's form «…နှင့် တူသည် / တူအောင်» (coordinator; kept: text shape)
    'sahetuko',  # «အမြစ် ရှိသော» / «အမြစ် … ရှိသော»: one value with or without the « … » gap at the «လည်း» of ca / ceva (R7 / rule 10; kept: construction)
    'sahetukassa',  # «အမြစ် ရှိသော» / «အမြစ် … ရှိသော»: one value with or without the « … » gap at the «လည်း» of ca / ceva (R7 / rule 10; kept: construction)
    'rūpī',  # «ရုပ် ဖြစ်သော»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'arūpī',  # «ရုပ် မဟုတ်သော»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'Āsavasampayuttaṃ',  # «စိတ်အစွန်းအထင်းနှင့် ယှဉ်တွဲသော» / «စိတ်အစွန်းအထင်းနှင့် … ယှဉ်တွဲသော»: one value with or without the « … » gap at the «လည်း» of ca / ceva (R7 / rule 10; kept: construction)
    'Āsavasampayutto',  # «စိတ်အစွန်းအထင်းနှင့် ယှဉ်တွဲသော» / «စိတ်အစွန်းအထင်းနှင့် … ယှဉ်တွဲသော»: one value with or without the « … » gap at the «လည်း» of ca / ceva (R7 / rule 10; kept: construction)
    'sāsavañca',  # «စိတ်အစွန်းအထင်း၏ အာရုံ … ဖြစ်နိုင်သော» / «စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော»: one value with or without the « … » gap at the «လည်း» of ca / ceva (R7 / rule 10; kept: construction)
    'sāsavo',  # «စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော» / «စိတ်အစွန်းအထင်း၏ အာရုံ … ဖြစ်နိုင်သော»: one value with or without the « … » gap at the «လည်း» of ca / ceva (R7 / rule 10; kept: construction)
    'saññojaniyo',  # «နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်သော» / «နှောင်ကြိုး၏ အာရုံ … ဖြစ်နိုင်သော»: one value with or without the « … » gap at the «လည်း» of ca / ceva (R7 / rule 10; kept: construction)
    'saññojanasampayutto',  # «နှောင်ကြိုးနှင့် ယှဉ်တွဲသော» / «နှောင်ကြိုးနှင့် … ယှဉ်တွဲသော»: one value with or without the « … » gap at the «လည်း» of ca / ceva (R7 / rule 10; kept: construction)
    'saññojaniyañca',  # «နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်သော» / «နှောင်ကြိုး၏ အာရုံ … ဖြစ်နိုင်သော»: one value with or without the « … » gap at the «လည်း» of ca / ceva (R7 / rule 10; kept: construction)
    'ganthasampayutto',  # «အထုံးနှင့် ယှဉ်တွဲသော» / «အထုံးနှင့် … ယှဉ်တွဲသော»: one value with or without the « … » gap at the «လည်း» of ca / ceva (R7 / rule 10; kept: construction)
    'vibhajantena',  # «ခွဲခြမ်းစိတ်ဖြာလျက်» / «ခွဲခြမ်းစိတ်ဖြာသူ»: two text forms of one meaning (map-harmonise §A; kept: text)
    'arūpaṃ',  # «ရုပ် မဟုတ်သော»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'ganthaniyo',  # «အထုံး၏ အာရုံ ဖြစ်နိုင်သော» / «အထုံး၏ အာရုံ … ဖြစ်နိုင်သော»: one value with or without the « … » gap at the «လည်း» of ca / ceva (R7 / rule 10; kept: construction)
    'nīvaraṇiyo',  # «အတားအဆီး၏ အာရုံ ဖြစ်နိုင်သော» / «အတားအဆီး၏ အာရုံ … ဖြစ်နိုင်သော»: one value with or without the « … » gap at the «လည်း» of ca / ceva (R7 / rule 10; kept: construction)
    'nīvaraṇasampayutto',  # «အတားအဆီးနှင့် ယှဉ်တွဲသော» / «အတားအဆီးနှင့် … ယှဉ်တွဲသော»: one value with or without the « … » gap at the «လည်း» of ca / ceva (R7 / rule 10; kept: construction)
    'nīvaraṇiyañca',  # «အတားအဆီး၏ အာရုံ … ဖြစ်နိုင်သော» / «အတားအဆီး၏ အာရုံ ဖြစ်နိုင်သော»: one value with or without the « … » gap at the «လည်း» of ca / ceva (R7 / rule 10; kept: construction)
    'nīvaraṇasampayuttañca',  # «အတားအဆီးနှင့် ယှဉ်တွဲသော» / «အတားအဆီးနှင့် … ယှဉ်တွဲသော»: one value with or without the « … » gap at the «လည်း» of ca / ceva (R7 / rule 10; kept: construction)
    'parāmaṭṭho',  # «မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်သော» / «မှားယွင်းသော ယူဆမှု၏ အာရုံ … ဖြစ်နိုင်သော»: one value with or without the « … » gap at the «လည်း» of ca / ceva (R7 / rule 10; kept: construction)
    'Ajjhattikaṃ',  # «အတွင်းပိုင်း»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'ajjhattikassa',  # «အတွင်းပိုင်း»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'bāhirassa',  # «ပြင်ပ»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'Upādā',  # «မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'Saṃkiliṭṭhañca',  # «ကိလေသာဖြင့် ညစ်နွမ်းသော» / «ကိလေသာဖြင့် … ညစ်နွမ်းသော»: one value with or without the « … » gap at the «လည်း» of ca / ceva (R7 / rule 10; kept: construction)
    'saṃkiliṭṭho',  # «ကိလေသာဖြင့် ညစ်နွမ်းသော» / «ကိလေသာဖြင့် … ညစ်နွမ်းသော»: one value with or without the « … » gap at the «လည်း» of ca / ceva (R7 / rule 10; kept: construction)
    'saṃkilesiko',  # «ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော» / «ကိလေသာ၏ အာရုံ … ဖြစ်နိုင်သော»: one value with or without the « … » gap at the «လည်း» of ca / ceva (R7 / rule 10; kept: construction)
    'kilesasampayutto',  # «ကိလေသာနှင့် ယှဉ်တွဲသော» / «ကိလေသာနှင့် … ယှဉ်တွဲသော»: one value with or without the « … » gap at the «လည်း» of ca / ceva (R7 / rule 10; kept: construction)
    'pahātabbahetukādhipati',  # «ပယ်ရမည့် အမြစ် ရှိသော အကြီးအမှူး» / «ပယ်ရမည့် အမြစ် ရှိသည် … အကြီးအမှူး»: one value with or without the « … » gap at the «လည်း» of ca / ceva (R7 / rule 10; kept: construction)
    'sappītikadukasadisaṃ',  # «ပီတိ ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူသည်» / «ပီတိ ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူအောင်»: the -sadisa note in each segment's form «…နှင့် တူသည် / တူအောင်» (coordinator; kept: text shape)
    'Kāmāvacaraṃ',  # «ကာမဘုံနှင့် ဆိုင်သော»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'Rūpāvacaraṃ',  # «သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'Arūpāvacaraṃ',  # «ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'arūpāvacare',  # «ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'arūpadukasadisā',  # «ရုပ်မရှိသော ဘုံ နှစ်မျိုးတွဲနှင့် တူအောင်» / «ရုပ်မရှိသော ဘုံ နှစ်မျိုးတွဲနှင့် တူသည်»: the -sadisa note in each segment's form «…နှင့် တူသည် / တူအောင်» (coordinator; kept: text shape)
    'Saraṇaṃ',  # «ပဋိပက္ခ ရှိသော»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'hīno',  # «ယုတ်ညံ့သော»: the pi-7 value is a later binding file's value under the same or its own binding tag
    'Cittadukakusalasadisaṃ',  # «စိတ် ဖြစ်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ် သဘောတရားနှင့် တူသည်» / «စိတ် ဖြစ်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ် သဘောတရားနှင့် တူအောင်»: the -sadisa note in each segment's form «…နှင့် တူသည် / တူအောင်» (coordinator; kept: text shape)
    'Lokiyadukaabyākatasadisaṃ',  # «လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော သဘောတရားနှင့် တူသည်» / «လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော သဘောတရားနှင့် တူအောင်»: the -sadisa note in each segment's form «…နှင့် တူသည် / တူအောင်» (coordinator; kept: text shape)
    'anuttaro',  # «ထိုထက် သာလွန်သည် မရှိသော»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'chattiṃsa',  # «သုံးဆယ့်ခြောက်ခု»: the count with the text's classifier «ခု» (T6), the same number as the binding «ပါး»
    'aṭṭhārasa',  # «ဆယ့်ရှစ်ခု»: the count with the text's classifier «ခု» (T6), the same number as the binding «ပါး»
    'vattabbaṃ',  # «ခေါ်ဆို၍ မရသော»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'ekūnavīsati',  # «ဆယ့်ကိုးခု»: the count with the text's classifier «ခု» (T6), the same number as the binding «ပါး»
    'sahetukañca',  # «အမြစ် ရှိသော» / «အမြစ် … ရှိသော»: one value with or without the « … » gap at the «လည်း» of ca / ceva (R7 / rule 10; kept: construction)
    'mūlakaṃ',  # «အခြေခံ အကြောင်း»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    'nānākaraṇaṃ',  # «ကွဲပြားချက်»: the pi-7 text's own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the binding value is not in the segment)
    # @@LUMP-FULL
}

# Headwords new in pi-7 (no binding line) whose single Marathi pi-7 tag does not describe the headword as the Burmese
# values show it: headword -> (adjusted English tag, reason).
MR_ADJUST = {
    # ---- sample ----
    # @@ADJ-SAMPLE
    # ---- full run ----
    'nabhāvanāya': ('not by development, the negated instrumental in the triad and dyad items (instrumental)',
        'the Marathi tag carries a note on the Marathi mapping that the Burmese value does not show; adjusted to the Burmese; Marathi tag: not by development, the negated instrumental in the triad and dyad items, mapped in several wordings'),
    'Nadassanena': ('not by seeing the truths, the negated instrumental in the dyad and the items without roots to be abandoned by seeing (instrumental)',
        'the Marathi tag carries a note on the Marathi mapping that the Burmese value does not show; adjusted to the Burmese; Marathi tag: not by seeing the truths, the negated instrumental in the dyad and the items without roots to be abandoned by seeing, mapped in several wordings'),
    'nevācayagāmināpacayagāmī': ('leading neither to accumulation nor to dismantling (masculine sg.)',
        'the Marathi tag carries a note on the Marathi mapping that the Burmese value does not show; adjusted to the Burmese; Marathi tag: leading neither to accumulation nor to dismantling, mapped as a joined or separate pair (masculine sg.)'),
    'Nevācayagāmināpacayagāmiṃ': ('leading neither to accumulation nor to dismantling (neuter sg.)',
        'the Marathi tag carries a note on the Marathi mapping that the Burmese value does not show; adjusted to the Burmese; Marathi tag: leading neither to accumulation nor to dismantling, mapped as a joined or separate pair (neuter sg.)'),
    'nevācayagāmināpacayagāmissa': ('of what leads neither to accumulation nor to dismantling (genitive sg.)',
        'the Marathi tag carries a note on the Marathi mapping that the Burmese value does not show; adjusted to the Burmese; Marathi tag: of what leads neither to accumulation nor to dismantling, mapped as a joined or separate pair (genitive sg.)'),
    'nevasekkhanāsekkho': ('belonging neither to one in training nor to one beyond training (masculine sg.)',
        'the Marathi tag carries a note on the Marathi mapping that the Burmese value does not show; adjusted to the Burmese; Marathi tag: belonging neither to one in training nor to one beyond training, mapped as a joined or separate pair (masculine sg.)'),
    'Nevasekkhanāsekkhaṃ': ('belonging neither to one in training nor to one beyond training (neuter sg.)',
        'the Marathi tag carries a note on the Marathi mapping that the Burmese value does not show; adjusted to the Burmese; Marathi tag: belonging neither to one in training nor to one beyond training, mapped as a joined or separate pair (neuter sg.)'),
    'nevasekkhanāsekkhañca': ('and belonging neither to one in training nor to one beyond training (neuter sg.)',
        'the Marathi tag carries a note on the Marathi mapping that the Burmese value does not show; adjusted to the Burmese; Marathi tag: and belonging neither to one in training nor to one beyond training, mapped as a joined or separate pair (neuter sg.)'),
    'nevasekkhanāsekkhassa': ('of what belongs neither to one in training nor to one beyond training (genitive sg.)',
        'the Marathi tag carries a note on the Marathi mapping that the Burmese value does not show; adjusted to the Burmese; Marathi tag: of what belongs neither to one in training nor to one beyond training, mapped as a joined or separate pair (genitive sg.)'),
    'Āsavañca': ('and a mental taint, item of the taint dyad (accusative sg. with -ñca)',
        'the Marathi tag carries a note on the Marathi mapping that the Burmese value does not show; adjusted to the Burmese; Marathi tag: and a mental taint, item of the taint dyad, also its negated form (accusative sg. with -ñca)'),
    'Saññojanaṃ': ('fetter, item of the fetter dyad, the dyad term itself a fetter (accusative sg.)',
        'the Marathi tag carries a note on the Marathi mapping that the Burmese value does not show; adjusted to the Burmese; Marathi tag: fetter, item of the fetter dyad, the dyad term itself a fetter, also its negated form (accusative sg.)'),
    'saññojano': ('fetter, item of the fetter dyad, the dyad term itself a fetter (nominative sg.)',
        'the Marathi tag carries a note on the Marathi mapping that the Burmese value does not show; adjusted to the Burmese; Marathi tag: fetter, item of the fetter dyad, the dyad term itself a fetter, also its negated form (nominative sg.)'),
    'Ganthaṃ': ('tie, knot, item of the tie dyad, the dyad term itself a tie (accusative sg.)',
        'the Marathi tag carries a note on the Marathi mapping that the Burmese value does not show; adjusted to the Burmese; Marathi tag: tie, knot, item of the tie dyad, the dyad term itself a tie, also its negated form (accusative sg.)'),
    'Ganthañca': ('and a tie, knot, item of the tie dyad (accusative sg. with -ñca)',
        'the Marathi tag carries a note on the Marathi mapping that the Burmese value does not show; adjusted to the Burmese; Marathi tag: and a tie, knot, item of the tie dyad, also its negated form (accusative sg. with -ñca)'),
    'nīvaraṇo': ('hindrance, item of the hindrance dyad, the dyad term itself a hindrance (nominative sg.)',
        'the Marathi tag carries a note on the Marathi mapping that the Burmese value does not show; adjusted to the Burmese; Marathi tag: hindrance, item of the hindrance dyad, the dyad term itself a hindrance, also its negated form (nominative sg.)'),
    'Nīvaraṇañceva': ('both a hindrance, item of the hindrance dyad (neuter sg. with -ñceva)',
        'the Marathi tag carries a note on the Marathi mapping that the Burmese value does not show; adjusted to the Burmese; Marathi tag: both a hindrance, item of the hindrance dyad, mapped as positive or as positive plus negated and plain (neuter sg. with -ñceva)'),
    'Parāmāsañca': ('and wrong grasping, item of the wrong-grasping dyad (accusative sg. with -ñca)',
        'the Marathi tag carries a note on the Marathi mapping that the Burmese value does not show; adjusted to the Burmese; Marathi tag: and wrong grasping, item of the wrong-grasping dyad, mapped joined with the plain noun (accusative sg. with -ñca)'),
    'upādāno': ('clinging, item of the clinging dyad, the dyad term itself a clinging (masculine sg.)',
        'the Marathi tag carries a note on the Marathi mapping that the Burmese value does not show; adjusted to the Burmese; Marathi tag: clinging, item of the clinging dyad, the dyad term itself a clinging, also its negated form (masculine sg.)'),
    'Upādānañca': ('and clinging, item of the clinging dyad, the dyad term itself a clinging (nominative/accusative sg. with -ñca)',
        'the Marathi tag carries a note on the Marathi mapping that the Burmese value does not show; adjusted to the Burmese; Marathi tag: and clinging, item of the clinging dyad, the dyad term itself a clinging, mapped alone or joined with the kind of clinging (nominative/accusative sg. with -ñca)'),
    'Kilesaṃ': ('defilement, item of the defilement dyad, the dyad term itself a defilement (accusative sg.)',
        'the Marathi tag carries a note on the Marathi mapping that the Burmese value does not show; adjusted to the Burmese; Marathi tag: defilement, item of the defilement dyad, the dyad term itself a defilement, also its negated form (accusative sg.)'),
    # @@ADJ-FULL
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
    stats['mr_adjusted'] = 0
    adjusted = set()
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
        for k in reversed(list(found)):                         # pi-6 first where several list a value
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
                tag = tags[0]
                if hw in MR_ADJUST:
                    tag = MR_ADJUST[hw][0]
                    adjusted.add(hw)
                    stats['mr_adjusted'] += 1
                senses = [(tag, list(vals))]
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
    for h in MR_ADJUST:
        if h in rows and h not in adjusted:
            errs.append(f'{h}: MR_ADJUST entry for a headword that does not take a single Marathi tag')
        if not MR_ADJUST[h][1].strip():
            errs.append(f'{h}: MR_ADJUST entry without a reason')
    unused = [h for h in list(MANUAL) + list(LUMP_OK) + list(MR_ADJUST) if h not in rows]
    if unused:
        print(f'note: MANUAL / LUMP_OK entries not in this input (fine for a part run): {unused}')
    with open(outp, 'w', encoding='utf-8', newline='\n') as f:
        f.write(f'# Pāli→Burmese pi-7 sense decisions, written by gen_decisions_my.py from {pathlib.Path(aggp).name}\n')
        f.write('# English tags: pi-6, then pi-5, pi-4, pi-3, pi-2, pi-1 Burmese senses (binding), else Marathi pi-7 senses '
                '(tags only), or MANUAL;\n')
        f.write('# values: pi-7 Burmese keyword map only.\n')
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
