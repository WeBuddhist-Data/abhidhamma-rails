"""Write the LUMP_OK blocks (sample, full) for the REVIEW headwords left after the MANUAL pass, each with its pi-7 values
and the reason it is one sense (checked by hand against rv-review.txt / rv-compact.txt, ids.py and kw.py).
usage: mklump.py <gen-out.txt> <sample-out.txt> <full-out.txt>"""
import re, sys
SAMPLE = {l.split('\t')[0] for l in open('agg-sample.tsv', encoding='utf-8') if l.strip()}
C = {
 'cond': ('the condition by its frame: ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း», the bare name, negatives '
          '(map-table T1-T4; kept: grammar)',
          'vigatapaccayā Naanantara Napacchājāta Nissaya Upanissaya purejātapaccayā upanissayapaccayā hetupaccayā '
          'ārammaṇapaccayā adhipatipaccayā anantarapaccayā samanantarapaccayā sahajātapaccayā āsevanapaccayā '
          'kammapaccayā natthipaccayā avigatapaccayā naadhipatipaccayā Naadhipati naārammaṇapaccayā Pacchājāta '
          'naindriya namagga'),
 'gap': ('one value with or without the « … » gap at the «လည်း» of ca / ceva (R7 / rule 10; kept: construction)',
         'sahetuko sahetukassa sahetukañca Āsavasampayuttaṃ Āsavasampayutto sāsavañca sāsavo saññojaniyo '
         'saññojanasampayutto saññojaniyañca ganthasampayutto ganthaniyo nīvaraṇiyo nīvaraṇasampayutto nīvaraṇiyañca '
         'nīvaraṇasampayuttañca parāmaṭṭho Saṃkiliṭṭhañca saṃkiliṭṭho saṃkilesiko kilesasampayutto '
         'pahātabbahetukādhipati'),
 'sadisa': ('the -sadisa note in each segment\'s form «…နှင့် တူသည် / တူအောင်» (coordinator; kept: text shape)',
            'paṭiccavārasadisā paṭiccavārasadiso paṭiccavārasadisaṃ dutiyagamanasadisaṃ sappītikadukasadisaṃ '
            'arūpadukasadisā Cittadukakusalasadisaṃ Lokiyadukaabyākatasadisaṃ'),
 'text': ('two text forms of one meaning (map-harmonise §A; kept: text)',
          'suciṇṇāni tadārammaṇatā ṭhānāṭhānakosallassa pavattipaṭisandhi saññojanādidukāni vibhajantena'),
 'act': ('the act compound: the whole act, the noun, or the bare noun before …pe… (U2; kept: construction)',
         'uposathakammaṃ ekāgārikaṃ gāmaghātaṃ'),
 'gram': ('grammatical forms of one lemma, one meaning (kept: grammar / construction)',
          'assādeti Paripuṇṇaṃ nevavipākanavipākadhammadhammo vipāko vipākassa'),
 'later': ('the pi-7 value is a later binding file\'s value under the same or its own binding tag',
           'paccayo rūpaṃ kammaṃ vipākā Saṃkhittaṃ kusalassa sutaṃ attānaṃ āhārā āhāraṃ kāyikaṃ dukkhaṃ dukkhassa '
           'avasesā Dassanena sekkho asekkho sukhassa uppannassa Ajjhattaṃ arūpaṃ Ajjhattikaṃ Upādā Kāmāvacaraṃ '
           'Rūpāvacaraṃ Arūpāvacaraṃ arūpāvacare Saraṇaṃ hīno'),
 'num': ('the count with the text\'s classifier «ခု» (T6), the same number as the binding «ပါး»',
         'sattarasa terasa pannarasa ekādasa dvādasa soḷasa cuddasa tevīsa tiṃsa chattiṃsa aṭṭhārasa ekūnavīsati'),
 'word': ('the pi-7 text\'s own word for the binding meaning (map-table «Values different from pi-1 … pi-6»; the '
          'binding value is not in the segment)',
          'saṃsaṭṭha samanantarā kusalākusalaṃ uppajjeyya uppajjeyyuṃ kiriyābyākataṃ vipākābyākate kiriyābyākate '
          'pañhā sahajāto datvā paccavekkhati vipassati vuṭṭhahantassa deti uppādenti bhaṇati harati Cakkaṃ Bhojanaṃ '
          'patthanā passitvā Gaṇanāya aññamaññapaccaya micchattaniyato sammattaniyato voropeti paro asaññasattā rūpī '
          'arūpī ajjhattikassa bāhirassa anuttaro vattabbaṃ mūlakaṃ nānākaraṇaṃ'),
}
cat = {}
for k, (_, hs) in C.items():
    for h in hs.split():
        assert h not in cat, h
        cat[h] = k
rev = []
on = False
for l in open(sys.argv[1], encoding='utf-8'):
    if l.startswith(('REVIEW', 'UNRESOLVED', 'ERRORS', 'note', 'wrote')):
        on = l.startswith('REVIEW'); continue
    if on and l.startswith('  '):
        hw = l[2:].split(' [')[0]
        vals = l.rstrip('\n').split(']: ', 1)[1]
        rev.append((hw, vals))
miss = [h for h, _ in rev if h not in cat]
extra = [h for h in cat if h not in {h for h, _ in rev}]
assert not miss and not extra, (miss, extra)
outs = {True: [], False: []}
for hw, vals in rev:
    vs = ' / '.join(f'«{v}»' for v in vals.split(' / '))
    outs[hw in SAMPLE].append(f'    {hw!r},  # {vs}: {C[cat[hw]][0]}')
open(sys.argv[2], 'w', encoding='utf-8').write('\n'.join(outs[True]) + '\n')
open(sys.argv[3], 'w', encoding='utf-8').write('\n'.join(outs[False]) + '\n')
print(len(outs[True]), len(outs[False]))
