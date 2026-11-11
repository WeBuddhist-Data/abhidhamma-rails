import pathlib
d = pathlib.Path(__file__).parent
ch = 'preamble'
M = {
 'T-1': {'awakened': 'sambuddhassa', 'awakened Buddha': 'sambuddhassa', 'Awakened Buddha': 'sambuddhassa',
         'blessed': 'bhagavato', 'buddha': 'sambuddhassa', 'fully': 'sammā',
         'Fully Awakened': 'sammāsambuddhassa', 'Fully Awakened Buddha': 'sammāsambuddhassa',
         'fully awakened Buddha': 'sammāsambuddhassa', 'homage': 'Namo', 'worthy': 'arahato'},
 '0': {'abhidhamma': 'Abhidhamma', 'Abhidhamma Piṭaka': 'Abhidhammapiṭake'},
 '2-0': {'analysis': 'Vibhaṅga', 'book': 'pāḷi', 'Book of Analysis': 'Vibhaṅgapāḷi'},
}
out = []
for line in (d / f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines():
    sid, kws = line.split('] ', 1)
    sid = sid[1:]
    m = M[sid]
    out.append(f'[{sid}] ' + ', '.join(f'{m[k.strip()]}={k.strip()}' for k in kws.split(', ')))
(d / f'{ch}.mapped.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
print('written', len(out))
