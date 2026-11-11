import pathlib, re, sys
root = pathlib.Path(__file__).resolve().parents[5]
d = pathlib.Path(__file__).parent
pali_dir = root / 'AI_translation' / 'pali' / 'pi-2_split_chapters'
NDE = '(no direct equivalent)'

for ch in sys.argv[1:]:
    segs, buf = {}, []
    for line in (pali_dir / f'{ch}.md').read_text(encoding='utf-8').splitlines():
        buf.append(line)
        m = re.search(r'\^([\w-]+)\s*$', line)
        if m:
            segs[m.group(1)] = '\n'.join(buf); buf = []
    absent, partial, nde = [], [], 0
    for line in (d / f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines():
        sid, rest = line.split('] ', 1)
        sid = sid[1:]
        text = segs[sid]
        words = set(re.findall(r'[^\W\d_]+', text))
        for pair in rest.split(', '):
            val, kw = pair.rsplit('=', 1)
            if val == NDE:
                nde += 1; continue
            for part in val.split(' / '):
                if part not in text:
                    absent.append((sid, part, kw))
                elif not all(w in words for w in part.split(' ')):
                    partial.append((sid, part, kw))
    print(ch, 'NDE', nde, 'absent', absent)
    print(ch, 'cut-compound values (substring only, not whole word):', sorted(set((p, k) for _, p, k in partial)))
