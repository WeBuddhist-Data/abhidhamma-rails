"""Tidy pass over the pi-6 Vietnamese senses parts 1-5 (brief: ../vi-senses-tidy-brief.md).

usage (run with python -I -X utf8 -B):
  tidy_senses_vi.py families            # family wording differences across the five parts (label stripped)
  tidy_senses_vi.py dump <regex>        # decision lines whose headword matches <regex> (case-insensitive), with values
  tidy_senses_vi.py backup              # copy decisions-part1..5.txt to backup-pre-tidy/ (never overwrites)
  tidy_senses_vi.py apply [--write]     # exact tag replacements of the table REPL below; --write writes the
                                        # decisions files (LF) and tidy-log.tsv
  tidy_senses_vi.py samplecheck         # part1-senses.md lines of the 91 sample headwords == sample-senses.md lines
Only decisions-part1..5.txt are edited; the 91 sample headwords of part 1 are never touched.
"""
import os
import re
import shutil
import sys
import unicodedata
from collections import OrderedDict, defaultdict

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import senses_tool_vi as T  # noqa: E402

PARTS = ('1', '2', '3', '4', '5')
LABEL = re.compile(r'\s*\(([^()]*)\)\s*$')


def nfc(s):
    return unicodedata.normalize('NFC', s)


def dec_path(k):
    return os.path.join(HERE, f'decisions-part{k}.txt')


def load_all():
    """{part: OrderedDict(hw -> (senses, values))}"""
    out = OrderedDict()
    for k in PARTS:
        rows = T.read_agg(os.path.join(HERE, f'agg-part{k}.tsv'))
        dec = T.read_decisions(dec_path(k))
        d = OrderedDict()
        for hw, (n, senses) in dec.items():
            d[hw] = (senses, rows[hw]['vals'] if hw in rows else {})
        out[k] = d
    return out


def base(tag):
    return LABEL.sub('', tag).strip().rstrip(',')


def label(tag):
    m = LABEL.search(tag)
    return m.group(1) if m else ''


def vals_str(vals):
    return ' | '.join(f'{v}={c}' for v, c in vals.items())


FAMILIES = [
    ('X-mulakam section labels', lambda hw, vs: hw.endswith('mūlakaṃ') and any('dựa trên' in v for v in vs)),
    ('moment phrases', lambda hw, vs: re.search(r'(uppādakkhaṇ|bhaṅgakkhaṇ)', hw.lower())),
    ('samangi persons', lambda hw, vs: 'samaṅg' in hw.lower()),
    ('Suddha-X-varo / -mulacakkavaro', lambda hw, vs: re.search(r'^suddha.*vār|mūlacakkavār', hw.lower())),
    ('other X-varo / -vare headings', lambda hw, vs: re.search(r'vār(o|a|e|epi|aṃ|ena|esu|ādi)$', hw.lower())
     and not re.search(r'^suddha|mūlacakkavār', hw.lower())),
    ('yatthaka / yassaka labels', lambda hw, vs: re.search(r'(yatthak|yassak)', hw.lower())),
    ('yamaka titles', lambda hw, vs: 'yamak' in hw.lower() and hw.lower() != 'yamakāni'),
    ('past verbs', lambda hw, vs: re.search(r'(ittha|itthāti|ākāsi)$', hw.lower())),
    ('future verbs', lambda hw, vs: re.search(r'(issati|issanti|issatīti|issantīti|essati|essanti|essatīti|issānti)$',
                                              hw.lower())),
    ('present verbs', lambda hw, vs: re.search(r'(jjati|jjanti|jjatī|jjatīti|jjantīti|jānāti|jānātīti|jānanti|'
                                               r'jahati|jahatīti|jahanti|bhāveti|bhāvetīti|bhāventi|karoti|'
                                               r'karotīti|karonti|jjhiti|seti|setīti|senti|sentīti)$', hw.lower())),
    ('participles', lambda hw, vs: re.search(r'^(uppajjamān|nirujjhamān|uppann|niruddh)', hw.lower())),
    ('dhatu members / planes', lambda hw, vs: 'dhātu' in hw.lower()),
    ('sankhara', lambda hw, vs: 'saṅkhār' in hw.lower()),
    ('persons', lambda hw, vs: re.search(r'(arah|anāgām|puthujjan|aṭṭhamak)', hw.lower())),
    ('sacca members', lambda hw, vs: re.search(r'^(nirodh|samuday|magg|dukkhasacc|sacc)', hw.lower())),
    ('pacchimacitta', lambda hw, vs: 'pacchima' in hw.lower()),
    ('anuloma / paccanika / patiloma', lambda hw, vs: re.search(r'^(anulom|paccanīk|paṭilom)', hw.lower())),
]


