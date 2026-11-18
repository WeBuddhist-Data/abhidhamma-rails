"""Part 1 helper: append decision lines for headwords 121-622 of agg-part1.tsv to decisions-part1.txt.
Each headword was reviewed by hand (Vietnamese values vs the approved Russian line, `words`/`show` for
every multi-value or multi-sense case). EXPLICIT holds the hand-written lines (splits, combined tags,
headwords missing from the Russian file). Every other headword was checked to be a one-meaning word
whose Russian line has exactly ONE sense; its tag is that Russian tag copied word for word.
The script stops if a headword not in EXPLICIT has no Russian line or a multi-sense Russian line."""
import os
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import senses_tool_vi as T  # noqa: E402

N = unicodedata.normalize
EXPLICIT = {
    'brahma': "divine, sublime, in brahmavihāra (compound member): cao thượng; "
              "the Brahmā world, in brahmaloka (compound member): Phạm Thiên",
    'mano': "mind, the thinking faculty, also adjectival 'mental' and the synonym of mind in the "
            "definition of citta (compound member and nominative sg.)",
    'kiriyā': "merely functional, producing no result (stem and compound member): chức năng / mang tính chức năng; "
              "doing, in akiriyā 'not doing' (noun): làm",
    'Dukaṃ': "pairs, the dyads of the matrix (heading member, as in Cūḷantaradukaṃ): bộ đôi; "
             "classification by twos, the section of the matter chapter (heading): phân loại theo nhóm hai",
    'Duka': "pairs, the dyad groups (heading member): bộ đôi; "
            "classification by twos, in Dukaniddeso of the matter chapter (heading member): phân loại theo nhóm hai",
    'cetasikaṃ': "mental, of the mind as opposed to the body (neuter sg. adjective): trong tâm / trạng thái trong tâm; "
                 "a mental concomitant, in acetasikaṃ (noun): đồng hành với tâm",
    'Parāmāsa': "misapprehension, wrong grasping by views, also in sīlabbataparāmāsa 'misapprehension of rules "
                "and rituals' (stem, heading member and compound final)",
    'ṭhiti': "stability, steadiness of mind (in the concentration list): sự ổn định; "
             "persistence, lasting of life (in the life-faculty list): sự tồn tại",
    'sampaggāho': "firm upholding of the mind (in the energy list): sự dốc sức; "
                  "self-exaltation (in the conceit list): sự tự đề cao",
    'nikkhitta': "laid down, put aside, in anikkhittachandatā and anikkhittadhuratā (compound member)",
    'khandhā': "aggregates, groups of phenomena (nominative pl.): khối; "
               "classes of offences, in āpattikkhandhā (compound final): nhóm",
    'maggo': "the path, as a set of factors, also the road in kummaggo 'crooked road', a synonym of wrong view "
             "(nominative sg.)",
    'hetū': "roots, the root conditions (nominative pl.): gốc rễ; "
            "causes, in the definition of skill in what is possible (nominative pl.): nguyên nhân",
    'āhāro': "nutriment, a sustaining condition, including edible food in kabaḷīkāro āhāro (nominative sg.)",
    'dukkha': "difficult, of the mode of progress in dukkhapaṭipadā (compound member): khó khăn; "
              "pain, painful feeling, bodily or in adukkhamasukha (stem and compound member): khó chịu / sự đau khổ; "
              "suffering in general, as in dukkhamūla 'root of suffering' (compound member): khổ đau / sự đau khổ",
    'sukha': "easy, pleasant, of the mode of progress in sukhapaṭipadā (compound member): dễ dàng; "
             "happiness, pleasant feeling of mind or body, as jhāna factor, in sukhindriya and in "
             "diṭṭhadhammasukhavihāra (compound member): hạnh phúc / dễ chịu",
    'bahiddhā': "externally, external, of what lies outside oneself (adverb and adjective): ở bên ngoài bản thân; "
                "outside, in 'ito bahiddhā' 'outside this Teaching' (adverb): bên ngoài",
    'eva': "quite, emphatic intensifier in vivicceva 'quite secluded' (particle): hoàn toàn; "
           "certainly, emphatic assertion in the matter chapter's 'sabbaṃ rūpaṃ … eva' (particle): chắc chắn",
    'āhāraṃ': "nutriment, a sustaining condition (accusative sg.): dưỡng chất; "
              "edible food, in 'āhāraṃ āhāreti' 'takes food' (accusative sg.): thức ăn",
}
EXPLICIT = {N('NFC', k): N('NFC', v) for k, v in EXPLICIT.items()}

aggp, decp, _ = T.part_paths('1')
rows = T.read_agg(aggp)
dec = T.read_decisions(decp)
ru = {}
with open(T.RU_SENSES, encoding='utf-8-sig') as f:
    for l in f:
        l = N('NFC', l.rstrip('\n'))
        i = l.find(': {')
        if i > 0 and l.endswith('}'):
            ru[l[:i]] = l[i + 3:-1]
out, errs = [], []
for h in rows:
    if h in dec or not rows[h]['vals']:
        continue
    if h in EXPLICIT:
        out.append(f'{h}: {{{EXPLICIT[h]}}}')
        continue
    if h not in ru:
        errs.append(f'{h}: no Russian line and no explicit decision')
        continue
    senses = ru[h].split('; ')
    if len(senses) != 1:
        errs.append(f'{h}: Russian line has {len(senses)} senses; needs an explicit decision')
        continue
    out.append(f'{h}: {{{senses[0].rsplit(": ", 1)[0]}}}')
if errs:
    print('\n'.join(errs))
    sys.exit(1)
with open(decp, 'a', encoding='utf-8', newline='\n') as f:
    f.write('# Part 1, headwords 121-622 (added for part 1; the 120 lines above are decisions-sample.txt unchanged).\n')
    f.write('\n'.join(out) + '\n')
print(f'appended {len(out)} decision lines')
