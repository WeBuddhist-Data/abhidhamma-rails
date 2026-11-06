"""QA fixes for the pi-6 rails translation, from 0-INBOX/pi-6-english-plain-qa-report.md.

Run from AI_translation/. Applies to the split chapters and the merged file.
The scripts in this folder do not contain these fixes, so run this again after
regenerating any chapter. Nothing is written unless every rule hits its expected count.
"""
import glob
import re
import sys

SPLIT = 'english/pi-6-english-plain-rails_split_chapters/*.md'
MERGED = 'english/pi-6-english-plain.md'

TERMS = r'(wholesome|unwholesome|indeterminate)'


def art(word):
    return 'an ' + word if word[0] in 'aeiou' else 'a ' + word


# (name, regex, replacement, expected count, block-ID prefix or None for anywhere)
RULES = [
    # Major: one group in the Pāli was split into two in the English.
    ('final existence + women/men (list)', r'those in their final existence, those being reborn as (women|men), ',
     r'\1 in their final existence being reborn, ', 20, '6-10-'),
    ('final existence + women/men (alone)', r'those in their final existence and those being reborn as (women|men),',
     r'\1 in their final existence being reborn,', 16, '6-10-'),
    ('final existence + with a nose', r'those in their final existence and those being reborn with a nose,',
     'those in their final existence being reborn with a nose,', 1, '6-10-396'),
    ('Pure Abodes + being reborn', r'For those in the Pure Abodes, those being reborn and non-percipient beings,',
     'For those being reborn in the Pure Abodes and for non-percipient beings,', 1, '6-10-277'),
    ('nibbāna + being reborn', r'attain final nibbāna and those being reborn',
     'attain final nibbāna, when they are being reborn', 51, '6-10-'),
    ('nibbāna + passing away', r'attain final nibbāna and those passing away',
     'attain final nibbāna, when they are passing away', 52, '6-10-'),

    # Minor: wording that is hard for a plain reader.
    ('several existences (1)', r'(women|men) who, in this same state, will show several existences',
     r'\1 who, remaining \1, will pass through several more existences', 94, '6-10-'),
    ('several existences (2)',
     r'(women|men), in this same state, after showing several existences, who will be reborn with (joy|equanimity) and attain',
     r'\1 who, remaining \1, will pass through several more existences, be reborn with \2 and attain', 48, '6-10-'),
    ('not what is X', r'Is what is not what is ' + TERMS + r' not \1 phenomena\?',
     lambda m: f'Is what is not {m[1]} not {art(m[1])} phenomenon?', 18, '6-9-'),
    ('is what is X', r'Is what is ' + TERMS + r' \1 phenomena\?',
     lambda m: f'Is what is {m[1]} {art(m[1])} phenomenon?', 18, '6-9-'),
    ('is X phenomena', r'Is ' + TERMS + r' phenomena what is \1\?', r'Are \1 phenomena \1?', 6, '6-9-'),
    ('not X phenomena', r'Is what is not ' + TERMS + r' phenomena not what is \1\?',
     lambda m: f'Is what is not {art(m[1])} phenomenon not {m[1]}?', 6, '6-9-'),
    ('not a phenomenon', r'Is what is not a phenomenon not ' + TERMS + r' phenomena\?',
     lambda m: f'Is what is not a phenomenon not {art(m[1])} phenomenon?', 21, '6-9-'),
    ('not included', r'([Ii]n) what is not included,', r'\1 what is not included in the realms,', 311, '6-7-'),
    ('wherever', r'wherever – does', 'in a given place – does', 270, '6-7-'),
    ('neither nor rebirth', r'no such thing as rebirth in neither the', 'no rebirth in a realm that is neither the', 2, '6-7-'),
    ('it is a woman', r'but it is a (woman|man)\.', r'but is a \1.', 2, '6-10-95'),
    ('run-on group', r'For those in the Pure Abodes, while the second consciousness is occurring, for non-percipient beings,',
     'For those in the Pure Abodes while the second consciousness is occurring, and for non-percipient beings,', 29, None),

    # Minor: stray characters and punctuation.
    ('stray ". ;"', r'\. ;', ';', 1, '6-7-325'),
    ('missing )', r'\(Based on the wisdom faculty\.…', '(Based on the wisdom faculty.)…', 1, '6-10-434'),
    ('added ellipsis', r'does not cease… \(the section on place', 'does not cease (the section on place', 1, '6-2-130'),
    ('heading 14', r'\(14\) The Section on Time Having Passed', '(14) Time Having Passed', 1, '6-8-82'),

    # Minor: the same heading worded two ways.
    ('heading', r'^#### Having Underlying Tendencies', '#### The Section on Having Underlying Tendencies', 1, '6-7-5-0'),
    ('heading', r'^#### Abandoning', '#### The Section on Abandoning', 1, '6-7-7-0'),
    ('heading', r'^#### Full Understanding', '#### The Section on Full Understanding', 1, '6-7-9-0'),
    ('heading', r'^#### What Is Abandoned', '#### The Section on What Is Abandoned', 1, '6-7-11-0'),
]