def families():
    data = load_all()
    for name, pred in FAMILIES:
        print(f'\n######## {name}')
        groups = defaultdict(list)
        for k, d in data.items():
            for hw, (senses, vals) in d.items():
                if pred(hw, vals):
                    for t, _ in senses:
                        groups[base(t)].append(f'p{k} {hw} ({label(t)}) [{vals_str(vals)}]')
        for b, items in groups.items():
            print(f'  == {b}  ×{len(items)}')
            for it in items:
                print(f'       {it}')


def dump(rx):
    r = re.compile(rx, re.I)
    data = load_all()
    for k, d in data.items():
        for hw, (senses, vals) in d.items():
            if r.search(hw):
                print(f'p{k} {hw}: {{' + '; '.join(t + (": " + " / ".join(v) if v else "") for t, v in senses)
                      + f'}}  [{vals_str(vals)}]')


def backup():
    bdir = os.path.join(HERE, 'backup-pre-tidy')
    os.makedirs(bdir, exist_ok=True)
    for k in PARTS:
        dst = os.path.join(bdir, f'decisions-part{k}.txt')
        if os.path.exists(dst):
            print(f'exists, not overwritten: {dst}')
            continue
        shutil.copyfile(dec_path(k), dst)
        print(f'copied -> {dst}')


# ---------------------------------------------------------------------------------------------------------------
# Replacement table: (part, headword, old tag, new tag, reason). Each old tag must occur exactly once in that
# headword's decision line; the replacement is exact.
# ---------------------------------------------------------------------------------------------------------------
RE = 'a round of the exposition'
MUL = ('X-mulakam closing labels: one pattern "the part based on X, a closing section label (neuter sg.)" '
       '(part 5 wording, 13 of 27; all are bracketed closing labels)')
MOM = 'moment phrases: pacchimacitta = "the final mind" (parts 3 and 5); -kkhanam forms take the -kkhane gloss'
SAM = ('samangi persons: "one endowed with X" (sg.) / "of those endowed with X" (gen. pl.), parts 2-3 wording; '
       'maggasamangi- pi-5 gloss "at the moment of the path"')
SUD = ('Suddha-X-varo: "the section on the pure X, the X taken alone, a round of the exposition (heading)"; '
       '-mulacakkavaro: "the section on the cycle based on the pure X, a round of the exposition (heading)" '
       '(conventions X-varo pattern; vi «thuần túy»)')
VAR = ('X-varo family: conventions pattern "the section on X, a round of the exposition" with case labels '
       '(heading) / (locative sg. heading) / (accusative sg. heading) / (instrumental sg. heading)')
YAT = 'yatthaka / yassaka labels: part 2 wording (first appearance) "the section by place / by person and place"'
TIT = ('yamaka titles: "title of the chapter on X" (no article, 11 of 13); inflected cross-references add '
       '"in a cross-reference" and the case label')
PST = ('past verbs: en pattern "having X (past or completed)" as uppajjittha / nirujjhittha; -ti forms add the '
       'question-particle label')
PAJ = 'pajahittha: re-glossed as the act ("having given up …"), like uppajjittha / parijanittha (brief)'
FUT = ('future verbs: pi-5 / conventions pattern "will X (3rd sg./pl. future)" (uppajjissati, nirujjhissanti); the en '
       'tags "(verb, present or future)" misdescribe a future form')
PRT = 'participles: conventions wording "in the process of ceasing", same pattern as uppajjamana'
DHA = 'X-dhatum members: the member tag (pi-1 … pi-5 nominative) with the accusative label'
PLN = 'kama- / arupadhatum in the Anusayayamaka: the plane only (brief): pi-5 Kamadhatuya / arupadhatuya gloss'
SKH = ('Yamaka definition ^6-6-1 (assasapassasa kayasankharo, vitakkavicara vacisankharo, sanna ca vedana ca '
       'cittasankharo): pi-6 tag, not the pi-1 … pi-5 volition tag (brief)')
MEM = 'yamaka member case form: the member tag with the label adapted (conventions §4)'

