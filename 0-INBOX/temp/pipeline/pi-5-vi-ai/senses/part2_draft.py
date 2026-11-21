"""Part 2: write decisions-part2.txt from (a) the hand-written decision lines in OVERRIDES below and
(b) for every other headword, the reviewed prior tag (pi-4 … pi-1 Vietnamese tag with a matching value,
else the single pi-5 Russian tag) that part2_view.py printed for review row by row.
  python -I -X utf8 -B part2_draft.py
"""
import importlib.util
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('p2v', os.path.join(HERE, 'part2_view.py'))
p2v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p2v)
stv = p2v.stv

OVERRIDES = r"""
karonti: {do, perform}
cittaṃ: {mind, a state of mind (nominative/accusative sg.)}
iddhiṃ: {supernormal power, in 'iddhiṃ vikubbati' (accusative sg.)}
mātā: {mother, a parent (nominative sg.)}
pitā: {father, a parent (nominative sg.)}
bhātā: {brother (nominative sg.)}
bhaginī: {sister (nominative sg.)}
bhāga: {side, part, in ubhatobhāga}
lakkhaṇāni: {characteristics, as in saṅkhatalakkhaṇāni and asaṅkhatalakkhaṇāni (nominative pl.): đặc tính; the bodily marks of a great man, in mahāpurisalakkhaṇāni (nominative pl.): tướng}
tiṭṭhati: {stands, persists}
dukkhā: {painful, of feeling or contact (feminine sg. and pl. adjective): khó chịu; suffering, unsatisfactory: khổ đau}
viharati: {dwells, abides, in a meditative attainment as in 'upasampajja viharati' (3rd sg. verb): an trú; lives, conducts oneself in a given manner, as in 'kāye kāyānupassī viharati' (3rd sg. verb): sống}
dhammesu: {phenomena, states, as in 'dhammesu dhammānupassī' and 'ajjhattaṃ dhammesu sati' (locative pl.): hiện tượng; doctrines (locative pl.): điều}
dhammā: {phenomena, states (nominative pl.): hiện tượng; mind-objects, what the mind as sixth sense knows (nominative pl.): đối tượng của ý}
atta: {one's own being, individual: cá nhân; self, in attānudiṭṭhi 'the view of a self' (compound member): tự ngã}
Saha: {together, along with (adverb and prefix): cùng / cùng với; at the very moment: ngay khi}
nikkhamitvā: {having gone out, in 'bahiddhā nikkhamitvā avekkhati' (absolutive)}
bahiddhā: {externally, external, of what lies outside oneself (adverb and adjective): ở bên ngoài bản thân; outside, in 'bahiddhā nikkhamitvā' 'having gone outside' (adverb): bên ngoài}
uppajjati: {arises, comes into being (3rd sg. present)}
sukhāya: {pleasant, of the feeling (feminine dative/genitive sg.): dễ chịu; for well-being (dative): hạnh phúc}
dha: {Dhammapada (citation): Kinh Pháp Cú; Dhammasaṅgaṇī, in the citation 'dha. sa.' (citation abbreviation): Liệt kê các hiện tượng}
saṅkhāra: {formations, the volitional factors of the fourth aggregate (compound member): tạo tác; exertion, in sa-/asaṅkhāraparinibbāyī: sự thúc đẩy}
puñjo: {heap, mass}
aṅga: {factor, a component, as in maggaṅga and bojjhaṅga (compound final): chi phần / bộ phận / phương diện; limbs of the body: bộ phận lớn}
rūpā: {visible forms, the objects of the eye (nominative pl.): hình sắc; bodily build: thân hình}
dhammo: {teaching, doctrine: Giáo Pháp / giáo pháp / giáo lý; sexual act: hành vi; inherent nature: bản chất}
dhamme: {the Buddha's teaching, in doubt about the Teacher and the Teaching (locative sg.): Giáo Pháp; state, in diṭṭheva dhamme 'here and now' (locative): đời}
sappi: {ghee, clarified butter, in sappikumbha 'a jar of ghee' (stem and nominative sg.)}
upādāya: {derived, dependent on the great elements (absolutive, as in upādārūpa): phái sinh; dependence, the name of the section on designation by dependence in the summary verse (absolutive): sự dựa vào}
madhu: {honey, in madhukumbha 'a jar of honey' (compound member)}
Cittena: {with a mind (instrumental sg.)}
nicca: {permanent, lasting, in niccabhatta and as predicate (stem and compound member): thường còn; ever-, always, of trees in niccapupphā and niccaphalikā (compound member): luôn}
niccaṃ: {lasting: thường còn; constantly, always, of the ever-flowering trees (adverb): luôn}
saṇṭhāti: {comes to stand, settles in a lower fruit, as in 'kattha saṇṭhāti' (3rd sg. verb): đứng vững; takes shape, forms, of the earth and of the sense bases in the womb (3rd sg. verb): hình thành}
phale: {fruit of the path, fruition, as in arahattaphale and sotāpattiphale (locative sg.)}
bojjhaṅga: {factor of awakening, as in bojjhaṅgabhāvanā (stem and compound member)}
padhāna: {endeavour, exertion, as in sammappadhāna (compound final)}
sīla: {rules or morality, ethical conduct, in sīlabbata 'rules and rituals' and as in sīlasaṃvara and sīlavisuddhi (compound member)}
uppāda: {arising, coming to be, as in uppādakkhaṇa and anuppādadhamma (compound member): nảy sinh / sinh khởi; shedding (of blood): làm chảy}
pādā: {bases, in iddhipādā (nominative pl., compound final): nền tảng; feet, as body parts formed in the womb (nominative pl.): bàn chân}
dhajo: {flag, banner, in pannaddhajo 'with the banner lowered' (nominative sg.)}
kata: {done, accomplished, in katakaraṇīyo 'one who has done what had to be done' (compound member)}
saṅkiṇṇa: {filled in (moat): đã lấp; mixed, adulterated: lẫn lộn}
ariyo: {a holy one (nominative sg.): bậc thánh; noble, of the path in 'ariyo aṭṭhaṅgiko maggo' (masculine nominative sg.): cao quý}
pāso: {snare, in oghapāso 'the snare of the flood' (compound final)}
ghano: {compact, solid: liền một khối; embryonic solid mass: khối cứng}
phassā: {contacts, the meetings of sense and object (nominative pl.): sự tiếp xúc; tangible objects, in the verse list of sense objects (nominative pl.): vật xúc chạm}
yogo: {yoke, binding to existence (nominative sg.): ách; application, effort: sự rèn luyện / sự tu tập}
moha: {delusion, as an unwholesome root and in mohasahagata (compound member)}
attha: {meaning, sense, as in atthamaññātuṃ 'to understand the meaning' (compound member)}
patta: {alms bowl, in pattacīvaradhāraṇa 'carrying bowl and robe' (compound member): bình bát; leaves, foliage (compound member): lá}
natthi: {there is not}
kāsāva: {ochre robe, in kāsāvadhāraṇā 'wearing the ochre robe' (compound member)}
cakkaṃ: {wheel, in dhammacakkaṃ 'the wheel of the Teaching' (accusative sg.)}
puna: {again, once more: lại / trở lại; renewed (re-birth): mới; furthermore (adverb): Lại nữa}
sacchikata: {directly experienced}
dukkho: {suffering, in apariññātadukkho 'one whose suffering is not fully understood' (compound final)}
dassanena: {by insight}
ekaṭṭhe: {co-existing with that: cùng hiện diện; identical in meaning: cùng một nghĩa}
phusitvā: {having personally experienced the liberations with the body (figurative, absolutive): chạm đến; having touched (absolutive): khi chạm}
diṭṭhī: {view, held opinion, in sakkāyadiṭṭhī (compound final)}
ariyena: {noble, of the path in 'ariyena aṭṭhaṅgikena maggena' (masculine instrumental sg.)}
jano: {an individual, people (nominative)}
avacarena: {belonging to a sphere, in rūpāvacarena (instrumental)}
cittānaṃ: {of minds, mental states}
jātiyā: {being born, the birth link (instrumental sg.): sự sinh; in that birth, within this life (instrumental): đời}
āma: {moral corruption: tanh hôi ô uế; raw flesh, in āmagandha 'smell of raw flesh' (compound member): tanh}
abhiññāya: {having directly known}
satāni: {hundreds (cardinal numeral, neuter pl.)}
Ariyassa: {noble, of noble virtue and concentration, as in 'ariyassa sīlassa' (masculine genitive sg.): cao quý; of the noble one, in 'ariyassa vinaye' 'in the discipline of the noble one' (genitive sg.): bậc thánh}
katvā: {on the ground that: vì cho rằng / khi coi; having performed: sau khi làm / sau khi}
Anāgataṃ rūpaṃ: {future matter: vật chất thuộc tương lai / vật chất … thuộc tương lai; future visible form, the object of the eye (phrase): hình sắc thuộc tương lai}
Atītaṃ rūpaṃ: {past matter: vật chất thuộc quá khứ / vật chất … thuộc quá khứ; past visible form, the object of the eye (phrase): hình sắc thuộc quá khứ}
Paccuppannaṃ rūpaṃ: {present matter: vật chất thuộc hiện tại / vật chất … thuộc hiện tại; present visible form, the object of the eye (phrase): hình sắc thuộc hiện tại}
rajjamānaṃ: {being dyed (cloth): khi đang được nhuộm; becoming lustful: đang tham đắm}
sukhadukkhaṃ: {pleasure and pain, pleasant and painful feeling (neuter sg. compound)}
kārako: {doer, the agent of a deed (nominative sg.)}
uppādo: {arising, coming into being (nominative sg.)}
samuppanno: {arisen, come into being (masculine nominative sg. participle)}
paṭiccasamuppanno: {dependently arisen, arisen through conditions (masculine nominative sg.)}
nirujjhamānaṃ: {ceasing, in the course of ceasing (present participle)}
sassatā: {eternal, everlasting (nominative pl.)}
arahattā: {from arahantship, the state of an arahant (ablative sg.)}
sata: {a hundred (numeral, compound member)}
sahassehi: {thousands, by the thousand (instrumental pl.)}
Sotāpattiphale: {in the fruit of stream-entry (locative sg.)}
Sotāpannassa: {of the stream-enterer (genitive sg.)}
vītadoso: {free from hatred, one whose hatred is gone (nominative sg.)}
pariññātaṃ: {fully understood (neuter sg. participle)}
sacchikato: {realized, directly experienced (masculine nominative sg. participle)}
visaññutto: {unfettered, released from bonds (nominative sg. participle)}
kilese jahati: {abandons the defilements (verb phrase)}
kilese: {defilements, the mental stains (accusative pl.)}
phusitvā viharati: {dwells having touched, abides having experienced with the body (verb phrase)}
Sakkāyadiṭṭhiṃ: {identity view, the view of a self in the aggregates (accusative sg.)}
Sakkāyadiṭṭhī: {identity view, the view of a self in the aggregates (nominative sg.)}
paṭiladdho: {obtained, acquired (nominative sg. participle)}
jahitā: {abandoned, given up (nominative pl. participle)}
abhabbo: {incapable, unable (nominative sg.)}
udapādi: {arose, came into being (aorist)}
vicikicchitaṃ: {doubt, wavering of mind (neuter sg.)}
Arahatte: {in arahantship, the state of an arahant (locative sg.)}
sotāpattiphalaṃ: {fruit of stream-entry, the first fruition (nominative/accusative sg.)}
ajātaṃ: {unborn, not yet come to be (neuter sg. participle)}
"""


