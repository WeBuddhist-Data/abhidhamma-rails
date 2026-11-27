"""Write the Pāli→Burmese pi-6 decisions file for senses_my.py (brief: pi-6-my/burmese-senses-brief.md).
Adapted from pi-5-my/senses/gen_decisions_my.py (same engine and MANUAL / LUMP_OK / TAG_CHANGED / NEW_SENSE mechanism);
the binding chain is now pi-5, then pi-4, pi-3, pi-2, pi-1; the tags for headwords new in pi-6 come from the Marathi pi-6
senses (tags only).

usage: python -I -X utf8 gen_decisions_my.py <agg.tsv> <decisions.txt>

For every headword of agg.tsv that has Burmese values (NDE-only headwords are skipped):
  1. a hand decision in MANUAL below wins;
  2. otherwise the approved Burmese senses are BINDING, pi-5 first, then pi-4, pi-3, pi-2, pi-1 (each looked up exact,
     else the one case-insensitive match: the aggregation keeps the first spelling seen). The reference is the line of
     the first of pi-5 / pi-4 / pi-3 / pi-2 / pi-1 that has the headword. Every pi-6 value that the reference lists goes
     under the reference's sense with its English tag, in the reference's sense order (a sense with no pi-6 value is
     left out). A pi-6 value the reference does not list:
       - a later binding file lists it: that file's sense (tag) is added after the reference's, or the value joins the
         reference sense with the same tag (REVIEW);
       - otherwise, the reference has one sense: the value joins it (REVIEW unless the headword is in LUMP_OK);
       - otherwise (the reference has several senses): UNRESOLVED (write MANUAL);
  3. otherwise, if the Marathi pi-6 senses file gives the headword ONE English tag, the line is that tag + every
     attested Burmese value (one sense; several values -> REVIEW unless LUMP_OK); where that Marathi tag does not
     describe the headword the Burmese values show (e.g. the tag of a compound member, or a positive tag on a negated
     verb), MR_ADJUST gives the adjusted English tag with its logged reason (NEW in pi-6; only for such headwords);
  4. otherwise (several Marathi senses, or no Marathi line) the headword is UNRESOLVED: write MANUAL.
Only the ENGLISH tags are read from the Marathi file; its Marathi values are dropped on parsing and never written.
A MANUAL entry for a pi-5 / pi-4 / pi-3 / pi-2 / pi-1 headword must keep the binding split: every value the binding
senses list (pi-5's sense for it, else pi-4's, pi-3's, pi-2's, pi-1's) sits under a sense whose tag starts with that
binding tag (an appended «, …» is allowed) unless the headword is in TAG_CHANGED (logged reason); and a MANUAL sense
that holds only values the binding senses do not list, with a tag that starts with none of the binding tags, is a NEW
sense and the headword must be in NEW_SENSE (logged reason).
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
    ('p5', ROOT / 'AI_translation/burmese/pi-5-pali-word-burmese-senses-plain.md'),
    ('p4', ROOT / 'AI_translation/burmese/pi-4-pali-word-burmese-senses-plain.md'),
    ('p3', ROOT / 'AI_translation/burmese/pi-3-pali-word-burmese-senses-plain.md'),
    ('p2', ROOT / 'AI_translation/burmese/pi-2-pali-word-burmese-senses-plain.md'),
    ('p1', ROOT / 'AI_translation/burmese/pi-1-pali-word-burmese-senses-plain.md'),
])
BOOK = {'p5': 'pi-5', 'p4': 'pi-4', 'p3': 'pi-3', 'p2': 'pi-2', 'p1': 'pi-1'}
MR_SENSES = ROOT / 'AI_translation/marathi/pi-6-pali-word-marathi-senses-plain.md'
VAL_RE = re.compile(r'^(.*)=(\d+)\[[^\]]*\]$')
NONLATIN = re.compile(r'[\u0900-\u097f\u1000-\u109f]')

# Hand decisions: headword -> [(English tag, [Burmese values])]. Values must be attested.
# Binding senses first (pi-5, else pi-4, pi-3, pi-2, pi-1 order and tag), then the senses new in pi-6.
MANUAL = OrderedDict([
    # ======== sample (agg-sample.tsv, the first 80 headwords) ========
    ('nāmā', [
        # pi-5 'by name' «အမည်» not attested; nāma = mentality «စိတ်ပိုင်း» (map-table rule 11, pi-1 nāma ^1-M2-109)
        ('mentality, the mental side, in the root chapter (nominative pl.)', ['စိတ်ပိုင်း']),
    ]),
    ('sambhavo', [
        # pi-2 sense kept; the hetuvāra word «ဖြစ်တည်ရာ» (^6-1-49, ^6-1-99) is the place of origination
        ('coming into being, origination (nominative sg.), here the source of origination, the fourth of the ten '
         'synonyms for a root in the hetuvāra', ['ဖြစ်တည်ရာ']),
    ]),
    ('kusalahetū', [
        # pi-2 sense kept; hetu gets its own word «အကြောင်း» in the hetuvāra list (map-table, sample departure 1)
        ("the wholesome roots (nominative pl.), here 'having the skilful as cause', the second of the ten synonyms for "
         'a root in the hetuvāra', ['ကုသိုလ်၏ အကြောင်း']),
    ]),
    ('paccayo', [
        # pi-5 support sense kept; parapaccayo 'reliance on others' not attested; paccaya «အထောက်အပံ့» (pi-1 ^1-1344)
        ('support, conditioning factor (nominative), here the ninth of the ten synonyms for a root in the hetuvāra',
         ['အထောက်အပံ့']),
    ]),
    # @@MANUAL-SAMPLE
    # ======== full run (agg-part1.tsv) ========
    # ---- REVIEW headwords: a pi-6 value the binding senses do not list, with a meaning of its own ----
    ('ekamūlakaṃ', [
        # pi-3 «တစ်မျိုးတွဲကို အခြေခံသော» (Dhātukathā, items one at a time) not attested; eka = the same root here
        ('based on one root in common (neuter sg.)', ['တူညီသော အမြစ်ကို အခြေခံသော']),
    ]),
    ('nāmapaccayā', [
        # pi-2 sense kept; the hetuvāra predicate «စိတ်ပိုင်း၏ အထောက်အပံ့» (^6-1-99) gives paccaya its own word
        ("conditioned by mentality (ablative), here the predicate 'having mentality as support', the ninth of the ten "
         'synonyms for a root in the hetuvāra (nominative pl.)', ['စိတ်ပိုင်း၏ အထောက်အပံ့']),
    ]),
    ('anulomaṃ', [
        # pi-5 debate order «အစဉ်အတိုင်း» not attested; the Yamaka's affirmative form (map-table, sample departure 2)
        ('the affirmative form of the paired questions, in the headings of each section (heading member)',
         ['အဟုတ်ပြ ပုံစံ']),
    ]),
    ('paccanīkaṃ', [
        # pi-5 inverted debate order «ပြောင်းပြန်» not attested; the Yamaka's negated form
        ('the negated form of the paired questions, in the headings of each section (heading member)',
         ['အငြင်းပြ ပုံစံ']),
    ]),
    ('viññāṇañca', [
        # pi-5 / pi-1 homograph viññāṇañc(āyatana) not attested; here viññāṇaṃ + ca (map-table R1)
        ('consciousness, knowing, viññāṇaṃ with ca (nominative sg.)', ['သိစိတ်']),
    ]),
    ('arūpaṃ', [
        # pi-5 / pi-2 adjective 'non-material' «ရုပ် မဟုတ်သော» not attested; the plane (map-table rule 11)
        ('the immaterial plane, existence without material form (accusative sg.)', ['ရုပ်မရှိသော ဘုံ']),
    ]),
    ('arūpā', [
        # pi-2 adjective «ရုပ် မဟုတ်သော» not attested; the ablative of the plane «Arūpā cavantānaṃ» (map-table R5)
        ("from the immaterial plane, in 'Arūpā cavantānaṃ' (ablative sg.)", ['ရုပ်မရှိသော ဘုံ']),
    ]),
    ('cakkaṃ', [
        # pi-5 / pi-2 wheel «စကြာ / တရားစက်» not attested; the cycle of the Yamaka's cakkavāras
        ('the cycle, the round of questions repeated with each term (heading member)', ['လှည့်ပတ်ခြင်း']),
    ]),
    ('dhātū', [
        # pi-5 sphere, plane «ဘုံ» not attested; the elements of ch. 4 (^6-4-4 …)
        ('elements, the eighteen elements of the chapter on elements (nominative pl.)', ['ဓာတ်']),
    ]),
    ('rūpadhātuṃ', [
        # pi-5 sense (element or plane) for the plane of the dhātupucchā (ch. 7); the visible-form element (ch. 4) is new
        ('the fine-material element or plane (accusative, also heading), here the fine-material plane of the '
         'questions on the planes (ch. 7)', ['သိမ်မွေ့သော ရုပ်ဘုံ']),
        ('the visible-form element, the object of the eye, one of the eighteen elements of ch. 4 (accusative sg.)',
         ['အဆင်းအရောင် ဓာတ်']),
    ]),
    ('aññaṃ', [
        # pi-5 / pi-2 / pi-1 'other, different' «တခြားစီ / အခြား / တခြား» not attested; the faculty word aññā
        ('final knowledge, the full understanding of aññindriya (nominative/accusative sg.)',
         ['အပြည့်အဝ သိမြင်ခြင်း']),
    ]),
    ('kāyasaṅkhāraṃ', [
        # pi-5 «ကိုယ်ဖြင့် ပြုပြင်ဖန်တီးမှု» (volition by the body) not attested; the bodily formation = breathing
        ('the bodily formation, the in-and-out breathing of the chapter on formations (accusative sg.)',
         ['ကိုယ်၏ ပြုပြင်ဖန်တီးမှု']),
    ]),
    ('vacīsaṅkhāraṃ', [
        # pi-5 «နှုတ်ဖြင့် ပြုပြင်ဖန်တီးမှု» (volition by speech) not attested; the verbal formation = vitakka-vicāra
        ('the verbal formation, applied and sustained thinking of the chapter on formations (accusative sg.)',
         ['နှုတ်၏ ပြုပြင်ဖန်တီးမှု']),
    ]),
    ('kāmāvacarānaṃ', [
        # pi-2 sense kept for the adjective of pacchimacitta (^6-6-39 …, map-harmonise §A 2); the beings are new (R5)
        ("of those belonging to the sense sphere (genitive pl.), here the adjective of pacchimacitta, 'the last mind "
         "of the sense sphere'", ['ကာမဘုံနှင့် ဆိုင်သော']),
        ('the beings of the sense-sphere plane, those who live there (genitive pl.)',
         ['ကာမဘုံ၌ ရှိသူ', 'ကာမဘုံ၌ ရှိသော']),
    ]),
    # ---- the plane words: the binding adjective sense, used here for the plane itself (R5) ----
    ('kāmāvacare', [
        ("belonging to the sense sphere (locative), here the sense-sphere plane itself, 'in the sense-sphere plane'",
         ['ကာမဘုံ']),
    ]),
    ('rūpāvacare', [
        ("belonging to the fine-material sphere (locative), here the fine-material plane itself, 'in the "
         "fine-material plane'", ['သိမ်မွေ့သော ရုပ်ဘုံ']),
    ]),
    ('arūpāvacare', [
        ("belonging to the immaterial sphere (locative), here the immaterial plane itself, 'in the immaterial plane'",
         ['ရုပ်မရှိသော ဘုံ']),
    ]),
    ('rūpāvacaraṃ', [
        ("belonging to the fine-material sphere (neuter sg.), here the fine-material plane itself, accusative of the "
         "goal, 'reborn in the fine-material plane'", ['သိမ်မွေ့သော ရုပ်ဘုံ']),
    ]),
    ('arūpāvacaraṃ', [
        ("belonging to the immaterial sphere (neuter sg.), here the immaterial plane itself, accusative of the goal, "
         "'reborn in the immaterial plane'", ['ရုပ်မရှိသော ဘုံ']),
    ]),
    ('kāmāvacaraṃ', [
        ("belonging to the sense sphere (neuter sg.), here the sense-sphere plane itself, accusative of the goal, "
         "'reborn in the sense-sphere plane'", ['ကာမဘုံ']),
    ]),
    ('kāmāvacarā', [
        ("belonging to the sense sphere (feminine or pl.), here the sense-sphere plane itself, ablative 'from the "
         "sense-sphere plane'", ['ကာမဘုံ']),
    ]),
    ('rūpāvacarā', [
        ("belonging to the fine-material sphere (feminine or pl.), here the fine-material plane itself, ablative "
         "'from the fine-material plane'", ['သိမ်မွေ့သော ရုပ်ဘုံ']),
    ]),
    # @@MANUAL-FULL
])

# Binding headwords whose MANUAL entry deliberately departs from a binding tag (headword: reason).
TAG_CHANGED = {
    # @@TAGCH
}

# Binding headwords whose MANUAL entry adds a sense with values the binding senses do not list (headword: reason).
NEW_SENSE = {
    # ---- sample ----
    'nāmā': "pi-5 'by name' «အမည်» not attested in pi-6; «စိတ်ပိုင်း» is nāma as mentality in the root chapter "
            "(^6-1-10-0, ^6-1-37 …; map-table rule 11, pi-1 nāma ^1-M2-109)",
    # @@NEW-SAMPLE
    # ---- full run ----
    'ekamūlakaṃ': "pi-3 'section label for items taken one at a time' «တစ်မျိုးတွဲကို အခြေခံသော» (Dhātukathā) not "
                  "attested; «တူညီသော အမြစ်ကို အခြေခံသော» is eka = the same root (^6-1-57 …; map-table)",
    'anulomaṃ': "pi-5 'direct order of argument' «အစဉ်အတိုင်း» not attested; «အဟုတ်ပြ ပုံစံ» is the affirmative form "
                "of the Yamaka's paired questions (^6-2-2-1-0 …; map-table, notes-sample departure 2)",
    'paccanīkaṃ': "pi-5 'inverted order of argument' «ပြောင်းပြန်» not attested; «အငြင်းပြ ပုံစံ» is the negated form "
                  "of the paired questions (^6-2-2-2-0 …; map-table)",
    'viññāṇañca': "pi-5 / pi-1 'infinity of consciousness' (viññāṇañcāyatana) not attested; «သိစိတ်» is viññāṇaṃ + ca "
                  "(^6-2-39, ^6-2-49; map-table R1)",
    'arūpaṃ': "pi-5 / pi-2 adjective 'immaterial' «ရုပ် မဟုတ်သော» not attested; «ရုပ်မရှိသော ဘုံ» is the immaterial "
              "plane (^6-2-50 …; map-table rule 11, my6-zeroshot-terms §6)",
    'arūpā': "pi-2 adjective «ရုပ် မဟုတ်သော» not attested; «ရုပ်မရှိသော ဘုံ» is the ablative of the plane, 'Arūpā "
             "cavantānaṃ' (^6-2-104 …; map-table R5)",
    'cakkaṃ': "pi-5 / pi-2 wheel «စကြာ / တရားစက်» (brahmacakka) not attested; «လှည့်ပတ်ခြင်း» is the cycle, the round "
              "of questions (^6-3-4 …; brief)",
    'dhātū': "pi-5 'sphere, plane' «ဘုံ» not attested; «ဓာတ်» is the elements of the chapter on elements (^6-4-4 …; "
             "brief: dhātu «ဓာတ်» vs pi-5 «ဘုံ»)",
    'rūpadhātuṃ': "pi-5 sense kept for the plane «သိမ်မွေ့သော ရုပ်ဘုံ» (ch. 7); «အဆင်းအရောင် ဓာတ်» is the "
                  "visible-form element of the eighteen (^6-4-10, ^6-4-11; map-harmonise §B kept: sense)",
    'aññaṃ': "pi-5 'other, different' «တခြားစီ / အခြား» not attested; «အပြည့်အဝ သိမြင်ခြင်း» is aññā, final "
             "knowledge, of the faculty aññindriya (^6-10-2 …; brief)",
    'kāyasaṅkhāraṃ': "pi-5 'volitional construction through the body' «ကိုယ်ဖြင့် …» not attested; «ကိုယ်၏ "
                     "ပြုပြင်ဖန်တီးမှု» is the bodily formation, the breathing of the saṅkhārayamaka (^6-6-159)",
    'vacīsaṅkhāraṃ': "pi-5 'volitional construction through speech' «နှုတ်ဖြင့် …» not attested; «နှုတ်၏ "
                     "ပြုပြင်ဖန်တီးမှု» is the verbal formation, vitakka-vicāra, of the saṅkhārayamaka (^6-6-159)",
    'kāmāvacarānaṃ': "pi-2 sense kept for the adjective «ကာမဘုံနှင့် ဆိုင်သော» (^6-6-39 …); «ကာမဘုံ၌ ရှိသူ / ရှိသော» "
                     "are the beings of the plane (^6-3-41 …; map-table R5, map-harmonise §B kept: grammar / sense)",
    # @@NEW-FULL
}

# Several Burmese values under one sense, or a value the binding sense does not list, checked by hand
# (variants or synonyms of one meaning, or the pi-6 text's own word for the binding meaning).
LUMP_OK = {
    # ---- sample ----
    'abyākatā dhammā',  # «… မဟုတ်သော သဘောတရား» whole = the pi-5 gapped «… မဟုတ်သော … သဘောတရား»: one phrase (rule 10), = pi-1
    'avasesā',          # «ကြွင်းကျန်သော» = pi-5 «ကြွင်းသော»: the remaining ones, = the pi-4 / pi-1 value (same tag)
    # @@LUMP-SAMPLE
    # ---- full run: REVIEW headwords checked by hand ----
    'avaseso',          # «ကြွင်းကျန်သော» = pi-5 «အကြွင်း»: the remaining, = the pi-1 value (same tag)
    'avasesaṃ',         # «ကြွင်းကျန်သော» = pi-5 «အကြွင်း»: the remaining, = the pi-1 value (same tag)
    'avasese',          # «ကြွင်းကျန်သော» = pi-5 «အကြွင်း»: the remaining (locative), one meaning
    'upapajjantānaṃ',   # «…ဖြစ်ပေါ်ဆဲသူ» / «…ဖြစ်ပေါ်ဆဲ»: one participle, agent noun or attributive (R3; kept: grammar)
    'upapajjantīnaṃ',   # «…ဖြစ်ပေါ်ဆဲ» / «…ဖြစ်ပေါ်ဆဲသူ»: one participle, attributive or agent noun (kept: grammar)
    'pañcavokārānaṃ',   # «… ဘဝ၌ ရှိသော» / «… ဘဝ၌ ရှိသူ»: the beings, attributive or agent noun (R5; kept: grammar)
    'rūpāvacarānaṃ',    # «… ရုပ်ဘုံ၌ ရှိသူ» / «… ရုပ်ဘုံ … ရှိသူ / ရှိသော»: the beings, shared ending (kept: construction)
    'arūpāvacarānaṃ',   # «… ဘုံ၌ ရှိသူ» / «… ဘုံ၌ ရှိသော»: the beings, agent noun or attributive (kept: grammar)
    'uppajjissati',     # «ဖြစ်ပေါ်လိမ့်မည်» / «ဖြစ်ပေါ်မည့်»: the future, finite or in a relative clause (R2; kept: grammar)
    'itaresaṃ',         # «အခြားသူ» / «အခြား»: the others, agent noun or attributive before a noun (kept: grammar)
    'pacchimabhavikānaṃ',  # «နောက်ဆုံး ဘဝ ရှိသူ» / «… ရှိသော»: agent noun or attributive (kept: grammar)
    'anabhisametāvīnaṃ',   # «…မသိမြင်ရသေးသူ» / «…မသိမြင်ရသေးသော»: agent noun or attributive (kept: grammar)
    'abhisametāvīnaṃ',  # «…သိမြင်ပြီးသူ» / «…သိမြင်ပြီးသော»: agent noun or attributive (kept: grammar)
    'yattha',           # «အကြင်နေရာ» = pi-5 «အကြင်»: the relative 'where', with its noun (g1 U3)
    'raso',             # «အရသာ» = the pi-2 / pi-1 taste sense (later binding file); pi-5 juice not attested
    'dukkhaṃ',          # «နာကျင်မှု» = the pi-2 pain sense (same tag as pi-5's «နာကျင်သော»): bodily pain in ch. 5 and 10
    'sukhaṃ',           # «သာယာမှု» = the pi-4 pleasure sense (same tag as pi-5's «သာယာသော»)
    'kāyasaṅkhāro',     # «ကိုယ်၏ …» = pi-5 «ကိုယ် …»: one lemma, the text's form (map-harmonise §A 12)
    'assāsapassāsā',    # «ဝင်လေ ထွက်လေ» = pi-5 «ထွက်သက် ဝင်သက်»: synonyms, in-breaths and out-breaths
    'arūpadhātuṃ',      # «ရုပ်မရှိသော ဘုံ» = pi-5 «ရုပ်မရှိသော ဓာတ်»: the plane, within the pi-5 'element or plane'
    'kāmadhātuṃ',       # «ကာမဘုံ» = pi-5 «ကာမ ဓာတ်»: the plane, within the pi-5 'element or plane'
    'uppajjamānaṃ',     # «ဖြစ်ပေါ်ဆဲ» = pi-5 «ဖြစ်ပေါ်သော»: one present participle (R3)
    'nirujjhamānaṃ',    # «ချုပ်ငြိမ်းဆဲ» = pi-5 «ချုပ်ငြိမ်းသော / …နေသော»: one present participle (R3)
    'akusalaṃ cittaṃ',  # «အကုသိုလ်စိတ်» = pi-5 «အကုသိုလ် စိတ်»: spacing, = pi-2 / pi-1
    'kusalaṃ cittaṃ',   # «ကုသိုလ်စိတ်» = pi-5 «ကုသိုလ် စိတ်»: spacing, = pi-2 / pi-1
    'atītānāgataṃ',     # «အတိတ် … အနာဂတ်» = pi-5 «အတိတ်နှင့် အနာဂတ်»: one phrase, gapped (rule 10)
    'nirujjhissanti',   # «ချုပ်ငြိမ်းလိမ့်မည်» = pi-5 «ချုပ်ငြိမ်းသည်»: the future (R2), one verb
    'sacchikaroti',     # «မျက်မှောက်ပြုသည်» = pi-5 «မျက်မှောက် ပြုသည်»: spacing (map-harmonise §A 13)
    'sacchikaronti',    # «မျက်မှောက်ပြုသည်» = pi-5 «မျက်မှောက် ပြုသည်»: spacing (map-harmonise §A 13)
    # @@LUMP-FULL
}

# Headwords new in pi-6 (no binding line) whose single Marathi pi-6 tag does not describe the headword as the Burmese
# values show it: headword -> (adjusted English tag, reason). NEW in pi-6.
MR_ADJUST = {
    # ---- sample ----
    'kusalamūlamūlā': ('the root of a root that is skilful (nominative pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root that is skilful'),
    'ekamūlamūlā': ('having one root of a root in common (nominative pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root of a root, in the method of that name'),
    'aññamaññamūlamūlā': ('each serving as the root of a root for the other (nominative pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: each serving as root for the other'),
    'kusalamūlakā': ('based on a root that is skilful (nominative pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root that is skilful'),
    'kusalamūlamūlakā': ('based on the root of a root that is skilful (nominative pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root that is skilful'),
    'ekamūlamūlakā': ('based on one root of a root in common (nominative pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root of a root, in the method of that name'),
    'aññamaññamūlamūlakā': ('each stemming from the other as the root of a root (nominative pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: each stemming from the other as a root'),
    'akusalamūlamūlā': ('the root of a root that is unskilful (nominative pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root that is unskilful'),
    'akusalamūlakā': ('based on a root that is unskilful (nominative pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root that is unskilful'),
    'akusalamūlamūlakā': ('based on the root of a root that is unskilful (nominative pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root that is unskilful'),
    'abyākatamūlamūlā': ('the root of a root that is neither skilful nor unskilful (nominative pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root of a root, in the method of that name'),
    'abyākatamūlakā': ('based on a root that is neither skilful nor unskilful (nominative pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root that is neither skilful nor unskilful'),
    'abyākatamūlamūlakā': ('based on the root of a root that is neither skilful nor unskilful (nominative pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root of a root, in the method of that name'),
    'nāmamūlamūlā': ('the root of a root belonging to the mental side (nominative pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root of a root, in the method of that name'),
    'nāmamūlakā': ('based on a root belonging to the mental side (nominative pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root belonging to the mental side'),
    'nāmamūlamūlakā': ('based on the root of a root belonging to the mental side (nominative pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root of a root, in the method of that name'),
    'kusalanidānā': ('having a skilful source, the third of ten synonyms for a root (nominative pl.)',
        'the Marathi tag is that of kusala alone; the Burmese value is the hetuvāra synonym; Marathi tag: skilful, karmically good (adjective)'),
    'kusalasamuṭṭhānā': ('having a skilful origin, the sixth of ten synonyms for a root (nominative pl.)',
        'the Marathi tag is that of kusala alone; the Burmese value is the hetuvāra synonym; Marathi tag: skilful, karmically good (adjective)'),
    'kusalārammaṇā': ('having a skilful object, the eighth of ten synonyms for a root (nominative pl.)',
        'the Marathi tag is that of kusala alone; the Burmese value is the hetuvāra synonym; Marathi tag: skilful, karmically good (adjective)'),
    'kusalasamudayā': ('having a skilful arising, the tenth of ten synonyms for a root (nominative pl.)',
        'the Marathi tag is that of kusala alone; the Burmese value is the hetuvāra synonym; Marathi tag: skilful, karmically good (adjective)'),
    # ---- full run ----
    'kusalamūlasahajātā dhammā': ('states arisen together with a root that is skilful (nominative pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: states that are skilful'),
    'kusalamūlamūlāti': ('the root of a root that is skilful (nominative pl., quoted with iti)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root that is skilful'),
    'kusalamūlamūlāni': ('the root of a root that is skilful (neuter pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root that is skilful'),
    'ekamūlamūlāti': ('having one root of a root in common (nominative pl., quoted with iti)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root of a root, in the method of that name'),
    'ekamūlamūlaṃ': ('having one root of a root in common (neuter sg.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root of a root, in the method of that name'),
    'ekamūlamūlañceva': ('having one root of a root in common (neuter sg., with ceva)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root of a root, in the method of that name'),
    'aññamaññamūlamūlāti': ('each serving as the root of a root for the other (nominative pl., quoted with iti)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: each serving as root for the other'),
    'aññamaññamūlamūlāni': ('each serving as the root of a root for the other (neuter pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: each serving as root for the other'),
    'ekamūlamūlāni': ('having one root of a root in common (neuter pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root of a root, in the method of that name'),
    'kusalamūlakāti': ('based on a root that is skilful (nominative pl., quoted with iti)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root that is skilful'),
    'kusalamūlakaṃ': ('based on a root that is skilful (neuter sg.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root that is skilful'),
    'kusalamūlakañceva': ('based on a root that is skilful (neuter sg., with ceva)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root that is skilful'),
    'kusalamūlamūlakāti': ('based on the root of a root that is skilful (nominative pl., quoted with iti)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root that is skilful'),
    'kusalamūlamūlakaṃ': ('based on the root of a root that is skilful (neuter sg.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root that is skilful'),
    'kusalamūlamūlakañceva': ('based on the root of a root that is skilful (neuter sg., with ceva)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root that is skilful'),
    'ekamūlamūlakāti': ('based on one root of a root in common (nominative pl., quoted with iti)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root of a root, in the method of that name'),
    'ekamūlamūlakaṃ': ('based on one root of a root in common (neuter sg.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root of a root, in the method of that name'),
    'ekamūlamūlakañceva': ('based on one root of a root in common (neuter sg., with ceva)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root of a root, in the method of that name'),
    'aññamaññamūlamūlakāti': ('each stemming from the other as the root of a root (nominative pl., quoted with iti)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: each stemming from the other as a root'),
    'aññamaññamūlamūlakāni': ('each stemming from the other as the root of a root (neuter pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: each stemming from the other as a root'),
    'ekamūlamūlakāni': ('based on one root of a root in common (neuter pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root of a root, in the method of that name'),
    'akusalamūlasahajātā dhammā': ('states arisen together with a root that is unskilful (nominative pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: states that are unskilful'),
    'akusalamūlamūlāti': ('the root of a root that is unskilful (nominative pl., quoted with iti)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root that is unskilful'),
    'akusalamūlamūlāni': ('the root of a root that is unskilful (neuter pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root that is unskilful'),
    'akusalamūlakāti': ('based on a root that is unskilful (nominative pl., quoted with iti)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root that is unskilful'),
    'akusalamūlakaṃ': ('based on a root that is unskilful (neuter sg.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root that is unskilful'),
    'akusalamūlakañceva': ('based on a root that is unskilful (neuter sg., with ceva)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root that is unskilful'),
    'akusalamūlamūlakāti': ('based on the root of a root that is unskilful (nominative pl., quoted with iti)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root that is unskilful'),
    'akusalamūlamūlakaṃ': ('based on the root of a root that is unskilful (neuter sg.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root that is unskilful'),
    'akusalamūlamūlakañceva': ('based on the root of a root that is unskilful (neuter sg., with ceva)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root that is unskilful'),
    'abyākatamūlasahajātā dhammā': ('states arisen together with a root that is neither skilful nor unskilful (nominative pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: states that are neither skilful nor unskilful'),
    'abyākatamūlamūlāti': ('the root of a root that is neither skilful nor unskilful (nominative pl., quoted with iti)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root of a root, in the method of that name'),
    'abyākatamūlamūlāni': ('the root of a root that is neither skilful nor unskilful (neuter pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root of a root, in the method of that name'),
    'abyākatamūlakāti': ('based on a root that is neither skilful nor unskilful (nominative pl., quoted with iti)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root that is neither skilful nor unskilful'),
    'abyākatamūlakaṃ': ('based on a root that is neither skilful nor unskilful (neuter sg.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root that is neither skilful nor unskilful'),
    'abyākatamūlamūlakāti': ('based on the root of a root that is neither skilful nor unskilful (nominative pl., quoted with iti)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root of a root, in the method of that name'),
    'abyākatamūlamūlakaṃ': ('based on the root of a root that is neither skilful nor unskilful (neuter sg.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root of a root, in the method of that name'),
    'nāmamūlasahajātā': ('arisen together with a root belonging to the mental side (nominative pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root belonging to the mental side'),
    'nāmamūlamūlāti': ('the root of a root belonging to the mental side (nominative pl., quoted with iti)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root of a root, in the method of that name'),
    'nāmamūlamūlāni': ('the root of a root belonging to the mental side (neuter pl.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root of a root, in the method of that name'),
    'nāmamūlakāti': ('based on a root belonging to the mental side (nominative pl., quoted with iti)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root belonging to the mental side'),
    'nāmamūlakaṃ': ('based on a root belonging to the mental side (neuter sg.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root belonging to the mental side'),
    'nāmamūlakañceva': ('based on a root belonging to the mental side (neuter sg., with ceva)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root belonging to the mental side'),
    'nāmamūlamūlakāti': ('based on the root of a root belonging to the mental side (nominative pl., quoted with iti)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root of a root, in the method of that name'),
    'nāmamūlamūlakaṃ': ('based on the root of a root belonging to the mental side (neuter sg.)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root of a root, in the method of that name'),
    'nāmamūlamūlakañceva': ('based on the root of a root belonging to the mental side (neuter sg., with ceva)',
        'the Marathi tag names the root member only; the Burmese value is the whole compound; Marathi tag: a root of a root, in the method of that name'),
    'kusalahetūti': ("the wholesome roots, here 'having the skilful as cause', the second of ten synonyms for a root (nominative pl., quoted with iti)",
        'the Marathi tag is that of kusala alone; the Burmese value is the hetuvāra synonym (= kusalahetū); Marathi tag: skilful, karmically good (adjective)'),
    'nuppajjati': ('does not come into being (negated, 3rd sg. present)',
        'the Marathi tag is the positive lemma gloss; the Burmese value is the negated verb; Marathi tag: coming into being (verb, present or future)'),
    'nuppajjatīti': ('does not come into being (negated, present, quoted with iti)',
        'the Marathi tag is the positive lemma gloss; the Burmese value is the negated verb; Marathi tag: coming into being (verb, present or future)'),
    'pañcavokārānaṃ': ('of beings in the existence with all five aggregates (genitive pl.)',
        'the Marathi tag names the plane; the Burmese value is the beings of that plane (R5); Marathi tag: existence with all five groups'),
    'arūpānaṃ': ('of beings in the immaterial plane (genitive pl.)',
        'the Marathi tag names the plane; the Burmese value is the beings of that plane (R5); Marathi tag: the plane of immaterial existence'),
    'nuppajjittha': ('did not come into being (negated, past)',
        'the Marathi tag is the positive lemma gloss; the Burmese value is the negated verb; Marathi tag: having come into being (past or completed)'),
    'nuppajjitthāti': ('did not come into being (negated, past, quoted with iti)',
        'the Marathi tag is the positive lemma gloss; the Burmese value is the negated verb; Marathi tag: having come into being (past or completed)'),
    'suddhāvāsānaṃ': ('of beings in the Pure Abodes, the highest fine-material planes of non-returners (genitive pl.)',
        'the Marathi tag names the plane; the Burmese value is the beings of that plane (R5); Marathi tag: the highest fine-material planes of non-returners'),
    'nuppajjissati': ('will not come into being (negated, future)',
        'the Marathi tag is the positive lemma gloss; the Burmese value is the negated verb; Marathi tag: coming into being (verb, present or future)'),
    'nuppajjissatīti': ('will not come into being (negated, future, quoted with iti)',
        'the Marathi tag is the positive lemma gloss; the Burmese value is the negated verb; Marathi tag: coming into being (verb, present or future)'),
    'asotakānaṃ': ('of those lacking the ear (genitive pl.)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: having or lacking the organ of hearing'),
    'sasotakānaṃ': ('of those having the ear (genitive pl.)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: having or lacking the organ of hearing'),
    'sacakkhukānaṃ': ('of those having the eye (genitive pl.)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: the organ of sight'),
    'acakkhukānaṃ': ('of those lacking the eye (genitive pl.)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: the organ of sight'),
    'yassakasadisaṃ': ("like the 'of whom' section, in an abbreviation note",
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: the part of a chapter dealing with individuals'),
    'rūpāvacarānaṃ': ('of beings in the fine-material plane (genitive pl.)',
        'the Marathi tag names the plane; the Burmese value is the beings of that plane (R5); Marathi tag: the plane of fine material existence'),
    'arūpāvacarānaṃ': ('of beings in the immaterial plane (genitive pl.)',
        'the Marathi tag names the plane; the Burmese value is the beings of that plane (R5); Marathi tag: the plane of immaterial existence'),
    'upapajjissati': ('will come into being (3rd sg. future), misspelt in the source for uppajjissati (map-harmonise §A 6)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: entering a new existence (verb or participle)'),
    'suddhadhātuvāro': ('heading: the section on the elements alone',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: the eighteen components of experience as a category'),
    'saccayamakaṃ': ('title of the chapter of pairs on the truths',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: the four noble truths as a category'),
    'nirodhasamāpannānaṃ': ('of those who have entered the attainment of cessation (genitive pl.)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: a state in which perception and feeling have stopped'),
    'anabhisametāvīnaṃ': ('of those who have not yet seen the truths directly (genitive pl.)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: those who have or have not seen the truths directly'),
    'abhisametāvīnaṃ': ('of those who have seen the truths directly (genitive pl.)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: those who have or have not seen the truths directly'),
    'yatthakasadisaṃ': ("like the 'where' section, in an abbreviation note",
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: a named division of a chapter'),
    'āpāyikānaṃ': ('of beings in the states of loss, the planes of unhappy rebirth (genitive pl.)',
        'the Marathi tag names the plane; the Burmese value is the beings of that plane (R5); Marathi tag: the planes of unhappy rebirth'),
    'pacchimacittasamaṅgīnaṃ': ('of those possessed of the last mind before death (genitive pl.)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: the last consciousness before death'),
    'taṇhāvippayuttacitte': ('in a mind dissociated from craving (locative)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: mind as the knowing of an object'),
    'yassayatthakasadisaṃ': ("like the 'of whom, where' section, in an abbreviation note",
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: a named division of a chapter'),
    'nirodhasamāpannānanti': ('of those who have entered the attainment of cessation (genitive pl., quoted with iti)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: a state in which perception and feeling have stopped'),
    'nappajahatīti': ('does not give up (negated, present, quoted with iti)',
        'the Marathi tag is the positive lemma gloss; the Burmese value is the negated verb; Marathi tag: giving up a defilement or tendency (verb)'),
    'nappajahissatīti': ('will not give up (negated, future, quoted with iti)',
        'the Marathi tag is the positive lemma gloss; the Burmese value is the negated verb; Marathi tag: giving up a defilement or tendency (verb)'),
    'nappajahissanti': ('will not give up (negated, 3rd pl. future)',
        'the Marathi tag is the positive lemma gloss; the Burmese value is the negated verb; Marathi tag: giving up a defilement or tendency (verb)'),
    'nappajahissati': ('will not give up (negated, 3rd sg. future)',
        'the Marathi tag is the positive lemma gloss; the Burmese value is the negated verb; Marathi tag: giving up a defilement or tendency (verb)'),
    'saṅkhārayamakaṃ': ('title of the chapter of pairs on the formations',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: the three kinds of formation as a category'),
    'suddhasaṅkhāravāro': ('heading: the section on the formations alone',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: the three kinds of formation as a category'),
    'avitakkaavicāraṃ': ('without applied and without sustained thinking (neuter sg.)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: applied and sustained thinking'),
    'avitakkaavicārapacchimacittasamaṅgīnaṃ': ('of those possessed of a last mind without applied and sustained thinking (genitive pl.)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: applied and sustained thinking'),
    'savitakkasavicārabhūmiyaṃ': ('in the level with applied and sustained thinking (locative)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: applied and sustained thinking'),
    'avitakkaavicārabhūmiyaṃ': ('in the level without applied and sustained thinking (locative)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: applied and sustained thinking'),
    'avitakkaavicārapacchimacittassa': ('of the last mind without applied and sustained thinking (genitive)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: applied and sustained thinking'),
    'savitakkasavicārapacchimacittassa': ('of the last mind with applied and sustained thinking (genitive)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: applied and sustained thinking'),
    'saṅkhārayamakepi': ('in the chapter of pairs on the formations too (locative, with pi)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: the three kinds of formation as a category'),
    'anusayayamakaṃ': ('title of the chapter of pairs on the tendencies',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: the seven dormant defilements as a category'),
    'anusayavāro': ('heading: the section on the tendencies',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: the seven dormant defilements as a category'),
    'anusayavāra': ('heading: the section on the tendencies (stem)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: the seven dormant defilements as a category'),
    'sānusayavāro': ('heading: the section on those who have a tendency',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: being subject to a stated tendency'),
    'sānusayavāra': ('heading: the section on those who have a tendency (stem)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: being subject to a stated tendency'),
    'dhātuvisajjanāvāro': ('heading: the section of answers on the planes',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: one of the three spheres as a stem or heading'),
    'anusayavāre': ('in the section on the tendencies (locative)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: the seven dormant defilements as a category'),
    'nānuseti': ('does not lie dormant (negated, 3rd sg. present)',
        'the Marathi tag is the positive lemma gloss; the Burmese value is the negated verb; Marathi tag: remaining dormant in the mind (verb)'),
    'nānusetīti': ('does not lie dormant (negated, present, quoted with iti)',
        'the Marathi tag is the positive lemma gloss; the Burmese value is the negated verb; Marathi tag: remaining dormant in the mind (verb)'),
    'nānusenti': ('do not lie dormant (negated, 3rd pl. present)',
        'the Marathi tag is the positive lemma gloss; the Burmese value is the negated verb; Marathi tag: remaining dormant in the mind (verb)'),
    'nānusentīti': ('do not lie dormant (negated, 3rd pl. present, quoted with iti)',
        'the Marathi tag is the positive lemma gloss; the Burmese value is the negated verb; Marathi tag: remaining dormant in the mind (verb)'),
    'sānusayavāre': ('in the section on those who have a tendency (locative)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: being subject to a stated tendency'),
    'nappajahati': ('does not give up (negated, 3rd sg. present)',
        'the Marathi tag is the positive lemma gloss; the Burmese value is the negated verb; Marathi tag: giving up a defilement or tendency (verb)'),
    'nappajahanti': ('do not give up (negated, 3rd pl. present)',
        'the Marathi tag is the positive lemma gloss; the Burmese value is the negated verb; Marathi tag: giving up a defilement or tendency (verb)'),
    'kāmadhātumūlakaṃ': ('based on the sense-sphere plane, a cycle tag (neuter sg.)',
        'the Marathi tag names the faculty or plane only; the Burmese value is the cycle label «…ကို အခြေခံသော»; Marathi tag: the sensual sphere as a place of tendencies'),
    'rūpadhātumūlakaṃ': ('based on the fine-material plane, a cycle tag (neuter sg.)',
        'the Marathi tag names the faculty or plane only; the Burmese value is the cycle label «…ကို အခြေခံသော»; Marathi tag: the fine-material sphere as a place of tendencies'),
    'arūpadhātumūlakaṃ': ('based on the immaterial plane, a cycle tag (neuter sg.)',
        'the Marathi tag names the faculty or plane only; the Burmese value is the cycle label «…ကို အခြေခံသော»; Marathi tag: the immaterial sphere as a place of tendencies'),
    'nakāmadhātumūlakaṃ': ('based on what is not the sense-sphere plane, a cycle tag (neuter sg.)',
        'the Marathi tag names the faculty or plane only; the Burmese value is the cycle label «…ကို အခြေခံသော»; Marathi tag: one of the three spheres as a stem or heading'),
    'narūpadhātumūlakaṃ': ('based on what is not the fine-material plane, a cycle tag (neuter sg.)',
        'the Marathi tag names the faculty or plane only; the Burmese value is the cycle label «…ကို အခြေခံသော»; Marathi tag: one of the three spheres as a stem or heading'),
    'naarūpadhātumūlakaṃ': ('based on what is not the immaterial plane, a cycle tag (neuter sg.)',
        'the Marathi tag names the faculty or plane only; the Burmese value is the cycle label «…ကို အခြေခံသော»; Marathi tag: one of the three spheres as a stem or heading'),
    'nakāmanaarūpadhātumūlakaṃ': ('based on what is neither the sense-sphere nor the immaterial plane, a cycle tag (neuter sg.)',
        'the Marathi tag names the faculty or plane only; the Burmese value is the cycle label «…ကို အခြေခံသော»; Marathi tag: one of the three spheres as a stem or heading'),
    'narūpanaarūpadhātumūlakaṃ': ('based on what is neither the fine-material nor the immaterial plane, a cycle tag (neuter sg.)',
        'the Marathi tag names the faculty or plane only; the Burmese value is the cycle label «…ကို အခြေခံသော»; Marathi tag: one of the three spheres as a stem or heading'),
    'nakāmanarūpadhātumūlakaṃ': ('based on what is neither the sense-sphere nor the fine-material plane, a cycle tag (neuter sg.)',
        'the Marathi tag names the faculty or plane only; the Burmese value is the cycle label «…ကို အခြေခံသော»; Marathi tag: one of the three spheres as a stem or heading'),
    'uppajjamānanti': ('arising, what is in the course of arising (present participle, quoted with iti)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: the process or section of coming into being'),
    'uppajjamānañca': ('arising, what is in the course of arising (present participle, with ca)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: the process or section of coming into being'),
    'nirujjhamānanti': ('ceasing, what is in the course of ceasing (present participle, quoted with iti)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: the process of coming to an end'),
    'nirujjhamānañca': ('ceasing, what is in the course of ceasing (present participle, with ca)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: the process of coming to an end'),
    'cittake': ("the mind section, in the names of the cited sections 'yassa cittake …' (locative)",
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: mind as the knowing of an object'),
    'pacchimakusalacittassa': ('of the last wholesome mind (genitive)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: mind as the knowing of an object'),
    'cakkhundriyamūlakaṃ': ('based on the eye faculty, a cycle tag (neuter sg.)',
        'the Marathi tag names the faculty or plane only; the Burmese value is the cycle label «…ကို အခြေခံသော»; Marathi tag: faculty of sight'),
    'ghānindriyamūlakaṃ': ('based on the nose faculty, a cycle tag (neuter sg.)',
        'the Marathi tag names the faculty or plane only; the Burmese value is the cycle label «…ကို အခြေခံသော»; Marathi tag: faculty of smell'),
    'itthindriyamūlakaṃ': ('based on the faculty of femaleness, a cycle tag (neuter sg.)',
        'the Marathi tag names the faculty or plane only; the Burmese value is the cycle label «…ကို အခြေခံသော»; Marathi tag: faculty of femaleness'),
    'purisindriyamūlakaṃ': ('based on the faculty of maleness, a cycle tag (neuter sg.)',
        'the Marathi tag names the faculty or plane only; the Burmese value is the cycle label «…ကို အခြေခံသော»; Marathi tag: faculty of maleness'),
    'jīvitindriyamūlakaṃ': ('based on the life faculty, a cycle tag (neuter sg.)',
        'the Marathi tag names the faculty or plane only; the Burmese value is the cycle label «…ကို အခြေခံသော»; Marathi tag: faculty that keeps living things alive'),
    'somanassindriyamūlakaṃ': ('based on the faculty of glad mental feeling, a cycle tag (neuter sg.)',
        'the Marathi tag names the faculty or plane only; the Burmese value is the cycle label «…ကို အခြေခံသော»; Marathi tag: faculty of glad mental feeling'),
    'upekkhindriyamūlakaṃ': ('based on the faculty of neutral feeling, a cycle tag (neuter sg.)',
        'the Marathi tag names the faculty or plane only; the Burmese value is the cycle label «…ကို အခြေခံသော»; Marathi tag: faculty of neutral feeling'),
    'saddhindriyamūlakaṃ': ('based on the faculty of trust, a cycle tag (neuter sg.)',
        'the Marathi tag names the faculty or plane only; the Burmese value is the cycle label «…ကို အခြေခံသော»; Marathi tag: faculty of trust'),
    'paññindriyamūlakaṃ': ('based on the faculty of wisdom, a cycle tag (neuter sg.)',
        'the Marathi tag names the faculty or plane only; the Burmese value is the cycle label «…ကို အခြေခံသော»; Marathi tag: faculty of seeing things as they are'),
    'sacakkhukā': ('those having the eye (nominative pl.)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: the organ of sight'),
    'upekkhāsampayuttapacchimacittaṃ': ('a last mind accompanied by neutral feeling (nominative sg.)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: the last consciousness before death'),
    'somanassasampayuttapacchimacittaṃ': ('a last mind accompanied by glad mental feeling (nominative sg.)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: the last consciousness before death'),
    'pacchimacittasamaṅgīna': ('of those possessed of the last mind before death (genitive pl., misspelt for pacchimacittasamaṅgīnaṃ)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: the last consciousness before death'),
    'upekkhāsampayuttapacchimacittasamaṅgīnaṃ': ('of those possessed of a last mind accompanied by neutral feeling (genitive pl.)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: the last consciousness before death'),
    'somanassasampayuttapacchimacittasamaṅgīnaṃ': ('of those possessed of a last mind accompanied by glad mental feeling (genitive pl.)',
        'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says; Marathi tag: the last consciousness before death'),
    'domanassindriyamūlakaṃ': ('based on the faculty of unhappy mental feeling, a cycle tag (neuter sg.)',
        'the Marathi tag names the faculty or plane only; the Burmese value is the cycle label «…ကို အခြေခံသော»; Marathi tag: faculty of unhappy mental feeling'),
    'anaññātaññassāmītindriyamūlakaṃ': ("based on the faculty 'I shall know the not yet known', a cycle tag (neuter sg.)",
        'the Marathi tag names the faculty or plane only; the Burmese value is the cycle label «…ကို အခြေခံသော»; Marathi tag: faculty belonging to the first path'),
    'aññindriyamūlakaṃ': ('based on the faculty of final knowledge, a cycle tag (neuter sg.)',
        'the Marathi tag names the faculty or plane only; the Burmese value is the cycle label «…ကို အခြေခံသော»; Marathi tag: faculty belonging to the higher paths and final fruit'),
    # @@ADJ
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
        for k in reversed(list(found)):                         # pi-5 first where several list a value
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
        f.write(f'# Pāli→Burmese pi-6 sense decisions, written by gen_decisions_my.py from {pathlib.Path(aggp).name}\n')
        f.write('# English tags: pi-5, then pi-4, pi-3, pi-2, pi-1 Burmese senses (binding), else Marathi pi-6 senses '
                '(tags only), or MANUAL;\n')
        f.write('# values: pi-6 Burmese keyword map only.\n')
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