REPL = [
    # ---- part 1 ----
    (1, 'Paṇṇattivāro', 'the part of a chapter dealing with terms',
     f'the section on terms, the designations, {RE} (heading)', VAR),
    (1, 'Padasodhanavāro', 'heading for the section that examines each term',
     f'the section on clarifying the terms, {RE} (heading)', VAR),
    (1, 'Padasodhanamūlacakkavāro', 'heading for the cycle that examines each term',
     f'the section on the cycle based on clarifying the terms, {RE} (heading)', SUD),
    (1, 'Suddhakhandhavāro', 'the section on the pure aggregates, the aggregates taken alone (heading)',
     f'the section on the pure aggregates, the aggregates taken alone, {RE} (heading)', SUD),
    (1, 'Suddhakhandhamūlacakkavāro', 'the cycle based on the pure aggregates, a round of the exposition (heading)',
     f'the section on the cycle based on the pure aggregates, {RE} (heading)', SUD),
    (1, 'Pavattivāro', 'the section on occurrence, the going-on of existence (heading)',
     f'the section on occurrence, the going-on of existence, {RE} (heading)', VAR),
    (1, 'Atītānāgatavāro', 'the section combining past and future',
     f'the section on past and future, {RE} (heading)', VAR),
    (1, 'Paṇṇattiuddesavāro', 'the statement section of the section on terms, its opening enumeration (heading)',
     'the statement section, the opening enumeration of the section on terms (heading)',
     'Uddesavaro / Niddesavaro sample pattern'),
    (1, 'Pariññāvāro', 'the section on knowing thoroughly', f'the section on knowing thoroughly, {RE} (heading)', VAR),
    (1, 'Khandhayamakaṃ', 'title of the chapter on the aggregates', 'title of the chapter on aggregates', TIT),
    (1, 'khandhe', 'the groups', 'aggregates, groups of phenomena (accusative pl.)', MEM),
    # ---- part 2 ----
    (2, 'Paṇṇattiniddesavāro', 'the exposition section on terms, the detailed explanation of the designations (heading)',
     'the exposition section, the detailed explanation of the section on terms (heading)',
     'Uddesavaro / Niddesavaro sample pattern'),
    (2, 'Suddhāyatanavāro', 'the section on the bare sense bases, a round of the exposition (heading)',
     f'the section on the pure sense bases, the sense bases taken alone, {RE} (heading)', SUD),
    (2, 'Suddhāyatanamūlacakkavāro',
     'the section on the cycles based on the bare sense bases, a round of the exposition (heading)',
     f'the section on the cycle based on the pure sense bases, {RE} (heading)', SUD),
    (2, 'uppajjitthāti', 'having come into being (past or completed)',
     'having come into being (past or completed, with the question particle -ti)', PST),
    (2, 'nirujjhitthāti', 'having come to an end (past or completed)',
     'having come to an end (past or completed, with the question particle -ti)', PST),
    (2, 'nirujjhissati', 'coming to an end (verb, present or future)', 'will come to an end (3rd sg. future)', FUT),
    (2, 'nirujjhissatīti', 'coming to an end (verb, present or future)',
     'will come to an end (3rd sg. future, with the question particle -ti)', FUT),
    (2, 'parijānātīti', 'comprehends fully (with the question particle -ti)',
     'comprehends fully (3rd sg. present, with the question particle -ti)', 'present verbs: label as pajahatiti'),
    (2, 'parijānittha', 'having known a thing thoroughly', 'having known a thing thoroughly (past or completed)', PST),
    (2, 'parijānitthāti', 'having known a thing thoroughly',
     'having known a thing thoroughly (past or completed, with the question particle -ti)', PST),
    (2, 'parijānissati', 'knowing a thing thoroughly (verb, present or future)',
     'will know a thing thoroughly (3rd sg. future)', FUT),
    (2, 'parijānissatīti', 'knowing a thing thoroughly (verb, present or future)',
     'will know a thing thoroughly (3rd sg. future, with the question particle -ti)', FUT),
    (2, 'parijānissanti', 'knowing a thing thoroughly (verb, present or future)',
     'will know a thing thoroughly (3rd pl. future)', FUT),
    (2, 'maggaṃ paṭilabhissanti', 'going to reach the noble path', 'will attain the path (3rd pl. future phrase)',
     FUT + '; parallel to aggamaggam patilabhissanti'),
    (2, 'paṭilabhissanti', 'going to reach the noble path', 'will attain, will reach the noble path (3rd pl. future)',
     FUT),
    (2, 'parinibbāyissanti', 'reaching complete liberation at death (future)',
     'will reach complete liberation at death (3rd pl. future)', FUT),
    (2, 'puthujjanā', 'unenlightened people as a group', 'ordinary persons, worldlings (nominative pl.)',
     'persons: the pi-1 … pi-5 Puthujjano gloss, label adapted'),
    (2, 'Cakkhāyatanamūlakaṃ', 'based on the eye base, the part of the cycle starting from it (section label)',
     'the part based on the eye base, a closing section label (neuter sg.)', MUL),
    (2, 'Ghānāyatanamūlakaṃ', 'based on the nose base, the part of the cycle starting from it (section label)',
     'the part based on the nose base, a closing section label (neuter sg.)', MUL),
    (2, 'Rūpāyatanamūlakaṃ', 'based on the base of visible forms, the part of the cycle starting from it (section label)',
     'the part based on the base of visible forms, a closing section label (neuter sg.)', MUL),
    (2, 'Manāyatanamūlakaṃ', 'based on the mind base, the part of the cycle starting from it (section label)',
     'the part based on the mind base, a closing section label (neuter sg.)', MUL),
    # ---- part 3 ----
    (3, 'Suddhadhātuvāro', 'the section on the elements alone, a round of the exposition (heading)',
     f'the section on the pure elements, the elements taken alone, {RE} (heading)', SUD),
    (3, 'Suddhadhātumūlacakkavāro', 'the section on the cycle rooted in the elements alone, a round of the exposition (heading)',
     f'the section on the cycle based on the pure elements, {RE} (heading)', SUD),
    (3, 'Suddhasaccavāro', 'the section on the truths alone, a round of the exposition (heading)',
     f'the section on the pure truths, the truths taken alone, {RE} (heading)', SUD),
    (3, 'Suddhasaccamūlacakkavāro', 'the section on the cycle rooted in the truths alone, a round of the exposition (heading)',
     f'the section on the cycle based on the pure truths, {RE} (heading)', SUD),
    (3, 'Suddhasaṅkhāravāro', 'the section on the formations alone, a round of the exposition (heading)',
     f'the section on the pure formations, the formations taken alone, {RE} (heading)', SUD),
    (3, 'Paṇṇattivāra', 'the part of a chapter dealing with terms',
     f'the section on terms, the designations, {RE} (heading)', VAR),
    (3, 'uppādavāranirodhavārepi', "in the section on arising and cessation too (locative sg., with pi 'also')",
     f"the section on arising and cessation, {RE} (locative sg. heading, with pi 'also')",
     VAR + '; = uppadanirodhavarepi'),
    (3, 'nirodhavārena', 'by way of the section on cessation (instrumental sg.)',
     f'the section on cessation, {RE} (instrumental sg. heading)', VAR),
    (3, 'pariññāvāraṃ', 'the section on knowing thoroughly',
     f'the section on knowing thoroughly, {RE} (accusative sg. heading)', VAR),
    (3, 'paccanīkaokāsā', 'opposite order by place, the negated half of the section on place (heading)',
     'opposite order by place, the negated half of a section (heading)', 'anuloma / paccanika family: = paccanikaokaso'),
    (3, 'Dhammadhātuṃ', 'mind-object element', 'the element of mind-objects (accusative sg.)', DHA),
    (3, 'cakkhudhātuṃ', 'sight element', 'the eye element (accusative sg.)', DHA),
    (3, 'āyatanayamake', 'title of the chapter on sense bases',
     'title of the chapter on sense bases, in a cross-reference (locative sg.)', TIT),
    (3, 'dhātuyamakepi', 'title of the chapter on elements',
     "title of the chapter on elements, in a cross-reference (locative sg., with pi 'also')", TIT),
    (3, 'dhātuyamakassa', 'title of the chapter on elements',
     'title of the chapter on elements, in a cross-reference (genitive sg.)', TIT),
    (3, 'āyatanayamakassa', 'title of the chapter on sense bases',
     'title of the chapter on sense bases, in a cross-reference (genitive sg.)', TIT),
    (3, 'dhātuyamakampi', 'title of the chapter on elements',
     "title of the chapter on elements, in a cross-reference (nominative sg., with pi 'also')", TIT),
    (3, 'khandhayamake', 'title of the chapter on aggregates',
     'title of the chapter on aggregates, in a cross-reference (locative sg.)', TIT),
    (3, 'saṅkhārayamakepi', 'title of the chapter on formations',
     "title of the chapter on formations, in a cross-reference (locative sg., with pi 'also')", TIT),
    (3, 'nirodhasaccaṃ', 'the truth of ending', 'the truth of ending, third of the four noble truths (nominative sg.)',
     'sacca members: Dukkhasaccam pattern (conventions), as nirodhasaccanti / -nca'),
    (3, 'yatthakasadisaṃ', 'like the section on place, the where-part of the exposition (neuter sg. adjective)',
     'like the section by place (neuter sg. adjective)', YAT + '; = yassakasadisam'),
    (3, 'yatthakā', 'the sections on place, the where-parts of the exposition (nominative pl.)',
     'the section by place, the questions about planes of existence (nominative pl. section label)', YAT),
    (3, 'yassayatthakasadisaṃ', 'like the section on person and place (neuter sg. adjective)',
     'like the section by person and place (neuter sg. adjective)', YAT),
    (3, 'yassayatthakepi', "in the section on person and place too (locative sg., with pi 'also')",
     "the section by person and place (locative sg. section label, with pi 'also')", YAT),
    (3, 'yassayatthake', 'in the section on person and place (locative sg.)',
     'the section by person and place (locative sg. section label)', YAT + '; = yassa yatthake'),
    (3, 'pajahittha', 'a defilement already given up',
     'having given up a defilement or tendency (past or completed)', PAJ),
    (3, 'pajahitthāti', 'a defilement already given up',
     'having given up a defilement or tendency (past or completed, with the question particle -ti)', PAJ),
    (3, 'nappajahittha', 'a defilement already given up',
     'not having given up a defilement or tendency (past or completed, negated)', PAJ + '; negated as nuppajjittha'),
    (3, 'nappajahitthāti', 'a defilement already given up',
     'not having given up a defilement or tendency (past or completed, negated, with the question particle -ti)',
     PAJ + '; negated as nuppajjitthati'),
    (3, 'pajahissati', 'giving up a defilement or tendency (verb)',
     'will give up a defilement or tendency (3rd sg. future)', FUT),
    (3, 'pajahissatīti', 'giving up a defilement or tendency (verb)',
     'will give up a defilement or tendency (3rd sg. future, with the question particle -ti)', FUT),
    (3, 'nappajahissati', 'giving up a defilement or tendency (verb)',
     'will not give up a defilement or tendency (3rd sg. future, negated)', FUT + '; negated as nuppajjissati'),
    (3, 'nappajahissatīti', 'giving up a defilement or tendency (verb)',
     'will not give up a defilement or tendency (3rd sg. future, negated, with the question particle -ti)',
     FUT + '; negated as nuppajjissatiti'),
    (3, 'nappajahissanti', 'giving up a defilement or tendency (verb)',
     'will not give up a defilement or tendency (3rd pl. future, negated)', FUT + '; negated as nuppajjissati'),
    (3, 'kāyasaṅkhāro', 'bodily formation, volition expressed through the body (nominative sg.)',
     'the bodily formation, in-and-out breathing (nominative sg.)', SKH),
    (3, 'kāyasaṅkhāroti', 'bodily formation, volition expressed through the body (nominative sg., with the question particle -ti)',
     'the bodily formation, in-and-out breathing (nominative sg., with the question particle -ti)', SKH),
    (3, 'kāyasaṅkhārañca', "bodily formation, volition expressed through the body (accusative sg., with ca 'and')",
     "the bodily formation, in-and-out breathing (accusative sg., with ca 'and')", SKH),
    (3, 'kāyasaṅkhāraṃ', 'volitional construction through the body',
     'the bodily formation, in-and-out breathing (accusative sg.)', SKH),
    (3, 'vacīsaṅkhāro', 'verbal activity, thought and reflection',
     'the verbal formation, directed and sustained thought (nominative sg.)', SKH),
    (3, 'vacīsaṅkhāroti', 'verbal activity, thought and reflection (nominative sg., with the question particle -ti)',
     'the verbal formation, directed and sustained thought (nominative sg., with the question particle -ti)', SKH),
    (3, 'vacīsaṅkhārañca', "verbal activity, thought and reflection (accusative sg., with ca 'and')",
     "the verbal formation, directed and sustained thought (accusative sg., with ca 'and')", SKH),
    (3, 'vacīsaṅkhāraṃ', 'volitional construction through speech',
     'the verbal formation, directed and sustained thought (accusative sg.)', SKH),
    (3, 'cittasaṅkhāro', 'mental activity, perception and feeling',
     'the mental formation, perception and feeling (nominative sg.)', SKH),
    (3, 'cittasaṅkhāroti', 'mental activity, perception and feeling (nominative sg., with the question particle -ti)',
     'the mental formation, perception and feeling (nominative sg., with the question particle -ti)', SKH),
    (3, 'cittasaṅkhārañca', "mental activity, perception and feeling (accusative sg., with ca 'and')",
     "the mental formation, perception and feeling (accusative sg., with ca 'and')", SKH),
    # ---- part 4 ----
    (4, 'Pajahanavāro', 'the section about giving up', f'the section on giving up, {RE} (heading)', VAR),
    (4, 'Pajahanavāra', 'the section about giving up', f'the section on giving up, {RE} (heading)', VAR),
    (4, 'Pajahanavāre', 'the section about giving up', f'the section on giving up, {RE} (locative sg. heading)', VAR),
    (4, 'Pajahanāvāre', 'the section about giving up',
     f'the section on giving up, {RE} (locative sg. heading, variant spelling)', VAR),
    (4, 'Pariññāvāra', 'the section on knowing thoroughly', f'the section on knowing thoroughly, {RE} (heading)', VAR),
    (4, 'Pariññāvāre', 'the section on knowing thoroughly',
     f'the section on knowing thoroughly, {RE} (locative sg. heading)', VAR),
    (4, 'Anusayavāre', f'the section on underlying tendencies, {RE} (locative, section label)',
     f'the section on underlying tendencies, {RE} (locative sg. heading)', VAR),
    (4, 'Sānusayavāre', f'the section on having an underlying tendency, {RE} (locative, section label)',
     f'the section on having an underlying tendency, {RE} (locative sg. heading)', VAR),
    (4, 'Pahīnavāre', f'the section on what has been given up, {RE} (locative, section label)',
     f'the section on what has been given up, {RE} (locative sg. heading)', VAR),
    (4, 'Puggalavāro', 'the part of a chapter dealing with individuals', f'the section on persons, {RE} (heading)', VAR),
    (4, 'Dhammavāro', 'the section on phenomena, of the Cittayamaka (heading)',
     f'the section on phenomena, {RE} (heading)', VAR),
    (4, 'Suddhadhammavāro', f'the section on plain phenomena, phenomena without qualification, {RE} (heading)',
     f'the section on the pure phenomena, the phenomena taken alone, {RE} (heading)', SUD),
    (4, 'Suddhadhammamūlacakkavāro', f'the cycle section based on plain phenomena, {RE} (heading)',
     f'the section on the cycle based on the pure phenomena, {RE} (heading)', SUD),
    (4, 'Anāgāmimaggasamaṅgī', 'endowed with the path of non-returning, the person at that path moment (nominative sg.)',
     'one endowed with the path of non-returning, the third path (nominative sg.)', SAM),
    (4, 'Anāgāmimaggasamaṅgiñca',
     "endowed with the path of non-returning, the person at that path moment (accusative sg., with ca 'and')",
     "one endowed with the path of non-returning, the third path (accusative sg., with ca 'and')", SAM),
    (4, 'Anāgāmimaggasamaṅgiṃ', 'endowed with the path of non-returning, the person at that path moment (accusative sg.)',
     'one endowed with the path of non-returning, the third path (accusative sg.)', SAM),
    (4, 'Aggamaggasamaṅgiṃ', 'endowed with the highest path, the person at the arahant path moment (accusative sg.)',
     'one endowed with the highest path, the path of arahantship (accusative sg.)', SAM),
    (4, 'maggasamaṅgīnaṃ', 'someone endowed with a stated path',
     'of those endowed with a path, at the moment of the path (genitive pl.)', SAM),
    (4, 'maggasamaṅgīnañca', 'someone endowed with a stated path',
     "of those endowed with a path, at the moment of the path (genitive pl., with ca 'and')", SAM),
    (4, 'Cittasamaṅgīnaṃ', 'endowed with a mind, those in whom a mind is present (genitive pl.)',
     'of those endowed with a mind, in whom a mind is present (genitive pl.)', SAM),
    (4, 'arūpadhātuṃ', 'the immaterial element or plane', 'the formless world, the immaterial sphere (accusative sg.)', PLN),
    (4, 'kāmadhātuṃ', 'the sensual element or plane', 'the world of sense desire, the sense sphere (accusative sg.)', PLN),
    (4, 'kāmadhātuṃyeva', "the sensual element or plane, with yeva 'only' (accusative sg.)",
     "the world of sense desire, the sense sphere (accusative sg., with yeva 'only')", PLN),
    (4, 'Kāmadhātumūlakaṃ', 'the part based on the world of sense desire (section label)',
     'the part based on the world of sense desire, a closing section label (neuter sg.)', MUL),
    (4, 'Rūpadhātumūlakaṃ', 'the part based on the world of form (section label)',
     'the part based on the world of form, a closing section label (neuter sg.)', MUL),
    (4, 'Arūpadhātumūlakaṃ', 'the part based on the formless world (section label)',
     'the part based on the formless world, a closing section label (neuter sg.)', MUL),
    (4, 'Nakāmadhātumūlakaṃ', 'the part based on what is not the world of sense desire (section label)',
     'the part based on what is not the world of sense desire, a closing section label (neuter sg.)', MUL),
    (4, 'Narūpadhātumūlakaṃ', 'the part based on what is not the world of form (section label)',
     'the part based on what is not the world of form, a closing section label (neuter sg.)', MUL),
    (4, 'Naarūpadhātumūlakaṃ', 'the part based on what is not the formless world (section label)',
     'the part based on what is not the formless world, a closing section label (neuter sg.)', MUL),
    (4, 'Nakāmanaarūpadhātumūlakaṃ', 'the part based on neither the world of sense desire nor the formless world (section label)',
     'the part based on neither the world of sense desire nor the formless world, a closing section label (neuter sg.)', MUL),
    (4, 'Narūpanaarūpadhātumūlakaṃ', 'the part based on neither the world of form nor the formless world (section label)',
     'the part based on neither the world of form nor the formless world, a closing section label (neuter sg.)', MUL),
    (4, 'Nakāmanarūpadhātumūlakaṃ', 'the part based on neither the world of sense desire nor the world of form (section label)',
     'the part based on neither the world of sense desire nor the world of form, a closing section label (neuter sg.)', MUL),
    (4, 'nirujjhamānaṃ', 'ceasing, in the course of ceasing (present participle)',
     'ceasing, in the process of ceasing (present participle)', PRT),
    (4, 'nirujjhamānanti', 'ceasing, in the course of ceasing (present participle, with the question particle -ti)',
     'ceasing, in the process of ceasing (present participle, with the question particle -ti)', PRT),
    (4, 'nirujjhamānañca', "ceasing, in the course of ceasing (present participle, with ca 'and')",
     "ceasing, in the process of ceasing (present participle, with ca 'and')", PRT),
    (4, 'Pacchimacittassa uppādakkhaṇe', 'at the moment of arising of the last mind, the final mind of a life (locative phrase)',
     'at the moment of arising of the final mind (locative phrase)', MOM + '; = Pacchimacittassa bhangakkhane'),
    (4, 'Sarāgapacchimacittassa uppādakkhaṇe', 'at the moment of arising of the last mind with lust (locative phrase)',
     'at the moment of arising of the final mind with lust (locative phrase)', MOM),
    (4, 'Pacchimakusalacittassa', 'of the last wholesome mind (genitive sg.)', 'of the final wholesome mind (genitive sg.)',
     MOM),
    (4, 'uppādakkhaṇaṃ', 'the first phase of an instant of consciousness',
     'the moment of arising, the first phase of a mind-moment (accusative sg.)', MOM),
    (4, 'uppādakkhaṇañca', 'the first phase of an instant of consciousness',
     "the moment of arising, the first phase of a mind-moment (accusative sg., with ca 'and')", MOM),
    (4, 'bhaṅgakkhaṇaṃ', 'the last phase of an instant of consciousness',
     'the moment of dissolution, the last phase of a mind-moment (accusative sg.)', MOM),
    (4, 'bhaṅgakkhaṇañca', 'the last phase of an instant of consciousness',
     "the moment of dissolution, the last phase of a mind-moment (accusative sg., with ca 'and')", MOM),
    (4, 'Indriyayamakaṃ', 'title of the chapter on the faculties', 'title of the chapter on faculties', TIT),
    # ---- part 5 ----
    (5, 'Suddhindriyavāro', f'the section on the pure faculties, the faculties taken by themselves, {RE} (heading)',
     f'the section on the pure faculties, the faculties taken alone, {RE} (heading)', SUD),
    (5, 'Pacchimacittasamaṅgīna', 'those possessed of the final mind before death (genitive pl., spelling without the final -ṃ)',
     'of those endowed with the final mind, the last consciousness before death (genitive pl., spelling without the final -ṃ)',
     SAM + '; = Pacchimacittasamanginam'),
    (5, 'upekkhāsampayuttapacchimacittasamaṅgīnaṃ', 'those possessed of the final mind associated with equanimity (genitive pl.)',
     'of those endowed with the final mind associated with equanimity (genitive pl.)', SAM),
    (5, 'somanassasampayuttapacchimacittasamaṅgīnaṃ', 'those possessed of the final mind associated with joy (genitive pl.)',
     'of those endowed with the final mind associated with joy (genitive pl.)', SAM),
    (5, 'maggasamaṅgino', 'someone endowed with a stated path',
     "those endowed with a path, at the moment of the path (accusative pl., in 'dve maggasamaṅgino ṭhapetvā')", SAM),
    (5, 'anāgāmimaggasamaṅgi', 'one possessed of the path of non-returning, the person at the third path moment (nominative sg.)',
     'one endowed with the path of non-returning, the third path (nominative sg., spelt with short -i)', SAM),
    (5, 'bhāvittha', 'having cultivated a quality', 'having cultivated a quality (past or completed)', PST),
    (5, 'bhāvitthāti', 'having cultivated a quality',
     'having cultivated a quality (past or completed, with the question particle -ti)', PST),
    (5, 'sacchikarittha', 'having made directly evident', 'having made directly evident (past or completed)', PST),
    (5, 'sacchikaritthāti', 'having made directly evident',
     'having made directly evident (past or completed, with the question particle -ti)', PST),
    (5, 'sacchākāsi', 'having made directly evident', 'having made directly evident (past or completed, aorist)', PST),
    (5, 'pajahissanti', 'giving up a defilement or tendency (verb)',
     'will give up a defilement or tendency (3rd pl. future)', FUT),
    (5, 'bhāvessati', 'cultivating a quality (verb, present or future)', 'will cultivate a quality (3rd sg. future)', FUT),
    (5, 'bhāvessatīti', 'cultivating a quality (verb, present or future)',
     'will cultivate a quality (3rd sg. future, with the question particle -ti)', FUT),
    (5, 'bhāvessanti', 'cultivating a quality (verb, present or future)', 'will cultivate a quality (3rd pl. future)', FUT),
    (5, 'sacchikarissati', 'making directly evident, experiencing (verb, present or future)',
     'will make directly evident, will experience (3rd sg. future)', FUT),
    (5, 'sacchikarissatīti', 'making directly evident, experiencing (verb, present or future)',
     'will make directly evident, will experience (3rd sg. future, with the question particle -ti)', FUT),
    (5, 'sacchikarissanti', 'making directly evident, experiencing (verb, present or future)',
     'will make directly evident, will experience (3rd pl. future)', FUT),
]