def main():
    rows = stv.read_agg(p2v.AGG)
    idx = p2v.prior_idx()
    ov = {}
    for line in OVERRIDES.strip().splitlines():
        line = stv.nfc(line.strip())
        if line:
            hw = line.split(': {', 1)[0]
            if hw in ov:
                sys.exit(f'override twice: {hw}')
            if hw not in rows:
                sys.exit(f'override for headword not in agg-part2.tsv: {hw}')
            ov[hw] = line
    out = ['# pi-5 (Kathāvatthu) Pāli→Vietnamese senses, part 2 (agg-part2.tsv, 908 rows).',
           '# Tag table reviewed headword by headword (senses-conventions.md §2): the approved pi-4 … pi-1 Vietnamese',
           '# tag where pi-5 has the same headword, sense and Vietnamese value (example or label adapted where it does',
           '# not occur in pi-5), otherwise the approved pi-5 Russian tag word for word; new tags only where the',
           '# Vietnamese splits differently or the Russian tag is a bare English hint.',
           '# Build: python -I -X utf8 -B senses_tool_vi.py build --part 2']
    todo = []
    for hw, r in rows.items():
        if not r['vals']:
            continue
        if hw in ov:
            out.append(ov[hw])
            continue
        line, src = p2v.draft_line(hw, r, idx)
        if line is None:
            todo.append(hw)
            continue
        out.append(line)
    with open(p2v.DEC, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(out) + '\n')
    print(f'wrote {len(out) - 6} decision lines ({len(ov)} hand-written overrides); TODO: {todo}')


if __name__ == '__main__':
    main()
