"""Assemble decisions-part1.txt: the 120 decision lines of decisions-sample.txt verbatim, then the part-1 decisions for agg-part1 lines 121-376."""
import os

D = os.path.dirname(os.path.abspath(__file__))

REST = r"""
# pi-6 Hindi senses, part 1, headwords 121-376 (agg-part1.tsv). Conventions: senses-conventions-pi6.md
akusalamūlakaṃ: {based on an unwholesome root (neuter sg.)}
akusalamūlakañceva: {based on an unwholesome root, with enclitic -ñceva 'both' (neuter sg.)}
akusalamūlamūlakāti: {based on a root of the unwholesome roots, with quotative -ti (nominative pl.)}
akusalamūlamūlakaṃ: {based on a root of the unwholesome roots (neuter sg.)}
akusalamūlamūlakañceva: {based on a root of the unwholesome roots, with enclitic -ñceva 'both' (neuter sg.)}
abyākatamūlāti: {indeterminate roots, roots neither wholesome nor unwholesome, with quotative -ti (nominative pl.)}
abyākatamūlāni: {indeterminate roots, roots neither wholesome nor unwholesome, the roots themselves (neuter nominative pl.)}
abyākatāti: {neither wholesome nor unwholesome, said of phenomena, with quotative -ti (nominative pl.)}
abyākataṃ: {neither wholesome nor unwholesome (neuter sg.)}
abyākatamūlasahajātā dhammā: {phenomena born together with an indeterminate root (nominative pl.)}
abyākatamūlamūlāti: {roots of the indeterminate roots, with quotative -ti (nominative pl.)}
abyākatamūlamūlāni: {roots of the indeterminate roots (neuter nominative pl.)}
abyākatamūlakāti: {based on an indeterminate root, with quotative -ti (nominative pl.)}
abyākatamūlakaṃ: {based on an indeterminate root (neuter sg.)}
abyākatamūlamūlakāti: {based on a root of the indeterminate roots, with quotative -ti (nominative pl.)}
abyākatamūlamūlakaṃ: {based on a root of the indeterminate roots (neuter sg.)}
nāmamūlāti: {roots of mentality, roots on the mental side, with quotative -ti (nominative pl.)}
nāmamūlāni: {roots of mentality, roots on the mental side, the roots themselves (neuter nominative pl.)}
nāmāti: {mentality, the mental side of phenomena, with quotative -ti (nominative pl.)}
nāmasamuṭṭhānaṃ: {originated from mentality, said of matter (neuter sg.)}
nāmaṃ: {mentality, the mental side of phenomena (neuter sg.)}
nāmañca: {and mentality, the mental side of phenomena, with enclitic -ñca (neuter sg.)}
nāmamūlasahajātā: {born together with a root of mentality, said of phenomena (nominative pl.)}
nāmamūlamūlāti: {roots of the roots of mentality, with quotative -ti (nominative pl.)}
nāmamūlamūlāni: {roots of the roots of mentality (neuter nominative pl.)}
nāmamūlakāti: {based on a root of mentality, with quotative -ti (nominative pl.)}
nāmamūlakaṃ: {based on a root of mentality (neuter sg.)}
nāmamūlakañceva: {based on a root of mentality, with enclitic -ñceva 'both' (neuter sg.)}
nāmamūlamūlakāti: {based on a root of the roots of mentality, with quotative -ti (nominative pl.)}
nāmamūlamūlakaṃ: {based on a root of the roots of mentality (neuter sg.)}
nāmamūlamūlakañceva: {based on a root of the roots of mentality, with enclitic -ñceva 'both' (neuter sg.)}
mūlavāraniddeso: {the exposition of the section on roots (heading)}
kusalahetūti: {wholesome causes, second of the ten names for a root, with quotative -ti (nominative pl.)}
nāmappabhavā: {beginnings of mentality, fifth of the ten names for a root (nominative pl.)}
bhagavato: {of the Blessed One, the Lord (genitive sg.)}
nāmahetū: {causes of mentality, second of the ten names for a root (nominative pl.)}
nāmapaccayā: {conditions of mentality, ninth of the ten names for a root (nominative pl.)}
niddesavāro: {the exposition section, the round that answers the questions (heading)}
sammāsambuddhassa: {of the perfectly self-awakened Buddha (genitive sg.)}
nāmasambhavā: {generators of mentality, fourth of the ten names for a root (nominative pl.)}
namo: {homage, reverence (nominative sg.)}
nāmāhārā: {nutriments of mentality, seventh of the ten names for a root (nominative pl.)}
nāmārammaṇā: {objects of mentality, eighth of the ten names for a root (nominative pl.)}
nāmasamudayā: {origins of mentality, tenth of the ten names for a root (nominative pl.)}
mūlayamakapāḷi: {the Pairs on Roots, title of the first chapter, in its closing line (heading)}
nāmasamuṭṭhānā: {originators of mentality, sixth of the ten names for a root (nominative pl.)}
nāmanidānā: {sources of mentality, third of the ten names for a root (nominative pl.)}
arahato: {of the worthy one, the arahant (genitive sg.)}
khandhayamakaṃ: {the Pairs on the Aggregates, title of the second chapter (heading)}
viññāṇakkhandho: {the aggregate of consciousness (nominative sg.)}
vedanākkhandho: {the aggregate of feeling (nominative sg.)}
rūpakkhandho: {the aggregate of material form (nominative sg.)}
saṅkhārakkhandho: {the aggregate of mental formations (nominative sg.)}
saññākkhandho: {the aggregate of perception (nominative sg.)}
pañcakkhandhā: {the five aggregates, the five groups of phenomena (nominative pl.)}
paṇṇattivāro: {the section on terminology (heading)}
viññāṇaṃ: {consciousness, the bare word in the word-checking pairs (nominative sg.)}
vedanā: {feeling, the bare word in the word-checking pairs (nominative sg.)}
saṅkhārā: {formations, the bare word in the word-checking pairs, also the three kinds of formation in the Saṅkhārayamaka (nominative pl.)}
saññā: {perception, recognition, the bare word in the word-checking pairs (nominative sg.)}
padasodhanavāro: {the section on checking the words (heading)}
anulomaṃ: {the positive part, with affirmative questions (heading)}
paccanīkaṃ: {the negative part, with negated questions (heading)}
padasodhanamūlacakkavāro: {the section on the cycle based on checking the words (heading)}
khandhā: {aggregates, groups of phenomena (nominative pl.)}
suddhakhandhavāro: {the section on the aggregates alone (heading)}
suddhakhandhamūlacakkavāro: {the section on the cycle based on the aggregates alone (heading)}
paṇṇattivāraniddesa: {the exposition of the section on terminology (heading)}
uppādavāro: {the section on arising (heading)}
pavattivāro: {the section on the process of occurrence (heading)}
anulomapuggalo: {the positive part, by person (heading)}
anulomaokāso: {the positive part, by place (heading)}
anulomapuggalokāsā: {the positive part, by person and place (heading)}
paccanīkapuggalo: {the negative part, by person (heading)}
paccanīkaokāso: {the negative part, by place (heading)}
paccanīkapuggalokāsā: {the negative part, by person and place (heading)}
khandho: {aggregate, group of phenomena (nominative sg.)}
atītānāgatavāro: {the section on past and future (heading)}
nirodhavāro: {the section on ceasing (heading)}
pavatti: {the process of occurrence, before the section number (heading member)}
paṇṇattiuddesavāro: {the summary section on terminology, the round that lists the questions (heading)}
uppādanirodhavāro: {the section on arising and ceasing (heading)}
viññāṇakkhandhoti: {the aggregate of consciousness, with quotative -ti (nominative sg.)}
vedanākkhandhoti: {the aggregate of feeling, with quotative -ti (nominative sg.)}
rūpakkhandhoti: {the aggregate of material form, with quotative -ti (nominative sg.)}
saṅkhārakkhandhoti: {the aggregate of mental formations, with quotative -ti (nominative sg.)}
saṅkhārakkhandhaṃ: {the aggregate of mental formations (accusative sg.)}
saññākkhandhoti: {the aggregate of perception, with quotative -ti (nominative sg.)}
ṭhapetvā: {leaving aside, excepting (absolutive)}
viññāṇanti: {consciousness, the bare word in the word-checking pairs, with quotative -ti (nominative sg.)}
vedanāti: {feeling, the bare word in the word-checking pairs, with quotative -ti (nominative sg.)}
rūpañceva: {the bare word 'form' in the word-checking pairs, wider than the aggregate or sense base, with enclitic -ñceva 'both' (nominative sg.)}
rūpanti: {the bare word 'form' in the word-checking pairs, wider than the aggregate or sense base, with quotative -ti (nominative sg.)}
saṅkhārāti: {formations, the bare word in the word-checking pairs, with quotative -ti (nominative pl.)}
diṭṭhisaññā: {perception in the sense of a view, wider than the aggregate of perception (nominative sg.)}
saññāti: {perception, recognition, the bare word in the word-checking pairs, with quotative -ti (nominative sg.)}
rūpakkhandhañca: {and the aggregate of material form, with enclitic -ñca (accusative sg.)}
saṅkhārakkhandhañca: {and the aggregate of mental formations, with enclitic -ñca (accusative sg.)}
saññākkhandhañca: {and the aggregate of perception, with enclitic -ñca (accusative sg.)}
rūpañca: {and the bare word 'form' in the word-checking pairs, wider than the aggregate or sense base, with enclitic -ñca (accusative sg.)}
saṅkhāre: {formations, the bare word in the word-checking pairs (accusative pl.)}
saññañca: {and perception, recognition, the bare word in the word-checking pairs, with enclitic -ñca (accusative sg.)}
avasesā khandhā: {the remaining aggregates, the rest of the five (nominative pl.)}
pariññāvāro: {the section on full understanding (heading)}
khandhoti: {aggregate, group of phenomena, with quotative -ti (nominative sg.)}
khandhe: {aggregates, groups of phenomena (accusative pl.)}
viññāṇañca: {and consciousness, the bare word in the word-checking pairs, with enclitic -ñca (accusative sg.)}
vedanaṃ: {feeling, the bare word in the word-checking pairs (accusative sg.)}
vedanañca: {and feeling, the bare word in the word-checking pairs, with enclitic -ñca (accusative sg.)}
saññaṃ: {perception, recognition, the bare word in the word-checking pairs (accusative sg.)}
paṇṇattiniddesavāro: {the exposition section on terminology (heading)}
uppajjati: {arises, comes into being (3rd sg. present)}
uppajjatīti: {arises, comes into being, with quotative -ti (3rd sg. present)}
pañcavokāraṃ: {five-aggregate existence, as a place (accusative sg.)}
arūpaṃ: {the immaterial realm, as a place of rebirth (accusative sg.)}
asaññasattaṃ: {the realm of non-percipient beings, as a place (accusative sg.)}
upapajjantānaṃ: {those being reborn (genitive pl. present participle)}
pañcavokāre: {five-aggregate existence, as a place (locative)}
arūpe: {the immaterial realm, as a place (locative)}
asaññasatte: {the realm of non-percipient beings, as a place (locative)}
nuppajjati: {does not arise, with fused negative na (3rd sg. present)}
nuppajjatīti: {does not arise, with fused negative na and quotative -ti (3rd sg. present)}
cavantānaṃ: {those dying, passing away (genitive pl. present participle)}
uppajjittha: {arose, had come into being (3rd sg. aorist)}
uppajjitthāti: {arose, had come into being, with quotative -ti (3rd sg. aorist)}
pañcavokārānaṃ: {beings of five-aggregate existence (genitive pl.)}
arūpānaṃ: {beings of the immaterial realm (genitive pl.)}
asaññasattānaṃ: {non-percipient beings (genitive pl.)}
nuppajjittha: {did not arise, with fused negative na (3rd sg. aorist)}
nuppajjitthāti: {did not arise, with fused negative na and quotative -ti (3rd sg. aorist)}
natthi: {there is none, the short answer that no such case exists (3rd sg. present)}
suddhāvāsānaṃ: {beings of the Pure Abodes (genitive pl.)}
uppajjissati: {will arise, will come into being (3rd sg. future)}
uppajjissatīti: {will arise, will come into being, with quotative -ti (3rd sg. future)}
parinibbāyissanti: {they will attain final nibbāna (3rd pl. future)}
itaresaṃ: {the rest, all the others, standing alone (genitive pl.): बाकी सब; the other ones of a named group, before that group (genitive pl.): बाकी}
upapajjitvā: {having been reborn (absolutive)}
nuppajjissati: {will not arise, with fused negative na (3rd sg. future)}
nuppajjissatīti: {will not arise, with fused negative na and quotative -ti (3rd sg. future)}
pacchimabhavikānaṃ: {those in their last existence (genitive pl.)}
pañcavokārā: {five-aggregate existence, as a place (ablative)}
suddhāvāsaṃ: {the Pure Abodes, as a place (accusative sg.)}
parinibbantānaṃ: {those attaining final nibbāna (genitive pl. present participle)}
asaññasattā: {the realm of non-percipient beings, as a place (ablative)}
suddhāvāse: {the Pure Abodes, as a place (locative)}
nirujjhati: {ceases, comes to an end (3rd sg. present)}
nirujjhatīti: {ceases, comes to an end, with quotative -ti (3rd sg. present)}
arūpā: {the immaterial realm, as a place (ablative)}
nirujjhittha: {ceased, had come to an end (3rd sg. aorist)}
nirujjhitthāti: {ceased, had come to an end, with quotative -ti (3rd sg. aorist)}
nirujjhissati: {will cease, will come to an end (3rd sg. future)}
nirujjhissatīti: {will cease, will come to an end, with quotative -ti (3rd sg. future)}
yattha: {where, in which place, opening an abbreviated question by place (relative adverb)}
yatthakaṃ: {the 'where' portion, the questions by place to be filled in (accusative sg.)}
vadanākkhandho: {the aggregate of feeling, variant spelling of vedanākkhandho (nominative sg.)}
uppādavāre: {in the section on arising, in the abbreviation notes (locative)}
vedanākkhandhaṃ: {the aggregate of feeling (accusative sg.)}
rūpakkhandhaṃ: {the aggregate of material form (accusative sg.)}
parijānāti: {fully understands, knows thoroughly (3rd sg. present)}
parijānātīti: {fully understands, knows thoroughly, with quotative -ti (3rd sg. present)}
parijānittha: {fully understood, had known thoroughly (3rd sg. aorist)}
parijānitthāti: {fully understood, had known thoroughly, with quotative -ti (3rd sg. aorist)}
parijānissati: {will fully understand, will know thoroughly (3rd sg. future)}
parijānissatīti: {will fully understand, will know thoroughly, with quotative -ti (3rd sg. future)}
vedanākkhandhañca: {and the aggregate of feeling, with enclitic -ñca (accusative sg.)}
arahā: {the worthy one, the arahant (nominative sg.)}
arahantañca: {and the worthy one, the arahant, with enclitic -ñca (accusative sg.)}
parijānanti: {they fully understand, know thoroughly (3rd pl. present)}
aggamaggasamaṅgiñca: {and the person possessed of the highest path, with enclitic -ñca (accusative sg.)}
aggamaggasamaṅgī: {the person possessed of the highest path, at the moment of the arahant path (nominative sg.)}
puggalā: {persons, individuals (nominative pl.)}
maggaṃ paṭilabhissanti: {they will attain the path (3rd pl. future, with object)}
paṭilabhissanti: {they will attain, will obtain (3rd pl. future)}
parijānissanti: {they will fully understand, will know thoroughly (3rd pl. future)}
puthujjanā: {ordinary people, worldlings not yet on the path (nominative pl.)}
khandhayamakapāḷi: {the Pairs on the Aggregates, title of the second chapter, in its closing line (heading)}
āyatanayamakaṃ: {the Pairs on the Sense Bases, title of the third chapter (heading)}
kāyāyatanaṃ: {the body sense base (nominative sg.)}
sotāyatanaṃ: {the ear sense base (nominative sg.)}
cakkhāyatanaṃ: {the eye sense base (nominative sg.)}
dhammāyatanaṃ: {the sense base of mind-objects (nominative sg.)}
manāyatanaṃ: {the mind sense base (nominative sg.)}
ghānāyatanaṃ: {the nose sense base (nominative sg.)}
gandhāyatanaṃ: {the smell sense base (nominative sg.)}
saddāyatanaṃ: {the sound sense base (nominative sg.)}
rasāyatanaṃ: {the taste sense base (nominative sg.)}
jivhāyatanaṃ: {the tongue sense base (nominative sg.)}
phoṭṭhabbāyatanaṃ: {the tangible sense base, base of the touchable (nominative sg.)}
rūpāyatanaṃ: {the visible-form sense base, the object of the eye (nominative sg.)}
kāyo: {the body, the bare word in the word-checking pairs (nominative sg.)}
sotaṃ: {the ear, the hearing organ, the bare word in the word-checking pairs (nominative sg.)}
cakkhu: {the eye, the seeing organ, the bare word in the word-checking pairs (nominative sg.)}
mano: {mind, the bare word in the word-checking pairs (nominative sg.)}
ghānaṃ: {the nose, the smelling organ, the bare word in the word-checking pairs (nominative sg.)}
gandho: {smell, odour, the bare word in the word-checking pairs (nominative sg.)}
saddo: {sound, what is heard, the bare word in the word-checking pairs (nominative sg.)}
raso: {taste, flavour, the bare word in the word-checking pairs (nominative sg.)}
jivhā: {the tongue, the tasting organ, the bare word in the word-checking pairs (nominative sg.)}
phoṭṭhabbo: {tangible object, what is touched, the bare word in the word-checking pairs (nominative sg.)}
cakkaṃ: {the cycle of questions, to be filled in by the reader (nominative sg.)}
āyatanā: {sense bases, the sense fields, the bare word in the word-checking pairs (nominative pl.)}
suddhāyatanavāro: {the section on the sense bases alone (heading)}
nāyatanā: {not sense bases, with fused negative na (nominative pl.)}
suddhāyatanamūlacakkavāro: {the section on the cycle based on the sense bases alone (heading)}
āyatanaṃ: {sense base, the sense field (nominative/accusative sg.)}
nāyatanaṃ: {not a sense base, with fused negative na (nominative sg.)}
kāyoti: {the body, the bare word in the word-checking pairs, with quotative -ti (nominative sg.)}
kāyāyatananti: {the body sense base, with quotative -ti (nominative sg.)}
kāyāyatanañca: {and the body sense base, with enclitic -ñca (nominative/accusative sg.)}
samādhigandho: {the scent of concentration, a figurative scent in the word-checking answers (nominative sg.)}
taṇhāsotaṃ: {the stream of craving, sota as 'stream', in the word-checking answers (nominative sg.)}
dibbasotaṃ: {the divine ear, supernormal hearing, in the word-checking answers (nominative sg.)}
dibbacakkhu: {the divine eye, supernormal sight, in the word-checking answers (nominative sg.)}
sotañceva: {the ear, the hearing organ, the bare word in the word-checking pairs, with enclitic -ñceva 'both' (nominative sg.)}
sotanti: {the ear, the hearing organ, the bare word in the word-checking pairs, with quotative -ti (nominative sg.)}
sotāyatananti: {the ear sense base, with quotative -ti (nominative sg.)}
sotāyatanañca: {and the ear sense base, with enclitic -ñca (nominative/accusative sg.)}
cakkhāyatananti: {the eye sense base, with quotative -ti (nominative sg.)}
cakkhāyatanañca: {and the eye sense base, with enclitic -ñca (nominative/accusative sg.)}
paññācakkhu: {the eye of wisdom, a figurative eye in the word-checking answers (nominative sg.)}
cakkhūti: {the eye, the seeing organ, the bare word in the word-checking pairs, with quotative -ti (nominative sg.)}
dhammāyatananti: {the sense base of mind-objects, with quotative -ti (nominative sg.)}
dhammāyatanañca: {and the sense base of mind-objects, with enclitic -ñca (nominative/accusative sg.)}
manoti: {mind, the bare word in the word-checking pairs, with quotative -ti (nominative sg.)}
manāyatananti: {the mind sense base, with quotative -ti (nominative sg.)}
ghānanti: {the nose, the smelling organ, the bare word in the word-checking pairs, with quotative -ti (nominative sg.)}
ghānāyatananti: {the nose sense base, with quotative -ti (nominative sg.)}
gandhāyatananti: {the smell sense base, with quotative -ti (nominative sg.)}
gandhāyatanañca: {and the smell sense base, with enclitic -ñca (nominative/accusative sg.)}
sīlagandho: {the scent of virtue, a figurative scent in the word-checking answers (nominative sg.)}
paññāgandho: {the scent of wisdom, a figurative scent in the word-checking answers (nominative sg.)}
gandhoti: {smell, odour, the bare word in the word-checking pairs, with quotative -ti (nominative sg.)}
saddoti: {sound, what is heard, the bare word in the word-checking pairs, with quotative -ti (nominative sg.)}
saddāyatananti: {the sound sense base, with quotative -ti (nominative sg.)}
rasāyatananti: {the taste sense base, with quotative -ti (nominative sg.)}
rasāyatanañca: {and the taste sense base, with enclitic -ñca (nominative/accusative sg.)}
attharaso: {the taste of meaning, a figurative taste in the word-checking answers (nominative sg.)}
dhammaraso: {the taste of the teaching, a figurative taste in the word-checking answers (nominative sg.)}
vimuttiraso: {the taste of liberation, a figurative taste in the word-checking answers (nominative sg.)}
rasoti: {taste, flavour, the bare word in the word-checking pairs, with quotative -ti (nominative sg.)}
jivhāti: {the tongue, the tasting organ, the bare word in the word-checking pairs, with quotative -ti (nominative sg.)}
jivhāyatananti: {the tongue sense base, with quotative -ti (nominative sg.)}
phoṭṭhabboti: {tangible object, what is touched, the bare word in the word-checking pairs, with quotative -ti (nominative sg.)}
phoṭṭhabbāyatananti: {the tangible sense base, base of the touchable, with quotative -ti (nominative sg.)}
rūpāyatananti: {the visible-form sense base, the object of the eye, with quotative -ti (nominative sg.)}
rūpāyatanañca: {and the visible-form sense base, the object of the eye, with enclitic -ñca (nominative/accusative sg.)}
kāyañca: {and the body, the bare word in the word-checking pairs, with enclitic -ñca (accusative sg.)}
sotañca: {and the ear, the hearing organ, the bare word in the word-checking pairs, with enclitic -ñca (accusative sg.)}
cakkhuñca: {and the eye, the seeing organ, the bare word in the word-checking pairs, with enclitic -ñca (accusative sg.)}
gandhañca: {and smell, odour, the bare word in the word-checking pairs, with enclitic -ñca (accusative sg.)}
rasañca: {and taste, flavour, the bare word in the word-checking pairs, with enclitic -ñca (accusative sg.)}
manāyatanañca: {and the mind sense base, with enclitic -ñca (nominative/accusative sg.)}
avaseso: {the remaining, the rest (masculine sg.)}
āyatanañceva: {sense base, the sense field, with enclitic -ñceva 'both' (nominative sg.)}
sotāyananti: {the ear sense base, variant spelling of sotāyatananti, with quotative -ti (nominative sg.)}
āyatananti: {sense base, the sense field, with quotative -ti (nominative sg.)}
"""


def main():
    with open(os.path.join(D, 'decisions-sample.txt'), encoding='utf-8-sig') as f:
        sample = [l.rstrip('\r\n') for l in f if l.strip() and not l.startswith('#')]
    assert len(sample) == 120, len(sample)
    rest = [l for l in REST.strip('\n').split('\n')]
    with open(os.path.join(D, 'decisions-part1.txt'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(sample + rest) + '\n')
    print('sample lines', len(sample), '| rest decision lines', len([l for l in rest if l and not l.startswith('#')]))


if __name__ == '__main__':
    main()
