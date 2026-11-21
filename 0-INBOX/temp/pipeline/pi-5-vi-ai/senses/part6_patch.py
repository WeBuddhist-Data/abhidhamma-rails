"""Part 6: replace decision lines of decisions-part6.txt by headword with the hand-written lines below (LF, UTF-8).
  python -I -X utf8 -B part6_patch.py
"""
import os
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
DEC = os.path.join(HERE, 'decisions-part6.txt')

LINES = r"""
vihāro: {living, abiding, in diṭṭhadhammasukhavihāro (nominative sg.)}
karaṇīyo: {deserving, in añjalikaraṇīyo: xứng đáng được … cung kính; fitting to be given, of instruction: điều nên làm}
samāhito: {composed (nominative)}
rāja: {king, chief of its kind, in sālarājamūle 'at the foot of the king of sal trees' (compound member)}
kāraṇikā: {those who inflict torture: người thi hành hình phạt; trainers of animals, listed with the elephant- and horse-keepers among the gods (nominative pl.): người huấn luyện}
hananti: {smite, of one's own deeds: đánh đập; slay, kill: sát hại}
mito: {measured out, in 'vibhatto bhāgaso mito' of the great hell's layout (masculine nominative sg. participle)}
majjhe: {in the midst of, in majjheurasmiṃ 'in the middle of the chest' (locative sg.)}
buddhānaṃ: {the Awakened Ones (genitive pl.)}
buddhā: {buddhas, the awakened ones (nominative pl.)}
dhammā niyatā: {phenomena fixed in their result, in the thesis 'sabbe dhammā niyatā' (nominative pl.)}
seyyāya: {lying, in gabbhaseyyāya 'while lying in the womb' (compound final, locative sg.)}
bhūtassa: {having become, in manussabhūtassa 'for one reborn as a human' (compound final, genitive sg.)}
"""


def main():
    new = {}
    for line in LINES.strip().split('\n'):
        line = unicodedata.normalize('NFC', line.strip())
        if line:
            new[line.split(': {', 1)[0]] = line
    with open(DEC, encoding='utf-8') as f:
        old = f.read().split('\n')
    out, done = [], set()
    for line in old:
        s = unicodedata.normalize('NFC', line)
        key = s[6:].strip() if s.startswith('#TODO ') else s.split(': {', 1)[0]
        if key in new and not (s.startswith('#') and not s.startswith('#TODO ')):
            out.append(new[key])
            done.add(key)
        else:
            out.append(s)
    left = [k for k in new if k not in done]
    if left:
        sys.exit(f'not found in decisions: {left}')
    with open(DEC, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(out))
    print(f'patched {len(done)} lines')


if __name__ == '__main__':
    main()
