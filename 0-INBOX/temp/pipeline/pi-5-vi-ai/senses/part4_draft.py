"""Part 4: write decisions-part4.txt from (a) the hand-written decision lines in OVERRIDES below and
(b) for every other headword, the prior tag reviewed row by row with part4_view.py (approved pi-4 … pi-1
Vietnamese tag whose sense has a matching value, else the single pi-5 Russian tag).
  python -I -X utf8 -B part4_draft.py
"""
import importlib.util
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('p4v', os.path.join(HERE, 'part4_view.py'))
p4v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p4v)
stv = p4v.stv

OVERRIDES = r"""
kataṃ: {what has been done: đã được làm / làm; the making or determining of a fruit, in 'phalassa kataṃ paññāpeti' (neuter sg. noun): sự phân định}
jīvitaṃ: {life, being alive, beside the life faculty in 'atthi jīvitaṃ, atthi jīvitindriyaṃ' (neuter sg.)}
maṃsa: {flesh, in maṃsacakkhu 'the fleshly eye' and maṃsasota (compound member)}
yoni: {mode of coming to birth: cách sinh; class of beings, in tiracchānayoni: cõi}
kāyā: {order of beings one dies out of: thân; groups, classes, in chaviññāṇakāyā (compound final): nhóm}
vāla: {hair, in the topknot compound cittavaṇḍavālamoḷiṃ (compound member)}
setu: {Setu, a young brahmin, proper name: Sê-tu; causeway, bridge, in setukārakā 'bridge builders' (compound member): cầu}
putto: {male child}
bhūmi: {the ground underfoot}
gacchati: {goes, travels to a destination: đi đến / bước đi; comes to, in 'gaṇanaṃ gacchati' 'is counted in' (3rd sg. verb): được … vào}
gatiyo: {places of rebirth: cõi tái sinh; courses open to the great man, in 'dveva gatiyo bhavanti' (nominative pl.): hướng đi}
purisassa: {of a male human, an individual: con người; of the great man, the bearer of the thirty-two marks, in mahāpurisassa (genitive sg.): bậc đại nhân}
suttaṃ: {a sermon of the Buddha}
avasesa: {remainder, what is left over, in anavasesappahānaṃ 'abandoning without remainder' (compound member)}
samāpajjantassa: {of one going into an attainment}
samāpajjati: {goes into an attainment}
pariyāye: {encompassing, in cetopariyāye: bao quát; occasion, turn, in apare vā pariyāye: lượt}
mithu: {mutual, each other, in mithubhedā 'through mutual split' (compound member)}
muttaṃ: {urine, in the washing simile 'muttena muttaṃ dhovati' (accusative sg.)}
niyāmatā: {fixed order of things, in dhammaniyāmatā: tính cố định; certainty of destiny, the fixed course: tính cố định}
āruppā: {the immaterial attainments}
bhūtā: {elements, the primaries (nominative pl.): yếu tố; become, achieved, in vasībhūtā: đã đạt được}
sakavādi: {the proponent of one's own doctrine}
cetasiko: {belonging to mind, a concomitant}
vādaṃ: {speech, in musāvādaṃ 'false speech' (compound final, accusative sg.)}
seyyaṃ: {sleeping place}
Latā: {climbing plant}
tīraṃ: {bank, coast}
ratto: {dyed with lust, impassioned: người đã tham đắm; by night, in divā ca ratto ca: đêm}
āhārā: {nutriments, sustaining conditions (nominative pl.): dưỡng chất; food, in samānāhārā 'having the same food' (compound final): thức ăn}
vipākā: {having results, in sukhavipākā}
udakaṃ: {water, also as rainfall}
pavattati: {goes on, comes about, of mental states: khởi lên; runs down, of water: chảy xuôi}
"""


def main():
    rows = stv.read_agg(p4v.AGG)
    idx = p4v.prior_idx()
    ov = {}
    for line in OVERRIDES.strip().splitlines():
        line = stv.nfc(line.strip())
        if line:
            hw = line.split(': {', 1)[0]
            if hw in ov:
                sys.exit(f'override twice: {hw}')
            if hw not in rows:
                sys.exit(f'override for headword not in agg-part4.tsv: {hw}')
            ov[hw] = line
    out = ['# pi-5 (Kathāvatthu) Pāli→Vietnamese senses, part 4 (agg-part4.tsv, 908 rows).',
           '# Tag table reviewed headword by headword (senses-conventions.md §2): the approved pi-4 … pi-1 Vietnamese',
           '# tag where pi-5 has the same headword, sense and Vietnamese value (example or label adapted where it does',
           '# not occur in pi-5), otherwise the approved pi-5 Russian tag word for word; new tags only where the',
           '# Vietnamese splits differently, the Russian has no line, or the prior example points to another sense.',
           '# Build: python -I -X utf8 -B senses_tool_vi.py build --part 4']
    todo = []
    for hw, r in rows.items():
        if not r['vals']:
            continue
        if hw in ov:
            out.append(ov[hw])
            continue
        tag, src = p4v.draft_line(hw, r, idx)
        if tag is None:
            todo.append(hw)
            continue
        out.append(f'{hw}: {{{tag}}}')
    with open(p4v.DEC, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(out) + '\n')
    print(f'wrote {len(out) - 6} decision lines ({len(ov)} hand-written overrides); TODO: {todo}')


if __name__ == '__main__':
    main()