def sample_headwords():
    return set(T.read_decisions(os.path.join(HERE, 'decisions-sample.txt')))


def apply(write):
    protected = sample_headwords()
    texts = {k: open(dec_path(k), encoding='utf-8').read() for k in PARTS}
    for k in PARTS:
        if '\r' in texts[k]:
            sys.exit(f'part {k}: CR in decisions file')
    lines = {k: texts[k].split('\n') for k in PARTS}
    errs, log, changed = [], [], defaultdict(set)
    seen = set()
    for part, hw, old, new, why in REPL:
        part, hw, old, new = str(part), nfc(hw), nfc(old), nfc(new)
        if (part, hw, old) in seen:
            errs.append(f'duplicate table row: p{part} {hw} {old!r}')
            continue
        seen.add((part, hw, old))
        if part == '1' and hw in protected:
            errs.append(f'p1 {hw}: sample headword, must not be changed')
            continue
        idx = [i for i, l in enumerate(lines[part]) if l.startswith(hw + ': {')]
        if len(idx) != 1:
            errs.append(f'p{part} {hw}: {len(idx)} decision lines')
            continue
        i = idx[0]
        body = lines[part][i][len(hw) + 3:-1]
        # the tag must be a whole tag: preceded by line start or "; ", followed by end, ": " (values follow)
        pat = re.compile(r'(^|; )' + re.escape(old) + r'(?=$|: )')
        hits = pat.findall(body)
        if len(hits) != 1:
            errs.append(f'p{part} {hw}: old tag found {len(hits)} times: {old!r}')
            continue
        if old == new:
            errs.append(f'p{part} {hw}: old == new')
            continue
        newbody = pat.sub(lambda m: m.group(1) + new, body, count=1)
        lines[part][i] = hw + ': {' + newbody + '}'
        changed[part].add(hw)
        log.append((part, hw, old, new, why))
    if errs:
        print(f'APPLY FAILED ({len(errs)}):')
        for e in errs:
            print('  ' + e)
        return 1
    for k in PARTS:
        print(f'part {k}: {len(changed[k])} lines changed')
    print(f'total replacements: {len(log)}')
    if write:
        for k in PARTS:
            with open(dec_path(k), 'w', encoding='utf-8', newline='\n') as f:
                f.write('\n'.join(lines[k]))
        with open(os.path.join(HERE, 'tidy-log.tsv'), 'w', encoding='utf-8', newline='\n') as f:
            f.write('part\theadword\told tag\tnew tag\treason\n')
            for row in log:
                f.write('\t'.join(row) + '\n')
        print('written: decisions-part1..5.txt, tidy-log.tsv')
    else:
        for row in log:
            print('  p{} {}: {!r} -> {!r}'.format(*row[:4]))
    return 0


def samplecheck():
    sample = [l for l in open(os.path.join(HERE, 'sample-senses.md'), encoding='utf-8').read().splitlines() if l]
    part1 = {T.parse_out_line(l)[0]: l
             for l in open(os.path.join(HERE, 'part1-senses.md'), encoding='utf-8').read().splitlines() if l}
    bad = [l for l in sample if part1.get(T.parse_out_line(l)[0]) != l]
    print(f'sample lines: {len(sample)} | identical in part1-senses.md: {len(sample) - len(bad)}')
    for l in bad:
        print('  DIFFERS: ' + l)
    return 1 if bad else 0


if __name__ == '__main__':
    a = [nfc(x) for x in sys.argv[1:]]
    if a[:1] == ['families']:
        families()
    elif a[:1] == ['dump'] and len(a) == 2:
        dump(a[1])
    elif a[:1] == ['backup']:
        backup()
    elif a[:1] == ['apply']:
        sys.exit(apply('--write' in a))
    elif a[:1] == ['samplecheck']:
        sys.exit(samplecheck())
    else:
        sys.exit(__doc__)
