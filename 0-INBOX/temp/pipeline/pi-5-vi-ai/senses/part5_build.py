"""Part 5: write decisions-part5.txt from (a) the hand-written decision lines in OVERRIDES below and
(b) for every other headword, the prior tag reviewed row by row with part5_draft.py (pi-4 … pi-1 Vietnamese
tag whose values match, else the single pi-5 Russian tag). Flagged draft rows (Vietnamese mismatch, several
values, multi-sense Russian line) must be either overridden or listed in ACCEPTED (draft checked by hand).
  python -I -X utf8 -B part5_build.py      then: python -I -X utf8 -B senses_tool_vi.py build --part 5
"""
import os
import sys
import importlib.util

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('p5d', os.path.join(HERE, 'part5_draft.py'))
p5d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p5d)
stv = p5d.stv

OVERRIDES = r"""
sasaṅkhāra: {with forceful effort, in sasaṅkhāraparinibbāyī (compound member)}
āyatanā: {sense bases, the sense fields, also when counted as in pañcevāyatanā (nominative pl.)}
mūla: {roots of plants (compound member): rễ cây; basis, foundation: gốc rễ}
assu: {tears, in the list asuci assu lohitaṃ sedo (nominative sg.)}
arūpino: {without material form (nominative pl.)}
Rūpino dhammā: {material phenomena, a dyad of the matrix (nominative pl.)}
Tiṭṭhanti: {remain, abide: tồn tại / đứng vững; lie in wait, in paripanthe tiṭṭhanti: mai phục}
manasikārā: {attention, attentions, as in amanasikārā (nominative pl.)}
āyu: {lifespan, vital duration, also in āyusaṅkhāro (stem and compound member)}
karaṇaṃ: {making, causing: tạo ra; making diverse, in nānākaraṇaṃ: tạo nên}
ārammaṇo: {having as object, compound final, as in sārammaṇo, anārammaṇo and ekārammaṇo (masculine nominative sg.)}
saññī: {perceiving, one who perceives (masculine nominative sg.)}
jātā: {born, come to birth, in sahajātā 'born together' (nominative pl. participle): sinh; filled with, in vedajātā: tràn đầy}
vihāra: {abiding, dwelling, in anupubbavihāra 'successive abidings' (compound final): an trú; monastic residence: tịnh xá}
samanantarā: {immediately after, right after (adverb)}
samādiyitvā: {having undertaken, taken upon oneself (absolutive)}
ekanta: {wholly, completely (compound member)}
bhāṇī: {one who speaks, compound final}
niyato: {fixed, certain in its result, of a person fixed in destiny as in sammattaniyato (masculine nominative sg.)}
uppāditaṃ: {shed, of blood (neuter sg. participle): bị làm cho chảy; aroused, of a state of mind: đã được làm sinh khởi}
Pāpa: {bad, evil, in pāpakamma 'evil deed' (compound member)}
hetunā: {by a root, a root condition, as in lobhahetunā and 'tena hetunā sahetukā' (instrumental sg.)}
dissanti: {appear to be, seem: dường như; are found, of readings: thấy}
ṭho: {lasting an aeon, in kappaṭṭho}
bhāvetvā: {having developed, having cultivated (absolutive)}
okkamati: {steps into, in 'niyāmaṃ okkamati' 'enters the fixed course' (3rd sg.): bước vào; descends into the womb: nhập vào / đi vào}
anuseti: {lies latent, persists dormant in beings (3rd sg. present)}
Dukkhāya: {painful, of the feeling (feminine dative/genitive sg.): khó chịu; to misery (dative): khổ đau}
kaṇṇo: {organ of hearing: tai; corner, in catukkaṇṇo: góc}
uppanna: {arisen, as in uppannavatthukā and uppannārammaṇā (compound member)}
saḷāyatanaṃ: {the six sense bases, as in Saḷāyatanakathā (nominative sg.)}
suññataṃ: {empty, emptiness, as the object of the path in 'suññataṃ ārabbha' (neuter sg.)}
kusalaṃ cittaṃ: {wholesome mind, as in 'kusalaṃ cittaṃ paṭilabheyya' (accusative sg.)}
"""

# flagged draft rows whose draft line (single pi-5 Russian tag, or matching Vietnamese tag) was checked and kept
ACCEPTED = """
santo paṇḍitā paccati bhāvo rūpānaṃ samuṭṭhitaṃ mogha samiddhi avaseso padesu me Sabbaso bhaṇati kāmo
jhāyī lābhī bāhira seyyā ṭhita amanussa rato vagga āpajjati Rūpataṇhā sīsaṃ yāpeti kareyya
rūpaṃ_kusalaṃ ārabbha_uppajjati citte_vattamāne vattamāne samaṅgī cakkhuviññāṇasamaṅgī uppādaṃ
vitakko_vicāro Mato visayaṃ Cakkhuviññāṇaṃ_uppajjati Cakkhuviññāṇaṃ_kusalaṃ Saṃvaro_kammaṃ
dhammataṇhā_lobho bhojanaṃ Anāgatārammaṇaṃ akusalā_dhammā
akusalaṃ_kāyakammaṃ akusalaṃ_manokammaṃ akusalaṃ_vacīkammaṃ
"""

HEADER = """# pi-5 (Kathāvatthu) Pāli→Vietnamese senses, part 5 (agg-part5.tsv, 908 headwords).
# Hand-reviewed tag table, headword by headword, following senses-conventions.md (pi-5) §2: the approved pi-4, then
# pi-3, pi-2, pi-1 Vietnamese tag where the Vietnamese values match (example / grammar label adapted where it does not
# fit pi-5); otherwise the approved pi-5 Russian tag word for word; new or combined tags only where needed.
# Written by part5_build.py (hand decisions in its OVERRIDES). Build: python -I -X utf8 -B senses_tool_vi.py build --part 5
"""


def main():
    aggp, decp, _ = stv.part_paths('5')
    rows = stv.read_agg(aggp)
    idx = stv._prior_index()
    over = {}
    for line in OVERRIDES.strip().splitlines():
        line = stv.nfc(line.strip())
        hw = line.split(': {', 1)[0]
        if hw not in rows:
            sys.exit(f'override for headword not in part 5: {hw!r}')
        if hw in over:
            sys.exit(f'duplicate override: {hw!r}')
        over[hw] = line
    accepted = {stv.nfc(w.replace('_', ' ')) for w in ACCEPTED.split()}
    for w in accepted:
        if w not in rows:
            sys.exit(f'accepted headword not in part 5: {w!r}')
    out, errs, n_over, n_auto = [], [], 0, 0
    for h, r in rows.items():
        if not r['vals']:
            continue
        if h in over:
            out.append(over[h])
            n_over += 1
            continue
        dl, src, notes, _ = p5d.propose(h, r, idx)
        if dl is None or (notes and h not in accepted):
            errs.append(f'{h}: flagged {notes}, needs an override or ACCEPTED entry')
            continue
        out.append(dl)
        n_auto += 1
    unused = accepted - {h for h in rows if h not in over}
    if errs:
        print('\n'.join(errs))
        sys.exit(f'{len(errs)} rows unresolved')
    with open(decp, 'w', encoding='utf-8', newline='\n') as f:
        f.write(HEADER + '\n'.join(out) + '\n')
    print(f'wrote {len(out)} decision lines ({n_over} hand overrides, {n_auto} reviewed prior tags) -> {decp}')


if __name__ == '__main__':
    main()