# (block ID, start of the note, the words the note belongs after)
NOTES = [
    ('6-5-33', '[variant: taṇhāvippayuttamaggavippayuttacittassa', 'consciousness not associated with the path or with craving'),
    ('6-5-61', '[variant: uppatticittassa', 'the rebirth consciousness'),
    ('6-5-69', '[variant: paṭilabhissanti', 'for others who will attain the path'),
    ('6-7-270', '[variant: pahīno', 'sensual desire and aversion are abandoned'),
    ('6-10-441', '[variant: tayo puggalā', 'Those possessing the three paths'),
    ('6-10-441', '[variant: aṭṭhamakañca', 'Apart from those possessing the four paths'),
    ('6-10-465', '[variant: satta', 'Eight kinds of person'),
    ('6-10-466', '[variant: pañca', 'Six kinds of person'),
]


def block_id_of(lines, index):
    """The ID of the block a line belongs to: the next ^id at or after this line."""
    for line in lines[index:]:
        m = re.search(r'\s\^(\S+)\s*$', line)
        if m:
            return m[1]
        if not line.strip():
            return None
    return None


def in_scope(block, scope):
    if scope is None:
        return True
    if scope.endswith('-'):
        return bool(block) and block.startswith(scope)
    return block == scope


def move_notes(line, block):
    moved = 0
    for nid, start, anchor in NOTES:
        if nid != block:
            continue
        search_from = 0
        while True:
            at = line.find(' ' + start, search_from)
            if at < 0:
                break
            end = line.index(']', at) + 1
            before = line.rfind(anchor, 0, at)
            if before < 0:
                search_from = end
                continue
            insert = before + len(anchor)
            if insert == at:
                search_from = end
                continue
            note = line[at:end]
            line = line[:insert] + note + line[insert:at] + line[end:]
            moved += 1
            search_from = insert + len(note)
    return line, moved


def apply(path, tally):
    with open(path, encoding='utf-8') as fh:
        lines = fh.read().split('\n')
    out = []
    for i, line in enumerate(lines):
        block = block_id_of(lines, i)
        for k, (_, pattern, repl, _, scope) in enumerate(RULES):
            if in_scope(block, scope):
                line, n = re.subn(pattern, repl, line)
                tally[k] += n
        line, moved = move_notes(line, block)
        tally['notes'] = tally.get('notes', 0) + moved
        out.append(line)
    return path, '\n'.join(out)


def run(paths):
    tally = {k: 0 for k in range(len(RULES))}
    results = [apply(p, tally) for p in paths]
    ok = True
    for k, (name, _, _, want, _) in enumerate(RULES):
        if tally[k] != want:
            print(f'COUNT MISMATCH {name}: expected {want}, got {tally[k]}')
            ok = False
    if tally['notes'] != 9:
        print(f'COUNT MISMATCH notes: expected 9, got {tally["notes"]}')
        ok = False
    return ok, results, tally


def main():
    splits = sorted(glob.glob(SPLIT))
    ok_split, res_split, tally = run(splits)
    ok_merged, res_merged, _ = run([MERGED])
    if not (ok_split and ok_merged):
        print('Nothing written.')
        sys.exit(1)
    for path, text in res_split + res_merged:
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(text)
    print(f'Applied {sum(v for v in tally.values())} changes in {len(splits)} split files and the merged file.')


if __name__ == '__main__':
    main()
