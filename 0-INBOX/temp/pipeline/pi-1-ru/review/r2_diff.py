import sys, re, difflib
base = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
files = sys.argv[1].split(',')
lo = sys.argv[2] if len(sys.argv) > 2 else None   # first ID to print
hi = sys.argv[3] if len(sys.argv) > 3 else None   # last ID to print
thr = float(sys.argv[4]) if len(sys.argv) > 4 else 0.75

def load(path):
    return open(path, encoding='utf-8').read().split('\n')

segs = []
for f in files:
    P = load(base + r'\pali\pi-1_split_chapters\\' + f)
    R = load(base + r'\russian\pi-1-russian-plain-rails_split_chapters\\' + f)
    assert len(P) == len(R), f
    curP, curR = [], []
    for p, r in zip(P, R):
        if not p.strip():
            if r.strip():
                print('ALIGN WARN', f, r[:80])
            continue
        curP.append(p); curR.append(r)
        m = re.search(r'\^([\w-]+)\s*$', p)
        if m:
            mr = re.search(r'\^([\w-]+)\s*$', r)
            if not mr or mr.group(1) != m.group(1):
                print('ID MISMATCH', m.group(1), r[-30:])
            segs.append((m.group(1), f, ' / '.join(curP), ' / '.join(curR)))
            curP, curR = [], []

def tok(s):
    s = re.sub(r'\^[\w-]+\s*$', '', s)
    return re.findall(r'\w+|[^\w\s]', s)

printing = lo is None
seen = []
for sid, f, p, r in segs:
    if sid == lo:
        printing = True
    tp, tr = tok(p), tok(r)
    best, bi = 0, -1
    for i, (sp, sr, _) in enumerate(seen):
        sm = difflib.SequenceMatcher(None, sp, tp, autojunk=False)
        if sm.real_quick_ratio() < best or sm.quick_ratio() < best:
            continue
        q = sm.ratio()
        if q > best:
            best, bi = q, i
    if printing:
        if best >= thr:
            sp, sr, sid0 = seen[bi]
            print(f'=== {sid} ({f}) ~ {sid0} ratio {best:.2f}')
            for tag, a1, a2, b1, b2 in difflib.SequenceMatcher(None, sp, tp, autojunk=False).get_opcodes():
                if tag != 'equal':
                    print(f'  P {tag}: {" ".join(sp[a1:a2])!r} -> {" ".join(tp[b1:b2])!r}')
            for tag, a1, a2, b1, b2 in difflib.SequenceMatcher(None, sr, tr, autojunk=False).get_opcodes():
                if tag != 'equal':
                    print(f'  R {tag}: {" ".join(sr[a1:a2])!r} -> {" ".join(tr[b1:b2])!r}')
        else:
            print(f'=== {sid} ({f}) NEW (best {best:.2f})')
            print('  P:', p)
            print('  R:', r)
    seen.append((tp, tr, sid))
    if sid == hi:
        printing = False
